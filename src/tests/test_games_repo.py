from src.league.repositories.games.sql_games_repo import SqlGamesRepo

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server}"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=DBEFinalProject;"
    "Trusted_Connection=yes;"
)

def test_games_repo():
    repo = SqlGamesRepo("{ODBC Driver 17 for SQL Server}", "(local)\SQLEXPRESS","DBEFinalProject", "Trusted_Connection=yes")
    (print("---- Testing create_game ----"))
    repo.create_game(1, 2, 7, '2025-03-11')

    (print("---- Testing fetch_game() ----"))
    game = repo.fetch_game(1)
    if game:
        print("Game id: " + str(game.game_id))
        print("Home Team id: " + str(game.home_team_id))
        print("Away Team id: " + str(game.away_team_id))
        print("Stadium ID: " + str(game.stadium_id))
        print("Home Score: " + str(game.home_score))
        print("Away Score: " + str(game.away_score))
        print("Game Date: " + str(game.game_date))
        print("\n")
    else:
        print("No player found.")
        
        
    (print("---- Testing save_game() ----"))
    repo.save_game(1, 1, 2, 7, 3, 7, "1900-01-01")
    game = repo.fetch_game(1)
    if game:
        print("Game id: " + str(game.game_id))
        print("Home Team id: " + str(game.home_team_id))
        print("Away Team id: " + str(game.away_team_id))
        print("Stadium ID: " + str(game.stadium_id))
        print("Home Score: " + str(game.home_score))
        print("Away Score: " + str(game.away_score))
        print("Game Date: " + str(game.game_date))
        print("\n")
    else:
        print("No player found.")