# Initialization Preparation Plan

## Pre-Initialization Discovery

Before any external mutation, the following discovery and validation steps must be completed:

### 1. Identity and Context Resolution

**Objective:** Establish authenticated context and capabilities

**Steps:**
```
1. Query identity subsystem for current authenticated user
2. Resolve Jira project context from RESEARCH.md configuration
3. Verify user has required permissions in target Jira project
4. Validate project supports required issue types (Initiative, Epic, Story)
5. Discover available components and validate or create required ones
6. Confirm workspace/account identity to avoid wrong-context mutations
```

**Required Capabilities:**
- Read current user identity
- Read project configuration and permissions
- List available issue types, components, and workflows

**Blocking Conditions:**
- No authenticated user
- Insufficient permissions for work item creation
- Project does not support required hierarchy levels

---

### 2. Existing Resource Discovery

**Objective:** Identify any existing Jira issues that can be reused

**Steps:**
```
1. Search for Initiative by exact title or stable ID from RESEARCH.md
2. If Initiative exists:
   a. Verify issue type is Initiative
   b. Read current description, status, and metadata
   c. Preserve existing content for merge
3. Search for Epics by title or stable IDs
4. If Epics exist:
   a. Verify parent relationship to Initiative
   b. Read current state and metadata
   c. Preserve existing links and content
5. Search for Stories by title or stable IDs
6. If Stories exist:
   a. Verify parent relationships to Epics
   b. Read current state, dependencies, and links
   c. Preserve existing content
```

**Search Strategy:**
- Use stable identifiers from RESEARCH.md external resources if available
- Search by exact title match within project scope
- Treat ambiguous matches as blocking (require user disambiguation)
- Never silently create duplicates

**Reuse Policy:**
- Existing issues are preferred over new creation
- Existing content is preserved and enhanced, not replaced
- Existing links and relationships are maintained
- Inconsistencies are reported for user resolution

---

### 3. Dependency Validation

**Objective:** Ensure hierarchy and dependency graph is valid and acyclic

**Steps:**
```
1. Validate Initiative can be root (no required parent)
2. Validate Epics can have Initiative as parent
3. Validate Stories can have Epic as parent
4. Confirm Story 2.1 can reference Stories 1.1 and 1.2 as blockers
5. Verify no circular dependencies in planned structure
```

**Validation Rules:**
- All parent relationships must be valid per Jira project schema
- Dependency references form directed acyclic graph (DAG)
- No self-references or circular blocks

---

## Initialization Execution Plan

After discovery validation and user approval, execute these mutation steps:

### Phase 1: Create/Update Initiative

**Issue:** MCP Aggregation Architecture Research

**Actions:**
```
IF Initiative exists by stable ID:
  1. Read current version/state
  2. Merge new description with existing content
  3. Update components/labels if needed
  4. Preserve existing links and metadata
  5. Verify update succeeded
ELSE:
  1. Create new Initiative issue
  2. Set title: "MCP Aggregation Architecture Research"
  3. Set description (full text from mapping)
  4. Set component: Research / Architecture
  5. Set labels: mcp, architecture-research, cloud-native
  6. Set assignee: [current user]
  7. Record stable ID in RESEARCH.md external resources
  8. Verify creation succeeded
```

**Post-Mutation Verification:**
- Stable ID/key exists and is recorded
- Issue type is Initiative
- Description is meaningful and non-empty
- Component and labels are set correctly
- Assignee is correct
- Status is initial state (no transition performed)
- Resource URL is exact and accessible

---

### Phase 2: Create/Update Epics

#### Epic 1: Architecture Pattern Analysis

**Actions:**
```
IF Epic exists by stable ID:
  1. Verify parent link to Initiative
  2. Merge description content
  3. Update metadata if needed
  4. Preserve existing relationships
ELSE:
  1. Create Epic issue
  2. Set parent: Initiative from Phase 1
  3. Set title: "Architecture Pattern Analysis"
  4. Set description (full text from mapping)
  5. Set component: Research / Architecture
  6. Set labels: mcp, architecture-patterns
  7. Set assignee: [current user]
  8. Record stable ID
```

