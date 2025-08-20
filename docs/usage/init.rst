init – create a baseline
========================

Record an empty ``chore(release): initialise baseline`` commit so that future runs of bumpwright have a starting point for comparisons. Run this once when first adopting bumpwright or after importing an existing project without prior release commits.

Primary options
---------------

* ``--summary [table|json]`` – Show project summary after initialisation in the chosen format.
  Must be followed by ``table`` or ``json``.

Examples
--------

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright init --summary table

   .. tab-item:: Markdown
      :sync: markdown

      .. markdown::

         Created baseline release commit.

         +------------------------+------------------+
         | Version                | 0.1.0            |
         | Public symbols         | 1                |
         | Changes since baseline | 0                |
         +------------------------+------------------+
         Public symbols:
           - __init__:foo
         No API-impacting changes since baseline.


   .. tab-item:: Json
      :sync: json

      .. code-block:: json

         {
           "version": "0.1.0",
           "public_symbols": ["__init__:foo"],
           "changes": []
         }

See :doc:`../guides/basics/first-release` for a step-by-step guide.
