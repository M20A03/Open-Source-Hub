"""
Knuth-Morris-Pratt linear time pattern matching algorithm.
"""
def compute_lps(pattern: str) -> list:
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0: length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(pattern: str, text: str) -> list:
    m, n = len(pattern), len(text)
    if m == 0: return []
    lps = compute_lps(pattern)
    i = j = 0
    matches = []
    while i < n:
        if pattern[j] == text[i]:
            i += 1; j += 1
        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0: j = lps[j - 1]
            else: i += 1
    return matches
