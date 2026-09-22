# AGENTS.md

## Project Purpose

`agentic-researcher` is an installable, portable agentic research system for planning, executing, documenting, and verifying evidence-based research.

A human researcher provides a research topic, scope, and optional workflow configuration. The system coordinates the research lifecycle using configurable external subsystems for work tracking, documentation, and optionally source or research repositories.

The product should support a researcher in:

- clarifying the research objective, scope, exclusions, evidence expectations, and expected outputs;
- creating an actionable research plan;
- initializing the configured research workspace and external systems;
- executing independent research tasks, including parallel work where supported by the host;
- recording evidence-backed findings with provenance;
- synthesizing dependent findings;
- preserving research state across context windows and agent sessions;
- verifying evidence, external artifacts, links, hierarchy, and metadata;
- completing and closing research only after explicit user approval.

The default subsystem profile uses Jira for ticketing and Confluence for research documents. These defaults may provide richer provider-specific behavior, but the core research lifecycle must remain independent of those products.

A Git repository is optional.

## Product and Distribution Model

`agentic-researcher` is a product to be installed by a researcher, not a repository that the researcher must clone in order to use it.

Supported hosts should be able to install the package through an appropriate plugin, skill, package, or agent installation mechanism. Installation mechanics are host-specific and are not part of the research workflow contract.

The research project created by the installed agent is separate from the `agentic-researcher` development repository.

## Standards Boundary

The portable core follows the Agent Plugins v1 standard and the Agent Skills specification.

Standard components are:

- `plugin.json`: Agent Plugin manifest.
- `skills/<skill-name>/SKILL.md`: portable Agent Skills.
- `mcp.json`: optional MCP server declarations.

Agent Plugins v1 does not standardize agent definitions. This project deliberately provides `agents/` as a non-standard but IDE-neutral extension following the Markdown agent convention used by Claude plugins and compatible agent hosts.

Agent definitions MUST avoid host-specific APIs, delegation syntax, tool names, permission models, and runtime assumptions wherever practical.

Agents provide role specialization, lifecycle orchestration, delegation, and coordination between portable skills. All essential research behavior MUST remain available through portable Agent Skills. No critical research rule may exist only in an agent definition.

A host supporting the `agents/` convention may expose the specialized multi-agent workflow. A host supporting Agent Skills but not `agents/` should still be able to execute the complete research lifecycle using portable skills.

Do not require researchers to create or maintain IDE-specific agent adapters. Host-specific compatibility files may be added when necessary for a target host, but they are optional, must not contain canonical research behavior, and must not be required configuration for a research project.

## Architecture Layers

Keep responsibilities separated into four layers:

```text
Agents
  |
  | orchestrate roles and lifecycle
  v
Skills
  |
  | implement research operations
  v
Logical subsystem capabilities
  |
  | provide abstract external operations
  v
Providers / MCP servers
```

### Agents

`agents/` contains canonical role and orchestration definitions:

- `research-orchestrator`
- `research-setup`
- `research-planner`
- `research-initializer`
- `research-executor`
- `research-verifier`
- `research-completer`

Agents should remain thin. Detailed reusable workflow behavior belongs in skills.

### Skills

Lifecycle skills currently include:

- `setup-research`
- `plan-research`
- `initialize-research`
- `execute-research`
- `verify-research`
- `complete-research`

Cross-cutting portable research capabilities include:

- `research-evidence`: evidence discovery/evaluation, atomic claims, contradiction search, and freshness;
- `manage-research-memory`: durable claims, sources, episodes, relationships, and selective retrieval;
- `research-synthesis`: traceable synthesis across evidence and dependent tasks.

Provider-specific conventions remain separate specializations.

### Logical Subsystems

Core workflows operate against logical subsystem roles rather than hardcoded products:

- `ticketing`: research planning and work tracking;
- `document_store`: durable human-readable research outputs;
- `repository`: optional source-code or research-artifact repository;
- `identity`: current-user and capability discovery.

### Provider Specializations

The default provider profile is:

```text
ticketing      -> Jira
document_store -> Confluence
repository     -> optional Git
```

Provider-specific behavior should be implemented through provider-specialized skills and MCP capabilities rather than embedded throughout generic research skills.

Jira and Confluence are intentionally opinionated first-class defaults. Generic workflows define research semantics; provider-specific skills define how those semantics are realized by a service.

Do not invent skill inheritance or override semantics. Compose generic and provider-specific skills.

## Research Lifecycle

Expose the research lifecycle to users as four conceptual phases:

```text
SETUP -> PLAN -> EXECUTE -> COMPLETE / VERIFY
```

The internal implementation may use more specialized agents and skills:

```text
SETUP
  -> research-setup

PLAN
  -> research-planner
  -> research-initializer

EXECUTE
  -> research-executor x N

COMPLETE / VERIFY
  -> research-verifier
  -> research-completer
```

Initialization and verification remain explicit internal operations even though they are grouped into the simpler user-facing lifecycle. The orchestrator owns lifecycle transitions. Skills own detailed operations.

## Research Project Model

Setup creates or adopts a local research project. A research project MUST be durable, shareable where desired, resumable across agent sessions, and understandable without conversation history.

Primary local artifacts are:

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

Derived indexes or caches may additionally exist under a Git-ignored location such as `research/.cache/`.

### RESEARCH.md

`RESEARCH.md` is the stable research manifest. It defines what the research is and how it is configured.

It should capture, where applicable:

- research topic and objective;
- scope and exclusions;
- expected outputs;
- evidence rules;
- configured logical subsystems and providers;
- provider-specific configuration;
- research conventions;
- approval policy;
- relevant external identifiers.

