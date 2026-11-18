# From Reflex Agents to Markov Decision Processes: Implementing Classical and Probabilistic AI Systems

**01AI0511 · Artificial Intelligence · Marwadi University · Department of CSE — AI, ML & DS**

---

## Abstract

This repository contains twelve self-contained implementations spanning the core paradigms of artificial intelligence—from deterministic state-space search and constraint satisfaction to symbolic planning, probabilistic inference, and sequential decision-making under uncertainty. Each module is a runnable Python program accompanied by an interactive Jupyter notebook, a per-practical README, and the original lab report.

The progression is deliberate. We begin with the simplest possible agent architecture (a condition→action reflex loop in a two-room vacuum world), advance through increasingly sophisticated search strategies (BFS, DFS, UCS, A*), enter adversarial territory (Minimax, Alpha-Beta), formalize constraint reasoning and symbolic knowledge (CSP, STRIPS, propositional logic), introduce probability (Bayesian networks, Naive Bayes), and conclude with sequential decision-making (Value Iteration on MDPs) and a comparative ML benchmark. No external ML framework is imported for Practicals 1–11; every algorithm is implemented from first principles using only the Python standard library.

---

## System Architecture & Paradigm Map

```
┌──────────────────────────────────────────────────────────────────────────┐
│                    AI SYSTEMS — 01AI0511 PARADIGM MAP                    │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────────────────────┐    ┌────────────────────────────────┐       │
│  │   AGENTS & SEARCH       │    │  ADVERSARIAL & CONSTRAINT      │       │
│  │                         │    │  SOLVING                       │       │
│  │  P01  Reflex / Goal     │    │  P04  Minimax / Alpha-Beta     │       │
│  │  P02  BFS / DFS / UCS   │    │  P06  CSP / AC-3 / MRV        │       │
│  │  P03  A* / Heuristics   │    │                                │       │
│  └────────────┬────────────┘    └───────────────┬────────────────┘       │
│               │                                 │                        │
│               ▼                                 ▼                        │
│  ┌─────────────────────────────────────────────────────────────┐         │
│  │            SYMBOLIC KNOWLEDGE & PLANNING                    │         │
│  │                                                             │         │
│  │  P05  Rule-Based Expert System (Forward / Backward Chain)   │         │
│  │  P09  STRIPS / Goal-Stack Planning (Blocks World)           │         │
│  │  P11  Propositional Logic — Model Checking & Resolution     │         │
│  └────────────────────────────┬────────────────────────────────┘         │
│                               │                                          │
│                               ▼                                          │
│  ┌─────────────────────────────────────────────────────────────┐         │
│  │       PROBABILISTIC & REINFORCEMENT LEARNING                │         │
│  │                                                             │         │
│  │  P07  Bayesian Network Inference / Naive Bayes Classifier   │         │
│  │  P10  Value Iteration — Grid-World MDP                      │         │
│  │  P12  ML Classifier Benchmark (k-NN, DT, NB, Perceptron)   │         │
│  └────────────────────────────┬────────────────────────────────┘         │
│                               │                                          │
│                               ▼                                          │
│  ┌─────────────────────────────────────────────────────────────┐         │
│  │          APPLIED NLP & RESPONSIBLE AI                       │         │
│  │                                                             │         │
│  │  P08  Text Classifier + Explainability + Ethics Report      │         │
│  └─────────────────────────────────────────────────────────────┘         │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Empirical Benchmarks & Experimental Observations

| # | Practical | Key Metric |
|---|-----------|------------|
| 01 | Reflex Agent (Vacuum World) | Score **16** over 6 steps — full convergence, both rooms cleaned |
| 02 | Uninformed Search (Maze) | BFS: shortest path · UCS: lowest cost (mud cells cost 5) · DFS: not optimal |
| 03 | A* (8-Puzzle) | Manhattan heuristic expands **far fewer** nodes than h=0, all return optimal-length paths |
| 04 | Minimax vs Alpha-Beta (Tic-Tac-Toe) | Alpha-Beta prunes **~96.6%** of the game tree vs full Minimax on empty board |
| 05 | Rule-Based Expert System | Forward chaining derives all reachable conclusions; backward chaining proves with full audit trail |
| 06 | CSP (Map Coloring + 8-Queens) | AC-3 + MRV backtracking solves Australia map coloring and 8-Queens |
| 07 | Bayesian Network + Naive Bayes | $P(\text{Burglary} \mid \text{JohnCalls}, \text{MaryCalls}) \approx 0.2842$ |
| 08 | Text Classifier + Ethics | **4/4** accuracy on test set; per-prediction top-3 word explanations with log-odds |
| 09 | STRIPS Blocks World | Goal-stack planner generates valid multi-step plans with correct precondition tracking |
| 10 | Value Iteration (Grid-World MDP) | Converges with $\gamma = 0.99$; optimal policy avoids $-1$ terminal, reaches $+1$ |
| 11 | Propositional Logic | KB $\models$ E proven by both model checking and resolution refutation |
| 12 | ML Classifier Benchmark | All 4 classifiers >80% test accuracy; k-NN(k=1) overfits, k=5 generalises |

---

## Module Index

| # | Module | main.py | notebook | report | Topic |
|---|--------|---------|----------|--------|-------|
| 01 | [`practical-01-reflex-agent/`](./practical-01-reflex-agent/) | [`main.py`](./practical-01-reflex-agent/main.py) | [`notebook.ipynb`](./practical-01-reflex-agent/notebook.ipynb) | [`report.pdf`](./practical-01-reflex-agent/report.pdf) | Simple Reflex & Goal-Based Agent |
| 02 | [`practical-02-uninformed-search/`](./practical-02-uninformed-search/) | [`main.py`](./practical-02-uninformed-search/main.py) | [`notebook.ipynb`](./practical-02-uninformed-search/notebook.ipynb) | [`report.pdf`](./practical-02-uninformed-search/report.pdf) | BFS, DFS, Uniform-Cost Search |
| 03 | [`practical-03-astar-path-planning/`](./practical-03-astar-path-planning/) | [`main.py`](./practical-03-astar-path-planning/main.py) | [`notebook.ipynb`](./practical-03-astar-path-planning/notebook.ipynb) | [`report.pdf`](./practical-03-astar-path-planning/report.pdf) | A* Search & Heuristic Comparison |
| 04 | [`practical-04-minimax-alpha-beta/`](./practical-04-minimax-alpha-beta/) | [`main.py`](./practical-04-minimax-alpha-beta/main.py) | [`notebook.ipynb`](./practical-04-minimax-alpha-beta/notebook.ipynb) | [`report.pdf`](./practical-04-minimax-alpha-beta/report.pdf) | Minimax & Alpha-Beta Pruning |
| 05 | [`practical-05-rule-based-expert-system/`](./practical-05-rule-based-expert-system/) | [`main.py`](./practical-05-rule-based-expert-system/main.py) | [`notebook.ipynb`](./practical-05-rule-based-expert-system/notebook.ipynb) | [`report.pdf`](./practical-05-rule-based-expert-system/report.pdf) | Rule-Based Expert System |
| 06 | [`practical-06-sudoku-csp/`](./practical-06-sudoku-csp/) | [`main.py`](./practical-06-sudoku-csp/main.py) | [`notebook.ipynb`](./practical-06-sudoku-csp/notebook.ipynb) | [`report.pdf`](./practical-06-sudoku-csp/report.pdf) | CSP — Map Coloring & N-Queens |
| 07 | [`practical-07-naive-bayes-disease-prediction/`](./practical-07-naive-bayes-disease-prediction/) | [`main.py`](./practical-07-naive-bayes-disease-prediction/main.py) | [`notebook.ipynb`](./practical-07-naive-bayes-disease-prediction/notebook.ipynb) | [`report.pdf`](./practical-07-naive-bayes-disease-prediction/report.pdf) | Bayesian Network & Naive Bayes |
| 08 | [`practical-08-website-classifier-chatbot/`](./practical-08-website-classifier-chatbot/) | [`main.py`](./practical-08-website-classifier-chatbot/main.py) | [`notebook.ipynb`](./practical-08-website-classifier-chatbot/notebook.ipynb) | [`report.pdf`](./practical-08-website-classifier-chatbot/report.pdf) | Text Classification & Ethics |
| 09 | [`practical-09-strips-warehouse-planning/`](./practical-09-strips-warehouse-planning/) | [`main.py`](./practical-09-strips-warehouse-planning/main.py) | [`notebook.ipynb`](./practical-09-strips-warehouse-planning/notebook.ipynb) | [`report.pdf`](./practical-09-strips-warehouse-planning/report.pdf) | STRIPS / Goal-Stack Planning |
| 10 | [`practical-10-value-iteration-gridworld/`](./practical-10-value-iteration-gridworld/) | [`main.py`](./practical-10-value-iteration-gridworld/main.py) | [`notebook.ipynb`](./practical-10-value-iteration-gridworld/notebook.ipynb) | [`report.pdf`](./practical-10-value-iteration-gridworld/report.pdf) | Value Iteration — Grid-World MDP |
| 11 | [`practical-11-logic-reasoning/`](./practical-11-logic-reasoning/) | [`main.py`](./practical-11-logic-reasoning/main.py) | [`notebook.ipynb`](./practical-11-logic-reasoning/notebook.ipynb) | report.pdf | Propositional Logic & Resolution |
| 12 | [`practical-12-ml-classifier-benchmark/`](./practical-12-ml-classifier-benchmark/) | [`main.py`](./practical-12-ml-classifier-benchmark/main.py) | [`notebook.ipynb`](./practical-12-ml-classifier-benchmark/notebook.ipynb) | report.pdf | ML Classifier Benchmark |

---

## Reproducibility & Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/artificial-intelligence-01AI0511.git
cd artificial-intelligence-01AI0511

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run any practical
python practical-01-reflex-agent/main.py
python practical-04-minimax-alpha-beta/main.py
python practical-10-value-iteration-gridworld/main.py

# 5. Or launch Jupyter for interactive exploration
jupyter notebook
# Then open any practical's notebook.ipynb
```

