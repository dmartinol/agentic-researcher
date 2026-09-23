# Jira Hierarchy Mapping

## Provider-Neutral to Jira Hierarchy

### Conceptual Mapping

```
Provider-Neutral Model         Jira Hierarchy
========================       ================

Research Project               Epic (RES-100)
  │
  ├─ Workstream 1             (Not needed - single scope)
  │   │
  │   ├─ Research Task        Story (RES-101)
  │   │
  │   └─ Research Task        Story (RES-102)
  │
  └─ Synthesis                Story (RES-103)
```

### Actual Jira Structure

```
RES-100 [Epic] 🧭
"MCP Architecture Research"
Component: architecture-analysis
Labels: research, mcp-protocol
│
├─ RES-101 [Story] 🔬
│  "Research direct connection pattern"
│  Component: architecture-analysis
│  Labels: research, direct-connection, mcp-protocol
│  Dependencies: None
│
├─ RES-102 [Story] 🔬
│  "Research gateway/aggregation pattern"
│  Component: architecture-analysis
│  Labels: research, gateway-pattern, mcp-protocol
│  Dependencies: None
│
└─ RES-103 [Story] 🧩
   "Synthesis: Architecture comparison"
   Component: synthesis
   Labels: research, comparison, mcp-protocol
   Dependencies: RES-101, RES-102
```

## Hierarchy Levels Not Used

**Initiative Level:** Not needed
- Single Epic scope
- No multi-epic coordination required

**Sub-task Level:** Not needed
- Stories are atomic research units
- No decomposition into smaller tasks required
- Each story has clear acceptance criteria

## Parallel Execution Structure

```
Timeline View:

Phase 1: Independent Research (Parallel)
┌─────────────────────────────────────┐
│ RES-101                             │  Can execute in parallel
│ Direct Connection Pattern           │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ RES-102                             │  Can execute in parallel
│ Gateway/Aggregation Pattern         │
└─────────────────────────────────────┘

                 ↓ (Both must complete)

Phase 2: Synthesis (Sequential)
┌─────────────────────────────────────┐
│ RES-103                             │  Depends on RES-101, RES-102
│ Architecture Comparison             │
└─────────────────────────────────────┘
```

## Component Usage

### architecture-analysis
Applied to:
- RES-100 (Epic)
- RES-101 (Story)
- RES-102 (Story)

Purpose: Categorizes architectural research and analysis work

### synthesis
Applied to:
- RES-103 (Story)

Purpose: Categorizes synthesis and comparison work that depends on research findings

## Label Strategy

### Cross-Cutting Labels
- `research`: Applied to ALL work items (RES-100, RES-101, RES-102, RES-103)
- `mcp-protocol`: Applied to ALL work items (topic identifier)

### Work-Specific Labels
- `direct-connection`: RES-101 only
- `gateway-pattern`: RES-102 only
- `comparison`: RES-103 only

### Label Benefits
1. Filter by research type: `labels = research`
2. Filter by pattern: `labels = direct-connection` OR `labels = gateway-pattern`
3. Filter synthesis tasks: `labels = comparison`
4. Filter by topic: `labels = mcp-protocol`
5. Cross-project research queries: `labels in (research, mcp-protocol)`

## Status Flow

All work items follow the same status flow:

```
To Do → In Progress → In Review → Done
  ↑          ↑            ↑          ↑
  │          │            │          │
Initialize  Execute   Verify    Complete
```

### Status Transitions NOT Allowed During Initialization
- All items remain in current status (typically "To Do")
- No automatic transitions to "In Progress"
- No automatic closure to "Done"

### Status Transitions During Execution
- Execute skill moves "To Do" → "In Progress"
- Verification moves "In Progress" → "In Review"
- Approval moves "In Review" → "Done"

## Epic-Story Relationships

### RES-100 Epic Link Structure

```
Epic: RES-100
├─ Epic Link: (none - top level)
│
Child Stories:
├─ RES-101 [Epic Link → RES-100]
├─ RES-102 [Epic Link → RES-100]
└─ RES-103 [Epic Link → RES-100]
```

### Verification Points
1. RES-100 has no parent Epic
2. RES-101 Epic Link points to RES-100
3. RES-102 Epic Link points to RES-100
4. RES-103 Epic Link points to RES-100
5. No other issues link to RES-100 as Epic

## Dependency Graph

```
Jira Dependencies (via description):

RES-101 ─┐
         ├─→ RES-103
RES-102 ─┘

Note: Jira native "Blocks/Blocked by" links can be added
      but are not required for initialization
```

## Confluence Integration

Each Jira work item maps to a Confluence page:

```
Jira                  Confluence
====                  ==========

RES-100 ←──link──→   "MCP Architecture Analysis" (root)
  │                   │
  │                   ├─ "Direct Connection Pattern"
  ├─ RES-101 ←link──→ │   (child page)
  │                   │
  │                   ├─ "Gateway/Aggregation Pattern"
  ├─ RES-102 ←link──→ │   (child page)
  │                   │
  │                   └─ "Architecture Comparison"
  └─ RES-103 ←link──→     (child page)
```

### Reciprocal Linking Convention
- Jira → Confluence: Link in Jira issue (to be added)
- Confluence → Jira: Jira card in page header (per research conventions)
- Both links must point to exact URLs (not search results)

## Summary

- **Hierarchy depth:** 2 levels (Epic → Story)
- **Total work items:** 4 (1 Epic + 3 Stories)
- **Parallel capacity:** 2 stories can execute simultaneously (RES-101, RES-102)
- **Sequential gate:** 1 story depends on completion (RES-103)
- **Components:** 2 (architecture-analysis, synthesis)
- **Labels:** 5 unique (research, mcp-protocol, direct-connection, gateway-pattern, comparison)
- **External links:** 4 bidirectional Jira ↔ Confluence links
