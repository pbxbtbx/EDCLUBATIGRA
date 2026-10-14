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


if __name__ == "__main__":
    unittest.main()
