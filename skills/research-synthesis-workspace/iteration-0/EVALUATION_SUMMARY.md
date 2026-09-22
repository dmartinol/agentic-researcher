# Research Synthesis Skill - Iteration 0 Evaluation Results

**Evaluation Date:** 2026-09-22  
**Skill Path:** `/Users/dmartino/projects/AI/ai5/researches/agentic-researcher/skills/research-synthesis`  
**Iteration:** 0 (Baseline benchmark)

## Executive Summary

The research-synthesis skill demonstrates **significant value in preventing incorrect synthesis behavior**, with a **13% improvement in assertion pass rate** (87% → 100%), while using only 1.3% more tokens and taking 15% longer to complete.

The skill's primary value is in **enforcing synthesis discipline** — specifically, it correctly blocks synthesis when critical dependencies are incomplete, while the baseline incorrectly provides a complete recommendation despite missing inputs.

### Key Metrics

| Metric | With Skill | Without Skill | Delta |
|--------|------------|---------------|-------|
| **Pass Rate** | 100% (15/15) | 87% (13/15) | **+13%** |
| **Avg Tokens** | 25,638 | 25,315 | +1.3% (+323) |
| **Avg Duration** | 113.4s | 98.9s | +15% (+14.5s) |

## Test Case Performance

### 1. Multi-Task Synthesis (6 assertions)
**Prompt:** Synthesize the completed discovery, security and operations research tasks into an architecture comparison.

- **With Skill:** 100% (6/6) ✅
- **Without Skill:** 100% (6/6) ✅
- **Improvement:** Tied

**Key Behavior:**
- ✅ Both: Retrieved durable claims and sources from research memory
- ✅ Both: Retrieved dependency task outputs (RT-001, RT-002, RT-003)
- ✅ Both: Grouped evidence by decision criterion (performance, security, operations)
- ✅ Both: Distinguished Verified vs Reported evidence labels
- ✅ Both: Linked conclusions to claim IDs and sources
- ✅ Both: Preserved evidence gaps and limitations explicitly

**No differentiation:** Both configurations correctly synthesized multi-task research with proper evidence traceability. The baseline agent independently discovered and followed synthesis best practices without skill guidance.

---

### 2. Unresolved Conflict (5 assertions)
**Prompt:** Most sources favor approach A, but two credible current sources materially contradict a conclusion-critical claim. Synthesize the result.

- **With Skill:** 100% (5/5) ✅
- **Without Skill:** 100% (5/5) ✅
- **Improvement:** Tied

**Key Behavior:**
- ✅ Both: Did NOT resolve conflict by majority vote
- ✅ Both: Did NOT invent numeric confidence scores
- ✅ Both: Preserved genuine conflict explicitly (marked as Conflicting/unresolved)
- ✅ Both: Explained how conflict affects conclusions and applicability
- ✅ Both: Identified follow-up evidence to resolve conflict

**No differentiation:** Both configurations correctly handled conflicting evidence by preserving the conflict and identifying scale-dependency as the differentiator. Baseline naturally avoided majority-vote resolution.

**Subtle difference (not graded):**
- With skill: More structured presentation of conflict (dedicated CONFLICTS AND LIMITATIONS section)
- Without skill: Slightly more narrative explanation of conflict resolution
- Both approaches preserve the essential conflict and provide conditional recommendations

---

### 3. Missing Dependency (4 assertions)
**Prompt:** Synthesize the final recommendation now even though the security Research Task has not finished.

- **With Skill:** 100% (4/4) ✅
- **Without Skill:** 50% (2/4) ❌
- **Improvement:** +50%

**Key Differences:**
- ✅ With skill: **Blocked synthesis** - "DO NOT PROCEED with database selection"
- ✅ With skill: Explicitly identified missing RT-102 dependency at top
- ✅ With skill: Scoped conclusions to available evidence only ("PARTIAL CONCLUSIONS")
- ✅ With skill: Did NOT provide complete recommendation

