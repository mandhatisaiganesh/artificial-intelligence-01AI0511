"""
Practical 5: Rule-based expert system (medical advisory) with forward and
backward chaining and an explanation facility.

DISCLAIMER: toy educational system, not medical advice.
"""

# Each rule: (name, set of conditions, conclusion)
RULES = [
    ("R1", {"fever", "cough"}, "flu_like"),
    ("R2", {"fever", "rash"}, "measles_like"),
    ("R3", {"sneezing", "runny_nose"}, "cold_like"),
    ("R4", {"flu_like", "body_ache"}, "influenza"),
    ("R5", {"cold_like", "no_fever"}, "common_cold"),
    ("R6", {"influenza"}, "advise_rest_fluids_see_doctor"),
    ("R7", {"common_cold"}, "advise_rest_and_fluids"),
    ("R8", {"measles_like"}, "advise_see_doctor_isolate"),
]


def forward_chain(facts):
    facts = set(facts)
    trace = []
    changed = True
    while changed:
        changed = False
        for name, conds, concl in RULES:
            if conds <= facts and concl not in facts:
                facts.add(concl)
                trace.append((name, conds, concl))
                changed = True
    return facts, trace


def backward_chain(goal, facts, depth=0, trace=None):
    """Return True if goal is provable from facts; record explanation."""
    trace = trace if trace is not None else []
    pad = "  " * depth
    if goal in facts:
        trace.append(f"{pad}{goal}: given fact")
        return True
    for name, conds, concl in RULES:
        if concl == goal:
            trace.append(f"{pad}{goal}: try {name} needs {sorted(conds)}")
            if all(backward_chain(c, facts, depth + 1, trace) for c in conds):
                return True
    trace.append(f"{pad}{goal}: cannot be proven")
    return False


def explain(trace):
    for name, conds, concl in trace:
        print(f"  {name}: IF {' AND '.join(sorted(conds))} THEN {concl}")


if __name__ == "__main__":
    cases = {
        "Case 1": {"fever", "cough", "body_ache"},
        "Case 2": {"sneezing", "runny_nose", "no_fever"},
        "Case 3": {"fever", "rash"},
    }
    for label, facts in cases.items():
        print(f"\n{label} symptoms: {sorted(facts)}")
        derived, trace = forward_chain(facts)
        print(" Forward chaining derived:", sorted(derived - facts))
        print(" Explanation (why):")
        explain(trace)

    print("\nBackward chaining: is 'influenza' provable for Case 1?")
    t = []
    ok = backward_chain("influenza", cases["Case 1"], trace=t)
    print("\n".join(t))
    print("Result:", ok)
