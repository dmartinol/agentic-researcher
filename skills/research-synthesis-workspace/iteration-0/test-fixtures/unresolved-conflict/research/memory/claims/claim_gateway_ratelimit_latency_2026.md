---
claim_id: claim_gateway_ratelimit_latency_2026
statement: "API gateway rate limiting adds 5-12ms latency at 100k+ RPS load (based on 2026 evidence)"
label: Verified
sources:
  - src_cloudflare_whitepaper_2026
  - src_netflix_blog_2026
created_at: 2026-09-21T15:30:00Z
updated_at: 2026-09-21T15:30:00Z
relationships:
  contradicts:
    - claim_gateway_ratelimit_performance
---

# Evidence

**Cloudflare Whitepaper (2026-09-15):**
> "Under sustained load exceeding 100,000 requests per second, we observed P50 latency increases of 5-8ms and P99 increases of 10-12ms when enabling rate limiting at the edge gateway compared to no rate limiting baseline."

**Netflix Engineering Blog (2026-09-18):**
> "We were surprised to find that gateway-level rate limiting became a bottleneck at high RPS. The state synchronization required for accurate distributed rate limiting added measurable latency (P99 increased by 7-15ms) during peak traffic."

## Qualifications

- Impact appears at high scale (100k+ RPS)
- Latency increase may be acceptable depending on SLA requirements
- Distributed rate limiting (required for multi-node gateways) adds synchronization overhead
- Local (per-instance) rate limiting would reduce this impact but sacrifice accuracy
