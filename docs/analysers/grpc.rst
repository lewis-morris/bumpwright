gRPC Analyser
=============

Overview
~~~~~~~~

Detects gRPC service and method changes in ``.proto`` files.

Dependencies
~~~~~~~~~~~~

None
    No additional packages required

Enable/Disable
~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright --enable-analyser grpc
         bumpwright --disable-analyser grpc

   .. tab-item:: Config
      :sync: config

      .. code-block:: toml

         [analysers]
         grpc = true  # set to false to disable

.. seealso::

   For configuration options, see :doc:`concepts/configuration#analysers`.

Severity Rules
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Change
     - Bump
   * - Added service
     - ``minor``
   * - Removed service
     - ``major``
   * - Added RPC method
     - ``minor``
   * - Removed RPC method
     - ``major``

Example
~~~~~~~

.. tab-set::

   .. tab-item:: Diff
      :sync: diff

      .. code-block:: diff

         @@
          service Foo {
             rpc Ping (Req) returns (Res);
         +    rpc Pong (Req) returns (Res);
          }

   .. tab-item:: Output
      :sync: output

      .. code-block:: text

         - [MINOR] Foo.Pong: Added RPC method
