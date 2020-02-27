from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    EqualTo,
    ValidationError,
)
from plot_hole.models import User


class RegistrationForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    confirm_password = PasswordField(
        validators=[DataRequired(), EqualTo("password", "use same password!")]
    )
    submit = SubmitField()

    def validate_email(self, email):
        email = User.objects(email=email.data)
        if email:
            raise ValidationError("User already exists")


class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    # remember = BooleanField('remember')
    submit = SubmitField()
