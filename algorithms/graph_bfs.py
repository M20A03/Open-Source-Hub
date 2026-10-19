"""
Breadth-First Search (BFS) graph traversal and unweighted shortest path.
"""
from collections import deque
from typing import Dict, List, Optional

def bfs_traversal(graph: Dict[str, List[str]], start: str) -> List[str]:
    visited = set([start])
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def shortest_path_unweighted(graph: Dict[str, List[str]], start: str, target: str) -> Optional[List[str]]:
    if start == target:
        return [start]
    visited = {start: None}
    queue = deque([start])
    while queue:
        curr = queue.popleft()
        if curr == target: break
        for nxt in graph.get(curr, []):
            if nxt not in visited:
                visited[nxt] = curr
                queue.append(nxt)
    if target not in visited: return None
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = visited[curr]
    return path[::-1]
