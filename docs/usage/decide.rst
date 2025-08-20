bumpwright decide
=================

Compare two git references and report the semantic version level they require without making changes.

Primary options
---------------

* ``--base BASE`` – base git reference to compare against.
* ``--head HEAD`` – head git reference.
* ``--format {text,md,json}`` – output style.
* ``--emit-changelog`` – print the expected changelog for the suggested version.
* ``--explain`` – show reasoning behind the suggested bump.
* ``--no-impl-change-patch`` – ignore implementation-only changes to public symbols.
* ``--repo-url URL`` – base repository URL used for commit links in changelog output.
* ``--changelog-template PATH`` – Jinja2 template file for changelog entries.
* ``--changelog-exclude REGEX`` – regex pattern for commit subjects to omit from changelog entries.

Arguments
---------

``--base BASE``
    Base git reference to compare against, for example ``origin/main``. Defaults to the last release commit if available, otherwise the previous commit (``HEAD^``).

``--head HEAD``
    Head git reference. Defaults to ``HEAD``.

``--format {text,md,json}``
    Output style. ``text`` prints plain console output, ``md`` emits Markdown, and ``json`` produces machine-readable data. Defaults to ``text``.

``--emit-changelog``
    Print the expected changelog for the suggested version. Respects changelog configuration and templating options.

``--explain``
    Log detected impacts, applied rules, and chosen bump level.

``--no-impl-change-patch``
    Do not treat implementation-only changes as patch-level impacts.

``--repo-url URL``
    Base repository URL used to build commit links in changelog output. Overrides ``[changelog].repo_url`` when provided. Defaults to none, showing raw commit hashes when unset.

``--changelog-template PATH``
    Jinja2 template file used when rendering changelog entries. Defaults to the built-in template or ``[changelog].template`` when configured. Useful for customising changelog layout.

``--changelog-exclude REGEX``
    Regex pattern for commit subjects to exclude from changelog entries. Repeatable. Patterns from configuration are combined with CLI values.

``--enable-analyser NAME``
    Enable analyser ``NAME`` in addition to configuration. Repeatable. Defaults to none.

``--disable-analyser NAME``
    Disable analyser ``NAME`` even if enabled in configuration. Repeatable. Defaults to none.

Examples
--------

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         # Omitting --head defaults to the current HEAD
         bumpwright decide --base origin/main --format md
         bumpwright decide --base origin/main --format json --emit-changelog

   .. tab-item:: Markdown
      :sync: markdown

      .. markdown::

         **bumpwright** suggests: `minor`
         - added CLI entry 'greet'

   .. tab-item:: Json
      :sync: json

      .. code-block:: json

         {
           "level": "minor",
           "confidence": 1.0,
           "reasons": ["added CLI entry 'greet'"],
           "impacts": [
             {"severity": "minor", "symbol": "cli.new_command", "reason": "added CLI entry 'greet'"}
           ],
           "changelog": "### 0.2.0 - 2023-01-01\n- add greet command\n"
         }

Decision anatomy
----------------

``bumpwright`` can justify its suggestions with ``--explain``. The flag logs
detected impacts and applied rules to ``stderr`` while the chosen level remains
on ``stdout``. This makes it easy to see which default or custom rules produced
each human-friendly reason.

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         $ bumpwright decide --base origin/main --format text --explain
         minor

         Detected impacts:
         - Added public symbol ``cli.new_command`` (rule: added_symbol)
         Applied rules: added_symbol=minor
         Chosen bump level: minor

   .. tab-item:: Markdown
      :sync: markdown

      .. markdown::

         **bumpwright** suggests: `minor`
         - added CLI entry 'greet'

         Detected impacts:
         - Added public symbol ``cli.new_command`` (rule: added_symbol)
         Applied rules: added_symbol=minor
         Chosen bump level: minor

   .. tab-item:: Json
      :sync: json

      .. code-block:: json

         {
           "level": "minor",
           "confidence": 1.0,
           "reasons": ["added CLI entry 'greet'"],
           "impacts": [
             {"severity": "minor", "symbol": "cli.new_command", "reason": "added CLI entry 'greet'"}
           ]
         }
