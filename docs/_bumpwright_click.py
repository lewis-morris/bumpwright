from __future__ import annotations

import argparse
import logging

import click

from bumpwright.cli.bump import bump_command
from bumpwright.cli.decide import decide_command
from bumpwright.cli.history import history_command
from bumpwright.cli.init import init_command


@click.group()
@click.option(
    "--config",
    default="bumpwright.toml",
    show_default=True,
    help="Path to configuration file. See :doc:`concepts/configuration` for details.",
)
@click.option("--quiet", is_flag=True, help="Only display warnings and errors.")
@click.option("--verbose", is_flag=True, help="Show debug messages.")
@click.pass_context
def cli(ctx: click.Context, config: str, quiet: bool, verbose: bool) -> None:
    """Suggest and apply semantic version bumps.

    Args:
        ctx: Click execution context.
        config: Path to the configuration file used for the run. Defaults to
            ``bumpwright.toml``.
        quiet: Reduce log output to warnings and errors.
        verbose: Increase log output to show debug messages.
    """
    root = logging.getLogger()
    if not root.hasHandlers():
        logging.basicConfig(level=logging.INFO, format="%(message)s")
    if quiet and verbose:
        raise click.UsageError("--quiet and --verbose are mutually exclusive")
    if quiet:
        root.setLevel(logging.WARNING)
    elif verbose:
        root.setLevel(logging.DEBUG)
    ctx.obj = argparse.Namespace(config=config)


@cli.command()
@click.option(
    "--summary",
    type=click.Choice(["table", "json"]),
    default=None,
    help="Show project summary after initialisation in the chosen format.",
)
@click.pass_obj
def init(args: argparse.Namespace, summary: str | None) -> int:
    """Create a baseline release commit.

    Args:
        args: Parsed command-line arguments from :func:`cli`.
        summary: Summary output format.

    Returns:
        Exit status code, where ``0`` indicates success and ``1`` an error.
    """
    args.summary = summary
    return init_command(args)


@cli.command()
@click.option(
    "--base",
    help=(
        "Base git reference when auto-deciding the level. Defaults to the last release "
        "commit or the previous commit (HEAD^)."
    ),
)
@click.option("--head", default="HEAD", show_default=True, help="Head git reference.")
@click.option(
    "--format",
    "output_fmt",
    type=click.Choice(["text", "md", "json"]),
    default="text",
    show_default=True,
    help="Output style: plain text, Markdown, or machine-readable JSON.",
)
@click.option(
    "--emit-changelog",
    is_flag=True,
    help="Print expected changelog for the suggested version.",
)
@click.option(
    "--explain", is_flag=True, help="Show reasoning behind the selected bump level."
)
@click.option(
    "--no-impl-change-patch",
    is_flag=True,
    help="Ignore implementation-only changes to public symbols.",
)
@click.option(
    "--repo-url",
    help=(
        "Base repository URL for linking commit hashes in Markdown output. "
        "Can also be set via [changelog].repo_url in configuration."
    ),
)
@click.option(
    "--changelog-template",
    type=str,
    help="Jinja2 template file for changelog entries; defaults to the built-in template or [changelog].template when configured.",
)
@click.option(
    "--changelog-exclude",
    multiple=True,
    help="Regex pattern for commit subjects to exclude from changelog (repeatable).",
)
@click.option(
    "--enable-analyser",
    multiple=True,
    help="Enable analyser NAME (repeatable) in addition to configuration.",
)
@click.option(
    "--disable-analyser",
    multiple=True,
    help="Disable analyser NAME (repeatable) even if configured.",
)
@click.pass_obj
def decide(
    args: argparse.Namespace,
    base: str | None,
    head: str,
    output_fmt: str,
    emit_changelog: bool,
    explain: bool,
    repo_url: str | None,
    changelog_template: str | None,
    changelog_exclude: tuple[str, ...],
    enable_analyser: tuple[str, ...],
    disable_analyser: tuple[str, ...],
    no_impl_change_patch: bool,
) -> int:
    """Suggest a version bump without modifying files."""

    args.base = base
    args.head = head
    args.output_fmt = output_fmt
    args.emit_changelog = emit_changelog
    args.explain = explain
    args.repo_url = repo_url
    args.changelog_template = changelog_template
    args.changelog_exclude = list(changelog_exclude)
    args.enable_analyser = list(enable_analyser)
    args.disable_analyser = list(disable_analyser)
    args.no_impl_change_patch = no_impl_change_patch
    return decide_command(args)


