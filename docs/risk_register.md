# Example Agent Risk Register

Synthetic example for a read-only operational knowledge agent.

| ID | Risk | Example trigger | Preventive control | Detection evidence | Owner |
|---|---|---|---|---|---|
| R-01 | Unsupported recommendation | Recommendation lacks a source | Require evidence IDs for material claims | Missing evidence check | Product / domain owner |
| R-02 | Unauthorised action | Agent tries to issue a purchase order | Tool allowlist; deny by default | Policy violation in trace | Operations / security |
| R-03 | Approval bypass | High-risk action has no human approval | Approval gate before execution | Approval event missing | Process owner |
| R-04 | Tool failure misreported as success | Tool returns error but agent says complete | Verify tool result status | Mismatch between tool result and final event | Engineering |
| R-05 | Prompt injection in retrieved content | Document attempts to override system policy | Treat retrieved content as data, not instructions | Adversarial test result | AI / security |
| R-06 | Regression after change | Previously passing case fails after model/config update | Versioned regression suite | Version comparison report | AI product owner |
| R-07 | Sensitive data exposure | Agent includes data beyond user permission | Data minimisation and access checks | Red-team / access test | Security / privacy |

This register is illustrative. Real projects require a context-specific assessment and named accountable owners.
