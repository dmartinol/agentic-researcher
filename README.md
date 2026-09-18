# Agentic Researcher

Portable Agent Plugin for planning and coordinating evidence-based research.

This package conforms to Agent Plugins v1.0.0:

- `plugin.json` is the portable manifest.
- `skills/` contains portable Agent Skills.
- `mcp.json` is the optional MCP configuration and currently declares no bundled servers.

The core standard does not define portable agent definitions, commands, or
hooks. Those remain client-specific extensions and are intentionally excluded
from the portable package. Clients can orchestrate the packaged skills using
their own agent or workflow features.

This repository also includes client-neutral executable phase agents under
`agents/`. Hosts may load these definitions using their native agent mechanism;
the definitions do not require a particular vendor, runtime, command format,
MCP server, or credential layout.

The included `opencode.json` is an optional OpenCode adapter. It registers the
portable skills and loads the root instructions and agent definitions as
context; it does not configure MCP servers or credentials.

Jira and Confluence are the default logical service choices described by the
skills. Users may provide alternative ticketing, document, repository, or
identity services through their client-managed MCP configuration and persistent
user settings.

## Skills

- `setup-research`: clarify objectives, service roles, conventions, and approvals
- `plan-research`: produce actionable Stories, Sub-tasks, dependencies, and outputs
- `initialize-research`: create or reuse external research structure
- `execute-research`: run an approved task-specific research skill
- `verify-research`: perform read-only quality and traceability checks
- `complete-research`: approval-gated card-based closure
- `agents/`: client-neutral orchestration and phase-agent definitions

See `docs/getting-started.md` for user instructions and how to run a dry-run.
See `docs/architecture.md` and `docs/demo-script.md` for the full workflow and
demonstration scenario.
