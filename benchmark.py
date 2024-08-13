"""Contains common functions and general class for benchmarks."""

import abc
import requests
import config
import aiohttp


def cpu_bound():
    """Useless CPU bound function."""
    r = config.SCALE * 10
    for i in range(r):
        for j in range(r):
            for k in range(r):
                if i + j == k:
                    continue


def network_bound():
    """Useless I/O bound function calling the local server."""
    _response = requests.get(config.LOCAL_TEST_SERVER, timeout=100000)


async def async_cpu_bound():
    """Even more useless Async wrapper for the CPU bounded function."""
    cpu_bound()


async def async_blocking_network_bound():
    """Even more useless async wrapper of the I/O bound function calling the local server."""
    _response = requests.get(config.LOCAL_TEST_SERVER, timeout=100000)


async def async_network_bound(session: aiohttp.ClientSession):
    """Useless async I/O bound function calling the local server using
    the non-eventloop-blocking aiohttp session.
    """
    async with session.get(config.LOCAL_TEST_SERVER) as response:
        await response.text()


class Benchmark(abc.ABC):
    """Abstract class for benchmarks."""

    @abc.abstractmethod
    def run_cpu_bound_benchmark(self) -> float:
        """CPU bound benchmarks based on scale.

        Returns:
            Time it took to complete in seconds.
        """
        pass

    @abc.abstractmethod
    def run_io_bound_benchmark(self) -> float:
        """I/O bound benchmarks based on scale.

        Returns:
            Time it took to complete in seconds.
        """
        pass
