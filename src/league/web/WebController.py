"""Web Controller class.

Creates the controller for our web app.

Author: Mason Pride
Version: 0.1
"""
from flask import render_template, request, redirect
from flask_classful import FlaskView, route  # type: ignore

## import from repositories
from src.league.repositories.teams.sql_teams_repo import SqlTeamsRepo
from src.league.repositories.players.sql_players_repo import SqlPlayersRepo
from src.league.repositories.player_stats.sql_player_stats_repo import SqlPlayerStatsRepo

## import forms
from src.league.web.forms.player_form import PlayerForm
from src.league.web.forms.player_stats_form import PlayerStatsForm


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
        stats_repo = SqlPlayerStatsRepo("{ODBC Driver 17 for SQL Server}", "(local)\\SQLEXPRESS", "DBEFinalProject", "Trusted_Connection=yes")
        averages = stats_repo.get_average_stats_by_position()
        return render_template("index.html", averages=averages)

    @route('/teams/')
    def teams(self):
        """Teams route method.

        Defines the route for teams.

        Returns:
            render template of teams
        """
        teams_repo = SqlTeamsRepo()
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

    @route('/player/<int:id>/edit', methods=['GET'])
    def edit_player(self, id: int):
        players_repo = SqlPlayersRepo("{ODBC Driver 17 for SQL Server}", "(local)\SQLEXPRESS","DBEFinalProject", "Trusted_Connection=yes")
        team_repo = SqlTeamsRepo("{ODBC Driver 17 for SQL Server}", "(local)\SQLEXPRESS","DBEFinalProject", "Trusted_Connection=yes")
        
        player = players_repo.fetch_player(id)
        form = PlayerForm(obj=player)

        teams = team_repo.get_all_teams()
        form.team_id.choices = [(team.team_id, team.name) for team in teams]

        return render_template("edit_player.html", form=form, player=player)

    @route('/player/<int:id>/edit', methods=['POST'])
    def edit_player_save(self, id: int):
        players_repo = SqlPlayersRepo("{ODBC Driver 17 for SQL Server}", "(local)\SQLEXPRESS","DBEFinalProject", "Trusted_Connection=yes")
        team_repo = SqlTeamsRepo("{ODBC Driver 17 for SQL Server}", "(local)\SQLEXPRESS","DBEFinalProject", "Trusted_Connection=yes")
        form = PlayerForm(request.form)
        
        teams = team_repo.get_all_teams()
        form.team_id.choices = [(team.team_id, team.name) for team in teams]

        if form.validate_on_submit():
            players_repo.save_player(
                player_id=id,
                team_id=form.team_id.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                number=form.number.data,
                birthday=form.birthday.data.strftime('%Y-%m-%d'),
                position=form.position.data
            )
            return redirect(f"/players/{id}/")
        
        player = players_repo.fetch_player(id)
        return render_template("edit_player.html", form=form, player=player)

    
    @route('/player/<int:id>/stats/edit', methods=['GET'])
    def edit_player_stats(self, id: int):
        players_repo = SqlPlayersRepo("{ODBC Driver 17 for SQL Server}", "(local)\SQLEXPRESS","DBEFinalProject", "Trusted_Connection=yes")
        stats_repo = SqlPlayerStatsRepo("{ODBC Driver 17 for SQL Server}", "(local)\SQLEXPRESS","DBEFinalProject", "Trusted_Connection=yes")
        player = players_repo.fetch_player(id)
        stats = stats_repo.get_player_stats(id)

        form = PlayerStatsForm(obj=stats)

        return render_template("player_stat_details.html", form=form, player=player)


    @route('/player/<int:id>/stats/edit', methods=['POST'])
    def edit_player_stats_save(self, id: int):
        players_repo = SqlPlayersRepo("{ODBC Driver 17 for SQL Server}", "(local)\\SQLEXPRESS", "DBEFinalProject", "Trusted_Connection=yes")
        stats_repo = SqlPlayerStatsRepo("{ODBC Driver 17 for SQL Server}", "(local)\\SQLEXPRESS", "DBEFinalProject", "Trusted_Connection=yes")

        form = PlayerStatsForm(request.form)

        if form.validate_on_submit():
            stats_repo.save_player_stats(
                player_id=id,
                games_played=form.games_played.data,
                hits=form.hits.data,
                runs=form.runs.data,
                home_runs=form.home_runs.data,
                rbi=form.rbi.data,
                strikeouts=form.strikeouts.data
            )
            return redirect(f"/players/{id}/")

        player = players_repo.fetch_player(id)
        return render_template("player_stat_details.html", form=form, player=player)