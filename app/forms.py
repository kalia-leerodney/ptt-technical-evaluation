from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired,Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class RegisterForm(FlaskForm):
    firstname = StringField('First Name', validators=[InputRequired()])
    lastname = StringField('Last Name', validators=[InputRequired(),Email()])
    email = StringField('Email', validators=[InputRequired()])
    currencyone = StringField('Currency One', validators=[InputRequired()])
    currencytwo = StringField('Currency Two', validators=[InputRequired()])

class CurrencyForm(FlaskForm):
    currencynameone = StringField('Currency One', validators=[InputRequired()])
    currencyoneamount = StringField('Amount', validators=[InputRequired()])
    currencynametwo = StringField('Currency Two', validators=[InputRequired()])

