# Contributing

Thanks for considering a contribution! This repo is a **public spec + demo**. We welcome:
- Clarifications to the operator schema/spec,
- Tests and examples for the evaluation harness,
- Documentation and whitepaper improvements.

## Ground rules
- Do not commit private datasets, logs, or secret keys.
- Keep clinical/therapeutic claims out of code and docs.
- Be kind and specific in code review; prefer small, focused PRs.

## How to propose changes
1. Open an issue describing the problem and your proposal.
2. If the change affects the public spec, include a small example.
3. Submit a PR linked to the issue; keep commits tidy and documented.

## Local dev
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
python examples/run_cmo_demo.py
```

## License
By contributing, you agree your contributions will be licensed under the repository’s license.
