---
claim_id: claim_sqs_encryption
statement: "Amazon SQS provides server-side encryption at rest using AWS KMS with no performance penalty"
label: Verified
sources:
  - src_aws_sqs_security_2026
created_at: 2026-09-20T14:00:00Z
updated_at: 2026-09-20T14:00:00Z
---

# Evidence

AWS SQS documentation confirms server-side encryption (SSE) using AWS KMS is available with transparent performance (no measurable latency impact per AWS whitepapers).

**Source:** AWS SQS Security Best Practices
**URL:** https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html
**Observation Date:** 2026-09-20

## Qualifications

- Encryption at rest only; in-transit encryption via TLS
- KMS key costs apply per API call
- Customer-managed keys require additional IAM permissions
