"""Implementation of benchmarks for the standard library Threading library."""

import threading
import time
import benchmark
import config


class ThreadingBenchmarks(benchmark.Benchmark):
    """Benchmarks for the Threading library."""

    def run_cpu_bound_benchmark(self) -> float:
        start = time.time()
        threads = []
        for _ in range(config.SCALE):
            thread = threading.Thread(target=benchmark.cpu_bound)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
        end = time.time()
        return end - start

    def run_io_bound_benchmark(self) -> float:
        start = time.time()
        threads = []
        for _ in range(config.SCALE):
            thread = threading.Thread(target=benchmark.network_bound)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
        end = time.time()
        return end - start
