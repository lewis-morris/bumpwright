First release
=============

Walk through creating an initial release with bumpwright.

#. Initialise bumpwright and create a configuration file.

   .. tab-set::

      .. tab-item:: Console
         :sync: console

         .. code-block:: console

            $ bumpwright init

      .. tab-item:: TOML
         :sync: toml

         .. code-block:: toml

            [tool.bumpwright]
            version_file = "demo.py"

#. Review the suggested version bump before committing.

   .. tab-set::

      .. tab-item:: Console
         :sync: console

         .. code-block:: console

            $ bumpwright decide --format md

      .. tab-item:: Markdown
         :sync: markdown

         .. markdown::

            **bumpwright** suggests: `minor`
            - [MINOR] demo:greet: Added public symbol

#. Create the release and tag it.

     .. code-block:: console
        :caption: Console

        $ bumpwright bump --commit --tag

   See :doc:`../../cli_reference` for more command details.

