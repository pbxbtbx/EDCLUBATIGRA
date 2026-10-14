#!/usr/bin/env python3
"""ATIBOT Academy: dependency-free educational typing application."""
import argparse, csv, hashlib, hmac, io, json, os, secrets, sqlite3, time, unicodedata
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from pathlib import Path
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs

ROOT = Path(__file__).resolve().parent
DB_PATH = os.environ.get("ATIGRA_DB", str(ROOT / "data" / "atigra.sqlite3"))
MODES = ["castle", "race", "bridge", "dragon", "explore", "portal"]
PLANETS = [
    ("Órbita del castillo", "Castle orbit", "⌂"),
    ("Nebulosa de cristal", "Crystal nebula", "◇"),
    ("Forja del dragón", "Dragon forge", "♜"),
    ("Bosque de circuitos", "Circuit forest", "♧"),
    ("Luna de las runas", "Rune moon", "☾"),
    ("Portal de las estrellas", "Star portal", "✧"),
]
DEFAULT_RULES = {
    "accuracy_weight": 0.75,
    "thresholds": [50, 65, 80, 95],
    "cap2_accuracy": 80,
    "cap3_accuracy": 90,
    "five_accuracy": 97,
}
SCHEMA = """
PRAGMA journal_mode=WAL;
CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT UNIQUE COLLATE NOCASE NOT NULL, email TEXT UNIQUE COLLATE NOCASE, alias TEXT NOT NULL, role TEXT NOT NULL CHECK(role IN ('teacher','student')), password TEXT NOT NULL, owner_id INTEGER REFERENCES users(id), created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS classes(id INTEGER PRIMARY KEY, teacher_id INTEGER NOT NULL REFERENCES users(id), name TEXT NOT NULL, archived INTEGER DEFAULT 0, leaderboard INTEGER DEFAULT 1, rules TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS enrollments(student_id INTEGER PRIMARY KEY REFERENCES users(id), class_id INTEGER NOT NULL REFERENCES classes(id));
CREATE TABLE IF NOT EXISTS planets(id INTEGER PRIMARY KEY, name_es TEXT, name_en TEXT, icon TEXT);
CREATE TABLE IF NOT EXISTS levels(id INTEGER PRIMARY KEY, owner_id INTEGER REFERENCES users(id), planet_id INTEGER REFERENCES planets(id), name TEXT NOT NULL, mode TEXT NOT NULL, text TEXT NOT NULL, language TEXT NOT NULL, target_wpm REAL NOT NULL, unlock_accuracy REAL NOT NULL, position INTEGER NOT NULL, published INTEGER DEFAULT 1);
CREATE TABLE IF NOT EXISTS assignments(id INTEGER PRIMARY KEY, class_id INTEGER REFERENCES classes(id), student_id INTEGER REFERENCES users(id), level_id INTEGER NOT NULL REFERENCES levels(id), position INTEGER NOT NULL, unlock_accuracy REAL NOT NULL DEFAULT 90, prerequisite_id INTEGER REFERENCES levels(id), weekly INTEGER DEFAULT 1, active INTEGER DEFAULT 1, CHECK((class_id IS NULL) != (student_id IS NULL)));
CREATE UNIQUE INDEX IF NOT EXISTS class_assignment ON assignments(class_id,level_id) WHERE class_id IS NOT NULL;
CREATE UNIQUE INDEX IF NOT EXISTS student_assignment ON assignments(student_id,level_id) WHERE student_id IS NOT NULL;
CREATE TABLE IF NOT EXISTS sessions(token TEXT PRIMARY KEY, user_id INTEGER NOT NULL REFERENCES users(id), csrf TEXT NOT NULL, expires REAL NOT NULL);
CREATE TABLE IF NOT EXISTS runs(id TEXT PRIMARY KEY, student_id INTEGER NOT NULL REFERENCES users(id), level_id INTEGER NOT NULL REFERENCES levels(id), text TEXT NOT NULL, target_wpm REAL NOT NULL, rules TEXT NOT NULL, started REAL NOT NULL, practice INTEGER NOT NULL, consumed INTEGER DEFAULT 0);
CREATE TABLE IF NOT EXISTS attempts(id INTEGER PRIMARY KEY, student_id INTEGER NOT NULL REFERENCES users(id), level_id INTEGER NOT NULL REFERENCES levels(id), class_id INTEGER REFERENCES classes(id), completed INTEGER NOT NULL, practice INTEGER NOT NULL, accuracy REAL, wpm REAL, active_ms INTEGER NOT NULL, score REAL, bots INTEGER, errors TEXT NOT NULL, typed INTEGER NOT NULL, correct INTEGER NOT NULL, created_at TEXT NOT NULL, week TEXT NOT NULL, eligible INTEGER DEFAULT 0);
CREATE INDEX IF NOT EXISTS attempt_student ON attempts(student_id,level_id,created_at);
CREATE TABLE IF NOT EXISTS weekly_snapshots(class_id INTEGER NOT NULL REFERENCES classes(id), week TEXT NOT NULL, results TEXT NOT NULL, PRIMARY KEY(class_id,week));
"""


