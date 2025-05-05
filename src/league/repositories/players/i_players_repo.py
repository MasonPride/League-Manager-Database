from abc import ABC, abstractmethod
from typing import Optional, List

from src.league.models.players import Players


class IPlayersRepo(ABC):
    @abstractmethod
    def fetch_player(self, player_id: int) -> Optional[Players]:
        pass

    @abstractmethod
    def get_player_by_name(self, first_name: str, last_name: str) -> Optional[Players]:
        pass
    
    @abstractmethod
    def create_player(self, team_id: int, first_name: str, last_name: str, number: int, birthday: str, position: str):
        pass
