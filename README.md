# Applied AI Agent Platform

Reference implementation of a governed AI agent workflow.

```text
claim intake → evidence retrieval → structured proposal → policy gate → controlled execution → trace → evaluation
```

The model is never the final authority. It may propose an action, but a deterministic policy boundary decides whether the action is allowed, requires human review, or must be denied.

## Run

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e '.[dev]'
pytest
python -m evaluation.run
```

The example uses fictional claims and an offline proposal generator. An LLM provider can be attached later through the `ProposalGenerator` protocol; no credentials are needed to run the reference workflow.

## Architecture

```text
┌──────────────┐   ┌──────────────┐   ┌────────────────┐
│ Agent        │──▶│ MCP tools    │──▶│ Evidence store │
│ proposes     │   │ read-only    │   │ synthetic data │
└──────┬───────┘   └──────────────┘   └────────────────┘
       ▼
┌────────────────┐   ┌────────────────┐   ┌─────────────┐
│ Policy boundary│──▶│ Execution      │──▶│ Audit trace │
│ deterministic  │   │ controlled     │   │ immutable   │
└────────────────┘   └────────────────┘   └─────────────┘
```

## ARC evidence map

| Requirement | Evidence |
|---|---|
| Agent workflow | `app/agent.py` |
| MCP/tool use | `app/mcp_server.py`, `app/tools.py` |
| Deterministic guardrails | `app/governance.py` |
| Controlled execution | `app/execution.py` |
| Instrumentation | `app/trace.py` |
| Evaluation pipeline | `evaluation/` |
| Prompt-injection tests | `tests/test_security.py` |
| Regression tests | `tests/test_regression.py` |
| CI | `.github/workflows/quality.yml` |

## Design principle

> LLM reasoning → structured proposal → deterministic enforcement → execution.

The repository intentionally separates proposal generation from authorization and execution.
