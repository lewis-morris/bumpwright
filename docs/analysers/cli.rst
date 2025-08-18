CLI Analyser
============

Overview
~~~~~~~~

Tracks ``argparse`` or ``click`` command-line interfaces through static analysis.

Dependencies
~~~~~~~~~~~~

None
    Statically analyses code; ``click`` needed only for ``click``-based projects

Enable/Disable
~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright --enable-analyser cli
         bumpwright --disable-analyser cli

   .. tab-item:: Config
      :sync: config

      .. code-block:: toml

         [analysers]
         cli = true  # set to false to disable

.. seealso::

   For configuration options, see :doc:`concepts/configuration#analysers`.

Severity Rules
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Change
     - Bump
   * - Added command
     - ``minor``
   * - Removed command
     - ``major``
   * - Added optional option
     - ``minor``
   * - Added required option
     - ``major``
   * - Removed optional option
     - ``minor``
   * - Removed required option
     - ``major``
   * - Option became optional
     - ``minor``
   * - Option became required
     - ``major``

Example
~~~~~~~

.. tab-set::

   .. tab-item:: Diff
      :sync: diff

      .. code-block:: diff

         @@
         @click.command()
-        def greet(name):
-            ...
+        @click.option("--force", required=True)
+        def greet(name, force):
+            ...

   .. tab-item:: Output
      :sync: output

      .. code-block:: text

         - [MAJOR] greet: Added required option '--force'
