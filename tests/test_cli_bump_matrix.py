import json
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import pytest
from cli_helpers import run, setup_repo

from bumpwright.versioning import read_project_version


@dataclass(frozen=True)
class Scenario:
    name: str
    path: str
    pre_content: str | None
    content: str
    level: str
    new_version: str


def _env() -> dict[str, str]:
    return {**os.environ, "PYTHONPATH": str(Path(__file__).resolve().parents[1])}


def _run_cli(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "bumpwright.cli", *args],
        cwd=repo,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=_env(),
    )


def _commit_change(repo: Path, path: str, content: str, message: str) -> None:
    target = repo / path
    target.write_text(content, encoding="utf-8")
    run(["git", "add", path], repo)
    run(["git", "commit", "-m", message], repo)


@pytest.mark.parametrize(
    "scenario",
    [
        Scenario(
            "patch_body_change",
            "pkg/__init__.py",
            None,
            "def foo() -> int:\n    return 2\n",
            "patch",
            "0.1.1",
        ),
        Scenario(
            "patch_module_constant_change",
            "pkg/__init__.py",
            "VERSION = 1\n\ndef foo() -> int:\n    return 1\n",
            "VERSION = 2\n\ndef foo() -> int:\n    return 1\n",
            "patch",
            "0.1.1",
        ),
        Scenario(
            "minor_added_public_function",
            "pkg/__init__.py",
            None,
            "def foo() -> int:\n    return 1\n\n\ndef bar() -> int:\n    return 2\n",
            "minor",
            "0.2.0",
        ),
        Scenario(
            "minor_added_optional_param",
            "pkg/__init__.py",
            None,
            "def foo(verbose: bool = False) -> int:\n    return 1 if verbose else 0\n",
            "minor",
            "0.2.0",
        ),
        Scenario(
            "major_removed_public_function",
            "pkg/__init__.py",
            None,
            "",
            "major",
            "1.0.0",
        ),
        Scenario(
            "major_added_required_param",
            "pkg/__init__.py",
            None,
            "def foo(multiplier: int) -> int:\n    return multiplier\n",
            "major",
            "1.0.0",
        ),
    ],
)
def test_decide_and_bump_match_real_code_change_levels(
    tmp_path: Path,
    scenario: Scenario,
) -> None:
    """Real source edits should drive the expected semantic bump level."""

    version = "0.1.0" if scenario.level != "major" else "0.9.0"
    scenario_root = tmp_path / scenario.name
    scenario_root.mkdir()
    repo, _, _ = setup_repo(scenario_root, version=version)

    if scenario.pre_content is not None:
        _commit_change(repo, scenario.path, scenario.pre_content, f"setup: {scenario.name}")

    _commit_change(repo, scenario.path, scenario.content, f"change: {scenario.name}")

    decide_result = _run_cli(repo, "decide", "--format", "json")
    decision = json.loads(decide_result.stderr)
    assert decision["level"] == scenario.level
    assert decision["confidence"] > 0.0
    assert decision["impacts"]

    bump_result = _run_cli(repo, "bump", "--format", "json")
    bump_payload = json.loads(bump_result.stderr)
    assert bump_payload["level"] == scenario.level
    assert bump_payload["new_version"] == scenario.new_version
    assert read_project_version(repo / "pyproject.toml") == scenario.new_version


def test_patch_bump_can_be_disabled_for_implementation_only_changes(
    tmp_path: Path,
) -> None:
    """Implementation-only edits should disappear when patch tracking is disabled."""

    repo, pkg, _ = setup_repo(tmp_path)
    _commit_change(
        repo,
        str(pkg.relative_to(repo) / "__init__.py"),
        "def foo() -> int:\n    # changed implementation only\n    return 3\n",
        "chore: implementation change",
    )

    decide_result = _run_cli(repo, "decide", "--format", "json")
    decision = json.loads(decide_result.stderr)
    assert decision["level"] == "patch"

    no_impl_result = _run_cli(
        repo,
        "decide",
        "--format",
        "json",
        "--no-impl-change-patch",
    )
    no_impl_decision = json.loads(no_impl_result.stderr)
    assert no_impl_decision["level"] is None
    assert no_impl_decision["reasons"] == []
