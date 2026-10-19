"""
Bellman-Ford algorithm with negative weight edge cycle detection.
"""
def bellman_ford(vertices: int, edges: list, start: int):
    dist = [float('inf')] * vertices
    dist[start] = 0
    for _ in range(vertices - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative weight cycle")
    return dist
