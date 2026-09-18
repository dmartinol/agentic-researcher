---
name: plan-research
description: Use after research setup is approved to decompose a research requirement into actionable Stories and Sub-tasks with skills, dependencies, descriptions, and expected document outputs.
---

# Plan Research

Create a proposed plan before making external changes. The plan must be
portable and expressed in logical service roles.

## Plan contents

For every Story and Sub-task define:

- Jira summary and non-empty description
- Goal, acceptance criteria, and evidence requirements
- Assigned execution skill
- Dependencies and parallelization boundaries
- Expected Confluence page and parent page
- Expected repository paths, if applicable
- Completion verification and approval gate

Use the configured hierarchy and component conventions. Do not invent a Jira
project, Confluence space, or repository root. Resolve missing identifiers with
the user.

## Quality rules

- Keep research findings separate from project-management instructions.
- Exclude timelines, budgets, staffing, and implementation roadmaps unless the
  user explicitly changes the research scope.
- Prefer independent tasks with explicit synthesis dependencies.
- Make setup idempotent: existing Jira items and pages must be reused after
  verifying their identity and parentage.

Present the complete plan and wait for approval before invoking
`initialize-research`.