def connect():
    db = sqlite3.connect(DB_PATH, timeout=20)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys=ON")
    return db


def now():
    return datetime.now(timezone.utc).isoformat()


def week_key(moment=None):
    d = (moment or datetime.now(timezone.utc)).astimezone(ZoneInfo("Europe/Madrid"))
    return (d.date() - timedelta(days=d.weekday())).isoformat()


def password_hash(password):
    if not isinstance(password, str) or not 8 <= len(password) <= 200:
        raise ValueError("password_length")
    salt = secrets.token_hex(16)
    return (
        salt
        + ":"
        + hashlib.scrypt(
            password.encode(), salt=bytes.fromhex(salt), n=16384, r=8, p=1
        ).hex()
    )


def password_ok(password, stored):
    try:
        salt, digest = stored.split(":")
        return hmac.compare_digest(
            digest,
            hashlib.scrypt(
                password.encode(), salt=bytes.fromhex(salt), n=16384, r=8, p=1
            ).hex(),
        )
    except (ValueError, AttributeError):
        return False


def seed(demo=None):
    if demo is None:
        demo = os.environ.get("ATIGRA_DEMO", "1") == "1"
    Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)
    with connect() as db:
        db.executescript(SCHEMA)
        if db.execute("SELECT 1 FROM levels LIMIT 1").fetchone():
            return
        if demo:
            teacher = db.execute(
                "INSERT INTO users(username,alias,role,password,created_at) VALUES(?,?,?,?,?)",
                (
                    "profe.demo",
                    "Comandante Demo",
                    "teacher",
                    password_hash("AtigraDemo2026!"),
                    now(),
                ),
            ).lastrowid
            cid = db.execute(
                "INSERT INTO classes(teacher_id,name,rules) VALUES(?,?,?)",
                (teacher, "Exploradores · DEMO", json.dumps(DEFAULT_RULES)),
            ).lastrowid
            for username, alias in [
                ("nova.demo", "Nova"),
                ("leo.demo", "Leo"),
                ("luna.demo", "Luna"),
            ]:
                uid = db.execute(
                    "INSERT INTO users(username,alias,role,password,owner_id,created_at) VALUES(?,?,?,?,?,?)",
                    (
                        username,
                        alias,
                        "student",
                        password_hash("AtigraDemo2026!"),
                        teacher,
                        now(),
                    ),
                ).lastrowid
                db.execute("INSERT INTO enrollments VALUES(?,?)", (uid, cid))
        for i, (es, en, icon) in enumerate(PLANETS, 1):
            db.execute("INSERT INTO planets VALUES(?,?,?,?)", (i, es, en, icon))
        exercises = [
            ("Base de lanzamiento", "asdf jklñ asdf jklñ", "asdf jkl asdf jkl"),
            (
                "Escudos centrales",
                "fff jjj ddd kkk sss lll aaa ñññ",
                "fff jjj ddd kkk sss lll aaa",
            ),
            ("Primeras runas", "faja sala dada falla", "sad lad fall salad"),
            (
                "Cristales superiores",
                "qwer tyui op qwer tyui op",
                "qwer tyui op qwer tyui op",
            ),
            ("Nave de luz", "río torre puerto ruta", "tree tire route rope"),
            ("Radar estelar", "quiero ir a tu torre", "we write our story"),
            ("Forja inferior", "zxcv bnm zxcv bnm", "zxcv bnm zxcv bnm"),
            ("Piezas del dragón", "nave casco brazo motor", "van cave zoom robot"),
            ("Vuelo mecánico", "mi nave vuela muy bien", "my brave robot can fly"),
            (
                "Sendero de palabras",
                "robot planeta castillo escudo",
                "robot planet castle shield",
            ),
            (
                "Recursos del bosque",
                "recoge metal y crea una nave",
                "collect metal and build a ship",
            ),
            (
                "Circuito de precisión",
                "practicar con calma ayuda mucho",
                "practice slowly and grow strong",
            ),
            ("Runas mayúsculas", "Atibot viaja a Marte.", "Atibot travels to Mars."),
            (
                "Señales del portal",
                "¡Hola! El dragón soñó con Ñandú.",
                "Hello! The dragon says: Ready?",
            ),
            (
                "Código del caballero",
                "Misión 5: energía al 100%.",
                "Mission 5: energy at 100%.",
            ),
            (
                "Bitácora espacial",
                "La nave cruza el cielo. ATIBOT cuida del equipo.",
                "The ship crosses the sky. ATIBOT helps the team.",
            ),
            (
                "El castillo estelar",
                "En el castillo espacial, un dragón protege las estrellas.",
                "In the space castle, a dragon protects the stars.",
            ),
            (
                "Gran portal",
                "¡Buen viaje, ATIBOT! La precisión abre nuevos mundos.",
                "Safe travels, ATIBOT! Accuracy opens new worlds.",
            ),
        ]
        for language in ("es", "en"):
            for i, (name, es, en) in enumerate(exercises):
                lid = db.execute(
                    "INSERT INTO levels(owner_id,planet_id,name,mode,text,language,target_wpm,unlock_accuracy,position) VALUES(NULL,?,?,?,?,?,?,90,?)",
                    (
                        i // 3 + 1,
                        (
                            name
                            if language == "es"
                            else [
                                "Launch base",
                                "Central shields",
                                "First runes",
                                "Upper crystals",
                                "Light ship",
                                "Star radar",
                                "Lower forge",
                                "Dragon parts",
                                "Mechanical flight",
                                "Word trail",
                                "Forest resources",
                                "Accuracy circuit",
                                "Capital runes",
                                "Portal signals",
                                "Knight code",
                                "Space log",
                                "Star castle",
                                "Grand portal",
                            ][i]
                        ),
                        MODES[i % 6],
                        es if language == "es" else en,
                        language,
                        10 + (i // 3) * 4,
                        i,
                    ),
                ).lastrowid
                # Default class uses Spanish; teachers can assign English separately.
                if demo and language == "es":
                    db.execute(
                        "INSERT INTO assignments(class_id,level_id,position,unlock_accuracy) VALUES(?,?,?,90)",
                        (cid, lid, i),
                    )


class Problem(Exception):
    def __init__(self, code, status=400):
        self.code = code
        self.status = status


def require(condition, code="forbidden", status=403):
    if not condition:
        raise Problem(code, status)


def public_user(user):
    return {k: user[k] for k in ("id", "username", "alias", "role", "email")}


def owns_class(db, user, cid):
    row = db.execute(
        "SELECT * FROM classes WHERE id=? AND teacher_id=?", (cid, user["id"])
    ).fetchone()
    require(row is not None)
    return dict(row)


def owns_student(db, user, sid):
    row = db.execute(
        "SELECT * FROM users WHERE id=? AND owner_id=? AND role='student'",
        (sid, user["id"]),
    ).fetchone()
    require(row is not None)
    return dict(row)


def usable_level(db, user, lid):
    row = db.execute(
        "SELECT * FROM levels WHERE id=? AND (owner_id IS NULL OR owner_id=?)",
        (lid, user["id"]),
    ).fetchone()
    require(row is not None)
    return dict(row)


def enrollment(db, sid):
    row = db.execute(
        "SELECT c.* FROM classes c JOIN enrollments e ON e.class_id=c.id WHERE e.student_id=?",
        (sid,),
    ).fetchone()
    return dict(row) if row else None


def student_levels(db, sid):
    cls = enrollment(db, sid)
    rows = db.execute(
        """SELECT a.*, l.name,l.mode,l.text,l.language,l.target_wpm,l.planet_id,l.published FROM assignments a JOIN levels l ON l.id=a.level_id WHERE a.active=1 AND l.published=1 AND (a.student_id=? OR (a.class_id=? AND ?=0)) ORDER BY a.position,a.id""",
        (sid, cls["id"] if cls else -1, cls["archived"] if cls else 1),
    ).fetchall()
    merged = {}
    for r in rows:
        r = dict(r)
        if r["level_id"] not in merged or r["student_id"] is not None:
            merged[r["level_id"]] = r
    levels = sorted(merged.values(), key=lambda x: (x["position"], x["id"]))
    best = {}
    for r in db.execute(
        "SELECT * FROM attempts WHERE student_id=? AND completed=1 AND practice=0 ORDER BY score DESC,accuracy DESC",
        (sid,),
    ):
        if r["level_id"] not in best:
            best[r["level_id"]] = dict(r)
    previous = None
    for r in levels:
        r["best"] = best.get(r["level_id"])
        prerequisite = r["prerequisite_id"] or (
            previous["level_id"] if previous else None
        )
        threshold = r["unlock_accuracy"]
        passed = (
            not prerequisite
            or db.execute(
                "SELECT 1 FROM attempts WHERE student_id=? AND level_id=? AND completed=1 AND practice=0 AND accuracy>=? LIMIT 1",
                (sid, prerequisite, threshold),
            ).fetchone()
            is not None
        )
        r["unlocked"] = bool(passed)
        r["prerequisite"] = prerequisite
        previous = r
    return levels


def grade(accuracy, wpm, target, rules):
    speed = min(100, wpm / target * 100)
    score = rules["accuracy_weight"] * accuracy + (1 - rules["accuracy_weight"]) * speed
    bots = 1 + sum(score >= x for x in rules["thresholds"])
    if accuracy < rules["cap2_accuracy"]:
        bots = min(bots, 2)
    elif accuracy < rules["cap3_accuracy"]:
        bots = min(bots, 3)
    if accuracy < rules["five_accuracy"] or wpm < target:
        bots = min(bots, 4)
    return round(score, 4), bots


def replay(text, events, active_ms):
    require(isinstance(events, list) and len(events) <= 20000, "invalid_events", 400)
    require(
        isinstance(active_ms, int) and 0 < active_ms <= 4 * 60 * 60 * 1000,
        "invalid_time",
        400,
    )
    text = unicodedata.normalize("NFC", text)
    typed = correct = 0
    buffer = []
    errors = {}
    last = -1
    for e in events:
        require(
            isinstance(e, dict)
            and isinstance(e.get("t"), int)
            and 0 <= e["t"]
            and last <= e["t"] <= active_ms,
            "invalid_events",
            400,
        )
        last = e["t"]
        if e.get("kind") == "backspace":
            if buffer:
                buffer.pop()
            continue
        ch = unicodedata.normalize("NFC", e.get("char", ""))
        require(
            e.get("kind") == "char"
            and len(ch) == 1
            and ch.isprintable()
            and len(buffer) < len(text),
            "invalid_events",
            400,
        )
        expected = text[len(buffer)]
        typed += 1
        if ch == expected:
            correct += 1
        else:
            errors[expected] = errors.get(expected, 0) + 1
        buffer.append(ch)
    complete = "".join(buffer) == text
    accuracy = correct / typed * 100 if typed else 0
    # Every character of a completed text is correct; corrected errors affect precision.
    wpm = (len(text) / 5) / (active_ms / 60000) if complete else 0
    return dict(
        completed=complete,
        accuracy=accuracy,
        wpm=wpm,
        errors=errors,
        typed=typed,
        correct=correct,
    )


def rank_week(db, cid, week):
    rows = db.execute(
        """SELECT a.*,u.alias FROM attempts a JOIN users u ON u.id=a.student_id WHERE a.class_id=? AND a.week=? AND a.eligible=1 AND a.completed=1 AND a.practice=0 ORDER BY a.score DESC,a.accuracy DESC,a.active_ms ASC,a.id ASC""",
        (cid, week),
    ).fetchall()
    best = {}
    for r in rows:
        if week == week_key():
            # The current challenge follows active assignment changes. Closed weeks
            # retain the eligibility recorded at completion, independent of edits.
            chosen = next(
                (
                    a
                    for a in student_levels(db, r["student_id"])
                    if a["level_id"] == r["level_id"]
                ),
                None,
            )
            if not chosen or not chosen["weekly"]:
                continue
        best.setdefault((r["student_id"], r["level_id"]), dict(r))
    students = {}
    for r in best.values():
        entry = students.setdefault(
            r["student_id"],
            dict(alias=r["alias"], score=0, accuracy=0, active_ms=0, levels=0),
        )
        entry["score"] += r["score"]
        entry["accuracy"] += r["accuracy"]
        entry["active_ms"] += r["active_ms"]
        entry["levels"] += 1
    for r in students.values():
        r["accuracy"] /= r["levels"]
        r["score"] = round(r["score"], 4)
    return sorted(
        students.values(),
        key=lambda x: (-x["score"], -x["accuracy"], x["active_ms"], x["alias"]),
    )


def leaderboard(db, cid, week):
    if week < week_key():
        saved = db.execute(
            "SELECT results FROM weekly_snapshots WHERE class_id=? AND week=?",
            (cid, week),
        ).fetchone()
        if saved:
            return json.loads(saved[0])
        results = rank_week(db, cid, week)
        db.execute(
            "INSERT OR IGNORE INTO weekly_snapshots VALUES(?,?,?)",
            (cid, week, json.dumps(results)),
        )
        return results
    return rank_week(db, cid, week)


def validate_level(data):
    name = str(data.get("name", "")).strip()
    text = unicodedata.normalize("NFC", str(data.get("text", "")))
    require(
        1 <= len(name) <= 100
        and 1 <= len(text) <= 2000
        and all(c.isprintable() for c in text),
        "invalid_level",
        400,
    )
    require(
        data.get("mode") in MODES and data.get("language") in ("es", "en"),
        "invalid_level",
        400,
    )
    target = float(data.get("target_wpm", 15))
    unlock = float(data.get("unlock_accuracy", 90))
    require(
        1 <= target <= 150
        and 0 <= unlock <= 100
        and 1 <= int(data.get("planet_id", 1)) <= 6,
        "invalid_level",
        400,
    )
    return (
        int(data.get("planet_id", 1)),
        name,
        data["mode"],
        text,
        data["language"],
        target,
        unlock,
        int(data.get("position", 0)),
        int(bool(data.get("published", True))),
    )


def validate_rules(rules):
    try:
        require(
            0 <= rules["accuracy_weight"] <= 1
            and len(rules["thresholds"]) == 4
            and rules["thresholds"] == sorted(rules["thresholds"])
            and all(0 <= x <= 100 for x in rules["thresholds"]),
            "invalid_rules",
            400,
        )
        require(
            0
            <= rules["cap2_accuracy"]
            <= rules["cap3_accuracy"]
            <= rules["five_accuracy"]
            <= 100,
            "invalid_rules",
            400,
        )
    except (KeyError, TypeError):
        raise Problem("invalid_rules", 400)
    return rules


class Handler(BaseHTTPRequestHandler):
    server_version = "Atigra/1.0"

    def log_message(self, fmt, *args):
        # Never log request bodies or credentials.
        super().log_message(fmt, *args)

    def send(
        self,
        data,
        status=200,
        headers=None,
        content_type="application/json; charset=utf-8",
    ):
        body = (
            data
            if isinstance(data, bytes)
            else json.dumps(data, ensure_ascii=False).encode()
        )
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "same-origin")
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'self'",
        )
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self.dispatch()

    def do_POST(self):
        self.dispatch()

    def dispatch(self):
        try:
            path = urlparse(self.path).path
            if not path.startswith("/api/"):
                require(self.command == "GET", "not_found", 404)
                names = {
                    "/": "index.html",
                    "/app.js": "app.js",
                    "/styles.css": "styles.css",
                }
                require(path in names, "not_found", 404)
                file = ROOT / "web" / names[path]
                return self.send(
                    file.read_bytes(),
                    content_type={
                        ".html": "text/html; charset=utf-8",
                        ".js": "text/javascript; charset=utf-8",
                        ".css": "text/css; charset=utf-8",
                    }[file.suffix],
                )
            data = {}
            if self.command == "POST":
                length = int(self.headers.get("Content-Length", "0"))
                require(0 < length <= 2000000, "invalid_body", 400)
                data = json.loads(self.rfile.read(length))
                require(isinstance(data, dict), "invalid_body", 400)
                origin = self.headers.get("Origin")
                require(
                    not origin or urlparse(origin).netloc == self.headers.get("Host"),
                    "forbidden",
                    403,
                )
            with connect() as db:
                if self.command == "POST":
                    db.execute("BEGIN IMMEDIATE")
                if path == "/api/config" and self.command == "GET":
                    return self.send(
                        {"demo": os.environ.get("ATIGRA_DEMO", "1") == "1"}
                    )
                if path == "/api/login" and self.command == "POST":
                    return self.login(db, data)
                cookies = SimpleCookie()
                cookies.load(self.headers.get("Cookie", ""))
                token = cookies.get("atigra")
                session = db.execute(
                    "SELECT * FROM sessions WHERE token=? AND expires>?",
                    (token.value if token else "", time.time()),
                ).fetchone()
                require(session is not None, "unauthenticated", 401)
                user = dict(
                    db.execute(
                        "SELECT * FROM users WHERE id=?", (session["user_id"],)
                    ).fetchone()
                )
                if self.command == "POST":
                    require(
                        hmac.compare_digest(
                            self.headers.get("X-CSRF-Token", ""), session["csrf"]
                        ),
                        "csrf",
                        403,
                    )
                if path == "/api/me":
                    return self.send(
                        {"user": public_user(user), "csrf": session["csrf"]}
                    )
                if path == "/api/logout" and self.command == "POST":
                    db.execute(
                        "DELETE FROM sessions WHERE token=?", (session["token"],)
                    )
                    return self.send(
                        {"ok": True},
                        headers={
                            "Set-Cookie": "atigra=; Path=/; Max-Age=0; HttpOnly; SameSite=Strict"
                        },
                    )
                if path == "/api/planets":
                    return self.send(
                        [dict(r) for r in db.execute("SELECT * FROM planets")]
                    )
                if user["role"] == "student":
                    return self.student(db, user, path, data)
                return self.teacher(db, user, path, data)
        except Problem as e:
            self.send({"error": e.code}, e.status)
        except (ValueError, TypeError, KeyError, json.JSONDecodeError, OverflowError):
            self.send({"error": "invalid_input"}, 400)
        except sqlite3.IntegrityError:
            self.send({"error": "conflict"}, 409)
        except Exception as e:
            print("Server error:", type(e).__name__, str(e))
            self.send({"error": "server_error"}, 500)

    def login(self, db, data):
        key = (self.client_address[0], str(data.get("login", "")).casefold())
        with self.server.rate_lock:
            failures = [
                t for t in self.server.failures.get(key, []) if t > time.time() - 300
            ]
            self.server.failures[key] = failures
            require(len(failures) < 10, "rate_limited", 429)
        login = str(data.get("login", ""))[:200]
        password = str(data.get("password", ""))[:200]
        user = db.execute(
            "SELECT * FROM users WHERE username=? OR email=?", (login, login)
        ).fetchone()
        # Use a dummy scrypt calculation to avoid cheap enumeration.
        valid = password_ok(
            password, user["password"] if user else self.server.dummy_password
        )
        if not user or not valid:
            with self.server.rate_lock:
                self.server.failures.setdefault(key, []).append(time.time())
            raise Problem("invalid_login", 401)
        token = secrets.token_urlsafe(32)
        csrf = secrets.token_urlsafe(32)
        db.execute("DELETE FROM sessions WHERE expires<?", (time.time(),))
        db.execute(
            "INSERT INTO sessions VALUES(?,?,?,?)",
            (token, user["id"], csrf, time.time() + 12 * 3600),
        )
        secure = "; Secure" if os.environ.get("ATIGRA_SECURE_COOKIE") == "1" else ""
        self.send(
            {"user": public_user(user), "csrf": csrf},
            headers={
                "Set-Cookie": f"atigra={token}; Path=/; Max-Age=43200; HttpOnly; SameSite=Strict{secure}"
            },
        )

    def student(self, db, user, path, data):
        sid = user["id"]
        cls = enrollment(db, sid)
        if path == "/api/student" and self.command == "GET":
            attempts = [
                dict(r)
                for r in db.execute(
                    "SELECT a.*,l.name,l.language FROM attempts a JOIN levels l ON l.id=a.level_id WHERE student_id=? ORDER BY a.id DESC",
                    (sid,),
                )
            ]
            levels = student_levels(db, sid)
            week = parse_qs(urlparse(self.path).query).get("week", [week_key()])[0]
            require(
                len(week) == 10 and datetime.fromisoformat(week).weekday() == 0,
                "invalid_week",
                400,
            )
            weeks = [
                r[0]
                for r in db.execute(
                    "SELECT DISTINCT week FROM attempts WHERE class_id=? ORDER BY week DESC",
                    (cls["id"] if cls else -1,),
                )
            ]
            return self.send(
                {
                    "levels": levels,
                    "attempts": attempts,
                    "class": (
                        {k: cls[k] for k in ("id", "name", "leaderboard")}
                        if cls
                        else None
                    ),
                    "week": week,
                    "weeks": weeks,
                    "leaderboard": (
                        leaderboard(db, cls["id"], week)
                        if cls and cls["leaderboard"] and not cls["archived"]
                        else []
                    ),
                }
            )
        require(self.command == "POST", "not_found", 404)
        if path == "/api/run":
            level = next(
                (
                    r
                    for r in student_levels(db, sid)
                    if r["level_id"] == int(data["level_id"])
                ),
                None,
            )
            require(level is not None and level["unlocked"], "level_locked", 403)
            rid = secrets.token_urlsafe(24)
            rules = json.loads(cls["rules"]) if cls else DEFAULT_RULES
            db.execute(
                "INSERT INTO runs VALUES(?,?,?,?,?,?,?,?,0)",
                (
                    rid,
                    sid,
                    level["level_id"],
                    level["text"],
                    level["target_wpm"],
                    json.dumps(rules),
                    time.time(),
                    int(bool(data.get("practice", False))),
                ),
            )
            return self.send({"run_id": rid, "level": level})
        if path == "/api/attempt":
            run = db.execute(
                "SELECT * FROM runs WHERE id=? AND student_id=? AND consumed=0",
                (data["run_id"], sid),
            ).fetchone()
            require(run is not None, "invalid_run", 409)
            active = data.get("active_ms", 0)
            abandoned = bool(data.get("abandoned", False))
            if abandoned and active == 0 and not data.get("events"):
                result = dict(
                    completed=False, accuracy=0, wpm=0, errors={}, typed=0, correct=0
                )
            else:
                result = replay(run["text"], data.get("events", []), active)
            require(
                isinstance(active, int)
                and active <= max(0, (time.time() - run["started"]) * 1000) + 2000,
                "invalid_time",
                400,
            )
            require(result["wpm"] <= 220, "implausible_speed", 400)
            if abandoned:
                result["completed"] = False
            require(result["completed"] or abandoned, "incomplete", 400)
            db.execute("UPDATE runs SET consumed=1 WHERE id=?", (run["id"],))
            score, bots = (
                grade(
                    result["accuracy"],
                    result["wpm"],
                    run["target_wpm"],
                    json.loads(run["rules"]),
                )
                if result["completed"] and not run["practice"]
                else (None, None)
            )
            levels = student_levels(db, sid)
            assignment = next(
                (r for r in levels if r["level_id"] == run["level_id"]), None
            )
            eligible = bool(
                cls and not cls["archived"] and assignment and assignment["weekly"]
            )
            previous = db.execute(
                "SELECT * FROM attempts WHERE student_id=? AND level_id=? AND completed=1 AND practice=0 ORDER BY score DESC LIMIT 1",
                (sid, run["level_id"]),
            ).fetchone()
            aid = db.execute(
                "INSERT INTO attempts(student_id,level_id,class_id,completed,practice,accuracy,wpm,active_ms,score,bots,errors,typed,correct,created_at,week,eligible) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    sid,
                    run["level_id"],
                    cls["id"] if cls else None,
                    int(result["completed"]),
                    run["practice"],
                    result["accuracy"],
                    result["wpm"],
                    active,
                    score,
                    bots,
                    json.dumps(result["errors"], ensure_ascii=False),
                    result["typed"],
                    result["correct"],
                    now(),
                    week_key(),
                    int(eligible),
                ),
            ).lastrowid
            return self.send(
                {
                    "attempt": dict(
                        db.execute(
                            "SELECT * FROM attempts WHERE id=?", (aid,)
                        ).fetchone()
                    ),
                    "previous": dict(previous) if previous else None,
                }
            )
        raise Problem("not_found", 404)

    def teacher(self, db, user, path, data):
        tid = user["id"]
        if path == "/api/teacher" and self.command == "GET":
            classes = [
                dict(r)
                for r in db.execute("SELECT * FROM classes WHERE teacher_id=?", (tid,))
            ]
            for cls in classes:
                cls["rules"] = json.loads(cls["rules"])
                cls["assignments"] = [
                    dict(r)
                    for r in db.execute(
                        "SELECT a.*,l.name,l.language FROM assignments a JOIN levels l ON l.id=a.level_id WHERE a.class_id=? ORDER BY a.position",
                        (cls["id"],),
                    )
                ]
            students = [
                dict(r)
                for r in db.execute(
                    "SELECT u.id,u.username,u.alias,u.email,e.class_id FROM users u LEFT JOIN enrollments e ON e.student_id=u.id WHERE u.owner_id=?",
                    (tid,),
                )
            ]
            individual = [
                dict(r)
                for r in db.execute(
                    "SELECT a.*,l.name,l.language FROM assignments a JOIN levels l ON l.id=a.level_id JOIN users u ON u.id=a.student_id WHERE u.owner_id=?",
                    (tid,),
                )
            ]
            levels = [
                dict(r)
                for r in db.execute(
                    "SELECT * FROM levels WHERE owner_id IS NULL OR owner_id=? ORDER BY position,language",
                    (tid,),
                )
            ]
            return self.send(
                {
                    "classes": classes,
                    "students": students,
                    "levels": levels,
                    "individual": individual,
                }
            )
        if path in ("/api/reports", "/api/export") and self.command == "GET":
            q = parse_qs(urlparse(self.path).query)
            sql = "SELECT a.*,l.name AS level_name,l.language,u.alias,u.username FROM attempts a JOIN users u ON u.id=a.student_id JOIN levels l ON l.id=a.level_id WHERE u.owner_id=?"
            params = [tid]
            for key, column in [
                ("class_id", "a.class_id"),
                ("student_id", "a.student_id"),
                ("level_id", "a.level_id"),
                ("language", "l.language"),
            ]:
                if q.get(key, [""])[0]:
                    sql += f" AND {column}=?"
                    params.append(q[key][0])
            for key, op in [("from", ">="), ("to", "<")]:
                if q.get(key, [""])[0]:
                    local = datetime.strptime(q[key][0], "%Y-%m-%d").replace(
                        tzinfo=ZoneInfo("Europe/Madrid")
                    )
                    if key == "to":
                        local += timedelta(days=1)
                    sql += f" AND a.created_at{op}?"
                    params.append(local.astimezone(timezone.utc).isoformat())
            rows = [dict(r) for r in db.execute(sql + " ORDER BY a.id DESC", params)]
            if path == "/api/reports":
                return self.send(rows)
            output = io.StringIO()
            columns = [
                "id",
                "alias",
                "username",
                "level_name",
                "language",
                "completed",
                "practice",
                "accuracy",
                "wpm",
                "active_ms",
                "score",
                "bots",
                "errors",
                "created_at",
                "week",
            ]
            writer = csv.DictWriter(output, fieldnames=columns, extrasaction="ignore")
            writer.writeheader()
            for r in rows:
                for k in columns:
                    if isinstance(r.get(k), str) and r[k].startswith(
                        ("=", "+", "-", "@", "\t", "\r")
                    ):
                        r[k] = "'" + r[k]
                writer.writerow(r)
            return self.send(
                ("\ufeff" + output.getvalue()).encode(),
                headers={
                    "Content-Disposition": "attachment; filename=atigra-results.csv"
                },
                content_type="text/csv; charset=utf-8",
            )
        if path == "/api/ranking" and self.command == "GET":
            q = parse_qs(urlparse(self.path).query)
            cid = int(q["class_id"][0])
            owns_class(db, user, cid)
            week = q.get("week", [week_key()])[0]
            require(
                len(week) == 10 and datetime.fromisoformat(week).weekday() == 0,
                "invalid_week",
                400,
            )
            return self.send({"week": week, "results": leaderboard(db, cid, week)})
        require(self.command == "POST", "not_found", 404)
        if path == "/api/class":
            name = str(data.get("name", "")).strip()
            require(1 <= len(name) <= 100, "invalid_input", 400)
            rules = validate_rules(data.get("rules", DEFAULT_RULES))
            if data.get("id"):
                owns_class(db, user, int(data["id"]))
                db.execute(
                    "UPDATE classes SET name=?,archived=?,leaderboard=?,rules=? WHERE id=?",
                    (
                        name,
                        int(bool(data.get("archived"))),
                        int(bool(data.get("leaderboard", True))),
                        json.dumps(rules),
                        data["id"],
                    ),
                )
                cid = data["id"]
            else:
                cid = db.execute(
                    "INSERT INTO classes(teacher_id,name,rules,leaderboard) VALUES(?,?,?,?)",
                    (
                        tid,
                        name,
                        json.dumps(rules),
                        int(bool(data.get("leaderboard", True))),
                    ),
                ).lastrowid
            return self.send({"id": cid})
        if path == "/api/student-account":
            alias = str(data.get("alias", "")).strip()
            username = str(data.get("username", "")).strip()
            email = str(data.get("email", "")).strip() or None
            require(
                1 <= len(alias) <= 60
                and 3 <= len(username) <= 60
                and all(c.isalnum() or c in "._-" for c in username),
                "invalid_input",
                400,
            )
            require(
                not email or ("@" in email and len(email) <= 200), "invalid_input", 400
            )
            cid = data.get("class_id")
            if cid:
                owns_class(db, user, int(cid))
            sid = db.execute(
                "INSERT INTO users(username,email,alias,role,password,owner_id,created_at) VALUES(?,?,?,'student',?,?,?)",
                (username, email, alias, password_hash(data["password"]), tid, now()),
            ).lastrowid
            if cid:
                db.execute("INSERT INTO enrollments VALUES(?,?)", (sid, cid))
            return self.send({"id": sid})
        if path == "/api/enrollment":
            sid = int(data["student_id"])
            owns_student(db, user, sid)
            cid = data.get("class_id")
            if cid:
                owns_class(db, user, int(cid))
            db.execute("DELETE FROM enrollments WHERE student_id=?", (sid,))
            if cid:
                db.execute("INSERT INTO enrollments VALUES(?,?)", (sid, cid))
            return self.send({"ok": True})
        if path == "/api/password":
            sid = int(data["student_id"])
            owns_student(db, user, sid)
            db.execute(
                "UPDATE users SET password=? WHERE id=?",
                (password_hash(data["password"]), sid),
            )
            db.execute("DELETE FROM sessions WHERE user_id=?", (sid,))
            db.execute("UPDATE runs SET consumed=1 WHERE student_id=?", (sid,))
            return self.send({"ok": True})
        if path == "/api/level":
            values = validate_level(data)
            if data.get("id"):
                row = usable_level(db, user, int(data["id"]))
                require(row["owner_id"] == tid, "shared_level_readonly", 403)
                db.execute(
                    "UPDATE levels SET planet_id=?,name=?,mode=?,text=?,language=?,target_wpm=?,unlock_accuracy=?,position=?,published=? WHERE id=?",
                    values + (data["id"],),
                )
                lid = data["id"]
            else:
                lid = db.execute(
                    "INSERT INTO levels(owner_id,planet_id,name,mode,text,language,target_wpm,unlock_accuracy,position,published) VALUES(?,?,?,?,?,?,?,?,?,?)",
                    (tid,) + values,
                ).lastrowid
            return self.send({"id": lid})
        if path == "/api/delete-level":
            lid = int(data["id"])
            level = usable_level(db, user, lid)
            require(level["owner_id"] == tid, "shared_level_readonly", 403)
            used = (
                db.execute(
                    "SELECT 1 FROM attempts WHERE level_id=? LIMIT 1", (lid,)
                ).fetchone()
                or db.execute(
                    "SELECT 1 FROM assignments WHERE level_id=? OR prerequisite_id=? LIMIT 1",
                    (lid, lid),
                ).fetchone()
                or db.execute(
                    "SELECT 1 FROM runs WHERE level_id=? LIMIT 1", (lid,)
                ).fetchone()
            )
            require(not used, "level_has_history", 409)
            db.execute("DELETE FROM levels WHERE id=?", (lid,))
            return self.send({"ok": True})
        if path == "/api/assignment":
            cid = data.get("class_id")
            sid = data.get("student_id")
            require(bool(cid) != bool(sid), "invalid_input", 400)
            if cid:
                owns_class(db, user, int(cid))
            if sid:
                owns_student(db, user, int(sid))
            lid = int(data["level_id"])
            level = usable_level(db, user, lid)
            prerequisite = data.get("prerequisite_id") or None
            if prerequisite:
                usable_level(db, user, int(prerequisite))
                require(int(prerequisite) != lid, "invalid_input", 400)
            unlock = float(data.get("unlock_accuracy", level["unlock_accuracy"]))
            require(0 <= unlock <= 100, "invalid_input", 400)
            existing = db.execute(
                "SELECT id FROM assignments WHERE level_id=? AND "
                + ("class_id=?" if cid else "student_id=?"),
                (lid, cid or sid),
            ).fetchone()
            values = (
                int(data.get("position", level["position"])),
                unlock,
                prerequisite,
                int(bool(data.get("weekly", True))),
                int(bool(data.get("active", True))),
            )
            if existing:
                db.execute(
                    "UPDATE assignments SET position=?,unlock_accuracy=?,prerequisite_id=?,weekly=?,active=? WHERE id=?",
                    values + (existing[0],),
                )
            else:
                db.execute(
                    "INSERT INTO assignments(position,unlock_accuracy,prerequisite_id,weekly,active,class_id,student_id,level_id) VALUES(?,?,?,?,?,?,?,?)",
                    values + (cid, sid, lid),
                )
            return self.send({"ok": True})
        raise Problem("not_found", 404)


def make_server(host="127.0.0.1", port=8000):
    import threading

    server = ThreadingHTTPServer((host, port), Handler)
    server.failures = {}
    server.rate_lock = threading.Lock()
    server.dummy_password = password_hash(secrets.token_urlsafe(20))
    return server


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default=os.environ.get("ATIGRA_HOST", "127.0.0.1"))
    parser.add_argument(
        "--port", type=int, default=int(os.environ.get("ATIGRA_PORT", "8000"))
    )
    parser.add_argument("--init-only", action="store_true")
    args = parser.parse_args()
    seed()
    if not args.init_only:
        server = make_server(args.host, args.port)
        print(f"ATIBOT Academy listening on {args.host}:{args.port}", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            server.server_close()
