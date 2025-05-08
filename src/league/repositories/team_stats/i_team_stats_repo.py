from abc import ABC, abstractmethod
from typing import Optional, List

from src.league.models.TeamStats import TeamStats


class ITeamStatsRepo(ABC):
    @abstractmethod
    def save_team_stats(self, team_id: int, wins: int, losses: int, runs_scored: int, runs_allowed: int, games_played: int) -> Optional[TeamStats]:
        pass

    @abstractmethod
    def get_team_stats(self, team_id: int) -> Optional[TeamStats]:
        pass
