Migrations Analyser
===================

Overview
~~~~~~~~

Scans Alembic migrations for schema impacts.

Dependencies
~~~~~~~~~~~~

``Alembic``
    Manage database schema migrations

Enable/Disable
~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright --enable-analyser migrations
         bumpwright --disable-analyser migrations

   .. tab-item:: Config
      :sync: config

      .. code-block:: toml

         [analysers]
         migrations = true  # set to false to disable

         [migrations]
         paths = ["migrations"]

.. seealso::

   For configuration options, see :doc:`concepts/configuration#analysers`.

Severity Rules
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Change
     - Bump
   * - Dropped column
     - ``major``
   * - Added non-nullable column without default
     - ``major``
   * - Added column
     - ``minor``
   * - Added index
     - ``minor``

Example
~~~~~~~

.. tab-set::

   .. tab-item:: Diff
      :sync: diff

      .. code-block:: diff

         @@
         def upgrade():
         -    pass
         +    op.add_column("users", sa.Column("email", sa.String(), nullable=False))

   .. tab-item:: Output
      :sync: output

      .. code-block:: text

         - [MAJOR] migrations/20240401_add_email.py: Added non-nullable column
