---
claim_id: claim_rabbitmq_throughput
statement: "RabbitMQ achieves 50k-100k messages/second depending on message routing complexity"
label: Verified
sources:
  - src_rabbitmq_docs_2026
created_at: 2026-09-20T11:30:00Z
updated_at: 2026-09-20T11:30:00Z
---

# Evidence

RabbitMQ documentation and CloudAMQP benchmarks show throughput of 50,000-100,000 messages/second for typical workloads. Performance varies significantly based on exchange type, routing complexity, and persistence requirements.

**Source:** RabbitMQ Performance Tuning Guide 2026
**URL:** https://www.rabbitmq.com/docs/performance
**Observation Date:** 2026-09-20

## Qualifications

- Higher throughput achieved with topic exchanges vs headers
- Persistent messages reduce throughput by ~40%
- Clustering adds coordination overhead
