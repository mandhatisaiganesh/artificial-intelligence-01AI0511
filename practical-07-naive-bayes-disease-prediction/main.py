"""
Practical 7: Bayesian network inference (classic Burglary-Alarm network)
implemented from scratch (inference by enumeration), plus a Naive Bayes
probabilistic classifier. Uses only the standard library.

Optional library version (if you can pip install):
    pip install pgmpy
    -> build BayesianNetwork + VariableElimination for the same network.
"""

from itertools import product

# Network: Burglary -> Alarm <- Earthquake ; Alarm -> JohnCalls, Alarm -> MaryCalls
P_B = 0.001
P_E = 0.002
P_A = {(True, True): 0.95, (True, False): 0.94, (False, True): 0.29, (False, False): 0.001}
P_J = {True: 0.90, False: 0.05}
P_M = {True: 0.70, False: 0.01}
VARS = ["B", "E", "A", "J", "M"]


def joint(a):
    """Joint probability for a full assignment dict."""
    p = P_B if a["B"] else 1 - P_B
    p *= P_E if a["E"] else 1 - P_E
    pa = P_A[(a["B"], a["E"])]
    p *= pa if a["A"] else 1 - pa
    pj = P_J[a["A"]]
    p *= pj if a["J"] else 1 - pj
    pm = P_M[a["A"]]
    p *= pm if a["M"] else 1 - pm
    return p


def enumerate_query(query_var, evidence):
    """P(query_var | evidence) by summing the joint over hidden variables."""
    dist = {}
    for qval in (True, False):
        total = 0.0
        for vals in product((True, False), repeat=len(VARS)):
            a = dict(zip(VARS, vals))
            if a[query_var] != qval:
                continue
            if any(a[k] != v for k, v in evidence.items()):
                continue
            total += joint(a)
        dist[qval] = total
    z = sum(dist.values())
    return {k: v / z for k, v in dist.items()}


# ---------------- Naive Bayes classifier (play-tennis style data) ------------
DATA = [
    ("Sunny", "Hot", "High", "No"), ("Sunny", "Hot", "High", "No"),
    ("Overcast", "Hot", "High", "Yes"), ("Rainy", "Mild", "High", "Yes"),
    ("Rainy", "Cool", "Normal", "Yes"), ("Rainy", "Cool", "Normal", "No"),
    ("Overcast", "Cool", "Normal", "Yes"), ("Sunny", "Mild", "High", "No"),
    ("Sunny", "Cool", "Normal", "Yes"), ("Rainy", "Mild", "Normal", "Yes"),
    ("Sunny", "Mild", "Normal", "Yes"), ("Overcast", "Mild", "High", "Yes"),
    ("Overcast", "Hot", "Normal", "Yes"), ("Rainy", "Mild", "High", "No"),
]


def naive_bayes_predict(x):
    labels = {r[-1] for r in DATA}
    scores = {}
    for lab in labels:
        rows = [r for r in DATA if r[-1] == lab]
        p = len(rows) / len(DATA)
        for i, v in enumerate(x):
            vocab = {r[i] for r in DATA}
            # Laplace smoothing
            p *= (sum(1 for r in rows if r[i] == v) + 1) / (len(rows) + len(vocab))
        scores[lab] = p
    z = sum(scores.values())
    return {k: v / z for k, v in scores.items()}


if __name__ == "__main__":
    print("Bayesian network: Burglary / Earthquake / Alarm / John / Mary")
    r = enumerate_query("B", {"J": True, "M": True})
    print(f"P(Burglary | JohnCalls, MaryCalls) = {r[True]:.4f}")
    r = enumerate_query("A", {"J": True})
    print(f"P(Alarm | JohnCalls)               = {r[True]:.4f}")
    r = enumerate_query("B", {"A": True})
    print(f"P(Burglary | Alarm)                = {r[True]:.4f}")

    print("\nNaive Bayes classifier (Outlook, Temp, Humidity -> Play)")
    for x in (("Sunny", "Cool", "High"), ("Overcast", "Mild", "Normal")):
        post = naive_bayes_predict(x)
        pred = max(post, key=post.get)
        print(f"{x} -> {pred}  {({k: round(v, 3) for k, v in post.items()})}")
