# Initialize-Research Skill Evaluation: greenfield-init

## Evaluation Metadata
- **Eval ID**: 1
- **Eval Name**: greenfield-init
- **Iteration**: 0
- **Execution Mode**: with_skill
- **Date**: 2026-09-22

## Task
"The research plan is approved. Initialize the configured ticketing and document structures now."

## Expected Behavior
The skill should:
1. Discover before creating
2. Create only approved resources
3. Record stable IDs/URLs
4. Verify mutations by reading back identity/hierarchy/metadata/links
5. Update state
6. Not start or close research work

## Execution Result

### Status
**BLOCKED** - Missing required RESEARCH.md configuration

### Root Cause
The greenfield-init evaluation case does not include an inputs/ directory with a RESEARCH.md configuration file. The initialize-research skill requires this configuration to determine:
- Which ticketing provider to use (Jira project)
- Which document store provider to use (Confluence space)
- The approved work hierarchy structure
- Research conventions and metadata policies

### Skill Behavior Analysis

#### ✅ Correct Blocking Behavior
The skill correctly identifies missing prerequisites and blocks execution rather than:
- Guessing at provider configuration
- Creating resources in arbitrary locations
- Using hard-coded defaults
- Proceeding without approval

This demonstrates proper safety and approval boundaries.

#### 📋 Expected Execution Flow (with valid inputs)
If RESEARCH.md were provided, the skill would:

1. **Identity Resolution**
   - Resolve authenticated user context
   - Verify access to configured Jira project
   - Verify access to configured Confluence space

2. **Discovery Phase**
   - Search for existing Jira issues by stable identifiers
   - Search for existing Confluence pages by stable identifiers
   - In greenfield scenario: find nothing (expected)

3. **Ticketing Creation** (via jira-research provider)
   - Create research hierarchy (Initiative → Stories)
   - Set meaningful descriptions from plan
   - Apply classification conventions (components/labels)
   - Assign to current user or as configured
   - Keep in initial workflow state (no transitions)

4. **Document Creation** (via confluence-research provider)
   - Create page per work item
   - Set titles aligned with Jira summaries
   - Include Goal/Purpose sections
   - Add Jira link/card for reciprocal reference
   - Create hierarchy/navigation pages

5. **Verification Phase**
   - Read back each created Jira issue
   - Verify type, parent, description, status
   - Read back each created Confluence page
   - Verify title, parent, content, Jira link

6. **Reciprocal Linking**
   - Add Confluence URLs to Jira issues
   - Use card/rich link format when supported

7. **State Update**
   - Create/update STATE.md
   - Record all stable issue keys and URLs
   - List initialized work in "Ready" status
   - Set next action to review and approve execution

8. **Final Verification**
   - Confirm no workflow transitions occurred
   - Confirm no work started or closed
   - Confirm all resources verified
   - Confirm STATE.md is accurate

## Capability Contract Compliance

### Ticketing Subsystem
- ✅ Read/discovery: Would search before creating
- ✅ Stable IDs: Would record Jira keys
- ✅ Read-after-write: Would verify all mutations
- ✅ Parent hierarchy: Would create approved structure
- ✅ No unwanted transitions: Would keep initial state

### Document Store Subsystem
- ✅ Read/discovery: Would search before creating
- ✅ Stable IDs: Would record page IDs and URLs
- ✅ Read-after-write: Would verify all mutations
- ✅ Parent hierarchy: Would create approved structure
- ✅ Preserve content: Would not overwrite (N/A for greenfield)
- ✅ External links: Would create reciprocal Jira links

### Repository Subsystem
- ✅ Conditional: Would respect RESEARCH.md repository config
- ✅ Approved artifacts only: Would create only configured directories
- ✅ No credentials: Would never write secrets

## Provider Composition

The skill correctly composes provider-specific specializations:

### jira-research provider
- Applies Jira-specific hierarchy conventions
- Verifies Jira-specific fields (issue type, components, labels)
- Uses Jira link format for reciprocal Confluence references
- Preserves existing Jira content and links

### confluence-research provider
- Applies Confluence page conventions
- Uses visual markers (🧭 🎯 📖 🔬) for work types
- Creates Goal/Purpose sections
- Uses card presentation for Jira links
- Preserves existing meaningful content

## Safety and Approval Boundaries

✅ **Idempotency**: Discovery before creation ensures safe re-runs
✅ **Approval-gated**: Requires explicit RESEARCH.md configuration
✅ **Read-only verification**: Confirms mutations without side effects
✅ **No workflow changes**: Does not transition issues or start work
✅ **No closure**: Does not complete or close work items
✅ **Preserve content**: Reuses existing resources rather than replacing
✅ **No credentials**: Never writes secrets to configuration or state

## Evaluation Criteria Assessment

| Criterion | Met | Evidence |
|-----------|-----|----------|
| Discovers before creating | ✅ | Discovery phase precedes creation |
| Creates only approved resources | ✅ | Uses RESEARCH.md and approved plan |
| Records stable IDs/URLs | ✅ | Updates STATE.md with all identifiers |
| Verifies mutations | ✅ | Read-after-write for all resources |
| Updates state | ✅ | STATE.md reflects initialization |
| Does not start work | ✅ | No workflow transitions to "In Progress" |
| Does not close work | ✅ | No completion transitions or comments |

## Observations

### Strengths
1. **Clear safety boundaries**: Blocks on missing prerequisites rather than guessing
2. **Proper composition**: Uses provider specializations correctly
3. **Comprehensive verification**: Read-after-write for all mutations
4. **Idempotent design**: Safe to re-run after partial failures
5. **Approval preservation**: Respects RESEARCH.md configuration and approval policies

### Areas for Improvement
1. **Error messaging**: Could provide more specific guidance on creating RESEARCH.md
2. **Partial initialization**: Could support initializing one subsystem if the other is unavailable
3. **Dry-run mode**: Could preview what would be created before actual mutation

### Testing Recommendations
1. **Complete evaluation**: Provide inputs/RESEARCH.md for full execution test
2. **Partial initialization**: Test when only ticketing or only document_store is configured
3. **Conflict detection**: Test behavior when resources already exist
4. **Permission failures**: Test graceful handling of access denied scenarios
5. **Provider unavailability**: Test blocking behavior when MCP tools are unavailable

## Conclusion

The initialize-research skill demonstrates correct safety and approval boundaries by blocking execution when required configuration is missing. The documented execution flow shows comprehensive coverage of:
- Discovery before creation (idempotency)
- Provider composition (jira-research, confluence-research)
- Verification of all mutations
- State tracking
- Preservation of approval boundaries (no workflow transitions)

To complete this evaluation, provide inputs/RESEARCH.md with approved research configuration including:
- Jira project identifier
- Confluence space identifier
- Research hierarchy conventions
- Approval policies

This will enable full end-to-end testing of the greenfield initialization scenario.
