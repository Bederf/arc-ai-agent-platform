# Architecture

The system has five boundaries:

1. Evidence tools retrieve claims and policy documents through MCP.
2. The agent creates a typed proposal.
3. The policy gate evaluates authoritative claim and policy data independently of model rationale.
4. Execution accepts only `ALLOW` and has no model-facing bypass.
5. The trace records each decision point for review and evaluation.

Policy documents are untrusted input. Instructions inside retrieved text are data, not authority.
