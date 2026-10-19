"""
Fast binary modular exponentiation algorithm.
"""
def power_mod(base: int, exp: int, mod: int) -> int:
    res = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1: res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res
