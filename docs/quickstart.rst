Quickstart
==========

.. _quickstart:

Copy and paste the steps below to bump your first version.

Prerequisites
-------------

- Python 3.11+
- Git
- A terminal with ``pip`` installed

.. _installation:

Installation
------------

.. code-block:: console

   pip install bumpwright

Initializing the Baseline
-------------------------

Start a demo project and prepare bumpwright for version tracking.

.. code-block:: console

   mkdir demo && cd demo
   git init
   cat > pyproject.toml <<'PY'
   [project]
   name = "demo"
   version = "0.1.0"
   PY
   cat > bumpwright.toml <<'BW'
   [project]
   public_roots=["demo"]
   BW
   mkdir demo
   echo "def greet() -> str:\n    return 'hi'" > demo/__init__.py
   git add .
   git commit -m "feat: add greet helper"
   bumpwright init

Making a Change and Deciding the Version
----------------------------------------

Add a new feature and let bumpwright suggest the appropriate version increment.

.. code-block:: console

   echo "def farewell() -> str:\n    return 'bye'" > demo/extra.py
   git add demo/extra.py
   git commit -m "feat: add farewell"
   bumpwright decide

Expected output:

.. code-block:: console

   bumpwright suggests: minor
   - [MINOR] extra:farewell: Added public symbol

Applying the Bump
-----------------

Apply the suggested version bump and update project files.

.. code-block:: console

   bumpwright bump --commit

Expected output:

.. code-block:: console

   bumpwright bumped version: 0.1.0 -> 0.2.0 (minor)
   Updated files:
   - pyproject.toml

For detailed options see :doc:`cli_reference` and :doc:`concepts/configuration`.
