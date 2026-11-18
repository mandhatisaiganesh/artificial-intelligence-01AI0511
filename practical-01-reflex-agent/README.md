# Practical 01 — Simple Reflex Agent & Goal-Based Agent

> **Vacuum World Environment**
> AI Pillar: Agents & Search

## Objective

Implement a simple reflex agent and a goal-based agent in the classic two-room vacuum world. Compare reactive condition→action rules with BFS-based plan generation.

## Key Concepts

`Simple Reflex Agent` · `Goal-Based Agent` · `Percept-Action Rules` · `BFS Planning` · `Performance Measure`

## Experimental Results

- Vacuum World score: **16** over 6 steps (full convergence, both rooms cleaned).
- Simple reflex agent: acts on current percept only (Dirty → Suck, Clean → move).
- Goal-based agent: uses BFS over state space to plan an optimal action sequence.

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
