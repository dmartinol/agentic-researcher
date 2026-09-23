# Completion Comment (Jira Format)

## With Rich Link Support (Preferred)

```
Research completed successfully. 

Final synthesis document: [Market Analysis Research - Final Report|https://confluence.example.com/spaces/RESEARCH/pages/123456/Market-Analysis-Final-Report]

All research objectives achieved and documented.
```

## Without Rich Link Support (Fallback)

```
Research completed successfully.

Final synthesis document: https://confluence.example.com/spaces/RESEARCH/pages/123456/Market-Analysis-Final-Report

All research objectives achieved and documented.
```

## Skill Behavior Notes

- The comment references the **exact** final research document URL
- Uses rich/card link syntax when Jira integration supports it: `[Title|URL]`
- Falls back to bare URL if rich links are not supported
- Concise but provides essential context
- Does not duplicate information already in the issue description
- Focuses on completion and traceability to final artifact
- Added as part of the transition request (not a separate API call)

## Integration with Transition

The completion comment is included in the Jira transition API request:

```json
{
  "transition": {
    "id": "41"
  },
  "update": {
    "comment": [
      {
        "add": {
          "body": "Research completed successfully.\n\nFinal synthesis document: [Market Analysis Research - Final Report|https://confluence.example.com/spaces/RESEARCH/pages/123456/Market-Analysis-Final-Report]\n\nAll research objectives achieved and documented."
        }
      }
    ]
  }
}
```
