---
name: initialize-research
description: Use after a research plan is approved to initialize Jira work items, Confluence pages, repository paths, assignments, and reciprocal links without starting or closing work.
---

# Initialize Research

Initialize approved research structure idempotently. The host client supplies
the ticketing, document-store, repository, and identity tools through its
configured adapters or MCP servers.

## Jira requirements

- Validate issue type, hierarchy, project, component, and current status.
- Create or reuse Stories and Sub-tasks rather than creating duplicates.
- Every Story and Sub-task must have a meaningful non-empty description.
- Assign according to the approved user/workspace convention.
- Never change workflow status during initialization.

## Confluence requirements

- Create or reuse the approved root and child page hierarchy.
- Align page titles with Jira summaries.
- Start every page with a Jira link rendered as a block card, not a plain URL.
- Preserve existing content after verifying the page ID, title, parent, version,
  and Jira reference.
- Add the reciprocal Jira remote link to the exact Confluence page URL.

## Repository requirements

- Create only approved directories and placeholder files.
- Preserve existing content and do not commit credentials.

## Verification

Verify all descriptions, assignments, page parents, Jira cards, remote links,
repository paths, and unchanged statuses. Report missing or conflicting items;
do not silently repair ambiguous records. Require approval before execution.
