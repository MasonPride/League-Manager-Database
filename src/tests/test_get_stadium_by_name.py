from src.league.repositories.stadiums.sql_stadiums_repo import SqlStadiumsRepo

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server}"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=DBEFinalProject;"
    "Trusted_Connection=yes;"
)

def test_get_stadium_by_name():
    repo = SqlStadiumsRepo("{ODBC Driver 17 for SQL Server}", "(local)\SQLEXPRESS","DBEFinalProject", "Trusted_Connection=yes")
    stadiums = repo.get_stadium_by_name("Wrigley Field")

    if stadiums:
        print("Stadium id: " + str(stadiums.stadium_id))
        print("Name: " + stadiums.name)
        print("Capacity: " + str(stadiums.capacity))
        print("City " + stadiums.city)
    else:
        print("No stadium found.")
