from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from plot_hole.models import User


class RegistrationForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    confirm_password = PasswordField(
        validators=[DataRequired(), EqualTo("password", "use same password!")]
    )
    submit = SubmitField()

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("User already exists")

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("User already exists")


class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    # remember = BooleanField('remember')
    submit = SubmitField()


class PlotForm(FlaskForm):
    lat = StringField("Lat", validators=[DataRequired()])
    long = StringField("Long", validators=[DataRequired()])
    submit = SubmitField("Plot")
