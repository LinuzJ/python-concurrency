"""Implementation of benchmarks for the standard library Multiprocessing library."""

import multiprocessing
import time
import benchmark
import config


class MultiprocessingBenchmarks(benchmark.Benchmark):
    """Benchmarks for the Multiprocessing library."""

    def __init__(self):
        self.cpu_count = multiprocessing.cpu_count()

    def run_cpu_bound_benchmark(self) -> float:
        start = time.time()

        with multiprocessing.Pool(processes=self.cpu_count) as p:
            p.starmap(benchmark.cpu_bound, [() for _ in range(config.SCALE)])

        end = time.time()
        return end - start

    def run_io_bound_benchmark(self) -> float:
        start = time.time()

        with multiprocessing.Pool(processes=self.cpu_count) as p:
            p.starmap(benchmark.network_bound, [() for _ in range(config.SCALE)])

        end = time.time()
        return end - start
