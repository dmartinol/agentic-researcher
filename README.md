# Agentic Researcher

[![Validate package](https://github.com/dmartinol/agentic-researcher/actions/workflows/validate.yml/badge.svg)](https://github.com/dmartinol/agentic-researcher/actions/workflows/validate.yml)
[![GitHub release](https://img.shields.io/github/v/release/dmartinol/agentic-researcher?include_prereleases)](https://github.com/dmartinol/agentic-researcher/releases)
[![License](https://img.shields.io/github/license/dmartinol/agentic-researcher)](https://github.com/dmartinol/agentic-researcher/blob/main/LICENSE)


Installable, portable agentic research system for planning, executing, documenting, and verifying evidence-based research.

The standards-based portable core follows Agent Plugins v1 and Agent Skills:

- `plugin.json` is the portable plugin manifest.
- `skills/` contains portable Agent Skills.
- `mcp.json` declares the default portable Atlassian MCP connection and remains credentials-free.

Agent Plugins v1 does not standardize agent definitions. This project deliberately includes IDE-neutral Markdown agent definitions under `agents/` as a non-standard extension following the convention used by Claude plugins and compatible hosts. Essential research behavior remains in portable skills so hosts without agent-definition support can still execute the lifecycle.

## Providers and subsystems

Lifecycle skills use logical subsystem roles:

- `ticketing`
- `document_store`
- optional `repository`
- `identity`

Provider-specific behavior is composed through specialized skills. Jira and Confluence are the default providers, implemented by `jira-research` and `confluence-research`.

The plugin declares Atlassian's remote MCP endpoint in portable `mcp.json`. Authentication remains client-managed; the package contains no credentials. Alternative providers can satisfy the capability contracts documented in `docs/subsystem-capabilities.md`.

No host-specific adapter is required by the project architecture.

## Research lifecycle

```text
SETUP -> PLAN -> EXECUTE -> COMPLETE / VERIFY
```

Internally, specialized setup, planning, initialization, execution, verification, and completion agents/skills preserve explicit approval and mutation boundaries.

## Research project

```text
RESEARCH.md       stable research definition and configuration
STATE.md          concise current/restart state
research/memory/  acquired claims, sources, and useful research history
research/reports/ research outputs
```

See `templates/RESEARCH.md`, `templates/STATE.md`, and `docs/research-memory.md`.

## Skills

Lifecycle skills:

- `setup-research`
- `plan-research`
- `initialize-research`
- `execute-research`
- `verify-research`
- `complete-research`

Research capabilities:

- `research-evidence`: source quality, claims, contradiction search, freshness
- `manage-research-memory`: durable claims/sources/episodes and selective retrieval
- `research-synthesis`: traceable synthesis across evidence and dependent tasks

Provider specializations:

- `jira-research`
- `confluence-research`

`agents/` contains the IDE-neutral orchestrator and specialized phase-agent definitions.

## Install and validate

Researchers install the package using their host's plugin/skill installation mechanism; cloning this development repository is not part of the research workflow. See `docs/getting-started.md`.

Contributors can run `python scripts/validate.py` and `pytest -q`. CI enforces package structure and the generic/provider architecture boundary.

The reproducible product demo is documented in `docs/demo-script.md` and `examples/demo-research/`.

See `AGENTS.md` for the authoritative project contract, `docs/architecture.md` for the architecture model, and `TODO.md` for the remaining roadmap.
