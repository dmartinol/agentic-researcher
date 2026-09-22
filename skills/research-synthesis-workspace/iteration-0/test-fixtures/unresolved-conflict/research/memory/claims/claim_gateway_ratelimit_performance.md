---
claim_id: claim_gateway_ratelimit_performance
statement: "API gateway rate limiting has negligible performance impact (<1ms latency)"
label: Conflicting
sources:
  - src_aws_apigateway_2025
  - src_kong_benchmarks_2024
  - src_cloudflare_whitepaper_2026
  - src_netflix_blog_2026
created_at: 2026-09-21T09:00:00Z
updated_at: 2026-09-21T15:30:00Z
relationships:
  contradicted_by:
    - claim_gateway_ratelimit_latency_2026
---

# Evidence

## Supporting Evidence (5 sources favor low/negligible impact)

1. **AWS API Gateway docs (2025)**: Claims <1ms overhead for rate limiting
2. **Kong Gateway benchmarks (2024)**: Reports 0.5ms median latency increase
3. **Nginx blog (2023)**: Describes rate limiting as "lightweight operation"
4. **Envoy docs (2024)**: States "minimal performance overhead"
5. **Azure API Management (2025)**: Advertises "sub-millisecond policy execution"

## Contradicting Evidence (2 credible current sources)

1. **Cloudflare whitepaper (Sept 2026)**: Reports 5-12ms latency increase at 100k RPS load
   - Source: `src_cloudflare_whitepaper_2026`
   - Recent (published 2026-09-15)
   - Authoritative (Cloudflare operates one of world's largest edge networks)

2. **Netflix blog (Sept 2026)**: Describes gateway rate limiting as "surprisingly expensive" at scale
   - Source: `src_netflix_blog_2026`
   - Recent (published 2026-09-18)
   - Authoritative (Netflix handles massive traffic volumes)

## Conflict Analysis

The contradiction appears **genuine and material**:
- Older sources (2023-2025) claim negligible impact
- Two credible 2026 sources report measurable impact at high scale
- Difference may be workload-dependent (RPS, request complexity)
- Cannot be resolved by majority vote

## Applicability Impact

This conflict directly affects the architecture decision for high-throughput APIs (>50k RPS). For low-traffic APIs, the older evidence may still hold.
