---
name: jira-research
description: Compose when Jira implements the ticketing subsystem to apply Jira-specific research hierarchy, metadata, linking, verification, and closure conventions.
---

# Jira Research Provider

Apply these conventions only when the approved `ticketing` provider is Jira.

## Setup and planning

Propose defaults and let the researcher confirm or override them:

- hierarchy: Initiative / Epic / Story / Sub-task, constrained by the target Jira project;
- component policy;
- label policy;
- assignment convention;
- target workflow/status convention.

Map provider-neutral Workstreams, Research Tasks, and Synthesis Tasks onto the approved Jira hierarchy. Do not force every Jira level when the project configuration or research plan does not need it.

Every research work item must have a meaningful non-empty description.

## Initialization

- Resolve project and current-user context before mutation.
- Discover/reuse existing issues by stable identity where possible.
- Verify issue type, parent, description, component/labels, assignee, and current status after mutation.
- Do not transition issues merely as part of initialization.
- When a document exists for the work item, add a reciprocal Jira link to the exact document URL.
- Preserve existing Jira content and links.

## Verification

Verify applicable Jira fields:

- issue identity/key;
- issue type;
- parent/hierarchy;
- description;
- component and labels;
- assignee;
- status;
- exact reciprocal document link.

Treat ambiguous issue matches as blocking.

## Completion

Before closure, query available transitions and select only the exact approved target transition.

Add a concise completion comment referencing the exact final research document. When the integration supports rich/card links, prefer that representation over a bare URL.

After mutation, verify final status and completion reference. Never close without explicit user approval.
