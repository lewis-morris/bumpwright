.. code-block:: toml

   [changelog]
   repo_url = "https://github.com/me/project"

Examples
========

Default template
----------------

.. tab-set::

   .. tab-item:: Markdown
       :sync: changelog

       .. markdown::

           ## [v1.2.4] - 2024-04-01 (2024-04-01T12:00:00+00:00)
           [Diff since v1.2.3](https://github.com/me/project/compare/v1.2.3...v1.2.4)
           - [abc1234](https://github.com/me/project/commit/abc1234) feat!: drop old API

           ### Breaking changes
           - drop old API

           ### Contributors
           - [Alice](https://github.com/alice)
           - Bob

   .. tab-item:: Json
       :sync: changelog

       .. code-block:: json

           {
             "version": "v1.2.4",
             "date": "2024-04-01",
             "release_datetime_iso": "2024-04-01T12:00:00+00:00",
             "compare_url": "https://github.com/me/project/compare/v1.2.3...v1.2.4",
             "commits": [
               {
                 "sha": "abc1234",
                 "link": "https://github.com/me/project/commit/abc1234",
                 "subject": "feat!: drop old API"
               }
             ],
             "breaking_changes": ["drop old API"],
             "contributors": [
               {"name": "Alice", "link": "https://github.com/alice"},
               {"name": "Bob"}
             ]
           }

Keep a Changelog-style header
-----------------------------

.. tab-set::

   .. tab-item:: Markdown
       :sync: changelog

       .. markdown::

           [v1.2.4] - 2024-04-01
           =====================

   .. tab-item:: Json
       :sync: changelog

       .. code-block:: json

           {
             "version": "v1.2.4",
             "date": "2024-04-01"
           }

Grouped sections
----------------

.. tab-set::

   .. tab-item:: Markdown
       :sync: changelog

       .. markdown::

           Added
           -----
           - feat: add greeting command

           Fixed
           -----
           - fix: correct greeting typo

   .. tab-item:: Json
       :sync: changelog

       .. code-block:: json

           {
             "added": ["feat: add greeting command"],
             "fixed": ["fix: correct greeting typo"]
           }

Compare link
------------

.. tab-set::

   .. tab-item:: Markdown
       :sync: changelog

       .. markdown::

           [Diff since v1.2.3](https://github.com/me/project/compare/v1.2.3...v1.2.4)

   .. tab-item:: Json
       :sync: changelog

       .. code-block:: json

           {
             "previous_tag": "v1.2.3",
             "version": "v1.2.4",
             "compare_url": "https://github.com/me/project/compare/v1.2.3...v1.2.4"
           }
