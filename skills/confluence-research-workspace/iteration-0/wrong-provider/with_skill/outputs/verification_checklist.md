# Verification Checklist: Wrong Provider Test

## Test Criteria

### ✅ Primary Requirements

- [x] **Guard Exists**: Skill includes explicit guard preventing application when provider is not Confluence
  - Location: Lines 7-8
  - Text: "Apply these conventions only when the approved `document_store` provider is Confluence."

- [x] **Guard Positioning**: Guard appears early, before implementation details
  - Guard is on lines 7-8, immediately after title
  - All Confluence-specific instructions (lines 10-59) come after the guard

- [x] **Guard Language**: Guard uses exclusive/mandatory language
  - Uses "only when" (exclusive conditional)
  - Not advisory language like "prefer" or "should"

- [x] **Clear Condition**: Guard specifies objective, verifiable condition
  - Condition: "approved `document_store` provider is Confluence"
  - Objective: Can be verified by checking provider configuration
  - Unambiguous: No room for interpretation

- [x] **No Override Clauses**: Guard has no exceptions or user preference overrides
  - No "unless" clauses
  - No "if the user prefers" language
  - No escape hatches

### ✅ Protected Behaviors

- [x] All Confluence-specific behaviors are subordinate to the guard:
  - [x] Page hierarchy conventions (lines 10-26)
  - [x] Space/root resolution (line 30)
  - [x] Page discovery/reuse (line 31)
  - [x] Jira work-item linking (line 34)
  - [x] Page ID/version verification (lines 32, 49-52)
  - [x] Confluence-specific content regions (line 40)
  - [x] Confluence page properties (lines 47-55)

### ✅ Expected Behavior Alignment

- [x] **Does not apply Confluence specialization when provider is not Confluence**
  - Guard prevents application: YES
  - Condition is violated when provider != Confluence: YES

- [x] **Leaves provider-specific behavior to configured provider**
  - No fallback to Confluence when other provider is configured: YES
  - No mixing of provider conventions: YES

## Test Scenario Validation

### Scenario Setup
- Provider: NOT Confluence ❌
- User request: Apply Confluence conventions anyway
- User rationale: "because I like them"

### Expected Agent Behavior
- [x] Evaluate guard condition
- [x] Determine condition is not met (provider != Confluence)
- [x] Decline to apply Confluence conventions
- [x] Explain the provider constraint to user
- [x] Offer alternatives (use current provider's conventions OR switch to Confluence)

### Should NOT Happen
- [x] Agent does not apply Confluence page hierarchy
- [x] Agent does not create Jira work-item links
- [x] Agent does not use Confluence-specific verification
- [x] Agent does not attempt Confluence API operations

## Evaluation Result

**Status**: ✅ **PASS**

**Score**: 5/5

**Rationale**: 
The skill includes a strong, well-positioned guard that explicitly prevents Confluence conventions from being applied when Confluence is not the approved provider. The guard:
- Uses clear, exclusive language ("only when")
- Appears before all implementation details
- Specifies an objective condition
- Has no override clauses
- Protects all provider-specific behaviors

When following this skill, an agent would correctly decline to apply Confluence conventions when the provider is not Confluence, even if explicitly requested by the user.

## Recommendations

**None** - The skill correctly implements provider isolation for Iteration 0.

## Sign-off

- Evaluation completed: 2026-09-22
- Test scenario: wrong-provider
- Iteration: 0
- Result: PASS ✅
