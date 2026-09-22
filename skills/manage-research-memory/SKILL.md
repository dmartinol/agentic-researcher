---
name: manage-research-memory
description: Use to persist, retrieve, relate, and update durable research claims, sources, and useful episodes without relying on conversation history.
---

# Manage Research Memory

Maintain `research/memory/` as authoritative acquired research knowledge. Human-readable files are canonical; indexes are derived.

## Canonical layout

```text
research/memory/
├── claims/
├── sources/
└── episodes/
```

Use one file per object and globally unique IDs such as UUIDs or ULIDs. Use the templates under `templates/memory/`.

## Sources

Before creating a source, search existing source records for the same canonical location/resource. Reuse the existing ID when it represents the same source.

A source record preserves identity, type, location, title, publication/version metadata when known, retrieval time, and notes needed to relocate the evidence.

Do not copy entire source documents into memory merely for convenience.

## Claims

A claim is an atomic, challengeable research statement. Before creating one, retrieve semantically/lexically relevant claims and decide whether the new observation:

- supports an existing claim;
- qualifies it;
- contradicts it;
- supersedes it;
- depends on it;
- is genuinely new.

Preserve prior claims rather than rewriting history. Update relationships and evidence state when new evidence changes the current understanding.

Use the project evidence labels: `Verified`, `Reported`, `Not established`, and `Conflicting`. Do not add numeric confidence.

## Episodes

Create an episode only when the research trajectory itself has reusable value: a failed/successful investigative approach, important research decision, misleading source, unresolved ambiguity, or discovery about where authoritative evidence lives.

Do not record routine tool calls, chain-of-thought, or a transcript of the conversation.

## Retrieval

Retrieve selectively for the current task:

1. search claim/source metadata and text lexically;
2. follow explicit claim/source relationships;
3. include supporting and conflicting claims;
4. include relevant unresolved questions/episodes;
5. use a derived full-text or vector index only as a retrieval aid.

Semantic similarity is not evidence of truth.

## Derived indexes

SQLite, FTS, embeddings, or vector stores may be generated under `research/.cache/`. They must be reproducible from canonical files and must never become the only source of truth.

## STATE.md

After meaningful research progress, update `STATE.md` with only what is needed to resume: current objective/work status, immediately relevant established findings, unresolved questions/conflicts, and next actions. Link/reference canonical claim IDs where useful instead of duplicating the evidence store.

Core rule: do not remember the conversation; remember the research.
