Command summary
===============

.. list-table:: Core workflow commands
   :header-rows: 1

   * - Step
     - Command
     - Reference
   * - Install
     - ``pip install bumpwright``
     - -
   * - Initialise
     - ``bumpwright init``
     - :ref:`init <cli_reference:init>`
   * - Make a change
     - ``git commit -m "feat: add farewell"``
     - -
   * - Decide the bump
     - ``bumpwright decide``
     - :ref:`decide <cli_reference:decide>`
   * - Apply the bump
     - ``bumpwright bump --commit``
     - :ref:`bump <cli_reference:bump>`
   * - Tag
     - ``bumpwright bump --commit --tag``
     - :ref:`bump <cli_reference:bump>`
   * - History / rollback / purge
     - ``bumpwright history --format md`` / ``bumpwright history --rollback v1.2.3`` / ``bumpwright history --purge``
     - :ref:`history <cli_reference:history>`
