"""Production WSGI bridge: reuse the tested API and use Waitress for HTTP."""

from email.message import Message
from http import HTTPStatus
import io
import os
import secrets
import threading
from types import SimpleNamespace

import server


def initialize():
    # Production must never silently create publicly known demo credentials.
    os.environ.setdefault("ATIGRA_DEMO", "0")
    server.seed()
    with server.connect() as db:
        if not db.execute("SELECT 1 FROM users LIMIT 1").fetchone():
            username = os.environ.get("ATIGRA_ADMIN_USERNAME", "comandante")
            password = os.environ.get("ATIGRA_ADMIN_PASSWORD")
            if not password:
                raise RuntimeError(
                    "Set ATIGRA_ADMIN_PASSWORD securely in hosting settings before first startup."
                )
            if not 3 <= len(username) <= 60 or not all(
                c.isalnum() or c in "._-" for c in username
            ):
                raise RuntimeError(
                    "ATIGRA_ADMIN_USERNAME must contain 3–60 letters, digits, dots, underscores or hyphens."
                )
            db.execute(
                "INSERT INTO users(username,alias,role,password,created_at) VALUES(?,?,'teacher',?,?)",
                (username, "Comandante", server.password_hash(password), server.now()),
            )


class WSGIHandler(server.Handler):
    def __init__(self, environ, runtime):
        self.command = environ.get("REQUEST_METHOD", "GET")
        self.path = environ.get("PATH_INFO", "/")
        if environ.get("QUERY_STRING"):
            self.path += "?" + environ["QUERY_STRING"]
        self.headers = Message()
        for name, value in environ.items():
            if name.startswith("HTTP_"):
                self.headers[name[5:].replace("_", "-")] = value
        for key, header in [
            ("CONTENT_LENGTH", "Content-Length"),
            ("CONTENT_TYPE", "Content-Type"),
        ]:
            if environ.get(key):
                self.headers[header] = environ[key]
        if not self.headers.get("Host"):
            self.headers["Host"] = environ.get("SERVER_NAME", "localhost")
        self.rfile = environ["wsgi.input"]
        self.wfile = io.BytesIO()
        self.client_address = (environ.get("REMOTE_ADDR", "unknown"), 0)
        self.server = runtime
        self.response_headers = []
        self.status = 500

    def send_response(self, code, message=None):
        self.status = code

    def send_header(self, name, value):
        self.response_headers.append((name, str(value)))

    def end_headers(self):
        pass


def create_app():
    initialize()
    runtime = SimpleNamespace(
        failures={},
        rate_lock=threading.Lock(),
        dummy_password=server.password_hash(secrets.token_urlsafe(20)),
    )

    def application(environ, start_response):
        request = WSGIHandler(environ, runtime)
        # Read-only health checks (Render uses GET). Unsupported methods never mutate.
        if request.command not in ("GET", "POST"):
            request.send(
                {"error": "method_not_allowed"},
                status=405,
                headers={"Allow": "GET, POST"},
            )
        else:
            request.dispatch()
        start_response(
            f"{request.status} {HTTPStatus(request.status).phrase}",
            request.response_headers,
        )
        return [request.wfile.getvalue()]

    return application


if __name__ == "__main__":
    from waitress import serve

    serve(
        create_app(),
        host=os.environ.get("ATIGRA_HOST", "0.0.0.0"),
        port=int(os.environ.get("PORT", os.environ.get("ATIGRA_PORT", "8000"))),
        threads=4,
        max_request_body_size=2000000,
        channel_timeout=30,
    )
