from abc import ABC, abstractmethod
from typing import Optional, List

from src.league.models.stadiums import Stadiums


class IStadiumsRepo(ABC):
    @abstractmethod
    def fetch_stadium(self, stadium_id: int) -> Optional[Stadiums]:
        pass

    @abstractmethod
    def get_stadium_by_name(self, name: str) -> Optional[Stadiums]:
        pass