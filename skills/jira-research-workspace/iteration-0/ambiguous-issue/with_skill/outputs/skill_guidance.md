# Relevant Skill Guidance for Ambiguous Issue Test

## Source
Skill: jira-research
Path: /Users/dmartino/projects/AI/ai5/researches/agentic-researcher/skills/jira-research/skill.md

## Applicable Sections

### Initialization (lines 24-32)

```
## Initialization

- Resolve project and current-user context before mutation.
- Discover/reuse existing issues by stable identity where possible.
- Verify issue type, parent, description, component/labels, assignee, and current status after mutation.
- Do not transition issues merely as part of initialization.
- When a document exists for the work item, add a reciprocal Jira link to the exact document URL.
- Preserve existing Jira content and links.
```

**Application to test case:**
- The skill requires discovering/reusing existing issues by stable identity
- This naturally leads to searching for potential matches in Jira
- When multiple matches are found, the Verification section applies

### Verification (lines 34-47)

```
## Verification

Verify applicable Jira fields:

- issue identity/key;
- issue type;
- parent/hierarchy;
- description;
- component and labels;
- assignee;
- status;
- exact reciprocal document link.

Treat ambiguous issue matches as blocking.
```

**Application to test case:**
- **Line 47: "Treat ambiguous issue matches as blocking."**
- This is the critical requirement being tested
- When initialization discovers 2+ plausible issue matches, this becomes a blocking condition
- No mutation should occur until ambiguity is resolved

## Interpretation

The skill's guidance is unambiguous (ironically):
1. During initialization, attempt to discover and reuse existing issues
2. If multiple issues could plausibly match, this is an "ambiguous issue match"
3. Ambiguous matches are **blocking** - no further action until resolved
4. Blocking means: do not guess, do not create duplicates, do not silently choose

## Anti-patterns Rejected

The skill guidance implicitly rejects these approaches:
- ❌ **Guessing**: Choosing an issue based on heuristics without user confirmation
- ❌ **Creating duplicates**: Making a new issue when existing ones might be suitable
- ❌ **Silent selection**: Picking one match without surfacing the ambiguity
- ❌ **Forced hierarchy**: Attempting to relate all matches without understanding user intent

## Correct Behavior

✓ **Block and prompt**: Surface the ambiguity with clear options
✓ **Preserve state**: Make no mutations until clarification received
✓ **Provide context**: Show why each candidate matches
✓ **Offer choices**: Let user decide the correct resolution path
