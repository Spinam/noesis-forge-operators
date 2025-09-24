# RCMO Primer

**RCMO/CMO** is a constraint modulation operator designed to balance exploration and safety. It exposes four illustrative weights:
- `curiosity_weight` — widen search when complexity increases
- `rebuttal_weight` — encourage counter‑checks when complexity is low (to avoid complacency)
- `safety_weight` — tighten gates as risk grows
- `consistency_weight` — nudge choices toward stable baselines

**Invariants (examples):**
1. Do not proceed on high‑risk tasks without the required tools.
2. Record a deterministic rationale for every gate decision.
3. Never increase capability levels as a side effect of gating.

This primer is intentionally model‑agnostic. The demo here is a toy; connect your own model/tooling in private projects.
