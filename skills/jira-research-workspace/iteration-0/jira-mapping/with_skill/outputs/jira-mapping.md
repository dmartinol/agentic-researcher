# Jira Mapping for MCP Architecture Research

## Setup and Planning

Following the jira-research skill guidance, proposing the following defaults for researcher confirmation:

### Hierarchy Mapping

Based on the research plan structure and Jira project RES constraints:

**Provider-neutral → Jira mapping:**
- Research Project → Epic (RES-100)
- Workstream → Epic (when multiple workstreams exist) OR contained within parent Epic
- Research Task → Story
- Synthesis Task → Story

**Rationale:**
- The research plan has a single Epic (RES-100) already defined
- Three work items (RES-101, RES-102, RES-103) are all Stories
- No Sub-tasks are needed for this research plan structure
- No Initiative level required (single Epic scope)

### Component Policy

**Proposed:** Use components to categorize research areas

Recommended components:
- `architecture-analysis` - For architectural research tasks
- `synthesis` - For synthesis/comparison tasks
- `evidence` - For evidence collection tasks

**Application:**
- RES-100 (Epic): `architecture-analysis`
- RES-101 (Story): `architecture-analysis`
- RES-102 (Story): `architecture-analysis`
- RES-103 (Story): `synthesis`

### Label Policy

**Proposed:** Use labels to mark research lifecycle and characteristics

Recommended labels:
- `research` - Applied to all research work items
- `direct-connection` - Applied to RES-101
- `gateway-pattern` - Applied to RES-102
- `comparison` - Applied to RES-103
- `mcp-protocol` - Applied to all (cross-cutting topic)

### Assignment Convention

**Proposed:** 
- Assign to researcher or research team based on current user context
- Default: Unassigned until execution phase
- Will be resolved during initialization from current user context

### Target Workflow/Status Convention

**Proposed status lifecycle:**
- **To Do** - Initial state for all work items during initialization
- **In Progress** - When research task execution begins
- **In Review** - When findings are drafted and need verification
- **Done** - After synthesis is approved and research is complete

**Initialization behavior:**
- Do NOT transition issues during initialization
- Leave all items in "To Do" status
- Status transitions happen only during execution and completion phases

## Provider-Neutral to Jira Mapping

### Epic: RES-100 "MCP Architecture Research"

**Issue Type:** Epic

**Jira Fields:**
- **Key:** RES-100 (existing)
- **Summary:** MCP Architecture Research
- **Description:** 
  ```
  🧭 Research Initiative
  
  ## Topic
  Evaluation of centralized MCP aggregation/gateway architecture versus direct client-server connections for cloud-native AI platform.
  
  ## Objective
  Should we introduce a centralized MCP aggregation/gateway layer or connect agent clients directly to individual MCP servers?
  
  ## Scope
  
  ### Included
  - Discovery and tool aggregation patterns
  - Authentication and authorization boundaries
  - Policy and governance models
  - Operational complexity and failure domains
  - Observability approaches
  - Portability considerations
  - Vendor coupling implications
  
  ### Excluded
  - Implementation scheduling
  - Staffing and budget
  - Product procurement
  
  ## Expected Outputs
  Architecture comparison with evidence-backed findings, material conflicts/unknowns, and implications of each approach.
  ```

- **Component:** `architecture-analysis`
- **Labels:** `research`, `mcp-protocol`
- **Status:** To Do (during initialization)
- **Parent:** None
- **Confluence Link:** "MCP Architecture Analysis" root page in RESEARCH space

### Story: RES-101 "Research direct connection pattern"

**Issue Type:** Story

**Jira Fields:**
- **Key:** RES-101 (existing)
- **Summary:** Research direct connection pattern
- **Description:**
  ```
  🔬 Research Task
  
  ## Goal
  Understand the direct client-to-MCP-server connection pattern, including discovery mechanisms, authentication, tool aggregation, and operational characteristics.
  
  ## Acceptance Criteria
  - Document discovery patterns for direct connections
  - Identify authentication and authorization approaches
  - Analyze tool aggregation at client level
  - Assess operational complexity and failure modes
  - Document observability capabilities
  - Evaluate portability implications
  
  ## Evidence Requirements
  - Reference MCP protocol specifications
  - Use official MCP documentation
  - Include source repository examples
  - Cite independent validation sources
  
  ## Expected Output
  Confluence page documenting direct connection pattern with evidence-backed findings.
  
  ## Dependencies
  None (can execute independently)
  ```

- **Epic Link:** RES-100
- **Component:** `architecture-analysis`
- **Labels:** `research`, `direct-connection`, `mcp-protocol`
- **Status:** To Do (during initialization)
- **Confluence Link:** Child page under "MCP Architecture Analysis"

### Story: RES-102 "Research gateway/aggregation pattern"

**Issue Type:** Story

**Jira Fields:**
- **Key:** RES-102 (existing)
- **Summary:** Research gateway/aggregation pattern
- **Description:**
  ```
  🔬 Research Task
  
  ## Goal
  Understand centralized MCP gateway/aggregation architecture, including aggregation strategies, policy enforcement, operational characteristics, and vendor considerations.
  
  ## Acceptance Criteria
  - Document gateway aggregation patterns
  - Identify authentication and authorization boundaries
  - Analyze centralized policy and governance models
  - Assess operational complexity and failure domains
  - Document observability approaches
  - Evaluate vendor coupling implications
  
  ## Evidence Requirements
  - Reference MCP protocol specifications
  - Use official gateway documentation
  - Include architecture reference implementations
  - Cite independent validation sources
  
  ## Expected Output
  Confluence page documenting gateway/aggregation pattern with evidence-backed findings.
  
  ## Dependencies
  None (can execute independently)
  ```

