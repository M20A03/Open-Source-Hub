"""
Sorting performance comparison between Timsort, Heapsort, and MergeSort.
"""
import time, random

def benchmark_sorting(size: int = 5000):
    data = [random.randint(0, 100000) for _ in range(size)]
    t0 = time.perf_counter()
    sorted(data)
    return time.perf_counter() - t0
