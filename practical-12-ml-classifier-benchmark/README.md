# Practical 12 — Implement and Compare AI Learning Models

> **Supervised Classifier Benchmark on Iris Dataset: k-NN, Decision Tree, Naive Bayes, Perceptron**  
> AI Pillar: Probabilistic & Machine Learning  
> Status: Completed & Verified

## Objective

To implement AI learning models such as **k-NN**, **Decision Tree**, **Naive Bayes (Gaussian)**, and **Perceptron** and compare their performance on the classic Fisher's Iris dataset.

## Dataset Specification

The Iris dataset (`Iris.csv`) contains 150 samples of flowers across three species:
- **Features (4):** Sepal Length (cm), Sepal Width (cm), Petal Length (cm), Petal Width (cm)
- **Target Label (3 classes):** `Iris-setosa`, `Iris-versicolor`, `Iris-virginica`
- **Data Partition:** 80% / 20% stratified train-test split (120 training, 30 testing samples, `random_state=42`).

## Models Evaluated

1. **k-Nearest Neighbors (k-NN):** $k = 5$ neighbors with `StandardScaler` feature normalization.
2. **Decision Tree Classifier:** Gini impurity splitting criterion (`random_state=42`).
3. **Naive Bayes (Gaussian):** Continuous Gaussian likelihood estimation with class priors.
4. **Perceptron:** Linear classification with `StandardScaler` (`max_iter=1000, random_state=42`).

## Experimental Results

| Algorithm | Testing Accuracy (%) | Best Model | Notes |
|---|:---:|:---:|---|
| **k-NN ($k=5$)** | **93.33%** | | High precision on Setosa & Virginica |
| **Decision Tree** | **93.33%** | | Balanced 0.90+ recall across all classes |
| **Naive Bayes (Gaussian)** | **96.67%** | 🏆 **Best** | Highest overall accuracy; only 1 misclassification |
| **Perceptron** | **86.67%** | | Lower accuracy due to non-linear class overlap between Versicolor & Virginica |

## Files

| File | Description |
|------|-------------|
| [`main.py`](./main.py) | Standalone Python implementation (supports both Scikit-learn and pure stdlib) |
| [`notebook.ipynb`](./notebook.ipynb) | Interactive Jupyter notebook with model pipelines and evaluation |
| [`Iris.csv`](./Iris.csv) | Canonical 150-sample Iris dataset |
| [`report.pdf`](./report.pdf) | Official verified laboratory report (7 pages) |

## Usage

```bash
python main.py
```

---
*Course: 01AI0511 — Artificial Intelligence · Marwadi University*
