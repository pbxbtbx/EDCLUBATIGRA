import http.cookiejar
import json
import os
import tempfile
import threading
import time
import unittest
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import server


class Client:
    def __init__(self, base):
        self.base = base
        self.csrf = ""
        self.cookies = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(self.cookies)
        )

    def request(self, path, data=None, csrf=True):
        headers = {"Content-Type": "application/json"}
        if csrf:
            headers["X-CSRF-Token"] = self.csrf
        req = urllib.request.Request(
            self.base + path,
            data=json.dumps(data).encode() if data is not None else None,
            headers=headers,
        )
        try:
            with self.opener.open(req) as r:
                body = r.read()
                return r.status, (
                    json.loads(body)
                    if r.headers["Content-Type"].startswith("application/json")
                    else body
                )
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read())

    def login(self, user="nova.demo"):
        status, result = self.request(
            "/api/login", {"login": user, "password": "AtigraDemo2026!"}
        )
        assert status == 200, (status, result)
        self.csrf = result["csrf"]
        return result


class ScoreTests(unittest.TestCase):
    def test_grade_thresholds_and_caps(self):
        for score, bots in [
            (49, 1),
            (50, 2),
            (65, 3),
            (80, 4),
            (95, 4),
            (97, 5),
            (100, 5),
        ]:
            # Equal accuracy/speed scores, except five requires full target.
            wpm = 20 if score >= 97 else score / 100 * 20
            rules = {**server.DEFAULT_RULES, "cap2_accuracy": 0, "cap3_accuracy": 0}
            _, actual = server.grade(score, wpm, 20, rules)
            self.assertEqual(actual, bots)
        self.assertEqual(server.grade(79, 50, 10, server.DEFAULT_RULES)[1], 2)
        self.assertEqual(server.grade(89, 50, 10, server.DEFAULT_RULES)[1], 3)
        self.assertEqual(server.grade(96.9, 50, 10, server.DEFAULT_RULES)[1], 4)
        self.assertEqual(server.grade(100, 19, 20, server.DEFAULT_RULES)[1], 4)
        self.assertAlmostEqual(server.grade(90, 10, 20, server.DEFAULT_RULES)[0], 80)

    def test_corrected_mistakes_and_composed_characters(self):
        events = [
            {"kind": "char", "char": "x", "t": 0},
            {"kind": "backspace", "t": 10},
            {"kind": "char", "char": "n\u0303", "t": 20},
            {"kind": "char", "char": "a\u0301", "t": 30},
        ]
        result = server.replay("ñá", events, 6000)
        self.assertTrue(result["completed"])
        self.assertAlmostEqual(result["accuracy"], 200 / 3)
        self.assertEqual(result["errors"], {"ñ": 1})
        self.assertEqual(result["typed"], 3)
        self.assertEqual(result["wpm"], 4)

    def test_incomplete_has_no_net_speed(self):
        r = server.replay("ab", [{"kind": "char", "char": "a", "t": 0}], 1000)
        self.assertFalse(r["completed"])
        self.assertEqual(r["wpm"], 0)

    def test_reject_invalid_events(self):
        for events in [
            [{"kind": "char", "char": "pasted", "t": 0}],
            [{"kind": "char", "char": "a", "t": -1}],
            [{"kind": "char", "char": "a", "t": 2000}],
            [{"kind": "char", "char": "a", "t": 10}, {"kind": "backspace", "t": 2}],
        ]:
            with self.assertRaises(server.Problem):
                server.replay("a", events, 1000)

    def test_madrid_week_and_dst(self):
        cases = [
            ("2026-10-11T21:59:59+00:00", "2026-10-05"),
            ("2026-10-11T22:00:00+00:00", "2026-10-12"),
            ("2026-10-25T22:59:59+00:00", "2026-10-19"),
            ("2026-10-25T23:00:00+00:00", "2026-10-26"),
            ("2026-03-29T21:59:59+00:00", "2026-03-23"),
            ("2026-03-29T22:00:00+00:00", "2026-03-30"),
        ]
        for value, expected in cases:
            self.assertEqual(server.week_key(datetime.fromisoformat(value)), expected)

    def test_password_hash(self):
        encoded = server.password_hash("strong-pass")
        self.assertNotIn("strong-pass", encoded)
        self.assertTrue(server.password_ok("strong-pass", encoded))
        self.assertFalse(server.password_ok("wrong", encoded))

    def test_clean_initialization_is_repeatable(self):
        old = server.DB_PATH
        try:
            temp = tempfile.TemporaryDirectory()
            server.DB_PATH = temp.name + "/clean.sqlite3"
            server.seed(demo=False)
            server.seed(demo=False)
            with server.connect() as db:
                self.assertEqual(
                    db.execute("SELECT COUNT(*) FROM users").fetchone()[0], 0
                )
                self.assertEqual(
                    db.execute("SELECT COUNT(*) FROM levels").fetchone()[0], 36
                )
        finally:
            server.DB_PATH = old
            temp.cleanup()


