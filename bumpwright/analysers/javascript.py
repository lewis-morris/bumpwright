"""Analyse JavaScript and TypeScript exports for semantic version impacts."""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Iterable
from fnmatch import fnmatch
from pathlib import Path

from ..compare import Impact, compare_funcs
from ..config import Config
from ..gitutils import _run, read_files_at_ref
from ..public_api import FuncSig, Param, PublicAPI
from . import register

_TYPE_MARKER = "__bumpwright_js_type__"
_VALUE_MARKER = "__bumpwright_js_value__"
_EXPORT_NAME = r"[$A-Z_a-z][$\w]*"


def _strip_comments(source: str) -> str:
    """Remove JavaScript comments while preserving string literals."""

    out: list[str] = []
    i = 0
    quote: str | None = None
    escaped = False
    while i < len(source):
        ch = source[i]
        nxt = source[i + 1] if i + 1 < len(source) else ""
        if quote:
            out.append(ch)
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == quote:
                quote = None
            i += 1
            continue
        if ch in {"'", '"', "`"}:
            quote = ch
            out.append(ch)
            i += 1
            continue
        if ch == "/" and nxt == "/":
            while i < len(source) and source[i] != "\n":
                i += 1
            out.append("\n")
            continue
        if ch == "/" and nxt == "*":
            i += 2
            while i + 1 < len(source) and not (
                source[i] == "*" and source[i + 1] == "/"
            ):
                out.append("\n" if source[i] == "\n" else " ")
                i += 1
            i += 2
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def _hash_text(text: str) -> str:
    normalized = " ".join(_strip_comments(text).split())
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def _split_top_level(text: str, delimiter: str = ",") -> list[str]:
    parts: list[str] = []
    start = 0
    depth = 0
    quote: str | None = None
    escaped = False
    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    closers = set(pairs.values())
    for idx, ch in enumerate(text):
        if quote:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == quote:
                quote = None
            continue
        if ch in {"'", '"', "`"}:
            quote = ch
            continue
        if ch in pairs:
            depth += 1
            continue
        if ch in closers and depth:
            depth -= 1
            continue
        if ch == delimiter and depth == 0:
            parts.append(text[start:idx].strip())
            start = idx + 1
    tail = text[start:].strip()
    if tail:
        parts.append(tail)
    return parts


def _split_first_top_level(text: str, delimiter: str) -> tuple[str, str | None]:
    parts = _split_top_level(text, delimiter)
    if len(parts) <= 1:
        return text.strip(), None
    return parts[0], delimiter.join(parts[1:]).strip()


def _clean_type_annotation(text: str | None) -> str | None:
    if text is None:
        return None
    cleaned = text.strip()
    return cleaned or None


def _parse_params(params_text: str) -> tuple[Param, ...]:
    params: list[Param] = []
    for raw in _split_top_level(params_text):
        if not raw:
            continue
        defaultless, default = _split_first_top_level(raw, "=")
        default = default.strip() if default is not None else None
        item = defaultless.strip()
        kind = "pos"
        if item.startswith("..."):
            kind = "vararg"
            item = item[3:].strip()
            default = default or "..."
        name_part, annotation = _split_first_top_level(item, ":")
        name = name_part.strip()
        if name.startswith("{") or name.startswith("["):
            name = name.replace(" ", "")
        optional = name.endswith("?")
        if optional:
            name = name[:-1]
            default = default or "undefined"
        if not name:
            continue
        params.append(
            Param(
                name,
                kind,
                default,
                _clean_type_annotation(annotation),
            )
        )
    return tuple(params)


def _find_matching(source: str, open_pos: int) -> int:
    opener = source[open_pos]
    closer = {"(": ")", "{": "}", "[": "]"}[opener]
    depth = 0
    quote: str | None = None
    escaped = False
    for idx in range(open_pos, len(source)):
        ch = source[idx]
        if quote:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == quote:
                quote = None
            continue
        if ch in {"'", '"', "`"}:
            quote = ch
            continue
        if ch == opener:
            depth += 1
        elif ch == closer:
            depth -= 1
            if depth == 0:
                return idx
    return -1