Do not use `RESEARCH.md` for volatile execution progress or accumulated research findings.

### STATE.md

`STATE.md` is the concise working state used to resume research. It should capture the current lifecycle phase and objective, work status, immediately relevant established findings, unresolved questions, contradictions requiring investigation, and next actions.

Keep `STATE.md` concise. It is working memory, not the authoritative evidence store.

### Research Memory

Persistent research artifacts are the durable memory of the research. Do not rely on conversation history as durable knowledge.

Important findings should be represented as claims with provenance to their supporting sources. The authoritative research memory should be human-readable and suitable for sharing and version control where appropriate.

Binary databases, SQLite indexes, embeddings, or vector databases may be used as derived retrieval layers, but they must not be the only authoritative representation of research knowledge.

The detailed memory model is defined in `docs/research-memory.md`; canonical object templates live under `templates/memory/`.

Do not use numeric confidence scores for claims. Express evidence state with the canonical labels, provenance, scope qualifications, conflicts, freshness, and unresolved gaps.

Core principle:

> Do not remember the conversation. Remember the research.

## Evidence Model

Keep important findings separate from planning and workflow metadata.

Use these evidence labels at claim level:

- `Verified`: supported by direct authoritative evidence.
- `Reported`: stated by a vendor or credible source but not independently verified.
- `Not established`: reviewed sources do not establish the claim; do not infer absence.
- `Conflicting`: credible sources disagree and the disagreement is preserved.

Research conclusions must be traceable to evidence and sources. Where relevant, preserve:

```text
CLAIM
  -> supported by EVIDENCE
  -> obtained from SOURCE
  -> observed at TIME
```

Do not silently replace contradictory findings. Preserve disagreement and resolve or report it explicitly. Record sufficient source and observation metadata to support later revalidation.

## Greenfield and Existing Research

Setup must distinguish between creating a new research project and adopting an existing one.

### Greenfield

For a new research project, setup may:

- create `RESEARCH.md`;
- create `STATE.md`;
- initialize the research-memory structure;
- prepare the approved ticketing hierarchy;
- prepare the approved document hierarchy;
- initialize optional repository artifacts.

External mutations remain approval-gated.

### Existing / Brownfield

When research artifacts already exist:

- discover before creating;
- identify existing manifests, state, tickets, documents, and repository artifacts;
- reconcile identities and relationships;
- reuse existing resources where possible;
- report inconsistencies;
- ask before destructive repair or replacement.

Never recreate resources merely because the current agent session did not create them.

## Workflow Safety and Mutation Rules

- Resolve and display the effective subsystem configuration before external mutations.
- Require explicit user approval before creating or updating external work items unless the approved research configuration explicitly authorizes the operation.
- Initialization must be idempotent.
- Discover and reuse existing resources rather than creating duplicates.
- After external mutations, verify the resulting resource rather than assuming the mutation succeeded as intended.
- Preserve existing research content. Never replace meaningful existing content with an initialization skeleton.
- Do not add timelines, budgets, staffing plans, or implementation roadmaps unless explicitly included in the approved research scope.
- Never close external work items without explicit user approval.
- Persistent configuration must not contain passwords, access tokens, private keys, authorization headers, or other secrets.
- Authentication remains the responsibility of the host or configured external integration.

## Default Jira and Confluence Profile

Jira and Confluence are the default providers and may implement richer conventions than the generic capability model.

Expected Jira/Confluence behavior includes:

- non-empty descriptions for research work items;
- configurable issue hierarchy and conventions;
- aligned ticket and document titles;
- hierarchical document organization corresponding to research work;
- links from research documents to their work items;
- reciprocal links from work items to their exact research documents;
- preservation of existing document content;
- post-mutation verification of hierarchy, metadata, links, and identity.

Detailed Jira and Confluence conventions belong in provider-specific skills and references rather than generic lifecycle instructions.

## Repository Role

A repository is optional.

When configured, distinguish between:

1. a repository that is a subject or source of the research; and
2. a repository used to persist research artifacts.

These roles may refer to the same repository but must not be assumed to do so. Git-tracked research memory is recommended when team sharing, review, history, or reproducibility is required. Do not require Git for workflows that do not need it.

## Collaboration

Research artifacts should be designed so humans and agents can inspect, diff, review, merge, validate, and resume work from them.

Prefer stable globally unique identifiers for independently created claims and sources when concurrent researchers or agents may contribute to the same research.

The research project, not the IDE conversation state, is the collaboration boundary.

## Change Guidelines

- Preserve the Agent Plugins root contract and closed `plugin.json` schema.
- Keep `mcp.json` credentials-free.
- Keep skill frontmatter limited to fields supported by the Agent Skills specification.
- Prefer portable skills, references, assets, and canonical agent instructions over client-specific behavior.
- Do not duplicate canonical research logic in host compatibility files.
- When changing the package contract, update `README.md`, `docs/architecture.md`, relevant templates, and relevant validation tests.
- Validate JSON and Agent Skill metadata after structural changes.

## Near-Term Development Direction

1. Establish `RESEARCH.md` and `STATE.md` templates.
2. Turn the research-memory design into a documented and executable capability.
3. Separate generic subsystem semantics from Jira/Confluence provider conventions.
4. Define logical capability contracts for ticketing, document-store, repository, and identity.
5. Resolve portable MCP configuration versus existing host-specific configuration.
6. Strengthen evidence acquisition, contradiction checking, and synthesis.
7. Define greenfield and existing-project discovery behavior.
8. Validate zero-clone installation on target agent hosts.
