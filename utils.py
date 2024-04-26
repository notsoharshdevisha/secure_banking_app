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


class Transaction:
    def __init__(self, source: str, target: str, amount: str):
        # checking if is valid account number
        if not source or len(source) != 10 or not source.isdigit():
            raise Exception("Bad arguments")

        # checking if is valid account number
        if not target or len(target) != 10 or not target.isdigit():
            raise Exception("Bad arguments")

        # validating amount to be transferred
        if not amount or not amount.isdigit() or int(amount) > 1000:
            raise Exception("Bad arguments")

        # cannot transfer to self
        if source == target:
            raise Exception("Bad arguments")

        self._source = source
        self._target = target
        self._amount = int(amount)

    def get_source(self) -> str:
        return self._source

    def get_target(self) -> str:
        return self._target

    def get_amount(self) -> int:
        return self._amount
