# 5-minute hiring-manager demo

## 0:00–0:45 — Business problem
An AI agent can sound convincing but still make an unauthorised tool call, rely on missing evidence or claim a failed operation succeeded. A single answer-quality score does not cover these risks.

## 0:45–1:30 — Lifecycle
Walk through ADL-0 requirements, ADL-1 workflow/trajectory, ADL-3 simulation, ADL-4 human evaluation, ADL-6 deployment governance and ADL-7 continuous learning.

## 1:30–2:30 — Show the test cases
Open `data/agent_test_cases.jsonl`. Explain that these are synthetic examples and each trace is structured as events, with evidence IDs and action fields.

## 2:30–3:30 — Run the evaluator
Run:
```bash
python -m src.adl.run_evaluation
```
Point out the score, recommendation and critical reasons.

## 3:30–4:15 — Show tests
Run:
```bash
python -m unittest discover -s tests -v
```
Explain the invariant: a critical failure overrides a high average score.

## 4:15–5:00 — Be candid about limitations
The evaluator is deterministic and transparent, but it is not a production agent, does not independently verify evidence truth and has not been statistically validated. The next step is human adjudication, broader cases, regression comparison and calibrated metrics.
