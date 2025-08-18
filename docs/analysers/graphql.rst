GraphQL Analyser
================

Overview
~~~~~~~~

Detects changes in GraphQL schema definitions.

Dependencies
~~~~~~~~~~~~

``graphql-core``
    Parse and validate GraphQL schemas

Enable/Disable
~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright --enable-analyser graphql
         bumpwright --disable-analyser graphql

   .. tab-item:: Config
      :sync: config

      .. code-block:: toml

         [analysers]
         graphql = true  # set to false to disable

.. seealso::

   For configuration options, see :doc:`concepts/configuration#analysers`.

Severity Rules
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Change
     - Bump
   * - Added type
     - ``minor``
   * - Removed type
     - ``major``
   * - Added field
     - ``minor``
   * - Removed field
     - ``major``

Example
~~~~~~~

.. tab-set::

   .. tab-item:: Diff
      :sync: diff

      .. code-block:: diff

         @@
         -  type User { id: ID! }
         +  type User { id: ID!, email: String }

   .. tab-item:: Output
      :sync: output

      .. code-block:: text

         - [MINOR] User.email: Added field 'email'

