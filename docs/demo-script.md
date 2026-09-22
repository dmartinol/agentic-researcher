# Demo Script

This demo proves the product lifecycle rather than a specific research answer. Use `examples/demo-research/scenario.md` as the scenario contract.

## Preconditions

- Install `agentic-researcher` with the target host's normal installation mechanism; do not clone this repository as part of the researcher workflow.
- Authenticate configured providers through the host.
- Use disposable or explicitly approved external resources for mutation testing.

## Demo

### 1. Setup

Ask the installed researcher to execute the scenario.

Expected: clarify consequential configuration, resolve logical subsystems, and present the effective configuration before mutation.

### 2. Plan

Approve setup and request a plan.

Expected: provider-neutral Workstreams, Research Tasks, dependencies, acceptance criteria, evidence needs, and a Synthesis Task. No external resources are created yet.

### 3. Initialize

Approve initialization.

Expected: provider resources are created or reused, stable IDs/URLs recorded, links/hierarchy verified, and repeated initialization creates no duplicates.

### 4. Execute

Approve task execution.

Expected: retrieve relevant memory first; gather authoritative evidence; record canonical sources and atomic claims; actively seek contradictions to conclusion-critical claims; check freshness; preserve unresolved gaps.

Independent Research Tasks may execute in parallel where supported.

### 5. Resume

Start a fresh agent session against the same research project.

Expected: reconstruct current work from `RESEARCH.md`, `STATE.md`, and selective memory retrieval rather than prior conversation.

### 6. Synthesize

Run the dependent Synthesis Task.

Expected: conclusions trace to claims/sources; genuine conflicts and missing evidence remain visible.

### 7. Verify

Request verification.

Expected: read-only checks cover acceptance criteria, evidence provenance, contradiction/freshness checks, memory integrity, external identities/hierarchy/links, and provider invariants.

### 8. Complete

Approve completion explicitly.

Expected: only then are configured external work items transitioned/closed and final outputs linked; final state is read back and verified.

## Brownfield variant

Repeat against a pre-existing research project. Discover and reconcile existing manifests, state, memory, work items, and documents before mutation. Do not recreate resources because the current session did not create them.

## Release evidence

Capture host/version, installation method, provider configuration without secrets, greenfield/brownfield result, idempotency result, resume result, and deviations. Manual observations determine whether environment-dependent P3 TODO items can be marked complete.
