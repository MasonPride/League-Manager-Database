"""Main class for league

This class will load and display the programs gui.

Author: Mason Pride
Version: 0.1
"""
from typing import List
from src.tests.test_get_stadium_by_name import test_get_stadium_by_name


class Main:
    """Main Class."""

    @staticmethod
    def main(args: List[str]) -> None:
        """Main method."""
        test_get_stadium_by_name()
        