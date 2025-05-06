
from typing import Optional, List

import pyodbc

from src.data_access.RecordNotFoundException import RecordNotFoundException
from src.data_access.sql_command_executor import SqlCommandExecutor
from src.league.repositories.games.i_games_repo import IGamesRepo
from src.league.models.games import Games


class SqlGamesRepo(IGamesRepo):
    def __init__(self, driver: str = "{ODBC Driver 17 for SQL Server}", server: str = "", database: str = "", trusted: bool = True):
        self.executor = SqlCommandExecutor(driver=driver, server=server, database=database, trusted=trusted)

    def create_game(self, home_team_id: int, away_team_id: int, stadium_id: int, game_date: str) -> Optional[Games]:
        # verify parameters
        if home_team_id is None:
            raise ValueError("Home Team cannot be empty.")
        if away_team_id is None:
            raise ValueError("Away Team cannot be empty.")
        if stadium_id is None:
            raise ValueError("Stadium_id cannot be empty.")
        if game_date is None:
            raise ValueError("GameDate cannot be empty.")

        sp_name = "League.CreateGame"
        inp_param_names = ['HomeTeamID', 'AwayTeamID', 'StadiumID', 'GameDate']
        inp_param_values = [home_team_id, away_team_id, stadium_id, game_date]
        out_param = {
            'sp_local': ['GameID'],
            'sp_local_types': ['int'],
            'sp_out': ["GameID"],
        }

        results = self.executor.execute_stored_procedure(sp_name,
                                                         input_param_names=inp_param_names,
                                                         input_param_values=inp_param_values,
                                                         output_param=out_param)
        if len(results) == 1:
            return Games(results[0].GameID_var, home_team_id, away_team_id, stadium_id, game_date)
        else:
            return None
        
    def fetch_game(self, game_id: int) -> Optional[Games]:
        sp_name = "League.FetchGame"
        inp_param_names = ['GameID']
        inp_param_values = [game_id]

        results = self.executor.execute_stored_procedure(sp_name,
                                                        input_param_names=inp_param_names,
                                                        input_param_values=inp_param_values)
        if len(results) == 1:
            return self.translate_games(results[0])
        else:
            raise RecordNotFoundException(team_id)
    
    def save_game(self, game_id: int, home_team_id: int, away_team_id: int, stadium_id: int, home_score: int, away_score: int, game_date: str):
        # verify parameters
        if home_team_id is None:
            raise ValueError("Home Team cannot be empty.")
        if away_team_id is None:
            raise ValueError("Away Team cannot be empty.")
        if stadium_id is None:
            raise ValueError("Stadium_id cannot be empty.")
        if game_date is None:
            raise ValueError("GameDate cannot be empty.")

        sp_name = "League.SaveGame"
        inp_param_names = ['GameID', 'HomeTeamID', 'AwayTeamID', 'StadiumID', 'GameDate', 'HomeScore', 'AwayScore']
        inp_param_values = [game_id, home_team_id, away_team_id, stadium_id, game_date, home_score, away_score]
        rows = self.executor.execute_stored_procedure(sp_name,
                                                      input_param_names=inp_param_names,
                                                      input_param_values=inp_param_values)
        
    def translate_games(self, row: pyodbc.Row) -> Games:
        return Games(row.GameID, row.HomeTeamID, row.AwayTeamID, row.StadiumID, row.GameDate, row.HomeScore, row.AwayScore) 
    
    