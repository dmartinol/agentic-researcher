---
name: plan-research
description: Use after research setup is approved to decompose a requirement into provider-neutral workstreams, research tasks, dependencies, acceptance criteria, and expected outputs.
---

# Plan Research

Create a proposed research plan before external mutation. Express the plan using research semantics, not provider-specific issue types.

## Internal plan model

Use:

- **Workstream**: a coherent area of investigation.
- **Research Task**: independently executable research work.
- **Synthesis Task**: work that depends on findings from other tasks.

For each task define:

- summary and meaningful description;
- goal and acceptance criteria;
- evidence requirements;
- assigned execution skill or generic research execution;
- dependencies and parallelization boundaries;
- expected document output;
- expected repository artifacts, if configured;
- completion verification and approval gate.

Provider specializations map this model onto external systems. For example, Jira may map workstreams/tasks to its configured issue hierarchy; a different ticketing provider may use another representation.

Do not invent provider identifiers, hierarchy values, document roots, or repository paths. Resolve missing required values through the approved configuration.

## Quality rules

- Keep research findings separate from workflow metadata.
- Exclude timelines, budgets, staffing, and implementation roadmaps unless explicitly in scope.
- Prefer independent tasks with explicit synthesis dependencies.
- Plan for idempotent initialization: external resources must be discoverable and reusable by stable identity.
- Preserve the approved evidence policy.

Present the complete provider-neutral plan plus any provider mapping that will be applied, and wait for approval before `initialize-research`.
