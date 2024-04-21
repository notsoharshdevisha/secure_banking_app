import sqlite3
from passlib.hash import pbkdf2_sha256
import random


def create_test_db() -> None:
    create_users()
    create_accounts()
    create_account_types()


def create_users() -> None:
    con: sqlite3.Connection = sqlite3.connect('test_bank.db')
    cur: sqlite3.Cursor = con.cursor()
    cur.execute('''
        CREATE TABLE users (email text primary key, name text, password text)
    ''')

    cur.execute(
        "INSERT INTO users VALUES (?, ?, ?)",
        ('alice@example.com', 'Alice Xu', pbkdf2_sha256.hash("123456")))

    cur.execute(
        "INSERT INTO users VALUES (?, ?, ?)",
        ('bob@example.com', 'Bobby Tables', pbkdf2_sha256.hash("123456")))

    con.commit()
    con.close()


def create_accounts() -> None:
    con: sqlite3.Connection = sqlite3.connect('test_bank.db')
    cur: sqlite3.Cursor = con.cursor()
    cur.execute('''
        CREATE TABLE accounts (
            id text primary key, owner text, balance integer, account_type text,
            foreign key(owner) references users(email),
            foreign key(account_type) references account_types(id)
            )
    ''')

    cur.execute(
        "INSERT INTO accounts VALUES (?, ?, ?, ?)",
        (generate_account_number(), 'alice@example.com', 7500, "a1df8500-5b1d-472b-8748-3441f118a89f"))

    cur.execute(
        "INSERT INTO accounts VALUES (?, ?, ?, ?)",
        (generate_account_number(), 'alice@example.com', 200, "391ed75a-31f5-45fc-a112-ac67e65a4891"))

    cur.execute(
        "INSERT INTO accounts VALUES (?, ?, ?, ?)",
        (generate_account_number(), 'bob@example.com', 3000, "a1df8500-5b1d-472b-8748-3441f118a89f"))

    cur.execute(
        "INSERT INTO accounts VALUES (?, ?, ?, ?)",
        (generate_account_number(), 'bob@example.com', 100, "391ed75a-31f5-45fc-a112-ac67e65a4891"))

    con.commit()
    con.close()


def generate_account_number() -> int:
    return random.randint(1000000000, 9999999999)


def create_account_types() -> None:
    con: sqlite3.Connection = sqlite3.connect("test_bank.db")
    curr: sqlite3.Cursor = con.cursor()
    curr.execute('''
        CREATE TABLE account_types (id text primary key, type text)
    ''')

    curr.execute(
        '''INSERT INTO account_types VALUES (?, ?)''',
        ("391ed75a-31f5-45fc-a112-ac67e65a4891", "checking")
    )

    curr.execute(
        '''INSERT INTO account_types VALUES (?, ?)''',
        ("a1df8500-5b1d-472b-8748-3441f118a89f", "savings")
    )

    con.commit()
    con.close()


if __name__ == "__main__":
    create_test_db()
