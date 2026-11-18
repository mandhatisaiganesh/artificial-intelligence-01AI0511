"""
Practical 2: Uninformed Search Strategies (BFS, DFS, Uniform Cost Search)
Course: 01AI0511 - Artificial Intelligence | Marwadi University
"""

from collections import deque
import heapq

# Directed unweighted graph
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["G"],
    "G": []
}

# Directed weighted graph for UCS
weighted_graph = {
    "A": [("B", 1), ("C", 5)],
    "B": [("D", 1)],
    "C": [("D", 1)],
    "D": [("G", 1)],
    "G": []
}


def bfs(graph, start, goal):
    """Breadth-First Search using a FIFO queue."""
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(path + [neighbor])
    return None


def dfs(graph, start, goal):
    """Depth-First Search using a LIFO stack."""
    stack = [[start]]
    visited = set()
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append(path + [neighbor])
    return None


def ucs(graph, start, goal):
    """Uniform-Cost Search using a min-heap priority queue."""
    pq = [(0, start, [start])]
    visited = set()
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return cost, path
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
    return float("inf"), None


if __name__ == "__main__":
    print("=" * 45)
    print(" ARTIFICIAL INTELLIGENCE PRACTICAL")
    print(" BFS | DFS | Uniform Cost Search")
    print("=" * 45)

    bfs_path = bfs(graph, "A", "G")
    dfs_path = dfs(graph, "A", "G")
    cost, ucs_path = ucs(weighted_graph, "A", "G")

    print("\nBFS Path :", " -> ".join(bfs_path))
    print("DFS Path :", " -> ".join(dfs_path))
    print("UCS Path :", " -> ".join(ucs_path))
    print("Total Cost:", cost)

    print("\nComparison")
    print("-" * 45)
    print("BFS : Uses Queue (FIFO) and finds shortest path.")
    print("DFS : Uses Stack (LIFO) and explores deep first.")
    print("UCS : Uses Priority Queue and finds minimum cost path.")
