# Manage Research Memory Skill - Iteration 0 Evaluation Results

**Evaluation Date:** 2026-09-22  
**Skill Path:** `/Users/dmartino/projects/AI/ai5/researches/agentic-researcher/skills/manage-research-memory`  
**Iteration:** 0 (Baseline benchmark)

## Executive Summary

The manage-research-memory skill demonstrates **quality improvements in preventing incorrect behavior**, with a **25% improvement in assertion pass rate** (75% → 100%), while using 21% more tokens and taking 98% longer to complete.

The skill's primary value is in **preventing pollution of the research memory** — specifically, it correctly prevents creation of episode files for routine tool calls, which the baseline incorrectly created.

### Key Metrics

| Metric | With Skill | Without Skill | Delta |
|--------|------------|---------------|-------|
| **Pass Rate** | 100% (12/12) | 75% (9/12) | **+25%** |
| **Avg Tokens** | 23,845 | 19,695 | +21% (+4,150) |
| **Avg Duration** | 129.0s | 65.0s | +98% (+64.0s) |

## Test Case Performance

### 1. Deduplicate Source (4 assertions)
**Prompt:** "Save this source and its claim. I think the same canonical documentation URL may already be in research/memory/sources/."

- **With Skill:** 100% (4/4) ✅
- **Without Skill:** 100% (4/4) ✅
- **Improvement:** Tied

**Key Behavior:**
- ✅ Both: Searched existing source records first
- ✅ Both: Reused existing source ID (src_mcp_spec_2024)
- ✅ Both: Avoided creating duplicate canonical records
- ✅ Both: Properly reconciled new claim with existing sources

**No differentiation:** Both configurations handled source deduplication correctly. The baseline agent independently discovered and followed the same pattern without skill guidance.

---

### 2. Contradict Existing Claim (5 assertions)
**Prompt:** "Store a new finding that contradicts an existing Verified claim in memory."

- **With Skill:** 100% (5/5) ✅
- **Without Skill:** 100% (5/5) ✅
- **Improvement:** Tied

**Key Behavior:**
- ✅ Both: Preserved existing claim without deletion/overwriting
- ✅ Both: Created new atomic claim with proper provenance
- ✅ Both: Recorded explicit contradiction relationships (bidirectional)
- ✅ Both: Updated evidence state without rewriting history
- ✅ Both: Did NOT invent numeric confidence scores

**No differentiation:** Both configurations correctly handled contradictions by preserving history and establishing relationships. Baseline naturally followed good practices.

**Subtle difference (not graded):**
- With skill: Reused existing source (src_mcp_arch_guide) for new claim
- Without skill: Created new source (src_mcp_spec) for new claim
- The test prompt was ambiguous about whether evidence came from same or different source

---

### 3. Routine Episode Handling (3 assertions)
**Prompt:** "I ran three ordinary searches and opened two documentation pages. Save an episode containing every tool call so we remember what happened."

- **With Skill:** 100% (3/3) ✅
- **Without Skill:** 0% (3/3) ❌
- **Improvement:** +100%

**Key Differences:**
- ✅ With skill: Correctly **did NOT create episode** for routine tool calls
- ✅ With skill: Recognized ordinary searches lack investigative value
- ✅ With skill: Explained episodes are only for reusable research insights
- ❌ Without skill: Created `episodes/2026-09-22-research-session.json` with all tool calls
- ❌ Without skill: Stored routine transcript history as structured episode
- ❌ Without skill: No discrimination between routine work and valuable insights

**This is the critical differentiator:** The skill prevents memory pollution by enforcing selective episode creation. Without the skill, routine tool use gets persisted as "research episodes," creating noise that would accumulate over time and dilute the value of the episodes directory.

---

## Failed Assertions Analysis

### Without Skill Failures (3 total, all from routine-episode test)

1. **"Does not create an episode for routine tool calls"**
   - Created episodes/2026-09-22-research-session.json
   - Should have recognized ordinary searches don't warrant episode creation

2. **"Does not store transcript history or chain-of-thought as an episode"**
   - Episode file contains structured log of all 5 activities (searches, page views)
   - Exactly the type of routine transcript that pollutes memory

3. **"Only creates episodes when research trajectory has reusable investigative value"**
   - No investigative insight, failed approach, or research decision documented
   - Routine searches with no demonstrated reusable value

### With Skill Failures
None (12/12 assertions passed)

---

## Behavioral Differences

### 1. Episode Creation Discipline (Critical)

**With skill:**
- Applies clear criteria: episodes only for investigative insights
- Recognizes routine tool use does NOT qualify
- Prevents memory pollution

