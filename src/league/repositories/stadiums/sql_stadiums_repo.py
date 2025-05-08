
from typing import Optional, List

import pyodbc


from dotenv import load_dotenv
import os
load_dotenv() 

from src.data_access.RecordNotFoundException import RecordNotFoundException
from src.data_access.sql_command_executor import SqlCommandExecutor
from src.league.repositories.stadiums.i_stadiums_repo import IStadiumsRepo
from src.league.models.stadiums import Stadiums


class SqlStadiumsRepo(IStadiumsRepo):
    def __init__(self, driver: str = str(os.getenv("DRIVER")), server: str = str(os.getenv("SERVER")), database: str = str(os.getenv("DATABASE")), trusted: bool = True):
        self.executor = SqlCommandExecutor(driver=driver, server=server, database=database, trusted=trusted)
        
    def fetch_stadium(self, stadium_id: int) -> Optional[Stadiums]:
            sp_name = "League.FetchStadium"
            inp_param_names = ['StadiumID']
            inp_param_values = [stadium_id]

            results = self.executor.execute_stored_procedure(sp_name,
                                                            input_param_names=inp_param_names,
                                                            input_param_values=inp_param_values)
            if len(results) == 1:
                return self.translate_stadiums(results[0])
            else:
                raise RecordNotFoundException(stadium_id)

    def get_stadium_by_name(self, name: str) -> Optional[Stadiums]:
        sp_name = "League.GetStadiumByName"
        inp_param_names = ['Name']
        inp_param_values = [name]

        results = self.executor.execute_stored_procedure(sp_name,
                                                        input_param_names=inp_param_names,
                                                        input_param_values=inp_param_values)
        if len(results) == 1:
            return self.translate_stadium(results[0])
        else:
            return None

    def get_all_stadiums(self) -> Optional[List[Stadiums]]:
        sp_name = "League.GetAllStadiums"
        results = self.executor.execute_stored_procedure(sp_name)

        if len(results) >= 1:
            return self.translate_stadiums(results)
        else:
            return None



    def translate_stadium(self, row: pyodbc.Row) -> Stadiums:
        return Stadiums(row.StadiumID, row.Name, row.Capacity, row.City)

    def translate_stadiums(self, rows: List[pyodbc.Row]) -> List[Stadiums]:
        stadiums = []
        for row in rows:
            stadiums.append(self.translate_stadium(row))
        return stadiums