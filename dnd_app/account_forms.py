"""Forms for account creation and management"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    """Form for registering an account"""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeatPassword = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Create Account')