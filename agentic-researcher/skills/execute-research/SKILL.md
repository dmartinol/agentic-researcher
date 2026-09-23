---
name: execute-research
description: Use for executing an approved research task by retrieving existing memory, acquiring evidence, recording claims, synthesizing findings, and updating configured outputs.
---

# Execute Research

Execute only an approved Research Task whose required initialization and dependencies are satisfied. This skill orchestrates portable research capabilities; it must remain useful without a topic-specific skill.

## Workflow

1. Read `RESEARCH.md`, `STATE.md`, task acceptance criteria, dependencies, expected outputs, and any assigned topic-specific skill.
2. Resolve linked external resources through their logical subsystem IDs.
3. Use `manage-research-memory` to retrieve relevant existing claims, sources, conflicts, and useful episodes.
4. Use a topic-specific skill when assigned; otherwise execute the investigation directly using `research-evidence`.
5. Acquire/evaluate sources and extract atomic material claims with provenance.
6. For conclusion-critical claims, perform contradiction and freshness checks through `research-evidence`.
7. Persist/reconcile sources and claims through `manage-research-memory`; preserve conflicts and superseded historical claims.
8. For Synthesis Tasks, or when task findings must be combined, apply `research-synthesis`.
9. Update configured human-readable outputs using applicable provider specializations.
10. Update `STATE.md` concisely and run `verify-research` before requesting completion.

## Execution quality

Do not treat prior agent output, search snippets, semantic similarity, or repeated assertions as evidence.

Prefer direct/authoritative evidence where appropriate, but distinguish what a source directly establishes from what it merely reports. Record unresolved gaps instead of inventing facts.

Independent Research Tasks may execute in parallel. Synthesis Tasks wait for declared dependencies unless the approved plan explicitly waives one.

Do not transition or close an external work item without explicit approval.
