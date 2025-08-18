Versioning
==========

Default Rules
-------------

By default, ``bumpwright`` maps API changes to version levels.
See :ref:`configuration <config-rules>` for how to adjust these mappings.

.. list-table:: API change → default bump
   :header-rows: 1

   * - API change
     - Default bump
   * - :doc:`Added public symbol </analysers/index>`
     - ``minor``
   * - :doc:`Removed public symbol </analysers/index>`
     - ``major``
   * - :doc:`Added required parameter </analysers/index>`
     - ``major``
   * - :doc:`Added optional parameter </analysers/index>`
     - ``minor``
   * - :doc:`Removed required parameter </analysers/index>`
     - ``major``
   * - :doc:`Removed optional parameter </analysers/index>`
     - ``minor``
   * - :doc:`Parameter kind changed </analysers/index>`
     - ``major``
   * - :doc:`Parameter default added or changed </analysers/index>`
     - ``minor``
   * - :doc:`Parameter default removed </analysers/index>`
     - ``major``

Custom Rules
------------

Some analyser checks expose configuration switches under ``[rules]``.

.. list-table:: Customisable rules
   :header-rows: 1

   * - Rule
     - Default bump
     - ``[rules]`` key
   * - :doc:`Return type changed </analysers/index>`
     - ``minor``
     - ``return_type_change``
   * - :doc:`Parameter annotation changed </analysers/index>`
     - ``patch``
     - ``param_annotation_change``

Example override:

.. code-block:: toml

   [rules]
   return_type_change = "major"
   param_annotation_change = "minor"

Summary
-------

``bumpwright`` supports Semantic Versioning (``SemVer``) and
Calendar Versioning (``CalVer``). Select a scheme via ``[version].scheme``
(:ref:`config-version`); SemVer is the default. CalVer encodes the release
date as ``YYYY.MM.PATCH``.

.. note::

   Release bumps clear prerelease and local/build metadata.

SemVer vs CalVer
----------------

.. tab-set::

   .. tab-item:: SemVer
      :sync: scheme

      Format: ``MAJOR.MINOR.PATCH``

      - major: ``1.2.3`` → ``2.0.0``
      - minor: ``1.2.3`` → ``1.3.0``
      - patch: ``1.2.3`` → ``1.2.4``

   .. tab-item:: CalVer
      :sync: scheme

      Format: ``YYYY.MM.PATCH``

      - major: ``2023.8.3`` → ``2024.1.0``
      - minor: ``2023.8.3`` → ``2023.9.0``
      - patch: ``2023.8.3`` → ``2023.8.4``

CLI
---

Decide the next version (:ref:`cli_reference:decide`):

.. tab-set::

   .. tab-item:: SemVer
      :sync: scheme

      .. code-block:: console

         $ bumpwright decide --format md
         bumpwright suggests: patch

   .. tab-item:: CalVer
      :sync: scheme

      .. code-block:: console

         $ bumpwright --config calver.toml decide --format md
         bumpwright suggests: patch

Apply a bump (:ref:`cli_reference:bump`):

.. tab-set::

   .. tab-item:: SemVer
      :sync: scheme

      .. code-block:: console

         $ bumpwright bump --dry-run --format md
         New version: 1.3.0

   .. tab-item:: CalVer
      :sync: scheme

      .. code-block:: console

         $ bumpwright --config calver.toml bump --dry-run --format md
         New version: 2023.9.0

Glossary
--------

prerelease
   labels like ``-rc.1`` marking early releases.
local/build
   metadata after ``+`` used for build tracking.

See :doc:`concepts/configuration` and :doc:`glossary` for details.