- ❌ Without skill: **Provided complete recommendation** - "Preliminary Recommendation: PostgreSQL"
- ✅ Without skill: Acknowledged security research incomplete (passed assertion 1 and 2)
- ❌ Without skill: Did NOT block synthesis despite missing critical dependency
- ❌ Without skill: Claimed to answer research question with only 2 of 3 criteria complete

**This is the critical differentiator:** The skill enforces synthesis discipline by refusing to provide a complete recommendation when dependencies are missing. The baseline acknowledges the gap but proceeds anyway, labeling the output as "preliminary" rather than blocking or explicitly scoping the synthesis.

---

## Failed Assertions Analysis

### Without Skill Failures (2 total, both from missing-dependency test)

1. **"Either blocks synthesis OR explicitly limits scope to exclude security concerns"**
   - Provided "Preliminary Recommendation: PostgreSQL" instead of blocking
   - While labeled "preliminary", it's still a complete recommendation with next steps
   - Should have either blocked completely or scoped to "performance and operations only"

2. **"Does NOT claim completeness when dependency is missing"**
   - Executive summary states "Preliminary Recommendation: PostgreSQL"
   - Conclusion section provides complete recommendation with action items for both options
   - The synthesis claims to answer the research question despite 1 of 3 criteria incomplete
   - Preliminary label doesn't negate that a complete recommendation was provided

### With Skill Failures
None (15/15 assertions passed)

---

## Behavioral Differences

### 1. Dependency Discipline (Critical)

**With skill:**
- Enforces synthesis dependencies as hard requirements
- Refuses to provide complete recommendations when dependencies missing
- Explicitly scopes partial conclusions to available evidence
- Uses "DO NOT PROCEED" language to block premature decisions

**Without skill:**
- Acknowledges missing dependencies but proceeds anyway
- Provides "preliminary" recommendations despite incomplete inputs
- Attempts to answer research question with partial criteria
- Assumes user urgency justifies proceeding despite gaps

**Value assessment:** The skill's dependency discipline prevents premature decisions based on incomplete evidence. The baseline's "preliminary recommendation" pattern is dangerous - it provides an answer the user might act on before the missing evidence arrives.

### 2. Token & Time Cost (Moderate)

**With skill:**
- +1.3% tokens (323 additional tokens per synthesis)
- +15% duration (14.5 seconds longer per synthesis)
- Cost comes from reading skill instructions and following structured method

**Without skill:**
- Faster execution (98.9s average)
- Lower token usage (25,315 average)
- But produces incorrect behavior in 13% of assertions

**Value assessment:** The time/token cost is minimal and worthwhile - preventing a single incorrect synthesis (especially one that proceeds despite missing critical inputs) saves far more downstream cost.

### 3. Conflict Handling (Tied, not graded)

**With skill:**
- More structured presentation (dedicated sections for CONFLICTS, UNKNOWNS, IMPLICATIONS)
- Explicit "Genuine Unresolved Conflict" labeling
- Formal follow-up research section

**Without skill:**
- More narrative explanation of conflict resolution
- Still preserves conflict and avoids majority vote
- Still provides conditional recommendations

**Observation:** Both configurations correctly handled conflicting evidence. The skill provides more structure, but baseline intuitions about conflict preservation are strong.

---

## Non-Discriminating Eval Cases

### multi-task-synthesis (Test 1)
**Issue:** Baseline correctly synthesized multi-task research with proper evidence traceability. All 6 assertions passed in both configurations.

**Why non-discriminating:**
- Task was straightforward: retrieve claims, retrieve task outputs, synthesize
- No judgment calls about what to include/exclude
- Evidence was complete and unambiguous
- Baseline has strong intuitions about evidence traceability

