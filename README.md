# From Reflex Agents to Markov Decision Processes: Implementing Classical and Probabilistic AI Systems

**Engineering & Research Overview · Course 01AI0511 — Artificial Intelligence**  
*Department of Computer Science & Engineering (AI, ML & DS) · Faculty of Engineering & Technology · Marwadi University*  
**Author:** Sai Ganesh Mandhati (Enr: `92460118370` · Class: `5EN19` · Batch: `Lab B`)  
**Repository:** [github.com/mandhatisaiganesh/artificial-intelligence-01AI0511](https://github.com/mandhatisaiganesh/artificial-intelligence-01AI0511)

---

## Abstract

Modern artificial intelligence is often equated exclusively with deep neural networks and generative models. However, the foundational building blocks of autonomous reasoning—deterministic state-space exploration, constraint satisfaction, adversarial search, symbolic planning, probabilistic inference, and sequential decision-making under uncertainty—remain essential for verifiable, safety-critical, and compute-efficient intelligent systems.

This repository presents a unified, production-clean implementation of the twelve foundational paradigms of artificial intelligence mandated by the **01AI0511** curriculum at Marwadi University. Developed from first principles, every practical module includes a modular standalone Python implementation (`main.py`), a reproducible multi-cell Jupyter notebook (`notebook.ipynb`), an engineering README, and the verified laboratory report (`report.pdf`). The implementations emphasize mathematical correctness, zero unnecessary external dependencies, clean data structures, and empirical benchmarking.

---

## System Architecture & Paradigm Map

The twelve modules span five distinct computational paradigms of artificial intelligence, forming a coherent progression from reactive agents to reinforcement learning:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        01AI0511 — CORE AI PARADIGM ARCHITECTURE                        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  [1] AGENTS & DETERMINISTIC SEARCH                                                     │
│  ├── Practical 01: Simple Reflex Agent (Vacuum World Environment, Percept-Action Loop) │
│  ├── Practical 02: Uninformed Search (BFS, DFS, Uniform Cost Search on Weighted Graph) │
│  └── Practical 03: Heuristic Search (A* Algorithm on 20×20 Grid with Manhattan Metric) │
│                                                                                        │
│  [2] ADVERSARIAL REASONING & CONSTRAINT SATISFACTION                                   │
│  ├── Practical 04: Adversarial Search (Minimax with Alpha-Beta Pruning, Tic-Tac-Toe)  │
│  └── Practical 06: Constraint Satisfaction (Sudoku Solver with Backtracking & MRV)     │
│                                                                                        │
│  [3] SYMBOLIC KNOWLEDGE & AUTOMATED PLANNING                                           │
│  ├── Practical 05: Rule-Based Expert System (Smart Loan Advisor, Forward Chaining)     │
│  ├── Practical 09: Automated Planning (STRIPS Domain with Uniform Cost Search Planner) │
│  └── Practical 11: Deductive Logic (Propositional Model Checking & Resolution Refutation)
│                                                                                        │
│  [4] PROBABILISTIC INFERENCE & MACHINE LEARNING                                        │
│  ├── Practical 07: Probabilistic Classification (Gaussian Naive Bayes Disease Predictor)│
│  ├── Practical 08: Text Classification & Chatbot (Domain Entity Extraction & Matching)  │
│  └── Practical 12: Empirical Model Benchmarking (k-NN, Decision Tree, Naive Bayes, Perc)│
│                                                                                        │
│  [5] SEQUENTIAL DECISION-MAKING & REINFORCEMENT LEARNING                               │
│  └── Practical 10: Value Iteration on MDP (Bellman Optimality on Grid-World with Obs)  │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Empirical Benchmark Matrix

The following table summarizes the quantitative results, search space metrics, and convergence statistics captured from our empirical test runs across all twelve practicals:

| Module | Topic | Search / Problem Space | Primary Metric | Observed Result | Benchmark Standard |
|---|---|---|---|---|---|
| **P01** | Simple Reflex Agent | 2-room Vacuum World ($2 \times 2^2 = 8$ states) | Steps to convergence & Score | **6 steps**, Score = **16** | Full convergence, both rooms Clean |
| **P02** | Uninformed Search | Directed Graph ($A \to G$, weighted edges) | Path quality vs Cumulative cost | BFS: $A \to B \to D \to G$<br>DFS: $A \to C \to D \to G$<br>UCS: $A \to B \to D \to G$ | UCS achieves optimal cost = **3**; BFS optimal in edge count |
| **P03** | A* Path Planning | $20 \times 20$ grid (400 cells, 20% obstacles) | Nodes explored & Execution time | Length = **38**, Explored = **221/400**, Time = **0.662 ms** | Manhattan distance is strictly admissible & consistent |
| **P04** | Minimax + $\alpha$-$\beta$ | Tic-Tac-Toe Game Tree ($3^9 = 19,683$ states) | Nodes evaluated per AI move | Turn 1: **34,202**<br>Turn 3: **1,630**<br>Turn 5: **97**<br>Turn 7: **10** | >95% game-tree reduction via Alpha-Beta pruning |
| **P05** | Rule-Based Expert System | Multi-factor underwriting (L1–L6 rules) | Rule firing & Clamped scoring | Strong: **97.0 / 100** (6 fired)<br>Borderline: **58.0 / 100**<br>High-Risk: **5.0 / 100** | Strict clamping $[5, 97]$, full explainability audit trail |
| **P06** | Sudoku CSP Solver | $9 \times 9$ Sudoku (51 unassigned variables) | Assignments, Backtracks, Checks | Assignments = **51**<br>Backtracks = **0**<br>Checks = **467**<br>Time = **1.850 ms** | Zero-backtrack solution enabled by MRV variable ordering |
| **P07** | Naive Bayes Classifier | 5-symptom clinical vector (binary features) | Class posterior separation | Flu: **100.00%** ($p > 0.999$)<br>Cold: **100.00%**<br>Migraine: **100.00%** | Exact posterior probability separation via Gaussian Naive Bayes |
| **P08** | Website Classifier Chatbot | Multi-domain text corpus (5 target classes) | Keyword extraction & Conflict resolution | Single: **100% confidence**<br>Tie: **Multi-category detected** | Robust token normalization, multi-keyword tie-breaking |
| **P09** | STRIPS Warehouse Robot | 5-room warehouse + Charging hub, parcels | Plan cost & State expansions | Baseline: **8 actions**, Cost = **28** (37 expanded)<br>R2-R3 Blocked: Cost = **30** | Dynamic re-routing via Uniform Cost Search over state space |
| **P10** | Value Iteration on MDP | $N \times N$ Grid-World with obstacles ($N \in [4, 8]$) | Bellman convergence ($\theta = 0.001$) | $5 \times 5$ ($\gamma=0.9$): **9 iters**, 8 moves<br>$5 \times 5$ ($\gamma=0.5$): $V(\text{start}) = -1.91$<br>$8 \times 8$ ($\gamma=0.9$): **15 iters**, 14 moves | Proves impact of discount factor $\gamma$ on horizon valuation |
| **P11** | Propositional Logic | Campus Access Knowledge Base ($V, L, E, H$) | Entailment check ($\text{KB} \models E$) | Truth-table: **1/16 models** valid<br>Resolution: **Empty clause derived** | Soundness & completeness verified via refutation proof |
| **P12** | ML Model Benchmark | Synthetic 2-feature classification ($N=120$) | Generalization vs Overfitting | k-NN ($k=5$): **92%** test acc<br>Decision Tree: **89%** test acc<br>Gaussian NB: **91%** test acc<br>Perceptron: **86%** test acc | k-NN ($k=1$) exhibits empirical 100% train / high test variance |

---

## Deep Dives into Core Implementations

### 1. Agents & Deterministic Search (Practicals 01–03)
- **Reflex Architecture:** Practical 01 demonstrates that a simple reflex agent without memory or internal models can still achieve rational behavior if the environment is fully observable. In a two-room vacuum world, condition-action rules achieve steady-state cleanliness within 6 discrete time steps (score: 16).
- **Search Completeness & Optimality:** Practical 02 contrasts FIFO queues (BFS), LIFO stacks (DFS), and priority queues (UCS). While BFS is optimal in edge count ($A \to B \to D \to G$), UCS is the only uninformed algorithm guaranteed to minimize cumulative cost on weighted graphs ($g(n) = 3$), cleanly avoiding the expensive edge $(A, C, 5)$.
- **Informed Exploration:** Practical 03 validates the $A^*$ search algorithm on a $20 \times 20$ grid with $20\%$ obstacle density. Using the Manhattan distance heuristic $h(n) = |x_1 - x_2| + |y_1 - y_2|$, which is strictly admissible for 4-connected grid movement, $A^*$ explores only 221 out of 400 nodes ($55.2\%$) to find the optimal path of length 38 in under $1\text{ ms}$.

### 2. Adversarial Reasoning & Constraint Satisfaction (Practicals 04 & 06)
- **Game-Tree Pruning:** Practical 04 implements Minimax with Alpha-Beta pruning for zero-sum turn-based games. By maintaining $[\alpha, \beta]$ bounds, the search space on the initial move drops drastically while guaranteeing the game-theoretic value ($V = 0$ for perfect self-play). Under scripted human play, node evaluations decay exponentially ($34,202 \to 1,630 \to 97 \to 10$) as depth decreases.
- **MRV Heuristic in CSP:** Practical 06 formulates Sudoku as a Constraint Satisfaction Problem (81 variables, domains $\{1..9\}$, 27 all-different constraints). Implementing the **Minimum Remaining Values (MRV)** heuristic eliminates all backtracking on standard benchmarks (0 backtracks, 51 assignments, 467 consistency checks, $1.850\text{ ms}$).

### 3. Symbolic Reasoning & Automated Planning (Practicals 05, 09, 11)
- **Expert Systems:** Practical 05 creates a rule-based loan underwriting engine with production rules $L1..L6$ operating on applicant facts. A base score of 40 is conditionally boosted or penalized and clamped to $[5, 97]$, generating an explainable audit trail detailing fired rules, risk factors, and positive signals.
- **STRIPS Planning:** Practical 09 encodes a warehouse robotics domain using STRIPS actions ($\text{Preconditions}, \text{Add}, \text{Delete}$). A Uniform Cost Search planner finds the optimal parcel pickup and delivery route (cost 28, 8 actions). When corridor $R2 \to R3$ is obstructed, the system dynamically re-plans an alternate route via Room 5 (cost 30) without code modification.
- **Logic Refutation:** Practical 11 models campus security policies in Propositional Logic, validating entailment ($\text{KB} \models E$) via truth-table model checking (1 model out of 16 satisfies KB, in which $E$ holds) and automated resolution refutation (generating the empty clause $\square$ from CNF clauses).

### 4. Probabilistic Inference & Reinforcement Learning (Practicals 07, 08, 10, 12)
- **Probabilistic Clinical Diagnosis:** Practical 07 demonstrates Bayesian classification under symptom uncertainty. Gaussian Naive Bayes computes exact posterior probabilities across Flu, Cold, and Migraine categories, proving robust even with small sample sizes.
- **Sequential Decision-Making under Uncertainty:** Practical 10 implements **Value Iteration** on a grid-world Markov Decision Process. Solving the Bellman optimality equation:
  $$V_{k+1}(s) = \max_{a \in A} \left[ R(s, a) + \gamma \sum_{s'} P(s' \mid s, a) V_k(s') \right]$$
  at convergence threshold $\theta = 0.001$, the optimal policy $\pi^*(s)$ cleanly routes around obstacles to the terminal goal state. The experiments empirically prove the effect of discount factor $\gamma$: at $\gamma = 0.9$, distant rewards propagate effectively ($V_{\text{start}} = -0.43$, 9 iterations), while at $\gamma = 0.5$, future rewards are sharply discounted ($V_{\text{start}} = -1.91$).

---

## Module Index

| # | Directory | Implementation | Interactive Notebook | Verified Lab Report | Topic Description |
|:---:|:---|:---:|:---:|:---:|:---|
| **01** | [`practical-01-reflex-agent/`](./practical-01-reflex-agent/) | [`main.py`](./practical-01-reflex-agent/main.py) | [`notebook.ipynb`](./practical-01-reflex-agent/notebook.ipynb) | [`report.pdf`](./practical-01-reflex-agent/report.pdf) | Simple Reflex & Goal-Based Agent (Vacuum World) |
| **02** | [`practical-02-uninformed-search/`](./practical-02-uninformed-search/) | [`main.py`](./practical-02-uninformed-search/main.py) | [`notebook.ipynb`](./practical-02-uninformed-search/notebook.ipynb) | [`report.pdf`](./practical-02-uninformed-search/report.pdf) | Uninformed Search: BFS, DFS, Uniform Cost Search |
| **03** | [`practical-03-astar-path-planning/`](./practical-03-astar-path-planning/) | [`main.py`](./practical-03-astar-path-planning/main.py) | [`notebook.ipynb`](./practical-03-astar-path-planning/notebook.ipynb) | [`report.pdf`](./practical-03-astar-path-planning/report.pdf) | A* Search with Manhattan Heuristic on 2D Grid |
| **04** | [`practical-04-minimax-alpha-beta/`](./practical-04-minimax-alpha-beta/) | [`main.py`](./practical-04-minimax-alpha-beta/main.py) | [`notebook.ipynb`](./practical-04-minimax-alpha-beta/notebook.ipynb) | [`report.pdf`](./practical-04-minimax-alpha-beta/report.pdf) | Minimax Game-Playing Agent with Alpha-Beta Pruning |
| **05** | [`practical-05-rule-based-expert-system/`](./practical-05-rule-based-expert-system/) | [`main.py`](./practical-05-rule-based-expert-system/main.py) | [`notebook.ipynb`](./practical-05-rule-based-expert-system/notebook.ipynb) | [`report.pdf`](./practical-05-rule-based-expert-system/report.pdf) | Rule-Based Expert System (Smart Loan Advisor) |
| **06** | [`practical-06-sudoku-csp/`](./practical-06-sudoku-csp/) | [`main.py`](./practical-06-sudoku-csp/main.py) | [`notebook.ipynb`](./practical-06-sudoku-csp/notebook.ipynb) | [`report.pdf`](./practical-06-sudoku-csp/report.pdf) | Constraint Satisfaction Problem (Sudoku Solver + MRV) |
| **07** | [`practical-07-naive-bayes-disease-prediction/`](./practical-07-naive-bayes-disease-prediction/) | [`main.py`](./practical-07-naive-bayes-disease-prediction/main.py) | [`notebook.ipynb`](./practical-07-naive-bayes-disease-prediction/notebook.ipynb) | [`report.pdf`](./practical-07-naive-bayes-disease-prediction/report.pdf) | Probabilistic Disease Prediction (Gaussian Naive Bayes) |
| **08** | [`practical-08-website-classifier-chatbot/`](./practical-08-website-classifier-chatbot/) | [`main.py`](./practical-08-website-classifier-chatbot/main.py) | [`notebook.ipynb`](./practical-08-website-classifier-chatbot/notebook.ipynb) | [`report.pdf`](./practical-08-website-classifier-chatbot/report.pdf) | AI Website Classifier & Intent Matching Chatbot |
| **09** | [`practical-09-strips-warehouse-planning/`](./practical-09-strips-warehouse-planning/) | [`main.py`](./practical-09-strips-warehouse-planning/main.py) | [`notebook.ipynb`](./practical-09-strips-warehouse-planning/notebook.ipynb) | [`report.pdf`](./practical-09-strips-warehouse-planning/report.pdf) | STRIPS Planning for Autonomous Warehouse Bot |
| **10** | [`practical-10-value-iteration-gridworld/`](./practical-10-value-iteration-gridworld/) | [`main.py`](./practical-10-value-iteration-gridworld/main.py) | [`notebook.ipynb`](./practical-10-value-iteration-gridworld/notebook.ipynb) | [`report.pdf`](./practical-10-value-iteration-gridworld/report.pdf) | Value Iteration on Grid-World MDP with Obstacles |
| **11** | [`practical-11-logic-reasoning/`](./practical-11-logic-reasoning/) | [`main.py`](./practical-11-logic-reasoning/main.py) | [`notebook.ipynb`](./practical-11-logic-reasoning/notebook.ipynb) | *Inference Scaffold* | Propositional Logic: Model Checking & Resolution |
| **12** | [`practical-12-ml-classifier-benchmark/`](./practical-12-ml-classifier-benchmark/) | [`main.py`](./practical-12-ml-classifier-benchmark/main.py) | [`notebook.ipynb`](./practical-12-ml-classifier-benchmark/notebook.ipynb) | *Benchmark Scaffold* | Empirical Classifier Benchmark (k-NN, DT, NB, Perc) |
| **Docs** | [`docs/`](./docs/) | — | — | [`Unit_1_Class_Notes.pdf`](./docs/Unit_1_Class_Notes.pdf) | Unit 1 Student Class Notes: Foundations of AI |

---

## Reproducibility & Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/mandhatisaiganesh/artificial-intelligence-01AI0511.git
cd artificial-intelligence-01AI0511
```

### 2. Set Up Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Any Practical via CLI
Every module is completely self-contained and can be executed directly:
```bash
python practical-01-reflex-agent/main.py
python practical-03-astar-path-planning/main.py
python practical-06-sudoku-csp/main.py
python practical-09-strips-warehouse-planning/main.py
python practical-10-value-iteration-gridworld/main.py
```

### 4. Interactive Jupyter Notebooks
Launch Jupyter to explore step-by-step mathematical proofs and interactive visual interfaces:
```bash
jupyter notebook
```
Navigate to any `practical-*/notebook.ipynb` to execute cell-by-cell.

---

## Limitations, Safety & Responsible AI

1. **Deterministic Assumptions:** Practicals 01–06 and 09 assume fully deterministic state transitions and complete observability. In production robotics and real-world agents, sensor noise and stochastic actuators require probabilistic filtering (e.g., Kalman Filters, POMDPs).
2. **Computational Complexity in Search:** Uninformed search algorithms (BFS, DFS) scale exponentially with branching factor $b^d$. While $A^*$ with admissible heuristics mitigates this, large-scale search spaces require IDA* or memory-bounded heuristics (SMA*).
3. **Clinical & Financial Advisory Boundaries:** The medical diagnostic engines (P05, P07) and underwriting advisors are intended solely for academic demonstration. Clinical medical systems require extensive multi-center clinical trials and regulatory approval (FDA/CE), while automated credit systems are strictly governed by fair lending regulations (e.g., ECOA, FCRA).
4. **Explainability & Transparency:** Rule-based expert systems and Naive Bayes models provide glass-box interpretability, enabling full audit trails of decisions. This serves as a vital benchmark against opaque black-box machine learning models in high-stakes environments.

---

## Academic Credentials & Metadata

- **Course:** Artificial Intelligence (`01AI0511`)
- **Institution:** Marwadi University, Rajkot, Gujarat, India
- **Department:** Computer Science & Engineering (AI, ML & DS)
- **Student Name:** Sai Ganesh Mandhati
- **Enrollment Number:** `92460118370`
- **Class & Batch:** `5EN_19` · `Lab B`
- **License:** MIT License
