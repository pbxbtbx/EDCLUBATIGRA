"""Production bridge tests, using standard-library WSGI HTTP transport."""

import json
import os
from pathlib import Path
import secrets
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch
import urllib.error
import urllib.request
from wsgiref.simple_server import make_server

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import server
import wsgi
from test_app import Client


class ProductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.old = server.DB_PATH
        server.DB_PATH = cls.temp.name + "/demo.sqlite3"
        with patch.dict(os.environ, {"ATIGRA_DEMO": "1", "ATIGRA_SECURE_COOKIE": "0"}):
            cls.app = wsgi.create_app()
        cls.http = make_server("127.0.0.1", 0, cls.app)
        cls.thread = threading.Thread(target=cls.http.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = "http://127.0.0.1:" + str(cls.http.server_port)

    @classmethod
    def tearDownClass(cls):
        cls.http.shutdown()
        cls.http.server_close()
        cls.thread.join()
        server.DB_PATH = cls.old
        cls.temp.cleanup()

    def test_student_and_teacher_sessions(self):
        pupil = Client(self.base)
        pupil.login()
        teacher = Client(self.base)
        teacher.login("profe.demo")
        self.assertEqual(pupil.request("/api/student")[0], 200)
        self.assertEqual(teacher.request("/api/teacher")[0], 200)
        self.assertEqual(pupil.request("/api/teacher")[0], 404)
        self.assertEqual(pupil.request("/api/class", {"name": "denied"})[0], 404)
        self.assertEqual(
            teacher.request("/api/class", {"name": "Online class"})[0], 200
        )
        self.assertEqual(
            teacher.request("/api/class", {"name": "no csrf"}, csrf=False)[0], 403
        )

    def test_assets_security_headers_and_method(self):
        with urllib.request.urlopen(self.base + "/") as response:
            self.assertIn(b"ATIBOT", response.read())
            self.assertEqual(response.headers["X-Content-Type-Options"], "nosniff")
            self.assertIn(
                "frame-ancestors 'none'", response.headers["Content-Security-Policy"]
            )
        for method in ("DELETE", "PUT", "HEAD"):
            request = urllib.request.Request(self.base + "/api/class", method=method)
            with self.assertRaises(urllib.error.HTTPError) as error:
                urllib.request.urlopen(request)
            self.assertEqual(error.exception.code, 405)
        self.assertEqual(Client(self.base).request("/api/me")[0], 401)

    def test_origin_rejection(self):
        client = Client(self.base)
        client.login("profe.demo")
        request = urllib.request.Request(
            self.base + "/api/class",
            data=json.dumps({"name": "Cross origin"}).encode(),
            headers={
                "Origin": "https://other.example",
                "Content-Type": "application/json",
                "X-CSRF-Token": client.csrf,
            },
        )
        with self.assertRaises(urllib.error.HTTPError) as error:
            client.opener.open(request)
        self.assertEqual(error.exception.code, 403)

    def test_clean_hosting_admin_and_restart(self):
        old = server.DB_PATH
        try:
            server.DB_PATH = self.temp.name + "/online.sqlite3"
            password = secrets.token_urlsafe(24)
            with patch.dict(
                os.environ,
                {
                    "ATIGRA_DEMO": "0",
                    "ATIGRA_ADMIN_USERNAME": "commander",
                    "ATIGRA_ADMIN_PASSWORD": password,
                },
            ):
                wsgi.initialize()
                with server.connect() as db:
                    user = db.execute("SELECT * FROM users").fetchone()
                    self.assertEqual(user["username"], "commander")
                    self.assertTrue(server.password_ok(password, user["password"]))
                    self.assertEqual(
                        db.execute("SELECT COUNT(*) FROM users").fetchone()[0], 1
                    )
                    self.assertEqual(
                        db.execute("SELECT COUNT(*) FROM levels").fetchone()[0], 96
                    )
                # Redeploy cannot overwrite existing accounts or require the bootstrap password again.
                with patch.dict(os.environ, {"ATIGRA_ADMIN_PASSWORD": ""}):
                    wsgi.initialize()
                with server.connect() as db:
                    self.assertEqual(
                        db.execute("SELECT COUNT(*) FROM users").fetchone()[0], 1
                    )
                    self.assertTrue(
                        server.password_ok(
                            password,
                            db.execute("SELECT password FROM users").fetchone()[0],
                        )
                    )
        finally:
            server.DB_PATH = old

    def test_bootstrap_requires_private_password(self):
        old = server.DB_PATH
        try:
            server.DB_PATH = self.temp.name + "/missing-password.sqlite3"
            with patch.dict(
                os.environ, {"ATIGRA_DEMO": "0", "ATIGRA_ADMIN_PASSWORD": ""}
            ):
                with self.assertRaisesRegex(RuntimeError, "ATIGRA_ADMIN_PASSWORD"):
                    wsgi.initialize()
        finally:
            server.DB_PATH = old


if __name__ == "__main__":
    unittest.main()
