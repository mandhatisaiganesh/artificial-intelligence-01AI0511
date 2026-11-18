"""
Practical 10: Value Iteration in a Grid-World Environment with Obstacles
Course: 01AI0511 - Artificial Intelligence | Marwadi University
"""

ACTIONS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def get_environment(n=5):
    """Creates NxN grid with start (0,0), goal (N-1, N-1), and fixed obstacles."""
    start = (0, 0)
    goal = (n - 1, n - 1)
    # Fixed deterministic obstacles matching lab manual
    if n == 5:
        obstacles = {(1, 2), (2, 2), (3, 1), (4, 0), (4, 1)}
    elif n == 6:
        obstacles = {(1, 2), (2, 2), (3, 1), (4, 3), (2, 4), (5, 1)}
    elif n == 8:
        obstacles = {(1, 2), (2, 2), (3, 1), (4, 3), (2, 4), (5, 1), (6, 5), (7, 2)}
    else:
        obstacles = set()

    states = [(r, c) for r in range(n) for c in range(n) if (r, c) not in obstacles]
    return states, start, goal, obstacles


def step(s, a, n, obstacles):
    """Deterministic transition: hitting wall/obstacle keeps agent in place."""
    dr, dc = ACTIONS[a]
    nr, nc = s[0] + dr, s[1] + dc
    if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in obstacles:
        return (nr, nc)
    return s


def value_iteration(n=5, gamma=0.9, theta=0.001):
    states, start, goal, obstacles = get_environment(n)
    V = {s: 0.0 for s in states}
    iterations = 0

    while True:
        delta = 0.0
        new_V = dict(V)
        iterations += 1

        for s in states:
            if s == goal:
                continue
            # Bellman optimality: max_a [ R(s, a) + gamma * V(s') ]
            # Reward: -1 for move, +10 for reaching goal
            action_values = []
            for a in ACTIONS:
                ns = step(s, a, n, obstacles)
                r = 10.0 if ns == goal else -1.0
                action_values.append(r + gamma * V[ns])

            best_val = max(action_values)
            delta = max(delta, abs(best_val - V[s]))
            new_V[s] = best_val

        V = new_V
        if delta < theta:
            break

    # Extract optimal policy
    policy = {}
    for s in states:
        if s == goal:
            policy[s] = "G"
            continue
        best_a = None
        best_val = float("-inf")
        for a in ACTIONS:
            ns = step(s, a, n, obstacles)
            r = 10.0 if ns == goal else -1.0
            val = r + gamma * V[ns]
            if val > best_val:
                best_val = val
                best_a = a
        policy[s] = best_a

    # Trace path from start to goal
    path = [start]
    curr = start
    for _ in range(n * n):
        if curr == goal:
            break
        a = policy[curr]
        curr = step(curr, a, n, obstacles)
        path.append(curr)

    return V, policy, path, iterations


if __name__ == "__main__":
    print("=" * 65)
    print(" VALUE ITERATION - GRID-WORLD MDP WITH OBSTACLES")
    print("=" * 65)

    tests = [
        {"n": 5, "gamma": 0.9, "desc": "5x5 grid, gamma=0.9"},
        {"n": 6, "gamma": 0.9, "desc": "6x6 grid, gamma=0.9"},
        {"n": 5, "gamma": 0.5, "desc": "5x5 grid, gamma=0.5 (strong discount)"},
        {"n": 8, "gamma": 0.9, "desc": "8x8 grid, gamma=0.9"}
    ]

    for t in tests:
        V, policy, path, iters = value_iteration(n=t["n"], gamma=t["gamma"])
        start_val = V[(0, 0)]
        print(f"\nTest: {t['desc']}")
        print(f"  Iterations to converge : {iters}")
        print(f"  Optimal path length    : {len(path) - 1} moves")
        print(f"  Start state value V(0,0): {start_val:.2f}")
        print(f"  Goal reached           : {'Yes' if path[-1] == (t['n']-1, t['n']-1) else 'No'}")
        print(f"  Path trace             : {' -> '.join(str(p) for p in path)}")

    print("\n" + "=" * 65)
