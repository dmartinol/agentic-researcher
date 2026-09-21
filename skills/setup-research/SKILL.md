---
name: setup-research
description: Use when starting a new research initiative and the user needs objectives, scope, service roles, conventions, approvals, and persistent settings clarified before planning.
---

# Set Up Research

Turn an initial research requirement into a complete, approved research
configuration. Use the host's structured question-and-answer tool when
available. Do not create tickets, pages, files, or MCP connections during
setup, and do not proceed to planning until the user approves the configuration.

## Interactive intake

Run the intake as a conversation, not as a single questionnaire. Ask one
decision at a time using a structured question with concise options when the
choice is bounded. Ask a free-form question when the answer cannot be safely
represented by options. After each answer:

1. Record the answer in the draft configuration.
2. Use it to choose the next relevant question.
3. Skip questions that are no longer applicable.
4. Explain any consequential default before applying it.

Do not ask the user to repeat information already supplied in the request. If a
single answer resolves multiple fields, record all of them and continue with
the next missing decision. If the user says “I don't know,” offer a safe
default, explain its impact, and mark it as an assumption requiring approval.

Use this order unless earlier answers require a different branch:

1. Objective: What decision or understanding should this research produce?
2. Audience: Who will use the result and at what level of technical detail?
3. Scope: Which questions, subjects, markets, versions, or time range are in scope?
4. Exclusions: What must not be investigated or concluded?
5. Evidence: Which sources are acceptable, how current must they be, and how
   should conflicts be handled?
6. Outputs: Which findings, comparisons, recommendations, or artifacts are
   required?
7. Execution mode: dry-run/mock, read-only external services, or approved
   mutations?
8. Systems: Which external systems are needed and what role does each serve?
9. Conventions: How should work items, pages, labels, assignments, and files be
   named and organized?
10. Approvals: Which gates are required before planning, mutation, execution,
    and closure?

Ask follow-up questions conditionally. Examples:

- If the user requests recommendations, ask which decision criteria and
  constraints should govern them.
- If the scope includes multiple platforms or products, ask for the selection
  method or offer a bounded sample.
- If the user requests current information, ask for a recency threshold.
- If a repository output is requested, ask for the approved repository root and
  artifact format.
- If an external system is needed, run the systems-discovery flow below.
- If dry-run is selected, do not ask for production project, space, or page IDs
  unless the user wants realistic mock identifiers.

## Systems discovery

Help the user define the systems needed for the workflow instead of assuming
that MCP servers already exist. First ask which logical roles are needed:

- `ticketing`: issues, assignments, links, comments, and transitions
- `document_store`: pages, hierarchy, content, and page links
- `repository`: research artifacts, sources, and deliverables
- `identity`: current user, permissions, and capability discovery
- `source_search` or another additional role when the research requires a
  specialized system

For each selected role, ask individually:

1. Which host-provided service or MCP server should implement the role?
2. Is it already configured in the host environment?
3. Which capabilities are required for this research?
4. Which non-secret project, space, repository, root, or account identifier is
   needed?
5. Which client-managed authentication profile should the host use, if any?

If the service is not configured, explain the required capability contract and
ask whether the user wants to configure it outside this workflow. Do not edit
MCP configuration, install servers, open authorization flows, or test external
mutations during setup. The setup result may record a pending configuration
action, a server name, capability names, and an authentication profile
reference, but never credentials.

For every role, classify it as `ready`, `pending host configuration`, `not
needed`, or `mock/dry-run`. A research setup is incomplete if a required role
is unresolved. If the user chooses dry-run, provide mock adapters for required
mutation roles and state clearly that no external records will change.

## Configuration conventions

Use logical roles rather than vendor names. Jira and Confluence are defaults
only; replace them when the host supplies compatible services.

Confirm, when applicable:

- Ticket hierarchy, components, labels, assignment rules, and status conventions
- Document root, page hierarchy, layouts, work-item cards, reciprocal links, and
  closure comments
- Repository root, research-state directory, artifact naming, and shared-memory
  policy
- Evidence labels: `Verified`, `Reported`, `Not established`, and `Conflicting`
- Approval gates before planning, mutation, execution, and closure

Do not invent project keys, space keys, repository roots, users, capabilities,
or status transitions. Resolve them with the user or mark them as pending.

## Completeness check

Before presenting setup for approval, verify that the draft contains:

- A stable research ID and title
- Objective, audience, scope, exclusions, and decision context
- Evidence policy and source-quality expectations
- Expected outputs and repository needs
- Execution mode and mutation boundary
- Every required logical role with adapter status and capability requirements
- Non-secret identifiers or explicit pending configuration items
- Naming, hierarchy, link, evidence, and approval conventions
- Open assumptions and unresolved questions

If a required field is missing, ask the next individual question. Do not hand an
incomplete setup to planning. If no further question is needed, present the
complete redacted configuration, assumptions, pending system configuration, and
unresolved optional choices.

## Persistence and output

After approval, persist the configuration in the host's approved shared
research-state location, separate from conversation context and research
findings. The state must be reusable by later phases and other authorized
developers. At minimum, preserve the stable research ID, service role mappings,
capability names, non-secret identifiers, conventions, approval decisions, and
phase status. Do not overwrite existing research state without confirming the
research ID and ownership.

Never store tokens, passwords, private keys, authorization headers, or raw
secrets in the research configuration, repository, pages, or persistent memory.

Present the final configuration summary and an exact approval request. Require
explicit approval before handing the result to `plan-research`.
