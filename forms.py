from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class LoginForm(FlaskForm):
    email = EmailField("Email:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])


class TransferForm(FlaskForm):
    from_field = StringField("From", validators=[DataRequired()])
    to_field = StringField("To", validators=[DataRequired()])
    amount = IntegerField("Amount", validators=[
                          DataRequired(), NumberRange(min=1, max=1000)])
