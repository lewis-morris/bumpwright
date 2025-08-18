Template variables & filters
============================

Changelog entries are rendered using Jinja2 templates. The following variables
are available to templates:

``version``
    Type: str
    New project version.
``date``
    Type: str
    Current date in ISO format.
``commits``
    Type: list[dict]
    Commit entries with ``sha``, ``subject``, and optional ``link`` keys.
``repo_url``
    Type: str | None
    Repository base URL used for commit and compare links.
``previous_tag``
    Type: str | None
    Previous version tag when available.
``compare_url``
    Type: str | None
    Diff link between ``previous_tag`` and ``v{{ version }}``.
``release_datetime_iso``
    Type: str
    ISO-8601 timestamp of the release commit.
``contributors``
    Type: list[dict]
    Contributor mappings with ``name`` and optional ``link`` keys.
``breaking_changes``
    Type: list[str]
    Commit descriptions flagged as breaking changes.

No custom filters are provided; any standard Jinja2 filter may be used.

See :doc:`config` for configuration and CLI options.
