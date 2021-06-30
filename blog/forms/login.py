from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class LoginForm(FlaskForm):
    email = StringField(
        "E-mail",
        [validators.DataRequired()],
    )
    password = PasswordField(
        "Password",
        [validators.DataRequired()],
    )
    submit = SubmitField("Login")