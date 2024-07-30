import asyncio
import time

import requests


async def network(i: int):
    response = requests.get("http://127.0.0.1:5000")

async def benchmark():
    tasks = []
    for i in range(10):
        tasks.append(network(i))
    await asyncio.gather(*tasks)

def run() -> int:
    start = time.time()
    asyncio.run(benchmark())
    end = time.time()
    return end - start
