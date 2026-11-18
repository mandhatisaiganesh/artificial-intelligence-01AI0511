"""
Practical 2: BFS, DFS and Uniform-Cost Search on a maze (grid) problem.
Compares search cost (nodes expanded) and path quality (path cost).
"""

import heapq
from collections import deque

MAZE = [
    "S.#.....",
    ".##.###.",
    "....#...",
    ".####.#.",
    "......#G",
]
# '#': wall, '.': open (cost 1), 'S': start, 'G': goal
# Cells marked below with higher cost (mud) so UCS differs from BFS.
MUD = {(0, 1): 5, (2, 1): 5, (2, 2): 5}


def find(ch):
    for r, row in enumerate(MAZE):
        for c, v in enumerate(row):
            if v == ch:
                return (r, c)


START, GOAL = find("S"), find("G")


def neighbors(pos):
    r, c = pos
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(MAZE) and 0 <= nc < len(MAZE[0]) and MAZE[nr][nc] != "#":
            yield (nr, nc), MUD.get((nr, nc), 1)


def path_cost(path):
    return sum(MUD.get(p, 1) for p in path[1:])


def bfs():
    frontier, seen, expanded = deque([[START]]), {START}, 0
    while frontier:
        path = frontier.popleft()
        node = path[-1]
        expanded += 1
        if node == GOAL:
            return path, expanded
        for n, _ in neighbors(node):
            if n not in seen:
                seen.add(n)
                frontier.append(path + [n])
    return None, expanded


def dfs():
    frontier, seen, expanded = [[START]], set(), 0
    while frontier:
        path = frontier.pop()
        node = path[-1]
        if node in seen:
            continue
        seen.add(node)
        expanded += 1
        if node == GOAL:
            return path, expanded
        for n, _ in neighbors(node):
            if n not in seen:
                frontier.append(path + [n])
    return None, expanded


def ucs():
    frontier, best, expanded = [(0, [START])], {}, 0
    while frontier:
        cost, path = heapq.heappop(frontier)
        node = path[-1]
        if node in best and best[node] <= cost:
            continue
        best[node] = cost
        expanded += 1
        if node == GOAL:
            return path, expanded
        for n, step in neighbors(node):
            heapq.heappush(frontier, (cost + step, path + [n]))
    return None, expanded


def show(path):
    grid = [list(r) for r in MAZE]
    for r, c in path[1:-1]:
        grid[r][c] = "*"
    return "\n".join("".join(r) for r in grid)


if __name__ == "__main__":
    print("Maze:\n" + "\n".join(MAZE), "\n")
    print(f"{'Algorithm':<6} {'Expanded':>9} {'Length':>7} {'Cost':>5}")
    for name, algo in (("BFS", bfs), ("DFS", dfs), ("UCS", ucs)):
        path, exp = algo()
        print(f"{name:<6} {exp:>9} {len(path)-1:>7} {path_cost(path):>5}")
        print(show(path), "\n")
    print("Observation: BFS gives the fewest steps, UCS gives the lowest cost,")
    print("DFS is not guaranteed optimal in either.")
