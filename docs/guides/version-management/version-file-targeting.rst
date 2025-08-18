Version file targeting
======================

Poetry
------

.. code-block:: toml

   [version]
   paths = ["pyproject.toml"]

Setuptools
----------

.. code-block:: toml

   [version]
   paths = ["setup.cfg"]

Monorepo
--------

.. code-block:: toml

   [version]
   paths = ["packages/*/pyproject.toml"]
   ignore = ["packages/legacy/**"]

Direct Bumpwright to update specific version files.
