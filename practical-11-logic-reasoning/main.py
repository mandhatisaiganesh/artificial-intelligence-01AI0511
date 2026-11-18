"""
Practical 11: Represent a real-world problem in propositional logic and derive
conclusions using (a) truth-table model checking and (b) resolution refutation.

Scenario (Smart campus access):
  1. If a student has a valid ID and the lab is open, the student can enter.   (V & L) -> E
  2. If it is a holiday, the lab is not open.                                  H -> ~L
  3. The student has a valid ID.                                               V
  4. It is not a holiday.                                                      ~H
  5. The lab is open on non-holidays.                                          ~H -> L
Query: Can the student enter (E)?
"""

from itertools import product

SYMBOLS = ["V", "L", "E", "H"]


# ---------- (a) Model checking via truth table -------------------------------
def kb_true(m):
    imp = lambda a, b: (not a) or b
    return (imp(m["V"] and m["L"], m["E"])
            and imp(m["H"], not m["L"])
            and m["V"]
            and not m["H"]
            and imp(not m["H"], m["L"]))


def entails(query):
    models = [dict(zip(SYMBOLS, v)) for v in product([True, False], repeat=len(SYMBOLS))]
    kb_models = [m for m in models if kb_true(m)]
    return all(query(m) for m in kb_models), len(kb_models), len(models)


# ---------- (b) Resolution refutation on CNF clauses -------------------------
# Clause = frozenset of literals; negation marked with '~'
def neg(l):
    return l[1:] if l.startswith("~") else "~" + l


KB_CNF = [
    {"~V", "~L", "E"},   # (V & L) -> E
    {"~H", "~L"},        # H -> ~L
    {"V"},
    {"~H"},
    {"H", "L"},          # ~H -> L
]


def resolve(c1, c2):
    out = []
    for lit in c1:
        if neg(lit) in c2:
            new = (c1 - {lit}) | (c2 - {neg(lit)})
            # skip tautologies
            if not any(neg(x) in new for x in new):
                out.append(frozenset(new))
    return out


def resolution_prove(kb, query):
    clauses = {frozenset(c) for c in kb} | {frozenset({neg(query)})}
    steps = []
    while True:
        new = set()
        lst = list(clauses)
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                for r in resolve(lst[i], lst[j]):
                    steps.append((set(lst[i]), set(lst[j]), set(r)))
                    if not r:
                        return True, steps
                    new.add(r)
        if new <= clauses:
            return False, steps
        clauses |= new


if __name__ == "__main__":
    print("KB (propositional logic):")
    print("  (V & L) -> E ;  H -> ~L ;  V ;  ~H ;  ~H -> L")

    result, kb_count, total = entails(lambda m: m["E"])
    print(f"\n(a) Truth-table: {kb_count} of {total} models satisfy the KB.")
    print(f"    KB |= E ?  {result}")

    proved, steps = resolution_prove(KB_CNF, "E")
    print(f"\n(b) Resolution refutation of ~E: KB |= E ?  {proved}")
    print("    Last few resolution steps:")
    for a, b, r in steps[-4:]:
        print(f"    {sorted(a)} + {sorted(b)} => {sorted(r) if r else '{} (empty clause)'}")

    result2, _, _ = entails(lambda m: m["H"])
    print(f"\nSanity check: KB |= H ?  {result2}  (expected False)")
