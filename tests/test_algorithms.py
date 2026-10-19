"""
Unit Tests for Algorithms
Author: Mayank Raj (M20A03)
"""

import unittest
from src.algorithms.search import binary_search, linear_search
from src.algorithms.graph import bfs, dfs

class TestAlgorithms(unittest.TestCase):
    def test_search(self):
        arr = [1, 3, 5, 7, 9, 11]
        self.assertEqual(binary_search(arr, 7), 3)
        self.assertEqual(binary_search(arr, 10), None)
        self.assertEqual(linear_search(arr, 3), 1)

    def test_graph(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }
        bfs_order = bfs(graph, 'A')
        self.assertIn('A', bfs_order)
        self.assertEqual(len(bfs_order), 6)

        dfs_order = dfs(graph, 'A')
        self.assertIn('A', dfs_order)
        self.assertEqual(len(dfs_order), 6)

if __name__ == '__main__':
    unittest.main()
