# Practical 11 — Logical Inference Using Propositional Logic

> **Student Exam Eligibility System**  
> AI Pillar: Symbolic Knowledge & Planning  
> Status: Completed & Verified

## Objective

To represent a real-world problem using propositional logic and perform logical inference using Python to derive conclusions.

## Problem Formulation

The system checks student attendance and assignment completion to determine exam eligibility:
- **P** = Student has attendance of at least 75%.
- **Q** = Student has completed all assignments.
- **R** = Student is eligible for the examination.

### Logical Rule
$$\left( P \land Q \right) \longrightarrow R$$

If and only if both conditions $P$ and $Q$ hold true, the student is inferred to be eligible for the examination.

## Experimental Results

From the verified lab run:
- **Test Case 1 (Likitha):** Attendance = $87\%$, Assignments = `"yes"`
  - $P = \text{True}$, $Q = \text{True} \implies R = \text{True}$
  - **Conclusion:** Student is ELIGIBLE.
- **Test Case 2:** Attendance = $68\%$ ($< 75\%$), Assignments = `"yes"`
  - $P = \text{False}$, $Q = \text{True} \implies R = \text{False}$
  - **Conclusion:** Student is NOT ELIGIBLE (Attendance below 75%).
- **Test Case 3:** Attendance = $82\%$, Assignments = `"no"`
  - $P = \text{True}$, $Q = \text{False} \implies R = \text{False}$
  - **Conclusion:** Student is NOT ELIGIBLE (Assignments incomplete).

## Files

| File | Description |
|------|-------------|
| [`main.py`](./main.py) | Standalone Python program (supports interactive CLI & automated modes) |
| [`notebook.ipynb`](./notebook.ipynb) | Interactive Jupyter notebook with logic inference steps |
| [`report.pdf`](./report.pdf) | Official laboratory report submitted for evaluation |

## Usage

```bash
python main.py
```

---
*Course: 01AI0511 — Artificial Intelligence · Marwadi University*
