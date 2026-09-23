# Jira Hierarchy Mapping

## Mapping Strategy

Since Jira is the approved ticketing provider, we apply Jira-specific conventions following the hierarchy: **Initiative → Epic → Story → Sub-task**.

This mapping is applied **only because Jira is configured** as the ticketing provider. The provider-neutral plan remains the authoritative source.

## Hierarchy Mapping

### Level 1: Initiative
**Jira Type:** Initiative  
**Provider-Neutral:** Research Project  
**Title:** "MCP Aggregation Architecture Research"

**Description:**
```
Research project to evaluate whether a cloud-native AI platform should introduce a centralized MCP aggregation/gateway layer versus direct agent-to-MCP connections.

Scope: Compare approaches for discovery, authentication, policy, operational complexity, observability, portability, and vendor coupling.

Expected Outputs: Evidence-backed architecture comparison with findings, conflicts, unknowns, and context-specific implications.
```

**Jira Fields:**
- Project: [To be resolved from configuration]
- Issue Type: Initiative
- Component: Research / Architecture
- Labels: mcp, architecture-research, cloud-native
- Assignee: [Current user from identity subsystem]

---

### Level 2: Epics (Workstreams)

#### Epic 1: Architecture Analysis
**Jira Type:** Epic  
**Provider-Neutral:** Workstream 1  
**Title:** "Architecture Pattern Analysis"

**Description:**
```
Workstream to analyze direct connection and aggregation gateway patterns for MCP integration.

This epic contains independent research tasks investigating different architectural approaches.
```

**Jira Fields:**
- Parent: Initiative (MCP Aggregation Architecture Research)
- Issue Type: Epic
- Component: Research / Architecture
- Labels: mcp, architecture-patterns
- Assignee: [Current user]

---

#### Epic 2: Synthesis and Recommendations
**Jira Type:** Epic  
**Provider-Neutral:** Workstream 2  
**Title:** "Comparative Analysis and Synthesis"

**Description:**
```
Workstream to synthesize findings from architecture research into evidence-backed comparison.

This epic contains synthesis tasks dependent on completion of architecture analysis tasks.
```

**Jira Fields:**
- Parent: Initiative (MCP Aggregation Architecture Research)
- Issue Type: Epic
- Component: Research / Synthesis
- Labels: mcp, synthesis, architecture-comparison
- Assignee: [Current user]
- Blocked By: Epic 1 (Architecture Analysis)

---

### Level 3: Stories (Research Tasks and Synthesis Tasks)

#### Story 1.1: Direct Connection Pattern Analysis
**Jira Type:** Story  
**Provider-Neutral:** Research Task 1.1  
**Title:** "Research: Direct Agent-to-MCP Connection Pattern"

**Description:**
```
Research Task: Investigate direct connection architecture where agent clients connect to individual MCP servers without intermediary layers.

Goal: Document the architecture, benefits, and challenges of direct agent-to-MCP connections.

Analysis Areas:
- Discovery mechanisms
- Authentication flows
- Operational characteristics
- Failure domains
- Operational complexity

Evidence Requirements:
- MCP protocol specifications
- Reference implementations
- Official documentation
- Community best practices

Expected Output: Technical analysis document in Confluence

Acceptance Criteria:
✓ Protocol interaction patterns documented
✓ Authentication/authorization boundaries identified
✓ Failure domains mapped
✓ Operational complexity assessed
✓ Evidence provenance recorded
✓ Contradictory evidence searched and preserved

Document Link: [To be added after document creation]
```

**Jira Fields:**
- Parent: Epic 1 (Architecture Pattern Analysis)
- Issue Type: Story
- Component: Research
- Labels: mcp, direct-connection, architecture-research
- Assignee: [Current user]
- Story Points: [Optional, based on project convention]

---

#### Story 1.2: Aggregation Gateway Pattern Analysis
**Jira Type:** Story  
**Provider-Neutral:** Research Task 1.2  
**Title:** "Research: Centralized MCP Aggregation Gateway Pattern"

