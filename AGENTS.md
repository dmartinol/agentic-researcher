# AGENTS.md

## Project Purpose

`agentic-researcher` is a portable Agent Plugin for planning and coordinating
evidence-based research workflows. It is intended to support a demo video and
later presentation to a wider audience.

The framework should help a user:

- Clarify a research requirement.
- Define scope, evidence rules, outputs, and exclusions.
- Build an actionable Jira-style plan with Stories, Sub-tasks, dependencies,
  descriptions, acceptance criteria, and assigned skills.
- Initialize linked document pages and repository locations.
- Execute independent research tasks in parallel.
- Synthesize dependent outputs.
- Verify evidence, links, hierarchy, and metadata.
- Complete and close work only after explicit user approval.

## Standards Boundary

This repository follows the **Agent Plugins v1.0.0** standard:

- Specification: <https://agent-plugins.org/specification>
- Plugin manifest: `plugin.json`
- Portable skills: `skills/<skill-name>/SKILL.md`
- Optional MCP configuration: `mcp.json`

Do not add vendor-specific agent, command, hook, permission, orchestration UX,
or persistent-memory files. Agent Plugins v1 standardizes skills and MCP
servers only. The client-neutral workflow definitions in `agents/` may be
provided as host-adaptable artifacts, but must not assume a particular agent
runtime or vendor.

An explicitly requested host adapter such as `opencode.json` may be provided,
but it must only load the client-neutral artifacts and must not move vendor
assumptions into `skills/`, `agents/`, or `mcp.json`.

Avoid vendor lock-in everywhere, including lock-in to OpenCode. Use logical
roles, capability contracts, portable skills, and client-neutral workflow
artifacts; vendor-specific adapters must remain replaceable extensions.

## Current State

The repository currently contains:

- `plugin.json`: valid Agent Plugins manifest.
- `mcp.json`: valid empty MCP configuration; no bundled MCP server is shipped.
- `skills/setup-research`: clarify objectives, service roles, conventions, and approvals.
- `skills/plan-research`: create the proposed research decomposition.
- `skills/initialize-research`: initialize Jira, document, and repository structure.
- `skills/execute-research`: execute an approved research Sub-task.
- `skills/verify-research`: verify evidence, hierarchy, metadata, and links.
- `skills/complete-research`: approval-gated completion and closure workflow.
- `agents/`: client-neutral orchestration and phase-agent definitions.
- `docs/architecture.md`: design boundaries and lifecycle.
- `docs/demo-script.md`: planned demo scenario and checkpoints.
- `docs/demo-script.md`: illustrative platform-landscape research scenario.

The skills are workflow specifications, not executable integrations. The host
agent/client supplies the tools, MCP connections, user memory, delegation, and
approval UI.

## Service Model

Use logical roles rather than hardcoded vendor names:

- `ticketing`: Jira by default; replaceable through MCP.
- `document_store`: Confluence by default; replaceable through MCP.
- `repository`: Git or another configured repository service.
- `identity`: current user and capability discovery.

Persistent user settings belong to the host client or agent runtime. The plugin
must not store user tokens, passwords, private keys, or authorization headers.
Configuration may contain service names, capability names, project/space/root
identifiers, page conventions, evidence labels, and references to client-managed
authentication profiles.

## Required Workflow Rules

- Resolve and display the effective service configuration before mutations.
- Require explicit approval before creating or updating external work items.
- Make initialization idempotent: verify identity and reuse existing Jira items
  and pages instead of creating duplicates.
- Require non-empty Jira descriptions for Stories and Sub-tasks.
- Keep page titles aligned with Jira summaries.
- Begin every Confluence page with a Jira link rendered as a block card.
- Add the reciprocal Jira remote link to the exact page URL.
- Verify issue type, parent, component, assignee, description, status, page ID,
  title, parent, version, card link, and reciprocal link after mutations.
- Preserve existing content; never overwrite a page with a skeleton.
- Keep research findings separate from planning and closure metadata.
- Use evidence labels at claim level:
  - `Verified`: supported by direct authoritative evidence.
  - `Reported`: stated by a vendor or credible source but not independently verified.
  - `Not established`: reviewed sources do not establish the claim; do not infer absence.
  - `Conflicting`: credible sources disagree and the disagreement is preserved.
- Do not add timelines, budgets, staffing, or implementation roadmaps unless
  explicitly included in the approved research scope.
- Never close a ticket without explicit user approval.

## Development Priorities

1. Add a portable research-manifest reference/template without making it a new
   Agent Plugins core component.
2. Add reusable skill references for Jira descriptions, Confluence page layouts,
   Jira block cards, reciprocal links, evidence labels, and closure comments.
3. Define MCP capability contracts in documentation for ticketing,
   document-store, repository, and identity roles.
4. Add a client-neutral dry-run example showing plan approval and idempotent
   initialization.
5. Add package validation against the canonical Agent Plugins and Agent Skills
   schemas.
6. Keep agent definitions client-neutral and adaptable across host runtimes.
7. Prepare the demo flow described in `docs/demo-script.md`.

## Change Guidelines

- Preserve the Agent Plugins root layout and closed `plugin.json` schema.
- Keep `mcp.json` credentials-free. Header values are package data, not a
  portable secret mechanism.
- Keep skill frontmatter limited to fields supported by the Agent Skills
  specification.
- Prefer portable instructions and references over client-specific commands.
- Update `README.md` and `docs/architecture.md` when the package contract changes.
- Validate JSON with `jq` and inspect every skill's `SKILL.md` frontmatter after
  changes.
