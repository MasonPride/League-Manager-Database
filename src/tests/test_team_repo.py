from src.league.repositories.teams.sql_teams_repo import SqlTeamsRepo

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server}"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=DBEFinalProject;"
    "Trusted_Connection=yes;"
)

def test_team_repo():
    repo = SqlTeamsRepo("{ODBC Driver 17 for SQL Server}", "(local)\SQLEXPRESS","DBEFinalProject", "Trusted_Connection=yes")
    
    '''
    (print("---- Testing fetch_team() ----"))
    team = repo.fetch_team(1)
    if team:
        print("Team id: " + str(team.stadium_id))
        print("Stadium id: " + str(team.stadium_id))
        print("Name: " + team.name)
        print("City: " + team.city)
        print("Founded " + str(team.founded_day))
        print("\n")
    else:
        print("No team found.")
        
    (print("---- Testing get_team_by_name() ----"))
    team = repo.get_team_by_name("Arizona Diamondbacks")
    if team:
        print("Team id: " + str(team.stadium_id))
        print("Stadium id: " + str(team.stadium_id))
        print("Name: " + team.name)
        print("City: " + team.city)
        print("Founded " + str(team.founded_day))
        print("\n")
    else:
        print("No team found.")
        
    (print("---- Testing save_team() ----"))
    repo.save_team(1, 1, "TEST NAME CHANGE", "TEST CITY CHANGE", "1900-01-01")
    
    # Printing the newly changed team
    team = repo.fetch_team(1)
    if team:
        print("Team id: " + str(team.stadium_id))
        print("Stadium id: " + str(team.stadium_id))
        print("Name: " + team.name)
        print("City: " + team.city)
        print("Founded " + str(team.founded_day))
        print("\n")
    else:
        print("No team found.")
        
    #Set the changed info back
    repo.save_team(1, 1, "Arizona Diamondbacks", "Phoenix", "1998-01-01")
    '''
    """
    teams = repo.get_all_teams()
    for team in teams:
        print("--- Team ---")
        print("Team id: " + str(team.stadium_id))
        print("Stadium id: " + str(team.stadium_id))
        print("Name: " + team.name)
        print("City: " + team.city)
        print("Founded " + str(team.founded_day))
        print("\n")
    else:
        print("No team found.")
    """
    
    
    ## Test get all players on a team
    team = repo.get_team_by_name("Arizona Diamondbacks")
    print("--- Get All Players From: " + team.name)
    players = repo.get_all_players_on_team(team.team_id)
    i = 1
    for player in players:
        print(str(i) + ".")
        print("Player id: " + str(player.player_id))
        print("First Name: " + player.first_name)
        print("Last Name: " + player.last_name)
        i+=1
        print("\n")