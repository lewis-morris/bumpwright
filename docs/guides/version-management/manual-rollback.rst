Manual rollback
===============

Undo a release when a previous version is required.

#. Identify the tag to revert.

     .. code-block:: console
        :caption: Console

        $ git tag --sort=version:refname | tail -n 1
        v1.2.0

#. Revert the release commit.

     .. code-block:: console
        :caption: Console

        $ git revert v1.2.0

#. Reset the version without creating a new tag.

     .. code-block:: console
        :caption: Console

        $ bumpwright bump --set 1.1.0 --no-tag --no-commit

   See :doc:`../../cli_reference` for more options.

