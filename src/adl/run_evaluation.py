"""Run the ADL synthetic-trace evaluator and write CSV output."""
import argparse
import csv
import json
from pathlib import Path
from .scoring import evaluate_case

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="data/agent_test_cases.jsonl")
    parser.add_argument("--output", default="reports/latest_results.csv")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    cases = []
    with input_path.open(encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if line.strip():
                try:
                    cases.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    raise SystemExit(f"Invalid JSON on line {line_no}: {exc}")

    if not cases:
        raise SystemExit("No test cases found.")

    results = [evaluate_case(case) for case in cases]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(results[0].keys())
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)

    print(f"Evaluated {len(results)} cases -> {output_path}")
    for result in results:
        print(f"{result['case_id']}: {result['score']}/100 | {result['recommendation']} | {result['critical_reasons'] or 'no critical rule triggered'}")

if __name__ == "__main__":
    main()
