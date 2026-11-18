"""
Practical 6: Constraint Satisfaction Problems using backtracking with
forward checking + MRV/LCV-style ordering and AC-3 arc consistency.
Problems: Map coloring (Australia) and N-Queens.
"""

from copy import deepcopy


class CSP:
    def __init__(self, domains, neighbors, constraint):
        self.domains = domains
        self.neighbors = neighbors
        self.constraint = constraint  # f(Xi, a, Xj, b) -> bool
        self.nodes = 0


def ac3(csp, domains):
    queue = [(xi, xj) for xi in domains for xj in csp.neighbors[xi]]
    while queue:
        xi, xj = queue.pop(0)
        revised = False
        for a in domains[xi][:]:
            if not any(csp.constraint(xi, a, xj, b) for b in domains[xj]):
                domains[xi].remove(a)
                revised = True
        if revised:
            if not domains[xi]:
                return False
            for xk in csp.neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True


def backtrack(csp, assignment, domains, forward_check=True):
    if len(assignment) == len(domains):
        return assignment
    # MRV: pick unassigned variable with smallest domain
    var = min((v for v in domains if v not in assignment), key=lambda v: len(domains[v]))
    for val in domains[var]:
        csp.nodes += 1
        if all(csp.constraint(var, val, n, assignment[n])
               for n in csp.neighbors[var] if n in assignment):
            new_domains = deepcopy(domains)
            new_domains[var] = [val]
            ok = True
            if forward_check:
                for n in csp.neighbors[var]:
                    if n not in assignment:
                        new_domains[n] = [b for b in new_domains[n]
                                          if csp.constraint(n, b, var, val)]
                        if not new_domains[n]:
                            ok = False
                            break
            if ok:
                assignment[var] = val
                result = backtrack(csp, assignment, new_domains, forward_check)
                if result:
                    return result
                del assignment[var]
    return None


def map_coloring():
    regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    borders = {("WA", "NT"), ("WA", "SA"), ("NT", "SA"), ("NT", "Q"), ("SA", "Q"),
               ("SA", "NSW"), ("SA", "V"), ("Q", "NSW"), ("NSW", "V")}
    nbrs = {r: [] for r in regions}
    for a, b in borders:
        nbrs[a].append(b)
        nbrs[b].append(a)
    domains = {r: ["Red", "Green", "Blue"] for r in regions}
    csp = CSP(domains, nbrs, lambda xi, a, xj, b: a != b)
    doms = deepcopy(domains)
    assert ac3(csp, doms)
    sol = backtrack(csp, {}, doms)
    print("Map coloring solution:", sol)
    print("Nodes tried:", csp.nodes)


def n_queens(n):
    cols = list(range(n))
    domains = {c: list(range(n)) for c in cols}
    nbrs = {c: [x for x in cols if x != c] for c in cols}

    def ok(ci, ri, cj, rj):
        return ri != rj and abs(ri - rj) != abs(ci - cj)

    csp = CSP(domains, nbrs, ok)
    sol = backtrack(csp, {}, deepcopy(domains))
    print(f"\n{n}-Queens solution (column -> row): {sol}  | nodes tried: {csp.nodes}")
    if sol:
        for r in range(n):
            print(" ".join("Q" if sol[c] == r else "." for c in range(n)))


if __name__ == "__main__":
    map_coloring()
    n_queens(8)
