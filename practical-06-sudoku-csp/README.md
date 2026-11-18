# Practical 06 — Constraint Satisfaction Problems

> **Map Coloring & N-Queens with AC-3 and MRV**
> AI Pillar: Adversarial & Constraint Solving

## Objective

Implement CSP solving with backtracking, forward checking, MRV (Minimum Remaining Values) variable ordering, and AC-3 arc consistency. Solve the Australia map coloring problem and 8-Queens.

## Key Concepts

`CSP` · `Backtracking` · `Forward Checking` · `MRV Heuristic` · `AC-3 Arc Consistency`

## Experimental Results

- Australia map coloring solved with 3 colours using AC-3 preprocessing + backtracking.
- 8-Queens solved with backtracking + forward checking; solution displayed as board.
- MRV ordering reduces nodes tried by selecting most constrained variable first.

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
