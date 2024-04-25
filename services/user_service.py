import sqlite3
import bcrypt
from flask import request, g, current_app
import jwt
from utils import get_db_name, create_token

SECRET = 'bfg28y7efg238re7r6t32gfo23vfy7237yibdyo238do2v3'


def get_user_with_credentials(email, password):
    con = None
    try:
        con = sqlite3.connect(get_db_name())
        cur = con.cursor()
        cur.execute('''
            SELECT email, name, password FROM users where email=?''',
                    (email,))
        row = cur.fetchone()
        if row is None:
            return None
        email, name, hash = row
        if not bcrypt.checkpw(bytes(password, 'utf-8'), hash):
            return None
        return {"email": email, "name": name, "token": create_token(email)}
    finally:
        if con is not None:
            con.close()


def logged_in():
    token = request.cookies.get('auth_token')
    if not token:
        return False
    try:
        data = jwt.decode(bytes(str(token), 'utf-8'),
                          current_app.config['SECRET_KEY'], algorithms=['HS256'])
        g.user = data['sub']
        return True
    except jwt.InvalidTokenError:
        return False
