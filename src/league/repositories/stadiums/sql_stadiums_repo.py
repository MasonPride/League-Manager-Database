
from typing import Optional, List

import pyodbc

from src.data_access.RecordNotFoundException import RecordNotFoundException
from src.data_access.sql_command_executor import SqlCommandExecutor
from src.league.repositories.stadiums.i_stadiums_repo import IStadiumsRepo
from src.league.models.stadiums import Stadiums


class SqlStadiumsRepo(IStadiumsRepo):
    def __init__(self, driver: str = "{ODBC Driver 17 for SQL Server}", server: str = "", database: str = "", trusted: bool = True):
        self.executor = SqlCommandExecutor(driver=driver, server=server, database=database, trusted=trusted)
        
    def fetch_stadium(self, person_id: int) -> Optional[Stadiums]:
            sp_name = "League.FetchStadium"
            inp_param_names = ['StadiumID']
            inp_param_values = [stadium_id]

            results = self.executor.execute_stored_procedure(sp_name,
                                                            input_param_names=inp_param_names,
                                                            input_param_values=inp_param_values)
            if len(results) == 1:
                return self.translate_stadiums(results[0])
            else:
                raise RecordNotFoundException(person_id)

    def get_stadium_by_name(self, name: str) -> Optional[Stadiums]:
        sp_name = "League.GetStadiumByName"
        inp_param_names = ['Name']
        inp_param_values = [name]

        results = self.executor.execute_stored_procedure(sp_name,
                                                        input_param_names=inp_param_names,
                                                        input_param_values=inp_param_values)
        if len(results) == 1:
            return self.translate_stadiums(results[0])
        else:
            return None



    def translate_stadiums(self, row: pyodbc.Row) -> Stadiums:
        return Stadiums(row.StadiumID, row.Name, row.Capacity, row.City)