Recipes
=======

Goal-oriented walkthroughs for common bumpwright workflows.

Library release
---------------

Releasing a Python package and tagging the repository.

**Scenario**
    After merging changes you need a new library version on PyPI.

**Minimal config**

.. code-block:: toml

    [project]
    public_roots = ["src"]
    [analysers]
    cli = true

More options are documented in :doc:`concepts/configuration` and :doc:`analysers/cli`.

**Command sequence**

#. Initialise the repository (run once):

   .. code-block:: console

      bumpwright init

#. Apply the version bump, commit and tag:

   .. code-block:: console

      bumpwright bump --commit --tag

**Expected output**

.. list-table::
   :header-rows: 1

   * - Command
     - Sample output
   * - ``bumpwright init``
     - Creates baseline commit ``v1.2.3``
   * - ``bumpwright bump --commit --tag``
     - Markdown ``### v1.2.4`` and a Git tag

Service deployment
------------------

Checking API compatibility before deploying a web service.

**Scenario**
    CI should block breaking HTTP route changes.

**Minimal config**

.. code-block:: toml

    [analysers]
    web_routes = true

See :doc:`analysers/web_routes` for analyser behaviour.

**Command sequence**

#. Compare against ``origin/main`` in CI:

   .. code-block:: console

      bumpwright decide --base origin/main --format json

#. Deploy only when ``level`` is not ``major``.

**Expected output**

.. list-table::
   :header-rows: 1

   * - Command
     - Sample output
   * - ``bumpwright decide --base origin/main --format json``
     - ``{"level": "minor", "confidence": 1.0}``

Changelog generation
--------------------

Updating a changelog alongside version bumps.

**Scenario**
    Release notes should be appended automatically.

**Minimal config**

.. code-block:: toml

    [changelog]
    path = "CHANGELOG.md"
    repo_url = "https://github.com/me/project"

Configuration details live in :doc:`changelog/index`.

**Command sequence**

#. Preview the changelog locally:

   .. code-block:: console

      bumpwright bump --changelog CHANGELOG.md --dry-run --format md

#. Apply bump, commit, tag and update the changelog:

   .. code-block:: console

      bumpwright bump --changelog CHANGELOG.md --commit --tag --format md

**Expected output**

.. list-table::
   :header-rows: 1

   * - Command
     - Sample output
   * - ``bumpwright bump --changelog CHANGELOG.md --dry-run --format md``
     - ``### v1.2.4\n- feat: add feature``
   * - ``bumpwright bump --changelog CHANGELOG.md --commit --tag --format md``
     - Same as above and a release tag
