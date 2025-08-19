CLI Reference
=============

Details for each command. See :doc:`quickstart` for a walkthrough.

Top-level command
-----------------

.. click:: _bumpwright_click:cli
   :prog: bumpwright
   :show-nested:

init
----

Create a baseline release commit.

.. click:: _bumpwright_click:init
   :prog: bumpwright init

decide
------

Suggest a version bump without modifying files.

.. click:: _bumpwright_click:decide
   :prog: bumpwright decide

bump
----

Apply the suggested version and update files.

.. click:: _bumpwright_click:bump
   :prog: bumpwright bump

history
-------

List previous bumps or roll back a release.

.. click:: _bumpwright_click:history
   :prog: bumpwright history
