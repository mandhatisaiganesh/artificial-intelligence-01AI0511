"""
Practical 12: Simple learning models (k-NN, Decision Tree, Naive Bayes,
Perceptron) implemented from scratch and compared on a toy dataset.

Dataset: a small 2-feature, 2-class problem (hours studied, hours slept -> pass/fail).
Split into train/test and compare accuracy.
"""

import math
import random
from collections import Counter

random.seed(42)


def make_data(n=120):
    data = []
    for _ in range(n):
        label = random.choice([0, 1])
        if label == 1:   # pass: more study, decent sleep
            x = (random.gauss(7, 1.5), random.gauss(7, 1.2))
        else:            # fail
            x = (random.gauss(3.5, 1.5), random.gauss(5, 1.5))
        data.append((x, label))
    random.shuffle(data)
    return data


# ------------------------------ k-NN ----------------------------------------
class KNN:
    def __init__(self, k=5):
        self.k = k

    def fit(self, data):
        self.data = data

    def predict(self, x):
        nearest = sorted(self.data, key=lambda d: math.dist(x, d[0]))[:self.k]
        return Counter(l for _, l in nearest).most_common(1)[0][0]


# --------------------------- Decision tree ----------------------------------
def gini(rows):
    if not rows:
        return 0
    c = Counter(l for _, l in rows)
    return 1 - sum((v / len(rows)) ** 2 for v in c.values())


class DecisionTree:
    def __init__(self, max_depth=3):
        self.max_depth = max_depth

    def fit(self, data):
        self.tree = self._build(data, 0)

    def _build(self, rows, depth):
        labels = Counter(l for _, l in rows)
        if depth >= self.max_depth or len(labels) == 1 or len(rows) < 4:
            return labels.most_common(1)[0][0]
        best = (None, None, 1e9)
        for f in range(2):
            for t in sorted({r[0][f] for r in rows}):
                left = [r for r in rows if r[0][f] <= t]
                right = [r for r in rows if r[0][f] > t]
                if not left or not right:
                    continue
                g = (len(left) * gini(left) + len(right) * gini(right)) / len(rows)
                if g < best[2]:
                    best = (f, t, g)
        if best[0] is None:
            return labels.most_common(1)[0][0]
        f, t, _ = best
        return (f, t,
                self._build([r for r in rows if r[0][f] <= t], depth + 1),
                self._build([r for r in rows if r[0][f] > t], depth + 1))

    def predict(self, x):
        node = self.tree
        while isinstance(node, tuple):
            f, t, l, r = node
            node = l if x[f] <= t else r
        return node


# ----------------------- Gaussian Naive Bayes -------------------------------
class GaussianNB:
    def fit(self, data):
        self.stats, self.prior = {}, {}
        for c in {l for _, l in data}:
            rows = [x for x, l in data if l == c]
            self.prior[c] = len(rows) / len(data)
            self.stats[c] = []
            for f in range(2):
                vals = [r[f] for r in rows]
                mu = sum(vals) / len(vals)
                var = sum((v - mu) ** 2 for v in vals) / len(vals) + 1e-9
                self.stats[c].append((mu, var))

    def predict(self, x):
        def logp(c):
            s = math.log(self.prior[c])
            for f, (mu, var) in enumerate(self.stats[c]):
                s += -0.5 * math.log(2 * math.pi * var) - (x[f] - mu) ** 2 / (2 * var)
            return s
        return max(self.stats, key=logp)


# ------------------------------ Perceptron ----------------------------------
class Perceptron:
    def __init__(self, lr=0.1, epochs=100):
        self.lr, self.epochs = lr, epochs

    def fit(self, data):
        self.w, self.b = [0.0, 0.0], 0.0
        # standardise features for stable training
        self.mu = [sum(d[0][f] for d in data) / len(data) for f in range(2)]
        self.sd = [math.sqrt(sum((d[0][f] - self.mu[f]) ** 2 for d in data) / len(data)) for f in range(2)]
        for _ in range(self.epochs):
            for x, y in data:
                err = y - self._raw(x)
                z = self._norm(x)
                self.w = [w + self.lr * err * zi for w, zi in zip(self.w, z)]
                self.b += self.lr * err

    def _norm(self, x):
        return [(x[f] - self.mu[f]) / self.sd[f] for f in range(2)]

    def _raw(self, x):
        z = self._norm(x)
        return 1 if sum(w * zi for w, zi in zip(self.w, z)) + self.b > 0 else 0

    def predict(self, x):
        return self._raw(x)


def accuracy(model, data):
    return sum(model.predict(x) == y for x, y in data) / len(data)


if __name__ == "__main__":
    data = make_data()
    split = int(0.7 * len(data))
    train, test = data[:split], data[split:]
    print(f"Train size={len(train)}, Test size={len(test)}\n")
    print(f"{'Model':<16}{'Train acc':>10}{'Test acc':>10}")
    for name, model in (("k-NN (k=5)", KNN(5)), ("Decision Tree", DecisionTree(3)),
                        ("Naive Bayes", GaussianNB()), ("Perceptron", Perceptron())):
        model.fit(train)
        print(f"{name:<16}{accuracy(model, train):>10.2f}{accuracy(model, test):>10.2f}")
    print("\nNote: k-NN has perfect-looking train accuracy only for k=1; compare test")
    print("accuracy for generalisation. Try changing k, tree depth and noise level.")
