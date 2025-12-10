import sqlite3
import pandas as pd

def create_excel_dumpfile():
    folder_bd = r"database/users.db"
    folder_excel = r"bot/admin_files/dump_files/orders.xlsx"

    conn = sqlite3.connect(folder_bd)

    query = '''SELECT telegram_id, date
                    FROM users
                    WHERE paid == 1'''

    df = pd.read_sql_query(query, conn)
    conn.close()
    df.to_excel(folder_excel, index=False)

    return folder_excel