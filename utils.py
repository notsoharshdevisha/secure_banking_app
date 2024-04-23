from flask import current_app
import jwt
from datetime import datetime, timedelta
from pytz import timezone


def get_db_name():
    return current_app.config['DB']


def create_token(email):
    now = datetime.now(timezone('US/Pacific'))
    payload = {'sub': email, 'iat': now, 'exp': now + timedelta(minutes=60)}
    token = jwt.encode(
        payload, get_secret_from_app_config(), algorithm='HS256')
    return token


def get_secret_from_app_config():
    return current_app.config['SECRET_KEY']
