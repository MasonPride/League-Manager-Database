"""Main class for league

This class will load and display the programs gui.

Author: Mason Pride
Version: 0.1
"""
from typing import List
from src.tests.test_get_stadium_by_name import test_get_stadium_by_name
from src.tests.test_team_repo import test_team_repo
from src.tests.test_players_repo import test_players_repo
from src.tests.test_games_repo import test_games_repo
from src.tests.test_player_stats_repo import test_player_stats_repo

class Main:
    """Main Class."""

    @staticmethod
    def main(args: List[str]) -> None:
        """Main method."""
        print("Starting main")
        