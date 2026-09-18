# Getting Started

## What this plugin does

This plugin coordinates an evidence-based research workflow. It helps an agent
turn a research request into an approved plan, initialize linked work items and
documents, execute research tasks, verify the evidence and links, and request
explicit approval before closure.

The plugin does not itself provide Jira, Confluence, repository, identity, web
search, or delegation tools. The host client supplies those capabilities and
authentication. `mcp.json` is empty by default, so configure services in the
host client when an external run is required.

## Try the demonstration scenario

The demonstration scenario uses this research question:

> Which operational agent platforms are relevant to the product portfolio, and
> what integration hooks do they provide?

The scenario illustrates three tasks:

1. Define scope, selection criteria, evidence labels, and exclusions.
2. Assess the selected platforms after the scope task passes.
3. Synthesize common capabilities and integration hooks after assessment passes.

The scenario is documented in `docs/demo-script.md`; it is not an executable
workflow or bundled research result. The host agent should turn the request
into a proposed manifest and plan. Task-specific capabilities, such as platform
assessment, must be provided or mapped by the host.

## Run a new research workflow

Load this repository's skills and, where supported, the definitions in
`agents/`. Then give the host agent a request such as:

```text
Start a research initiative using the agentic-researcher workflow.
Objective: compare operational agent platforms and assess their integration
relevance to our product portfolio.
Use a dry-run or mock service adapter. Do not create or update external records.
First run setup and show me the redacted configuration and unresolved questions.
Stop for explicit approval after setup and after planning.
```

The expected phase order is:

`setup -> plan -> initialize -> execute -> verify -> complete`

The host should stop for approval before planning, external mutations, and
closure. Independent tasks may run in parallel; dependent tasks wait until
their prerequisites pass.

## Dry-run mode

Use the host client's dry-run mode or a mock adapter. A dry run should show the
resolved configuration, proposed work items, page hierarchy, links, delegation,
verification results, and approval gates without mutating Jira, Confluence, a
repository, or another external service.

The plugin has no portable dry-run switch. The adapter or host client must
implement the no-mutation behavior. A real service run is optional and requires
explicit mutation approval.

## External-service run

Before an external run, provide the host client with logical service roles:

- `ticketing`
- `document_store`
- `repository`
- `identity`

The agent must resolve and display the effective configuration, redact
authentication data, verify capabilities, and reuse existing records where
possible. Do not put tokens, passwords, private keys, or authorization headers
in this repository or in a research manifest.

## Further reading

- `skills/setup-research/SKILL.md`: required setup questions and approval
- `skills/plan-research/SKILL.md`: plan structure and dependency rules
- `docs/demo-script.md`: end-to-end demonstration checkpoints
- `docs/architecture.md`: service roles, lifecycle, and host boundary
