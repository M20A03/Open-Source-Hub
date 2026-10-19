"""
Fixed-size Circular Queue buffer implementation.
"""
class CircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.queue = [None] * k
        self.head = 0
        self.tail = 0
        self.size = 0
        
    def enqueue(self, val) -> bool:
        if self.is_full(): return False
        self.queue[self.tail] = val
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True
        
    def dequeue(self):
        if self.is_empty(): return None
        val = self.queue[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return val
        
    def is_empty(self) -> bool: return self.size == 0
    def is_full(self) -> bool: return self.size == self.capacity
