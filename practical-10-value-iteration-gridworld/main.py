"""
Practical 10: Value Iteration on a grid-world MDP (Russell & Norvig 4x3 world).

Grid (row 0 is top):
    .  .  .  +1
    .  #  . -1
    S  .  .  .
Stochastic moves: 0.8 intended direction, 0.1 each perpendicular.
"""

ROWS, COLS = 3, 4
WALL = {(1, 1)}
TERMINALS = {(0, 3): 1.0, (1, 3): -1.0}
STEP_REWARD = -0.04
GAMMA = 0.99
ACTIONS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
PERP = {"^": ("<", ">"), "v": ("<", ">"), "<": ("^", "v"), ">": ("^", "v")}
STATES = [(r, c) for r in range(ROWS) for c in range(COLS) if (r, c) not in WALL]


def move(s, a):
    r, c = s[0] + ACTIONS[a][0], s[1] + ACTIONS[a][1]
    if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in WALL:
        return (r, c)
    return s


def transitions(s, a):
    p1, p2 = PERP[a]
    return [(0.8, move(s, a)), (0.1, move(s, p1)), (0.1, move(s, p2))]


def q_value(V, s, a):
    return sum(p * (STEP_REWARD + GAMMA * V[s2]) for p, s2 in transitions(s, a))


def value_iteration(eps=1e-6):
    V = {s: 0.0 for s in STATES}
    for s, r in TERMINALS.items():
        V[s] = r
    it = 0
    while True:
        it += 1
        delta = 0.0
        newV = dict(V)
        for s in STATES:
            if s in TERMINALS:
                continue
            newV[s] = max(q_value(V, s, a) for a in ACTIONS)
            delta = max(delta, abs(newV[s] - V[s]))
        V = newV
        if delta < eps:
            return V, it


def extract_policy(V):
    pol = {}
    for s in STATES:
        if s in TERMINALS:
            pol[s] = "T"
        else:
            pol[s] = max(ACTIONS, key=lambda a: q_value(V, s, a))
    return pol


if __name__ == "__main__":
    V, iters = value_iteration()
    pol = extract_policy(V)
    print(f"Converged in {iters} iterations (gamma={GAMMA}, step reward={STEP_REWARD})\n")
    print("Utilities:")
    for r in range(ROWS):
        print("  ".join("  ####" if (r, c) in WALL else f"{V[(r, c)]:+.3f}" for c in range(COLS)))
    print("\nOptimal policy:")
    for r in range(ROWS):
        print("  ".join("#" if (r, c) in WALL else pol[(r, c)] for c in range(COLS)))
