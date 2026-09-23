# Sample Inputs for greenfield-init Evaluation

This file documents the inputs that would be required to execute a complete greenfield initialization with the initialize-research skill.

## Required: RESEARCH.md

Save to: `inputs/RESEARCH.md`

```markdown
---
status: plan-approved
---

# Research: MCP Aggregation Architecture

## Topic

Model Context Protocol (MCP) aggregation and gateway patterns for cloud-native AI platforms

## Objective

Should a cloud-native AI platform introduce a centralized MCP aggregation/gateway layer rather than connecting agent clients directly to individual MCP servers?

## Scope

### Included

- Discovery and tool aggregation approaches
- Authentication and authorization boundaries
- Policy and governance capabilities
- Operational complexity and failure domains
- Observability and monitoring
- Portability and vendor coupling
- Current MCP protocol specifications
- Production deployment patterns

### Excluded

- Implementation scheduling and staffing
- Budget and cost analysis
- Specific product procurement
- Custom MCP server development

## Expected Outputs

A concise architecture comparison with:
- Evidence-backed findings for each evaluation dimension
- Material conflicts and unknowns identified
- Implications of centralized vs. direct connection approaches
- Context-dependent recommendations (no forced binary choice)

## Evidence Policy

- Prefer authoritative and primary sources where available.
- Record provenance for important factual claims.
- Preserve conflicting credible evidence.
- Do not infer absence from lack of evidence.
- Revalidate evidence when freshness materially affects the conclusion.

Additional research-specific evidence requirements:
- Use current MCP protocol specifications (v1.0 or later)
- Prefer official documentation from protocol maintainers
- Validate architectural claims with source repositories
- Use independent sources for critical decision factors
- Check version/date applicability for all cited evidence

## Subsystems

### Ticketing

Provider: Jira

Configuration:
- Project: RES
- Hierarchy: Epic → Story → Sub-task
- Component: "MCP Research"
- Labels: mcp, architecture, research
- Assignment: Current user
- Initial status: To Do

### Document Store

Provider: Confluence

Configuration:
- Space: RESEARCH
- Root page: "Active Research"
- Page hierarchy mirrors work hierarchy
- Visual markers: 🧭 Epic, 🔬 Research Story, 🧩 Synthesis Story
- Author metadata: Include creation date
- Jira link format: Card presentation

### Repository

Enabled: Yes

Provider: Git

Purpose: research-artifacts

Configuration:
- Repository: Current working repository
- Artifacts path: research/
- Memory path: research/memory/
- Reports path: research/reports/

## Research Conventions

### Work Hierarchy
- One Epic for the overall research
- Multiple Research Task stories for independent investigation areas
- One Synthesis Task story dependent on Research Tasks
- Sub-tasks only if meaningful decomposition exists

### Work Item Descriptions
- Epic: Research topic, objective, and scope summary
- Research Task: Specific investigation area and expected findings
- Synthesis Task: Integration objective and dependent tasks

### Document Structure
- Epic page: Research overview with child page links
- Research Task pages: Investigation area with findings sections
- Synthesis Task page: Integrated analysis and recommendations

### Classification
- Component: "MCP Research" on all Jira issues
- Labels: mcp, architecture, research on Epic; specific tags on tasks
- Confluence labels: Match Jira labels for cross-reference

## Approval Policy

External initialization requires approval: Yes

Plan requires approval before execution: Yes

Closure requires explicit approval: Yes

## External Resources

<!-- Stable IDs and links will be recorded here during initialization -->
```

## Optional: approved-plan.md

Save to: `inputs/approved-plan.md`

