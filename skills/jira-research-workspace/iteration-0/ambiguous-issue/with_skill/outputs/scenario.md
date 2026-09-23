# Test Scenario: Ambiguous Issue Detection

## Context
Testing the jira-research skill's handling of ambiguous issue matches during initialization.

## Scenario Setup

### Planned Research Task
**Research Task ID:** RT-001
**Title:** "Investigate API Performance Degradation in Production"
**Description:** Research the root cause of 200ms latency increase in the /api/users endpoint observed in production over the last week.
**Type:** Research Task
**Workstream:** Performance Investigation

### Discovered Jira Issues

#### Issue 1: PERF-123
- **Summary:** "API Performance Issues - Users Endpoint"
- **Description:** "The /api/users endpoint is showing slower response times. Need to investigate."
- **Type:** Story
- **Status:** Open
- **Component:** API
- **Labels:** performance, api
- **Assignee:** Unassigned
- **Created:** 2026-09-15

#### Issue 2: PERF-456
- **Summary:** "Investigate Production Performance Degradation"
- **Description:** "Production monitoring shows API latency has increased. Focus on user-related endpoints."
- **Type:** Task
- **Status:** To Do
- **Component:** Performance
- **Labels:** production, performance, investigation
- **Assignee:** Unassigned
- **Created:** 2026-09-18

## Ambiguity Analysis

Both issues appear to match the planned Research Task RT-001:
- **PERF-123** matches on: users endpoint, performance investigation, API focus
- **PERF-456** matches on: production performance degradation, investigation scope

Neither is a perfect match, but both are plausible candidates for reuse during initialization.
