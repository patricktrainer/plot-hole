from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired


class PlotForm(FlaskForm):
    lat = FloatField("Lat", validators=[DataRequired()])
    long = FloatField("Long", validators=[DataRequired()])
    submit = SubmitField("Plot")
