import sqlite3
import time
import os

def get_load():
    with open(f'/proc/loadavg', 'r') as f:
        data = f.read().split()
        load_1min = float(data[0])
        print(load_1min)
        return load_1min

def get_mem():
    with open(f'/proc/meminfo', 'r') as f:
        data = f.read()
        mem_free = None

        for line in data.split('\n'):
            if 'MemFree' in line:
                mem_free = int(line.split()[1])
        return mem_free

def get_cpu():
    with open(f'/proc/stat', 'r') as f:
        return f.read()

print(get_load())
print(get_mem())