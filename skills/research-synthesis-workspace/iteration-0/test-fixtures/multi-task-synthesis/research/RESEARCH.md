# Architecture Comparison: Message Queue Selection

## Research Question

Which message queue technology should we adopt: RabbitMQ, Apache Kafka, or Amazon SQS?

## Acceptance Criteria

- Compare security posture across three options
- Evaluate operational complexity and monitoring requirements
- Assess performance characteristics for our 50k msg/sec workload
- Provide traceable evidence for each decision criterion

## Scope

- Current technology versions (as of Sept 2026)
- Cloud deployment (AWS environment)
- Event-driven microservices architecture

## Research Tasks

- [x] **RT-001-discovery**: Discovery research on message queue options
- [x] **RT-002-security**: Security evaluation of each option
- [x] **RT-003-operations**: Operations and monitoring assessment
- [ ] **RT-004-synthesis**: Architecture comparison synthesis

## Dependencies

RT-004 depends on: RT-001, RT-002, RT-003
