---
name: verify-research
description: Use before completing a research task or presenting a research package to verify evidence quality, contradiction/freshness checks, memory traceability, configured subsystem resources, and cross-links.
---

# Verify Research

Perform a read-only verification pass using generic research checks plus configured provider specializations.

## Research checks

- Required fields and acceptance criteria are addressed.
- Material conclusions trace to canonical claim IDs and sources where durable research memory is configured.
- Claim labels follow `Verified`, `Reported`, `Not established`, or `Conflicting`.
- `Not established` is not treated as proof of absence.
- Conclusion-critical claims received an active contradiction search.
- Time-sensitive conclusion-critical claims satisfy the configured freshness policy or are explicitly marked for revalidation.
- Credible conflicts are preserved rather than silently resolved.
- Superseded historical claims remain traceable when relevant.
- Synthesis does not silently fill missing dependency evidence.
- Derived indexes are not treated as canonical evidence.

## Subsystem checks

- Ticketing work-item identity, hierarchy, description, assignment/classification, and status match the approved configuration.
- Document identity, title, parent, content, and required work-item link match the approved configuration.
- Required reciprocal links resolve to the exact configured resources.
- Repository artifacts are present, traceable, and free of secrets.
- Existing meaningful content has not been replaced by initialization skeletons.
- No timeline, budget, staffing, or implementation-roadmap content was added unless explicitly in scope.

Apply verification rules from configured provider specializations when available. Otherwise verify only the generic capability contract and approved research configuration.

Return pass, warning, and blocking findings. Missing evidence for a conclusion-critical claim, an uninvestigated material conflict, or violated required freshness policy is blocking unless the approved research scope explicitly accepts that limitation.

Do not mutate resources during verification.
