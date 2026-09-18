# Demo Script

## Scenario

Given a research requirement such as:

> Identify operational agent platforms, compare their integration hooks, and
> assess relevance to a product portfolio.

The researcher should:

1. Ask clarifying questions about scope, evidence, outputs, and exclusions.
2. Resolve Jira, Confluence, repository, and identity roles through the host
   client and its MCP configuration.
3. Propose a Story/Sub-task plan and page hierarchy.
4. Show the user the plan and wait for approval.
5. Generate Jira descriptions, page templates, Jira cards, and reciprocal links.
6. Show parallel task delegation and dependency-aware synthesis.
7. Verify evidence labels, hierarchy, and links before requesting closure approval.

Load the definitions from `agents/` using the host's native agent mechanism and
show `research-orchestrator` delegating to `research-setup`,
`research-planner`, `research-initializer`, `research-executor`,
`research-verifier`, and `research-completer`. Show independent ready Sub-tasks
running concurrently and the synthesis Sub-task held until its `depends_on`
items pass verification.

## Demonstration checkpoints

- Jira/Confluence logical defaults can be replaced by MCP service configuration.
- The resolved user configuration is shown without exposing credentials.
- Re-running initialization reuses existing issues and pages.
- A missing description or reciprocal link is reported and repaired.
- Closure is blocked until the user approves it.

The demo should also make clear that Agent Plugins v1 provides portable skills
and MCP configuration only. The files under `agents/` are client-neutral
workflow definitions; the host client still supplies agent execution, MCP
services, authentication, and persistent user-memory behavior.
