"""Demo different Concurrency libraries"""

import argparse
import asyncio_benchmarks
import multiprocessing_benchmarks
import threading_benchmarks


def main():
    """Launch benchmarks and print results"""

    parser = argparse.ArgumentParser(
        description="Choose Concurrency library to benchmark"
    )

    parser.add_argument("--asyncio", action="store_true", help="Use Asyncio")
    parser.add_argument("--threading", action="store_true", help="Use Threading")
    parser.add_argument(
        "--multiprocessing", action="store_true", help="Use Multiprocessing"
    )

    args = parser.parse_args()

    benchmark_results = {"cpu": [], "network": []}

    if args.asyncio:
        async_io = asyncio_benchmarks.AsyncioBenchmark()

        benchmark_results["network"].append(
            ("asyncio_non_blocking", async_io.run_io_bound_benchmark())
        )

        benchmark_results["network"].append(
            ("asyncio_blocking", async_io.run_io_bound_blocking_benchmark())
        )

        benchmark_results["cpu"].append(
            ("asyncio_cpu", async_io.run_cpu_bound_benchmark())
        )

    if args.multiprocessing:
        mp = multiprocessing_benchmarks.MultiprocessingBenchmarks()
        benchmark_results["network"].append(
            ("multiprocessing", mp.run_io_bound_benchmark())
        )

        benchmark_results["cpu"].append(
            ("multiprocessing_cpu", mp.run_cpu_bound_benchmark())
        )

    if args.threading:
        threading = threading_benchmarks.ThreadingBenchmarks()

        benchmark_results["network"].append(
            ("threading", threading.run_io_bound_benchmark())
        )
        benchmark_results["cpu"].append(
            ("threading_cpu", threading.run_cpu_bound_benchmark())
        )

    for test, results in benchmark_results.items():
        print(f"{test} bounded benchmarks:")
        for variation, result in results:
            print(f"    {variation}: {result}")


if __name__ == "__main__":
    main()
