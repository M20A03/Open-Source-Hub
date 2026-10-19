"""
Unit test suite for Segment Tree.
"""
from structures.segment_tree import SegmentTree

def test_segment_tree():
    st = SegmentTree([1, 3, 5, 7, 9, 11])
    assert st.query(1, 3) == 15
