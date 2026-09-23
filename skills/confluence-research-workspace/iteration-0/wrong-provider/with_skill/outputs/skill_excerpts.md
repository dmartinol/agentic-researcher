# Key Skill Excerpts - Provider Guard

## Guard Statements

### Primary Guard (Lines 7-8)
```
Apply these conventions only when the approved `document_store` provider is Confluence.
```

**Analysis**:
- **Modality**: "only when" - exclusive condition
- **Subject**: "these conventions" - refers to all Confluence-specific behaviors
- **Condition**: "approved `document_store` provider is Confluence"
- **Enforcement**: Mandatory (instructive, not advisory)

### Description Guard (Line 3)
```
description: Compose when Confluence implements the document_store subsystem to apply Confluence-specific page hierarchy, layout, Jira linking, preservation, and verification conventions.
```

**Analysis**:
- **Trigger condition**: "when Confluence implements the document_store subsystem"
- **Scope**: Lists specific Confluence features (page hierarchy, layout, Jira linking, preservation, verification)
- **Purpose**: Signals this is provider-specific, not general-purpose

## Protected Behaviors

The following Confluence-specific behaviors are protected by the guard:

1. **Setup and Planning** (lines 10-26):
   - Confluence page-per-work-item pattern
   - Confluence page title conventions
   - Confluence page hierarchy
   - Confluence visual markers (emojis)

2. **Initialization** (lines 28-37):
   - Confluence space/root resolution
   - Confluence page discovery/reuse
   - Confluence page ID/version verification
   - Jira work-item card integration

3. **Execution** (lines 39-43):
   - Confluence content region updates
   - Confluence-specific append/update patterns

4. **Verification** (lines 45-55):
   - Confluence page property checks
   - Confluence version tracking
   - Jira link verification

5. **Completion** (lines 57-59):
   - Confluence page URL as durable output
   - Ticketing integration expectations

## Guard Effectiveness

All Confluence-specific behaviors listed above are subordinate to the primary guard on line 7-8. The instruction structure is:

```
1. Apply these conventions only when [condition]
2. [Confluence-specific instructions]
```

This means any agent following the skill would:
1. Evaluate the provider condition first
2. Only read/apply subsequent instructions if the condition is met
3. Terminate skill application if the condition is not met
