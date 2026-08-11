import sqlite3
import time
import os

def get_load():
    with open(f'/proc/loadavg', 'r') as f:
        data = f.read().split()
        print(data)
        return f.read()

def get_mem():
    with open(f'/proc/meminfo', 'r') as f:
        return f.read()

def get_cpu():
    with open(f'/proc/stat', 'r') as f:
        return f.read()

print(get_load())