```markdown
# Approved Research Plan: MCP Aggregation Architecture

## Work Breakdown

### Epic: MCP Aggregation Architecture Research
- **Summary**: Evaluate centralized MCP aggregation vs. direct connection patterns
- **Description**: Compare architectural approaches for discovery, tool aggregation, authentication, policy enforcement, operational complexity, observability, and portability in cloud-native AI platforms using MCP.

### Research Task 1: Discovery and Tool Aggregation
- **Summary**: Research discovery and tool aggregation approaches
- **Description**: Investigate how centralized aggregation and direct connection patterns handle service discovery, tool capability aggregation, and client-side vs. server-side aggregation trade-offs.
- **Expected Findings**: Comparison of discovery mechanisms, aggregation complexity, and capability exposure patterns

### Research Task 2: Authentication and Authorization
- **Summary**: Research authentication and authorization boundaries
- **Description**: Analyze how each pattern handles authentication propagation, authorization policy enforcement, token management, and credential isolation.
- **Expected Findings**: Security boundary analysis and credential flow comparison

### Research Task 3: Policy and Governance
- **Summary**: Research policy and governance capabilities
- **Description**: Evaluate centralized policy enforcement, tool usage governance, audit logging, and compliance controls in each pattern.
- **Expected Findings**: Policy enforcement mechanisms and governance capabilities

### Research Task 4: Operational Complexity
- **Summary**: Research operational complexity and failure domains
- **Description**: Compare deployment complexity, failure isolation, blast radius, recovery patterns, and operational overhead.
- **Expected Findings**: Operational complexity assessment and failure domain analysis

### Research Task 5: Observability
- **Summary**: Research observability and monitoring approaches
- **Description**: Investigate centralized vs. distributed monitoring, trace correlation, metrics aggregation, and debugging capabilities.
- **Expected Findings**: Observability pattern comparison

### Research Task 6: Portability and Vendor Coupling
- **Summary**: Research portability and vendor coupling implications
- **Description**: Analyze protocol dependency, vendor lock-in, migration complexity, and standardization alignment.
- **Expected Findings**: Portability and coupling assessment

### Synthesis Task: Architecture Comparison
- **Summary**: Synthesize MCP architecture findings
- **Description**: Integrate findings from all research tasks into comprehensive architecture comparison with evidence-backed recommendations.
- **Dependencies**: All Research Tasks (1-6)
- **Expected Outputs**: Final architecture comparison document with context-dependent recommendations
```

## File Structure

For complete evaluation setup:

```
inputs/
├── RESEARCH.md          # Required: Approved research configuration
└── approved-plan.md     # Optional: Detailed work breakdown

outputs/                 # Created by evaluation execution
├── response.txt         # Complete skill execution log
├── execution-summary.md # Evaluation analysis
├── STATE.md            # Updated research state (if successful)
└── mutation-ledger.json # Created resource inventory (if successful)
```

## Execution Command

With inputs provided, invoke the skill:

```bash
claude /initialize-research
```

Or via the research-initializer agent:

```bash
claude @research-initializer "The research plan is approved. Initialize the configured ticketing and document structures now."
```

## Expected Outputs (with valid inputs)

### STATE.md
Updated with:
- Phase: Initialized
- Work Status: Ready items list with Jira keys
- External Resources: All Jira keys and Confluence page URLs
- Next Actions: Review and approve execution

### mutation-ledger.json
```json
{
  "created_resources": [
    {
      "type": "jira_issue",
      "key": "RES-XXX",
      "url": "https://jira.example.com/browse/RES-XXX",
      "issue_type": "Epic",
      "summary": "MCP Aggregation Architecture Research",
      "verified": true
    },
    {
      "type": "confluence_page",
      "id": "123456",
      "url": "https://confluence.example.com/display/RESEARCH/123456",
      "title": "🧭 MCP Aggregation Architecture Research",
      "parent": "Active Research",
      "verified": true
    }
  ],
  "discovered_resources": [],
  "reused_resources": [],
  "blocked_operations": []
}
```

### Jira Issues Created
- 1 Epic: MCP Aggregation Architecture Research
- 6 Stories: Research tasks for each investigation area
- 1 Story: Synthesis task (dependent on research tasks)

### Confluence Pages Created
- 1 Epic page: Research overview
- 6 Research task pages
- 1 Synthesis task page
- All with reciprocal Jira links

### Repository Artifacts
- research/memory/ directory created
- research/reports/ directory created
- No files created yet (initialization only)

## Notes

This sample configuration uses the MCP aggregation architecture research scenario from `examples/demo-research/scenario.md` to provide realistic and complete inputs for the greenfield initialization evaluation.
