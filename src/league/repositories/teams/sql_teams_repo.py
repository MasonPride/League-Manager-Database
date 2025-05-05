
from typing import Optional, List

import pyodbc

from src.data_access.RecordNotFoundException import RecordNotFoundException
from src.data_access.sql_command_executor import SqlCommandExecutor
from src.league.repositories.teams.i_teams_repo import ITeamsRepo
from src.league.models.teams import Teams


class SqlTeamsRepo(ITeamsRepo):
    def __init__(self, driver: str = "{ODBC Driver 17 for SQL Server}", server: str = "", database: str = "", trusted: bool = True):
        self.executor = SqlCommandExecutor(driver=driver, server=server, database=database, trusted=trusted)
        
    def fetch_team(self, team_id: int) -> Optional[Teams]:
            sp_name = "League.FetchTeam"
            inp_param_names = ['TeamID']
            inp_param_values = [team_id]

            results = self.executor.execute_stored_procedure(sp_name,
                                                            input_param_names=inp_param_names,
                                                            input_param_values=inp_param_values)
            if len(results) == 1:
                return self.translate_teams(results[0])
            else:
                raise RecordNotFoundException(team_id)

    def get_team_by_name(self, name: str) -> Optional[Teams]:
        sp_name = "League.GetTeamByName"
        inp_param_names = ['Name']
        inp_param_values = [name]

        results = self.executor.execute_stored_procedure(sp_name,
                                                        input_param_names=inp_param_names,
                                                        input_param_values=inp_param_values)
        if len(results) == 1:
            return self.translate_teams(results[0])
        else:
            return None

    def save_team(self, team_id: int, stadium_id: int, name: str, city: str, founded_day: str):
        # verify parameters
        if name is None:
            raise ValueError("Name cannot be empty.")
        if city is None:
            raise ValueError("City cannot be empty.")
        if founded_day is None:
            raise ValueError("founded_daycannot be empty.")

        sp_name = 'League.SaveTeam'
        inp_param_names = ['TeamID', 'StadiumID', 'Name', 'City', 'FoundedDay']
        inp_param_values = [team_id, stadium_id, name, city, founded_day]
        rows = self.executor.execute_stored_procedure(sp_name,
                                                      input_param_names=inp_param_names,
                                                      input_param_values=inp_param_values)

    def translate_teams(self, row: pyodbc.Row) -> Teams:
        return Teams(row.TeamID, row.StadiumID, row.Name, row.City, row.FoundedDay)