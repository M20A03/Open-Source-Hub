"""
High-Performance Search Algorithms
Author: Mayank Raj (M20A03)
Co-Author: mayankrajdhn5-prog
"""

from typing import List, Optional, TypeVar

T = TypeVar('T')

def binary_search(arr: List[T], target: T) -> Optional[int]:
    """Perform iterative binary search on a sorted list with O(log n) time complexity."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

def linear_search(arr: List[T], target: T) -> Optional[int]:
    """Perform sequential search with O(n) time complexity."""
    for index, item in enumerate(arr):
        if item == target:
            return index
    return None
