# Overview

**Goal:** Build small, auditable **operators (“ontoglyphs”)** that stabilize model behavior under confabulation and reward hacking, then chain them into **recursive ensembles** (debate schools, forests) and, eventually, **neurocognitive prosthetics**.

## Operators
- **One-to-one behavior**: explicit identity, version, invariants
- **Weights**: curiosity/rebuttal/safety/consistency
- **Interface**: `apply(task, context) -> decision, rationale`
- **Evaluation**: deterministic, reproducible, model-free demos in this repo

## CMO (RCMO)
Constraint Modulation Operator that acts like a **safe activation/gating** function inside a reasoning loop. It *does not* call a model here; it shows how to combine invariants and weights to produce a gate decision.

## Registry
We use an **append-only** registry pattern: versions are appended, not overwritten. This improves auditability and supports research forks without destroying provenance.

## Vision
- Operators → **Akashic Agents** (ensembles with debate & suppression/boosting)
- Agents → **therapeutic symbionts** (long‑term research; non‑clinical in this repo)