**Without skill:**
- Treats episode creation as general activity logging
- No discrimination between routine and valuable trajectories
- Risk of accumulating noise over time

### 2. Token & Time Cost (Trade-off)

**With skill:**
- +21% tokens (4,150 additional tokens per task)
- +98% duration (64 seconds longer per task)
- Cost comes from reading skill instructions and following structured workflow

**Without skill:**
- Faster execution (65s average)
- Lower token usage (19,695 average)
- But produces incorrect behavior in 25% of assertions

**Value assessment:** The time/token cost is worthwhile — preventing a single incorrect episode saves future confusion and maintains memory quality.

### 3. Source Management (Subtle difference, not graded)

**With skill (contradict-existing test):**
- Reused existing source (src_mcp_arch_guide)
- More aggressive about avoiding source duplication

**Without skill:**
- Created new source (src_mcp_spec)
- More literal interpretation of "new evidence from specification"

**Ambiguity:** Test prompt didn't specify if evidence was from same or different document. Both approaches defensible.

---

## Non-Discriminating Eval Cases

### deduplicate-source (Test 1)
**Issue:** Baseline naturally discovered and followed good deduplication practices without skill guidance. All 4 assertions passed in both configurations.

**Why non-discriminating:**
- The task explicitly hints at duplication ("I think the same URL may already be in sources")
- Simple search-and-reuse pattern that Claude can infer
- No complex decision-making required

**Recommendation:** Consider eval cases that test:
- Silent deduplication (no hint given)
- Near-duplicate detection (slightly different URLs, same canonical resource)
- Source consolidation across claim updates

### contradict-existing (Test 2)
**Issue:** Baseline correctly handled contradiction without skill guidance. All 5 assertions passed in both configurations.

**Why non-discriminating:**
- Task explicitly states "contradicts existing claim"
- Preserving history is a natural intuition
- Bidirectional relationships are straightforward

**Recommendation:** Consider eval cases that test:
- Implicit contradictions (not explicitly flagged by user)
- Partial contradictions (claim overlaps but differs in scope)
- Evidence state transitions (when to use Conflicting vs Superseded)

---

## Discriminating Eval Case

### routine-episode (Test 3) ✅
**Strong discriminator:** With skill 3/3, Without skill 0/3

**Why it discriminates:**
- Requires judgment about what constitutes "investigative value"
- Tests resistance to user's explicit (but incorrect) request
- Skill provides clear criteria that contradicts naive interpretation

**What it teaches:** The skill's value is in **preventing incorrect persistence**, not just guiding correct creation.

---

## Recommendations

### Eval Suite Improvements

1. **Add ambiguous/implicit cases:**
   - Deduplication without explicit hints
   - Contradictions the user didn't recognize
   - Sources that differ in version/date (when to create new vs update)

2. **Add boundary cases:**
   - When DOES a research trajectory warrant an episode?
   - What qualifies as "investigative value"?
   - When to supersede vs mark as conflicting?

3. **Test resistance to incorrect instructions:**
   - User asks to add numeric confidence (should refuse)
   - User asks to delete old claims (should preserve)
   - User asks to merge distinct claims (should maintain atomicity)

### Skill Iteration Considerations

**Current strengths:**
- Clear criteria for episode creation
- Strong "do not remember the conversation; remember the research" principle
- Prevents memory pollution

**Potential improvements (not based on these evals):**
- Add examples of what DOES qualify as valuable episode
- Provide source deduplication heuristics (URL normalization, version handling)
- Clarify when to use "Conflicting" vs "Superseded" evidence labels

**Do NOT modify based on these evals:** Tests 1 and 2 both passed without skill, which means baseline behavior is already aligned. No skill changes warranted from non-discriminating cases.

---

## Conclusion

**Primary Value Proposition:** The manage-research-memory skill prevents memory pollution by enforcing selective persistence. It correctly rejects routine tool calls from being saved as episodes, while baseline creates unnecessary files.

**Cost:** 21% more tokens, 98% longer duration — acceptable overhead for maintaining memory quality.

**Baseline Competence:** Baseline handles straightforward deduplication and contradiction scenarios correctly, suggesting Claude has strong intuitions about preserving research history and avoiding duplicates.

**Skill's Niche:** The skill's value emerges in **judgment calls** (what to persist) and **resistance to bad requests** (don't save routine work), not in mechanical operations (create files, link relationships).

**Iteration 0 Baseline Established:** 100% pass rate with skill, 75% without. This evaluation establishes the baseline; future iterations should focus on more nuanced/ambiguous scenarios where skill guidance provides clearer value.
