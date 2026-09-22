---
claim_id: claim_postgres_read_performance
statement: "PostgreSQL with proper indexing achieves <10ms P95 latency for our user lookup queries"
label: Verified
sources:
  - src_postgres_benchmark_2026
created_at: 2026-09-21T10:00:00Z
updated_at: 2026-09-21T10:00:00Z
---

# Evidence

Benchmark results from PostgreSQL 16 on AWS RDS show P95 latency under 10ms for indexed SELECT queries on 10M row user table.

**Source:** PostgreSQL Performance Tuning Guide 2026
**URL:** https://www.postgresql.org/docs/16/performance-tips.html
**Observation Date:** 2026-09-21

## Qualifications

- Requires B-tree indexes on frequently queried columns
- Performance degrades without proper index maintenance
- Tested on db.r6g.xlarge instances
