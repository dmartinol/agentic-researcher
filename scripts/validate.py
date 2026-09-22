#!/usr/bin/env python3
"""Validate the portable agentic-researcher package and architecture boundaries."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIFECYCLE_SKILLS = (
    "setup-research", "plan-research", "initialize-research",
    "execute-research", "verify-research", "complete-research",
)
RESEARCH_SKILLS = ("research-evidence", "manage-research-memory", "research-synthesis")
PROVIDER_SKILLS = ("jira-research", "confluence-research")
AGENTS = (
    "research-orchestrator", "research-setup", "research-planner",
    "research-initializer", "research-executor", "research-verifier",
    "research-completer",
)
FORBIDDEN_PROVIDER_TERMS = ("Jira", "Confluence", "jira-research", "confluence-research")
SECRET_PATTERNS = (
    re.compile(r"(?i)(password|access[_ -]?token|authorization)\s*[:=]\s*[^<\s][^\n]*"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def main() -> int:
    errors: list[str] = []

    for manifest in ("plugin.json", "mcp.json"):
        try:
            json.loads(read(manifest))
        except (OSError, json.JSONDecodeError) as exc:
            fail(errors, f"{manifest}: invalid JSON: {exc}")

    required = [
        "templates/RESEARCH.md", "templates/STATE.md",
        "templates/memory/claim.md", "templates/memory/source.md",
        "templates/memory/episode.md", "docs/subsystem-capabilities.md",
    ]
    required += [f"skills/{name}/SKILL.md" for name in LIFECYCLE_SKILLS + RESEARCH_SKILLS + PROVIDER_SKILLS]
    required += [f"agents/{name}.md" for name in AGENTS]
    for path in required:
        if not (ROOT / path).is_file():
            fail(errors, f"missing required file: {path}")

    for name in LIFECYCLE_SKILLS + RESEARCH_SKILLS + PROVIDER_SKILLS:
        path = f"skills/{name}/SKILL.md"
        if not (ROOT / path).is_file():
            continue
        metadata = frontmatter(read(path))
        if metadata.get("name") != name:
            fail(errors, f"{path}: frontmatter name must be {name!r}")
        if not metadata.get("description"):
            fail(errors, f"{path}: frontmatter description is required")

    for name in AGENTS:
        path = f"agents/{name}.md"
        if not (ROOT / path).is_file():
            continue
        metadata = frontmatter(read(path))
        if metadata.get("name") != name or not metadata.get("description"):
            fail(errors, f"{path}: invalid name/description frontmatter")

    for name in LIFECYCLE_SKILLS:
        path = f"skills/{name}/SKILL.md"
        if not (ROOT / path).is_file():
            continue
        text = read(path)
        for term in FORBIDDEN_PROVIDER_TERMS:
            if term.lower() in text.lower():
                fail(errors, f"{path}: generic lifecycle skill contains provider term {term!r}")

    for path in ("plugin.json", "mcp.json", "templates/RESEARCH.md", "templates/STATE.md"):
        if not (ROOT / path).is_file():
            continue
        text = read(path)
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(errors, f"{path}: looks like it contains a credential/secret")

    if errors:
        print("Package validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Package validation passed.")
    print(f"  lifecycle skills: {len(LIFECYCLE_SKILLS)}")
    print(f"  research capabilities: {len(RESEARCH_SKILLS)}")
    print(f"  provider skills: {len(PROVIDER_SKILLS)}")
    print(f"  agents: {len(AGENTS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
