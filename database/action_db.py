import sqlite3


def insert_user_db(tg_id: int):
    with sqlite3.connect(r"database\users.db") as conn:
        cur = conn.cursor()

        cur.execute('''INSERT INTO users (telegram_id) VALUES (?)''',
                    (tg_id,))