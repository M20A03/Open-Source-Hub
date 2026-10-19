"""
Depth-First Search (DFS) implementation and connected components detection.
"""
from typing import Dict, List, Set

def dfs_recursive(graph: Dict[str, List[str]], node: str, visited: Set[str], result: List[str]):
    visited.add(node)
    result.append(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)

def find_connected_components(graph: Dict[str, List[str]]) -> List[List[str]]:
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            comp = []
            dfs_recursive(graph, node, visited, comp)
            components.append(comp)
    return components
