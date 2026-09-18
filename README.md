# Applied AI Agent Platform

[![Quality](https://github.com/Bederf/arc-ai-agent-platform/actions/workflows/quality.yml/badge.svg)](https://github.com/Bederf/arc-ai-agent-platform/actions/workflows/quality.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Reference implementation of a governed AI agent workflow.

```text
claim intake → evidence retrieval → structured proposal → policy gate → controlled execution → trace → evaluation
```

The model is never the final authority. It may propose an action, but a deterministic policy boundary decides whether the action is allowed, requires human review, or must be denied.

## Run

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e '.[dev]'
pytest
python3 -m evaluation.run
python3 -m app.demo
```

The demo prints the complete governed path and its audit stages:

```text
claim → proposal → policy decision → controlled execution → trace
```

The evaluation report also summarizes decision distribution and successful
executions, making regression results visible in CI rather than reducing them
to a single pass/fail number.

The example uses fictional claims and an offline proposal generator. An LLM provider can be attached later through the `ProposalGenerator` protocol; no credentials are needed to run the reference workflow.

## What this demonstrates

- A typed proposal boundary between agent reasoning and execution
- Read-only MCP tools for evidence retrieval
- Deterministic authorization independent of model rationale
- Prompt-injection and proposal-tampering regression tests
- Traceable policy and execution decisions
- CI evaluation with decision-distribution and execution metrics

## Limitations

This is a compact reference implementation, not a production claims system.
The data is synthetic, the proposal generator is offline, and the execution
adapter is intentionally controlled. Production use would require real
identity, authorization, audit storage, privacy controls, provider evaluation,
and human operational processes.

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

## Project documents

- [Architecture](docs/architecture.md)
- [Incident response](docs/incident-response.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [License](LICENSE)
