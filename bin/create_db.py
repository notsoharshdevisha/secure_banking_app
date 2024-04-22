import sqlite3
import bcrypt

con = sqlite3.connect('bank.db')
cur = con.cursor()
cur.execute('''
    CREATE TABLE users (
        email text primary key, name text, password text)''')
cur.execute(
    "INSERT INTO users VALUES (?, ?, ?)",
    ('alice@example.com', 'Alice Xu', bcrypt.hashpw(b"123456", bcrypt.gensalt())))
cur.execute(
    "INSERT INTO users VALUES (?, ?, ?)",
    ('bob@example.com', 'Bobby Tables', bcrypt.hashpw(b"123456", bcrypt.gensalt())))
con.commit()
con.close()
