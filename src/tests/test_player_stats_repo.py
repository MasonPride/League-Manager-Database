from src.league.repositories.player_stats.sql_player_stats_repo import SqlPlayerStatsRepo
from src.league.repositories.players.sql_players_repo import SqlPlayersRepo

def test_player_stats_repo():
    stats_repo = SqlPlayerStatsRepo("{ODBC Driver 17 for SQL Server}", "(local)\SQLEXPRESS","DBEFinalProject", "Trusted_Connection=yes")
    player_repo = SqlPlayersRepo("{ODBC Driver 17 for SQL Server}", "(local)\SQLEXPRESS","DBEFinalProject", "Trusted_Connection=yes")
    player_id = 1 
    player = player_repo.fetch_player(player_id)
    stats = stats_repo.get_player_stats(player_id)
    print(f"--- Player Stats for PlayerID {player_id} ---")
    print(f"Name: {player.first_name} {player.last_name}")
    print(f"Number: {player.number}")
    print(f"Games Played: {stats.games_played}")
    print(f"Hits: {stats.hits}")
    print(f"Runs: {stats.runs}")
    print(f"Home Runs: {stats.home_runs}")
    print(f"RBIs: {stats.rbi}")
    print(f"RBIs: {stats.strikeouts}")