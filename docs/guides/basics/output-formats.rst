Output formats
==============

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright decide --format md
         bumpwright decide --format json

   .. tab-item:: Markdown
      :sync: markdown

      .. markdown::

         **bumpwright** suggests: `minor`
         - added CLI entry 'greet'

   .. tab-item:: Json
      :sync: json

      .. code-block:: json

         {
           "level": "minor",
           "confidence": 1.0,
           "reasons": [],
           "impacts": []
         }
