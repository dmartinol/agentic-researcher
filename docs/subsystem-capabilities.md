# Logical Subsystem Capability Contracts

Lifecycle skills depend on logical capabilities, not tool or MCP method names. Hosts and provider skills map available integrations onto these contracts.

The contracts describe required semantics. They are not a new runtime API.

## ticketing

Read/discovery capabilities:

- identify or search for a work item by stable identity;
- read type/kind, parent, description, classification, assignee, status, links, and comments;
- discover valid workflow transitions.

Mutation capabilities, when approved:

- create a work item under an approved parent;
- update description/classification/assignment;
- create a link to another exact resource;
- add a comment/closure reference;
- transition using a discovered valid transition.

Required properties:

- return stable IDs and exact resource URLs;
- support read-after-write verification;
- distinguish not-found from ambiguous matches.

## document_store

Read/discovery capabilities:

- identify/search documents by stable identity and approved location;
- read title, parent, content/version metadata, and links.

Mutation capabilities, when approved:

- create a document under an approved parent;
- update content without destroying unrelated existing content;
- create supported links/cards to exact external resources.

Required properties:

- return stable IDs and exact resource URLs;
- support read-after-write verification;
- expose enough version/identity information to avoid accidental replacement.

## repository

Capabilities are optional and depend on configured purpose (`source`, `research-artifacts`, or `both`):

- discover repository/root identity;
- read approved files/artifacts;
- create/update approved research artifacts;
- preserve unrelated existing content;
- return stable paths/references.

Repository integration must not be required when the research does not need it.

## identity

Read-only capabilities:

- resolve the current authenticated user when required;
- expose provider/account/workspace identity needed to avoid acting in the wrong context;
- expose enough capability/permission information to identify unsupported required operations.

Identity discovery must not be treated as authorization to mutate.

## Provider mapping

Provider-specialized skills document how provider concepts satisfy these semantics. Tool names and MCP method names are host/integration details and must not leak into generic lifecycle skills.

If a required capability cannot be mapped reliably, classify that subsystem as `pending host configuration` and block the dependent mutation rather than guessing.
