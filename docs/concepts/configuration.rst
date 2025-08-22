Configuration Reference
=======================

``bumpwright`` reads settings from ``bumpwright.toml``. Missing sections fall
back to built-in defaults. Use ``--config`` to point to an alternative file.

.. note::
   Environment variables prefixed with ``BUMPWRIGHT_`` provide default values
   for CLI flags. See :ref:`config-envvars` for the full list.

For a side-by-side comparison of CLI flags, configuration keys, and environment
variables, see :doc:`../configuration_summary`.

.. _config-overview:

Configuration overview
----------------------

A ``bumpwright.toml`` file is divided into thematic sections that mirror the
tool's major features. Each section groups related options controlling project
scope, analysis behaviour, or release outputs. The table below provides a quick
map before diving into the detailed references.

.. list-table:: Configuration sections
   :header-rows: 1

   * - Section
     - Purpose
     - Category
   * - :ref:`Project <config-project>`
     - Define the package roots and visibility rules.
     - Project
   * - :ref:`Ignore <config-ignore>`
     - Exclude paths from analysis.
     - Project
   * - :ref:`Rules <config-rules>`
     - Override default bump levels for API changes.
     - Project
   * - :ref:`Analysers <config-analysers>`
     - Enable and configure API analysers.
     - Analysis
   * - :ref:`Migrations <config-migrations>`
     - Locate Alembic migration directories.
     - Analysis
   * - :ref:`OpenAPI <config-openapi>`
     - Configure OpenAPI specification paths.
     - Analysis
   * - :ref:`Version <config-version>`
     - Control version file detection and scheme.
     - Output
   * - :ref:`Changelog <config-changelog>`
     - Configure changelog generation.
     - Output

.. _config-quick-setup:

Quick setup
-----------

Create ``bumpwright.toml`` in the project root and enable any analysers you
need:

.. code-block:: toml

   [project]
   package = "my_package"

   [analysers]
   cli = true

Run ``bumpwright bump --base v1.0.0 --head HEAD`` to compare revisions. See
:ref:`quickstart` for a walkthrough.

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright bump --base v1.0.0 --head HEAD

   .. tab-item:: Output
      :sync: output

      .. code-block:: text

         bumpwright suggests: minor

.. _config-reference:

Reference
---------

All configuration keys are grouped by section below. Each block shows default
values and accepted types.

.. _config-project:

Project
~~~~~~~

.. code-block:: toml

   [project]
   package = ""
   public_roots = ["."]
   private_prefixes = ["_"]
   extra_public_files = ["README.*", "docs/**/*.rst"]

.. list-table::
   :header-rows: 1

   * - Key
     - Default
     - CLI flag
   * - ``package``
     - ``""``
     - (none)
   * - ``public_roots``
     - ``["."]``
     - (none)
   * - ``private_prefixes``
     - ``["_"]``
     - (none)
   * - ``extra_public_files``
     - ``["README.*", "docs/**/*.rst"]``
     - (none)

package
    Importable package containing the project's code. When empty the repository layout is used.
public_roots
    Paths whose contents constitute the public API. Any modified Python file
    within these roots triggers a patch bump, even if only private helpers
    change.
private_prefixes
    Symbol prefixes treated as private and ignored during API analysis.
extra_public_files
    Additional glob patterns for files that trigger a patch bump when modified.

.. _config-ignore:

Ignore
~~~~~~

.. code-block:: toml

   [ignore]
   paths = ["tests/**", "examples/**", "scripts/**"]

.. list-table::
   :header-rows: 1

   * - Key
     - Default
     - CLI flag
   * - ``paths``
     - ``["tests/**", "examples/**", "scripts/**"]``
     - (none)

paths
    Glob patterns excluded from analysis.

.. _config-rules:

Rules
~~~~~

``bumpwright`` detects common public API changes and assigns default semantic
version bumps:

Added public symbol
    ``minor``
Removed public symbol
    ``major``
Added required parameter
    ``major``
Added optional parameter
    ``minor``
Removed required parameter
    ``major``
Removed optional parameter
    ``minor``
Parameter kind changed
    ``major``
Parameter default added or changed
    ``minor``
Parameter default removed
    ``major``
Return type changed
    ``minor`` *
Parameter annotation changed
    ``patch`` *
Implementation changed
    ``patch`` *

Entries marked with ``*`` can be overridden in ``bumpwright.toml`` via the
``[rules]`` section:

.. code-block:: toml

   [rules]
   return_type_change = "major"
   param_annotation_change = "minor"
   implementation_change = "minor"

.. list-table::
   :header-rows: 1

   * - Key
     - Default
     - CLI flag
   * - ``return_type_change``
     - ``"minor"``
     - (none)
   * - ``param_annotation_change``
     - ``"patch"``
     - (none)
   * - ``implementation_change``
     - ``"patch"``
     - (none)

.. _config-rules-return-type-change:

return_type_change
    Bump level when a function's return type changes.
.. _config-rules-param-annotation-change:

param_annotation_change
    Bump level for parameter annotation changes.
.. _config-rules-implementation-change:

implementation_change
    Bump level when a public symbol's implementation changes without altering
    its signature.

