from abc import ABC, abstractmethod
from typing import Optional, List

from src.league.models.PlayerStats import PlayerStats


class IPlayerStatsRepo(ABC):
    @abstractmethod
    def save_player_stats(self, player_id: int) -> Optional[PlayerStats]:
        pass

    @abstractmethod
    def get_player_stats(self, player_id: int) -> Optional[PlayerStats]:
        pass

    @abstractmethod
    def get_average_stats_by_position(self) -> List[dict]:
        pass