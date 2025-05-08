from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired, NumberRange
from wtforms.widgets import NumberInput

class TeamStatsForm(FlaskForm):
    wins = IntegerField("Wins", validators=[InputRequired(), NumberRange(min=0)])
    losses = IntegerField("Losses", validators=[InputRequired(), NumberRange(min=0)])
    runs_scored = IntegerField("Runs Scored", validators=[InputRequired(), NumberRange(min=0)])
    runs_allowed = IntegerField("Runs Allowed", validators=[InputRequired(), NumberRange(min=0)])
    games_played = IntegerField("Games Played", validators=[InputRequired(), NumberRange(min=0)])

