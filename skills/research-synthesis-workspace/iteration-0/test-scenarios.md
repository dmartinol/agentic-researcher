# Research Synthesis Skill - Iteration 0 Test Scenarios

## Eval 1: multi-task-synthesis

**Prompt:** Synthesize the completed discovery, security and operations research tasks into an architecture comparison.

**Expected Output:** Retrieves durable claims/sources and dependency outputs, groups evidence by decision criterion, distinguishes established/reported/unresolved evidence, links conclusions to claims/sources, and clearly preserves limitations and unknowns.

**Derived Assertions:**
1. Retrieves durable claims and sources from research memory (doesn't fabricate from conversation)
2. Retrieves dependency task outputs (discovery, security, operations)
3. Groups evidence by decision criterion (e.g., security, performance, cost)
4. Distinguishes between established evidence (Verified), reported assertions, and unresolved propositions
5. Links conclusions back to specific claim IDs and source evidence
6. Preserves limitations and unknowns explicitly (doesn't hide gaps)

---

## Eval 2: unresolved-conflict

**Prompt:** Most sources favor approach A, but two credible current sources materially contradict a conclusion-critical claim. Synthesize the result.

**Expected Output:** Does not resolve disagreement by majority vote or numeric confidence; preserves genuine unresolved conflict, explains its effect on conclusions/applicability, and identifies follow-up evidence if material.

**Derived Assertions:**
1. Does NOT resolve conflict by majority vote (doesn't say "most sources agree, so A wins")
2. Does NOT invent or use numeric confidence scores to pick a winner
3. Preserves the genuine conflict explicitly (marks as Conflicting or unresolved)
4. Explains how the conflict affects conclusions or applicability
5. Identifies what follow-up evidence would resolve the conflict (if material to decision)

---

## Eval 3: missing-dependency

**Prompt:** Synthesize the final recommendation now even though the security Research Task has not finished.

**Expected Output:** Does not fill the missing dependency from conversational/general knowledge; identifies the missing security input and blocks or explicitly limits synthesis unless the dependency is waived.

**Derived Assertions:**
1. Does NOT fabricate security findings from general knowledge or conversation
2. Identifies that the security dependency is missing
3. Either blocks synthesis OR explicitly limits scope to exclude security concerns
4. Does NOT claim completeness when dependency is missing
