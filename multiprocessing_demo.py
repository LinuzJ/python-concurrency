
import multiprocessing
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
    with multiprocessing.Pool(10) as p:
        p.map(network, range(100))

def benchmark_cpu_bound():
    with multiprocessing.Pool(10) as p:
        p.map(cpu_bound, range(10))

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