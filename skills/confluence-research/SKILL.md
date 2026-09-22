---
name: confluence-research
description: Compose when Confluence implements the document_store subsystem to apply Confluence-specific page hierarchy, layout, Jira linking, preservation, and verification conventions.
---

# Confluence Research Provider

Apply these conventions only when the approved `document_store` provider is Confluence.

## Setup and planning

Propose defaults and let the researcher confirm or override them:

- one research page per external work item where useful;
- page title aligned with the work-item summary, without requiring the Jira key;
- page hierarchy reflecting useful research/work hierarchy;
- a short Goal/Purpose section derived from the approved task description;
- author/date metadata where useful;
- optional visual markers:
  - 🧭 Initiative
  - 🎯 Epic
  - 📖 Story
  - ☑️ task without research outcomes
  - 🔬 task with research outcomes
  - 🧩 synthesis/intermediate outcomes
  - 🏁 research deliverable.

## Initialization

- Resolve the approved space/root before mutation.
- Discover/reuse existing pages before creation.
- Verify page ID, title, parent, and version before updating.
- Preserve existing meaningful content; never replace it with an empty/template skeleton.
- Put the associated Jira work-item link near the page header using card presentation when supported.
- Give container pages useful initial hierarchy/navigation content.
- Add/update Goal/Purpose without overwriting research findings.
- Return the exact page URL for reciprocal ticketing links.

## Execution

Append or update research outcomes in the intended content region while preserving the work-item reference, Goal/Purpose, existing findings, and unrelated content.

Use exact source references and the approved evidence labels.

## Verification

Verify applicable Confluence properties:

- page ID;
- title;
- parent;
- version/currentness;
- expected content;
- exact Jira work-item link/card;
- preservation of existing meaningful content.

## Completion

Keep the final page as the durable human-readable research output. Ensure its exact URL is used by the ticketing provider's closure reference.
