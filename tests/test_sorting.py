"""
Unit Tests for Sorting Algorithms
"""

import unittest
from src.algorithms.sorting import mergesort, quicksort

class TestSorting(unittest.TestCase):
    def test_mergesort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        self.assertEqual(mergesort(arr), [11, 12, 22, 25, 34, 64, 90])
        self.assertEqual(mergesort([]), [])
        self.assertEqual(mergesort([5]), [5])

    def test_quicksort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        self.assertEqual(quicksort(arr), [11, 12, 22, 25, 34, 64, 90])
        self.assertEqual(quicksort([]), [])
        self.assertEqual(quicksort([5]), [5])

if __name__ == '__main__':
    unittest.main()
