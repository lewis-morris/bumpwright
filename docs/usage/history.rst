history – list & rollback releases
=================================

Display existing Git tags alongside their version numbers. If the project's
current version differs from the latest tag, a warning is emitted. Output can
be formatted as plain text, Markdown, or JSON, and previous releases may be
rolled back or purged when necessary. Dates default to ISO-8601 in UTC; pass
``--local-time`` for human-readable local output.

Undo a bump
-----------

Reverse a tagged release without touching untracked files:

.. code-block:: console

   bumpwright history --rollback v1.2.3

Primary options
---------------

* ``--format`` – Output style: ``text`` (default), ``md``, or ``json``.
* ``--local-time`` – Render commit dates in the local timezone instead of ISO-8601.
* ``--stats`` – Include line change statistics between successive tags.
* ``--rollback TAG`` – Delete ``TAG`` and restore versioned files to the previous
  commit without touching untracked files. A new commit titled
  ``chore(release): undo TAG`` is created when changes are detected. Remember to
  push the tag deletion and the commit to your remote repository.
* ``--purge`` – Remove all bumpwright release tags and commits, restoring
  versioned files while leaving other commits untouched and requiring the
  project to be reinitialised.

Dry run
-------

Preview release history without modifying the repository. Use ``--local-time``
to convert ISO timestamps to your local timezone.

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright history --stats --local-time
         bumpwright release history:
         - v0.2.0 0.2.0 2024-01-02 00:00:00 +1 -0
         - v0.1.0 0.1.0 2024-01-01 00:00:00

   .. tab-item:: Markdown
      :sync: markdown

      .. code-block:: console

         bumpwright history --format md --stats --local-time

      .. markdown::

         **bumpwright** release history:
         | Tag   | Version | Date               | Stats |
         | ---   | ------- | ----               | ----- |
         | v0.2.0 | 0.2.0  | 2024-01-02 00:00:00 | +1 -0 |
         | v0.1.0 | 0.1.0  | 2024-01-01 00:00:00 |       |

   .. tab-item:: Json
      :sync: json

      .. code-block:: console

         bumpwright history --format json --stats --local-time

      .. code-block:: json

         [
           {
             "tag": "v0.2.0",
             "version": "0.2.0",
             "date": "2024-01-02 00:00:00",
             "stats": {"insertions": 1, "deletions": 0}
           },
           {
             "tag": "v0.1.0",
             "version": "0.1.0",
             "date": "2024-01-01 00:00:00"
           }
         ]

Rollback
--------

Undo a tagged release by supplying the tag name to ``--rollback``. The command
deletes the tag locally and reverts only the versioned files and changelog to
their previous state. All other files remain untouched, and a commit recording
the reversal is created.

.. code-block:: console

   bumpwright history --rollback v1.2.3

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright history --stats --format md
         bumpwright history --rollback v1.2.4

   .. tab-item:: Output (text)
      :sync: text

      .. code-block:: text

         Rolled back to v1.2.3

   .. tab-item:: JSON
      :sync: json

      .. code-block:: json

         {"action":"rollback","to":"v1.2.3"}

Afterward, push both the commit and tag deletion to your remote repository:

.. code-block:: console

   git push origin HEAD
   git push origin :v1.2.3

Purge
-----

Remove all bumpwright-generated releases and tags, restoring versioned files to
their prior state and leaving the repository uninitialised. Push the tag
deletions to your remote repository after running the command:

.. code-block:: console

   bumpwright history --purge

.. code-block:: console

   git push origin --delete <tag>
