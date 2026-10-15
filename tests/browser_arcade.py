"""Real-browser checks for the 30 free challenges and animation lifecycle."""

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
class ArcadeFlow(unittest.TestCase):
    def test_variety_animation_pause_reduced_motion_and_cleanup(self):
        with tempfile.TemporaryDirectory() as temp:
            handle = server.make_server(port=0)
            port = handle.server_port
            handle.server_close()
            with open(temp + "/server.log", "w") as log:
                process = subprocess.Popen(
                    [sys.executable, "server.py", "--port", str(port)],
                    cwd=server.ROOT,
                    env={
                        **os.environ,
                        "ATIGRA_DB": temp + "/arcade.sqlite3",
                        "ATIGRA_DEMO": "1",
                    },
                    stdout=log,
                    stderr=log,
                )
                try:
                    for _ in range(80):
                        try:
                            urllib.request.urlopen(
                                f"http://127.0.0.1:{port}/api/config", timeout=0.2
                            )
                            break
                        except OSError:
                            time.sleep(0.1)
                    with sync_playwright() as p:
                        browser = p.chromium.launch(
                            headless=True,
                            executable_path=shutil.which("chromium"),
                            args=["--no-sandbox"],
                        )
                        page = browser.new_page(
                            viewport={"width": 1440, "height": 1080},
                            reduced_motion="no-preference",
                        )
                        errors = []
                        forbidden = []
                        page.on("pageerror", lambda error: errors.append(str(error)))
                        page.on(
                            "request",
                            lambda req: (
                                forbidden.append(req.url)
                                if "/api/run" in req.url or "/api/attempt" in req.url
                                else None
                            ),
                        )
                        page.goto(f"http://127.0.0.1:{port}")
                        page.wait_for_selector("#open-arcade")
                        page.locator("#open-arcade").click()
                        self.assertEqual(page.locator("[data-stage-id]").count(), 30)
                        self.assertEqual(page.locator(".arcade-card").count(), 10)
                        self.assertEqual(
                            len(
                                set(
                                    page.evaluate(
                                        "AtigraArcade.levels.map(x=>x.text.es)"
                                    )
                                )
                            ),
                            30,
                        )
                        self.assertEqual(
                            len(
                                set(
                                    page.evaluate(
                                        "AtigraArcade.levels.map(x=>x.text.en)"
                                    )
                                )
                            ),
                            30,
                        )
                        page.locator('[data-stage-id="race-2"]').click()
                        page.wait_for_selector("#type-input")
                        self.assertEqual(page.evaluate("AtigraMotion.activeLoops()"), 1)
                        page.evaluate(
                            'window.firstGlyph=document.querySelector("#typing-text span")'
                        )
                        word = page.evaluate('state.game.level.text.split(" ")[0]+" "')
                        page.locator("#type-input").press_sequentially(word, delay=35)
                        self.assertTrue(
                            page.evaluate(
                                'window.firstGlyph===document.querySelector("#typing-text span")'
                            )
                        )
                        first = page.evaluate("state.game.sceneProgress")
                        target = page.evaluate("progressRatio()")
                        page.wait_for_timeout(90)
                        second = page.evaluate("state.game.sceneProgress")
                        self.assertGreater(second, first)
                        self.assertLess(second, target)
                        self.assertTrue(
                            page.locator(".race-ship").evaluate(
                                'node=>getComputedStyle(node).transform!=="none"'
                            )
                        )
                        page.locator("#pause-button").click()
                        frozen = page.evaluate(
                            "[state.game.sceneProgress,state.game.scenePhase,activeTime()]"
                        )
                        self.assertEqual(page.evaluate("AtigraMotion.activeLoops()"), 0)
                        page.wait_for_timeout(180)
                        self.assertEqual(
                            page.evaluate(
                                "[state.game.sceneProgress,state.game.scenePhase,activeTime()]"
                            ),
                            frozen,
                        )
                        page.locator("#pause-button").click()
                        self.assertEqual(page.evaluate("AtigraMotion.activeLoops()"), 1)
                        # Motion preference is respected by JavaScript, not just CSS.
                        page.locator('[data-action="motion"]').click()
                        self.assertEqual(page.evaluate("AtigraMotion.activeLoops()"), 0)
                        page.locator("#pause-button").click()
                        next_word = page.evaluate(
                            'state.game.level.text.slice(state.game.buffer.length).split(" ")[0]+" "'
                        )
                        page.locator("#type-input").press_sequentially(
                            next_word, delay=10
                        )
                        self.assertAlmostEqual(
                            page.evaluate("state.game.sceneProgress"),
                            page.evaluate("progressRatio()"),
                            places=5,
                        )
                        self.assertEqual(page.evaluate("AtigraMotion.activeLoops()"), 0)
                        # All eighteen presets complete with the real engine, in reduced motion.
                        stages = page.evaluate(
                            "AtigraArcade.levels.map(x=>({id:x.id,mode:x.mode,tier:x.tier}))"
                        )
                        for stage in stages:
                            page.locator("#guest-library").click()
                            page.locator(
                                '[data-stage-id="' + stage["id"] + '"]'
                            ).click()
                            page.wait_for_selector("#type-input")
                            self.assertEqual(
                                page.locator("#game-scene").get_attribute("data-mode"),
                                stage["mode"],
                            )
                            self.assertEqual(
                                page.locator("#game-scene").get_attribute("data-tier"),
                                str(stage["tier"]),
                            )
                            if stage["mode"] == "bridge":
                                self.assertEqual(
                                    page.locator(".rune").count(), 2 + stage["tier"] * 4
                                )
                            if stage["mode"] == "castle":
                                self.assertEqual(
                                    page.locator(".meteor").count(), stage["tier"]
                                )
                            if stage["mode"] == "portal":
                                self.assertEqual(
                                    page.locator(".portal-ring").count(),
                                    stage["tier"] + 1,
                                )
                            text = page.evaluate("state.game.level.text")
                            page.locator("#type-input").press_sequentially(
                                text, delay=1
                            )
                            page.wait_for_selector("#result-back")
                            self.assertEqual(
                                page.evaluate("state.game.result.attempt.accuracy"), 100
                            )
                            self.assertIsNone(
                                page.evaluate("state.game.result.attempt.score")
                            )
                            self.assertEqual(
                                page.locator(
                                    ".rating-panel .bot-slot:not(.empty)"
                                ).count(),
                                5,
                            )
                            self.assertEqual(
                                page.locator(".maker-supremo").inner_text(),
                                "MAKER SUPREMO",
                            )
                            self.assertEqual(
                                page.locator(".rating-panel .bot-slot").count(), 5
                            )
                            self.assertEqual(
                                page.evaluate("AtigraMotion.activeLoops()"), 0
                            )
                        # Exact accuracy and the speed threshold both matter, even when rounded UI values look perfect.
                        for accuracy, wpm, expected_bots, supreme in [
                            (100, 10, 5, True),
                            (100, 9.999, 4, False),
                            (99.999, 10, 5, False),
                            (79, 20, 2, False),
                            (89, 20, 3, False),
                            (0, 0, 1, False),
                        ]:
                            rating = page.evaluate(
                                "([accuracy,wpm]) => resultRating({accuracy,wpm,bots:null,score:null},10)",
                                [accuracy, wpm],
                            )
                            self.assertEqual(rating["bots"], expected_bots)
                            self.assertEqual(rating["supreme"], supreme)
                        authoritative = page.evaluate(
                            "resultRating({accuracy:98,wpm:20,bots:3,score:77},10)"
                        )
                        self.assertEqual(authoritative["bots"], 3)
                        self.assertEqual(authoritative["score"], 77)
                        # Forward navigation starts the next trial and differs visually from Back.
                        page.locator("#result-back").click()
                        page.locator("#try-game").click()
                        page.locator("#type-input").press_sequentially(
                            page.evaluate("state.game.level.text"), delay=1
                        )
                        page.wait_for_selector("#result-next")
                        styles = page.evaluate(
                            "['#result-next','#result-back'].map(id => {const s=getComputedStyle(document.querySelector(id)); return [s.backgroundColor,s.fontFamily]})"
                        )
                        self.assertNotEqual(styles[0][0], styles[1][0])
                        self.assertNotEqual(styles[0][1], styles[1][1])
                        page.locator("#result-next").click()
                        page.wait_for_selector("#type-input")
                        self.assertEqual(
                            page.evaluate("state.game.level.stage_id"), "castle-2"
                        )
                        page.locator("#type-input").press_sequentially(
                            page.evaluate("state.game.level.text"), delay=1
                        )
                        page.wait_for_selector("#result-back")
                        # Restore the last stage for repeat/language checks.
                        page.evaluate("startGuestGame('portal-3','es')")
                        page.locator("#type-input").press_sequentially(
                            page.evaluate("state.game.level.text"), delay=1
                        )
                        page.wait_for_selector("#result-back")
                        # Repeating preserves the chosen mission, including after a UI language switch.
                        page.locator('[data-language="en"]').click()
                        page.locator("#result-repeat").click()
                        page.wait_for_selector("#type-input")
                        self.assertEqual(
                            page.evaluate("state.game.level.stage_id"), "portal-3"
                        )
                        self.assertEqual(
                            page.evaluate("state.game.level.language"), "es"
                        )
                        self.assertEqual(page.evaluate("state.game.buffer.length"), 0)
                        page.set_viewport_size({"width": 768, "height": 1024})
                        self.assertLessEqual(
                            page.evaluate("document.documentElement.scrollWidth"), 768
                        )
                        # A system preference change must also stop JS animation.
                        page.locator('[data-action="motion"]').click()
                        page.emulate_media(reduced_motion="reduce")
                        page.wait_for_function(
                            "() => document.querySelector('#game-scene').classList.contains('scene-reduced')"
                        )
                        self.assertEqual(page.evaluate("AtigraMotion.activeLoops()"), 0)
                        page.locator("#pause-button").click()
                        self.assertEqual(page.evaluate("AtigraMotion.activeLoops()"), 0)
                        page.emulate_media(reduced_motion="no-preference")
                        page.wait_for_function("() => AtigraMotion.activeLoops() === 1")
                        page.locator("#guest-library").click()
                        self.assertLessEqual(
                            page.evaluate("document.documentElement.scrollWidth"), 768
                        )
                        page.locator(".modal-close").click()
                        page.once("dialog", lambda dialog: dialog.accept())
                        page.locator("#guest-exit").click()
                        page.wait_for_selector("#login-form")
                        self.assertEqual(page.evaluate("AtigraMotion.activeLoops()"), 0)
                        self.assertEqual(forbidden, [])
                        import sqlite3

                        with sqlite3.connect(temp + "/arcade.sqlite3") as db:
                            self.assertEqual(
                                db.execute("SELECT COUNT(*) FROM attempts").fetchone()[
                                    0
                                ],
                                0,
                            )
                            self.assertEqual(
                                db.execute("SELECT COUNT(*) FROM runs").fetchone()[0], 0
                            )
                            self.assertEqual(
                                db.execute("SELECT COUNT(*) FROM levels").fetchone()[0],
                                96,
                            )
                        self.assertEqual(errors, [])
                        browser.close()
                finally:
                    process.terminate()
                    process.wait(timeout=5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
