---
name: research-setup
description: Establishes approved research scope, services, conventions, and gates.
---

Follow `skills/setup-research/SKILL.md`. Turn the user's requirement into a
complete proposed research manifest without external mutations.

Use the host's question-and-answer tool when available. Ask one decision at a
time, adapt subsequent questions to prior answers, and do not ask the user to
repeat information already provided. Guide the user through required logical
service roles and any additional systems or MCP services, including their
capability requirements and non-secret identifiers. Do not edit MCP
configuration, install servers, or mutate external services during setup.

Do not present setup as complete while a required field or system role is
unresolved. Store only client-managed authentication profile references, never
credentials.

Return unresolved questions, a redacted effective configuration, proposed
manifest fields, and the exact approval being requested.
