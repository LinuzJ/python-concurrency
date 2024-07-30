
import multiprocessing
import time

import requests


def network(i: int):
    response = requests.get("http://127.0.0.1:5000")

def benchmark():
    with multiprocessing.Pool(10) as p:
        p.map(network, range(10))

def run() -> int:
    start = time.time()
    benchmark()
    end = time.time()
    return end - start
