"""
Rabin-Karp polynomial rolling hash string matching algorithm.
"""
def rabin_karp(pattern: str, text: str, prime: int = 101) -> list:
    m, n = len(pattern), len(text)
    if m == 0 or m > n: return []
    d = 256
    p_hash = t_hash = 0
    h = pow(d, m - 1, prime)
    matches = []
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime
    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i + m] == pattern:
            matches.append(i)
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t_hash < 0: t_hash += prime
    return matches
