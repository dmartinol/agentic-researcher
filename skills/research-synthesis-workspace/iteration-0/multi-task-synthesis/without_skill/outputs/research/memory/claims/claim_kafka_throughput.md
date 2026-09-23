---
claim_id: claim_kafka_throughput
statement: "Apache Kafka achieves 2M+ messages/second throughput on standard hardware"
label: Verified
sources:
  - src_kafka_benchmarks_2026
created_at: 2026-09-20T10:15:00Z
updated_at: 2026-09-20T10:15:00Z
---

# Evidence

Apache Kafka's official benchmark results from September 2026 demonstrate throughput exceeding 2 million messages per second on commodity hardware (3-node cluster, m5.2xlarge instances).

**Source:** Kafka Performance Benchmarks 2026
**URL:** https://kafka.apache.org/benchmarks/2026
**Observation Date:** 2026-09-20

## Qualifications

- Benchmark used 1KB message size
- Results on AWS m5.2xlarge (8 vCPU, 32 GB RAM)
- Replication factor of 3
- Performance degrades with larger message sizes
