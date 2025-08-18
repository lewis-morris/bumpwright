CLI Reference
=============

The ``bumpwright`` command-line interface helps manage project version bumps.
For an introduction see :doc:`get-started` and :doc:`concepts/configuration`.

When to use
-----------

Use the CLI to initialise a project, preview upcoming version bumps,
apply the bump, or inspect release history.

Top-level command
-----------------

.. click:: _bumpwright_click:cli
   :prog: bumpwright
   :show-nested:

init
----

Create a baseline release commit.

When to use
^^^^^^^^^^^

Run after setting up a project to start tracking releases.

Common combos
^^^^^^^^^^^^^

* ``bumpwright init --summary table`` – show a summary after initialisation.

.. click:: _bumpwright_click:init
   :prog: bumpwright init

decide
------

Suggest a version bump without modifying files.

When to use
^^^^^^^^^^^

Preview the next version based on commits since the last release.

Common combos
^^^^^^^^^^^^^

* ``bumpwright decide --format md`` – produce Markdown for pull requests.
* ``bumpwright decide --emit-changelog`` – include expected changelog text.

.. click:: _bumpwright_click:decide
   :prog: bumpwright decide

bump
----

Apply a version bump and update project files.

When to use
^^^^^^^^^^^

Update version metadata when preparing a release.

Common combos
^^^^^^^^^^^^^

* ``bumpwright bump --commit --tag`` – commit and tag the new version.
* ``bumpwright bump --dry-run`` – preview the next version without changes.

.. click:: _bumpwright_click:bump
   :prog: bumpwright bump

history – list & rollback releases
---------------------------------

List releases, show statistics, or roll back a tagged release.

When to use
^^^^^^^^^^^

Review past releases or undo an incorrect tag.

Common combos
^^^^^^^^^^^^^

* ``bumpwright history --stats`` – include line change statistics.
* ``bumpwright history --rollback v1.2.3`` – remove a release tag.

.. click:: _bumpwright_click:history
   :prog: bumpwright history

