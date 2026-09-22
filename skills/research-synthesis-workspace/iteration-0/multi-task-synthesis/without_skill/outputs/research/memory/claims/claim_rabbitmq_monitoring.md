---
claim_id: claim_rabbitmq_monitoring
statement: "RabbitMQ requires manual setup of Prometheus exporters and custom dashboards for production monitoring"
label: Reported
sources:
  - src_rabbitmq_monitoring_2026
created_at: 2026-09-20T13:20:00Z
updated_at: 2026-09-20T13:20:00Z
---

# Evidence

RabbitMQ Management Plugin provides web UI and HTTP API, but production-grade observability requires integrating third-party exporters (rabbitmq_exporter for Prometheus) and building custom Grafana dashboards.

**Source:** RabbitMQ Monitoring Guide
**URL:** https://www.rabbitmq.com/docs/monitoring
**Observation Date:** 2026-09-20

## Qualifications

- Native management plugin has basic metrics only
- Community-maintained exporters not officially supported
- CloudAMQP managed service provides built-in dashboards
