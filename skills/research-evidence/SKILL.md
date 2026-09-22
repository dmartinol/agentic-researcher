---
name: research-evidence
description: Use to discover, evaluate, acquire, and reconcile evidence for material research claims, including contradiction and freshness checks.
---

# Research Evidence

Build traceable evidence for a research question without treating search results, prior agent output, or semantic similarity as proof.

## Start from the question

Translate the task into explicit evidence needs:

- claims that must be established;
- claims that would materially change the conclusion if false;
- relevant scope, version, geography, population, and time window;
- acceptable source types and freshness rules from `RESEARCH.md`.

Retrieve relevant existing claims and sources before searching so the investigation can confirm, update, or challenge what is already known.

## Source discovery

Prefer the strongest available evidence for the claim:

1. direct primary evidence such as official documentation, specifications, source code, datasets, filings, or original research;
2. independent authoritative or expert sources;
3. credible secondary reporting;
4. discovery sources that lead to stronger evidence.

Vendor/author statements can establish what that source reports, but do not automatically establish independent truth. Search snippets, generated summaries, and uncited prior agent statements are discovery aids, not evidence.

Record useful sources through `manage-research-memory`.

## Claim extraction

Make each durable claim precise enough to be challenged independently. Avoid combining several facts into one claim when they may have different evidence.

For each material claim record:

- exact statement;
- evidence label: `Verified`, `Reported`, `Not established`, or `Conflicting`;
- supporting source IDs and the relevant evidence/location;
- observation/retrieval time;
- scope/version/time qualifications;
- relationships to existing claims when applicable.

Do not invent numeric confidence scores.

## Evidence labels

- **Verified**: direct authoritative evidence establishes the claim within its stated scope.
- **Reported**: a credible source states the claim, but it is not independently/directly established.
- **Not established**: reviewed evidence does not establish the proposition. This is not evidence of absence.
- **Conflicting**: credible evidence materially disagrees and the conflict remains unresolved.

A label describes evidence state, not certainty about all possible worlds.

## Contradiction search

For every conclusion-critical claim, actively try to falsify or qualify it before synthesis:

- search for authoritative sources that disagree;
- check newer versions/dates;
- inspect exceptions, limitations, and scope differences;
- compare independent evidence where practical.

Preserve credible disagreement. Do not choose a convenient source and discard the conflict.

## Freshness

Use publication/version dates and `retrieved_at` to judge whether evidence is current enough for the approved policy. Revalidate stale conclusion-critical claims. If a newer claim replaces an historically correct one, preserve both and use a `supersedes` relationship.

## Stop condition

Evidence gathering may stop when acceptance criteria are covered and conclusion-critical claims have adequate source quality, contradiction search, and freshness checks. Record unresolved gaps explicitly rather than extending research indefinitely.
