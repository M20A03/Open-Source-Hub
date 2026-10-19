"""
Bloom filter implementation with murmur3/hash variations.
"""
import hashlib

class BloomFilter:
    def __init__(self, size: int = 1000):
        self.size = size
        self.bit_array = [False] * size
        
    def _hashes(self, item: str):
        h1 = int(hashlib.md5(item.encode()).hexdigest(), 16) % self.size
        h2 = int(hashlib.sha256(item.encode()).hexdigest(), 16) % self.size
        return [h1, h2]
        
    def add(self, item: str):
        for h in self._hashes(item): self.bit_array[h] = True
            
    def contains(self, item: str) -> bool:
        return all(self.bit_array[h] for h in self._hashes(item))
