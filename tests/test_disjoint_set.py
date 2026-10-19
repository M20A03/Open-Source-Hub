"""
Unit test suite for Disjoint Set Union (DSU).
"""
from structures.disjoint_set import DisjointSet

def test_dsu():
    dsu = DisjointSet(5)
    assert dsu.union(0, 1) is True; assert dsu.find(0) == dsu.find(1)
