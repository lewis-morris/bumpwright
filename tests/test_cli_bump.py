import argparse
import logging
import subprocess
from pathlib import Path

import pytest
from cli_helpers import run, setup_repo

from bumpwright.cli.bump import bump_command
from bumpwright.gitutils import GitCommandError


def _args(commit: bool = False, tag: bool = False) -> argparse.Namespace:
    """Build argument namespace for ``bump_command`` tests."""

    return argparse.Namespace(
        config="bumpwright.toml",
        base=None,
        head="HEAD",
        output_fmt="text",
        repo_url=None,
        enable_analyser=[],
        disable_analyser=[],
        pyproject="pyproject.toml",
        version_path=[],
        version_ignore=[],
        commit=commit,
        tag=tag,
        dry_run=False,
        changelog=None,
        changelog_template=None,
        changelog_exclude=[],
    )


def _prepare_repo(tmp_path: Path) -> Path:
    repo, pkg, _ = setup_repo(tmp_path)
    (pkg / "extra.py").write_text("def bar() -> int:\n    return 2\n", encoding="utf-8")
    run(["git", "add", "pkg/extra.py"], repo)
    run(["git", "commit", "-m", "feat: add bar"], repo)
    return repo


def test_bump_commit_failure(
    monkeypatch, tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """Return ``1`` and log an error when committing fails."""

    repo = _prepare_repo(tmp_path)

    def fail(
        args: list[str], cwd: str | None = None
    ) -> subprocess.CompletedProcess[str]:
        if args[0] == "commit":
            raise GitCommandError(1, ["git", *args], stderr="boom")
        return subprocess.CompletedProcess(["git", *args], 0, "", "")

    monkeypatch.setattr("bumpwright.cli.bump.run_git", fail)
    monkeypatch.chdir(repo)
    with caplog.at_level(logging.ERROR):
        res = bump_command(_args(commit=True))
    assert res == 1
    assert "Failed to commit release" in caplog.text
    assert "boom" not in caplog.text


def test_bump_tag_failure(
    monkeypatch, tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """Return ``1`` and log an error when tagging fails."""

    repo = _prepare_repo(tmp_path)

    def fail(
        args: list[str], cwd: str | None = None
    ) -> subprocess.CompletedProcess[str]:
        if args[0] == "rev-parse":
            raise GitCommandError(1, ["git", *args], stderr="missing")
        if args[0] == "tag":
            raise GitCommandError(1, ["git", *args], stderr="boom")
        return subprocess.CompletedProcess(["git", *args], 0, "", "")

    monkeypatch.setattr("bumpwright.cli.bump.run_git", fail)
    monkeypatch.chdir(repo)
    with caplog.at_level(logging.ERROR):
        res = bump_command(_args(tag=True))
    assert res == 1
    assert "Failed to create tag" in caplog.text
    assert "boom" not in caplog.text


def test_bump_command_updates_node_package_json(
    monkeypatch, tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """Node-only projects should bump package.json from JavaScript impacts."""

    repo = tmp_path / "repo"
    repo.mkdir()
    run(["git", "init"], repo)
    run(["git", "config", "user.email", "a@b.c"], repo)
    run(["git", "config", "user.name", "tester"], repo)
    (repo / "package.json").write_text(
        '{\n  "name": "demo",\n  "version": "1.2.3"\n}\n',
        encoding="utf-8",
    )
    src = repo / "src"
    src.mkdir()
    (src / "index.js").write_text(
        "export function run(task) { return task; }\n", encoding="utf-8"
    )
    (repo / "bumpwright.toml").write_text(
        "[analysers]\njavascript = true\n[javascript]\nroots = ['src']\n",
        encoding="utf-8",
    )
    run(["git", "add", "."], repo)
    run(["git", "commit", "-m", "base"], repo)
    (src / "index.js").write_text(
        "export function run(task, env = {}) { return task; }\n",
        encoding="utf-8",
    )
    run(["git", "add", "src/index.js"], repo)
    run(["git", "commit", "-m", "feat: add optional env"], repo)

    monkeypatch.chdir(repo)
    with caplog.at_level(logging.INFO):
        result = bump_command(_args())

    assert result == 0
    assert '"version": "1.3.0"' in (repo / "package.json").read_text(encoding="utf-8")
    assert "bumpwright bumped version: 1.2.3 -> 1.3.0 (minor)" in caplog.text
