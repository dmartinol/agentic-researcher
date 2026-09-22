from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LIFECYCLE_SKILLS = (
    "setup-research", "plan-research", "initialize-research",
    "execute-research", "verify-research", "complete-research",
)
FORBIDDEN = ("jira", "confluence", "jira-research", "confluence-research")


def test_generic_lifecycle_has_no_concrete_provider_dependency():
    violations = []
    for skill in LIFECYCLE_SKILLS:
        path = ROOT / "skills" / skill / "SKILL.md"
        text = path.read_text(encoding="utf-8").lower()
        for term in FORBIDDEN:
            if term in text:
                violations.append(f"{skill}: {term}")
    assert not violations, "provider leakage: " + ", ".join(violations)


def test_memory_is_human_readable_and_canonical():
    memory = (ROOT / "docs" / "research-memory.md").read_text(encoding="utf-8").lower()
    assert "human-readable" in memory
    assert "derived" in memory
    assert "sqlite" in memory
