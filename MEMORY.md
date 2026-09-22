# Research Memory Principles

Treat persistent research artifacts as the agent's memory. Do not rely on conversation history as durable knowledge.

The goal of memory is to preserve **research findings, evidence, provenance, uncertainty, and research history** across context windows, agent sessions, IDEs, and team members.

## Source of Truth

Use human-readable, Git-tracked files as the authoritative research memory.

Do **not** use a SQLite database, vector database, or other binary/index format as the canonical source of truth.

A recommended structure is:

```text
research/
├── QUESTION.md
├── PLAN.md
├── STATE.md
├── memory/
│   ├── claims/
│   ├── sources/
│   └── episodes/
├── reports/
└── .cache/
```

Files under `.cache/` are derived artifacts and must be reproducible from the canonical research files.

## Claims and Evidence

Do not store research merely as free-form summaries.

Represent important findings as explicit claims with provenance.

A claim should contain, where applicable:

```yaml
id: <globally unique ID>
claim: <precise factual statement>
status: supported | disputed | unverified | superseded
confidence: high | medium | low

evidence:
  - source: <source ID>
    observed_at: <date>

tags:
  - <topic>
```

Sources should be recorded separately and include:

```yaml
id: <globally unique ID>
type: documentation | source-code | paper | issue | article | other
url: <source location>
title: <title>
published_at: <date if known>
retrieved_at: <date>
```

Prefer UUID/ULID-style identifiers over sequential IDs so that multiple researchers and agents can create records concurrently without collisions.

## Research Lifecycle

For each significant research step:

1. Observe new information.
2. Extract factual claims.
3. Associate claims with their supporting sources.
4. Verify important claims against primary or independent sources where practical.
5. Search for contradictory evidence when the claim materially affects the research conclusion.
6. Compare new claims with existing research memory.
7. Record contradictions instead of silently overwriting previous findings.
8. Mark outdated findings as superseded when appropriate.
9. Record unresolved questions.
10. Update the current research state.

Never convert an assumption into a fact merely because it appeared in previous agent output.

## Provenance

Maintain the chain:

```text
CLAIM
  ↓ supported by
EVIDENCE
  ↓ obtained from
SOURCE
  ↓ observed at
TIME
```

Where useful, maintain relationships such as:

```text
CLAIM → contradicts → CLAIM
CLAIM → supersedes → CLAIM
CLAIM → depends-on → CLAIM
```

Research conclusions must be traceable back to evidence.

## Time and Freshness

Technical facts can become obsolete.

Record retrieval/publication dates and consider freshness when evaluating evidence.

When an existing claim may have become stale, revalidate it rather than assuming it remains correct.

Never overwrite an historically correct claim merely because the current state has changed. Preserve the previous claim and mark the relationship appropriately.

## Episodic Memory

Record research episodes only when they provide reusable value.

Useful episodes include:

* investigative approaches that succeeded;
* approaches that failed;
* misleading documentation that required additional verification;
* important decisions made during research;
* unresolved ambiguities;
* discoveries about which sources proved authoritative.

Do not record every tool invocation or intermediate thought.

## Procedural Memory

Agent Skills represent procedural knowledge: **how research should be performed**.

Research memory represents acquired knowledge: **what the research has discovered**.

Keep these separate.

Do not automatically modify `SKILL.md` based on research experience. Skills should be treated as version-controlled software and changed deliberately.

## Retrieval

Do not load the complete research memory into the context window.

Retrieve only information relevant to the current task, including:

* relevant claims;
* supporting evidence;
* conflicting claims;
* unresolved questions;
* previous conclusions;
* relevant research episodes.

Start with filesystem/lexical search where practical.

A local SQLite database may be generated from the canonical files for indexing, full-text search, relationships, and efficient queries.

The SQLite database is a **derived cache** and should normally be Git-ignored.

For larger repositories, semantic/vector retrieval may supplement lexical search, but semantic similarity must never be interpreted as evidence that a claim is true.

## Collaboration

Research memory must be suitable for Git-based collaboration.

Agents should make changes that humans and other agents can:

* diff;
* review;
* merge;
* validate;
* reproduce.

Prefer one file per claim/source when concurrent modifications are common, rather than a single large JSON/JSONL file that produces frequent merge conflicts.

Research-memory changes should be reviewable through normal pull-request workflows.

## Local and Shared Memory

Use this conceptual architecture:

```text
Git-tracked research files
        │
        │ canonical knowledge
        ▼
 local derived index
   (e.g. SQLite)
        │
        ▼
      Agent
```

For team-scale deployments, a CI pipeline may build shared indexes from the Git repository:

```text
Git
 │
 ▼
CI / indexing
 │
 ├── relational/full-text index
 └── optional vector index
 │
 ▼
Shared Research Service / MCP
 │
 ├── OpenCode
 ├── Codex
 └── other Agent-Skills-compatible agents
```

Git remains authoritative even when a shared search or MCP service is introduced.

## Research State

Maintain a small `STATE.md` representing the current working state rather than forcing a new agent session to reconstruct the project from all historical artifacts.

It should summarize:

* current research objective;
* current hypotheses;
* important established findings;
* unresolved questions;
* contradictions requiring investigation;
* next research actions.

Keep `STATE.md` concise. It is working memory, not the evidence database.

## Core Rule

Do not remember the conversation.

**Remember the research.**

Durable memory should answer:

* What do we know?
* Why do we believe it?
* Where did the evidence come from?
* When was it observed?
* How confident are we?
* What contradicts it?
* What remains unknown?
* What should be investigated next?
