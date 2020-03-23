"""Forms for account creation and management"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from dnd_app import app, mysql


class RegistrationForm(FlaskForm):
    """Form for registering an account"""
    ## Declare form fields and their constraints.
    username = StringField('Username', validators=
                           [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeatPassword = PasswordField('Confirm Password', validators=
                                   [DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')

    def validate_username(self, username):
        '''Determine if username to register is unique via MySQL query'''
        ## Query the database for username and store results in 'duplicate'.
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT accountName FROM account WHERE accountName=%s", (username.data,))
        duplicate = cursor.fetchone()
        cursor.close()
        if duplicate is not None:
            ## Username exists in database
            raise ValidationError('Username in use, please choose another.')
        ##Username is unique
        return

class LoginForm(FlaskForm):
    #Form to Login
    username = StringField('Username', validators=[DataRequired(), Length(min = 2, max = 20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Create Account')