def _statement_end(source: str, start: int) -> int:
    for idx in range(start, len(source)):
        if source[idx] in {";", "\n"}:
            return idx
    return len(source)


def _module_name_from_path(root: str, path: str) -> str:
    rel = Path(path).with_suffix("")
    try:
        rel = rel.relative_to(Path(root))
    except ValueError:
        pass
    if rel.name == "index":
        rel = rel.parent
    name = ".".join(part for part in rel.parts if part and part != ".")
    return name or "index"


def _normalize_package_path(value: str) -> str | None:
    path = value.strip()
    if not path or path.startswith("#"):
        return None
    if path.startswith("./"):
        path = path[2:]
    return path or None


def _collect_export_paths(value: object) -> set[str]:
    paths: set[str] = set()
    if isinstance(value, str):
        normalized = _normalize_package_path(value)
        if normalized:
            paths.add(normalized)
    elif isinstance(value, list):
        for item in value:
            paths.update(_collect_export_paths(item))
    elif isinstance(value, dict):
        for item in value.values():
            paths.update(_collect_export_paths(item))
    return paths


def _package_entrypoints_at_ref(
    ref: str,
    package_json: str,
    extensions: Iterable[str],
    cwd: str | None = None,
) -> list[str]:
    contents = read_files_at_ref(ref.strip(), [package_json], cwd)
    text = contents.get(package_json)
    if text is None:
        return []
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return []
    paths: set[str] = set()
    for key in ("main", "module", "types", "typings", "browser"):
        value = data.get(key)
        if isinstance(value, str):
            normalized = _normalize_package_path(value)
            if normalized:
                paths.add(normalized)
    paths.update(_collect_export_paths(data.get("exports")))
    allowed = tuple(extensions)
    return sorted(path for path in paths if path.endswith(allowed))


def _is_public(name: str, private_prefixes: Iterable[str]) -> bool:
    return not name.startswith(tuple(private_prefixes))


def _record(  # noqa: PLR0913
    api: PublicAPI,
    module_name: str,
    export_name: str,
    params: tuple[Param, ...],
    returns: str | None,
    text: str,
    private_prefixes: Iterable[str],
) -> None:
    if not _is_public(export_name, private_prefixes):
        return
    fullname = f"{module_name}:{export_name}"
    api[fullname] = FuncSig(fullname, params, returns, _hash_text(text))


def _parse_function_decl(
    source: str,
    match: re.Match[str],
) -> tuple[str, tuple[Param, ...], str | None, str]:
    name = match.group("name") or "default"
    open_paren = match.end() - 1
    close_paren = _find_matching(source, open_paren)
    params = _parse_params(source[open_paren + 1 : close_paren])
    returns: str | None = None
    tail_start = close_paren + 1
    body_start = source.find("{", tail_start)
    if body_start != -1:
        tail = source[tail_start:body_start]
        ret_match = re.search(r":\s*(?P<ret>.+?)\s*$", tail)
        if ret_match:
            returns = ret_match.group("ret").strip()
        body_end = _find_matching(source, body_start)
        end = body_end + 1 if body_end != -1 else _statement_end(source, body_start)
    else:
        end = _statement_end(source, close_paren)
    return name, params, returns, source[match.start() : end]


