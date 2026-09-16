import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from actions import ensure_default_config, extract_command_target, extract_search_query, normalize_query


class EnsureDefaultConfigTests(unittest.TestCase):
    def test_creates_default_config_when_missing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.ini"
            self.assertFalse(config_path.exists())

            ensure_default_config(config_path)

            self.assertTrue(config_path.exists())
            content = config_path.read_text(encoding="utf-8")
            self.assertIn("[DEFAULT]", content)
            self.assertIn("master = YourName", content)

    def test_normalizes_spoken_phrases(self):
        self.assertEqual(normalize_query("  What’s up? Please search for Python tutorials.  "), "what's up please search for python tutorials")

    def test_extracts_search_text_from_natural_language(self):
        self.assertEqual(extract_search_query("please search for Python tutorials"), "python tutorials")

    def test_extracts_target_for_web_opening(self):
        self.assertEqual(extract_command_target("open youtube now"), "youtube now")


if __name__ == "__main__":
    unittest.main()
