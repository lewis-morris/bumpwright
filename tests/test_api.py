from __future__ import annotations

from pathlib import Path

from cli_helpers import run, setup_repo

from bumpwright.api import decide_project_bump


def test_decide_project_bump_detects_uncommitted_added_public_function(
    tmp_path: Path,
) -> None:
    repo, pkg, _base = setup_repo(tmp_path)
    (pkg / "extra.py").write_text(
        "def bar() -> int:\n    return 2\n",
        encoding="utf-8",
    )

    decision = decide_project_bump(repo, include_worktree=True)

    assert decision.level == "minor"
    assert decision.old_version == "0.1.0"
    assert decision.suggested_version == "0.2.0"
    assert "pkg/extra.py" in decision.changed_paths
    assert any(impact["symbol"] == "extra:bar" for impact in decision.impacts)


def test_decide_project_bump_detects_uncommitted_removed_public_symbol(
    tmp_path: Path,
) -> None:
    repo, pkg, _base = setup_repo(tmp_path)
    (pkg / "extra.py").write_text(
        "def bar() -> int:\n    return 2\n",
        encoding="utf-8",
    )
    run(["git", "add", "pkg/extra.py"], repo)
    run(["git", "commit", "-m", "feat: add bar"], repo)
    (pkg / "extra.py").unlink()

    decision = decide_project_bump(repo, base="HEAD", include_worktree=True)

    assert decision.level == "major"
    assert "pkg/extra.py" in decision.changed_paths
    assert any(
        impact["severity"] == "major" and impact["symbol"] == "extra:bar"
        for impact in decision.impacts
    )


def test_decide_project_bump_ignores_version_only_worktree_change(
    tmp_path: Path,
) -> None:
    repo, _pkg, _base = setup_repo(tmp_path)
    (repo / "pyproject.toml").write_text(
        "[project]\nname = 'demo'\nversion = '0.1.1'\n",
        encoding="utf-8",
    )

    decision = decide_project_bump(repo, include_worktree=True)

    assert decision.level is None
    assert decision.old_version == "0.1.1"
    assert decision.suggested_version == "0.1.1"
