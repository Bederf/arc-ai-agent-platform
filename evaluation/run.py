import json
from collections import Counter
from pathlib import Path

from app.agent import assess_claim


def run() -> dict:
    cases = json.loads((Path(__file__).parent / "dataset.json").read_text())
    results = []
    for case in cases:
        result = assess_claim(
            case["claim_id"],
            proposed_action=case.get("action", "approve_claim"),
            proposed_amount=case.get("amount"),
        )
        results.append({"name": case["name"], "expected": case["expected"], "actual": result["decision"], "passed": result["decision"] == case["expected"]})
    report = {
        "total": len(results),
        "passed": sum(item["passed"] for item in results),
        "decision_counts": dict(Counter(item["actual"] for item in results)),
        "execution_successes": sum(
            item["actual"] == "ALLOW" for item in results
        ),
        "cases": results,
    }
    print(json.dumps(report, indent=2))
    return report


if __name__ == "__main__":
    report = run()
    raise SystemExit(0 if report["passed"] == report["total"] else 1)
