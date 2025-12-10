from datetime import datetime

import sqlite3


file = r"database\users.db"

def insert_user_db(tg_id: int):
    date = datetime.now().date()

    with sqlite3.connect(file) as conn:
        cur = conn.cursor()

        cur.execute('''INSERT INTO users (telegram_id,
                                          date) 
                                    VALUES (?, ?)''',
                    (tg_id, date))
        

def insert_subuser_db(tg_id: int):
    with sqlite3.connect(file) as conn:
        cur = conn.cursor()

        cur.execute('''UPDATE users
                       SET subscribed = 1, free_pdf_given = 1
                       WHERE telegram_id == (?)''',
                       (tg_id,))
        

def insert_paid_db(tg_id: int):
    with sqlite3.connect(file) as conn:
        cur = conn.cursor()

        cur.execute('''UPDATE users
                       SET paid_pdf_given = 1, paid = 1
                       WHERE telegram_id == (?)''',
                       (tg_id,))