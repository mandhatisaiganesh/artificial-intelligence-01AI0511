# Practical 07 — Bayesian Network & Naive Bayes Classifier

> **Probabilistic Inference from Scratch**
> AI Pillar: Probabilistic & Reinforcement Learning

## Objective

Implement Bayesian network inference by enumeration on the classic Burglary-Alarm network. Additionally, build a Naive Bayes classifier with Laplace smoothing for the Play Tennis dataset.

## Key Concepts

`Bayesian Networks` · `Inference by Enumeration` · `Naive Bayes` · `Laplace Smoothing` · `Conditional Independence`

## Experimental Results

- P(Burglary | JohnCalls, MaryCalls) ≈ 0.2842 (matching textbook value).
- Naive Bayes correctly classifies play-tennis test instances with posterior probabilities.
- Both implementations use only the standard library (no external dependencies).

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
