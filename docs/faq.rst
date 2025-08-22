FAQ & Troubleshooting
=====================

Common issues
-------------

.. dropdown:: No analysers run

   *Cause*: All analysers are disabled or their optional dependencies are missing.

   *Fix*: Enable the required analysers in :doc:`concepts/configuration` and install
   their dependencies using the instructions in :ref:`installation`.

.. dropdown:: Configuration not found

   *Cause*: ``bumpwright.toml`` is missing or located outside the current
   working directory.

   *Fix*: Create the file or pass ``--config`` to specify its path. See
   :doc:`concepts/configuration` for details.

.. dropdown:: Git errors

   *Cause*: Commands are executed outside a Git repository or references such as
   ``--base`` and ``--head`` are unreachable.

   *Fix*: Run inside a valid repository and ensure the required references exist.
   Additional setup tips can be found in :ref:`installation`.

.. dropdown:: Version keeps incrementing

   *Cause*: The version file was modified by a previous run and has not been
   committed or reverted.

   *Fix*: Commit or discard the change before rerunning, or use ``--dry-run`` to
   preview the bump without writing to disk. See :ref:`usage` for details on
   dry runs.

.. dropdown:: Changelog file not created

   *Cause*: ``--changelog`` was supplied without a file path or the destination
   directory does not exist.

   *Fix*: Pass a valid path to ``--changelog`` or create the containing directory
   before running Bumpwright.

.. dropdown:: Template path not found

   *Cause*: The Jinja2 template used for release notes, referenced by ``--changelog-template``, cannot be located.

   *Fix*: Provide the full path to an existing Jinja2 template or add it to the expected
   location so Bumpwright can render the release notes.

FAQ
---

.. dropdown:: Why do I get version conflicts when bumping?

   Conflicting version numbers in files or Git tags can cause bumps to fail.
   Ensure the version defined in your configuration matches the latest tag.
   See :doc:`concepts/configuration` for controlling version sources.

.. dropdown:: How do I check which analysers ran?

   Run with ``--format json`` to inspect analyser impacts or review your
   configuration to see which analysers are enabled. The :doc:`cli_reference`
   describes all available command-line options.

.. dropdown:: Can I simulate a bump without writing to disk?

   Yes. Run with ``--dry-run`` to preview changes without modifying files.
   ``--dry-run`` still respects ``--changelog`` for path resolution but does
   not write any files. The :ref:`usage` guide explains how to combine this
   with other options.

.. dropdown:: Why do I see Git errors about missing references?

   Bumpwright compares two Git references. Fetch all remote branches and tags
   so the specified ``--base`` and ``--head`` exist. See :ref:`installation`
   for repository setup tips.

