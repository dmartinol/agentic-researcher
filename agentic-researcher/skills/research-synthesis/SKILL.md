---
name: research-synthesis
description: Use to synthesize evidence and dependent research tasks into traceable conclusions while preserving conflicts, gaps, scope, and uncertainty.
---

# Research Synthesis

Produce conclusions from durable research evidence, not from conversational recall.

## Inputs

Retrieve:

- acceptance criteria and synthesis question;
- relevant claims and supporting sources;
- conflicting and superseded claims;
- outputs of declared dependency tasks;
- unresolved questions and evidence gaps;
- scope and freshness requirements from `RESEARCH.md`.

## Synthesis method

1. Group claims by the question or decision criterion they address.
2. Separate established evidence from reported assertions and unresolved propositions.
3. Reconcile apparent conflicts caused by version, date, scope, terminology, or population differences.
4. Preserve genuine unresolved conflicts as `Conflicting`.
5. Identify missing evidence that materially limits the conclusion.
6. Derive only conclusions supported by the cited claims.
7. State important qualifications and applicability boundaries.
8. Link conclusions back to claim IDs/source evidence.

Do not resolve disagreement by majority vote or by assigning arbitrary numeric confidence.

## Dependent tasks

A Synthesis Task must not run until required Research Tasks are complete or explicitly waived. If a dependency is incomplete, identify the missing input rather than silently filling the gap with general knowledge.

## Output

A useful synthesis distinguishes:

- conclusions;
- supporting evidence;
- conflicts/limitations;
- unknowns;
- implications that follow from the evidence;
- follow-up research needed, if material.

Persist new durable synthesis claims through `manage-research-memory` when they are likely to be reused. Update the configured report/document output and concise `STATE.md`.
