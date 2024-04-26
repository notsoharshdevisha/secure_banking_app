from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class LoginForm(FlaskForm):
    email = EmailField("Email:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])


class TransferForm(FlaskForm):
    source = StringField("From", validators=[DataRequired()])
    target = StringField("To", validators=[DataRequired()])
    amount = IntegerField("Amount", validators=[
                          DataRequired(), NumberRange(min=1, max=1000)])
