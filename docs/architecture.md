# Architecture

This repository is an Agent Plugins v1.0.0 package. The portable core is
deliberately limited to `plugin.json`, `skills/`, and optional `mcp.json`.
Agents, commands, hooks, permissions, and orchestration UX are client-specific
and must not be added as portable top-level components.

The repository also contains client-neutral agent definitions under `agents/`.
They are workflow artifacts, not an Agent Plugins schema component. A host maps
them to its own agent runtime and supplies delegation, permissions, persistence,
and approval UX. The definitions do not name or require a particular vendor.

## Logical services

The framework depends on logical roles rather than named products:

- `ticketing`: issues, assignments, links, comments, and workflow transitions
- `document_store`: pages, hierarchy, content updates, and page links
- `repository`: analysis files, sources, and deliverables
- `identity`: current user, permissions, and service capability discovery

Jira and Confluence are the default logical service choices described by the
skills. A client can supply a different service through its MCP configuration
when it satisfies the capability contract required by the workflow.

MCP placement is host-specific: research setup may configure an approved
server in the active research repository's client adapter or in host-level
configuration. The included OpenCode adapter enables the official Atlassian Rovo
MCP server as a non-secret default for Jira and Confluence. The portable
plugin's `mcp.json`, skills, and agents remain credential-free and must not
contain user-specific authentication profiles.

## Configuration precedence

Settings resolve in this order:

1. Explicit request for the current operation
2. Research manifest
3. Persisted user configuration
4. Framework defaults

The resolved setup must be displayed for approval before the first external
mutation. Tokens and credentials are never stored in the plugin, manifests,
pages, or Git. Persisted user settings belong to the host client or agent
runtime; the portable plugin stores no user-specific configuration.

## Lifecycle

1. Clarify objectives and constraints.
2. Resolve service adapters and conventions.
3. Produce a proposed plan and dependency graph.
4. Obtain approval.
5. Initialize issues, pages, links, and repository content idempotently through
   client-provided tools or MCP servers.
6. Execute independent tasks through the packaged skills.
7. Verify outputs and cross-links.
8. Request approval before completion or closure.

## Agent orchestration

The agent definitions map the lifecycle to these roles:

| Phase | Agent | Mutation policy |
| --- | --- | --- |
| Setup | `research-setup` | No external mutation |
| Plan | `research-planner` | No external mutation |
| Initialize | `research-initializer` | Approved, idempotent mutation |
| Execute | `research-executor` | Approved task artifacts only |
| Verify | `research-verifier` | Read-only |
| Complete | `research-completer` | Explicit closure approval |

`agents/research-orchestrator` delegates setup and planning serially, gates
initialization on both approvals, then schedules ready independent Sub-tasks in
parallel from `depends_on`. Synthesis tasks wait for all declared dependencies.
Verification is a barrier before completion. A failed or ambiguous operation
remains blocked and is reported rather than being retried with guessed values.

Host permissions are defense in depth, not a substitute for the approval rules
in the skills. Host service tools must still enforce their own authorization and
audit behavior.

## Demo boundary

The first demo should use a client dry-run or mock adapter by default. A real
Jira/Confluence run can be shown as an optional approved path, but the demo
must make configuration resolution, client-provided MCP services, mutations,
and approval gates visible.
