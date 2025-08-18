OpenAPI Analyser
================

Overview
~~~~~~~~

Detects changes in OpenAPI specification files.

Dependencies
~~~~~~~~~~~~

``PyYAML``
    Parse YAML-formatted OpenAPI documents

Enable/Disable
~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright --enable-analyser openapi
         bumpwright --disable-analyser openapi

   .. tab-item:: Config
      :sync: config

      .. code-block:: toml

         [analysers]
         openapi = true

         [openapi]
         paths = ["openapi.yaml"]

.. seealso::

   For configuration options, see :doc:`concepts/configuration#analysers`.

Severity Rules
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Change
     - Bump
   * - Added endpoint
     - ``minor``
   * - Removed endpoint
     - ``major``
   * - Added schema
     - ``minor``
   * - Removed schema
     - ``major``
   * - Changed schema definition
     - ``major``

Example
~~~~~~~

.. tab-set::

   .. tab-item:: Diff
      :sync: diff

      .. code-block:: diff

         @@
         paths:
           /pets:
         -    get: {}
         +    post: {}

   .. tab-item:: Output
      :sync: output

      .. code-block:: text

         - [MAJOR] GET /pets: Removed endpoint
         - [MINOR] POST /pets: Added endpoint

