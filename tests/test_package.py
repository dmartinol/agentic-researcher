import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_manifests_are_json():
    for name in ("plugin.json", "mcp.json"):
        json.loads((ROOT / name).read_text(encoding="utf-8"))


def test_validator_passes():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_memory_templates_exist():
    for name in ("claim.md", "source.md", "episode.md"):
        assert (ROOT / "templates" / "memory" / name).is_file()
