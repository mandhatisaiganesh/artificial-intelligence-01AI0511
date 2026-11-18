# Practical 02 — Uninformed Search: BFS, DFS, UCS

> **Maze Navigation with Cost Analysis**
> AI Pillar: Agents & Search

## Objective

Implement Breadth-First Search, Depth-First Search, and Uniform-Cost Search on a grid maze with variable step costs. Compare path optimality, total cost, and nodes expanded.

## Key Concepts

`BFS` · `DFS` · `Uniform-Cost Search` · `Frontier Management` · `Path Cost vs Path Length`

## Experimental Results

- BFS finds the shortest path (fewest steps).
- UCS finds the lowest-cost path, correctly avoiding "mud" cells (cost 5).
- DFS is not guaranteed optimal in either metric.

## Files

| File | Description |
|------|-------------|
| [`main.py`](./main.py) | Complete standalone Python implementation |
| [`notebook.ipynb`](./notebook.ipynb) | Interactive Jupyter notebook with step-by-step cells |
| [`report.pdf`](./report.pdf) | Lab report (PDF) |

## Usage

```bash
python main.py
```

---
*Course: 01AI0511 — Artificial Intelligence · Marwadi University*