Examples
^^^^^^^^

Removing a public symbol triggers a major bump:

.. tab-set::

   .. tab-item:: Before
      :sync: before

      .. code-block:: python

         def add(a: int, b: int) -> int:
             return a + b

   .. tab-item:: After
      :sync: after

      .. code-block:: python

         # ``add`` removed

Changing a return type triggers a minor bump by default:

.. tab-set::

   .. tab-item:: Before
      :sync: before

      .. code-block:: python

         def greet() -> str:
             return "hi"

   .. tab-item:: After
      :sync: after

      .. code-block:: python

         def greet() -> int:
             return 1

.. _config-analysers:

Analysers
~~~~~~~~~

.. code-block:: toml

   [analysers]
   cli = false
   grpc = false
   web_routes = false
   migrations = false
   openapi = false
   graphql = false

.. list-table::
   :header-rows: 1

   * - Key
     - Default
     - CLI flag
   * - ``cli``
     - ``false``
     - ``--enable-analyser cli``
   * - ``grpc``
     - ``false``
     - ``--enable-analyser grpc``
   * - ``web_routes``
     - ``false``
     - ``--enable-analyser web_routes``
   * - ``migrations``
     - ``false``
     - ``--enable-analyser migrations``
   * - ``openapi``
     - ``false``
     - ``--enable-analyser openapi``
   * - ``graphql``
     - ``false``
     - ``--enable-analyser graphql``

cli
    Detects changes to command-line interfaces implemented with ``argparse`` or ``click``.
grpc
    Detects gRPC service and method changes in ``.proto`` files.
web_routes
    Tracks additions or removals of web routes in frameworks such as Flask or FastAPI.
migrations
    Scans Alembic migrations for schema impacts.
openapi
    Detects changes to OpenAPI specification files.
graphql
    Detects GraphQL schema changes.

.. _config-migrations:

Migrations
~~~~~~~~~~

.. code-block:: toml

   [migrations]
   paths = ["migrations"]

paths
    Default: ``["migrations"]``
    Directories containing Alembic migration scripts to inspect.

.. _config-openapi:

OpenAPI
~~~~~~~

.. code-block:: toml

   [openapi]
   paths = ["openapi.yaml", "openapi.yml", "openapi.json"]

paths
    Default: ``["openapi.yaml", "openapi.yml", "openapi.json"]``
    Paths to OpenAPI specification documents.

.. _config-version:

Version
~~~~~~~

.. code-block:: toml

   [version]
   paths = [
       "pyproject.toml",
       "setup.py",
       "setup.cfg",
       "**/__init__.py",
       "**/version.py",
       "**/_version.py",
   ]
   ignore = [
       "build/**",
       "dist/**",
       "*.egg-info/**",
       ".eggs/**",
       ".venv/**",
       "venv/**",
       ".env/**",
       "**/__pycache__/**",
   ]
   scheme = "semver"

.. list-table::
   :header-rows: 1

   * - Key
     - Default
     - CLI flag
   * - ``paths``
     - ``["pyproject.toml", "setup.py", "setup.cfg", "**/__init__.py", "**/version.py", "**/_version.py"]``
     - ``--version-path``
   * - ``ignore``
     - ``["build/**", "dist/**", "*.egg-info/**", ".eggs/**", ".venv/**", "venv/**", ".env/**", "**/__pycache__/**"]``
     - ``--version-ignore``
   * - ``scheme``
     - ``"semver"``
     - (none)

paths
    Glob patterns scanned for version declarations.
ignore
    Glob patterns appended to the default exclusion list for version replacement.
scheme
    Versioning scheme used when bumping. Supported values include ``"semver"`` and ``"calver"``.

.. _config-changelog:

Changelog
~~~~~~~~~

.. code-block:: toml

   [changelog]
   path = ""
   template = ""
   exclude = []
   repo_url = ""

.. list-table::
   :header-rows: 1

   * - Key
     - Default
     - CLI flag
   * - ``path``
     - ``""``
     - ``--changelog``
   * - ``template``
     - ``""``
     - ``--changelog-template``
   * - ``exclude``
     - ``[]``
     - ``--changelog-exclude``
   * - ``repo_url``
     - ``""``
     - ``--repo-url``

path
    Changelog file location. Empty string disables generation.
template
    Jinja2 template file. Empty string uses the built-in template.
exclude
    Regular expressions for commit subjects to omit.
repo_url
    Base repository URL for commit and compare links.

.. _config-examples:

Examples
--------

Custom version rules
~~~~~~~~~~~~~~~~~~~~

.. code-block:: toml

   [rules]
   return_type_change = "major"

Ignore paths
~~~~~~~~~~~~

.. code-block:: toml

   [ignore]
   paths = ["tests/**", "examples/**"]

Version file locations
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: toml

   [version]
   paths = ["pyproject.toml", "setup.py", "src/pkg/__init__.py"]
   ignore = ["examples/**"]
   scheme = "semver"

Automatic bump with commit and tag
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a walkthrough that commits and tags the new version automatically, see
:doc:`guides/version-management/automatic-bump-commit-tag`.

.. _config-envvars:

Environment variables
---------------------

``bumpwright`` reads defaults for many CLI flags from environment variables.

.. list-table::
   :header-rows: 1

   * - Variable
     - Default
     - CLI flag
     - Used by
   * - ``BUMPWRIGHT_CONFIG``
     - ``bumpwright.toml``
     - ``--config``
     - all
   * - ``BUMPWRIGHT_QUIET``
     - ``False``
     - ``--quiet``
     - all
   * - ``BUMPWRIGHT_VERBOSE``
     - ``False``
     - ``--verbose``
     - all
   * - ``BUMPWRIGHT_SUMMARY``
     - ``None``
     - ``--summary``
     - init
   * - ``BUMPWRIGHT_BASE``
     - last release or ``HEAD^``
     - ``--base``
     - decide, bump
   * - ``BUMPWRIGHT_HEAD``
     - ``HEAD``
     - ``--head``
     - decide, bump
   * - ``BUMPWRIGHT_FORMAT``
     - ``text``
     - ``--format``
     - decide, bump, history
   * - ``BUMPWRIGHT_REPO_URL``
     - ``None``
     - ``--repo-url``
     - decide, bump
   * - ``BUMPWRIGHT_EXPLAIN``
     - ``False``
     - ``--explain``
     - decide, bump
   * - ``BUMPWRIGHT_ENABLE_ANALYSER``
     - ``-``
     - ``--enable-analyser``
     - decide, bump
   * - ``BUMPWRIGHT_DISABLE_ANALYSER``
     - ``-``
     - ``--disable-analyser``
     - decide, bump
   * - ``BUMPWRIGHT_PYPROJECT``
     - ``pyproject.toml``
     - ``--pyproject``
     - bump
   * - ``BUMPWRIGHT_VERSION_PATH``
     - ``-``
     - ``--version-path``
     - bump
   * - ``BUMPWRIGHT_VERSION_IGNORE``
     - ``-``
     - ``--version-ignore``
     - bump
   * - ``BUMPWRIGHT_TAG``
     - ``False``
     - ``--tag``
     - bump
   * - ``BUMPWRIGHT_DRY_RUN``
     - ``False``
     - ``--dry-run``
     - bump
   * - ``BUMPWRIGHT_CHANGELOG``
     - ``None``
     - ``--changelog``
     - bump
   * - ``BUMPWRIGHT_CHANGELOG_TEMPLATE``
     - ``None``
     - ``--changelog-template``
     - decide, bump
   * - ``BUMPWRIGHT_CHANGELOG_EXCLUDE``
     - ``-``
     - ``--changelog-exclude``
     - decide, bump
   * - ``BUMPWRIGHT_STATS``
     - ``False``
     - ``--stats``
     - history
   * - ``BUMPWRIGHT_ROLLBACK``
     - ``None``
     - ``--rollback``
     - history
   * - ``BUMPWRIGHT_PURGE``
     - ``False``
     - ``--purge``
     - history

``BUMPWRIGHT_CONFIG``
    Path to configuration file.

``BUMPWRIGHT_QUIET``
    Only display warnings and errors.

``BUMPWRIGHT_VERBOSE``
    Show debug messages.

``BUMPWRIGHT_SUMMARY``
    Show project summary after initialisation.

``BUMPWRIGHT_BASE``
    Base git reference when auto-deciding the level.

``BUMPWRIGHT_HEAD``
    Head git reference.

``BUMPWRIGHT_FORMAT``
    Output style for CLI commands.

``BUMPWRIGHT_REPO_URL``
    Base repository URL for linking commit hashes in Markdown output.

``BUMPWRIGHT_EXPLAIN``
    Show reasoning behind the selected bump level.

``BUMPWRIGHT_ENABLE_ANALYSER``
    Enable analyser names in addition to configuration.

``BUMPWRIGHT_DISABLE_ANALYSER``
    Disable analyser names even if configured.

``BUMPWRIGHT_PYPROJECT``
    Path to the project's ``pyproject.toml`` file.

``BUMPWRIGHT_VERSION_PATH``
    Additional glob pattern for files containing the project version.

``BUMPWRIGHT_VERSION_IGNORE``
    Glob pattern for files to exclude from version updates.

``BUMPWRIGHT_TAG``
    Create a git tag for the new version.

``BUMPWRIGHT_DRY_RUN``
    Display the new version without modifying any files.

``BUMPWRIGHT_CHANGELOG``
    Append release notes to a file or stdout when set to ``-``.

``BUMPWRIGHT_CHANGELOG_TEMPLATE``
    Jinja2 template file for changelog entries.

``BUMPWRIGHT_CHANGELOG_EXCLUDE``
    Regex pattern for commit subjects to exclude from the changelog.

``BUMPWRIGHT_STATS``
    Include line change statistics between successive tags.

``BUMPWRIGHT_ROLLBACK``
    Delete a tag and restore files to the previous commit.

``BUMPWRIGHT_PURGE``
    Remove all bumpwright release tags and commits.

.. _config-cli-equivalents:

CLI equivalents
---------------

Many configuration keys have corresponding command-line flags. For a complete
mapping, see the :doc:`cli_reference`.