**Post-Mutation Verification:**
- Stable ID/key exists
- Issue type is Epic
- Parent link to Initiative verified
- Description is complete
- Metadata correct
- No status transition

---

#### Epic 2: Comparative Analysis and Synthesis

**Actions:**
```
IF Epic exists by stable ID:
  1. Verify parent link to Initiative
  2. Verify blocked-by link to Epic 1 (if supported)
  3. Merge description content
ELSE:
  1. Create Epic issue
  2. Set parent: Initiative from Phase 1
  3. Set title: "Comparative Analysis and Synthesis"
  4. Set description (full text from mapping)
  5. Set component: Research / Synthesis
  6. Set labels: mcp, synthesis, architecture-comparison
  7. Set assignee: [current user]
  8. Create blocked-by link to Epic 1 (if Epic-level dependencies supported)
  9. Record stable ID
```

**Post-Mutation Verification:**
- Stable ID/key exists
- Issue type is Epic
- Parent link verified
- Dependency link verified (if applicable)
- Description complete
- No status transition

---

### Phase 3: Create/Update Stories

#### Story 1.1: Direct Connection Pattern Analysis

**Actions:**
```
IF Story exists by stable ID:
  1. Verify parent link to Epic 1
  2. Merge description
  3. Update document link placeholder
ELSE:
  1. Create Story issue
  2. Set parent: Epic 1
  3. Set title: "Research: Direct Agent-to-MCP Connection Pattern"
  4. Set description (full text from mapping)
  5. Set component: Research
  6. Set labels: mcp, direct-connection, architecture-research
  7. Set assignee: [current user]
  8. Record stable ID
  9. Add comment: "Document link will be added after Confluence initialization"
```

**Post-Mutation Verification:**
- Stable ID/key exists
- Issue type is Story
- Parent link to Epic 1 verified
- Description complete with acceptance criteria
- All metadata correct
- No premature status transition

---

#### Story 1.2: Aggregation Gateway Pattern Analysis

**Actions:**
```
IF Story exists by stable ID:
  1. Verify parent link to Epic 1
  2. Merge description
ELSE:
  1. Create Story issue
  2. Set parent: Epic 1
  3. Set title: "Research: Centralized MCP Aggregation Gateway Pattern"
  4. Set description (full text from mapping)
  5. Set component: Research
  6. Set labels: mcp, aggregation-gateway, architecture-research
  7. Set assignee: [current user]
  8. Record stable ID
  9. Add comment: "Document link will be added after Confluence initialization"
```

**Post-Mutation Verification:**
- Stable ID/key exists
- Issue type is Story
- Parent link to Epic 1 verified
- Description complete
- Metadata correct
- No status transition

---

#### Story 2.1: Comparative Architecture Analysis

**Actions:**
```
IF Story exists by stable ID:
  1. Verify parent link to Epic 2
  2. Verify blocked-by links to Stories 1.1 and 1.2
  3. Merge description
ELSE:
  1. Create Story issue
  2. Set parent: Epic 2
  3. Set title: "Synthesis: MCP Architecture Pattern Comparison"
  4. Set description (full text from mapping)
  5. Set component: Research / Synthesis
  6. Set labels: mcp, synthesis, architecture-comparison
  7. Set assignee: [current user]
  8. Create blocked-by links to Stories 1.1 and 1.2
  9. Record stable ID
  10. Add comment: "This synthesis task depends on completion of research tasks 1.1 and 1.2"
```

**Post-Mutation Verification:**
- Stable ID/key exists
- Issue type is Story
- Parent link to Epic 2 verified
- Dependency links (blocked-by) verified
- Dependencies form valid DAG
- Description complete with synthesis requirements
- Metadata correct
- No status transition

---

### Phase 4: Add Reciprocal Document Links

**Note:** This phase executes AFTER Confluence documents are created during document store initialization.

**For Each Story:**
```
1. Wait for corresponding Confluence document creation
2. Retrieve exact document URL from document store
3. Add Jira link to exact document URL
4. If integration supports rich/card links, use card representation
5. Verify link created successfully
6. Add comment: "Research document: [exact URL]"
```

**Verification:**
- Every Story has reciprocal link to its Confluence document
- Links are exact URLs, not ambiguous references
- Link representation matches integration capabilities (card > bare URL)

