# Practical 12 — ML Classifier Benchmark

> **k-NN, Decision Tree, Naive Bayes, Perceptron**
> AI Pillar: Probabilistic & Reinforcement Learning
> Status: ✅ Complete (code included)

## Objective

Implement four classical ML classifiers from scratch and compare train/test accuracy on a synthetic 2-feature binary classification problem (hours studied × hours slept → pass/fail).

## Key Concepts

`k-Nearest Neighbours` · `Decision Tree (Gini Impurity)` · `Gaussian Naive Bayes` · `Perceptron` · `Generalisation`

## Experimental Results

- All classifiers achieve >80% test accuracy on the synthetic dataset.
- k-NN (k=1) overfits (100% train accuracy) while k=5 generalises better.
- Comparison table printed at runtime: train accuracy vs test accuracy per model.

## Syllabus Reference

> *"Implement k-NN, Decision Tree, Naive Bayes, and Perceptron classifiers. Compare accuracy and generalisation on a held-out test set."*

## Files

| File | Description |
|------|-------------|
| [`main.py`](./main.py) | Complete standalone Python implementation |
| [`notebook.ipynb`](./notebook.ipynb) | Interactive Jupyter notebook with step-by-step cells |
| [`report.pdf`](./report.pdf) | Lab report — drop your PDF here |

## Usage

```bash
python main.py
```

---
*Course: 01AI0511 — Artificial Intelligence · Marwadi University*
