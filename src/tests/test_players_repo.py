from src.league.repositories.players.sql_players_repo import SqlPlayersRepo

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server}"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=DBEFinalProject;"
    "Trusted_Connection=yes;"
)

def test_players_repo():
    repo = SqlPlayersRepo("{ODBC Driver 17 for SQL Server}", "(local)\SQLEXPRESS","DBEFinalProject", "Trusted_Connection=yes")
    """
    (print("---- Testing create_player ----"))
    repo.create_player(1, 'Jason', 'Hendrix', 33, '1999-03-11', 'C')
    player = repo.fetch_player(1)
    if player:
        print("Player id: " + str(player.player_id))
        print("Team id: " + str(player.team_id))
        print("First Name: " + player.first_name)
        print("Last Name: " + player.last_name)
        print("\n")
    else:
        print("No player found.")
    
    (print("---- Testing get_player_by_name() ----"))
    player2 = repo.get_player_by_name("Jason", "Hendrix")
    if player2:
        print("Player id: " + str(player2.player_id))
        print("Team id: " + str(player2.team_id))
        print("First Name: " + player2.first_name)
        print("Last Name: " + player2.last_name)
        print("\n")
    else:
        print("No player found.")
    """
    (print("---- Testing fetch_player() ----"))
    player3 = repo.fetch_player(200)
    if player3:
        print("Player id: " + str(player3.player_id))
        print("Team id: " + str(player3.team_id))
        print("First Name: " + player3.first_name)
        print("Last Name: " + player3.last_name)
        print("\n")
    else:
        print("No player found.")

    """
    (print("---- Testing save_player() ----"))
    repo.save_player(1, 1, "Fake First Name", "Fake Last Name", 22, "2001-04-01", "P")
    # Printing the newly changed team
    player5 = repo.fetch_player(1)
    if player5:
        print("Player id: " + str(player5.player_id))
        print("Team id: " + str(player5.team_id))
        print("First Name: " + player5.first_name)
        print("Last Name: " + player5.last_name)
        print("\n")
    else:
        print("No team found.")
    """
        