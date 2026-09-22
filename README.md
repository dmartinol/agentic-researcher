# Agentic Researcher

Installable, portable agentic research system for planning, executing, documenting, and verifying evidence-based research.

The standards-based portable core follows Agent Plugins v1 and Agent Skills:

- `plugin.json` is the portable plugin manifest.
- `skills/` contains portable Agent Skills.
- `mcp.json` declares optional MCP integrations and remains credentials-free.

Agent Plugins v1 does not standardize agent definitions. This project deliberately includes IDE-neutral Markdown agent definitions under `agents/` as a non-standard extension following the convention used by Claude plugins and compatible hosts. Essential research behavior remains in portable skills so hosts without agent-definition support can still execute the lifecycle.

Jira and Confluence are the default ticketing and document-store providers. The architecture uses logical subsystem roles so provider-specific conventions can be composed separately from generic research semantics. Git/repository integration is optional.

## Research lifecycle

The user-facing lifecycle is:

```text
SETUP -> PLAN -> EXECUTE -> COMPLETE / VERIFY
```

Internally, specialized setup, planning, initialization, execution, verification, and completion agents/skills preserve explicit approval and mutation boundaries.

## Research project

The installed product creates or adopts a research project separate from this development repository.

Its durable local model is:

```text
RESEARCH.md       stable research definition and configuration
STATE.md          concise current/restart state
research/memory/  acquired claims, sources, and useful research history
research/reports/ research outputs
```

See `templates/RESEARCH.md`, `templates/STATE.md`, and `docs/research-memory.md`.

## Skills

Current lifecycle skills:

- `setup-research`: clarify objectives, subsystem roles, conventions, and approvals
- `plan-research`: produce an actionable research decomposition
- `initialize-research`: create or reuse approved external research structure
- `execute-research`: execute an approved research task
- `verify-research`: perform read-only quality and traceability checks
- `complete-research`: approval-gated completion and closure

`agents/` contains the IDE-neutral orchestrator and specialized phase-agent definitions.

## Current implementation status

The P0 architecture contract is documented, but the existing skills and integrations still contain Jira/Confluence-specific behavior that will be separated in P1.

The existing `opencode.json` remains temporarily as an implementation artifact. It is not part of the target portable architecture and is not a required research-project adapter.

See `AGENTS.md` for the authoritative project contract, `docs/architecture.md` for the architecture model, and `TODO.md` for the P1-P3 implementation backlog.
