"""
Unit test suite for dynamic programming functions.
"""
from algorithms.dynamic_programming import fibonacci, knapsack, longest_common_subsequence

def test_fibonacci():
    assert fibonacci(0) == 0; assert fibonacci(1) == 1; assert fibonacci(10) == 55

def test_knapsack():
    assert knapsack([1, 2, 3], [10, 15, 40], 6) == 65

def test_lcs():
    assert longest_common_subsequence("abcde", "ace") == 3
