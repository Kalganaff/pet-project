import random

def get_load1():
    with open(f'/proc/loadavg', 'r') as f:
        data = f.read().split()
        load_1min = float(data[0])
        return load_1min

def get_mem1():
    with open(f'/proc/meminfo', 'r') as f:
        data = f.read()
        mem_free = None
        for line in data.split('\n'):
            if 'MemFree' in line:
                mem_free = int(line.split()[1])
        return mem_free

def get_load():
    # Генерируем нагрузку от 0.1 до 5.0 с разными значениями
    return round(random.uniform(0.1, 5.0), 2)

def get_mem():
    # Генерируем память от 8 млн до 12 млн с разными значениями
    return random.randint(8000000, 12000000)