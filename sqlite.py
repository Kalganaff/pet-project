import sqlite3
import feelings
from datetime import datetime

from feelings import get_load, get_mem

db_path = "metrics.db"
time = datetime.now()
con = sqlite3.connect(db_path)
cur = con.cursor()

"""Создаем таблицу метрик с временем в которое проводился так называемый забор данных из ядра, средняя нагрузка за минуту
текущая используемая память, ну и нагрузка на сpu."""

cur.execute("CREATE TABLE IF NOT EXISTS metrics(time, load, mem)")
cur.execute(
            "INSERT INTO metrics (time, load, mem) VALUES (?, ?, ?)",
            (time, get_load(), get_mem())
)

con.commit()

cur.execute("SELECT * FROM metrics")
rows = cur.fetchall()

for row in rows:
    print(row)

con.close()