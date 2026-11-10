"""Missing-input-file CLI behavior for toc.py.

Run with the stdlib runner (no new framework)::

    python -m unittest test_toc_missing_file -v

or with pytest::

    python -m pytest test_toc_missing_file.py -q
"""
import os
import subprocess
import sys
import unittest

TOC_PY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "toc.py")


class TestTocMissingFile(unittest.TestCase):
    def run_toc(self, *argv):
        return subprocess.run(
            [sys.executable, TOC_PY, *argv],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    def test_missing_file_exits_nonzero_without_traceback(self):
        proc = self.run_toc("does-not-exist-23.md")
        combined = proc.stdout + proc.stderr
        self.assertNotEqual(proc.returncode, 0)
        self.assertNotIn("Traceback", combined)

    def test_missing_file_reports_clean_error(self):
        proc = self.run_toc("does-not-exist-23.md")
        self.assertIn("does-not-exist-23.md", proc.stderr)


if __name__ == "__main__":
    unittest.main()
