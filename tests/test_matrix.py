"""
Unit Tests for Matrix Operations
"""

import unittest
from src.algorithms.matrix import matrix_multiply, matrix_transpose

class TestMatrix(unittest.TestCase):
    def test_multiply(self):
        A = [[1.0, 2.0], [3.0, 4.0]]
        B = [[2.0, 0.0], [1.0, 2.0]]
        expected = [[4.0, 4.0], [10.0, 8.0]]
        self.assertEqual(matrix_multiply(A, B), expected)

    def test_transpose(self):
        A = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
        expected = [[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]]
        self.assertEqual(matrix_transpose(A), expected)

if __name__ == '__main__':
    unittest.main()
