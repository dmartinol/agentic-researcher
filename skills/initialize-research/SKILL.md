---
name: initialize-research
description: Use after a research plan is approved to create or reuse configured external work items, documents, and repository artifacts idempotently without starting or closing work.
---

# Initialize Research

Initialize the approved research structure through configured logical subsystems. Use the capability contracts in `docs/subsystem-capabilities.md` and compose provider-specific skills for selected providers.

## Ticketing

- Discover existing work items before creation.
- Create or reuse the approved work hierarchy.
- Preserve meaningful descriptions and metadata.
- Apply approved assignment and classification conventions.
- Do not change workflow status unless initialization explicitly requires and approves it.
- Record stable external IDs and URLs in the research configuration/state as appropriate.

## Document store

- Discover existing documents before creation.
- Create or reuse the approved document hierarchy.
- Preserve existing meaningful content.
- Apply approved title, parent, template, and cross-link conventions.
- Record stable document IDs and URLs.

## Repository

- Create only approved directories/artifacts.
- Preserve existing content.
- Never write credentials or secrets.

## Provider composition

When Jira is the ticketing provider, apply `jira-research`. When Confluence is the document-store provider, apply `confluence-research`. Provider skills may add richer validation and linking requirements but must not weaken the generic safety rules.

## Verification

After each mutation, read back enough state to verify identity, hierarchy, metadata, links, and unchanged fields that matter. Report ambiguous or conflicting resources rather than guessing or silently replacing them.

Update `STATE.md` with initialized/blocked work and require approval before execution.
