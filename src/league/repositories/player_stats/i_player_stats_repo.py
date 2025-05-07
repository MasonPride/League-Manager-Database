from abc import ABC, abstractmethod
from typing import Optional, List

from src.league.models.PlayerStats import PlayerStats


class IPlayerStatsRepo(ABC):
    @abstractmethod
    def save_player_stats(self, player_id: int, games_played: int, hits: int, runs: int, home_runs: int, rbi: int, strikeouts: int) -> Optional[PlayerStats]:
        pass

    @abstractmethod
    def get_player_stats(self, player_id: int) -> Optional[PlayerStats]:
        pass

    @abstractmethod
    def get_average_stats_by_position(self) -> List[dict]:
        pass