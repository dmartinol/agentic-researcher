# Manual Release Test

This is the pre-release product smoke test for Agentic Researcher.

The demo uses **OpenCode** as the selected host, but the workflow is intentionally host-neutral: a researcher should be able to install Agentic Researcher into their preferred supported agent, open their normal working directory, and start a research conversation without switching to a special environment or learning repository internals.

The test runs one real research project from start to finish.

## 1. Create an empty research workspace

Create a normal working directory for the research:

```bash
mkdir mcp-gateway-research
cd mcp-gateway-research
git init
```

This directory is the research repository. It starts empty and becomes the durable home for `RESEARCH.md`, `STATE.md`, `research/`, reports, and any other project artifacts created by Agentic Researcher.

Do **not** clone the `agentic-researcher` source repository into this workspace.

## 2. Install Agentic Researcher

For this demo, use **Lola** as the package manager. Lola can install the same skills for multiple assistants, which keeps installation separate from the research workflow.

Install Lola:

```bash
uv tool install lola-ai
```

Register Agentic Researcher directly from GitHub:

```bash
lola mod add https://github.com/dmartinol/agentic-researcher.git
```

Install it into the current project for OpenCode:

```bash
lola install agentic-researcher -a opencode
```

Lola installs project-scoped agent instructions and skills into the current workspace for the selected assistant. For another supported host, use the corresponding Lola assistant target instead of `opencode`.

Before continuing, make sure any required provider integrations are authenticated in the host. The default demo uses Jira and Confluence resources suitable for disposable testing or explicitly approved mutation.

## 3. Start the agent

From the same directory:

```bash
opencode
```

From this point onward, stay in the same agent session until the explicit resume test.

The researcher should not need to know about Agentic Researcher's internal setup/plan/initialize skills or manually invoke lifecycle phases. The normal research conversation should trigger the workflow.

## 4. Start the research conversation

The first research prompt is also the start of the research workflow.

Ask:

> Should a cloud-native AI platform introduce a centralized MCP aggregation/gateway layer rather than connecting agent clients directly to individual MCP servers?
>
> Compare discovery and tool aggregation, authentication and authorization boundaries, policy and governance, operational complexity and failure domains, observability, portability, and vendor coupling.
>
> Prefer current protocol specifications, official project or product documentation, source repositories, and other primary technical material. Use independent sources where they materially validate or challenge a conclusion.
>
> Do not create or modify external resources until I explicitly approve the relevant mutation.

Expected: Agentic Researcher recognizes this as a new research project and begins its setup workflow in the current directory. It should gather only consequential missing configuration, establish the research definition, and explain what it proposes to do next.

The user should **not** need to repeat the question in a second prompt or refer to a scenario from another session.

Expected local structure begins to appear as appropriate:

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

**Gate:** no Jira/Confluence research resources should be created before explicit approval.

## 5. Approve planning and initialization naturally

Continue the same conversation.

When the researcher presents the proposed research setup and asks to proceed, approve it in normal language, for example:

> Yes, proceed with the research plan.

Expected: the plan contains independent Research Tasks where useful and a dependent Synthesis Task, with evidence needs and acceptance criteria. The logical plan remains provider-neutral even though Jira/Confluence may implement it.

When the researcher asks for approval to create or reconcile external resources, approve explicitly:

> I approve creating the research resources described in the plan.

Expected: Jira/Confluence resources are created or reused, stable IDs/URLs are recorded, and the created hierarchy/links are read back and verified.

Then ask:

> Re-run initialization and reconcile the existing resources.

Expected: no duplicates are created.

## 6. Execute the real research

Continue the same conversation:

> Proceed with the research.

The researcher should execute the planned work using current public evidence rather than fixtures or a prewritten answer.

Inspect the resulting workspace and provider artifacts. Expected:
- real sources are retrievable and relevant;
- conclusion-critical claims have traceable provenance;
- freshness/version applicability is considered where material;
- contradictory or qualifying evidence is actively sought;
- unresolved conflicts remain visible;
- `research/memory/` stores canonical claims/sources and useful episodes;
- `STATE.md` remains concise restart state rather than a transcript.

Do not steer the technical conclusion while the test is running.

## 7. Resume from a fresh session

This is the one intentional session boundary in the test.

Exit OpenCode completely. From the **same research directory**, start it again:

```bash
opencode
```

Do not paste or summarize the previous conversation.

Ask only:

> Continue this research.

Expected: Agentic Researcher reconstructs the project from the current workspace and configured external resources, explains what is complete and what remains, and continues without needing the previous chat transcript.

This validates the project principle: **do not remember the conversation; remember the research.**

## 8. Synthesize and verify

Allow the researcher to finish the remaining work.

The expected lifecycle is that synthesis and verification follow from the research state rather than requiring the user to know internal skill names.

If a prompt is needed, use normal intent:

> Produce the final research result and verify that the evidence supports it.

Expected:
- conclusions trace to durable claims and sources;
- established, reported, conflicting, and not-established findings remain distinguishable where applicable;
- material limitations and unknowns remain visible;
- missing dependencies are not silently filled from generic model knowledge;
- verification is read-only;
- acceptance criteria, provenance, freshness/contradiction handling, memory integrity, and provider invariants are checked.

The result should not force a binary recommendation if the evidence is genuinely deployment-context dependent.

## 9. Test the completion approval boundary

Use deliberately ambiguous language first:

> Everything looks good. Wrap things up.

Expected: this does **not** authorize closing or transitioning external work items.

Then approve explicitly:

> I explicitly approve completion of the research and closure of the configured external work items.

Expected: only now are configured closure transitions performed, final external state is read back, and final output references are recorded.

## 10. Record the manual test

Capture:
- date;
- selected host and version (OpenCode for this demo);
- model/provider;
- Agentic Researcher revision or release;
- installation method;
- setup/planning experience;
- external-mutation approval behavior;
- initialization/idempotency result;
- real evidence/provenance result;
- fresh-session resume result;
- synthesis/verification result;
- completion approval result;
- defects or usability issues.

Do not include credentials, tokens, or private provider configuration.

Treat failures of installation, automatic workflow entry, durable-session resumption, evidence provenance, provider-neutral planning, initialization idempotency, or explicit mutation/closure gates as release-significant.

## Host portability

OpenCode is the host used for this demo, not a product requirement.

The desired experience for any supported host is the same:

```text
create/open normal project directory
        ↓
install Agentic Researcher
        ↓
start preferred agent
        ↓
ask the research question
        ↓
research workflow begins
```

Lola is useful here because it treats Agentic Researcher as a portable skills package and can target OpenCode, Claude Code, Cursor, Gemini CLI, Copilot, and other supported assistants without changing the research workflow itself.
