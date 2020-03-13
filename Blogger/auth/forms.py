from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, EqualTo, InputRequired, ValidationError

from Blogger.users.models import User


class LoginForm(FlaskForm):
    email = EmailField('Email', [InputRequired(), Email()])
    password = PasswordField('Password', [InputRequired()])
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    name = StringField('Name', [InputRequired()])
    email = EmailField('Email', [InputRequired(), Email()])
    password = PasswordField('Password', [InputRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     [InputRequired(), EqualTo('password', message="Passwords do not match")])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.find_user_by_email(email.data)
        if user:
            raise ValidationError('That email is already taken. Please use a different one.')
