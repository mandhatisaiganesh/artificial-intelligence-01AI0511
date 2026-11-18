# Practical 04 — Minimax & Alpha-Beta Pruning

> **Tic-Tac-Toe Game Tree Search**
> AI Pillar: Adversarial & Constraint Solving

## Objective

Implement the Minimax algorithm and Alpha-Beta pruning for Tic-Tac-Toe. Measure the node reduction from pruning and demonstrate optimal self-play (guaranteed draw under perfect play).

## Key Concepts

`Minimax` · `Alpha-Beta Pruning` · `Game Tree` · `Terminal Evaluation` · `Optimal Play`

## Experimental Results

- Alpha-Beta prunes ~96.6% of the game tree compared to full Minimax on empty board.
- Self-play (Minimax-X vs Alpha-Beta-O) always results in a draw — confirming optimal play.
- Both algorithms return the same game-theoretic value (0 = draw from empty board).

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
