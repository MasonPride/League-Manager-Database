from abc import ABC, abstractmethod
from typing import Optional, List

from src.league.models.TeamStats import TeamStats


class ITeamStatsRepo(ABC):
    @abstractmethod
    def save_team_stats(self, team_id: int, games_played: int, hits: int, runs: int, home_runs: int, rbi: int, strikeouts: int) -> Optional[TeamStats]:
        pass

    @abstractmethod
    def get_team_stats(self, team_id: int) -> Optional[TeamStats]:
        pass
