import sqlite3


def check_user_db(tg_id: int):
    with sqlite3.connect(r"database\users.db") as conn:
        cur = conn.cursor()

        cur.execute('''SELECT id FROM users WHERE telegram_id == (?)''',
                    (tg_id,))
        result = cur.fetchall()

        return result