"""
Sorting Algorithms Library
Author: Mayank Raj (M20A03)
Co-Author: mayankrajdhn5-prog
"""

from typing import List, TypeVar

T = TypeVar('T')

def mergesort(arr: List[T]) -> List[T]:
    """Perform out-of-place MergeSort with O(n log n) time complexity."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quicksort(arr: List[T]) -> List[T]:
    """Perform QuickSort with O(n log n) expected time complexity."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
