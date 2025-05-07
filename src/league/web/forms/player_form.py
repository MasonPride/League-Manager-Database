from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange

class PlayerForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=32)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=32)])
    number = IntegerField("Number", validators=[DataRequired(), NumberRange(min=0, max=99)])
    position = SelectField("Position", choices=[
        ('P', 'Pitcher'), ('C', 'Catcher'), ('1B', '1st Base'),
        ('2B', '2nd Base'), ('3B', '3rd Base'), ('SS', 'Shortstop'),
        ('LF', 'Left Field'), ('CF', 'Center Field'), ('RF', 'Right Field')
    ], validators=[DataRequired()])
    birthday = DateField("Birthday", format='%Y-%m-%d', validators=[DataRequired()])
    team_id = SelectField("Team", coerce=int, validators=[DataRequired()])