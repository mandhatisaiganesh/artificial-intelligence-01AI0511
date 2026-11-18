"""
Practical 4: Minimax with Alpha-Beta Pruning - Tic-Tac-Toe
Course: 01AI0511 - Artificial Intelligence | Marwadi University
"""

HUMAN = "O"
AI = "X"
EMPTY = " "

lines = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


def print_board(board):
    rows = []
    for r in range(3):
        rows.append(" | ".join(board[r * 3:r * 3 + 3]))
    print(("\n" + "-" * 9 + "\n").join(rows))


def winner(board):
    for a, b, c in lines:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return EMPTY not in board


nodes_evaluated = 0


def minimax(board, depth, alpha, beta, maximizing):
    global nodes_evaluated
    nodes_evaluated += 1

    win = winner(board)
    if win == AI:
        return 10 - depth
    if win == HUMAN:
        return depth - 10
    if is_full(board):
        return 0

    if maximizing:
        best = float("-inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, depth + 1, alpha, beta, False)
                board[i] = EMPTY
                best = max(best, score)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = float("inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax(board, depth + 1, alpha, beta, True)
                board[i] = EMPTY
                best = min(best, score)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best


def best_move(board):
    best_score = float("-inf")
    move = None
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, 0, float("-inf"), float("inf"), False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                move = i
    return move


def scripted_human_move(board):
    """A fixed sequence representing a sensible opponent."""
    for i in [4, 0, 2, 6, 8, 1, 3, 5, 7]:
        if board[i] == EMPTY:
            return i
    return None


if __name__ == "__main__":
    board = [EMPTY] * 9
    turn = AI
    move_no = 0

    print("=" * 55)
    print(" MINIMAX + ALPHA-BETA PRUNING - TIC-TAC-TOE")
    print("=" * 55)

    while True:
        move_no += 1
        print(f"\nMove {move_no} ({turn}'s turn)")

        if turn == AI:
            nodes_evaluated = 0
            pos = best_move(board)
            board[pos] = AI
            print(f"AI plays position {pos} (nodes evaluated: {nodes_evaluated})")
        else:
            pos = scripted_human_move(board)
            board[pos] = HUMAN
            print(f"Opponent plays position {pos}")

        print_board(board)

        w = winner(board)
        if w:
            print(f"\nResult: {w} WINS!")
            break
        if is_full(board):
            print("\nResult: DRAW")
            break

        turn = HUMAN if turn == AI else AI

    print("=" * 55)
