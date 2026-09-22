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
- [ ] Validate the P0 documentation as a coherent package contract.

## P1 - Provider separation and integrations

Refactor existing lifecycle skills so generic behavior uses logical subsystem terminology and provider details are composed separately.

### Capability contracts

- Define ticketing capabilities.
- Define document-store capabilities.
- Define repository capabilities.
- Define identity/capability-discovery behavior.
- Resolve the relationship between portable `mcp.json` and current host-specific MCP configuration.
- Revisit/remove `opencode.json` once portable/default integration behavior is implemented.

### Jira specialization

Provide opinionated defaults and ask the researcher to confirm or override them.

- Hierarchy: Initiative / Epic / Story / Sub-task.
- Decide component policy.
- Decide labeling policy.
- Link each research work item to its document.
- Require meaningful descriptions.
- Verify issue type, parent, assignee, metadata, status, and links after mutation.

### Confluence specialization

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

- Turn the memory model into an executable portable research capability.
- Define canonical claim/source/episode formats.
- Strengthen source discovery and source-quality guidance.
- Define evidence acquisition and claim extraction behavior.
- Require contradiction search for conclusion-critical claims.
- Define freshness/revalidation behavior.
- Strengthen synthesis across dependent research tasks.
- Define selective retrieval from research memory.
- Keep SQLite/vector indexes optional and derived.
- Ensure research can execute competently without a topic-specific skill.

## P3 - Product integration, validation, and demo

- Implement and test greenfield project initialization.
- Implement and test existing/brownfield discovery and reconciliation.
- Add package validation against Agent Plugins and Agent Skills schemas.
- Validate skill frontmatter and JSON manifests.
- Add client-neutral dry-run coverage for approvals and idempotency.
- Test zero-clone installation on target hosts.
- Document supported installation mechanisms without making them architecture requirements.
- Update the demo flow to show install -> setup -> plan -> execute -> verify -> explicit completion.
- Verify Jira/Confluence default-provider behavior end to end.
