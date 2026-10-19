"""
Unit test suite for Circular Queue buffer.
"""
from structures.circular_queue import CircularQueue

def test_queue():
    q = CircularQueue(3)
    assert q.enqueue(10) is True; assert q.dequeue() == 10
