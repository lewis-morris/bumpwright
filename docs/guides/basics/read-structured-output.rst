Read structured output
======================

.. tab-set::

   .. tab-item:: Console
      :sync: console

      .. code-block:: console

         bumpwright decide --format json | jq -r '.level'

   .. tab-item:: Output
      :sync: output

      .. code-block:: text

         minor

Consume structured decisions.
