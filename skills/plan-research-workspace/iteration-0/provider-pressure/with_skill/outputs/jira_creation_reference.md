# Jira Creation Reference

This document provides reference information for creating the planned Jira structure.

## Overview

The plan-research skill creates a **provider-neutral** research plan first, then maps it to Jira's specific issue types. This reference shows what that Jira creation would look like.

## Epic Creation

**Type**: Epic  
**Summary**: Gateway Technology Evaluation  
**Description**:
```
Evaluate three gateway options to determine the most suitable solution for our requirements.

Acceptance Criteria:
- Complete technical assessments of all three gateway options
- Comparative analysis completed with decision matrix
- Final recommendation approved by stakeholders
- Implementation roadmap created for selected option
```

## Story 1: Assess Gateway Option A

**Type**: Story  
**Epic Link**: Gateway Technology Evaluation  
**Summary**: Assess Gateway Option A  
**Description**:
```
Complete technical evaluation of Gateway Option A including architecture, features, performance, and integration capabilities.

Acceptance Criteria:
- Architecture and design patterns documented
- Feature matrix completed
- Performance benchmarks identified
- Integration requirements catalogued
- Operational complexity assessed
- Security and compliance capabilities evaluated
- Technical assessment document (gateway-option-a-assessment.md) completed
```

### Sub-tasks for Story 1

1. **Research Gateway A architecture and design patterns**
   - Investigate and document the architectural approach and core design patterns used by Gateway Option A

2. **Document Gateway A feature set and capabilities**
   - Create comprehensive feature matrix covering all capabilities offered by Gateway Option A

3. **Identify Gateway A performance benchmarks**
   - Research and document performance metrics, throughput, latency, and scalability characteristics

4. **Catalog Gateway A integration requirements**
   - Document integration patterns, APIs, protocols, and compatibility requirements

5. **Assess Gateway A operational complexity**
   - Evaluate deployment, configuration, monitoring, and maintenance requirements

6. **Evaluate Gateway A security and compliance**
   - Research security features, compliance certifications, and audit capabilities

## Story 2: Assess Gateway Option B

**Type**: Story  
**Epic Link**: Gateway Technology Evaluation  
**Summary**: Assess Gateway Option B  
**Description**:
```
Complete technical evaluation of Gateway Option B including architecture, features, performance, and integration capabilities.

Acceptance Criteria:
- Architecture and design patterns documented
- Feature matrix completed
- Performance benchmarks identified
- Integration requirements catalogued
- Operational complexity assessed
- Security and compliance capabilities evaluated
- Technical assessment document (gateway-option-b-assessment.md) completed
```

### Sub-tasks for Story 2

1. **Research Gateway B architecture and design patterns**
   - Investigate and document the architectural approach and core design patterns used by Gateway Option B

2. **Document Gateway B feature set and capabilities**
   - Create comprehensive feature matrix covering all capabilities offered by Gateway Option B

3. **Identify Gateway B performance benchmarks**
   - Research and document performance metrics, throughput, latency, and scalability characteristics

4. **Catalog Gateway B integration requirements**
   - Document integration patterns, APIs, protocols, and compatibility requirements

5. **Assess Gateway B operational complexity**
   - Evaluate deployment, configuration, monitoring, and maintenance requirements

6. **Evaluate Gateway B security and compliance**
   - Research security features, compliance certifications, and audit capabilities

## Story 3: Assess Gateway Option C

**Type**: Story  
**Epic Link**: Gateway Technology Evaluation  
**Summary**: Assess Gateway Option C  
**Description**:
```
Complete technical evaluation of Gateway Option C including architecture, features, performance, and integration capabilities.

Acceptance Criteria:
- Architecture and design patterns documented
- Feature matrix completed
- Performance benchmarks identified
- Integration requirements catalogued
- Operational complexity assessed
- Security and compliance capabilities evaluated
- Technical assessment document (gateway-option-c-assessment.md) completed
```

### Sub-tasks for Story 3

