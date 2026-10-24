# ARC — Applied AI Agent Platform

[![Quality](https://github.com/Bederf/arc-ai-agent-platform/actions/workflows/quality.yml/badge.svg)](https://github.com/Bederf/arc-ai-agent-platform/actions/workflows/quality.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](pyproject.toml)
[![MCP](https://img.shields.io/badge/MCP-supported-6E56CF)](app/mcp_server.py)

## A small, runnable reference for governed AI agents

ARC shows how to build an AI workflow where the model can reason and propose, but cannot silently authorise or execute an action.

```text
claim intake → evidence retrieval → structured proposal → policy gate
           → controlled execution → audit trace → evaluation
```

The project is intentionally compact and offline. It is designed to be read, run, tested and adapted.

## Why ARC exists

Many agent demos stop at “the model called a tool”. Real systems need a clear answer to a harder question:

> What is allowed to happen after the model makes a proposal?

ARC puts that decision in deterministic, inspectable software. Every proposal becomes one of three outcomes:

- **ALLOW** — the action satisfies policy and may enter controlled execution;
- **REQUIRE_HUMAN_REVIEW** — the action may be plausible, but a person must approve it;
- **DENY** — the action violates policy or lacks authoritative evidence.

## Run the complete workflow

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e '.[dev]'

pytest
python3 -m app.demo
python3 -m evaluation.run
```

No API keys or external services are required. The demo uses fictional claims, synthetic evidence and an offline proposal generator.

The evaluation reports decision distribution and successful executions instead of reducing the result to a single pass/fail number.

## What you can learn from it

- How to put a typed proposal boundary between reasoning and execution
- How read-only MCP tools can provide evidence without granting authority
- How to enforce policy independently of model rationale
- How to test prompt injection and proposal tampering
- How to require human review for high-impact actions
- How to record decisions and execution stages for later inspection
- How to evaluate agent behavior with a small deterministic dataset

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

The key separation is:

```text
LLM reasoning → structured proposal → deterministic enforcement → execution
```

See the [architecture notes](docs/architecture.md) for the contracts and boundaries.

## Repository map

| Concern | Implementation |
|---|---|
| Agent workflow | [`app/agent.py`](app/agent.py) |
| Typed domain models | [`app/models.py`](app/models.py) |
| Evidence tools and MCP | [`app/tools.py`](app/tools.py), [`app/mcp_server.py`](app/mcp_server.py) |
| Deterministic policy | [`app/governance.py`](app/governance.py) |
| Controlled execution | [`app/execution.py`](app/execution.py) |
| Audit instrumentation | [`app/trace.py`](app/trace.py) |
| Evaluation | [`evaluation/`](evaluation/) |
| Security tests | [`tests/test_security.py`](tests/test_security.py) |
| Workflow/regression tests | [`tests/test_workflow.py`](tests/test_workflow.py), [`tests/test_regression.py`](tests/test_regression.py) |

## Scope and limitations

ARC is a reference implementation, not a production claims system. It uses synthetic data, an offline proposal generator and a deliberately controlled execution adapter.

A production deployment would still need real identity and authorization, durable audit storage, privacy controls, provider evaluation, operational processes and domain-specific review.

## Design principle

> **AI may propose. Evidence, policy and accountable software decide what can happen.**

## Contributing

The most useful contributions are small, testable extensions that preserve the authority boundary. See [CONTRIBUTING.md](CONTRIBUTING.md) and open an issue or pull request with the intended behavior, policy impact and tests.

## Project documents

- [Architecture](docs/architecture.md)
- [Incident response](docs/incident-response.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [License](LICENSE)
