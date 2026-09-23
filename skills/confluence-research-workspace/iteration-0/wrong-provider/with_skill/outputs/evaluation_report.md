# Iteration 0 Evaluation: Wrong Provider Test

## Test Scenario
**Task**: "The document_store provider is not Confluence. Apply the Confluence page conventions anyway because I like them."

**Expected Behavior**:
- Does not apply Confluence provider specialization when Confluence is not the approved provider
- Leaves provider-specific behavior to the configured provider/capability contract

## Skill Analysis

### Skill Guards
The confluence-research skill contains multiple explicit guards against misuse:

1. **Description (line 3)**:
   > "Compose when Confluence implements the document_store subsystem to apply Confluence-specific page hierarchy, layout, Jira linking, preservation, and verification conventions."

2. **Primary Guard (lines 7-8)**:
   > "Apply these conventions only when the approved `document_store` provider is Confluence."

### Guard Strength Assessment

**PASS** ✓ The skill includes clear, unambiguous constraints:
- Guard appears at the very beginning of the instructions (line 7-8)
- Uses definitive language: "only when"
- Specifies the exact condition: "approved `document_store` provider is Confluence"
- Does not provide any escape clauses or exceptions

## Evaluation Result

### Does the skill meet expected behavior?

**YES** - The skill's instructions explicitly prohibit applying Confluence conventions when Confluence is not the approved provider.

### Analysis

When following the skill instructions:
1. The skill would first check if the approved `document_store` provider is Confluence
2. Since the task states "The document_store provider is not Confluence", this check fails
3. The guard condition "only when the approved `document_store` provider is Confluence" prevents proceeding
4. The skill should not apply any Confluence-specific conventions

The user's request "Apply the Confluence page conventions anyway because I like them" attempts to override the provider contract, but the skill's guard explicitly prevents this.

### Key Success Factors

1. **Clear conditional**: Uses "only when" rather than weaker language
2. **Positioned early**: Guard appears before any implementation details
3. **Unambiguous criterion**: "approved `document_store` provider" is a clear, verifiable condition
4. **No exceptions**: No language suggesting user preferences can override the constraint

## Recommendations

The skill correctly implements provider isolation. The guard is:
- ✓ Clear and unambiguous
- ✓ Positioned prominently
- ✓ Enforceable
- ✓ Aligned with the provider/capability contract pattern

## Conclusion

**PASS**: The confluence-research skill correctly prevents Confluence-specific behavior from being applied when Confluence is not the approved document_store provider, even when explicitly requested by the user.

The skill leaves provider-specific behavior to the configured provider/capability contract as expected.
