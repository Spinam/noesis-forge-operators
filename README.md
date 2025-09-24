# Noēsis Forge — Operator Lab (Public Spec)

**TL;DR**: Composable **operators (“ontoglyphs”)** that make model behavior *stable under reward hacking and confabulation*. Current milestone: **RCMO/CMO** — a safe activation/gating operator for reasoning loops with invariants, weights, and an evaluation harness.

> **Status:** Public, research-friendly spec with a minimal demo. This repo intentionally excludes private notebooks/logs and any clinical content. See [LEGAL/DISCLAIMER.md](LEGAL/DISCLAIMER.md).

## Why now
Brittle reasoning, confabulation, and reward hacking are expected behaviors of nascent cognition. Rather than deny them, we **design for them**: we build a middle layer of small, auditable operators that enforce local constraints and can be chained into **recursive ensembles** (debate schools, hybrid forests) to stabilize cognition.

## What’s in this repo
- **Spec + demo** of the `RCMO/CMO` operator (safe activation/gating inside task loops).
- **Append-only engine** skeleton for registering operator versions.
- **Evaluation harness** (toy) for sanity checks and reporting.
- **Docs/whitepapers**: the conceptual arc from recursive cognition to operator design, plus a short note on our prime-factorization period-finding experiment (novel, consistent; not more efficient).

## Quickstart
**Requirements:** Python 3.10+

```bash
# (optional) create and activate a virtualenv
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

# install
pip install -e .

# run a tiny demo
python examples/run_cmo_demo.py
```

Expected output: a short table of toy tasks with gate decisions and a mini report.

## Repo map
```
noesis-forge-operators/
├─ configs/
│  └─ cmo_v7.yaml                 # example weight schedule
├─ data/
│  └─ toy_tasks.jsonl             # tiny synthetic dataset
├─ docs/
│  ├─ overview.md                 # high-level design
│  └─ whitepapers/
│     ├─ RCMO_Primer.md
│     ├─ Recursive_Cognition_Arc.md
│     └─ Prime_Factorization_Period_Finding.md
├─ operators/
│  └─ cmo/
│     ├─ operator.json            # JSON spec for CMO
│     └─ configs/
│        └─ cmo_v7.yaml           # operator-local config
├─ schema/
│  └─ operator.schema.json        # minimal JSON Schema for operators
├─ src/noesis_forge/
│  ├─ engine/engine.py            # append-only registry skeleton
│  ├─ eval/harness.py             # toy evaluation harness
│  └─ operators/cmo_operator.py   # demo implementation
├─ examples/run_cmo_demo.py
├─ LEGAL/DISCLAIMER.md
├─ ROADMAP.md
├─ CONTRIBUTING.md
├─ CODE_OF_CONDUCT.md
├─ SECURITY.md
├─ LICENSE
└─ pyproject.toml
```

## Operator (ontoglyph) at a glance
- **Identity**: versioned, append-only registration.
- **Invariants**: safety/consistency conditions that must hold.
- **Weights**: explicit parameters (e.g., curiosity, rebuttal, safety).
- **Interface**: `apply(task, context) -> decision, rationale, logs`.
- **Eval**: reproducible, toy harness for sanity (no model calls here).

## Not clinical software
Our *therapeutic prosthetic* vision is long-term research. Nothing here is intended for diagnosis or treatment. See [LEGAL/DISCLAIMER.md](LEGAL/DISCLAIMER.md).

## Contributing & governance
- **Issues/PRs welcome** for spec clarifications, tests, and docs.
- Keep proprietary datasets/logs private.
- Use the sanitization guidance in this README and in docs.

## License
- **Code/spec**: MIT
- **Docs/whitepapers**: CC BY 4.0 (attribution to the Noēsis Forge project).

**Quick Links**  
- [Public CV](docs/cv/Stephen_Green_CV_PUBLIC.md)  
- [Whitepapers Index](docs/whitepapers/INDEX.md)  
- [Operator Spec & Demo (this repo)](README.md)


---

If this repo helps you, consider opening an issue with feedback, or sharing a link to your experiments. We’re building toward **neurocognitive prosthetics** through small, reliable building blocks.
