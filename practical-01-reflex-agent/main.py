"""
Practical 1: Simple Reflex Agent - Vacuum Cleaner World
Course: 01AI0511 - Artificial Intelligence | Marwadi University
"""

class VacuumEnvironment:
    """A two-room environment (Room A and Room B) that can be Clean or Dirty."""
    def __init__(self, status=None):
        self.locations = ["A", "B"]
        self.status = status if status else {"A": "Dirty", "B": "Dirty"}

    def display(self):
        print(f"Room A: {self.status['A']:<6} | Room B: {self.status['B']:<6}")


class SimpleReflexVacuumAgent:
    """Simple reflex agent driven by condition-action rules without internal state."""
    def __init__(self):
        self.location = "A"
        self.performance = 0

    def act(self, environment):
        percept = environment.status[self.location]
        print(f"Agent at {self.location} | Percept: {percept}")

        if percept == "Dirty":
            print(f"Action : SUCK (cleaning Room {self.location})")
            environment.status[self.location] = "Clean"
            self.performance += 10
        elif self.location == "A":
            print("Action : MOVE RIGHT")
            self.location = "B"
            self.performance -= 1
        elif self.location == "B":
            print("Action : MOVE LEFT")
            self.location = "A"
            self.performance -= 1


if __name__ == "__main__":
    env = VacuumEnvironment()
    agent = SimpleReflexVacuumAgent()

    print("=" * 55)
    print(" SIMPLE REFLEX AGENT - VACUUM CLEANER WORLD")
    print("=" * 55)

    print("\nInitial Environment State:")
    env.display()
    print("-" * 55)

    steps = 6
    for step in range(1, steps + 1):
        print(f"\nStep {step}")
        agent.act(env)
        env.display()

    print("-" * 55)
    print(f"Total Performance Score : {agent.performance}")
    print("Final Environment State :")
    env.display()
    print("=" * 55)
