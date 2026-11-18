"""
Practical 8: AI Website Classifier Chatbot Prototype
Course: 01AI0511 - Artificial Intelligence | Marwadi University
"""

import re

categories = {
    "Artificial Intelligence": [
        "ai", "artificial intelligence", "machine learning",
        "deep learning", "neural network", "chatgpt", "nlp", "llm"
    ],
    "Programming": ["python", "java", "c++", "programming", "coding"],
    "Cybersecurity": ["malware", "phishing", "hacking", "firewall"],
    "E-Commerce": ["buy", "shop", "shopping", "laptop", "cart", "store"],
    "Sports": ["cricket", "football", "match", "score", "player"]
}

website_types = {
    "Artificial Intelligence": "AI / ML Learning & Research Websites",
    "Programming": "Developer & Coding Portals",
    "Cybersecurity": "Security & Network Defense Hubs",
    "E-Commerce": "Online Shopping Websites",
    "Sports": "Live Sports & Scores Portals"
}


def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9+# ]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_keywords(text):
    clean = preprocess(text)
    detected = {}
    for cat, kws in categories.items():
        matches = []
        for kw in kws:
            pattern = r"\b" + re.escape(kw) + r"\b"
            if re.search(pattern, clean):
                matches.append(kw)
        if matches:
            detected[cat] = matches
    return detected


def classify_text(text):
    detected = extract_keywords(text)
    if not detected:
        return {
            "status": "unknown",
            "message": "Topic not identified. Try AI, Programming, Cybersecurity, E-Commerce, or Sports."
        }

    scores = {cat: len(kws) for cat, kws in detected.items()}
    highest = max(scores.values())
    best = [c for c, s in scores.items() if s == highest]

    if len(best) > 1:
        all_kw = []
        for b in best:
            all_kw.extend(detected[b])
        return {
            "status": "multiple",
            "categories": best,
            "keywords": all_kw,
            "message": f"Multiple topics detected: {' & '.join(best)} (Keywords: {', '.join(all_kw)})"
        }

    chosen = best[0]
    return {
        "status": "single",
        "category": chosen,
        "website_type": website_types.get(chosen, "General"),
        "keywords": detected[chosen],
        "confidence": 100.0
    }


if __name__ == "__main__":
    test_queries = [
        "I want to learn about machine learning and neural networks.",
        "I want to buy a new laptop online.",
        "How can I protect my computer from malware?",
        "Who won the cricket match?",
        "I want to learn Python for machine learning.",
        "Tell me about quantum physics."
    ]

    print("=" * 65)
    print(" AI WEBSITE CLASSIFIER CHATBOT")
    print("=" * 65)

    for q in test_queries:
        res = classify_text(q)
        print(f"\nInput: \"{q}\"")
        if res["status"] == "single":
            print(f"  Category     : {res['category']}")
            print(f"  Website Type : {res['website_type']}")
            print(f"  Keywords     : {', '.join(res['keywords'])}")
            print(f"  Confidence   : {res['confidence']:.0f}%")
        elif res["status"] == "multiple":
            print(f"  {res['message']}")
        else:
            print(f"  {res['message']}")
    print("=" * 65)
