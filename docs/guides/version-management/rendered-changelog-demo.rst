Rendered changelog demo
=======================

.. tab-set::

   .. tab-item:: Markdown
       :sync: changelog

       .. markdown::

           ## [v0.1.1] - 2024-04-01
           [Diff since v0.1.0](https://github.com/me/project/compare/v0.1.0...v0.1.1)
           - alice
           - bob
           ### Breaking changes
           - removed old API

   .. tab-item:: Json
       :sync: changelog

       .. code-block:: json

           {
             "version": "v0.1.1",
             "date": "2024-04-01",
             "compare_url": "https://github.com/me/project/compare/v0.1.0...v0.1.1",
             "contributors": ["alice", "bob"],
             "breaking_changes": ["removed old API"]
           }

Shows the built-in template and a rendered entry.