@cli.command()
@click.option(
    "--base",
    help=(
        "Base git reference when auto-deciding the level. Defaults to the last release "
        "commit or the previous commit (HEAD^)."
    ),
)
@click.option("--head", default="HEAD", show_default=True, help="Head git reference.")
@click.option(
    "--format",
    "output_fmt",
    type=click.Choice(["text", "md", "json"]),
    default="text",
    show_default=True,
    help="Output style: plain text, Markdown, or machine-readable JSON.",
)
@click.option(
    "--repo-url",
    help=(
        "Base repository URL for linking commit hashes in Markdown output. "
        "Can also be set via [changelog].repo_url in configuration."
    ),
)
@click.option(
    "--explain",
    is_flag=True,
    help="Show reasoning behind the selected bump level.",
)
@click.option(
    "--no-impl-change-patch",
    is_flag=True,
    help="Ignore implementation-only changes to public symbols.",
)
@click.option(
    "--enable-analyser",
    multiple=True,
    help="Enable analyser NAME (repeatable) in addition to configuration.",
)
@click.option(
    "--disable-analyser",
    multiple=True,
    help="Disable analyser NAME (repeatable) even if configured.",
)
@click.option(
    "--pyproject",
    default="pyproject.toml",
    show_default=True,
    help="Path to the project's pyproject.toml file.",
)
@click.option(
    "--version-path",
    multiple=True,
    help=(
        "Additional glob pattern for files containing the project version "
        "(repeatable). Defaults include ``pyproject.toml``, ``setup.py``, "
        "``setup.cfg``, and any ``__init__.py``, ``version.py``, or "
        "``_version.py`` files."
    ),
)
@click.option(
    "--version-ignore",
    multiple=True,
    help="Glob pattern for paths to exclude from version updates (repeatable).",
)
@click.option(
    "--commit", is_flag=True, help="Create a git commit for the version change."
)
@click.option("--tag", is_flag=True, help="Create a git tag for the new version.")
@click.option(
    "--dry-run",
    is_flag=True,
    help="Display the new version without modifying any files.",
)
@click.option(
    "--changelog",
    type=str,
    flag_value="-",
    default=None,
    nargs=1,
    is_flag=False,
    metavar="[FILE]",
    help=(
        "Append release notes to FILE or stdout when no path is given. "
        "Defaults to [changelog].path in configuration when omitted."
    ),
)
@click.option(
    "--changelog-template",
    type=str,
    help=(
        "Jinja2 template file for changelog entries; defaults to the built-in "
        "template or [changelog].template when configured."
    ),
)
@click.option(
    "--changelog-exclude",
    multiple=True,
    help=(
        "Regex pattern for commit subjects to exclude from changelog "
        "(repeatable). Combined with patterns from [changelog].exclude."
    ),
)
@click.pass_obj
def bump(args: argparse.Namespace, **kwargs: object) -> int:
    """Update version metadata and optionally commit and tag the change.

    Args:
        args: Parsed command-line arguments from :func:`cli`.
        ``**kwargs``: Command-specific options. Notable parameters include:

            base (str | None): Git reference used as the comparison base when
            inferring the bump level. Defaults to the latest release commit or
            ``HEAD^``.

            head (str): Git reference representing the working tree. Defaults
            to ``HEAD``.

            output_fmt (str): Output format: ``text`` (default), ``md`` for
            Markdown, or ``json`` for machine-readable output.

            repo_url (str | None): Base repository URL used to build commit
            links in Markdown output. Overrides ``[changelog].repo_url`` when
            provided.

            decide (bool): When ``True``, only report the bump level without
            modifying any files.

            enable_analyser (tuple[str, ...]): Names of analysers to enable in
            addition to those configured.

            disable_analyser (tuple[str, ...]): Names of analysers to disable
            even if configured.

            no_impl_change_patch (bool): When ``True``, ignore implementation-only
            changes to public symbols when determining the bump level.

            pyproject (str): Path to ``pyproject.toml``. Defaults to
            ``pyproject.toml``.

            version_path (tuple[str, ...]): Extra glob patterns for files whose
            version fields should be updated. Defaults include
            ``pyproject.toml``, ``setup.py``, ``setup.cfg``, and any
            ``__init__.py``, ``version.py``, or ``_version.py`` files.

            version_ignore (tuple[str, ...]): Glob patterns for paths to exclude
            from version updates.

            commit (bool): Create a git commit containing the version change.

            tag (bool): Create a git tag for the new version.

            dry_run (bool): Show the new version without modifying files.

            changelog (str | None): Write release notes to the given file or
            stdout when ``-`` is provided.

            changelog_template (str | None): Path to a Jinja2 template used to
            render changelog entries. Defaults to the built-in template.

            changelog_exclude (tuple[str, ...]): Regex patterns of commit
            subjects to omit from changelog entries.

    Returns:
        Exit status code, where ``0`` indicates success and ``1`` an error.
    """
    params = vars(args).copy()
    params.update(kwargs)
    params["enable_analyser"] = list(params.get("enable_analyser", []))
    params["disable_analyser"] = list(params.get("disable_analyser", []))
    params["version_path"] = list(params.get("version_path", []))
    params["version_ignore"] = list(params.get("version_ignore", []))
    params["changelog_exclude"] = list(params.get("changelog_exclude", []))
    return bump_command(argparse.Namespace(**params))


@cli.command()
@click.option(
    "--format",
    "output_fmt",
    type=click.Choice(["text", "md", "json"]),
    default="text",
    show_default=True,
    help="Output style: plain text, Markdown, or machine-readable JSON.",
)
@click.option(
    "--local-time",
    is_flag=True,
    help="Display commit dates in local time instead of ISO-8601.",
)
@click.option(
    "--stats",
    is_flag=True,
    help="Include line change statistics between successive tags.",
)
@click.option(
    "--rollback",
    metavar="TAG",
    help="Delete TAG and restore versioned files to the previous commit.",
)
@click.option(
    "--purge",
    is_flag=True,
    help="Remove all bumpwright release tags and commits, restoring versioned files.",
)
@click.pass_obj
def history(
    args: argparse.Namespace,
    output_fmt: str,
    local_time: bool,
    stats: bool,
    rollback: str | None,
    purge: bool,
) -> int:
    """List existing git tags, roll back a release, or purge bumpwright state.

    Args:
        args: Parsed command-line arguments from :func:`cli`.
        output_fmt: Desired output format.
        stats: Whether to include diff statistics between tags.
        rollback: Tag to remove and restore to the previous commit.
        purge: Remove all bumpwright release tags and reset versioned files.

    Returns:
        Exit status code, where ``0`` indicates success and ``1`` an error.
    """

    args.output_fmt = output_fmt
    args.local_time = local_time
    args.stats = stats
    args.rollback = rollback
    args.purge = purge
    return history_command(args)
