"""Implementation of benchmarks for the standard library Asyncio library."""

import asyncio
import time
import aiohttp
import config
import benchmark


class AsyncioBenchmark(benchmark.Benchmark):
    """Benchmarks for the Asyncio library."""

    def run_cpu_bound_benchmark(self) -> float:
        start = time.time()
        asyncio.run(self.__run_async_cpu_bound_benchmark())
        end = time.time()
        return end - start

    def run_io_bound_benchmark(self) -> float:
        start = time.time()
        asyncio.run(self.__run_async_io_bound_benchmark())
        end = time.time()
        return end - start

    def run_io_bound_blocking_benchmark(self) -> float:
        """Same as normal I/O bound, but using the standard
        eventloop blocking request library instead of the
        asyncio specific library.
        """
        start = time.time()
        asyncio.run(self.__run_async_io_bound_blocking_benchmark())
        end = time.time()
        return end - start

    async def __run_async_cpu_bound_benchmark(self):
        """Asyncio version of the CPU bound benchmarks based on scale."""
        tasks = []
        for _ in range(config.SCALE):
            tasks.append(benchmark.async_cpu_bound())
        await asyncio.gather(*tasks)

    async def __run_async_io_bound_benchmark(self):
        """Async version of the I/O bound benchmarks using non-blocking aiohttp session."""
        tasks = []
        async with aiohttp.ClientSession() as session:
            for _ in range(config.SCALE):
                tasks.append(benchmark.async_network_bound(session))
            await asyncio.gather(*tasks)

    async def __run_async_io_bound_blocking_benchmark(self):
        """Async version of the I/O bound benchmarks using blocking standard request."""
        tasks = []
        for _ in range(config.SCALE):
            tasks.append(benchmark.async_blocking_network_bound())
        await asyncio.gather(*tasks)
