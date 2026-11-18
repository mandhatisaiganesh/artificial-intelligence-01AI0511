"""
Practical 4: Game-playing agent for Tic-Tac-Toe using Minimax and Alpha-Beta pruning.
Compares number of nodes evaluated, then plays a game: Minimax(X) vs Alpha-Beta(O).
"""

LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8),
         (0, 4, 8), (2, 4, 6)]


def winner(b):
    for a, c, d in LINES:
        if b[a] != " " and b[a] == b[c] == b[d]:
            return b[a]
    return None


def moves(b):
    return [i for i, v in enumerate(b) if v == " "]


def terminal_value(b):
    w = winner(b)
    if w == "X":
        return 1
    if w == "O":
        return -1
    if not moves(b):
        return 0
    return None


class Counter:
    n = 0


def minimax(b, player):
    Counter.n += 1
    t = terminal_value(b)
    if t is not None:
        return t
    vals = []
    for m in moves(b):
        b[m] = player
        vals.append(minimax(b, "O" if player == "X" else "X"))
        b[m] = " "
    return max(vals) if player == "X" else min(vals)


def alphabeta(b, player, alpha=-2, beta=2):
    Counter.n += 1
    t = terminal_value(b)
    if t is not None:
        return t
    if player == "X":
        v = -2
        for m in moves(b):
            b[m] = "X"
            v = max(v, alphabeta(b, "O", alpha, beta))
            b[m] = " "
            alpha = max(alpha, v)
            if alpha >= beta:
                break
        return v
    v = 2
    for m in moves(b):
        b[m] = "O"
        v = min(v, alphabeta(b, "X", alpha, beta))
        b[m] = " "
        beta = min(beta, v)
        if alpha >= beta:
            break
    return v


def best_move(b, player, algo):
    best, best_m = None, None
    for m in moves(b):
        b[m] = player
        v = algo(b, "O" if player == "X" else "X")
        b[m] = " "
        if best is None or (player == "X" and v > best) or (player == "O" and v < best):
            best, best_m = v, m
    return best_m


def show(b):
    for r in range(3):
        print(" " + " | ".join(b[3 * r:3 * r + 3]))
        if r < 2:
            print("---+---+---")


if __name__ == "__main__":
    empty = [" "] * 9
    Counter.n = 0
    v1 = minimax(empty[:], "X")
    n1 = Counter.n
    Counter.n = 0
    v2 = alphabeta(empty[:], "X")
    n2 = Counter.n
    print(f"Minimax:    value={v1}, nodes={n1}")
    print(f"Alpha-Beta: value={v2}, nodes={n2}  ({100 * (1 - n2 / n1):.1f}% fewer)")

    print("\nSelf-play: X uses Minimax, O uses Alpha-Beta")
    board, player = [" "] * 9, "X"
    while terminal_value(board) is None:
        algo = minimax if player == "X" else alphabeta
        board[best_move(board, player, algo)] = player
        player = "O" if player == "X" else "X"
    show(board)
    w = winner(board)
    print("Result:", f"{w} wins" if w else "Draw (optimal play)")
