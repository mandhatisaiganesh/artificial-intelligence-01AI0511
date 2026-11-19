import os
os.environ['MPLCONFIGDIR'] = '/tmp/mpl'
"""
Practical 3: A* Path Planning on 2D Grid with Obstacles
Course: 01AI0511 - Artificial Intelligence | Marwadi University
"""

import heapq
import random
import time
import os

ROWS = 20
COLS = 20
START = (0, 0)
GOAL = (19, 19)
OBSTACLE_PROBABILITY = 0.20
RANDOM_SEED = 42
random.seed(RANDOM_SEED)


def create_grid(rows, cols, obstacle_probability, start, goal):
    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            if (r, c) == start or (r, c) == goal:
                row.append(0)
            elif random.random() < obstacle_probability:
                row.append(1)
            else:
                row.append(0)
        grid.append(row)
    return grid


def manhattan_distance(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)


def get_neighbors(node, grid):
    row, col = node
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    rows, cols = len(grid), len(grid[0])
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
            neighbors.append((nr, nc))
    return neighbors


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def a_star(grid, start, goal):
    start_time = time.perf_counter()
    open_set = []
    counter = 0
    initial_h = manhattan_distance(start, goal)
    heapq.heappush(open_set, (initial_h, counter, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: initial_h}
    closed_set = set()
    explored_nodes = []

    while open_set:
        current_f, _, current = heapq.heappop(open_set)
        if current in closed_set:
            continue
        closed_set.add(current)
        explored_nodes.append(current)

        if current == goal:
            path = reconstruct_path(came_from, current)
            return {
                "path": path,
                "explored": explored_nodes,
                "g_score": g_score,
                "f_score": f_score,
                "execution_time": time.perf_counter() - start_time,
                "success": True
            }

        for neighbor in get_neighbors(current, grid):
            if neighbor in closed_set:
                continue
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                h = manhattan_distance(neighbor, goal)
                f_score[neighbor] = tentative_g + h
                counter += 1
                heapq.heappush(open_set, (tentative_g + h, counter, neighbor))

    return {
        "path": [],
        "explored": explored_nodes,
        "g_score": g_score,
        "f_score": f_score,
        "execution_time": time.perf_counter() - start_time,
        "success": False
    }


def save_visualization(grid, result, output_path="astar_path_planning.png"):
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import numpy as np

        display_grid = np.array(grid, dtype=float)
        # Mark explored as 0.3
        for r, c in result["explored"]:
            if (r, c) != START and (r, c) != GOAL:
                display_grid[r, c] = 0.4

        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(display_grid, cmap="viridis")

        if result["path"]:
            pr, pc = zip(*result["path"])
            ax.plot(pc, pr, color="gold", linewidth=3, label="A* Shortest Path")

        ax.scatter([START[1]], [START[0]], color="lime", s=120, label="START", zorder=5)
        ax.scatter([GOAL[1]], [GOAL[0]], color="red", s=120, marker="*", label="GOAL", zorder=5)

        ax.set_title(f"A* Search: Explored {len(result['explored'])} Nodes | Path Length {len(result['path'])-1}")
        ax.set_xlabel("Column")
        ax.set_ylabel("Row")
        ax.legend(loc="upper left")
        plt.tight_layout()
        plt.savefig(output_path, dpi=150)
        plt.close()
        print(f"\nVisualization saved to {output_path}")
    except Exception as e:
        print(f"\n(Matplotlib plot skipped: {e})")


if __name__ == "__main__":
    grid = create_grid(ROWS, COLS, OBSTACLE_PROBABILITY, START, GOAL)
    result = a_star(grid, START, GOAL)

    print("=" * 65)
    print(" A* SEARCH ALGORITHM")
    print("=" * 65)
    print(f"Grid Size        : {ROWS} x {COLS}")
    print(f"Start Node       : {START}")
    print(f"Goal Node        : {GOAL}")
    print(f"Obstacle Density : {OBSTACLE_PROBABILITY * 100:.1f}%")
    print("-" * 65)
    print(f"Path Found       : {'YES' if result['success'] else 'NO'}")
    print(f"Path Length      : {len(result['path']) - 1}")
    print(f"Nodes Explored   : {len(result['explored'])}")
    print(f"Execution Time   : {result['execution_time']:.6f} seconds")
    print("=" * 65)

    if result["success"]:
        print("\nA* COST ANALYSIS (first 10 steps)")
        print("-" * 65)
        print(f"{'Node':<12} {'g(n)':<8} {'h(n)':<8} {'f(n)':<8}")
        print("-" * 65)
        for node in result["path"][:10]:
            g = result["g_score"][node]
            h = manhattan_distance(node, GOAL)
            f = g + h
            print(f"{str(node):<12} {g:<8} {h:<8} {f:<8}")

        output_png = os.path.join(os.path.dirname(__file__), "astar_path_planning.png")
        save_visualization(grid, result, output_png)
