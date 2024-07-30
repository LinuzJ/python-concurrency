import threading
import time
import requests

def cpu_bound(_i: int):
    r = 100
    for i in range(r):
        for j in range(r):
            for k in range(r):
                if i + j == k:
                    continue

def network(i: int):
    response = requests.get("http://127.0.0.1:5000")

def benchmark():
    threads = []
    for i in range(100):
        thread = threading.Thread(target=network, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def benchmark_cpu_bound():
    threads = []
    for i in range(10):
        thread = threading.Thread(target=cpu_bound, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def run() -> int:
    start = time.time()
    benchmark()
    end = time.time()
    return end - start

def run_cpu_bound() -> int:
    start = time.time()
    benchmark_cpu_bound()
    end = time.time()
    return end - start