**Description:**
```
Research Task: Investigate centralized gateway/aggregation layer approaches for MCP integration.

Goal: Document the architecture, benefits, and challenges of centralized MCP aggregation.

Analysis Areas:
- Gateway architecture patterns
- Policy enforcement capabilities
- Observability characteristics
- Vendor coupling implications
- Operational complexity

Evidence Requirements:
- Architecture patterns from similar systems
- Protocol aggregation specifications
- Gateway implementation examples
- Production deployment experiences

Expected Output: Technical analysis document in Confluence

Acceptance Criteria:
✓ Gateway architecture patterns documented
✓ Policy enforcement capabilities identified
✓ Observability characteristics assessed
✓ Vendor coupling implications analyzed
✓ Evidence provenance recorded
✓ Material conflicts identified and preserved

Document Link: [To be added after document creation]
```

**Jira Fields:**
- Parent: Epic 1 (Architecture Pattern Analysis)
- Issue Type: Story
- Component: Research
- Labels: mcp, aggregation-gateway, architecture-research
- Assignee: [Current user]
- Story Points: [Optional, based on project convention]

---

#### Story 2.1: Comparative Architecture Analysis
**Jira Type:** Story  
**Provider-Neutral:** Synthesis Task 2.1  
**Title:** "Synthesis: MCP Architecture Pattern Comparison"

**Description:**
```
Synthesis Task: Compare direct connection and aggregation gateway patterns based on research findings.

Goal: Synthesize findings into evidence-backed architecture comparison.

Comparison Dimensions:
- Discovery and tool aggregation
- Authentication/authorization boundaries
- Policy and governance
- Operational complexity and failure domains
- Observability
- Portability
- Vendor coupling

Evidence Requirements:
- Validated claims from dependent research tasks
- Cross-pattern verification
- Deployment context considerations

Expected Output: Architecture comparison report in Confluence

Acceptance Criteria:
✓ All comparison dimensions addressed
✓ Evidence-backed findings with provenance
✓ Material conflicts/unknowns explicitly documented
✓ Context-dependent implications identified
✓ No forced binary recommendation when evidence is contextual
✓ Synthesis references validated source evidence
✓ Contradictions preserved without silent resolution
✓ Recommendations tied to specific deployment contexts

Dependencies: Requires completion of Stories 1.1 and 1.2

Document Link: [To be added after document creation]
```

**Jira Fields:**
- Parent: Epic 2 (Comparative Analysis and Synthesis)
- Issue Type: Story
- Component: Research / Synthesis
- Labels: mcp, synthesis, architecture-comparison
- Assignee: [Current user]
- Blocked By: Story 1.1, Story 1.2
- Story Points: [Optional, based on project convention]

---

## Mapping Rationale

### Why This Hierarchy?

1. **Initiative Level**: Represents the entire research project as a cohesive effort with clear objective and scope.

2. **Epic Level**: Maps to provider-neutral Workstreams, grouping related research activities.

3. **Story Level**: Maps to individual Research Tasks and Synthesis Tasks that are independently executable units of work.

4. **Sub-task Level**: Not used in this plan because the task granularity is already appropriate for Story level. Sub-tasks would be created only if operational execution requires further decomposition.

### Hierarchy Constraints Applied

- Validated against target Jira project capabilities
- Respects Jira's hierarchy rules (Initiative → Epic → Story → Sub-task)
- Does not force unnecessary hierarchy levels
- Every work item has meaningful, non-empty description
- Descriptions focus on research goals, not just workflow metadata

### Jira-Specific Conventions Applied

**Components:**
- Research: For investigative tasks
- Synthesis: For synthesis/analysis tasks
- Architecture: Domain classification

**Labels:**
- Subject tags: mcp, architecture-research, cloud-native
- Pattern tags: direct-connection, aggregation-gateway
- Activity tags: synthesis, architecture-comparison

**Assignment:**
- Current authenticated user (from identity subsystem)
- Consistent across all related work items

**Status/Workflow:**
- Initial status: To Do (or project-default initial state)
- No transitions during initialization (per Jira conventions)
- Transitions executed only during approved execution phases

**Links:**
- Reciprocal Confluence document links (added after document creation)
- Dependency links (Blocked By) for synthesis tasks
- Parent/child relationships through hierarchy
