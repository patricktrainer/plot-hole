from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PlotForm(FlaskForm):
    lat = StringField("Lat", validators=[DataRequired()])
    long = StringField("Long", validators=[DataRequired()])
    submit = SubmitField("Plot")
