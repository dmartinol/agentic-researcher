---
name: complete-research
description: Use only after research verification passes and the user approves completion to add a card-based closure comment and transition the Jira item using its verified workflow.
---

# Complete Research

Completion is an explicit approval-gated operation.

Before mutation:

- Verify the final Confluence page and exact Jira remote link.
- Query available Jira transitions and use the exact approved target status.
- Confirm the issue is the expected Sub-task under the expected Story.

The closure comment must use the host's structured document format with a
completion paragraph followed by a card linking to the exact Confluence page.
Do not put the page URL in a plain-text paragraph.

After mutation, verify the final Jira status and that the closure comment
contains the expected card URL. If any check fails, stop without guessing.
