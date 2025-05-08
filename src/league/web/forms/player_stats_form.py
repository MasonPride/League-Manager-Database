from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired, NumberRange
from wtforms.widgets import NumberInput

class PlayerStatsForm(FlaskForm):
    games_played = IntegerField("Games Played", validators=[InputRequired(), NumberRange(min=0)], widget=NumberInput())
    hits = IntegerField("Hits", validators=[InputRequired(), NumberRange(min=0)], widget=NumberInput())
    runs = IntegerField("Runs", validators=[InputRequired(), NumberRange(min=0)], widget=NumberInput())
    home_runs = IntegerField("Home Runs", validators=[InputRequired(), NumberRange(min=0)], widget=NumberInput())
    rbi = IntegerField("RBI's", validators=[InputRequired(), NumberRange(min=0)], widget=NumberInput())
    strikeouts = IntegerField("Strikeouts", validators=[InputRequired(), NumberRange(min=0)], widget=NumberInput())
