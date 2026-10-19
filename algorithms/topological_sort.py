"""
Topological sorting using in-degree queue (Kahn's algorithm).
"""
from collections import deque

def kahn_topological_sort(num_nodes: int, edges: list) -> list:
    in_degree = [0] * num_nodes
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1
    queue = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    if len(order) != num_nodes:
        raise ValueError("Graph contains a cycle")
    return order