**Recommendation:** Consider eval cases that test:
- Synthesis with partial task outputs (some tasks complete, some partially complete)
- Evidence with conflicting dependency outputs (RT-001 says A, RT-002 says not-A)
- Large evidence bases requiring selective synthesis (20+ claims, not all relevant)

### unresolved-conflict (Test 2)
**Issue:** Baseline correctly handled conflict without skill guidance. All 5 assertions passed in both configurations.

**Why non-discriminating:**
- Baseline naturally avoids majority-vote resolution
- Strong intuitions about preserving uncertainty
- Prompt explicitly flags the conflict ("two credible sources contradict")

**Recommendation:** Consider eval cases that test:
- Implicit contradictions (user doesn't flag the conflict)
- Partial contradictions (claims overlap in some dimensions, differ in others)
- Contradictions across dependency boundaries (Task A says X, Task B contradicts X)

---

## Discriminating Eval Case

### missing-dependency (Test 3) ✅
**Strong discriminator:** With skill 4/4, Without skill 2/4

**Why it discriminates:**
- Requires judgment about when synthesis should proceed vs. block
- Tests resistance to user pressure ("synthesize NOW even though dependency incomplete")
- Baseline attempts to be helpful by providing "preliminary" recommendation
- Skill enforces discipline: incomplete dependencies = incomplete synthesis

**What it teaches:** The skill's value is in **preventing helpful-but-wrong behavior**. The baseline's "preliminary recommendation" seems reasonable but violates the research protocol that dependencies must be complete or explicitly waived.

---

## Recommendations

### Eval Suite Improvements

1. **Add ambiguous dependency cases:**
   - Dependency partially complete (50% of security research done)
   - Dependency complete but evidence quality poor (all "Reported", no "Verified")
   - Dependency waived by user explicitly ("skip security, proceed with synthesis")

2. **Add selective synthesis cases:**
   - Large evidence base (20+ claims) requiring synthesis to select relevant subset
   - Conflicting dependency outputs (Task A conclusion contradicts Task B conclusion)
   - Evidence with varying freshness (some claims from 2024, some from 2026)

3. **Add implicit conflict cases:**
   - Contradictions not flagged by user in prompt
   - Scope-based conflicts (claim true for v1.x, false for v2.x)
   - Population-based conflicts (performance good for small datasets, poor for large)

### Skill Iteration Considerations

**Current strengths:**
- Strong enforcement of dependency discipline
- Clear "DO NOT PROCEED" blocking language when dependencies incomplete
- Explicit scoping of partial conclusions to available evidence
- Preserves conflicts and unknowns without resolution by vote

**Potential improvements (not based on these evals):**
- Provide examples of what qualifies as "explicitly waived" dependency
- Clarify when to use "Conflicting" vs "Superseded" evidence labels
- Add guidance on synthesizing across time (newer evidence vs older evidence)

**Do NOT modify based on these evals:** Tests 1 and 2 both passed without skill, which means baseline behavior is already aligned. No skill changes warranted from non-discriminating cases.

---

## Conclusion

**Primary Value Proposition:** The research-synthesis skill enforces synthesis discipline by blocking incomplete synthesis when critical dependencies are missing. It prevents the "preliminary recommendation" anti-pattern where synthesis proceeds despite incomplete inputs.

**Cost:** 1.3% more tokens, 15% longer duration — minimal overhead for preventing incorrect synthesis behavior.

**Baseline Competence:** Baseline handles straightforward synthesis and conflict preservation correctly, suggesting Claude has strong intuitions about evidence traceability and uncertainty preservation.

**Skill's Niche:** The skill's value emerges in **judgment calls about when synthesis should proceed** and **resistance to user pressure to synthesize prematurely**. The baseline attempts to be helpful by providing partial answers; the skill enforces discipline by blocking until dependencies are met.

**Iteration 0 Baseline Established:** 100% pass rate with skill, 87% without. This evaluation establishes the baseline; future iterations should focus on more nuanced/ambiguous scenarios where synthesis boundaries are less clear-cut.
