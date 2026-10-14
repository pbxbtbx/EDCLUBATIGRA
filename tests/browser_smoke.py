"""Optional real-browser integration test; requires Playwright and Chromium."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import server

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sync_playwright = None


@unittest.skipUnless(
    sync_playwright and shutil.which("chromium"),
    "Install Playwright and Chromium for browser validation",
)
class BrowserFlow(unittest.TestCase):
    def test_six_games_teacher_student_and_accessibility(self):
        with tempfile.TemporaryDirectory() as temp:
            old = server.DB_PATH
            server.DB_PATH = temp + "/browser.sqlite3"
            server.seed()
            # Test fixture: six short, independent missions. Product seed is untouched.
            with server.connect() as db:
                for i, mode in enumerate(server.MODES, 1):
                    db.execute(
                        "UPDATE levels SET text=?,mode=? WHERE id=?",
                        ("ñ á Ñ." if i == 1 else "go " + mode, mode, i),
                    )
                    db.execute(
                        "UPDATE assignments SET unlock_accuracy=0 WHERE level_id=?",
                        (i,),
                    )
            server.DB_PATH = old
            http = server.make_server(port=0)
            port = http.server_port
            http.server_close()
            log = open(temp + "/server.log", "w")
            process = subprocess.Popen(
                [sys.executable, "server.py", "--port", str(port)],
                cwd=server.ROOT,
                env={**os.environ, "ATIGRA_DB": temp + "/browser.sqlite3"},
                stdout=log,
                stderr=log,
            )
            try:
                for _ in range(50):
                    try:
                        urllib.request.urlopen(
                            f"http://127.0.0.1:{port}/api/config", timeout=0.2
                        )
                        break
                    except Exception:
                        time.sleep(0.1)
                with sync_playwright() as p:
                    browser = p.chromium.launch(
                        headless=True,
                        executable_path=shutil.which("chromium"),
                        args=["--no-sandbox"],
                    )
                    page = browser.new_page(viewport={"width": 1440, "height": 1050})
                    errors = []
                    page.on("pageerror", lambda e: errors.append(str(e)))
                    page.goto(f"http://127.0.0.1:{port}")
                    # Keyboard navigation into login.
                    page.keyboard.press("Tab")
                    self.assertIn("Skip", page.locator(":focus").inner_text())
                    # Exercise the actual submit button, including recovery paths.
                    page.locator("#login-form button[type=submit]").click()
                    self.assertIn(
                        "Escribe tu usuario", page.locator("#login-error").inner_text()
                    )
                    page.locator("#login-form [name=login]").fill("nova.demo")
                    page.locator("#login-form [name=password]").fill("AtigraDemo2026!")
                    page.route("**/api/login", lambda route: route.abort())
                    page.locator("#login-form button[type=submit]").click()
                    page.wait_for_function(
                        "() => document.querySelector('#login-error').textContent.includes('No se puede conectar')"
                    )
                    self.assertTrue(
                        page.locator("#login-form button[type=submit]").is_enabled()
                    )
                    page.unroute("**/api/login")
                    page.locator("#login-form [name=password]").fill(
                        "incorrect-password"
                    )
                    page.locator("#login-form button[type=submit]").click()
                    page.wait_for_function(
                        "() => document.querySelector('#login-error').textContent.includes('incorrectos')"
                    )
                    self.assertTrue(
                        page.locator("#login-form button[type=submit]").is_enabled()
                    )
                    page.locator("#login-form [name=password]").fill("AtigraDemo2026!")
                    page.route(
                        "**/api/student",
                        lambda route: route.fulfill(
                            status=400,
                            content_type="application/json",
                            body='{"error":"invalid_input","reference":"test1234"}',
                        ),
                    )
                    page.locator("#login-form button[type=submit]").click()
                    page.wait_for_function(
                        "() => document.querySelector('#login-error').textContent.includes('La contraseña se ha aceptado')"
                    )
                    self.assertIn("test1234", page.locator("#login-error").inner_text())
                    self.assertIsNone(page.evaluate("state.user"))
                    self.assertTrue(
                        page.locator("#login-form button[type=submit]").is_enabled()
                    )
                    page.unroute("**/api/student")
                    page.locator("#login-form button[type=submit]").click()
                    page.wait_for_selector(".planet-card")
                    self.assertEqual(page.locator(".planet-card").count(), 6)
                    page.locator('[data-language="en"]').click()
                    self.assertIn("Hello", page.locator("h1").inner_text())
                    page.locator('[data-language="es"]').click()
                    for i, mode in enumerate(server.MODES, 1):
                        page.locator(f'.mission-chip[data-start="{i}"]').click()
                        page.locator("#assessed-start").click()
                        page.wait_for_selector("#type-input")
                        self.assertEqual(
                            page.locator(".scene-label").inner_text().lower(),
                            page.evaluate("t(state.game.level.mode)").lower(),
                        )
                        text = page.evaluate("state.game.level.text")
                        if i == 1:
                            page.locator("#type-input").press("x")
                            page.locator("#type-input").press("Backspace")
                            # Composition produces one normalized character, not intermediates.
                            page.locator("#type-input").evaluate(
                                """el => {
                              el.dispatchEvent(new CompositionEvent('compositionstart', {bubbles:true}));
                              el.dispatchEvent(new CompositionEvent('compositionend', {data:'ñ', bubbles:true}));
                            }"""
                            )
                            self.assertEqual(
                                page.evaluate('state.game.buffer.join("")'),
                                "ñ",
                                page.evaluate(
                                    "({paused:state.game.paused,events:state.game.events,composition:state.game.composition})"
                                ),
                            )
                            self.assertFalse(
                                page.locator("#type-input").evaluate(
                                    "el => el.dispatchEvent(new ClipboardEvent('paste', {bubbles:true,cancelable:true}))"
                                )
                            )
                            page.locator("#type-input").evaluate(
                                "el => el.dispatchEvent(new KeyboardEvent('keydown', {key:'a',repeat:true,bubbles:true,cancelable:true}))"
                            )
                            self.assertEqual(
                                page.evaluate('state.game.buffer.join("")'), "ñ"
                            )
                            page.locator("#pause-button").click()
                            self.assertTrue(page.locator("#type-input").is_disabled())
                            elapsed = page.evaluate("activeTime()")
                            page.wait_for_timeout(300)
                            self.assertLessEqual(
                                abs(page.evaluate("activeTime()") - elapsed), 2
                            )
                            page.locator("#pause-button").click()
                            page.locator("#type-input").press_sequentially(
                                text[1:], delay=200
                            )
                        else:
                            page.locator("#type-input").press_sequentially(
                                text, delay=200
                            )
                        page.wait_for_selector("#result-back", timeout=10000)
                        self.assertIn(
                            "Misión completada", page.locator("h1").inner_text()
                        )
                        if i == 1:
                            result = page.evaluate("state.game.result.attempt")
                            self.assertEqual(result["typed"], len(text) + 1)
                            self.assertLess(result["accuracy"], 100)
                        page.locator("#result-back").click()
                        page.wait_for_selector(".planet-card")
                    page.locator('[data-page="progress"]').first.click()
                    page.wait_for_selector("table")
                    self.assertIn("ñ", page.locator("body").inner_text())
                    # Persisted progress survives logout and reload.
                    page.locator('.topbar [data-action="logout"]').click()
                    page.wait_for_selector("#login-form")
                    page.reload()
                    page.locator('[data-demo="nova.demo"]').click()
                    page.wait_for_selector(".planet-card")
                    self.assertEqual(len(page.evaluate("state.student.attempts")), 6)
                    # Tablet layout avoids page-level horizontal scrolling.
                    page.set_viewport_size({"width": 768, "height": 1024})
                    self.assertLessEqual(
                        page.evaluate("document.documentElement.scrollWidth"), 768
                    )
                    page.set_viewport_size({"width": 1440, "height": 1050})
                    page.locator('.topbar [data-action="logout"]').click()
                    page.wait_for_selector("#login-form")
                    page.locator('[data-demo="profe.demo"]').click()
                    page.wait_for_selector("#create-class")
                    page.locator("#create-class").click()
                    page.locator(".modal input[name=name]").fill("Browser class")
                    page.locator(".modal button[type=submit]").click()
                    page.wait_for_selector(".modal", state="detached")
                    self.assertIn("Browser class", page.locator("body").inner_text())
                    page.locator("[data-new-student]").first.click()
                    for name, value in [
                        ("alias", "Browser Pilot"),
                        ("username", "browser.pilot"),
                        ("password", "BrowserPass2026!"),
                    ]:
                        page.locator(f".modal [name={name}]").fill(value)
                    page.locator(".modal button[type=submit]").click()
                    page.wait_for_selector(".modal", state="detached")
                    self.assertIn("Browser Pilot", page.locator("body").inner_text())
                    page.locator('[data-page="levels"]').click()
                    page.wait_for_selector("#new-level")
                    page.locator("#new-level").click()
                    page.locator(".modal [name=name]").fill("Browser mission")
                    page.locator(".modal [name=text]").fill("¡Hola, ñ!")
                    page.locator(".modal button[type=submit]").click()
                    page.wait_for_selector(".modal", state="detached")
                    self.assertIn("Browser mission", page.locator("body").inner_text())
                    page.locator('[data-page="reports"]').click()
                    page.wait_for_selector("#report-body table")
                    self.assertIn("Nova", page.locator("#report-body").inner_text())
                    with page.expect_download() as download:
                        page.locator("#export-csv").click()
                    path = download.value.path()
                    self.assertIn("Nova", Path(path).read_text())
                    page.locator('[data-language="en"]').click()
                    page.wait_for_selector("#report-body table")
                    self.assertIn("Reports", page.locator("h1").inner_text())
                    self.assertEqual(errors, [])
                    browser.close()
            finally:
                process.terminate()
                process.wait(timeout=5)
                log.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
