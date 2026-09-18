---
name: execute-research
description: Use for executing an approved research Sub-task through a task-specific skill while recording evidence in the configured document store and repository.
---

# Execute Research

Execute only an approved Sub-task whose initialization has been verified.

## Workflow

1. Read the Jira description, acceptance criteria, linked page, research
   manifest, and assigned skill.
2. Confirm the task's dependencies are complete or explicitly approved.
3. Gather primary sources first and label material claims as `Verified`,
   `Reported`, `Not established`, or `Conflicting`.
4. Record findings in the linked Confluence page and supporting repository
   paths using the configured templates.
5. Preserve the Jira card, source traceability, and existing content.
6. Run the task-specific verification skill before requesting completion.

Independent Sub-tasks may execute in parallel. Synthesis tasks must wait for
their declared dependencies.

Do not transition or close the Jira item without explicit approval.
