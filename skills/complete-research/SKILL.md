---
name: complete-research
description: Use only after research verification passes and the user explicitly approves completion to record closure and transition configured external work items.
---

# Complete Research

Completion is an explicit approval-gated operation.

Before mutation:

- confirm verification has no unresolved blocking findings;
- resolve the exact ticketing work item and final document/output resources;
- discover allowed ticketing transitions rather than guessing a status;
- confirm the target item belongs to the expected research hierarchy;
- compose provider-specific closure rules for the selected ticketing/document providers.

Record a concise completion reference linking the exact final research output using the provider's supported rich-link representation when configured.

After mutation, read back and verify the final work-item status and closure reference. If any check fails, stop without guessing.

When Jira and Confluence are selected, apply the `jira-research` and `confluence-research` closure conventions.
