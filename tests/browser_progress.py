"""Interactive decisions, persistent arcade progress, restart and teacher reports."""

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
    sync_playwright and shutil.which("chromium"), "Playwright and Chromium required"
)
class ProgressFlow(unittest.TestCase):
    def test_decisions_saved_progress_restart_and_teacher_reports(self):
        with tempfile.TemporaryDirectory() as temp:
            handle = server.make_server(port=0)
            port = handle.server_port
            handle.server_close()
            base = f"http://127.0.0.1:{port}"
            processes = []
            log = open(temp + "/server.log", "w")

            def start():
                process = subprocess.Popen(
                    [sys.executable, "server.py", "--port", str(port)],
                    cwd=server.ROOT,
                    env={
                        **os.environ,
                        "ATIGRA_DB": temp + "/progress.sqlite3",
                        "ATIGRA_DEMO": "1",
                    },
                    stdout=log,
                    stderr=log,
                )
                processes.append(process)
                for _ in range(80):
                    try:
                        urllib.request.urlopen(base + "/api/config", timeout=0.2)
                        return process
                    except OSError:
                        time.sleep(0.1)
                self.fail("Server failed to start")

            try:
                process = start()
                with sync_playwright() as p:
                    browser = p.chromium.launch(
                        headless=True,
                        executable_path=shutil.which("chromium"),
                        args=["--no-sandbox"],
                    )
                    page = browser.new_page(
                        viewport={"width": 1280, "height": 1000},
                        reduced_motion="no-preference",
                    )
                    errors = []
                    page.on("pageerror", lambda error: errors.append(str(error)))
                    page.on("dialog", lambda dialog: dialog.accept())

                    def choose(expected, correct=True):
                        for button in page.locator(".decision-choice").all():
                            if (
                                button.get_attribute("data-choice") == expected
                            ) == correct:
                                button.click()
                                return
                        self.fail("No matching choice button")

                    page.goto(base)
                    page.locator("#open-arcade").click()
                    page.locator('[data-stage-id="reaction-1"]').click()
                    page.wait_for_selector(".decision-choice")
                    expected = page.evaluate("state.game.level.text[0]")
                    # Select by the actual choice value to avoid matching unrelated labels.
                    choose(expected, False)
                    self.assertEqual(page.evaluate("state.game.buffer.length"), 0)
                    self.assertEqual(page.evaluate("localStats().accuracy"), 0)
                    self.assertIn(
                        "error", page.locator("#decision-feedback").inner_text()
                    )
                    choose(expected)
                    self.assertEqual(page.evaluate("state.game.buffer.length"), 1)
                    page.locator("#pause-button").click()
                    self.assertEqual(
                        page.locator(".decision-choice:disabled").count(), 3
                    )
                    phase = page.evaluate("state.game.scenePhase")
                    page.wait_for_timeout(180)
                    self.assertEqual(page.evaluate("state.game.scenePhase"), phase)
                    page.locator("#pause-button").click()
                    self.assertEqual(
                        page.locator(".decision-choice:enabled").count(), 3
                    )
                    page.screenshot(path="/tmp/atigra-reaction.png", full_page=True)
                    page.locator("#type-input").press_sequentially(
                        page.evaluate("state.game.level.text.slice(1)"), delay=150
                    )
                    page.wait_for_selector("#result-back")
                    self.assertEqual(page.locator(".maker-supremo").count(), 0)
                    page.locator("#guest-library").click()
                    page.locator('[data-stage-id="rockets-2"]').click()
                    self.assertEqual(page.locator(".incoming-rocket").count(), 2)
                    first = page.locator(".incoming-rocket").first.evaluate(
                        "el=>getComputedStyle(el).transform"
                    )
                    page.wait_for_timeout(180)
                    self.assertNotEqual(
                        first,
                        page.locator(".incoming-rocket").first.evaluate(
                            "el=>getComputedStyle(el).transform"
                        ),
                    )
                    original = page.locator(".dodge-bot").evaluate(
                        "el=>getComputedStyle(el).transform"
                    )
                    expected = page.evaluate("state.game.level.text[0]")
                    choose(expected)
                    page.wait_for_timeout(180)
                    self.assertNotEqual(
                        original,
                        page.locator(".dodge-bot").evaluate(
                            "el=>getComputedStyle(el).transform"
                        ),
                    )
                    page.screenshot(path="/tmp/atigra-rockets.png", full_page=True)
                    page.set_viewport_size({"width": 375, "height": 812})
                    self.assertLessEqual(
                        page.evaluate("document.documentElement.scrollWidth"), 375
                    )
                    page.locator("#guest-exit").click()
                    page.set_viewport_size({"width": 1280, "height": 1000})
                    page.locator('[data-demo="nova.demo"]').click()
                    page.wait_for_selector(".planet-card")
                    saved = []
                    for mode in ("rockets", "reaction", "collect", "platforms"):
                        page.locator("[data-arcade]").click()
                        self.assertIn(
                            "se guarda", page.locator(".modal .notice").inner_text()
                        )
                        page.locator('[data-stage-id="' + mode + '-1"]').click()
                        page.wait_for_selector("#type-input")
                        self.assertFalse(page.evaluate("!!state.game.guest"))
                        self.assertEqual(
                            page.locator("#game-scene").get_attribute("data-tier"), "1"
                        )
                        text = page.evaluate("state.game.level.text")
                        if mode in ("collect", "platforms"):
                            page.screenshot(
                                path="/tmp/atigra-" + mode + ".png", full_page=True
                            )
                        if mode == "reaction":
                            choose(text[0], False)
                            for char in text:
                                page.wait_for_timeout(160)
                                choose(char)
                        else:
                            page.locator("#type-input").press_sequentially(
                                text, delay=150
                            )
                        page.wait_for_selector("#result-back")
                        self.assertIn(
                            "Resultado guardado", page.locator(".result").inner_text()
                        )
                        result = page.evaluate("state.game.result.attempt")
                        self.assertEqual(result["practice"], 1)
                        self.assertIsNone(result["score"])
                        self.assertIn(result["feedback_bots"], range(1, 6))
                        if mode == "reaction":
                            self.assertLess(result["accuracy"], 100)
                            self.assertEqual(result["maker_supremo"], 0)
                        saved.append(result["id"])
                        page.locator("#result-back").click()
                        page.wait_for_selector("[data-arcade]")
                    self.assertEqual(len(page.evaluate("state.student.attempts")), 4)
                    page.locator("[data-arcade]").click()
                    self.assertEqual(page.locator(".stage-history").count(), 4)
                    page.screenshot(
                        path="/tmp/atigra-saved-progress.png", full_page=True
                    )
                    page.locator(".modal-close").click()
                    page.locator('[data-page="progress"]').first.click()
                    page.wait_for_selector("table")
                    self.assertIn(
                        "Progreso de práctica",
                        page.locator(".practice-progress").inner_text(),
                    )
                    self.assertEqual(
                        page.locator(".practice-progress .chart-bar").count(), 8
                    )
                    self.assertIn("Tres señales", page.locator("body").inner_text())
                    page.locator('.topbar [data-action="logout"]').click()
                    page.locator('[data-demo="profe.demo"]').click()
                    page.wait_for_selector("#create-class")
                    page.locator('[data-page="reports"]').click()
                    page.wait_for_selector("#report-body table")
                    self.assertIn(
                        "Progreso de práctica",
                        page.locator("#report-body").inner_text(),
                    )
                    rows = page.request.get(base + "/api/reports").json()
                    self.assertEqual([r["id"] for r in rows], list(reversed(saved)))
                    with page.expect_download() as download:
                        page.locator("#export-csv").click()
                    csv = Path(download.value.path()).read_text()
                    self.assertIn("feedback_bots", csv)
                    self.assertIn("Nova", csv)
                    # Restart the real server and keep the same SQLite file and browser session.
                    process.terminate()
                    process.wait(timeout=5)
                    process = start()
                    page.reload()
                    page.wait_for_selector("#create-class")
                    page.locator('[data-page="reports"]').click()
                    page.wait_for_selector("#report-body table")
                    self.assertEqual(
                        page.request.get(base + "/api/reports").json(), rows
                    )
                    self.assertEqual(errors, [])
                    browser.close()
            finally:
                for process in processes:
                    if process.poll() is None:
                        process.terminate()
                        process.wait(timeout=5)
                log.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
