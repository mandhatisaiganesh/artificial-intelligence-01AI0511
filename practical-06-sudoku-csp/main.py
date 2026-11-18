"""
Practical 6: Sudoku Solver using Constraint Satisfaction Problem (CSP) & MRV
Course: 01AI0511 - Artificial Intelligence | Marwadi University
"""

import time
import copy

PUZZLE_1 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

stats = {"assignments": 0, "backtracks": 0, "checks": 0}


def candidates(grid, r, c):
    """Consistency check: digits not used in row, column, or 3x3 box."""
    used = set(grid[r]) | {grid[i][c] for i in range(9)}
    br, bc = 3 * (r // 3), 3 * (c // 3)
    used |= {grid[i][j] for i in range(br, br + 3) for j in range(bc, bc + 3)}
    stats["checks"] += 1
    return [d for d in range(1, 10) if d not in used]


def select_mrv(grid):
    """Minimum Remaining Values heuristic: pick empty cell with fewest candidates."""
    best = None
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                opts = candidates(grid, r, c)
                if best is None or len(opts) < len(best[2]):
                    best = (r, c, opts)
    return best


def solve(grid):
    """Recursive backtracking search with MRV."""
    cell = select_mrv(grid)
    if cell is None:
        return True
    r, c, opts = cell
    for d in opts:
        grid[r][c] = d
        stats["assignments"] += 1
        if solve(grid):
            return True
        grid[r][c] = 0
        stats["backtracks"] += 1
    return False


def print_board(grid):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("-" * 21)
        row_str = []
        for c in range(9):
            if c % 3 == 0 and c != 0:
                row_str.append("|")
            row_str.append(str(grid[r][c]) if grid[r][c] != 0 else ".")
        print(" ".join(row_str))


if __name__ == "__main__":
    grid = copy.deepcopy(PUZZLE_1)
    print("=" * 55)
    print(" SUDOKU SOLVER - CONSTRAINT SATISFACTION PROBLEM (MRV)")
    print("=" * 55)
    print("\nInitial Board (Puzzle 1 - 51 empty cells):")
    print_board(grid)

    start_time = time.perf_counter()
    success = solve(grid)
    duration_ms = (time.perf_counter() - start_time) * 1000.0

    print("\nSolved Board:")
    print_board(grid)

    print("-" * 55)
    print(f"Status             : {'Solved!' if success else 'No solution'}")
    print(f"Assignments tried  : {stats['assignments']}")
    print(f"Backtracks         : {stats['backtracks']}")
    print(f"Consistency checks : {stats['checks']}")
    print(f"Execution time     : {duration_ms:.3f} ms")
    print("=" * 55)
