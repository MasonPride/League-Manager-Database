
from typing import Optional, List

import pyodbc

from dotenv import load_dotenv
import os

load_dotenv() 

from src.data_access.RecordNotFoundException import RecordNotFoundException
from src.data_access.sql_command_executor import SqlCommandExecutor
from src.league.repositories.team_stats.i_team_stats_repo import ITeamStatsRepo
from src.league.models.TeamStats import TeamStats


class SqlTeamStatsRepo(ITeamStatsRepo):
    def __init__(self, driver: str = str(os.getenv("DRIVER")), server: str = str(os.getenv("SERVER")), database: str = str(os.getenv("DATABASE")), trusted: bool = True):
        self.executor = SqlCommandExecutor(driver=driver, server=server, database=database, trusted=trusted)


    def save_team_stats(self, team_id: int, wins: int, losses: int, runs_scored: int, runs_allowed: int, games_played: int) -> Optional[TeamStats]:
        # Validate inputs
        if team_id is None:
            raise ValueError("PlayerID cannot be empty.")
        if games_played is None:
            raise ValueError("Games Played cannot be empty.")
        if wins is None:
            raise ValueError("Wins cannot be empty.")
        if losses is None:
            raise ValueError("Losses cannot be empty.")
        if runs_scored is None:
            raise ValueError("Run Scored cannot be empty.")
        if runs_allowed is None:
            raise ValueError("Runs Allowed cannot be empty.")
        
        sp_name = 'League.SaveTeamStats'
        inp_param_names = ['TeamID', 'Wins', 'Losses', 'RunsScored', 'RunsAllowed', 'GamesPlayed']
        inp_param_values = [team_id, wins, losses, runs_scored, runs_allowed, games_played,]

        self.executor.execute_stored_procedure(
            sp_name,
            input_param_names=inp_param_names,
            input_param_values=inp_param_values
        )

    def get_team_stats(self, team_id: int) -> Optional[TeamStats]:
        sp_name = "League.GetTeamStats"
        inp_param_names = ['TeamID']
        inp_param_values = [team_id]

        results = self.executor.execute_stored_procedure(sp_name,
                                                        input_param_names=inp_param_names,
                                                        input_param_values=inp_param_values)
        if len(results) == 1:
            return self.translate_stats(results[0])
        else:
            raise RecordNotFoundException(team_id)


    def translate_stats(self, row: pyodbc.Row) -> TeamStats:
        return TeamStats(row.TeamStatID, row.TeamID, row.Wins, row.Losses, row.RunsScored, row.RunsAllowed, row.GamesPlayed)