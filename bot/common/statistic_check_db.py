import os
import sqlite3

import matplotlib.pyplot as plt


def analys_users_db():
    file = r"database/users.db"

    year_list = [year for year in range(2025, 2028)]
    month_list = [month for month in range(1, 13)]

    years = []
    people = []

    with sqlite3.connect(file) as conn:
        cur = conn.cursor()
        for year in year_list:
            for month in month_list:
                cur.execute('''SELECT id 
                            FROM users 
                            WHERE date LIKE ?
                            ORDER BY date ASC''',
                            (f"{year}-{month:02d}%",))
                
                a = cur.fetchall()
                if a:
                    years.append(f"{year}-{month:02d}")
                    people.append(len(a))

    return years, people


def quantity_files():
    folder = r"bot/admin_files/statistics_image"
    quantity = len([f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))])

    return quantity

def create_statistics():
    result_analys = analys_users_db()
    quantity = quantity_files()

    dates = result_analys[0]
    counts = result_analys[1]

    folder = fr"bot/admin_files/statistics_image/chart{quantity+1}.png"

    plt.figure(figsize=(8,4))
    plt.plot(dates, counts, marker='o', linewidth=2)
    plt.title("Количество новых пользователей по дням")
    plt.xlabel("Дата")
    plt.ylabel("Пользователи")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(folder)

    return folder