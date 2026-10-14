import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
import unittest
import urllib.request
import json

ROOT = Path(__file__).resolve().parents[1]


class LauncherTests(unittest.TestCase):
    def test_local_start_reuse_and_persistence(self):
        with tempfile.TemporaryDirectory() as temp:
            with socket.socket() as sock:
                sock.bind(("127.0.0.1", 0))
                port = sock.getsockname()[1]
            env = {
                **os.environ,
                "ATIGRA_DB": temp + "/local.sqlite3",
                "ATIGRA_DEMO": "1",
            }
            command = [
                sys.executable,
                str(ROOT / "iniciar.py"),
                "--no-browser",
                "--port",
                str(port),
            ]
            with open(temp + "/server.log", "w") as log:
                process = subprocess.Popen(
                    command, cwd=temp, env=env, stdout=log, stderr=log
                )
                try:
                    for _ in range(80):
                        try:
                            with urllib.request.urlopen(
                                f"http://127.0.0.1:{port}/api/config", timeout=0.2
                            ) as response:
                                self.assertTrue(json.loads(response.read())["demo"])
                            break
                        except OSError:
                            if process.poll() is not None:
                                self.fail("Launcher stopped before readiness")
                            time.sleep(0.1)
                    else:
                        self.fail("Launcher readiness timeout")
                    result = subprocess.run(
                        command,
                        cwd=temp,
                        env=env,
                        capture_output=True,
                        text=True,
                        timeout=5,
                    )
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertIn("ya esta funcionando", result.stdout)
                    self.assertTrue(Path(env["ATIGRA_DB"]).is_file())
                finally:
                    process.terminate()
                    process.wait(timeout=5)

    def test_stale_server_uses_new_port_without_stopping_old_one(self):
        from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
        import threading

        class Legacy(BaseHTTPRequestHandler):
            def do_GET(self):
                body = b'{"demo": true}'
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, *args):
                pass

        legacy = ThreadingHTTPServer(("127.0.0.1", 0), Legacy)
        thread = threading.Thread(target=legacy.serve_forever, daemon=True)
        thread.start()
        with tempfile.TemporaryDirectory() as temp:
            env = {**os.environ, "ATIGRA_DB": temp + "/new.sqlite3", "ATIGRA_DEMO": "1"}
            with open(temp + "/launch.log", "w") as log:
                process = subprocess.Popen(
                    [
                        sys.executable,
                        str(ROOT / "iniciar.py"),
                        "--no-browser",
                        "--port",
                        str(legacy.server_port),
                    ],
                    cwd=temp,
                    env=env,
                    stdout=log,
                    stderr=log,
                )
                try:
                    import re

                    new_port = None
                    for _ in range(100):
                        text = Path(temp + "/launch.log").read_text()
                        found = re.search(
                            r"ATIBOT listo en tu ordenador: http://127\.0\.0\.1:(\d+)",
                            text,
                        )
                        if found:
                            new_port = int(found[1])
                            break
                        if process.poll() is not None:
                            self.fail(text)
                        time.sleep(0.1)
                    self.assertIsNotNone(new_port)
                    self.assertNotEqual(new_port, legacy.server_port)
                    with urllib.request.urlopen(
                        f"http://127.0.0.1:{new_port}/api/config", timeout=3
                    ) as response:
                        self.assertIn("build", json.loads(response.read()))
                    with urllib.request.urlopen(
                        f"http://127.0.0.1:{legacy.server_port}/api/config", timeout=3
                    ) as response:
                        self.assertEqual(json.loads(response.read()), {"demo": True})
                finally:
                    process.terminate()
                    process.wait(timeout=5)
                    legacy.shutdown()
                    legacy.server_close()
                    thread.join()


if __name__ == "__main__":
    unittest.main()
