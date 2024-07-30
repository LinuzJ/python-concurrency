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

    benchmark_results = []

    if args.asyncio:
        asyncio_results = asyncio_demo.run()
        benchmark_results.append(("asyncio", asyncio_results))

    if args.multiprocessing:
        mp_results = multiprocessing_demo.run()
        benchmark_results.append(("multiprocessing", mp_results))

    if args.threading:
        threading_results = threading_demo.run()
        benchmark_results.append(("threading", threading_results))

    for variation, result in benchmark_results:
        print(f"{variation}: {result} seconds")

if __name__ == '__main__':
    main()
