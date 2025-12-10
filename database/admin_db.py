import sqlite3


file = r"database/admins.db"

def check_admin(tg_id: int):
    with sqlite3.connect(file) as conn:
        cur = conn.cursor()

        cur.execute('''SELECT id FROM admins 
                       WHERE admin_tg_id == (?)''',
                       (tg_id,))
        admin = cur.fetchall()
        print(admin)
        return admin