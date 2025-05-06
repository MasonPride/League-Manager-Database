
from typing import Optional, List

import pyodbc

from src.data_access.RecordNotFoundException import RecordNotFoundException
from src.data_access.sql_command_executor import SqlCommandExecutor
from src.league.repositories.player_stats.i_player_stats_repo import IPlayerStatsRepo
from src.league.models.PlayerStats import PlayerStats


class SqlPlayerStatsRepo(IPlayerStatsRepo):
    def __init__(self, driver: str = "{ODBC Driver 17 for SQL Server}", server: str = "", database: str = "", trusted: bool = True):
        self.executor = SqlCommandExecutor(driver=driver, server=server, database=database, trusted=trusted)

    def save_player_stats(self, player_id: int) -> Optional[PlayerStats]:
        pass

    def get_player_stats(self, player_id: int) -> Optional[PlayerStats]:
        sp_name = "League.GetPlayerStats"
        inp_param_names = ['PlayerID']
        inp_param_values = [player_id]

        results = self.executor.execute_stored_procedure(sp_name,
                                                        input_param_names=inp_param_names,
                                                        input_param_values=inp_param_values)
        if len(results) == 1:
            return self.translate_stats(results[0])
        else:
            raise RecordNotFoundException(player_id)

    def translate_stats(self, row: pyodbc.Row) -> PlayerStats:
        return PlayerStats(row.PlayerStatID, row.PlayerID, row.GamesPlayed, row.Hits, row.Runs, row.HomeRuns, row.RBI)