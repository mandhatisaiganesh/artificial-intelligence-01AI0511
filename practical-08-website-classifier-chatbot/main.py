"""
Practical 8: Mini AI application - Text classification (spam vs ham) with a
Naive Bayes classifier built from scratch, plus an ethics & explainability report.

Explainability: we show the top words that pushed each prediction.
"""

import math
import re
from collections import Counter

TRAIN = [
    ("win a free prize now click here", "spam"),
    ("congratulations you won cash claim your reward", "spam"),
    ("free entry limited offer urgent call now", "spam"),
    ("get cheap loans instantly no credit check", "spam"),
    ("exclusive deal free gift click link", "spam"),
    ("you have been selected for a free vacation", "spam"),
    ("are we meeting for lunch tomorrow", "ham"),
    ("please send the assignment before friday", "ham"),
    ("practical lab is rescheduled to monday", "ham"),
    ("can you share the notes from today's class", "ham"),
    ("happy birthday hope you have a great day", "ham"),
    ("let us study together for the exam", "ham"),
]
TEST = [
    ("claim your free cash prize now", "spam"),
    ("lab assignment notes for monday class", "ham"),
    ("urgent free loan offer click", "spam"),
    ("are you coming to the exam study group", "ham"),
]


def tokenize(t):
    return re.findall(r"[a-z']+", t.lower())


class NaiveBayesText:
    def fit(self, data):
        self.classes = {c for _, c in data}
        self.prior = {}
        self.counts = {c: Counter() for c in self.classes}
        for text, c in data:
            self.counts[c].update(tokenize(text))
        self.vocab = set().union(*[set(cnt) for cnt in self.counts.values()])
        n = len(data)
        for c in self.classes:
            self.prior[c] = sum(1 for _, y in data if y == c) / n
        self.total = {c: sum(self.counts[c].values()) for c in self.classes}

    def word_logp(self, w, c):
        return math.log((self.counts[c][w] + 1) / (self.total[c] + len(self.vocab)))

    def predict(self, text):
        words = [w for w in tokenize(text) if w in self.vocab]
        scores = {c: math.log(self.prior[c]) + sum(self.word_logp(w, c) for w in words)
                  for c in self.classes}
        pred = max(scores, key=scores.get)
        return pred, words

    def explain(self, words, pred):
        other = next(c for c in self.classes if c != pred)
        contrib = [(w, self.word_logp(w, pred) - self.word_logp(w, other)) for w in set(words)]
        return sorted(contrib, key=lambda x: -x[1])[:3]


ETHICS_REPORT = """
ETHICS & EXPLAINABILITY REPORT
------------------------------
Explainability : Naive Bayes is transparent; each word's log-likelihood ratio shows
                 why a message was flagged (printed above per prediction).
Fairness/Bias  : Training data is tiny and English-only; it may over-flag informal
                 or non-native writing. Real systems need diverse, audited data.
Privacy        : Emails are personal data. Use consent, anonymisation, and data
                 minimisation; do not log message content unnecessarily.
Safety         : False positives (real mail marked spam) can hide important
                 messages. Keep a human-in-the-loop 'review spam' folder.
Limitations    : Bag-of-words ignores context/sarcasm; evaluate with precision,
                 recall and F1, not accuracy alone, on a larger held-out set.
"""

if __name__ == "__main__":
    model = NaiveBayesText()
    model.fit(TRAIN)
    correct = 0
    for text, truth in TEST:
        pred, words = model.predict(text)
        correct += pred == truth
        why = ", ".join(f"{w}({s:+.2f})" for w, s in model.explain(words, pred))
        print(f"'{text}'\n  -> predicted={pred} (actual={truth}) | key words: {why}")
    print(f"\nAccuracy on toy test set: {correct}/{len(TEST)}")
    print(ETHICS_REPORT)