---

## Post-Initialization Verification

After all mutations complete, perform comprehensive verification:

### Verification Checklist

**Initiative:**
- [ ] Stable ID recorded in RESEARCH.md external resources
- [ ] Issue type is Initiative
- [ ] Description is meaningful and complete
- [ ] Components and labels correct
- [ ] Assignee is current user
- [ ] Status is initial state (not transitioned)
- [ ] Resource URL is exact and accessible

**Epic 1 (Architecture Analysis):**
- [ ] Stable ID recorded
- [ ] Issue type is Epic
- [ ] Parent link to Initiative verified
- [ ] Description complete
- [ ] Metadata correct
- [ ] Contains 2 child Stories (1.1, 1.2)

**Epic 2 (Synthesis):**
- [ ] Stable ID recorded
- [ ] Issue type is Epic
- [ ] Parent link to Initiative verified
- [ ] Dependency on Epic 1 visible (if supported)
- [ ] Description complete
- [ ] Contains 1 child Story (2.1)

**Story 1.1:**
- [ ] Stable ID recorded
- [ ] Issue type is Story
- [ ] Parent is Epic 1
- [ ] Description includes goal, analysis areas, acceptance criteria
- [ ] No dependencies (can start independently)
- [ ] Document link added (after Confluence init)

**Story 1.2:**
- [ ] Stable ID recorded
- [ ] Issue type is Story
- [ ] Parent is Epic 1
- [ ] Description includes goal, analysis areas, acceptance criteria
- [ ] No dependencies (can start independently)
- [ ] Document link added (after Confluence init)

**Story 2.1:**
- [ ] Stable ID recorded
- [ ] Issue type is Story
- [ ] Parent is Epic 2
- [ ] Description includes synthesis requirements
- [ ] Blocked-by links to Stories 1.1 and 1.2
- [ ] Dependencies form valid DAG (no cycles)
- [ ] Document link added (after Confluence init)

**Hierarchy Integrity:**
- [ ] All parent-child relationships verified
- [ ] No orphaned issues
- [ ] No circular dependencies
- [ ] Dependency graph is acyclic

**Content Quality:**
- [ ] All descriptions are meaningful and non-empty
- [ ] All acceptance criteria are explicit
- [ ] Evidence requirements are clear
- [ ] Expected outputs are documented

**Metadata Consistency:**
- [ ] All components align with work item type
- [ ] Labels are appropriate and consistent
- [ ] Assignees are all current user
- [ ] No premature status transitions

---

## Idempotence Strategy

Initialization must be safely repeatable:

**Discovery Before Mutation:**
- Always search for existing issues by stable ID first
- Never assume absence; always verify
- Treat ambiguous matches as blocking errors

**Update vs. Create:**
- Prefer update for existing resources
- Merge new content with existing content
- Preserve existing links and metadata
- Never silently replace existing work

**Stable Identifiers:**
- Record all created issue keys in RESEARCH.md
- Use recorded IDs in subsequent discovery
- Verify ID/key matches before mutation

**Verification:**
- Read-after-write for all mutations
- Compare actual state to expected state
- Report discrepancies without silent repair

---

## Approval Gates

**Before Discovery:**
- Display resolved configuration (project, user, hierarchy mapping)
- Request approval to query external systems

**Before Mutation:**
- Display complete initialization plan
- Show existing vs. new resources
- Indicate all mutations that will be performed
- Request explicit approval

**After Mutation:**
- Display verification results
- Report any discrepancies or warnings
- Confirm initialization succeeded before proceeding to execution

---

## Error Handling

**Blocking Errors:**
- Authentication failure
- Insufficient permissions
- Project does not support required issue types
- Ambiguous issue matches
- Circular dependencies detected
- Parent relationship not allowed by schema
- Mutation verification failure

**Recoverable Warnings:**
- Optional components not available (use default)
- Rich link format not supported (use bare URL)
- Epic-level dependencies not supported (document in comments)

**Recovery Actions:**
- Report blocking errors to user
- Do not proceed with partial initialization
- Preserve all existing content
- Roll back only if safe and approved
- Record errors in STATE.md for diagnosis
