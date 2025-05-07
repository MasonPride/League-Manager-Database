from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets import NumberInput

class PlayerStatsForm(FlaskForm):
    games_played = IntegerField("Games Played", validators=[DataRequired(), NumberRange(min=0)], widget=NumberInput())
    hits = IntegerField("Hits", validators=[DataRequired(), NumberRange(min=0)], widget=NumberInput())
    runs = IntegerField("Runs", validators=[DataRequired(), NumberRange(min=0)], widget=NumberInput())
    home_runs = IntegerField("Home Runs", validators=[DataRequired(), NumberRange(min=0)], widget=NumberInput())
    rbi = IntegerField("RBI's", validators=[DataRequired(), NumberRange(min=0)], widget=NumberInput())
    strikeouts = IntegerField("Strikeouts", validators=[DataRequired(), NumberRange(min=0)], widget=NumberInput())
