Configuration Summary
=====================

This table maps configuration options between the command line, ``bumpwright.toml``, and environment variables. Blank cells indicate that no equivalent is available.

.. list-table::
   :header-rows: 1
   :widths: 1 1 1

   * - CLI flag
     - ``bumpwright.toml`` key
     - Environment variable
   * - ``--config``
     - (n/a)
     - ``BUMPWRIGHT_CONFIG``
   * - ``--quiet``
     - (n/a)
     - ``BUMPWRIGHT_QUIET``
   * - ``--verbose``
     - (n/a)
     - ``BUMPWRIGHT_VERBOSE``
   * - ``--summary``
     - (n/a)
     - ``BUMPWRIGHT_SUMMARY``
   * - ``--base``
     - (n/a)
     - ``BUMPWRIGHT_BASE``
   * - ``--head``
     - (n/a)
     - ``BUMPWRIGHT_HEAD``
   * - ``--format``
     - (n/a)
     - ``BUMPWRIGHT_FORMAT``
   * - ``--repo-url``
     - ``[changelog].repo_url``
     - ``BUMPWRIGHT_REPO_URL``
   * - ``--explain``
     - (n/a)
     - ``BUMPWRIGHT_EXPLAIN``
   * - ``--enable-analyser NAME``
     - ``[analysers].<name> = true``
     - ``BUMPWRIGHT_ENABLE_ANALYSER``
   * - ``--disable-analyser NAME``
     - ``[analysers].<name> = false``
     - ``BUMPWRIGHT_DISABLE_ANALYSER``
   * - ``--pyproject``
     - (n/a)
     - ``BUMPWRIGHT_PYPROJECT``
   * - ``--version-path``
     - ``[version].paths``
     - ``BUMPWRIGHT_VERSION_PATH``
   * - ``--version-ignore``
     - ``[version].ignore``
     - ``BUMPWRIGHT_VERSION_IGNORE``
   * - ``--tag``
     - (n/a)
     - ``BUMPWRIGHT_TAG``
   * - ``--dry-run``
     - (n/a)
     - ``BUMPWRIGHT_DRY_RUN``
   * - ``--changelog``
     - ``[changelog].path``
     - ``BUMPWRIGHT_CHANGELOG``
   * - ``--changelog-template``
     - ``[changelog].template``
     - ``BUMPWRIGHT_CHANGELOG_TEMPLATE``
   * - ``--changelog-exclude``
     - ``[changelog].exclude``
     - ``BUMPWRIGHT_CHANGELOG_EXCLUDE``
   * - ``--stats``
     - (n/a)
     - ``BUMPWRIGHT_STATS``
   * - ``--rollback``
     - (n/a)
     - ``BUMPWRIGHT_ROLLBACK``
   * - ``--purge``
     - (n/a)
     - ``BUMPWRIGHT_PURGE``