def _extract_esm(
    source: str, module_name: str, private_prefixes: Iterable[str]
) -> PublicAPI:
    api: PublicAPI = {}
    func_re = re.compile(
        rf"export\s+(?:default\s+)?(?:async\s+)?function(?:\s+(?P<name>{_EXPORT_NAME}))?\s*\(",
        re.MULTILINE,
    )
    for match in func_re.finditer(source):
        name, params, returns, text = _parse_function_decl(source, match)
        _record(api, module_name, name, params, returns, text, private_prefixes)

    class_re = re.compile(rf"export\s+(?:default\s+)?class\s+(?P<name>{_EXPORT_NAME})")
    for match in class_re.finditer(source):
        body_start = source.find("{", match.end())
        if body_start == -1:
            end = _statement_end(source, match.end())
        else:
            body_end = _find_matching(source, body_start)
            end = body_end + 1 if body_end != -1 else _statement_end(source, body_start)
        _record(
            api,
            module_name,
            match.group("name"),
            (),
            None,
            source[match.start() : end],
            private_prefixes,
        )

    value_re = re.compile(
        rf"export\s+(?:const|let|var)\s+(?P<name>{_EXPORT_NAME})\s*=\s*(?P<value>.+?)(?:;|$)",
        re.MULTILINE | re.DOTALL,
    )
    for match in value_re.finditer(source):
        value = match.group("value").strip()
        arrow = re.match(
            r"(?:async\s*)?\((?P<params>.*?)\)\s*(?::\s*(?P<ret>[^=]+?))?\s*=>",
            value,
            re.DOTALL,
        )
        if arrow:
            params = _parse_params(arrow.group("params"))
            returns = _clean_type_annotation(arrow.group("ret"))
        else:
            params = ()
            returns = _VALUE_MARKER
        _record(
            api,
            module_name,
            match.group("name"),
            params,
            returns,
            match.group(0),
            private_prefixes,
        )

    type_re = re.compile(
        rf"export\s+(?:interface|type|enum)\s+(?P<name>{_EXPORT_NAME})(?P<body>.*?)(?=\nexport\s+|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    for match in type_re.finditer(source):
        _record(
            api,
            module_name,
            match.group("name"),
            (),
            _TYPE_MARKER,
            match.group(0),
            private_prefixes,
        )

    named_re = re.compile(r"export\s*\{(?P<body>.*?)\}\s*;?", re.DOTALL)
    for match in named_re.finditer(source):
        for item in _split_top_level(match.group("body")):
            if not item:
                continue
            parts = re.split(r"\s+as\s+", item)
            export_name = parts[-1].strip()
            _record(
                api, module_name, export_name, (), _VALUE_MARKER, item, private_prefixes
            )
    return api


def _extract_commonjs(
    source: str, module_name: str, private_prefixes: Iterable[str]
) -> PublicAPI:
    api: PublicAPI = {}
    assign_re = re.compile(
        rf"(?:module\.)?exports\.(?P<name>{_EXPORT_NAME})\s*=\s*(?P<value>.+?)(?:;|$)",
        re.MULTILINE | re.DOTALL,
    )
    for match in assign_re.finditer(source):
        value = match.group("value").strip()
        func = re.match(
            r"(?:async\s*)?function\s*\((?P<params>.*?)\)", value, re.DOTALL
        )
        arrow = re.match(
            r"(?:async\s*)?\((?P<params>.*?)\)\s*(?::\s*(?P<ret>[^=]+?))?\s*=>",
            value,
            re.DOTALL,
        )
        if func:
            params = _parse_params(func.group("params"))
            returns = None
        elif arrow:
            params = _parse_params(arrow.group("params"))
            returns = _clean_type_annotation(arrow.group("ret"))
        else:
            params = ()
            returns = _VALUE_MARKER
        _record(
            api,
            module_name,
            match.group("name"),
            params,
            returns,
            match.group(0),
            private_prefixes,
        )

    object_re = re.compile(r"module\.exports\s*=\s*\{(?P<body>.*?)\}\s*;?", re.DOTALL)
    for match in object_re.finditer(source):
        for item in _split_top_level(match.group("body")):
            if not item:
                continue
            export_name = item.split(":", 1)[0].strip()
            _record(
                api, module_name, export_name, (), _VALUE_MARKER, item, private_prefixes
            )
    return api


def extract_javascript_api_from_source(
    module_name: str,
    code: str,
    private_prefixes: Iterable[str] = ("_",),
) -> PublicAPI:
    """Extract exported JavaScript/TypeScript symbols from source text."""

    cleaned = _strip_comments(code)
    api = _extract_esm(cleaned, module_name, private_prefixes)
    api.update(_extract_commonjs(cleaned, module_name, private_prefixes))
    return api


def diff_javascript_api(old: PublicAPI, new: PublicAPI) -> list[Impact]:
    """Compute semantic-version impacts between JavaScript API snapshots."""

    impacts: list[Impact] = []
    for symbol in old.keys() - new.keys():
        impacts.append(Impact("major", symbol, "Removed public symbol"))
    for symbol in old.keys() & new.keys():
        old_sig = old[symbol]
        new_sig = new[symbol]
        if _TYPE_MARKER in {old_sig.returns, new_sig.returns}:
            if old_sig.body_hash != new_sig.body_hash:
                impacts.append(Impact("major", symbol, "Changed exported type"))
            continue
        impacts.extend(
            compare_funcs(
                old_sig,
                new_sig,
                return_type_change="minor",
                param_annotation_change="patch",
                body_change="patch",
            )
        )
    for symbol in new.keys() - old.keys():
        impacts.append(Impact("minor", symbol, "Added public symbol"))
    return impacts


def _list_javascript_files_at_ref(  # noqa: PLR0913
    ref: str,
    roots: Iterable[str],
    extensions: Iterable[str],
    ignore_globs: Iterable[str],
    cwd: str | None = None,
    entrypoints: Iterable[str] = (),
) -> set[str]:
    """List JavaScript/TypeScript files under ``roots`` at a git ref."""

    ref = ref.strip()
    allowed = tuple(extensions)
    roots_norm = [str(Path(root)) for root in roots]
    out = _run(["git", "ls-tree", "-r", "--name-only", ref], cwd)
    paths: set[str] = set()
    if roots_norm:
        for line in out.splitlines():
            path = Path(line)
            path_text = str(path)
            if not path_text.endswith(allowed):
                continue
            if not any(
                path_text == root or path_text.startswith(root.rstrip("/") + "/")
                for root in roots_norm
            ):
                continue
            if any(fnmatch(path_text, pattern) for pattern in ignore_globs):
                continue
            paths.add(path_text)
    for entrypoint in entrypoints:
        path_text = str(Path(entrypoint))
        if path_text.endswith(allowed) and not any(
            fnmatch(path_text, pattern) for pattern in ignore_globs
        ):
            paths.add(path_text)
    return paths


def _build_javascript_api_at_ref(  # noqa: PLR0913
    ref: str,
    roots: Iterable[str],
    extensions: Iterable[str],
    ignores: Iterable[str],
    private_prefixes: Iterable[str],
    cwd: str | None = None,
    entrypoints: Iterable[str] = (),
) -> PublicAPI:
    """Collect JavaScript/TypeScript exported API at ``ref``."""

    ref = ref.strip()
    paths = sorted(
        _list_javascript_files_at_ref(
            ref, roots, extensions, ignores, cwd=cwd, entrypoints=entrypoints
        )
    )
    contents = read_files_at_ref(ref, paths, cwd)
    api: PublicAPI = {}
    root_list = list(roots)
    for path in paths:
        code = contents.get(path)
        if code is None:
            continue
        root = next(
            (
                candidate
                for candidate in root_list
                if path == candidate or path.startswith(candidate.rstrip("/") + "/")
            ),
            str(Path(path).parent),
        )
        module_name = _module_name_from_path(root, path)
        api.update(
            extract_javascript_api_from_source(module_name, code, private_prefixes)
        )
    return api


@register("javascript", "Analyze JavaScript and TypeScript exported APIs.")
class JavaScriptAnalyser:
    """Analyser plugin for JavaScript and TypeScript public exports."""

    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg

    def collect(self, ref: str) -> PublicAPI:
        roots = self.cfg.javascript.roots
        entrypoints = self.cfg.javascript.entrypoints
        if not entrypoints:
            discovered = _package_entrypoints_at_ref(
                ref,
                self.cfg.javascript.package_json,
                self.cfg.javascript.extensions,
            )
            if discovered:
                roots = []
                entrypoints = discovered
        return _build_javascript_api_at_ref(
            ref,
            roots,
            self.cfg.javascript.extensions,
            self.cfg.ignore.paths,
            self.cfg.project.private_prefixes,
            entrypoints=entrypoints,
        )

    def compare(self, old: PublicAPI, new: PublicAPI) -> list[Impact]:
        return diff_javascript_api(old, new)
