"""Demo different Concurrency libraries"""
import argparse
import asyncio_demo
import multiprocessing_demo
import threading_demo

def main():
    """Launch benchmarks and print results
    """

    parser = argparse.ArgumentParser(description="Choose Concurrency library to benchmark")

    parser.add_argument("--asyncio", action="store_true", help="Use Asyncio")
    parser.add_argument("--threading", action="store_true", help="Use Threading")
    parser.add_argument("--multiprocessing", action="store_true", help="Use Multiprocessing")

    args = parser.parse_args()

    benchmark_results = {
        "cpu": [],
        "network": []
    }

    if args.asyncio:
        asyncio_results_blocking = asyncio_demo.run_blocking()
        benchmark_results["network"].append(("asyncio_blocking", asyncio_results_blocking))

        asyncio_results_non_blocking = asyncio_demo.run_non_blocking()
        benchmark_results["network"].append(("asyncio_non_blocking", asyncio_results_non_blocking))

        asyncio_results_cpu = asyncio_demo.run_cpu_bound()
        benchmark_results["cpu"].append(("asyncio_cpu", asyncio_results_cpu))

    if args.multiprocessing:
        mp_results = multiprocessing_demo.run()
        benchmark_results["network"].append(("multiprocessing", mp_results))

        mp_results_cpu = multiprocessing_demo.run_cpu_bound()
        benchmark_results["cpu"].append(("multiprocessing_cpu", mp_results_cpu))

    if args.threading:
        threading_results = threading_demo.run()
        benchmark_results["network"].append(("threading", threading_results))

        threading_results_cpu = threading_demo.run_cpu_bound()
        benchmark_results["cpu"].append(("threading_cpu", threading_results_cpu))

    for test, results in benchmark_results.items():
        print(f"{test} bounded benchmarks:")
        for variation, result in results:
            print(f"    {variation}: {result}")
if __name__ == '__main__':
    main()
