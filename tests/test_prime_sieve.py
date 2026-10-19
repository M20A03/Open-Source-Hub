"""
Unit test suite for Prime Sieve.
"""
from math.prime_sieve import sieve_of_eratosthenes

def test_sieve():
    primes = sieve_of_eratosthenes(20)
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19]
