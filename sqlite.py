import sqlite3
import feelings
from datetime import datetime
from feelings import get_load, get_mem

db_path = "metrics.db"


def save_metrics():
    """Создаем таблицу метрик с временем в которое проводился так называемый забор данных из ядра, средняя нагрузка за минуту
    текущая используемая память, ну и нагрузка на сpu."""
    time = datetime.now().isoformat()
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS metrics(time, load, mem)")
    #Наполняем данными из скрипта feelings
    cur.execute("INSERT INTO metrics (time, load, mem) VALUES (?, ?, ?)",(time, get_load(), get_mem()))
    con.commit()
    con.close()

def load_metrics_db(metrics_db):
    """Функция отдает данные из базы"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(metrics_db)
    rows = cur.fetchall()
    con.close()
    return rows

