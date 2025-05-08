
from typing import Optional, List

import pyodbc

from dotenv import load_dotenv
import os
load_dotenv() 

from src.data_access.RecordNotFoundException import RecordNotFoundException
from src.data_access.sql_command_executor import SqlCommandExecutor
from src.league.repositories.teams.i_teams_repo import ITeamsRepo
from src.league.models.teams import Teams
from src.league.models.players import Players


class SqlTeamsRepo(ITeamsRepo):
    def __init__(self, driver: str = str(os.getenv("DRIVER")), server: str = str(os.getenv("SERVER")), database: str = str(os.getenv("DATABASE")), trusted: bool = True):
        self.executor = SqlCommandExecutor(driver=driver, server=server, database=database, trusted=trusted)
        
    def fetch_team(self, team_id: int) -> Optional[Teams]:
            sp_name = "League.FetchTeam"
            inp_param_names = ['TeamID']
            inp_param_values = [team_id]

            results = self.executor.execute_stored_procedure(sp_name,
                                                            input_param_names=inp_param_names,
                                                            input_param_values=inp_param_values)
            if len(results) == 1:
                return self.translate_team(results[0])
            else:
                raise RecordNotFoundException(team_id)
            
    def get_all_teams(self) -> Optional[List[Teams]]:
        sp_name = "League.GetAllTeams"
        results = self.executor.execute_stored_procedure(sp_name)

        if len(results) >= 1:
            return self.translate_teams(results)
        else:
            return None

    def get_team_by_name(self, name: str) -> Optional[Teams]:
        sp_name = "League.GetTeamByName"
        inp_param_names = ['Name']
        inp_param_values = [name]

        results = self.executor.execute_stored_procedure(sp_name,
                                                        input_param_names=inp_param_names,
                                                        input_param_values=inp_param_values)
        if len(results) == 1:
            return self.translate_team(results[0])
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
        
    def get_all_players_on_team(self, team_id: int) -> Optional[List[Players]]:
        sp_name = "League.GetAllPlayersOnTeam"
        inp_param_names = ['TeamID']
        inp_param_values = [team_id]

        results = self.executor.execute_stored_procedure(sp_name,
                                                        input_param_names=inp_param_names,
                                                        input_param_values=inp_param_values)

        if len(results) >= 1:
            return self.translate_players(results)
        else:
            return None

    def translate_team(self, row: pyodbc.Row) -> Teams:
        return Teams(row.TeamID, row.StadiumID, row.Name, row.City, row.FoundedDay)
    
    def translate_teams(self, rows: List[pyodbc.Row]) -> List[Teams]:
        teams = []
        for row in rows:
            teams.append(self.translate_team(row))
        return teams
    
    def translate_player(self, row: pyodbc.Row) -> Players:
        return Players(row.PlayerID, row.TeamID, row.FirstName, row.LastName, row.Number, row.Birthday, row.Position)

    def translate_players(self, rows: List[pyodbc.Row]) -> List[Players]:
        players = []
        for row in rows:
            players.append(self.translate_player(row))
        return players