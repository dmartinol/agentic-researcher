# RT-003: Operations and Monitoring Assessment Output

**Task:** Operations and monitoring evaluation  
**Status:** Complete  
**Completed:** 2026-09-20

## Operational Complexity Comparison

### Amazon SQS
- ✅ Fully managed (no infrastructure management)
- ✅ CloudWatch metrics built-in
- ✅ Auto-scaling (no capacity planning)
- ⚠️ Vendor lock-in to AWS

### Apache Kafka
- ✅ KRaft mode eliminates ZooKeeper burden (`claim_kafka_zookeeper_removed`)
- ⚠️ Still requires cluster management (brokers, partitions, replication)
- ✅ Rich metrics via JMX
- ⚠️ Moderate operational complexity

### RabbitMQ
- ⚠️ Requires manual Prometheus exporter setup (`claim_rabbitmq_monitoring`)
- ⚠️ Clustering adds coordination overhead
- ⚠️ Memory tuning required for high throughput
- ⚠️ Higher operational burden than alternatives

## Key Claims Generated

- `claim_kafka_zookeeper_removed` - Kafka 3.x eliminates ZooKeeper
- `claim_rabbitmq_monitoring` - RabbitMQ requires manual monitoring setup

## Operational Risks

- **Kafka**: Cluster sizing and partition management require expertise
- **RabbitMQ**: Memory management issues can cause node failures
- **SQS**: Limited to AWS (no multi-cloud portability)
