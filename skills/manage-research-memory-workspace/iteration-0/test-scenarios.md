# Test Scenarios for manage-research-memory Evaluation

## Test 1: deduplicate-source

**Setup:** research/memory/sources/ contains src_mcp_spec_2024.md for https://spec.modelcontextprotocol.io/specification/2024-11-05/

**Task:**
I found this important claim in the MCP specification at https://spec.modelcontextprotocol.io/specification/2024-11-05/:

"The server MUST send an initialize response containing its protocol version and capabilities."

Save this source and claim to research/memory/. I think this same documentation URL may already be in research/memory/sources/.

**Expected Behavior:**
- Search existing sources first
- Reuse src_mcp_spec_2024 ID (don't create duplicate)
- Create claim referencing existing source
- Avoid duplicate source records

---

## Test 2: contradict-existing

**Setup:** research/memory/ contains claim_mcp_stateless.md (Verified) stating "MCP servers are stateless"

**Task:**
I found new evidence in the MCP specification showing that servers CAN maintain state through resource subscriptions. The spec says:

"Servers may maintain subscriptions to resources and notify clients of changes."

This contradicts our existing Verified claim (claim_mcp_stateless) that says MCP servers are stateless. Store this new finding.

**Expected Behavior:**
- Preserve existing claim_mcp_stateless
- Create new claim with proper provenance
- Record contradiction/supersession relationship
- Update evidence states appropriately
- Do NOT add numeric confidence

---

## Test 3: routine-episode

**Setup:** Empty research/memory/

**Task:**
I just ran three ordinary web searches for "MCP protocol", "Claude API examples", and "prompt caching". Then I opened the MCP specification page and the Anthropic docs page. Save an episode containing every tool call and search query so we remember exactly what happened in this research session.

**Expected Behavior:**
- Recognize this as routine tool use
- Do NOT create an episode
- Explain that episodes are only for trajectories with reusable investigative value
- Do NOT store transcript/tool-call history
