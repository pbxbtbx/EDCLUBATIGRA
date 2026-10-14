"""Local administrator operations. Passwords are read without echoing."""

import argparse
import getpass
import server

parser = argparse.ArgumentParser(description="Manage ATIBOT teacher accounts locally")
parser.add_argument(
    "action", choices=["create-teacher", "reset-password", "init-clean"]
)
parser.add_argument("--username")
parser.add_argument("--alias")
args = parser.parse_args()
if args.action == "init-clean":
    server.seed(demo=False)
    print("Schema and 36 levels initialized. Existing databases are preserved.")
else:
    server.seed()
    if not args.username:
        parser.error("--username is required")
    password = getpass.getpass("New password (8–200 characters): ")
    if password != getpass.getpass("Confirm password: "):
        raise SystemExit("Passwords differ")
    encoded = server.password_hash(password)
    with server.connect() as db:
        if args.action == "create-teacher":
            if not 3 <= len(args.username) <= 60 or not all(
                c.isalnum() or c in "._-" for c in args.username
            ):
                raise SystemExit("Invalid username")
            db.execute(
                "INSERT INTO users(username,alias,role,password,created_at) VALUES(?,?,'teacher',?,?)",
                (args.username, args.alias or args.username, encoded, server.now()),
            )
        else:
            user = db.execute(
                "SELECT id FROM users WHERE username=?", (args.username,)
            ).fetchone()
            if not user:
                raise SystemExit("Unknown username")
            db.execute("UPDATE users SET password=? WHERE id=?", (encoded, user["id"]))
            db.execute("DELETE FROM sessions WHERE user_id=?", (user["id"],))
            db.execute("UPDATE runs SET consumed=1 WHERE student_id=?", (user["id"],))
    print("Account updated. No password was stored in plaintext.")
