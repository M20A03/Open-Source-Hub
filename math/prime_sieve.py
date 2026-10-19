"""
Sieve of Eratosthenes prime generation up to N.
"""
def sieve_of_eratosthenes(limit: int) -> list:
    if limit < 2: return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p): is_prime[i] = False
    return [i for i, p in enumerate(is_prime) if p]
