import asyncio
import time
import aiohttp
import requests

async def cpu_bound():
    r = 100
    for i in range(r):
        for j in range(r):
            for k in range(r):
                if i + j == k:
                    continue

async def network_blocking(i: int):
    response = requests.get("http://127.0.0.1:5000")

async def network_non_blocking(i: int, session: aiohttp.ClientSession):
    async with session.get("http://127.0.0.1:5000") as response:
        await response.text()

async def benchmark_non_blocking():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            tasks.append(network_non_blocking(i, session))
        await asyncio.gather(*tasks)

async def benchmark_blocking():
    tasks = []
    for i in range(100):
        tasks.append(network_blocking(i))
    await asyncio.gather(*tasks)

async def benchmark_cpu_bound():
    tasks = []
    for i in range(10):
        tasks.append(cpu_bound())
    await asyncio.gather(*tasks)

def run_blocking() -> int:
    start = time.time()
    asyncio.run(benchmark_blocking())
    end = time.time()
    return end - start

def run_non_blocking() -> int:
    start = time.time()
    asyncio.run(benchmark_blocking())
    end = time.time()
    return end - start

def run_cpu_bound() -> int:
    start = time.time()
    asyncio.run(benchmark_cpu_bound())
    end = time.time()
    return end - start