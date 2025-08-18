Basic CLI Example
=================

Run ``bumpwright`` against two Git references to see the suggested semantic version bump.

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright decide --format md

   .. tab-item:: Markdown
      :sync: markdown

      .. markdown::

         **bumpwright** suggests: `None`

         (no API-impacting changes detected)

The command compares your baseline with ``HEAD`` and prints the recommended level along with reasons for the decision.
