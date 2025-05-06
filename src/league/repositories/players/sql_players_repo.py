
from typing import Optional, List

import pyodbc

from src.data_access.RecordNotFoundException import RecordNotFoundException
from src.data_access.sql_command_executor import SqlCommandExecutor
from src.league.repositories.players.i_players_repo import IPlayersRepo
from src.league.models.players import Players


class SqlPlayersRepo(IPlayersRepo):
    def __init__(self, driver: str = "{ODBC Driver 17 for SQL Server}", server: str = "", database: str = "", trusted: bool = True):
        self.executor = SqlCommandExecutor(driver=driver, server=server, database=database, trusted=trusted)


    def create_player(self, team_id: int, first_name: str, last_name: str, number: int, birthday: str, position: str) -> Optional[Players]:
        # verify parameters
        if first_name is None:
            raise ValueError("Name cannot be empty.")
        if last_name is None:
            raise ValueError("Name cannot be empty.")
        if number is None:
            raise ValueError("Number cannot be empty.")
        if birthday is None:
            raise ValueError("Birthday cannot be empty.")
        if position is None:
            raise ValueError("Position cannot be empty.")

        sp_name = "League.CreatePlayer"
        inp_param_names = ['TeamID', 'FirstName', 'LastName', 'Number', 'Birthday', 'Position']
        inp_param_values = [team_id, first_name, last_name, number, birthday, position]
        out_param = {
            'sp_local': ['PlayerID'],
            'sp_local_types': ['int'],
            'sp_out': ["PlayerID"],
        }

        results = self.executor.execute_stored_procedure(sp_name,
                                                         input_param_names=inp_param_names,
                                                         input_param_values=inp_param_values,
                                                         output_param=out_param)
        if len(results) == 1:
            return Players(results[0].PlayerID_var, team_id, first_name, last_name, number, birthday, position)
        else:
            return None
        
    def fetch_player(self, player_id: int) -> Optional[Players]:
            sp_name = "League.FetchPlayer"
            inp_param_names = ['PlayerID']
            inp_param_values = [player_id]

            results = self.executor.execute_stored_procedure(sp_name,
                                                            input_param_names=inp_param_names,
                                                            input_param_values=inp_param_values)
            if len(results) == 1:
                return self.translate_players(results[0])
            else:
                raise RecordNotFoundException(team_id)

    def get_player_by_name(self, first_name: str, last_name: str) -> Optional[Players]:
        sp_name = "League.GetPlayerByName"
        inp_param_names = ['FirstName', 'LastName']
        inp_param_values = [first_name, last_name]

        results = self.executor.execute_stored_procedure(sp_name,
                                                        input_param_names=inp_param_names,
                                                        input_param_values=inp_param_values)
        if len(results) == 1:
            return self.translate_players(results[0])
        else:
            return None

    def save_player(self, player_id: int, team_id: int, first_name: str, last_name: str, number: int, birthday: str, position: str):
        # verify parameters
        if first_name is None:
            raise ValueError("Name cannot be empty.")
        if last_name is None:
            raise ValueError("Name cannot be empty.")
        if number is None:
            raise ValueError("Number cannot be empty.")
        if birthday is None:
            raise ValueError("Birthday cannot be empty.")
        if position is None:
            raise ValueError("Position cannot be empty.")

        sp_name = 'League.SavePlayer'
        inp_param_names = ['PlayerID', 'TeamID', 'FirstName', 'LastName', 'Number', 'Birthday', 'Position']
        inp_param_values = [player_id, team_id, first_name, last_name, number, birthday, position]
        rows = self.executor.execute_stored_procedure(sp_name,
                                                      input_param_names=inp_param_names,
                                                      input_param_values=inp_param_values)

    def translate_players(self, row: pyodbc.Row) -> Players:
        return Players(row.PlayerID, row.TeamID, row.FirstName, row.LastName, row.Number, row.Birthday, row.Position)