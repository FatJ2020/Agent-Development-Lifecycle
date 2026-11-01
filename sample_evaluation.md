# Sample Evaluation Summary

This summary describes the six synthetic starter cases. Reproduce the exact CSV by running the evaluator.

## What the demo is designed to show

- A clean, source-grounded read-only trace can pass the rule checks.
- A high-risk request can be safely redirected to a human approval process without executing the action.
- A prohibited action is blocked even if the rest of the trace looks complete.
- Missing required evidence blocks the release recommendation.
- A tool error that is later described as success is labelled as a task-outcome failure in the synthetic expected label; semantic detection of this mismatch is not yet implemented.

## Interpretation

`PASS_FOR_REVIEW` means the configured checks passed for this synthetic trace. It is not production authorisation.

`REVIEW` means one or more non-critical checks failed.

`BLOCK` means a critical condition was triggered. The reason is included in the CSV to make the decision auditable.

## Next improvement

The included labels are illustrative synthetic labels, not human-adjudicated ground truth. The next step is to have independent human reviewers validate expected outcomes and measure false-pass and false-block rates. The evaluator does not independently verify evidence truth or semantic consistency between tool results and the final response.
