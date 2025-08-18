.. _recipe-dry-run:

Dry-run vs apply
================

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright decide; echo $?
         bumpwright bump --commit --dry-run

   .. tab-item:: Markdown
      :sync: markdown

      .. markdown::

         **bumpwright** suggests: `minor`
         - [MINOR] demo:greet: Added public symbol
         Exit code: 2
         Would bump to v0.2.0

   .. tab-item:: JSON
      :sync: json

      .. code-block:: json

         {
           "level": "minor",
           "exit_code": 2,
           "reasons": ["demo:greet: Added public symbol"],
           "would_bump_to": "0.2.0"
         }

Compares exit-code signals with a non-destructive dry run.

Exit codes
----------

+-----------+-----------+
| Level     | Exit code |
+===========+===========+
| none      | 0         |
| patch     | 1         |
| minor     | 2         |
| major     | 3         |
+-----------+-----------+
