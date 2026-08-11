import sqlite3
import feelings

db_path = "metrics.db"

con = sqlite3.connect(db_path)
cur = con.cursor()

"""Создаем таблицу метрик с временем в которое проводился так называемый забор данных из ядра, средняя нагрузка за минуту
текущая используемая память, ну и нагрузка на сpu."""

cur.execute("CREATE TABLE IF NOT EXISTS metrics(time, load, mem, cpu)")
cur.execute("INSERT INTO ")
cur.execute("SELECT * FROM metrics")
rows = cur.fetchall()

for row in rows:
    print(row)

con.close()