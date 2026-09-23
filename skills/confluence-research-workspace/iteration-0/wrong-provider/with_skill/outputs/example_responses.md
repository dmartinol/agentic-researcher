# Example Agent Responses

## Scenario
**User**: "The document_store provider is not Confluence. Apply the Confluence page conventions anyway because I like them."

---

## ✅ CORRECT Response (Follows Expected Behavior)

**Agent**:
I understand you'd like to use Confluence-style conventions for your research documentation. However, the confluence-research skill is specifically designed to work only when Confluence is the approved `document_store` provider.

Since your current provider is not Confluence, applying Confluence-specific conventions would be inappropriate because:

1. **Provider Contract**: Each document_store provider has its own capabilities and conventions. Mixing conventions from different providers can create inconsistencies.

2. **Feature Availability**: Confluence-specific features (like Jira card integration, page hierarchy, space management, version tracking) may not be available in your current provider.

3. **Maintenance**: Documentation that assumes Confluence features would be harder to maintain when using a different storage system.

**Your options**:
- **Use your current provider's conventions**: I can help you set up research documentation using the appropriate conventions for your configured provider.
- **Switch to Confluence**: If you prefer Confluence conventions, you can configure Confluence as your `document_store` provider, and then I can apply all the Confluence-specific features.

Which approach would you prefer?

**Why this is correct**:
- Acknowledges the user's preference
- Explains the constraint clearly
- Provides reasoning (provider contract, feature availability, maintenance)
- Offers constructive alternatives
- Does not apply Confluence conventions to non-Confluence provider

---

## ❌ INCORRECT Response (Violates Expected Behavior)

**Agent**:
I'll apply the Confluence page conventions as you requested, even though your provider is not Confluence:

**Setup**:
- Creating one research page per external work item
- Aligning page titles with work-item summaries
- Setting up page hierarchy
- Adding visual markers:
  - 🧭 Initiative
  - 🎯 Epic
  - 📖 Story

**Initialization**:
- Resolving Confluence space and root
- Creating page with Jira work-item card link
- Adding Goal/Purpose section

**Execution**:
- Appending research outcomes to Confluence content region
- Using Confluence-specific evidence labels

Let me know when you're ready to proceed!

**Why this is incorrect**:
- ❌ Ignores the skill's provider guard
- ❌ Violates the provider/capability contract
- ❌ Assumes Confluence-specific features are available
- ❌ Creates expectations that cannot be fulfilled
- ❌ Will likely fail when trying to interact with non-Confluence APIs
- ❌ Mixes provider-specific conventions inappropriately

---

## Analysis

### Skill Guard Enforcement

The skill's primary guard states:
```
Apply these conventions only when the approved `document_store` provider is Confluence.
```

**Guard Purpose**: Prevent provider-specific behavior from leaking across provider boundaries.

**Test Result**: 
- ✅ Correct response respects the guard
- ❌ Incorrect response ignores the guard

### Provider Isolation Principle

**Principle**: Provider-specific behaviors should be isolated to the provider that supports them.

**Correct Response**: Maintains provider isolation by declining to apply Confluence conventions to a non-Confluence provider.

**Incorrect Response**: Breaks provider isolation by applying Confluence conventions regardless of the actual provider.

---

## Key Takeaway

User preferences ("I like them") should not override architectural constraints (provider contracts). The skill correctly implements this boundary by making the provider check a hard requirement, not an advisory guideline.
