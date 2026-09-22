---
name: setup-research
description: Use when starting or adopting a research initiative and the user needs objectives, scope, subsystem roles, conventions, approvals, and persistent settings clarified before planning.
---

# Set Up Research

Turn an initial research requirement into a complete, approved research configuration. Do not create external work items, documents, repository artifacts, or connections during setup, and do not proceed to planning until the user approves the configuration.

Use `RESEARCH.md` as the stable configuration contract and `STATE.md` for current workflow state. For existing research, discover and reconcile those artifacts before proposing replacements.

## Interactive intake

Run intake as a conversation. Do not ask the user to repeat information already supplied. Resolve, where applicable:

1. objective and audience;
2. scope and exclusions;
3. evidence expectations and freshness;
4. expected outputs;
5. execution mode and mutation boundary;
6. required logical subsystems;
7. provider-specific conventions;
8. approval gates.

Explain consequential defaults before applying them. Mark unresolved assumptions explicitly.

## Subsystem discovery

Resolve logical roles before provider details:

- `ticketing`: work items, hierarchy, assignments, links, comments, transitions;
- `document_store`: durable documents, hierarchy, content, and links;
- `repository`: optional source or research-artifact repository;
- `identity`: current-user and capability discovery;
- additional source/search systems when required by the research.

For each required role:

1. select a provider;
2. discover whether the host exposes the required capabilities;
3. resolve non-secret identifiers such as project, space, repository, or root;
4. classify the role as `ready`, `pending host configuration`, `not needed`, or `mock/dry-run`.

Use the capability contracts in `docs/subsystem-capabilities.md`. Do not assume a particular MCP server, tool name, or host configuration format.

Apply the provider specialization selected in the approved research configuration when one is available. Provider defaults are configuration concerns and must not be hardcoded into this generic lifecycle skill.

Do not put user credentials or host-specific authentication profiles in the research project.

## Completeness check

Before approval verify that the draft contains:

- stable research title/ID where needed;
- objective, audience, scope, exclusions, and decision context;
- evidence policy and expected outputs;
- execution mode and mutation boundary;
- every required logical role, provider, capability status, and non-secret identifier;
- applicable provider conventions;
- approval gates;
- open assumptions and unresolved questions.

A required unresolved role blocks initialization.

## Persistence and output

After approval, persist stable configuration in `RESEARCH.md` and current phase/restart information in `STATE.md`. Preserve existing research state when adopting an existing project.

Never store tokens, passwords, private keys, authorization headers, or raw secrets.

Present the effective configuration and request explicit approval before handing the result to `plan-research`.
