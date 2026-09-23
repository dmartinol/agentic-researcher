# Test Scenario: Existing Content

## Context
- Document store provider: Confluence
- Confluence space: RESEARCH
- Root page: "Research Documentation"
- Associated Jira ticket: PROJ-123 "Evaluate Redis vs PostgreSQL for session storage"

## Existing Page State

**Page ID:** 987654321
**Title:** Session Storage Research
**Parent:** Research Documentation (page ID: 123456789)
**Current Version:** 3
**URL:** https://confluence.example.com/pages/987654321

### Current Page Content:

```
Session Storage Research

Last updated: Sep 15, 2026

I've been looking into Redis vs PostgreSQL for our session storage needs. Here are my initial findings:

Redis provides significantly better performance for session data. In our load testing, Redis handled 50,000 concurrent sessions with p95 latency under 5ms, while PostgreSQL showed p95 latency around 45ms for the same workload.

Memory efficiency is a concern with Redis - we'd need approximately 2GB of RAM per 100K active sessions based on our session data structure. PostgreSQL stores sessions on disk but requires more aggressive connection pooling.

The team has experience with both technologies. Redis requires more operational overhead (cluster management, failover configuration) but PostgreSQL is already in our stack for the main application database.

One major consideration: Redis sessions are ephemeral by default. We'd need to configure persistence, which adds complexity. PostgreSQL sessions persist naturally but require a cleanup job for expired sessions.

Cost analysis shows Redis would require dedicated infrastructure ($500/month estimated for production HA setup), while PostgreSQL could use our existing database cluster with minimal additional cost.
```

## Task
The research needs to be brought into the proper Confluence structure:
- Add Jira work-item link (PROJ-123) near the header
- Add Goal/Purpose section based on the Jira ticket
- Preserve all existing research findings
- Maintain proper page metadata
- Do NOT replace content with empty template
