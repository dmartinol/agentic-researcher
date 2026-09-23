# Getting Started

`agentic-researcher` is intended to be installed into a compatible agent host. Researchers should not need to clone this development repository.

## 1. Install

Use the plugin/skill installation mechanism provided by your host to install the distributable package from the repository's `agentic-researcher/` subdirectory.

Installation syntax is host-specific. The package architecture does not depend on a particular installer. A compatible host should expose the portable Agent Skills; hosts supporting the Markdown `agents/` convention can also expose the specialized multi-agent workflow.

## 2. Connect providers

The default profile uses the Atlassian MCP declaration in `agentic-researcher/mcp.json` for Jira and Confluence. Authentication is handled by the host/client and is never stored in the research project.

Alternative providers may be used when they satisfy `agentic-researcher/docs/subsystem-capabilities.md`.

## 3. Start research

Start with the research question, for example:

> Research whether our platform should adopt an MCP aggregation layer. Compare architectural options, operational trade-offs, and security implications. Use authoritative sources and call out unresolved conflicts.

Setup clarifies scope, outputs, evidence requirements, subsystem configuration, and approval gates.

## 4. Approve plan and initialization

The user-facing lifecycle is:

```text
SETUP -> PLAN -> EXECUTE -> COMPLETE / VERIFY
```

Planning is read-only. External initialization is explicit and idempotent: existing resources must be discovered and reused rather than duplicated.

## 5. Inspect durable research

```text
RESEARCH.md
STATE.md
research/
├── memory/
│   ├── claims/
│   ├── sources/
│   └── episodes/
└── reports/
```

Research can resume from these artifacts without depending on prior conversation history.

## 6. Complete explicitly

Verification is read-only and checks evidence traceability, conflicts, freshness, subsystem resources, and links. Closing/transitions require explicit approval.

## Contributor validation

```bash
python scripts/validate.py
pytest -q
```

CI runs these checks on pull requests and main.

See `docs/demo-script.md` for the reproducible product demo.
