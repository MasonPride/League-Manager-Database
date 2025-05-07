
from typing import Optional, List

import pyodbc

from src.data_access.RecordNotFoundException import RecordNotFoundException
from src.data_access.sql_command_executor import SqlCommandExecutor
from src.league.repositories.player_stats.i_player_stats_repo import IPlayerStatsRepo
from src.league.models.PlayerStats import PlayerStats


class SqlPlayerStatsRepo(IPlayerStatsRepo):
    def __init__(self, driver: str = "{ODBC Driver 17 for SQL Server}", server: str = "", database: str = "", trusted: bool = True):
        self.executor = SqlCommandExecutor(driver=driver, server=server, database=database, trusted=trusted)


    def save_player_stats(self, player_id: int, games_played: int, hits: int, runs: int, home_runs: int, rbi: int, strikeouts: int) -> Optional[PlayerStats]:
        # Validate inputs
        if player_id is None:
            raise ValueError("PlayerID cannot be empty.")
        if games_played is None:
            raise ValueError("Games Played cannot be empty.")
        if hits is None:
            raise ValueError("Hits cannot be empty.")
        if runs is None:
            raise ValueError("Runs cannot be empty.")
        if home_runs is None:
            raise ValueError("HomeRuns cannot be empty.")
        if rbi is None:
            raise ValueError("rbi cannot be empty.")
        if strikeouts is None:
            raise ValueError("strikouts cannot be empty.")
        
        sp_name = 'League.SavePlayerStats'
        inp_param_names = ['PlayerID', 'GamesPlayed', 'Hits', 'Runs', 'HomeRuns', 'RBI', 'Strikeouts']
        inp_param_values = [player_id, games_played, hits, runs, home_runs, rbi, strikeouts]

        self.executor.execute_stored_procedure(
            sp_name,
            input_param_names=inp_param_names,
            input_param_values=inp_param_values
        )

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

    def get_average_stats_by_position(self) -> Optional[List[dict]]:
        sp_name = 'League.GetAverageStatsByPosition'

        rows = self.executor.execute_stored_procedure(sp_name)

        if not rows:
            return None

        return [
            {
                "position": row.Position,
                "avg_runs": float(row.AvgRuns),
                "avg_home_runs": float(row.AvgHomeRuns),
                "avg_strikeouts": float(row.AvgStrikeouts)
            }
            for row in rows
        ]
        

    def translate_stats(self, row: pyodbc.Row) -> PlayerStats:
        return PlayerStats(row.PlayerStatID, row.PlayerID, row.GamesPlayed, row.Hits, row.Runs, row.HomeRuns, row.RBI, row.Strikeouts)