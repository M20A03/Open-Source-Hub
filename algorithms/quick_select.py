"""
Quickselect algorithm for finding k-th smallest element in O(n) average time.
"""
def quickselect(arr: list, k: int) -> int:
    if not 0 <= k < len(arr):
        raise IndexError("k out of bounds")
    pivot = arr[len(arr) // 2]
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]
    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))
