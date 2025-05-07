"""Web Controller class.

Creates the controller for our web app.

Author: Mason Pride
Version: 0.1
"""
from flask import render_template, request
from flask_classful import FlaskView, route  # type: ignore

## import from repositories
from src.league.repositories.teams.sql_teams_repo import SqlTeamsRepo
from src.league.repositories.players.sql_players_repo import SqlPlayersRepo
from src.league.repositories.player_stats.sql_player_stats_repo import SqlPlayerStatsRepo


class WebController(FlaskView):
    """WebController class."""
    route_base = "/"

    @route('/')
    def index(self):
        """Index route method.

        Defines the route for index.

        Returns:
            render template of index
        """
        return render_template("index.html")

    @route('/teams/')
    def teams(self):
        """Teams route method.

        Defines the route for teams.

        Returns:
            render template of teams
        """
        teams_repo = SqlTeamsRepo("{ODBC Driver 17 for SQL Server}", "(local)\SQLEXPRESS","DBEFinalProject", "Trusted_Connection=yes")
        teams = teams_repo.get_all_teams()
        return render_template("teams.html", teams=teams)

    @route('/teams/<id>/', methods=['GET'])
    def show_team(self, id: int):
        """Teams id route method.

        Gets the details of a specific team from id

        Returns:
            render template of team_details
        """
        teams_repo = SqlTeamsRepo("{ODBC Driver 17 for SQL Server}", "(local)\SQLEXPRESS","DBEFinalProject", "Trusted_Connection=yes")
        team = teams_repo.fetch_team(id)
        players = teams_repo.get_all_players_on_team(id)
        return render_template("team_details.html", team=team, players=players)

    @route('/players/<id>/', methods=['GET'])
    def show_player(self, id: int):
        """Players id  route method.

        Gets the details of a specific player from id

        Returns:
            render template of player_details
        """
        players_repo = SqlPlayersRepo("{ODBC Driver 17 for SQL Server}", "(local)\SQLEXPRESS","DBEFinalProject", "Trusted_Connection=yes")
        stats_repo = SqlPlayerStatsRepo("{ODBC Driver 17 for SQL Server}", "(local)\SQLEXPRESS","DBEFinalProject", "Trusted_Connection=yes")
        team_repo = SqlTeamsRepo("{ODBC Driver 17 for SQL Server}", "(local)\SQLEXPRESS","DBEFinalProject", "Trusted_Connection=yes")
        player = players_repo.fetch_player(id)
        stats = stats_repo.get_player_stats(id)
        team = team_repo.fetch_team(player.team_id)
        return render_template("player_details.html", player=player, stats=stats, team=team)