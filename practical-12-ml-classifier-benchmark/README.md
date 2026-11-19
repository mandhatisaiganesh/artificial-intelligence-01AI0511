# Practical 12 — Implement and Compare AI Learning Models

> **Supervised Classifier Benchmark: k-NN, Decision Tree, Naive Bayes**  
> AI Pillar: Probabilistic & Machine Learning  
> Status: Completed & Verified

## Objective

To implement simple AI learning models such as **k-NN**, **Decision Tree**, and **Naive Bayes** and compare their performance on a toy dataset predicting student performance (Pass/Fail).

## Dataset Specification

The dataset consists of 16 student records with 2 input features:
- **Feature 1:** Study Hours ($1 \dots 10$)
- **Feature 2:** Attendance Percentage ($40\% \dots 98\%$)
- **Target Label:** Performance ($0 = \text{Fail}$, $1 = \text{Pass}$)

### Data Split
- Test size: $25\%$ ($4$ testing samples, $12$ training samples)
- Stratified sampling with random state $42$ ensures balanced class distribution in train and test splits.

## Models Evaluated

1. **k-Nearest Neighbors (k-NN):** $k = 3$ neighbors using Euclidean distance metric.
2. **Decision Tree Classifier:** Gini impurity splitting criterion (`random_state=42`).
3. **Gaussian Naive Bayes:** Continuous Gaussian likelihood estimation with class priors.

## Experimental Results

| Model | Predicted Labels on Test Set | Actual Ground Truth | Accuracy |
|---|:---:|:---:|:---:|
| **k-Nearest Neighbors ($k=3$)** | `[0, 1, 0, 1]` | `[0, 1, 0, 1]` | **100.0%** |
| **Decision Tree Classifier** | `[0, 1, 0, 1]` | `[0, 1, 0, 1]` | **100.0%** |
| **Gaussian Naive Bayes** | `[0, 1, 0, 1]` | `[0, 1, 0, 1]` | **100.0%** |

## Files

| File | Description |
|------|-------------|
| [`main.py`](./main.py) | Full implementation (with Scikit-learn + zero-dependency fallback) |
| [`notebook.ipynb`](./notebook.ipynb) | Interactive Jupyter notebook comparing all 3 classifiers |
| [`report.pdf`](./report.pdf) | Official laboratory report submitted for evaluation |

## Usage

```bash
python main.py
```

---
*Course: 01AI0511 — Artificial Intelligence · Marwadi University*
