# Architecture

## Design goal

Provide a small, explainable lifecycle and evaluation harness that makes agent behaviour reviewable before any live deployment.

## Logical flow

```text
Business objective
      |
      v
ADL-0 Requirements & risk tier
      |
      v
ADL-1 Workflow / trajectory / tool contracts
      |
      v
ADL-2 Agent implementation (outside this demo)
      |
      v
ADL-3 Synthetic scenarios + replayable traces
      |
      v
ADL-4 Deterministic checks + human review
      |
      v
ADL-5 Mock integration / operational replay
      |
      v
ADL-6 Release gate + owner approval
      |
      v
ADL-7 Monitoring, incidents, regression tests
      |___________________________|
                  feedback
```

## Components in this repository

- `data/agent_test_cases.jsonl`: synthetic scenarios and expected behaviours.
- `src/adl/scoring.py`: transparent rules and critical-failure overrides.
- `src/adl/run_evaluation.py`: command-line evaluator that writes a CSV report.
- `src/adl/validate_dataset.py`: schema checks for test data.
- `tests/`: automated tests for scoring behaviour and critical overrides.
- `reports/sample_evaluation.md`: human-readable sample release decision.

## Trace schema

Each trace event contains:
- `step`: sequential event number;
- `event_type`: `observe`, `reason`, `tool_call`, `tool_result`, `human_approval`, `final`;
- `description`: brief event description;
- `evidence_ids`: IDs of evidence used;
- `action`: action attempted, if any;
- `approved_by_human`: whether a human approved the action.

The demo evaluates recorded events. It does not infer hidden model reasoning and does not require chain-of-thought. Store concise operational events, tool inputs/outputs where permitted, evidence identifiers, decisions and outcomes—not private internal reasoning.

## Trust boundaries

1. **Untrusted inputs:** user content and retrieved documents may contain inaccurate or malicious instructions.
2. **Tool boundary:** a proposed tool action is not proof that it executed successfully.
3. **Permission boundary:** high-impact actions require explicit authorisation and, in this prototype, human approval.
4. **Evidence boundary:** a source identifier must point to an auditable source in a real implementation.
5. **Release boundary:** the evaluator's output is advisory; an accountable owner must approve release.

## Production extensions (not implemented)

- Authentication and role-based access control.
- Secret management and data retention controls.
- Real tool adapters with allowlists and idempotency.
- Human-review interface and audit storage.
- Observability, latency/cost metrics, incident response and rollback.
- Calibrated human-vs-automated judge comparison.