1. **Research Gateway C architecture and design patterns**
   - Investigate and document the architectural approach and core design patterns used by Gateway Option C

2. **Document Gateway C feature set and capabilities**
   - Create comprehensive feature matrix covering all capabilities offered by Gateway Option C

3. **Identify Gateway C performance benchmarks**
   - Research and document performance metrics, throughput, latency, and scalability characteristics

4. **Catalog Gateway C integration requirements**
   - Document integration patterns, APIs, protocols, and compatibility requirements

5. **Assess Gateway C operational complexity**
   - Evaluate deployment, configuration, monitoring, and maintenance requirements

6. **Evaluate Gateway C security and compliance**
   - Research security features, compliance certifications, and audit capabilities

## Story 4: Comparative Analysis and Recommendation

**Type**: Story  
**Epic Link**: Gateway Technology Evaluation  
**Summary**: Comparative Analysis and Recommendation  
**Blocked By**: Assess Gateway Option A, Assess Gateway Option B, Assess Gateway Option C  
**Description**:
```
Synthesize findings from all gateway assessments into side-by-side comparison and provide data-driven recommendation.

Acceptance Criteria:
- Side-by-side feature comparison matrix completed
- Cost-benefit analysis conducted
- Risk assessment completed for each option
- Clear recommendation documented with justification
- Implementation roadmap created
- Comparison document (gateway-comparison-and-recommendation.md) completed
- Stakeholder approval obtained
```

### Sub-tasks for Story 4

1. **Create feature comparison matrix**
   - Build comprehensive side-by-side comparison of features across all three gateway options

2. **Conduct cost-benefit analysis**
   - Analyze total cost of ownership and benefits for each gateway option

3. **Perform risk assessment for each option**
   - Identify and evaluate risks associated with adopting each gateway option

4. **Draft recommendation with justification**
   - Create evidence-based recommendation identifying the preferred gateway option with supporting rationale

5. **Create implementation roadmap for recommended option**
   - Outline high-level implementation plan for the recommended gateway

6. **Present findings to stakeholders**
   - Present research findings, comparison, and recommendation to stakeholders for approval

## Implementation Notes

### Using Jira REST API

The structure could be created programmatically using the Jira REST API:

1. **Create Epic** using `/rest/api/3/issue`
2. **Create Stories** with epic link using `/rest/api/3/issue`
3. **Create Sub-tasks** with parent link using `/rest/api/3/issue`
4. **Set Dependencies** using issue links (`blocks`/`is blocked by`)

### Using Jira CLI

If using a Jira CLI tool (like `jira-cli`):

```bash
# Create epic
epic_key=$(jira create epic --summary "Gateway Technology Evaluation" --description "...")

# Create stories
story1_key=$(jira create story --epic "$epic_key" --summary "Assess Gateway Option A" --description "...")
story2_key=$(jira create story --epic "$epic_key" --summary "Assess Gateway Option B" --description "...")
story3_key=$(jira create story --epic "$epic_key" --summary "Assess Gateway Option C" --description "...")
story4_key=$(jira create story --epic "$epic_key" --summary "Comparative Analysis and Recommendation" --description "...")

# Create sub-tasks for each story
jira create subtask --parent "$story1_key" --summary "Research Gateway A architecture and design patterns"
# ... etc
```

### Manual Creation Order

If creating manually in Jira UI:

1. Create the Epic first
2. Create Stories 1-3 (can be done in any order)
3. Create all sub-tasks for Stories 1-3
4. Create Story 4
5. Add dependency links from Story 4 to Stories 1-3
6. Create all sub-tasks for Story 4

## Evidence Policy to Apply

When executing research tasks, ensure all work includes:
- Primary source references (official documentation)
- Quantitative metrics where available
- Community/industry feedback
- Concrete examples or case studies
- Version/date stamps for time-sensitive information

## Next Step

Per the plan-research skill workflow, this plan should be reviewed and approved before proceeding to the `initialize-research` skill, which would perform the actual Jira creation.
