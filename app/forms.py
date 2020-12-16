from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationFrom(FlaskForm):
    username = StringField('Username',
                           validators=[Length(min=4, max=25,
                                              message='Це поле має бути між 4 та 25 символів'),
                                       DataRequired(message="Це обов'язкове поле")])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[Length(min=6,
                                                message='Це поле має бути більше 6-ти символів'),
                                         DataRequired(message="Це обов'язкове поле")])
    confirm_password = PasswordField('Confirm password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')