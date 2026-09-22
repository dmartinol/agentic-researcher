# RT-002: Security Evaluation Output

**Task:** Security evaluation of message queue options  
**Status:** Complete  
**Completed:** 2026-09-20

## Security Posture Comparison

### Amazon SQS
- ✅ Server-side encryption (KMS) with no performance penalty (`claim_sqs_encryption`)
- ✅ AWS IAM integration (native access control)
- ✅ SOC 2, HIPAA, PCI DSS compliant (AWS certifications)
- ✅ Managed service (AWS handles security patches)

### Apache Kafka
- ⚠️ TLS encryption available but requires manual configuration
- ⚠️ ACL-based authorization (requires ZooKeeper or KRaft setup)
- ✅ SASL/SCRAM authentication supported
- ⚠️ Security responsibility on operator (self-managed)

### RabbitMQ
- ⚠️ TLS encryption requires manual certificate management
- ✅ Pluggable authentication (LDAP, OAuth supported)
- ⚠️ No built-in encryption at rest
- ⚠️ Security patching requires manual upgrades

## Key Claims Generated

- `claim_sqs_encryption` - SQS provides KMS encryption at rest

## Security Gaps

- **RabbitMQ**: No evidence found for encryption at rest capability
- **Kafka**: No claims generated for specific compliance certifications (need follow-up)
