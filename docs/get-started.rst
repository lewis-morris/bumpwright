Get Started
===========

.. _quickstart:

Set up a tiny project and run Bumpwright in minutes. See :ref:`recipe-first-release` for an end-to-end release and :ref:`recipe-dry-run` for a comparison of dry runs with applying changes.

.. _installation:

Install
-------

Requires Python 3.11 or later.

.. code-block:: console
   :caption: Console

   pip install bumpwright

Initialise
----------

Create a minimal project and baseline release commit.

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         mkdir demo && cd demo
         git init
         cat > pyproject.toml <<'EOF2'
         [project]
         name = "demo"
         version = "0.1.0"
         EOF2
         cat > bumpwright.toml <<'EOF'
         [project]
         public_roots=['demo']

         [changelog]
         repo_url = "https://github.com/USER/REPO"
         EOF
         mkdir demo
         echo "def greet() -> str:\n    return 'hi'\n" > demo/__init__.py
         git add .
         git commit -m "feat: add greet helper"
         bumpwright init --summary

   .. tab-item:: Markdown
      :sync: markdown

      .. markdown::

         ### Created baseline release commit

         | Field                  | Value |
         | ---------------------- | ----- |
         | Version                | 0.1.0 |
         | Public symbols         | 1     |
         | Changes since baseline | 0     |

   .. tab-item:: JSON
      :sync: json

      .. code-block:: json

         {
           "version": "0.1.0",
           "public_symbols": 1,
           "changes_since_baseline": 0
         }

.. seealso::

   For a deeper tour of available settings, see :doc:`concepts/configuration`.

Make a change
-------------

.. code-block:: bash
   :caption: Console

   echo "def farewell() -> str:\n    return 'bye'\n" > demo/extra.py
   git add demo/extra.py
   git commit -m "feat: add farewell"

Decide the bump
---------------

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright decide
         bumpwright suggests: minor
         - [MINOR] extra:farewell: Added public symbol

   .. tab-item:: Markdown
      :sync: markdown

      .. markdown::

         **bumpwright** suggests: `minor`
         - [MINOR] extra:farewell: Added public symbol

   .. tab-item:: JSON
      :sync: json

      .. code-block:: json

         {
           "level": "minor",
           "confidence": 1.0,
           "reasons": ["extra:farewell: Added public symbol"],
           "impacts": []
         }

Bumpwright inspects the public API and recommends the next semantic version.

.. seealso::

   Learn how bumpwright decides bump levels in :doc:`concepts/versioning`.

Apply the bump
--------------

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright bump --commit --repo-url https://github.com/USER/REPO
         bumpwright bumped version: 0.1.0 -> 0.2.0 (minor)
         Updated files:
         - pyproject.toml
         Skipped files:
         - demo/__init__.py

   .. tab-item:: Markdown
      :sync: markdown

      .. markdown::

         **bumpwright** bumped version: `0.1.0` -> `0.2.0` (minor)

         Updated files:
         - `pyproject.toml`

         Skipped files:
         - `demo/__init__.py`

   .. tab-item:: JSON
      :sync: json

      .. code-block:: json

         {
           "old_version": "0.1.0",
           "new_version": "0.2.0",
           "level": "minor",
           "confidence": 1.0,
           "reasons": ["extra:farewell: Added public symbol"],
           "files": ["pyproject.toml"],
           "skipped": ["demo/__init__.py"]
         }

See :doc:`guides/basics/command-summary` for a table of core commands.
Learn how to generate release notes in :doc:`changelog/index`.

Next steps
----------

- Configure behaviour with :doc:`concepts/configuration`.
- Explore common workflows in :doc:`guides/recipes`.

Flow
----

Visualise the release pipeline from commit to publication.

.. mermaid::

   %%{init: {'theme': 'dark'}}%%
   flowchart LR
      commit[Commit] --> decide[Decide]
      decide --> bump[Bump/Tag]
      bump --> release[Release]

.. _usage:

Usage and commands
------------------

The ``bumpwright`` command-line interface provides tools to manage project versions based on public API changes. By default, the ``bump`` subcommand compares the current commit against the last release commit, or the previous commit (``HEAD^``) when no release exists. This section lists shared options and links to individual command guides.

Global options
~~~~~~~~~~~~~~

``--config``
    Path to the configuration file. Defaults to ``bumpwright.toml`` in the current working directory.

Commands
~~~~~~~~

.. toctree::
   :maxdepth: 1

   usage/init
   usage/decide
   usage/bump
   usage/history
