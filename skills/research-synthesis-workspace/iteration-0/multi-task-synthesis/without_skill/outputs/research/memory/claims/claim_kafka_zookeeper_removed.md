---
claim_id: claim_kafka_zookeeper_removed
statement: "Kafka 3.x+ eliminates ZooKeeper dependency via KRaft consensus protocol"
label: Verified
sources:
  - src_kafka_kraft_guide
created_at: 2026-09-20T12:45:00Z
updated_at: 2026-09-20T12:45:00Z
---

# Evidence

Apache Kafka 3.3+ (released May 2023) declared KRaft mode production-ready, removing the operational burden of managing a separate ZooKeeper cluster.

**Source:** Kafka KRaft Mode Documentation
**URL:** https://kafka.apache.org/documentation/#kraft
**Observation Date:** 2026-09-20

## Qualifications

- KRaft production-ready as of Kafka 3.3 (May 2023)
- Migration from ZooKeeper to KRaft requires downtime
- Some legacy tooling still assumes ZooKeeper presence
