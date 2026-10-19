"""
Segment Tree implementation for range sum queries and point updates.
"""
class SegmentTree:
    def __init__(self, data: list):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        if self.n > 0: self._build(data, 0, 0, self.n - 1)
            
    def _build(self, data, node, start, end):
        if start == end: self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            self._build(data, 2 * node + 1, start, mid)
            self._build(data, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
            
    def query(self, l: int, r: int, node=0, start=0, end=None) -> int:
        if end is None: end = self.n - 1
        if r < start or end < l: return 0
        if l <= start and end <= r: return self.tree[node]
        mid = (start + end) // 2
        return self.query(l, r, 2 * node + 1, start, mid) + self.query(l, r, 2 * node + 2, mid + 1, end)
