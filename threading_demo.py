import threading
import time
import requests

def network(i: int):
    response = requests.get("http://127.0.0.1:5000")

def benchmark():
    threads = []
    for i in range(10):
        thread = threading.Thread(target=network, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def run() -> int:
    start = time.time()
    benchmark()
    end = time.time()
    return end - start
