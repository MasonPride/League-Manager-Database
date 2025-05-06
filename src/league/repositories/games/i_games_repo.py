from abc import ABC, abstractmethod
from typing import Optional, List

from src.league.models.games import Games


class IGamesRepo(ABC):
    @abstractmethod
    def fetch_game(self, game_id: int) -> Optional[Games]:
        pass
    
    @abstractmethod
    def create_game(self, home_team_id: int, away_team_id: int, stadium_id: int, game_date: str):
        pass

    @abstractmethod
    def save_game(self, home_team_id: int, away_team_id: int, stadium_id: int, home_score: int, away_score: int, game_date: str):
        pass
