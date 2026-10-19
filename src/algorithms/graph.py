"""
Graph Traversal Algorithms
Author: Mayank Raj (M20A03)
Co-Author: mayankrajdhn5-prog
"""

from collections import deque
from typing import Dict, List, Optional, Set

def bfs(graph: Dict[str, List[str]], start_node: str) -> List[str]:
    """Breadth-First Search traversal."""
    visited: Set[str] = set([start_node])
    queue: deque = deque([start_node])
    order: List[str] = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def dfs(graph: Dict[str, List[str]], start_node: str, visited: Optional[Set[str]] = None) -> List[str]:
    """Depth-First Search traversal."""
    if visited is None:
        visited = set()
    order: List[str] = []
    visited.add(start_node)
    order.append(start_node)

    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))
    return order
