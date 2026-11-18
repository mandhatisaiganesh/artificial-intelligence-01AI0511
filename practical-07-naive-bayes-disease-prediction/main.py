"""
Practical 7: Probabilistic Classifier (Naive Bayes) for Disease Prediction
Course: 01AI0511 - Artificial Intelligence | Marwadi University
"""

import math

# Use scikit-learn GaussianNB if available; otherwise provide zero-dependency fallback
try:
    from sklearn.naive_bayes import GaussianNB
except ImportError:
    class GaussianNB:
        """Lightweight standard-library implementation of Gaussian Naive Bayes."""
        def __init__(self):
            self.classes_ = []
            self.stats = {}
            self.priors = {}

        def fit(self, X, y):
            self.classes_ = sorted(list(set(y)))
            n = len(y)
            for c in self.classes_:
                c_rows = [X[i] for i in range(n) if y[i] == c]
                self.priors[c] = len(c_rows) / n
                self.stats[c] = []
                num_features = len(X[0])
                for f in range(num_features):
                    vals = [row[f] for row in c_rows]
                    mean = sum(vals) / len(vals)
                    var = sum((v - mean) ** 2 for v in vals) / len(vals) + 1e-9
                    self.stats[c].append((mean, var))
            return self

        def predict_proba(self, X):
            results = []
            for row in X:
                scores = []
                for c in self.classes_:
                    log_p = math.log(self.priors[c])
                    for f, (mean, var) in enumerate(self.stats[c]):
                        val = row[f]
                        log_p += -0.5 * math.log(2 * math.pi * var) - ((val - mean) ** 2) / (2 * var)
                    scores.append(math.exp(log_p))
                total = sum(scores)
                results.append([s / total for s in scores])
            return results

        def predict(self, X):
            probas = self.predict_proba(X)
            return [self.classes_[row.index(max(row))] for row in probas]


# Canonical 5-symptom training dataset from Lab Manual:
# Features: [Fever, Cough, Headache, Body Pain, Sore Throat]
X = [
    [1, 1, 1, 1, 1],  # Flu
    [1, 1, 1, 1, 0],  # Flu
    [1, 1, 0, 1, 1],  # Flu
    [0, 1, 0, 0, 1],  # Cold
    [0, 1, 1, 0, 1],  # Cold
    [0, 1, 0, 0, 0],  # Cold
    [0, 0, 1, 0, 0],  # Migraine
    [0, 0, 1, 1, 0],  # Migraine
]

y = [
    "Flu", "Flu", "Flu",
    "Cold", "Cold", "Cold",
    "Migraine", "Migraine"
]

model = GaussianNB()
model.fit(X, y)


def predict_disease(symptoms):
    """
    symptoms: list of 5 binary integers [Fever, Cough, Headache, Body Pain, Sore Throat]
    """
    patient = [symptoms]
    pred = model.predict(patient)[0]
    probs = model.predict_proba(patient)[0]
    prob_dict = {cls: prob * 100.0 for cls, prob in zip(model.classes_, probs)}
    return pred, prob_dict


if __name__ == "__main__":
    print("=" * 55)
    print(" NAIVE BAYES DISEASE PREDICTION SYSTEM")
    print("=" * 55)

    test_vectors = [
        {"name": "Test Flu", "symptoms": [1, 1, 1, 1, 0], "desc": "Fever=1, Cough=1, Headache=1, BodyPain=1, SoreThroat=0"},
        {"name": "Test Cold", "symptoms": [0, 1, 0, 0, 1], "desc": "Fever=0, Cough=1, Headache=0, BodyPain=0, SoreThroat=1"},
        {"name": "Test Migraine", "symptoms": [0, 0, 1, 0, 0], "desc": "Fever=0, Cough=0, Headache=1, BodyPain=0, SoreThroat=0"}
    ]

    for tv in test_vectors:
        pred, probs = predict_disease(tv["symptoms"])
        print(f"\nScenario: {tv['name']} ({tv['desc']})")
        print(f"  Predicted Disease: {pred}")
        print("  Probabilities:")
        for dis, p in probs.items():
            print(f"    {dis:<10}: {p:6.2f}%")

    print("\nNote: This is an educational demonstration, not a medical diagnosis.")
    print("=" * 55)
