import sqlite3
import bcrypt
from flask import request, g, current_app
import jwt
from utils import get_db_name, create_token


def get_user_with_credentials(email, password):
    con = None
    try:
        con = sqlite3.connect(get_db_name())
        cur = con.cursor()
        # using execute provided my squlite3 lib to prevent SQL injection attacks
        cur.execute('''
            SELECT email, name, password FROM users where email=?''',
                    (email,))
        row = cur.fetchone()

        # return None if user not found in database
        if row is None:
            return None
        email, name, hash = row
        # verifying password and returning None if incorrect
        if not bcrypt.checkpw(bytes(password, 'utf-8'), hash):
            return None
        return {"email": email, "name": name, "token": create_token(email)}
    finally:
        if con is not None:
            con.close()


def logged_in():
    token = request.cookies.get('auth_token')
    # is unauthenticated if auth_token not found
    if not token:
        return False
    try:
        # verifying the token
        data = jwt.decode(bytes(str(token), 'utf-8'),
                          current_app.config['SECRET_KEY'], algorithms=['HS256'])
        g.user = data['sub']
        return True
    # return False if token is invalid
    except jwt.InvalidTokenError:
        return False
