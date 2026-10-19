"""
Fenwick Tree (Binary Indexed Tree) for dynamic prefix sums.
"""
class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)
        
    def update(self, index: int, delta: int):
        i = index + 1
        while i <= self.size:
            self.tree[i] += delta
            i += i & (-i)
            
    def query(self, index: int) -> int:
        s = 0
        i = index + 1
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
