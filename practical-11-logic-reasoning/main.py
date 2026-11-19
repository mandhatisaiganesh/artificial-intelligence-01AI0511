"""
Practical 11: Logical Inference Using Propositional Logic
Course: 01AI0511 - Artificial Intelligence | Marwadi University

Problem Description:
  The system evaluates student exam eligibility based on:
  - P = Student attendance is at least 75%
  - Q = Student has completed all assignments
  - R = Student is eligible for examination

Logical Rule: (P and Q) -> R
"""

import sys


def evaluate_eligibility(name, attendance, assignments_completed):
    """Evaluates propositional logic facts and derives conclusion R."""
    P = attendance >= 75.0
    Q = str(assignments_completed).strip().lower() in ["yes", "y", "true", "1"]
    R = P and Q
    return P, Q, R


def display_inference(name, attendance, assignments_completed):
    """Formats and prints the propositional logic inference steps."""
    P, Q, R = evaluate_eligibility(name, attendance, assignments_completed)

    print("\n" + "=" * 50)
    print("           LOGICAL INFERENCE")
    print("=" * 50)
    print(f"\nStudent Name: {name}")
    print("\nPropositional Facts:")
    print(f"P: Attendance is at least 75% = {P}")
    print(f"Q: All assignments completed = {Q}")
    print("\nApplying Logical Rule:")
    print("(P AND Q) -> R")

    if R:
        print("\nConclusion: Student is ELIGIBLE")
        print("The student can appear for the examination.")
    else:
        print("\nConclusion: Student is NOT ELIGIBLE")
        if not P:
            print("- Attendance is below 75%.")
        if not Q:
            print("- All assignments are not completed.")

    print("\n" + "=" * 50)
    print("           PROGRAM COMPLETED")
    print("=" * 50)
    return R


def run_interactive():
    print("=" * 50)
    print("       STUDENT EXAM ELIGIBILITY SYSTEM")
    print("=" * 50)
    name = input("\nEnter student name: ")
    attendance = float(input("Enter attendance percentage: "))
    assignments = input("Have you completed all assignments? (yes/no): ").lower()
    display_inference(name, attendance, assignments)


if __name__ == "__main__":
    if "--interactive" in sys.argv or "-i" in sys.argv:
        run_interactive()
    else:
        print("=" * 50)
        print("       STUDENT EXAM ELIGIBILITY SYSTEM")
        print("=" * 50)

        test_cases = [
            {"name": "Likitha", "attendance": 87.0, "assignments": "yes"},
            {"name": "Rahul", "attendance": 68.0, "assignments": "yes"},
            {"name": "Sneha", "attendance": 82.0, "assignments": "no"},
        ]

        for case in test_cases:
            display_inference(case["name"], case["attendance"], case["assignments"])
