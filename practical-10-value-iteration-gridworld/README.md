# Practical 10 — Value Iteration on Grid-World MDP

> **Sequential Decision-Making Under Uncertainty**
> AI Pillar: Probabilistic & Reinforcement Learning

## Objective

Implement Value Iteration for the Russell & Norvig 4×3 grid-world MDP with stochastic transitions (0.8 intended direction, 0.1 each perpendicular). Extract the optimal policy from converged utilities.

## Key Concepts

`Markov Decision Process` · `Value Iteration` · `Bellman Equation` · `Optimal Policy` · `Discount Factor`

## Experimental Results

- Converges with γ = 0.99 and step reward = −0.04.
- Optimal policy navigates around the −1 terminal state to reach the +1 terminal.
- Utilities and policy displayed as grid visualisations.

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
