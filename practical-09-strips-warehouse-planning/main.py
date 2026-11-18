"""
Practical 9: STRIPS and Goal-Stack Planning with Uniform Cost Search
Domain: AI Warehouse Robot between Charging Station and 5 Rooms
Course: 01AI0511 - Artificial Intelligence | Marwadi University
"""

import heapq
from collections import namedtuple, defaultdict

Action = namedtuple("Action", ["name", "pre", "add", "dele", "cost"])

EDGES = {
    ("Charging", "R1"): 4,
    ("Charging", "R2"): 5,
    ("R1", "R2"): 3,
    ("R1", "R3"): 4,
    ("R2", "R3"): 3,
    ("R3", "R4"): 5,
    ("R3", "R5"): 4,
    ("R4", "R5"): 3
}


def build_actions(blocked_corridors=None):
    blocked = blocked_corridors or set()
    acts = []

    # Bidirectional MOVE
    for (a, b), c in EDGES.items():
        if (a, b) not in blocked and (b, a) not in blocked:
            acts.append(Action(f"MOVE({a}->{b})", {f"At(Robot,{a})"}, {f"At(Robot,{b})"}, {f"At(Robot,{a})"}, c))
            acts.append(Action(f"MOVE({b}->{a})", {f"At(Robot,{b})"}, {f"At(Robot,{a})"}, {f"At(Robot,{b})"}, c))

    # PICK and DROP for rooms 1-5
    for r in ["R1", "R2", "R3", "R4", "R5"]:
        for p in ["P1", "P2", "P3", "P4", "P5"]:
            # PICK
            acts.append(Action(
                f"PICK({p},{r})",
                {f"At(Robot,{r})", f"At({p},{r})", "GripperEmpty"},
                {f"Holding({p})"},
                {f"At({p},{r})", "GripperEmpty"},
                1
            ))
            # DROP
            acts.append(Action(
                f"DROP({p},{r})",
                {f"At(Robot,{r})", f"Holding({p})"},
                {f"At({p},{r})", "GripperEmpty", "Delivered"},
                {f"Holding({p})"},
                1
            ))
    return acts


def ucs_plan(init_state, goal_predicates, actions):
    """Uniform-Cost Search over state space."""
    # Index actions by robot location precondition for speed
    by_loc = defaultdict(list)
    general_acts = []
    for a in actions:
        loc_pre = [p for p in a.pre if p.startswith("At(Robot,")]
        if loc_pre:
            by_loc[loc_pre[0]].append(a)
        else:
            general_acts.append(a)

    pq = [(0, 0, frozenset(init_state), [])]
    best = {}
    tie = 0
    expanded = 0

    while pq:
        cost, _, state, plan = heapq.heappop(pq)
        if state in best and best[state] <= cost:
            continue
        best[state] = cost
        expanded += 1

        if goal_predicates.issubset(state):
            return plan, cost, expanded

        # Candidate actions based on robot location
        r_loc = [p for p in state if p.startswith("At(Robot,")]
        candidates = general_acts[:]
        if r_loc:
            candidates.extend(by_loc[r_loc[0]])

        for a in candidates:
            if a.pre.issubset(state):
                nxt = frozenset((state - a.dele) | a.add)
                nc = cost + a.cost
                if nxt not in best or nc < best[nxt]:
                    tie += 1
                    heapq.heappush(pq, (nc, tie, nxt, plan + [a.name]))

    return None, float("inf"), expanded


if __name__ == "__main__":
    print("=" * 65)
    print(" STRIPS WAREHOUSE ROBOT PLANNING (GOAL-STACK + UCS)")
    print("=" * 65)

    init_state = {"At(Robot,Charging)", "GripperEmpty", "At(P2,R2)", "At(P5,R5)"}
    goal_state = {"Delivered", "At(Robot,Charging)", "At(P2,R4)"}

    # Scenario 1: Canonical run (Destination = Room 4)
    actions = build_actions()
    plan, cost, exp = ucs_plan(init_state, {"Delivered", "At(Robot,Charging)"}, actions)

    print("\nScenario 1: Deliver any parcel to destination")
    print(f"Total plan cost : {cost}")
    print(f"States expanded : {exp}")
    print(f"Action count    : {len(plan)}")
    print("Action sequence :")
    for i, a in enumerate(plan, 1):
        print(f"  {i}. {a}")

    # Scenario 2: Corridor Room 2 - Room 3 blocked (Re-planning)
    blocked_actions = build_actions(blocked_corridors={("R2", "R3")})
    plan2, cost2, exp2 = ucs_plan(init_state, {"Delivered", "At(Robot,Charging)"}, blocked_actions)

    print(f"\nScenario 2: Corridor R2-R3 blocked (Dynamic Re-planning)")
    print(f"Re-planned cost : {cost2}")
    print(f"States expanded : {exp2}")
    print("Action sequence :")
    for i, a in enumerate(plan2, 1):
        print(f"  {i}. {a}")
    print("=" * 65)
