"""
Unit test suite for Trie data structure.
"""
from algorithms.trie_search import Trie

def test_trie():
    t = Trie()
    t.insert("apple")
    assert t.search("apple") is True
    assert t.search("app") is False
    assert t.starts_with("app") is True
