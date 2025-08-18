Automatic bump with commit and tag
=================================

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright bump --base v1.0.0 --head HEAD --commit --tag --format md
         bumpwright bump --base v1.0.0 --head HEAD --commit --tag --format json

   .. tab-item:: Markdown
      :sync: markdown

      .. markdown::

         **bumpwright** bumped version: `1.0.0` -> `1.0.1` (patch)

   .. tab-item:: Json
      :sync: json

      .. code-block:: json

         {
           "old_version": "1.0.0",
           "new_version": "1.0.1",
           "level": "patch",
           "files": [],
           "skipped": []
         }
