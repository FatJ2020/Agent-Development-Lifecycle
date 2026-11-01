# ADL Lifecycle: Entry Criteria, Activities and Exit Evidence

| Stage | Key question | Activities | Exit evidence |
|---|---|---|---|
| ADL-0 Requirement Engineering | What business outcome and boundaries are required? | Define user, task, success metric, risk tier, prohibited actions and fallback | Approved requirements and acceptance tests |
| ADL-1 Workflow & Trajectory Design | How should the agent reach the outcome? | Map states, tools, hand-offs, retries, stop conditions and human escalation | Reviewed workflow and tool contracts |
| ADL-2 Agent Construction | Is the smallest viable implementation built? | Implement prompt/configuration, retrieval or tools, permissions and logging | Versioned build, unit tests and known limitations |
| ADL-3 Simulation & Scenario Testing | What happens under normal and abnormal conditions? | Test happy path, edge cases, malformed inputs, tool errors and adversarial instructions | Reproducible scenario results |
| ADL-4 Human Evaluation | Is the behaviour useful, grounded and appropriate? | Review correctness, completeness, traceability, actionability and risk | Human rubric and adjudicated failures |
| ADL-5 Digital-Twin / Operational Validation | Does the workflow hold up in a representative environment? | Replay synthetic cases, mock integrations, test recovery and rollback | Integration evidence and rollback test |
| ADL-6 Deployment Governance | Is release risk accepted by the right owner? | Check permissions, approvals, monitoring, support and rollback | Signed release checklist |
| ADL-7 Continuous Learning | Are new failures captured and regressions prevented? | Monitor incidents, triage drift, add regression tests, version changes | Change log and passing regression suite |

## Gate rule

A stage does not pass simply because its activities were performed. The exit evidence must exist and be reviewed. A critical policy, authorisation or evidence failure blocks release regardless of the average score.

## Automotive-to-agentic-AI analogy

- Requirements and acceptance criteria ↔ product requirements and verification plans.
- Stage gates ↔ risk-based release gates.
- Traceability ↔ auditable links from requirement to test to result.
- Change control ↔ regression testing after configuration/model/tool changes.
- Cross-functional review ↔ business owner, engineering, security, legal/compliance and operations.

This is an analogy, not a claim that an AI agent is identical to a physical product. AI systems introduce probabilistic behaviour, prompt injection, data leakage and model/version drift that need specific controls.
