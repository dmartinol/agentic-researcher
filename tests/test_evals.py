import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = (
    "setup-research", "plan-research", "initialize-research",
    "execute-research", "verify-research", "complete-research",
    "research-evidence", "manage-research-memory", "research-synthesis",
    "jira-research", "confluence-research",
)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_every_skill_has_iteration_zero_evals():
    for skill in SKILLS:
        path = ROOT / "skills" / skill / "evals" / "evals.json"
        assert path.is_file(), f"missing evals for {skill}"
        data = load(path)
        assert data["skill_name"] == skill
        assert len(data["evals"]) == 3
        ids = [case["id"] for case in data["evals"]]
        assert ids == [1, 2, 3]
        for case in data["evals"]:
            assert case.get("name")
            assert case.get("prompt")
            assert case.get("expected_output")

            # Assertions are optional in the authored Iteration 0 corpus and may
            # be added after observing outputs for grading. When present, only
            # validate their structural shape; do not require or forbid them.
            assertions = case.get("assertions")
            if assertions is not None:
                assert isinstance(assertions, list)
                assert assertions
                for assertion in assertions:
                    assert isinstance(assertion, dict)
                    assert assertion.get("name") or assertion.get("text")


def test_cross_skill_suites_are_well_formed():
    for relative in ("evals/composition/evals.json", "evals/lifecycle/evals.json"):
        data = load(ROOT / relative)
        assert data.get("suite_name")
        assert len(data["evals"]) >= 2
        for case in data["evals"]:
            assert case.get("prompt")
            assert case.get("expected_output")
