import io
import unittest
from unittest.mock import patch

import src.stdio.dialog as script


class TestHello(unittest.TestCase):
    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_main_yes(self, mock_stdout, mock_stdin):
        script.main()
        self.assertEqual(
            "Welcome to Mincong's demo\nThanks for confirmation\n",
            mock_stdout.getvalue(),
        )

    @patch("builtins.input", side_effect=["n"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_main_no(self, mock_stdout, mock_stdin):
        script.main()
        self.assertEqual(
            "Welcome to Mincong's demo\nSorry to see you go\n", mock_stdout.getvalue()
        )
