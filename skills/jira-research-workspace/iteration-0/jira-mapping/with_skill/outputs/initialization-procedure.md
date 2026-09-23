# Jira Initialization Procedure

## Overview

This procedure maps the provider-neutral research plan for "MCP Architecture Research" into Jira project RES, following the jira-research skill requirements.

## Prerequisites

1. Jira project RES is accessible
2. Current user has permission to view and update issues
3. Components exist: `architecture-analysis`, `synthesis`
4. Workflow supports "To Do" status

## Initialization Steps

### Step 1: Resolve Context

```
Action: Query Jira project RES
Verify:
  - Project exists and is accessible
  - Current user identity
  - Available issue types (Epic, Story)
  - Available components
  - Workflow states
```

### Step 2: Discover Existing Work Items

```
Action: Search for existing issues by key
Query: project = RES AND key in (RES-100, RES-101, RES-102, RES-103)

Expected results:
  - RES-100 exists (Epic)
  - RES-101 exists (Story)
  - RES-102 exists (Story)
  - RES-103 exists (Story)

If any issue does NOT exist:
  - Treat as blocking
  - Report missing issue
  - Do not proceed with creation without approval
```

### Step 3: Verify/Update RES-100 (Epic)

```
Action: Read RES-100 current state

Verify:
  - Issue type = Epic
  - Parent = None

Update (only if field is empty or approval given):
  - Description = Research topic, objective, scope, outputs
  - Component = architecture-analysis
  - Labels += [research, mcp-protocol]
  
Preserve:
  - Existing description content
  - Existing labels
  - Existing links
  - Current status

Do NOT:
  - Transition status
  - Remove existing content
```

### Step 4: Verify/Update RES-101 (Story)

```
Action: Read RES-101 current state

Verify:
  - Issue type = Story
  - Epic Link = RES-100

Update (only if field is empty or approval given):
  - Description = Goal, acceptance criteria, evidence requirements, output
  - Component = architecture-analysis
  - Labels += [research, direct-connection, mcp-protocol]

Preserve:
  - Existing description content
  - Existing labels
  - Existing links
  - Current status

Do NOT:
  - Transition status
  - Remove existing content
```

### Step 5: Verify/Update RES-102 (Story)

```
Action: Read RES-102 current state

Verify:
  - Issue type = Story
  - Epic Link = RES-100

Update (only if field is empty or approval given):
  - Description = Goal, acceptance criteria, evidence requirements, output
  - Component = architecture-analysis
  - Labels += [research, gateway-pattern, mcp-protocol]

Preserve:
  - Existing description content
  - Existing labels
  - Existing links
  - Current status

Do NOT:
  - Transition status
  - Remove existing content
```

### Step 6: Verify/Update RES-103 (Story)

```
Action: Read RES-103 current state

Verify:
  - Issue type = Story
  - Epic Link = RES-100

Update (only if field is empty or approval given):
  - Description = Goal, acceptance criteria, dependencies, evidence requirements, output
  - Component = synthesis
  - Labels += [research, comparison, mcp-protocol]

Preserve:
  - Existing description content
  - Existing labels
  - Existing links
  - Current status

Do NOT:
  - Transition status
  - Remove existing content
```

### Step 7: Add Reciprocal Confluence Links

```
When Confluence pages exist:

For RES-100:
  - Check if Confluence root page "MCP Architecture Analysis" exists
  - If exists, add Jira link using card presentation
  - Add to page header per research conventions

For RES-101:
  - Check if Confluence page for direct connection research exists
  - If exists, add Jira link using card presentation

For RES-102:
  - Check if Confluence page for gateway research exists
  - If exists, add Jira link using card presentation

For RES-103:
  - Check if Confluence page for synthesis exists
  - If exists, add Jira link using card presentation

Note: Do NOT add Confluence links to Jira during this phase
      Confluence links in Jira will be added by confluence-research skill
```

### Step 8: Post-Mutation Verification

For each work item, read back and verify:

**RES-100:**
- [ ] Key = RES-100
- [ ] Type = Epic
- [ ] Parent = None
- [ ] Description is non-empty
- [ ] Component = architecture-analysis
- [ ] Labels include [research, mcp-protocol]
- [ ] Status = To Do (or existing status if not changed)

**RES-101:**
- [ ] Key = RES-101
- [ ] Type = Story
- [ ] Epic Link = RES-100
- [ ] Description is non-empty
- [ ] Component = architecture-analysis
- [ ] Labels include [research, direct-connection, mcp-protocol]
- [ ] Status = To Do (or existing status if not changed)

**RES-102:**
- [ ] Key = RES-102
- [ ] Type = Story
- [ ] Epic Link = RES-100
- [ ] Description is non-empty
- [ ] Component = architecture-analysis
- [ ] Labels include [research, gateway-pattern, mcp-protocol]
- [ ] Status = To Do (or existing status if not changed)

**RES-103:**
- [ ] Key = RES-103
- [ ] Type = Story
- [ ] Epic Link = RES-100
- [ ] Description is non-empty
- [ ] Component = synthesis
- [ ] Labels include [research, comparison, mcp-protocol]
- [ ] Status = To Do (or existing status if not changed)

### Step 9: Report Ambiguities

If any of the following occur, report as blocking:
- Issue exists but wrong type
- Epic link points to wrong parent
- Multiple issues match search criteria
- Component or label cannot be set
- Any verification step fails

Do NOT:
- Guess which issue to update
- Silently replace content
- Force status transitions
- Proceed with partial success

## Rollback Strategy

If initialization fails or verification identifies issues:

1. Document current state of all issues
2. Report failures and ambiguities
3. Do not attempt automatic rollback
4. Request approval for remediation
5. Preserve all existing Jira content

## Success Criteria

Initialization is complete when:
- All four work items (RES-100, RES-101, RES-102, RES-103) are verified
- All hierarchy relationships are correct
- All descriptions are meaningful and non-empty
- All components and labels are set
- All existing content is preserved
- No status transitions occurred during initialization
- All verification checks pass
- State is documented for execution phase
