from abc import ABC, abstractmethod
from typing import Optional, List

from src.league.models.teams import Teams


class ITeamsRepo(ABC):
    @abstractmethod
    def fetch_team(self, team_id: int) -> Optional[Teams]:
        pass

    @abstractmethod
    def get_team_by_name(self, name: str) -> Optional[Teams]:
        pass
    
    @abstractmethod
    def save_team(self, team_id: int, stadium_id: int, name: str, city: str, founded_day: str):
        pass