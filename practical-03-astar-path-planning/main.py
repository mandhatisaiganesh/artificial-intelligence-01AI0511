"""
Practical 3: A* search for the 8-puzzle with different heuristics.
Heuristics compared: h0 (zero = uniform cost), misplaced tiles, Manhattan distance.
"""

import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
MOVES = {"U": -3, "D": 3, "L": -1, "R": 1}


def h_zero(s):
    return 0


def h_misplaced(s):
    return sum(1 for i, v in enumerate(s) if v != 0 and v != GOAL[i])


def h_manhattan(s):
    total = 0
    for i, v in enumerate(s):
        if v:
            gi = GOAL.index(v)
            total += abs(i // 3 - gi // 3) + abs(i % 3 - gi % 3)
    return total


def successors(s):
    z = s.index(0)
    for m, d in MOVES.items():
        if (m == "U" and z < 3) or (m == "D" and z > 5):
            continue
        if (m == "L" and z % 3 == 0) or (m == "R" and z % 3 == 2):
            continue
        n = list(s)
        n[z], n[z + d] = n[z + d], n[z]
        yield m, tuple(n)


def solvable(s):
    arr = [v for v in s if v]
    inv = sum(1 for i in range(len(arr)) for j in range(i + 1, len(arr)) if arr[i] > arr[j])
    return inv % 2 == 0


def astar(start, h):
    frontier = [(h(start), 0, start, [])]
    best_g = {start: 0}
    expanded = 0
    while frontier:
        f, g, state, path = heapq.heappop(frontier)
        if g > best_g.get(state, float("inf")):
            continue
        expanded += 1
        if state == GOAL:
            return path, expanded
        for m, nxt in successors(state):
            ng = g + 1
            if ng < best_g.get(nxt, float("inf")):
                best_g[nxt] = ng
                heapq.heappush(frontier, (ng + h(nxt), ng, nxt, path + [m]))
    return None, expanded


if __name__ == "__main__":
    start = (8, 1, 3, 4, 0, 2, 7, 6, 5)
    assert solvable(start), "unsolvable instance"
    print("Start state:", start)
    print(f"{'Heuristic':<18} {'Moves':>6} {'Expanded':>9}  Path")
    for name, h in (("h=0 (UCS)", h_zero),
                    ("Misplaced tiles", h_misplaced),
                    ("Manhattan", h_manhattan)):
        path, exp = astar(start, h)
        print(f"{name:<18} {len(path):>6} {exp:>9}  {''.join(path)}")
    print("\nAll heuristics are admissible, so all return optimal-length paths;")
    print("the more informed Manhattan heuristic expands far fewer nodes.")
