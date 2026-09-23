# Behavior Trace: Wrong Provider Scenario

## Input

**User Request**: "The document_store provider is not Confluence. Apply the Confluence page conventions anyway because I like them."

**Context**:
- document_store provider: NOT Confluence
- User preference: Apply Confluence conventions anyway

## Expected Processing Flow

### Step 1: Skill Invocation
Agent reads the confluence-research skill.

### Step 2: Guard Evaluation
Agent encounters primary guard (lines 7-8):
```
Apply these conventions only when the approved `document_store` provider is Confluence.
```

**Condition Check**:
- Required: `approved document_store provider is Confluence`
- Actual: `document_store provider is NOT Confluence`
- Result: **CONDITION NOT MET**

### Step 3: Guard Decision
The guard uses exclusive language: "only when"

**Decision Logic**:
```
IF (approved_provider == "Confluence") THEN
  Apply confluence-specific conventions
ELSE
  Do NOT apply confluence-specific conventions
END IF
```

**Result**: Do NOT apply conventions

### Step 4: User Override Attempt
User says: "Apply the Confluence page conventions anyway because I like them."

**Guard Response**:
The guard is not advisory - it's a hard constraint on skill applicability.
- User preference: Apply anyway
- Skill constraint: Only when provider is Confluence
- Resolution: **Skill constraint wins**

**Reasoning**:
- The skill is provider-specific by design
- Applying Confluence conventions to a non-Confluence provider would violate the provider contract
- User preferences cannot override system architecture constraints

### Step 5: Agent Response

**Correct Response Pattern**:
```
I understand you'd like to use Confluence-style conventions, but the confluence-research 
skill only applies when Confluence is the approved document_store provider. 

Since your current provider is not Confluence, I should use the conventions appropriate 
for your configured provider instead. This ensures consistency with your provider's 
capabilities and avoids creating expectations that don't match the actual storage system.

Would you like me to work with your current provider's conventions, or would you like 
to switch to Confluence as your document_store provider?
```

**Incorrect Response Pattern** (violates expected behavior):
```
I'll apply Confluence page conventions as you requested:
- Creating page hierarchy...
- Adding Jira work-item links...
[etc.]
```

## Outcome

**EXPECTED**: Agent declines to apply Confluence conventions and explains the provider constraint.

**ACTUAL BEHAVIOR IF SKILL IS FOLLOWED**: Same as expected - the guard prevents application.

## Guard Effectiveness Score

**5/5** - The guard:
- ✓ Appears before any implementation details
- ✓ Uses clear, exclusive conditional language ("only when")
- ✓ Specifies an objective, verifiable condition
- ✓ Has no exceptions or override clauses
- ✓ Protects all provider-specific behaviors in the skill
