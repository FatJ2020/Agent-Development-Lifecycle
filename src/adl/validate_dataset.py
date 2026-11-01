"""Basic schema validator for the synthetic JSONL test set."""
import argparse
import json
from pathlib import Path

REQUIRED_FIELDS = {
    "case_id", "title", "risk_tier", "expected_outcome",
    "required_evidence_ids", "prohibited_actions",
    "requires_human_approval", "trace"
}
EVENT_FIELDS = {"step", "event_type", "description", "evidence_ids", "action", "approved_by_human"}

def validate_case(case, line_no):
    errors = []
    missing = REQUIRED_FIELDS - set(case)
    if missing:
        errors.append(f"line {line_no}: missing fields {sorted(missing)}")
    if not isinstance(case.get("trace"), list) or not case.get("trace"):
        errors.append(f"line {line_no}: trace must be a non-empty list")
        return errors
    for i, event in enumerate(case["trace"], 1):
        missing_event = EVENT_FIELDS - set(event)
        if missing_event:
            errors.append(f"line {line_no}, event {i}: missing fields {sorted(missing_event)}")
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="data/agent_test_cases.jsonl")
    args = parser.parse_args()
    errors, count = [], 0
    with Path(args.input).open(encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                continue
            count += 1
            try:
                case = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_no}: invalid JSON: {exc}")
                continue
            errors.extend(validate_case(case, line_no))
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print(f"Dataset valid: {count} cases.")
if __name__ == "__main__":
    main()
