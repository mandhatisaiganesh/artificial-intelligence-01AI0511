"""
Practical 1: Simple Reflex Agent and Goal-Based Agent in a toy environment.

Environment: the classic two-room vacuum world (rooms A and B).
- Simple reflex agent: acts only on the current percept (location, status).
- Goal-based agent: plans a sequence of actions to reach a goal state
  (both rooms clean) using a model of the environment.

Python environment setup (run once):
    python3 -m venv venv
    source venv/bin/activate          # Windows: venv\\Scripts\\activate
    pip install numpy matplotlib      # optional; this file uses only stdlib
"""

from collections import deque
import random


# ----------------------------- Environment ---------------------------------
class VacuumWorld:
    """Two rooms: 'A' and 'B'. Each room is 'Clean' or 'Dirty'."""

    def __init__(self, loc="A", status=None):
        self.loc = loc
        self.status = status or {"A": random.choice(["Clean", "Dirty"]),
                                 "B": random.choice(["Clean", "Dirty"])}
        self.score = 0

    def percept(self):
        return self.loc, self.status[self.loc]

    def execute(self, action):
        if action == "Suck":
            if self.status[self.loc] == "Dirty":
                self.score += 10
            self.status[self.loc] = "Clean"
        elif action == "Right":
            self.loc = "B"
            self.score -= 1
        elif action == "Left":
            self.loc = "A"
            self.score -= 1
        # "NoOp" does nothing

    def is_clean(self):
        return all(s == "Clean" for s in self.status.values())


# ----------------------------- Agents --------------------------------------
def simple_reflex_agent(percept):
    """Condition-action rules based only on the current percept."""
    loc, status = percept
    if status == "Dirty":
        return "Suck"
    return "Right" if loc == "A" else "Left"


class GoalBasedAgent:
    """Uses a model of the world and BFS to find a plan reaching the goal."""

    ACTIONS = ["Suck", "Left", "Right"]

    def __init__(self):
        self.plan = []

    @staticmethod
    def _result(state, action):
        loc, a, b = state
        if action == "Suck":
            return (loc, "Clean", b) if loc == "A" else (loc, a, "Clean")
        if action == "Left":
            return ("A", a, b)
        if action == "Right":
            return ("B", a, b)
        return state

    @staticmethod
    def _goal(state):
        return state[1] == "Clean" and state[2] == "Clean"

    def _bfs(self, start):
        frontier = deque([(start, [])])
        seen = {start}
        while frontier:
            state, path = frontier.popleft()
            if self._goal(state):
                return path
            for act in self.ACTIONS:
                nxt = self._result(state, act)
                if nxt not in seen:
                    seen.add(nxt)
                    frontier.append((nxt, path + [act]))
        return []

    def act(self, world):
        if not self.plan:
            start = (world.loc, world.status["A"], world.status["B"])
            self.plan = self._bfs(start)
        return self.plan.pop(0) if self.plan else "NoOp"


# ----------------------------- Run -----------------------------------------
def run(agent_name, world, max_steps=10):
    print(f"\n=== {agent_name} === start: loc={world.loc}, status={world.status}")
    agent = GoalBasedAgent() if agent_name == "Goal-based agent" else None
    for step in range(1, max_steps + 1):
        if world.is_clean() and agent_name == "Goal-based agent":
            break
        if agent:
            action = agent.act(world)
        else:
            action = simple_reflex_agent(world.percept())
        world.execute(action)
        print(f"Step {step}: action={action:5s} -> loc={world.loc}, status={world.status}")
        if world.is_clean() and agent is None:
            break
    print(f"Goal reached: {world.is_clean()} | Score: {world.score}")


if __name__ == "__main__":
    random.seed(1)
    init = {"A": "Dirty", "B": "Dirty"}
    run("Simple reflex agent", VacuumWorld("A", dict(init)))
    run("Goal-based agent", VacuumWorld("A", dict(init)))
