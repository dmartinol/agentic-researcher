# Agentic Researcher

Agentic Researcher provides an agent-orchestrated research workflow. These are runtime instructions for an installed Agentic Researcher package, not contributor instructions for developing the package.

## Entry point

When the user asks to start, conduct, continue, resume, verify, or complete research, the host primary agent MUST delegate lifecycle control to `research-orchestrator`.

Do not execute the research lifecycle directly from the host primary agent. Do not select lifecycle skills directly from the user's top-level research request when `research-orchestrator` is available.

`research-orchestrator` owns the lifecycle:

```text
setup -> plan -> initialize -> execute -> verify -> complete
```

If `RESEARCH.md` does not exist, treat the request as a greenfield research project and delegate to the orchestrator, which begins with `research-setup`. Missing project state is not permission to perform a standalone evidence review.

If `RESEARCH.md` and `STATE.md` exist, delegate to the orchestrator, which inspects durable state and resumes the appropriate lifecycle phase.

The orchestrator delegates phase work to the installed specialized research agents. Phase agents compose and apply the skills required for their operation.

The user should not need to know or name internal agents, skills, or lifecycle phases. A normal research request is sufficient to enter the workflow.

## Control boundaries

- Setup and planning do not authorize external mutations.
- Initialization may mutate configured external systems only after the required explicit approval.
- Execution follows the approved plan and configured mutation boundary.
- Verification is read-only.
- Completion and closure of external work require explicit closure approval.
- Never store credentials or secrets in research artifacts.

## Durable research state

Use `RESEARCH.md` for stable research configuration, `STATE.md` for concise restart state, and `research/memory/` for durable claims, sources, and useful episodes.

Do not rely on conversation history as authoritative research memory.

> Do not remember the conversation. Remember the research.
