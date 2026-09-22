---
claim_id: claim_mongodb_horizontal_scaling
statement: "MongoDB supports horizontal scaling via sharding with automatic balancing"
label: Verified
sources:
  - src_mongodb_docs_2026
created_at: 2026-09-21T11:00:00Z
updated_at: 2026-09-21T11:00:00Z
---

# Evidence

MongoDB documentation confirms native sharding support with automatic chunk migration and balancing across shards.

**Source:** MongoDB Sharding Documentation
**URL:** https://www.mongodb.com/docs/manual/sharding/
**Observation Date:** 2026-09-21

## Qualifications

- Sharding requires upfront shard key design
- Poorly chosen shard keys can cause hotspots
- Adds operational complexity (config servers, mongos routers)
