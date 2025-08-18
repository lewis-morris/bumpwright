bumpwright bump
===============

Update version information in ``pyproject.toml`` and other files. By default, ``bumpwright`` also searches ``setup.py``, ``setup.cfg`` and any ``__init__.py``, ``version.py`` or ``_version.py`` files for a version assignment. Files inside common build artefacts and virtual environments are ignored by default (``build/**``, ``dist/**``, ``*.egg-info/**``, ``.eggs/**``, ``.venv/**``, ``venv/**``, ``.env/**`` and ``**/__pycache__/**``). These locations can be customised via the ``[version]`` section in ``bumpwright.toml`` or augmented with ``--version-path`` and ``--version-ignore`` to add or exclude patterns. See :doc:`../guides/version-management/version-file-targeting` for targeting specific version files.

Primary options
---------------

* ``--base BASE`` – base git reference when auto-deciding the level.
* ``--head HEAD`` – head git reference.
* ``--commit`` – create a git commit for the version change.
* ``--tag`` – create a git tag for the new version.
* ``--dry-run`` – preview changes without modifying any files.
* ``--explain`` – show reasoning behind the selected bump level.
* ``--no-impl-change-patch`` – ignore implementation-only changes to public symbols.

Arguments
---------

``--base BASE``
    Base git reference when auto-deciding the level. Defaults to the last release commit if available, otherwise the previous commit (``HEAD^``).

``--head HEAD``
    Head git reference. Defaults to ``HEAD``.

``--format {text,md,json}``
    Output style. ``text`` prints plain console output, ``md`` emits Markdown, and ``json`` produces machine-readable data. Defaults to ``text``.

``--explain``
    Log detected impacts, applied rules, and chosen bump level before any files are modified.

``--no-impl-change-patch``
    Do not treat implementation-only changes as patch-level impacts when computing the bump.

``--repo-url URL``
    Base repository URL used to build commit links in Markdown output. Overrides ``[changelog].repo_url`` when provided. Defaults to none, showing raw commit hashes when unset.

``--enable-analyser NAME``
    Enable analyser ``NAME`` in addition to configuration. Repeatable. Defaults to none.

``--disable-analyser NAME``
    Disable analyser ``NAME`` even if enabled in configuration. Repeatable. Defaults to none.

``--changelog [FILE]``
    Append release notes for the new version to ``FILE``. When ``FILE`` is omitted or set to ``-``, the changelog entry is printed to standard output. Defaults to none, producing no changelog unless ``[changelog].path`` in ``bumpwright.toml`` supplies a default. See :doc:`../concepts/configuration` for more detail.

``--changelog-template PATH``
    Jinja2 template file used when rendering changelog entries. Defaults to the built-in template or ``[changelog].template`` when configured. Useful for customising changelog layout.

``--changelog-exclude REGEX``
    Regex pattern for commit subjects to exclude from changelog entries. Repeatable. Patterns from configuration are combined with CLI values.

``--pyproject PATH``
    Path to the project's ``pyproject.toml`` file. Defaults to ``pyproject.toml``.

``--version-path GLOB``
    Glob pattern for files that contain the project version. May be repeated to update multiple locations. Defaults to none, using only the built-in search paths.

``--version-ignore GLOB``
    Glob pattern for paths to exclude from version updates. Defaults to none.

``--commit``
    Create a git commit for the version change. Defaults to ``false``.

``--tag``
    Create a git tag for the new version. Defaults to ``false``.

``--dry-run``
    Display the new version without modifying any files. Defaults to ``false``.

.. note::
   Omitting ``--base`` compares against the last release commit or ``HEAD^``. When ``--commit`` or ``--tag`` is used, the working tree must be clean.

Examples
--------

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright bump --pyproject pyproject.toml --commit --tag

   .. tab-item:: Markdown
      :sync: markdown

      .. markdown::

         ### v1.2.3 -> v1.2.4 (patch)
         - pyproject.toml

   .. tab-item:: Json
      :sync: json

      .. code-block:: json

         {
           "old_version": "1.2.3",
           "new_version": "1.2.4",
           "level": "patch",
           "files": ["pyproject.toml"]
         }

This prints the old and new versions and, when ``--commit`` and ``--tag`` are set, commits and tags the release. Omitting ``--base`` compares against the last release commit or the previous commit (``HEAD^``), and omitting ``--head`` assumes ``HEAD``.

Changelog generation
--------------------
``bumpwright`` can generate Markdown release notes from commits between the base and head references. Use ``--changelog`` to choose an output file and specify a repository URL via ``[changelog].repo_url`` or ``--repo-url`` to link commit hashes. See :doc:`../changelog/index` for template variables, configuration options, and examples.

.. code-block:: toml

   [changelog]
   repo_url = "https://github.com/me/project"

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright bump --changelog CHANGELOG.md

   .. tab-item:: Markdown
      :sync: markdown

      .. markdown::

         ### v1.2.4
         - feat: add amazing change

   .. tab-item:: Json
      :sync: json

      .. code-block:: json

         {
           "changelog": "### v1.2.4\n- feat: add amazing change\n"
         }

Preview changes
---------------

To preview changes without touching the filesystem, combine ``--dry-run`` with a chosen output format:

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright bump --dry-run --format md
         bumpwright bump --dry-run --format json

   .. tab-item:: Markdown
      :sync: markdown

      .. markdown::

         ### v1.2.3 -> v1.2.4 (patch)
         - pyproject.toml

   .. tab-item:: Json
      :sync: json

      .. code-block:: json

         {
           "old_version": "1.2.3",
           "new_version": "1.2.4",
           "level": "patch",
           "confidence": 1.0,
           "reasons": ["added CLI entry 'greet'"],
           "files": ["pyproject.toml"],
           "skipped": []
         }

The ``confidence`` and ``reasons`` fields mirror those shown when running ``bumpwright decide``. ``files`` lists paths that would be updated by the bump, while ``skipped`` records any files ignored by configuration.

Omitting ``--base`` compares against the last release commit or the previous commit (``HEAD^``); leaving out ``--head`` uses the current ``HEAD``.

Full workflow
-------------

A typical release sequence might look like this:

.. code-block:: console

   git checkout -b feature/amazing-change
   # edit code
   git commit -am "feat: add amazing change"
   bumpwright bump --commit --tag
   git push origin HEAD && git push --tags

All commands read configuration from ``bumpwright.toml`` by default. Use ``--config`` to specify an alternate file.

Common errors
-------------

``pyproject.toml`` not found
    Ensure you run the command at the project root or pass ``--pyproject`` with the correct path.

Changes not applied after running
    The ``--dry-run`` flag previews the bump without touching files. Remove it and, if desired, add ``--commit`` and ``--tag`` to persist the change.

Versioned files created or removed
    Call ``bumpwright.versioning.clear_version_file_cache()`` before the next run or change ``--version-path``/``--version-ignore`` patterns so ``bumpwright`` rescans the filesystem.
