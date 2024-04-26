import sqlite3
from utils import get_db_name


def get_balance(account_number: str, owner: str) -> None:
    con = None
    try:
        con = sqlite3.connect(get_db_name())
        cur = con.cursor()
        cur.execute('''
            SELECT balance FROM accounts where id=? and owner=?''',
                    (account_number, owner))
        row = cur.fetchone()
        if row is None:
            return None
        return row[0]
    finally:
        if con is not None:
            con.close()


def do_transfer(transaction):
    source = transaction.get_source()
    target = transaction.get_target()
    amount = transaction.get_amount()

    con = None
    try:
        con = sqlite3.connect(get_db_name())
        cur = con.cursor()
        cur.execute('''
            SELECT id FROM accounts where id=?''',
                    (target,))
        target_account = cur.fetchone()
        cur.execute('''
            SELECT id FROM accounts where id=?''',
                    (source,))
        source_account = cur.fetchone()
        if target_account is None or source_account is None:
            return False
        cur.execute('''
            UPDATE accounts SET balance=balance-? where id=?''',
                    (amount, source))
        cur.execute('''
            UPDATE accounts SET balance=balance+? where id=?''',
                    (amount, target))
        con.commit()
        return True
    finally:
        if con is not None:
            con.close()
