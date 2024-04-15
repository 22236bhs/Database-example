import sqlite3

DATABASE = "fighters.db"

with sqlite3.connect(DATABASE) as db:
    cursor = db.cursor()
    sql = "SELECT * FROM fighter;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for data in results:
        print(data)