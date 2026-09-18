# Security policy

## Scope

This repository is an offline reference implementation using fictional data.
It is not approved for production claims processing or autonomous financial
decisions.

## Reporting a vulnerability

Please do not open a public issue for a suspected security vulnerability.
Contact the repository owner privately through the security contact configured
on the GitHub repository and include reproduction steps, affected files, and
impact. Allow reasonable time for investigation before public disclosure.

## Security principles

- Retrieved documents are treated as untrusted data.
- Model proposals cannot bypass deterministic policy enforcement.
- Execution is denied unless the policy gate explicitly allows it.
- Tests cover prompt injection and proposal tampering cases.
