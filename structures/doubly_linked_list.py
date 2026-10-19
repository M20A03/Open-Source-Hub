"""
Doubly Linked List with sentinel head and tail nodes.
"""
class Node:
    def __init__(self, val=0, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def append(self, val):
        node = Node(val, self.tail.prev, self.tail)
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1
        
    def to_list(self):
        res = []
        curr = self.head.next
        while curr != self.tail:
            res.append(curr.val)
            curr = curr.next
        return res
