"""
Practical 9: STRIPS representation and Goal-Stack Planning for Blocks World.

State: set of ground predicates, e.g. On(A,B), OnTable(C), Clear(A), ArmEmpty, Holding(X)
Operators: Pickup(x), Putdown(x), Stack(x,y), Unstack(x,y)
"""


# Each operator -> (preconditions, add list, delete list)
def operator(name, *args):
    if name == "Pickup":
        (x,) = args
        return ({("OnTable", x), ("Clear", x), ("ArmEmpty",)},
                {("Holding", x)},
                {("OnTable", x), ("Clear", x), ("ArmEmpty",)})
    if name == "Putdown":
        (x,) = args
        return ({("Holding", x)},
                {("OnTable", x), ("Clear", x), ("ArmEmpty",)},
                {("Holding", x)})
    if name == "Stack":
        x, y = args
        return ({("Holding", x), ("Clear", y)},
                {("On", x, y), ("Clear", x), ("ArmEmpty",)},
                {("Holding", x), ("Clear", y)})
    if name == "Unstack":
        x, y = args
        return ({("On", x, y), ("Clear", x), ("ArmEmpty",)},
                {("Holding", x), ("Clear", y)},
                {("On", x, y), ("Clear", x), ("ArmEmpty",)})
    raise ValueError(name)


def achievers(pred, state):
    """Operators that can add the given predicate, chosen using the current state
    so that the operator is actually relevant (e.g. unstack the block that is
    really on top of x, or the block we are holding)."""
    kind = pred[0]
    if kind == "Holding":
        x = pred[1]
        below = [p[2] for p in state if p[0] == "On" and p[1] == x]
        if below:
            return [("Unstack", x, below[0])]
        return [("Pickup", x)]
    if kind == "On":
        return [("Stack", pred[1], pred[2])]
    if kind == "OnTable":
        return [("Putdown", pred[1])]
    if kind == "Clear":
        x = pred[1]
        above = [p[1] for p in state if p[0] == "On" and p[2] == x]
        if above:
            return [("Unstack", above[0], x)]
        held = [p for p in state if p == ("Holding", x)]
        if held:
            return [("Putdown", x)]
        return []
    if kind == "ArmEmpty":
        held = [p[1] for p in state if p[0] == "Holding"]
        return [("Putdown", held[0])] if held else []
    return []


BLOCKS = []


def goal_stack_plan(initial, goal, limit=5000):
    state = set(initial)
    stack = [("GOALSET", frozenset(goal))]
    plan = []
    steps = 0
    while stack and steps < limit:
        steps += 1
        kind, item = stack.pop()
        if kind == "GOALSET":
            unsatisfied = [g for g in item if g not in state]
            if unsatisfied:
                stack.append(("GOALSET", item))
                for g in unsatisfied:
                    stack.append(("PRED", g))
        elif kind == "PRED":
            if item in state:
                continue
            # choose an achiever whose preconditions are most likely satisfiable
            candidates = achievers(item, state)
            if not candidates:
                continue
            op = candidates[0]
            stack.append(("OP", op))
            pre, _, _ = operator(*op)
            stack.append(("GOALSET", frozenset(pre)))
        elif kind == "OP":
            pre, add, dele = operator(*item)
            if pre <= state:
                state = (state - dele) | add
                plan.append(item)
            else:
                stack.append(("OP", item))
                stack.append(("GOALSET", frozenset(pre)))
    return plan, state


def fmt(op):
    return f"{op[0]}({', '.join(op[1:])})"


if __name__ == "__main__":
    BLOCKS[:] = ["A", "B", "C"]
    # Initial: C on A, B on table. A on table.   Goal: A on B, B on C
    initial = {("On", "C", "A"), ("OnTable", "A"), ("OnTable", "B"),
               ("Clear", "C"), ("Clear", "B"), ("ArmEmpty",)}
    goal = {("On", "A", "B"), ("On", "B", "C")}
    plan, final = goal_stack_plan(initial, goal)
    print("Initial:", sorted(initial))
    print("Goal   :", sorted(goal))
    print("\nPlan:")
    for i, op in enumerate(plan, 1):
        print(f" {i}. {fmt(op)}")
    print("\nGoal satisfied:", goal <= final)
    print("Plan length:", len(plan))
