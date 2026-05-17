"""Stable Python API for bumpwright decisions."""

from __future__ import annotations

import argparse
import os
import subprocess
import tempfile
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterator

from .cli.decide import _collect_impacts
from .compare import Impact, decide_bump
from .config import load_config
from .gitutils import changed_paths, last_release_commit, run_git
from .analysers.utils import clear_caches
from .versioning import bump_string, read_project_version


@dataclass(frozen=True)
class BumpDecision:
    """Machine-readable semantic version decision."""

    level: str | None
    confidence: float
    reasons: list[str]
    impacts: list[dict[str, str]]
    changed_paths: list[str]
    base: str
    head: str
    old_version: str | None
    suggested_version: str | None

    def to_dict(self) -> dict[str, object]:
        """Return a JSON-serialisable representation."""

        return asdict(self)


@contextmanager
def _pushd(path: Path) -> Iterator[None]:
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


def _dirty_paths(repo_root: Path) -> list[str]:
    status = run_git(
        ["status", "--porcelain=v1", "--untracked-files=all"],
        cwd=str(repo_root),
    ).stdout
    paths: set[str] = set()
    for line in status.splitlines():
        if not line:
            continue
        if line.startswith("?? "):
            paths.add(line[3:])
            continue
        path = line[3:]
        if " -> " in path:
            _old, path = path.split(" -> ", 1)
        if path:
            paths.add(path)
    return sorted(paths)


def _worktree_snapshot_ref(repo_root: Path) -> str:
    """Create an anonymous commit object representing the current worktree."""

    dirty = _dirty_paths(repo_root)
    if not dirty:
        return "HEAD"

    with tempfile.NamedTemporaryFile(prefix="bumpwright-index-") as index_file:
        env = {**os.environ, "GIT_INDEX_FILE": index_file.name}
        subprocess.run(
            ["git", "read-tree", "HEAD"],
            cwd=repo_root,
            env=env,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        for path in dirty:
            target = repo_root / path
            cmd = ["git", "add", "--", path] if target.exists() else ["git", "rm", "--cached", "-q", "--", path]
            subprocess.run(
                cmd,
                cwd=repo_root,
                env=env,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        tree = subprocess.run(
            ["git", "write-tree"],
            cwd=repo_root,
            env=env,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        ).stdout.strip()
        return subprocess.run(
            ["git", "commit-tree", tree, "-p", "HEAD", "-m", "bumpwright worktree snapshot"],
            cwd=repo_root,
            env=env,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        ).stdout.strip()


def _args(
    *,
    enable_analyser: list[str] | None,
    disable_analyser: list[str] | None,
    no_impl_change_patch: bool,
) -> argparse.Namespace:
    return argparse.Namespace(
        enable_analyser=enable_analyser,
        disable_analyser=disable_analyser,
        no_impl_change_patch=no_impl_change_patch,
        explain=False,
    )


def _default_base(repo_root: Path) -> str:
    release = last_release_commit(str(repo_root))
    if release:
        return release
    try:
        run_git(["rev-parse", "--verify", "HEAD^"], cwd=str(repo_root))
    except subprocess.CalledProcessError:
        return "HEAD"
    return "HEAD^"


def decide_project_bump(  # noqa: PLR0913
    repo_root: str | Path = ".",
    *,
    config_path: str | Path = "bumpwright.toml",
    base: str | None = None,
    head: str = "HEAD",
    include_worktree: bool = False,
    enable_analyser: list[str] | None = None,
    disable_analyser: list[str] | None = None,
    no_impl_change_patch: bool = False,
) -> BumpDecision:
    """Return the semantic version decision for a repository.

    When ``include_worktree`` is true, uncommitted tracked and untracked changes
    are represented by an anonymous git commit object and analysed with the same
    path used for normal ref-to-ref comparisons.
    """

    root = Path(repo_root).resolve()
    config = Path(config_path)
    if not config.is_absolute():
        config = root / config

    with _pushd(root):
        clear_caches()
        cfg = load_config(config)
        resolved_base = base or _default_base(root)
        resolved_head = _worktree_snapshot_ref(root) if include_worktree else head
        impacts = _collect_impacts(
            resolved_base,
            resolved_head,
            cfg,
            _args(
                enable_analyser=enable_analyser,
                disable_analyser=disable_analyser,
                no_impl_change_patch=no_impl_change_patch,
            ),
        )
        decision = decide_bump(impacts)
        old_version: str | None
        suggested_version: str | None
        try:
            old_version = read_project_version(root / "pyproject.toml")
        except (FileNotFoundError, KeyError):
            old_version = None
        if old_version and decision.level:
            suggested_version = bump_string(old_version, decision.level, cfg.version.scheme)
        else:
            suggested_version = old_version
        try:
            paths = sorted(changed_paths(resolved_base, resolved_head, cwd=str(root)))
        except subprocess.CalledProcessError:
            paths = []
        clear_caches()

    return BumpDecision(
        level=decision.level,
        confidence=decision.confidence,
        reasons=decision.reasons,
        impacts=[_impact_to_dict(impact) for impact in impacts],
        changed_paths=paths,
        base=resolved_base,
        head=resolved_head,
        old_version=old_version,
        suggested_version=suggested_version,
    )


def _impact_to_dict(impact: Impact) -> dict[str, str]:
    return {
        "severity": impact.severity,
        "symbol": impact.symbol,
        "reason": impact.reason,
    }


__all__ = ["BumpDecision", "decide_project_bump"]
