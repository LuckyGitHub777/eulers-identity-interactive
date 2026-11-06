import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
class StaticExperienceTests(unittest.TestCase):
    def test_pages_present(self):
        for name in ("index.html","matrix.html","phase.html"):
            with self.subTest(name=name):
                self.assertIn("<html",(ROOT/name).read_text(encoding="utf-8").lower())
    def test_local_assets(self):
        for name in ("app.js","styles.css","favicon.svg","modules/unit-circle.js"):
            self.assertTrue((ROOT/name).is_file())
    def test_no_remote_runtime_scripts(self):
        import re
        for name in ("index.html","matrix.html","phase.html"):
            page=(ROOT/name).read_text(encoding="utf-8")
            self.assertIsNone(re.search(r'<script[^>]+src=["\']https?://',page,re.I))
