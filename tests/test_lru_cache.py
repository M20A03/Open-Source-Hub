"""
Unit test suite for LRU cache decorator.
"""
from utils.lru_cache import simple_lru

def test_lru():
    calls = 0
    @simple_lru(2)
    def compute(x):
        nonlocal calls; calls += 1; return x * 2
    assert compute(2) == 4; assert compute(2) == 4; assert calls == 1
