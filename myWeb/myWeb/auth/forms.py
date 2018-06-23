# third party import
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

# local import
from ..models import Employee

class RegistrationForm(FlaskForm):
    """
    Form For user to create new account
    """
    email=StringField('Email',validators=[DataRequired(),Email()])
    username=StringField('Username',validators=[DataRequired()])
    first_name=StringField('First Name',validators=[DataRequired()])
    last_name=StringField('Last Name',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),EqualTo('confirm_password')])
    confirm_password=PasswordField('Confirm Password')
    submit=SubmitField('Register')

    def validate_username(self,field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('UserName is already taken')

    def validate_email(self,field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already taken')



class LoginForm(FlaskForm):
    """
    Form for user to login 
    """
    email=StringField('Email',validators=[DataRequired(), Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Login')