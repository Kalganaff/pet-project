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
        load_1min = 0.9
        return load_1min

def get_mem():
        mem_free = int(8282882)
        return mem_free