### Dependencies

All practicals (1–11) run on the **Python standard library alone** — no `pip install` needed for core functionality. The `requirements.txt` includes optional libraries for extended features:

| Package | Used By | Purpose |
|---------|---------|---------|
| `numpy` | Optional | Array operations (not required by any main.py) |
| `matplotlib` | Optional | Plotting and visualisation |
| `scikit-learn` | P12 (optional) | Comparison baseline for classifier benchmark |
| `gradio` | Optional | Interactive web UI demos |
| `jupyter` | All | Notebook execution |

---

## Limitations, Safety & Responsible AI

### Deterministic Assumptions
Practicals 1–6 and 9 operate in fully observable, deterministic environments. Real-world AI systems must handle partial observability, noisy sensors, and non-deterministic action outcomes. The grid-world MDP (Practical 10) is the only module that explicitly models stochastic transitions.

### State-Space Explosion
The search algorithms (BFS, DFS, A*) demonstrated here work on small problem instances. Uninformed search scales exponentially with branching factor and depth; even A* with Manhattan distance becomes impractical for puzzles larger than the 15-puzzle without pattern database heuristics or IDA*.

### Rule-Engine Heuristics vs Statistical Underwriting
The expert system (Practical 5) uses hand-crafted production rules. In production medical or financial advisory systems, such rules must be authored and validated by domain experts, regularly audited, and supplemented by statistical models trained on representative, labelled data.

