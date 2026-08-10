import time
import os


def read_proc(file):
    with open(f'/proc/{file}', 'r') as f:
        return f.read()


while True:
    # Читаем данные
    meminfo = read_proc('meminfo')
    loadavg = read_proc('loadavg')
    cpu_stat = read_proc('stat')

    # Обрабатываем (логируем, выводим, сохраняем)
    print(f"[{time.strftime('%H:%M:%S')}] Load: {loadavg.split()[0]}")

    # Ждем 5 секунд
    time.sleep(5)

