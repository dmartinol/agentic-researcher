---
name: verify-research
description: Use before completing a research task or presenting a research package to verify evidence, page structure, Jira metadata, repository traceability, and reciprocal links.
---

# Verify Research

Perform a read-only verification pass.

## Checks

- Required fields and acceptance criteria are addressed.
- Major claims have sources or an explicit evidence label.
- `Not established` means sources do not establish the claim; it does not mean
  the capability is absent.
- Jira issue type, parent, component, assignee, description, and status are correct.
- Confluence page title, parent, version, Jira block card, and content are correct.
- Jira contains the exact reciprocal page remote link.
- Repository artifacts are present, traceable, and free of secrets.
- No timeline, budget, staffing, or implementation-roadmap content was added
  unless explicitly in scope.

Return a verification report with pass, warning, and blocking findings.