### Educational Boundaries
- **Medical demos (P5, P7):** Toy systems with fabricated rules/data. Not suitable for clinical use.
- **Spam classifier (P8):** Trained on 12 examples. Real spam filters require diverse, large-scale corpora and continuous retraining.
- **ML benchmark (P12):** Synthetic data with Gaussian clusters. Real-world feature spaces are rarely this cleanly separable.

### Ethics & Explainability
Practical 8 includes an explicit ethics report addressing fairness, bias, privacy, and the limitations of bag-of-words models. We encourage extending this analysis to every AI system in this repository and beyond.

---

## Technical Stack

| Component | Version |
|-----------|---------|
| Python | ≥ 3.8 |
| External dependencies | None required (stdlib only for P01–P11) |
| Notebook format | nbformat 4.5 |
| License | MIT |

---

## Repository Structure

```
artificial-intelligence-01AI0511/
├── README.md                                   # This file
├── requirements.txt                            # Consolidated Python dependencies
├── .gitignore                                  # Python / Jupyter / OS ignores
├── practical-01-reflex-agent/                  # Agents & Search
├── practical-02-uninformed-search/             # Agents & Search
├── practical-03-astar-path-planning/           # Agents & Search
├── practical-04-minimax-alpha-beta/            # Adversarial & Constraint Solving
├── practical-05-rule-based-expert-system/       # Symbolic Knowledge & Planning
├── practical-06-sudoku-csp/                    # Adversarial & Constraint Solving
├── practical-07-naive-bayes-disease-prediction/ # Probabilistic & RL
├── practical-08-website-classifier-chatbot/     # Applied NLP & Responsible AI
├── practical-09-strips-warehouse-planning/      # Symbolic Knowledge & Planning
├── practical-10-value-iteration-gridworld/      # Probabilistic & RL
├── practical-11-logic-reasoning/               # Symbolic Knowledge & Planning
└── practical-12-ml-classifier-benchmark/        # Probabilistic & RL
```

Each practical folder contains:
- `main.py` — Standalone, runnable Python script
- `notebook.ipynb` — Multi-cell Jupyter notebook
- `README.md` — Per-practical technical overview
- `report.pdf` — Original lab report (where available)

---

*Built for coursework in 01AI0511 — Artificial Intelligence, Marwadi University.*