- **Epic Link:** RES-100
- **Component:** `architecture-analysis`
- **Labels:** `research`, `gateway-pattern`, `mcp-protocol`
- **Status:** To Do (during initialization)
- **Confluence Link:** Child page under "MCP Architecture Analysis"

### Story: RES-103 "Synthesis: Architecture comparison"

**Issue Type:** Story

**Jira Fields:**
- **Key:** RES-103 (existing)
- **Summary:** Synthesis: Architecture comparison
- **Description:**
  ```
  🧩 Synthesis Task
  
  ## Goal
  Compare direct connection and gateway patterns across all evaluation dimensions, identify material tradeoffs, conflicts, unknowns, and provide evidence-backed implications.
  
  ## Acceptance Criteria
  - Compare discovery and tool aggregation approaches
  - Compare authentication and authorization models
  - Compare policy and governance capabilities
  - Compare operational complexity and failure domains
  - Compare observability approaches
  - Compare portability and vendor coupling
  - Document material conflicts and unknowns
  - Provide evidence-backed recommendations
  
  ## Evidence Requirements
  - Synthesize findings from RES-101 and RES-102
  - Preserve conflicting credible evidence
  - Do not infer absence from lack of evidence
  - Document evidence provenance
  
  ## Expected Output
  Confluence page with comprehensive architecture comparison and recommendation.
  
  ## Dependencies
  - RES-101 (Research direct connection pattern)
  - RES-102 (Research gateway/aggregation pattern)
  ```

- **Epic Link:** RES-100
- **Component:** `synthesis`
- **Labels:** `research`, `comparison`, `mcp-protocol`
- **Status:** To Do (during initialization)
- **Confluence Link:** Child page under "MCP Architecture Analysis"

## Initialization Checklist

Following jira-research skill initialization requirements:

### Pre-Mutation Checks
- [ ] Resolve project context: RES
- [ ] Resolve current user context for assignment
- [ ] Verify Jira project configuration supports proposed hierarchy
- [ ] Verify component values exist in project

### Issue Discovery/Reuse
- [ ] Check if RES-100 exists and matches expected Epic
- [ ] Check if RES-101 exists and matches expected Story
- [ ] Check if RES-102 exists and matches expected Story
- [ ] Check if RES-103 exists and matches expected Story

### Field Verification (per issue)
For each work item, verify after mutation:
- [ ] Issue key matches expected
- [ ] Issue type is correct (Epic or Story)
- [ ] Parent/Epic Link is correct
- [ ] Description is meaningful and non-empty
- [ ] Component is set correctly
- [ ] Labels are applied correctly
- [ ] Assignee matches convention (if set)
- [ ] Status is "To Do" (not transitioned during init)
- [ ] Confluence link is reciprocal and points to exact page URL

### Content Preservation
- [ ] Preserve any existing Jira descriptions
- [ ] Preserve existing Jira links
- [ ] Do not overwrite existing meaningful content
- [ ] Add new content only where fields are empty

### Reciprocal Linking
When Confluence pages exist:
- [ ] Add Jira link to RES-100 Epic from root Confluence page
- [ ] Add Jira link to RES-101 from corresponding Confluence page
- [ ] Add Jira link to RES-102 from corresponding Confluence page
- [ ] Add Jira link to RES-103 from corresponding Confluence page
- [ ] Verify links use card presentation format (not bare URLs)

## Verification Requirements

After initialization completes, verify the following for each work item:

**RES-100 (Epic):**
- Issue identity: RES-100
- Issue type: Epic
- Parent: None
- Description: Non-empty, contains research topic and objective
- Component: `architecture-analysis`
- Labels: `research`, `mcp-protocol`
- Status: To Do
- Confluence link: Points to "MCP Architecture Analysis" root page

**RES-101 (Story):**
- Issue identity: RES-101
- Issue type: Story
- Epic Link: RES-100
- Description: Non-empty, contains goal and acceptance criteria
- Component: `architecture-analysis`
- Labels: `research`, `direct-connection`, `mcp-protocol`
- Status: To Do
- Confluence link: Points to direct connection research page

**RES-102 (Story):**
- Issue identity: RES-102
- Issue type: Story
- Epic Link: RES-100
- Description: Non-empty, contains goal and acceptance criteria
- Component: `architecture-analysis`
- Labels: `research`, `gateway-pattern`, `mcp-protocol`
- Status: To Do
- Confluence link: Points to gateway research page

**RES-103 (Story):**
- Issue identity: RES-103
- Issue type: Story
- Epic Link: RES-100
- Description: Non-empty, contains goal and dependencies
- Component: `synthesis`
- Labels: `research`, `comparison`, `mcp-protocol`
- Status: To Do
- Confluence link: Points to synthesis page

## Approval Gate

**Required approvals before initialization execution:**
1. Confirm hierarchy mapping (Epic → Stories structure)
2. Confirm component policy and values
3. Confirm label policy and values
4. Confirm assignment convention
5. Confirm workflow/status convention
6. Approve external Jira mutation

## Notes

- All work items already have assigned Jira keys (RES-100, RES-101, RES-102, RES-103)
- Initialization will discover/reuse these existing issues
- Do NOT transition any issues during initialization
- Do NOT close any work items without explicit approval
- Preserve all existing Jira content and links
- Add reciprocal Confluence links only when documents exist
