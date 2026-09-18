---
name: setup-research
description: Use when starting a new research initiative and the user needs objectives, scope, service roles, conventions, approvals, and persistent settings clarified before planning.
---

# Set Up Research

Turn an initial research requirement into an approved research configuration.
Do not create tickets, pages, files, or MCP connections until the user approves
the resolved setup.

## Clarify

Confirm:

- Research objective and audience
- In-scope and out-of-scope questions
- Evidence policy and source quality expectations
- Expected outputs and repository needs
- Ticketing, document-store, repository, and identity service roles
- Jira hierarchy, components, labels, assignment rules, and status conventions
- Confluence root, page hierarchy, layouts, Jira card links, emojis, and closure comments
- Approval gates before planning, mutation, execution, and closure

## Service roles

Use logical roles rather than vendor names:

- `ticketing`
- `document_store`
- `repository`
- `identity`

Jira and Confluence are the default role choices. If the user supplies MCP
services, discover and verify the capabilities needed for each role. Do not
store credentials in the research configuration; store only client-managed
authentication references.

## Persistent settings

Store the approved user/workspace configuration in the host agent's persistent
memory, separate from conversation context and research findings. Include:

- Selected service adapters and capability names
- Project/space/root identifiers
- Page and ticket conventions
- Evidence labels and comment templates
- Approval preferences

Never store tokens, passwords, private keys, or authorization headers.

## Output

Present a configuration summary and unresolved questions. Require explicit user
approval before handing the result to `plan-research`.
