from __future__ import annotations

import os
from pathlib import Path

from bumpwright import gitutils
from bumpwright.analysers.javascript import (
    JavaScriptAnalyser,
    _build_javascript_api_at_ref,
    _list_javascript_files_at_ref,
    diff_javascript_api,
    extract_javascript_api_from_source,
)
from bumpwright.config import Config


def test_extracts_esm_function_and_optional_params() -> None:
    api = extract_javascript_api_from_source(
        "index",
        """
export function greet(name: string, title = "Mr", ...tags: string[]): string {
  return `${title} ${name}`;
}
""",
    )

    sig = api["index:greet"]
    assert [param.name for param in sig.params] == ["name", "title", "tags"]
    assert sig.params[0].default is None
    assert sig.params[0].annotation == "string"
    assert sig.params[1].default == '"Mr"'
    assert sig.params[2].kind == "vararg"
    assert sig.returns == "string"


def test_extracts_commonjs_exports() -> None:
    api = extract_javascript_api_from_source(
        "index",
        """
exports.run = function (task, options = {}) { return task(options); };
module.exports.stop = (code = 0) => code;
module.exports = { health, alias: runAlias };
""",
    )

    assert {"index:run", "index:stop", "index:health", "index:alias"} <= set(api)
    assert api["index:run"].params[0].name == "task"
    assert api["index:stop"].params[0].default == "0"


def test_diff_removed_and_added_exports() -> None:
    old = extract_javascript_api_from_source(
        "index",
        "export function removed() {}\nexport function kept() {}\n",
    )
    new = extract_javascript_api_from_source(
        "index",
        "export function kept() {}\nexport function added() {}\n",
    )

    impacts = diff_javascript_api(old, new)
    assert any(i.severity == "major" and i.symbol == "index:removed" for i in impacts)
    assert any(i.severity == "minor" and i.symbol == "index:added" for i in impacts)


def test_diff_required_param_major_optional_param_minor() -> None:
    old = extract_javascript_api_from_source("index", "export function run(task) {}\n")
    added_required = extract_javascript_api_from_source(
        "index", "export function run(task, env) {}\n"
    )
    added_optional = extract_javascript_api_from_source(
        "index", "export function run(task, env = {}) {}\n"
    )

    required_impacts = diff_javascript_api(old, added_required)
    optional_impacts = diff_javascript_api(old, added_optional)

    assert any(i.severity == "major" and "env" in i.reason for i in required_impacts)
    assert any(i.severity == "minor" and "env" in i.reason for i in optional_impacts)


def test_type_shape_change_is_major() -> None:
    old = extract_javascript_api_from_source(
        "types",
        "export interface User { id: string; }\n",
    )
    new = extract_javascript_api_from_source(
        "types",
        "export interface User { id: string; name: string; }\n",
    )

    impacts = diff_javascript_api(old, new)
    assert any(i.severity == "major" and i.symbol == "types:User" for i in impacts)


def test_comment_only_change_is_ignored() -> None:
    old = extract_javascript_api_from_source(
        "index",
        "export function run(task) {\n  return task;\n}\n",
    )
    new = extract_javascript_api_from_source(
        "index",
        "export function run(task) {\n  // comment\n  return task;\n}\n",
    )

    assert diff_javascript_api(old, new) == []


def test_javascript_file_listing_and_analyser(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    src = repo / "src"
    src.mkdir(parents=True)
    (repo / "package.json").write_text('{"name":"demo","main":"src/index.ts"}\n')
    (src / "index.ts").write_text("export function run(task) { return task; }\n")
    (src / "ignore.test.ts").write_text("export function ignored() {}\n")

    gitutils._run(["git", "init"], str(repo))
    gitutils._run(["git", "config", "user.email", "test@example.com"], str(repo))
    gitutils._run(["git", "config", "user.name", "Test"], str(repo))
    gitutils._run(["git", "add", "."], str(repo))
    gitutils._run(["git", "commit", "-m", "base"], str(repo))
    base = gitutils._run(["git", "rev-parse", "HEAD"], str(repo))

    (src / "index.ts").write_text(
        "export function run(task, env = {}) { return task; }\nexport const added = 1;\n"
    )
    gitutils._run(["git", "add", "src/index.ts"], str(repo))
    gitutils._run(["git", "commit", "-m", "head"], str(repo))
    head = gitutils._run(["git", "rev-parse", "HEAD"], str(repo))

    files = _list_javascript_files_at_ref(
        base,
        ["src"],
        [".ts"],
        ["src/*.test.ts"],
        str(repo),
        entrypoints=["src/index.ts"],
    )
    assert files == {"src/index.ts"}

    old_api = _build_javascript_api_at_ref(
        base, ["src"], [".ts"], ["src/*.test.ts"], ["_"], str(repo)
    )
    assert "index:run" in old_api

    cfg = Config()
    cfg.javascript.roots = ["src"]
    cfg.javascript.extensions = [".ts"]
    cfg.ignore.paths = ["src/*.test.ts"]
    analyser = JavaScriptAnalyser(cfg)

    old_cwd = os.getcwd()
    os.chdir(repo)
    try:
        old_state = analyser.collect(base)
        new_state = analyser.collect(head)
    finally:
        os.chdir(old_cwd)

    impacts = analyser.compare(old_state, new_state)
    assert any(i.severity == "minor" and i.symbol == "index:added" for i in impacts)
    assert any(i.severity == "minor" and "env" in i.reason for i in impacts)


def test_javascript_analyser_uses_package_json_entrypoints(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    src = repo / "src"
    src.mkdir(parents=True)
    (repo / "package.json").write_text(
        '{"name":"demo","main":"src/index.js","exports":"./src/index.js"}\n',
        encoding="utf-8",
    )
    (src / "index.js").write_text("export function run(task) { return task; }\n")
    (src / "internal.js").write_text(
        "export function internal(task) { return task; }\n"
    )

    gitutils._run(["git", "init"], str(repo))
    gitutils._run(["git", "config", "user.email", "test@example.com"], str(repo))
    gitutils._run(["git", "config", "user.name", "Test"], str(repo))
    gitutils._run(["git", "add", "."], str(repo))
    gitutils._run(["git", "commit", "-m", "base"], str(repo))
    base = gitutils._run(["git", "rev-parse", "HEAD"], str(repo))

    (src / "internal.js").write_text("export function renamed(task) { return task; }\n")
    gitutils._run(["git", "add", "src/internal.js"], str(repo))
    gitutils._run(["git", "commit", "-m", "head"], str(repo))
    head = gitutils._run(["git", "rev-parse", "HEAD"], str(repo))

    cfg = Config()
    cfg.javascript.roots = ["src"]
    analyser = JavaScriptAnalyser(cfg)

    old_cwd = os.getcwd()
    os.chdir(repo)
    try:
        old_state = analyser.collect(base)
        new_state = analyser.collect(head)
    finally:
        os.chdir(old_cwd)

    assert set(old_state) == {"index:run"}
    assert analyser.compare(old_state, new_state) == []
