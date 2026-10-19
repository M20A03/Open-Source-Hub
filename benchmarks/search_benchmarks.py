"""
Linear search vs Binary search throughput benchmarks.
"""
import time, bisect

def benchmark_search(size: int = 10000):
    data = list(range(size))
    t0 = time.perf_counter()
    bisect.bisect_left(data, size // 2)
    return time.perf_counter() - t0
