.. _recipe-first-release:

First release from zero
=======================

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright init
         bumpwright decide --format md
         bumpwright decide --format json
         bumpwright bump --commit --tag --format md
         bumpwright bump --commit --tag --format json

   .. tab-item:: Markdown
      :sync: markdown

      .. markdown::

         Baseline initialised.
         **bumpwright** suggests: `minor`
         - [MINOR] demo:greet: Added public symbol
         **bumpwright** bumped version: `0.1.0` -> `0.2.0` (minor)
         Updated files:
         - `pyproject.toml`
         - `demo.py`
         Tagged v0.2.0

   .. tab-item:: Json
      :sync: json

      .. code-block:: json

         {
           "init": "baseline initialised",
           "decision": {
             "level": "minor",
             "confidence": 1.0,
             "reasons": ["[MINOR] demo:greet: Added public symbol"],
             "impacts": []
           },
           "release": {
             "old_version": "0.1.0",
             "new_version": "0.2.0",
             "level": "minor",
             "files": ["pyproject.toml", "demo.py"]
           }
         }

Initialises the project, evaluates the bump, and creates the release.
