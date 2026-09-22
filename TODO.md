# TODO

This backlog follows the architecture contract in `AGENTS.md`. P0 establishes the contract and documentation; later phases change runtime behavior.

## P0 - Architecture contract

- [x] Define the installable product and standards boundary.
- [x] Define `agents/` as the deliberate IDE-neutral, non-standard agent extension.
- [x] Define four user-facing lifecycle phases while retaining specialized internal agents.
- [x] Define logical subsystems and provider-specialization boundaries.
- [x] Add `templates/RESEARCH.md`.
- [x] Add `templates/STATE.md`.
- [x] Move the research-memory model to `docs/research-memory.md`.
- [x] Define greenfield versus existing/brownfield research behavior.
- [x] Validate the P0 documentation as a coherent package contract.

## P1 - Provider separation and integrations

Refactor existing lifecycle skills so generic behavior uses logical subsystem terminology and provider details are composed separately.

### Capability contracts

- [x] Define ticketing capabilities.
- [x] Define document-store capabilities.
- [x] Define repository capabilities.
- [x] Define identity/capability-discovery behavior.
- [x] Refactor lifecycle skills to use logical subsystem terminology.
- [x] Declare the default Atlassian integration in portable `mcp.json`.
- [x] Remove the obsolete `opencode.json` adapter.

### Jira specialization

- [x] Add `jira-research` provider specialization.

Provide opinionated defaults and ask the researcher to confirm or override them.

- Hierarchy: Initiative / Epic / Story / Sub-task.
- Decide component policy.
- Decide labeling policy.
- Link each research work item to its document.
- Require meaningful descriptions.
- Verify issue type, parent, assignee, metadata, status, and links after mutation.

### Confluence specialization

- [x] Add `confluence-research` provider specialization.

Provide opinionated defaults and ask the researcher to confirm or override them.

- Default to one page per Jira work item.
- Align page title with ticket summary without requiring the Jira ID.
- Mirror useful work hierarchy with sub-pages.
- Put the Jira link near the page header using card presentation where supported.
- Add reciprocal Jira remote links to exact page URLs.
- Give container pages useful initial hierarchy/navigation content.
- Add a short Goal/Purpose section summarizing the work item.
- Record author/date where useful.
- Preserve existing content; never replace it with a skeleton.
- Allow setup/initialization to create approved template pages idempotently.
- Define optional default visual markers:
  - 🧭 Initiative
  - 🎯 Epic
  - 📖 Story
  - ☑️ Sub-task without research outcomes
  - 🔬 Sub-task with research outcomes
  - 🧩 Sub-task with synthesized/intermediate outcomes
  - 🏁 Sub-task with research deliverables

## P2 - Research quality and memory

- [x] Turn the memory model into an executable portable research capability.
- [x] Define canonical claim/source/episode formats.
- [x] Strengthen source discovery and source-quality guidance.
- [x] Define evidence acquisition and claim extraction behavior.
- [x] Require contradiction search for conclusion-critical claims.
- [x] Define freshness/revalidation behavior.
- [x] Strengthen synthesis across dependent research tasks.
- [x] Define selective retrieval from research memory.
- [x] Keep SQLite/vector indexes optional and derived.
- [x] Ensure research can execute competently without a topic-specific skill.

## P3 - Product integration, validation, and demo

- [x] Add greenfield and existing/brownfield lifecycle fixtures and expected invariants.
- [x] Add package/architecture validation for manifests, skills, agents, templates, provider separation, and secret hygiene.
- [x] Validate skill/agent frontmatter and JSON manifests in CI.
- [x] Document client-neutral approval/idempotency expectations and a reproducible dry-run/demo scenario.
- [ ] Test zero-clone installation on target hosts.
- [x] Document installation as a host-specific mechanism without making it an architecture requirement.
- [x] Update the demo flow to show install -> setup -> plan -> initialize -> execute -> resume -> synthesize -> verify -> explicit completion.
- [ ] Verify greenfield and brownfield behavior end to end on a real host.
- [ ] Verify Jira/Confluence default-provider behavior end to end.
