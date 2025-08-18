.. _analyser-template:

Analyser Name
=============

Overview
~~~~~~~~
Briefly describe what the analyser checks.

Dependencies
~~~~~~~~~~~~
List any required packages or state ``None``.

Enable/Disable
~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Console

      .. code-block:: bash

         bumpwright --enable-analyser NAME
         bumpwright --disable-analyser NAME

   .. tab-item:: Config

      .. code-block:: toml

         [analysers]
         NAME = true

.. seealso::

   For configuration options, see :doc:`concepts/configuration#analysers`.

Severity Rules
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Change
     - Bump
   * - Example change
     - ``minor``

Example
~~~~~~~

.. tab-set::

   .. tab-item:: Diff

      .. code-block:: diff

         @@
         - old
         + new

   .. tab-item:: Output

      .. code-block:: text

         - [MINOR] Description of the change
