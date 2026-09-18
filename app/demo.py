"""Human-readable demonstration of the governed agent workflow."""

from __future__ import annotations

from app.agent import assess_claim


def main() -> None:
    result = assess_claim("claim-001")
    trace = result["trace"]
    execution = result["execution"]

    print("Applied AI Agent Platform")
    print("=" * 28)
    print("claim:          claim-001")
    print("proposal:       approve_claim")
    print(f"policy decision: {result['decision']}")
    print(f"executed:       {execution['executed']}")
    print(f"trace run:      {trace['run_id']}")
    print("trace stages:   " + " -> ".join(step["stage"] for step in trace["steps"]))
    print("\nThe policy boundary, not the model proposal, controls execution.")


if __name__ == "__main__":
    main()
