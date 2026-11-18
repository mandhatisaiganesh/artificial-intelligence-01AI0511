# Practical 03 — A* Search & Heuristic Comparison

> **8-Puzzle with Manhattan Distance**
> AI Pillar: Agents & Search

## Objective

Implement A* search for the 8-puzzle problem. Compare three admissible heuristics: h=0 (reducing to UCS), misplaced tiles, and Manhattan distance—demonstrating how heuristic informativeness reduces search effort.

## Key Concepts

`A* Search` · `Admissible Heuristics` · `Manhattan Distance` · `Misplaced Tiles` · `Informed Search`

## Experimental Results

- All heuristics return optimal-length solutions (admissibility guarantee).
- Manhattan distance expands far fewer nodes than h=0 or misplaced tiles.
- Demonstrates the trade-off between heuristic computation cost and search efficiency.

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
