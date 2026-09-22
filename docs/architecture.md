# Architecture

`agentic-researcher` separates portable research semantics from host integration and provider-specific behavior.

## Package boundary

The standards-based portable core consists of:

- `plugin.json`
- `skills/`
- optional `mcp.json`

The repository deliberately also contains IDE-neutral agent definitions under `agents/`. Agent Plugins v1 does not standardize agents, so these are a non-standard extension following the Markdown-agent convention used by Claude plugins and compatible hosts.

Essential research behavior must remain available through skills. Agents specialize roles, orchestrate phases, and delegate work; they must not become the only location of critical workflow rules.

Host-specific compatibility files are optional. Researchers must not be required to author or maintain host adapters.

## Architecture layers

```text
agents
  |
  v
portable skills
  |
  v
logical subsystem capabilities
  |
  v
provider-specific skills / MCP services
```

Generic research semantics belong above provider details.

## Logical subsystems

The framework uses these logical roles:

- `ticketing`: research planning and work tracking
- `document_store`: durable research documents and outputs
- `repository`: optional source or research-artifact repository
- `identity`: current-user and capability discovery

The default profile maps ticketing to Jira and document storage to Confluence. Git is an optional repository provider.

Jira and Confluence are first-class, opinionated defaults, but their conventions must not define the generic subsystem contract. Provider-specific behavior belongs in specialized skills/references and configured MCP capabilities.

The logical capability semantics are defined in `docs/subsystem-capabilities.md`. Lifecycle skills do not depend on provider tool names.

The default Jira/Confluence profile is composed through `skills/jira-research` and `skills/confluence-research`.

The portable `mcp.json` declares Atlassian's Streamable HTTP MCP endpoint as the default integration. Agent Plugins leaves OAuth/credential handling to the client, so the package contains no credentials or portable auth profile. Alternative providers may be supplied by a host when they satisfy the required capability semantics.

No host-specific adapter is required for the default architecture.

## Research project

The installed product operates on a research project distinct from this development repository.

A project has three complementary durable concepts:

```text
RESEARCH.md       what this research is
STATE.md          where the research is now
research/memory/  what the research knows
```

`RESEARCH.md` is the stable manifest: objective, scope, outputs, evidence policy, subsystem configuration, conventions, approvals, and stable external identifiers.

`STATE.md` is concise working/restart state: phase, current objective, work status, immediately relevant findings, unresolved questions, contradictions, and next actions.

`research/memory/` contains durable acquired knowledge such as claims, sources, and useful research episodes. See `docs/research-memory.md`.

Derived indexes may exist locally but are not authoritative.

## Configuration precedence

Settings resolve in this order:

1. explicit request for the current operation;
2. `RESEARCH.md`;
3. persisted host/user configuration;
4. framework defaults.

The resolved setup must be displayed for approval before the first external mutation.

## Lifecycle

The user-facing lifecycle has four conceptual phases:

```text
SETUP -> PLAN -> EXECUTE -> COMPLETE / VERIFY
```

The internal role decomposition remains more precise:

| User phase | Agent | Mutation policy |
| --- | --- | --- |
| Setup | `research-setup` | No external mutation |
| Plan | `research-planner` | No external mutation |
| Plan | `research-initializer` | Approved, idempotent mutation |
| Execute | `research-executor` | Approved task artifacts only |
| Complete / Verify | `research-verifier` | Read-only |
| Complete / Verify | `research-completer` | Explicit closure approval |

`research-orchestrator` owns lifecycle transitions and delegation. Initialization remains a distinct approval-gated operation. Verification remains a barrier before completion.

Parallel execution and synthesis dependencies are host capabilities coordinated by the orchestrator; the research semantics must remain usable on a host that only supports skills.

## Greenfield and existing projects

Setup classifies the project as new or existing.

For greenfield research, it may create local manifest/state/memory structure and, after approval, initialize external work/document structures.

For existing research, setup discovers and reconciles existing manifests, state, tickets, documents, repository artifacts, identities, and relationships before creating anything. Inconsistencies are reported rather than silently repaired.

Initialization must be idempotent in both modes.

## Evidence and memory

Important findings are represented as claims with provenance. The framework preserves contradictory credible evidence rather than silently overwriting it.

Claim-level evidence labels are:

- `Verified`
- `Reported`
- `Not established`
- `Conflicting`

Research memory is human-readable and durable. Conversation history is not authoritative memory.

## Provider defaults

The Jira/Confluence default profile may define richer conventions including ticket hierarchy, descriptions, document hierarchy, aligned titles, card/link presentation, reciprocal links, labels, and post-mutation verification.

These are provider conventions, not universal requirements of every ticketing or document system.

## Distribution

A researcher should be able to install `agentic-researcher` through a supported plugin, skill, package, or host-native installation mechanism without cloning this development repository.

Distribution mechanisms are host-specific implementation details. They must not alter the research workflow contract or require researchers to maintain host adapters.

## Demo boundary

The demo should make the distinction between product installation and research-project creation visible. It should demonstrate configuration resolution, approval gates, durable local state, provider-backed initialization, evidence-based execution, verification, and explicit completion approval.
