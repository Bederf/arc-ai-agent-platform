# Contributing

Thanks for contributing. Keep changes small, testable, and consistent with the
governance boundaries documented in `docs/architecture.md`.

## Development

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e '.[dev]'
pytest
python3 -m evaluation.run
```

Every change should include tests for new behavior. Do not add real personal,
claims, policy, or production credentials; the reference dataset is fictional.

## Pull requests

Describe the behavior changed, the safety boundary affected, and the tests
run. Pull requests must pass the GitHub Actions quality workflow.
