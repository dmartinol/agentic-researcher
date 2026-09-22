---
name: verify-research
description: Use before completing a research task or presenting a research package to verify evidence, configured subsystem resources, repository traceability, and cross-links.
---

# Verify Research

Perform a read-only verification pass using generic subsystem checks plus the selected provider specializations.

## Generic checks

- Required fields and acceptance criteria are addressed.
- Major claims have sources or an explicit evidence label.
- `Not established` means reviewed sources do not establish the claim; it does not mean the capability is absent.
- Ticketing work-item identity, hierarchy, description, assignment/classification, and status match the approved configuration.
- Document identity, title, parent, content, and required work-item link match the approved configuration.
- Required reciprocal links resolve to the exact configured resources.
- Repository artifacts are present, traceable, and free of secrets.
- Existing meaningful content has not been replaced by initialization skeletons.
- No timeline, budget, staffing, or implementation-roadmap content was added unless explicitly in scope.

Apply the verification rules from each configured provider specialization when available. Otherwise verify only the generic capability contract and approved research configuration.

Return pass, warning, and blocking findings. Do not mutate resources during verification.