class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.old = server.DB_PATH
        server.DB_PATH = cls.temp.name + "/test.sqlite3"
        server.seed()
        cls.http = server.make_server(port=0)
        cls.thread = threading.Thread(target=cls.http.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = "http://127.0.0.1:" + str(cls.http.server_port)
        with server.connect() as db:
            cls.other = db.execute(
                "INSERT INTO users(username,alias,role,password,created_at) VALUES(?,?,'teacher',?,?)",
                (
                    "other",
                    "Other",
                    server.password_hash("AtigraDemo2026!"),
                    server.now(),
                ),
            ).lastrowid
            cls.foreign_class = db.execute(
                "INSERT INTO classes(teacher_id,name,rules) VALUES(?,?,?)",
                (cls.other, "Other class", json.dumps(server.DEFAULT_RULES)),
            ).lastrowid

    @classmethod
    def tearDownClass(cls):
        cls.http.shutdown()
        cls.http.server_close()
        cls.thread.join()
        server.DB_PATH = cls.old
        cls.temp.cleanup()

    def setUp(self):
        self.student = Client(self.base)
        self.student.login()
        self.teacher = Client(self.base)
        self.teacher.login("profe.demo")
        self.other_client = Client(self.base)
        self.other_client.login("other")

    def complete(self, client, lid=1, seconds=12, events=None):
        status, r = client.request("/api/run", {"level_id": lid})
        self.assertEqual(status, 200, r)
        with server.connect() as db:
            db.execute(
                "UPDATE runs SET started=started-? WHERE id=?", (seconds, r["run_id"])
            )
        chars = r["level"]["text"]
        events = events or [
            {"kind": "char", "char": ch, "t": i * 100} for i, ch in enumerate(chars)
        ]
        return client.request(
            "/api/attempt",
            {"run_id": r["run_id"], "events": events, "active_ms": seconds * 1000},
        )

    def test_seed_and_roles(self):
        status, report = self.teacher.request("/api/teacher")
        self.assertEqual(status, 200)
        self.assertEqual(
            len([l for l in report["levels"] if l["owner_id"] is None]), 36
        )
        self.assertEqual(len(set(l["mode"] for l in report["levels"])), 6)
        self.assertEqual(self.student.request("/api/teacher")[0], 404)
        self.assertEqual(self.student.request("/api/reports")[0], 404)
        self.assertEqual(self.teacher.request("/api/student")[0], 404)
        self.assertEqual(
            len(self.other_client.request("/api/teacher")[1]["students"]), 0
        )

    def test_csrf_and_ownership(self):
        self.assertEqual(
            self.teacher.request("/api/class", {"name": "Test"}, csrf=False)[0], 403
        )
        self.assertEqual(
            self.teacher.request(
                "/api/class", {"id": self.foreign_class, "name": "stolen"}
            )[0],
            403,
        )
        self.assertEqual(
            self.other_client.request(
                "/api/password", {"student_id": 2, "password": "new-secret"}
            )[0],
            403,
        )
        self.assertEqual(
            self.other_client.request(
                "/api/enrollment", {"student_id": 2, "class_id": self.foreign_class}
            )[0],
            403,
        )
        self.assertEqual(
            self.other_client.request(
                "/api/assignment", {"student_id": 2, "level_id": 1}
            )[0],
            403,
        )
        self.assertEqual(self.other_client.request("/api/ranking?class_id=1")[0], 403)
        self.assertEqual(self.other_client.request("/api/reports?student_id=2")[1], [])

    def test_persistence_unlock_and_no_client_score(self):
        status, result = self.complete(self.student)
        self.assertEqual(status, 200, result)
        self.assertEqual(result["attempt"]["bots"], 5)
        self.assertEqual(result["attempt"]["score"], 100)
        self.student.request("/api/logout", {})
        self.student.login()
        levels = self.student.request("/api/student")[1]["levels"]
        self.assertIsNotNone(levels[0]["best"])
        self.assertTrue(levels[1]["unlocked"])

    def test_individual_assignment_removal_preserves_history(self):
        status, result = self.complete(self.student)
        self.assertEqual(status, 200)
        self.assertEqual(
            self.teacher.request(
                "/api/assignment", {"class_id": 1, "level_id": 1, "active": False}
            )[0],
            200,
        )
        self.assertNotIn(
            1,
            [r["level_id"] for r in self.student.request("/api/student")[1]["levels"]],
        )
        self.assertTrue(
            any(
                a["level_id"] == 1
                for a in self.student.request("/api/student")[1]["attempts"]
            )
        )
        self.assertEqual(
            self.teacher.request(
                "/api/assignment", {"class_id": 1, "level_id": 1, "active": True}
            )[0],
            200,
        )
        self.assertEqual(
            self.teacher.request(
                "/api/assignment",
                {"student_id": 2, "level_id": 19, "position": 0, "unlock_accuracy": 0},
            )[0],
            200,
        )
        self.assertIn(
            19,
            [r["level_id"] for r in self.student.request("/api/student")[1]["levels"]],
        )
        self.teacher.request(
            "/api/assignment", {"student_id": 2, "level_id": 19, "active": False}
        )

    def test_locked_run_abandoned_and_practice(self):
        self.assertEqual(self.student.request("/api/run", {"level_id": 18})[0], 403)
        _, run = self.student.request("/api/run", {"level_id": 1})
        status, res = self.student.request(
            "/api/attempt",
            {"run_id": run["run_id"], "events": [], "active_ms": 0, "abandoned": True},
        )
        self.assertEqual(status, 200)
        self.assertIsNone(res["attempt"]["bots"])
        self.assertIsNone(res["attempt"]["score"])
        self.assertEqual(
            self.student.request(
                "/api/attempt",
                {
                    "run_id": run["run_id"],
                    "events": [],
                    "active_ms": 0,
                    "abandoned": True,
                },
            )[0],
            409,
        )
        _, run = self.student.request("/api/run", {"level_id": 1, "practice": True})
        with server.connect() as db:
            db.execute(
                "UPDATE runs SET started=started-20 WHERE id=?", (run["run_id"],)
            )
        events = [
            {"kind": "char", "char": ch, "t": i * 100}
            for i, ch in enumerate(run["level"]["text"])
        ]
        status, res = self.student.request(
            "/api/attempt",
            {
                "run_id": run["run_id"],
                "events": events,
                "active_ms": 20000,
                "score": 100,
                "bots": 5,
            },
        )
        self.assertEqual(status, 200)
        self.assertIsNone(res["attempt"]["bots"])
        self.assertTrue(res["attempt"]["practice"])

    def test_foreign_run_and_anti_manipulation(self):
        other = Client(self.base)
        other.login("leo.demo")
        _, run = self.student.request("/api/run", {"level_id": 1})
        self.assertEqual(
            other.request(
                "/api/attempt",
                {
                    "run_id": run["run_id"],
                    "events": [],
                    "active_ms": 0,
                    "abandoned": True,
                },
            )[0],
            409,
        )
        events = [{"kind": "char", "char": ch, "t": 0} for ch in run["level"]["text"]]
        self.assertEqual(
            self.student.request(
                "/api/attempt",
                {"run_id": run["run_id"], "events": events, "active_ms": 1},
            )[0],
            400,
        )
        self.assertEqual(
            self.student.request(
                "/api/attempt",
                {"run_id": run["run_id"], "events": events, "active_ms": 999999},
            )[0],
            400,
        )

    def test_create_move_reset_and_level(self):
        _, cls = self.teacher.request("/api/class", {"name": "New class"})
        status, user = self.teacher.request(
            "/api/student-account",
            {
                "username": "test.student",
                "alias": "Pilot",
                "password": "AtigraDemo2026!",
                "class_id": cls["id"],
            },
        )
        self.assertEqual(status, 200)
        pupil = Client(self.base)
        pupil.login("test.student")
        self.assertEqual(
            self.teacher.request(
                "/api/password",
                {"student_id": user["id"], "password": "changed-password"},
            )[0],
            200,
        )
        self.assertEqual(pupil.request("/api/me")[0], 401)
        self.assertEqual(
            pupil.request(
                "/api/login", {"login": "test.student", "password": "AtigraDemo2026!"}
            )[0],
            401,
        )
        self.assertEqual(
            self.teacher.request(
                "/api/enrollment", {"student_id": user["id"], "class_id": 1}
            )[0],
            200,
        )
        self.assertEqual(
            self.teacher.request(
                "/api/enrollment", {"student_id": user["id"], "class_id": None}
            )[0],
            200,
        )
        level = {
            "name": "Custom ñ",
            "text": "ñ á Ñ",
            "mode": "portal",
            "language": "es",
            "target_wpm": 10,
            "unlock_accuracy": 91,
            "published": False,
        }
        status, created = self.teacher.request("/api/level", level)
        self.assertEqual(status, 200)
        self.assertEqual(
            self.other_client.request("/api/level", {**level, "id": created["id"]})[0],
            403,
        )
        self.assertEqual(
            self.teacher.request(
                "/api/level", {**level, "id": created["id"], "published": True}
            )[0],
            200,
        )

    def test_weekly_best_only_history_and_privacy(self):
        self.complete(self.student, seconds=12)
        self.complete(self.student, seconds=30)
        status, ranking = self.teacher.request("/api/ranking?class_id=1")
        self.assertEqual(status, 200)
        nova = next(r for r in ranking["results"] if r["alias"] == "Nova")
        self.assertEqual(nova["score"], 100)
        self.assertNotIn("email", nova)
        self.assertNotIn("username", nova)
        with server.connect() as db:
            monday = "2026-01-05"
            db.execute(
                "INSERT INTO attempts(student_id,level_id,class_id,completed,practice,accuracy,wpm,active_ms,score,bots,errors,typed,correct,created_at,week,eligible) VALUES(2,1,1,1,0,97,20,10000,99,5,'{}',10,10,?,?,1)",
                ("2026-01-06T12:00:00+00:00", monday),
            )
        self.assertEqual(
            self.teacher.request("/api/ranking?class_id=1&week=" + monday)[1][
                "results"
            ][0]["score"],
            99,
        )
        with server.connect() as db:
            self.assertIsNotNone(
                db.execute(
                    "SELECT * FROM weekly_snapshots WHERE week=?", (monday,)
                ).fetchone()
            )

    def test_challenge_removal_and_ties(self):
        self.complete(self.student)
        self.teacher.request(
            "/api/assignment", {"class_id": 1, "level_id": 1, "weekly": False}
        )
        self.assertFalse(
            any(
                r["alias"] == "Nova"
                for r in self.teacher.request("/api/ranking?class_id=1")[1]["results"]
            )
        )
        self.teacher.request(
            "/api/assignment", {"class_id": 1, "level_id": 1, "weekly": True}
        )
        other = Client(self.base)
        other.login("leo.demo")
        self.complete(other, seconds=20)
        results = self.teacher.request("/api/ranking?class_id=1")[1]["results"]
        self.assertEqual(results[0]["alias"], "Nova")
        self.assertEqual(results[0]["score"], results[1]["score"])
        self.assertLess(results[0]["active_ms"], results[1]["active_ms"])

    def test_delete_distinct_from_unassign(self):
        level = {
            "name": "Unused",
            "text": "abc",
            "mode": "portal",
            "language": "en",
            "target_wpm": 10,
        }
        _, created = self.teacher.request("/api/level", level)
        self.assertEqual(
            self.other_client.request("/api/delete-level", {"id": created["id"]})[0],
            403,
        )
        self.assertEqual(
            self.teacher.request("/api/delete-level", {"id": created["id"]})[0], 200
        )
        _, created = self.teacher.request("/api/level", level)
        self.teacher.request(
            "/api/assignment", {"class_id": 1, "level_id": created["id"]}
        )
        self.assertEqual(
            self.teacher.request("/api/delete-level", {"id": created["id"]})[0], 409
        )

    def test_export_and_static_assets(self):
        self.complete(self.student)
        status, csv = self.teacher.request("/api/export?student_id=2")
        self.assertEqual(status, 200)
        self.assertIn(b"Nova", csv)
        self.assertEqual(
            self.other_client.request("/api/export?student_id=2")[1].count(b"\n"), 1
        )
        for path in ("/", "/app.js", "/styles.css"):
            self.assertEqual(Client(self.base).request(path)[0], 200)
        self.assertEqual(Client(self.base).request("/server.py")[0], 404)
        self.assertEqual(Client(self.base).request("/api/student")[0], 401)


if __name__ == "__main__":
    unittest.main()
