Web Route Analyser
==================

Overview
~~~~~~~~

Detects HTTP route changes in Flask or FastAPI apps.

Dependencies
~~~~~~~~~~~~

``Flask`` or ``FastAPI``
    Framework providing HTTP routes

Enable/Disable
~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright --enable-analyser web_routes
         bumpwright --disable-analyser web_routes

   .. tab-item:: Config
      :sync: config

      .. code-block:: toml

         [analysers]
         web_routes = true  # set to false to disable

.. seealso::

   For configuration options, see :doc:`concepts/configuration#analysers`.

Severity Rules
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Change
     - Bump
   * - Added route
     - ``minor``
   * - Removed route
     - ``major``
   * - Added optional param
     - ``minor``
   * - Added required param
     - ``major``
   * - Removed optional param
     - ``minor``
   * - Removed required param
     - ``major``
   * - Param became optional
     - ``minor``
   * - Param became required
     - ``major``

Example
~~~~~~~

.. tab-set::

   .. tab-item:: Diff
      :sync: diff

      .. code-block:: diff

         @@
         @app.get("/users/{user_id}")
         -def get_user(user_id: int):
         -    ...
         +def get_user(user_id: int, verbose: bool = False):
         +    ...

   .. tab-item:: Output
      :sync: output

      .. code-block:: text

         - [MINOR] GET /users/{user_id}: Added optional param 'verbose'
