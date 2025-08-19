Analyzers Guide
===============

Analyzers inspect different facets of your project to detect API changes.
Bumpwright ships optional analyzers for the :doc:`CLI <cli>`, :doc:`gRPC <grpc>` services,
:doc:`web routes <web_routes>`, :doc:`database migrations <migrations>`, :doc:`OpenAPI documents <openapi>`
and :doc:`GraphQL schemas <graphql>`. The table below lists each analyzer, the key used
to configure it, and the CLI flag to enable it for a single run.

.. list-table:: Available analyzers
   :header-rows: 1

   * - Analyser
     - Configuration key
     - CLI flag
   * - :doc:`CLI <cli>`
     - ``cli``
     - ``--enable-analyser cli``
   * - :doc:`gRPC <grpc>`
     - ``grpc``
     - ``--enable-analyser grpc``
   * - :doc:`Web routes <web_routes>`
     - ``web_routes``
     - ``--enable-analyser web_routes``
   * - :doc:`Migrations <migrations>`
     - ``migrations``
     - ``--enable-analyser migrations``
   * - :doc:`OpenAPI <openapi>`
     - ``openapi``
     - ``--enable-analyser openapi``
   * - :doc:`GraphQL <graphql>`
     - ``graphql``
     - ``--enable-analyser graphql``

Enable analyzers in ``bumpwright.toml``:

.. code-block:: toml

   [analysers]
   cli = true        # enable CLI analysis
   grpc = true       # enable gRPC analysis
   web_routes = true # enable web route analysis
   migrations = true # enable migrations analysis
   openapi = true    # enable OpenAPI analysis
   graphql = true    # enable GraphQL analysis

   [migrations]
   paths = ["migrations"]  # directories with Alembic scripts

   [openapi]
   paths = ["openapi.yaml"]

You can also toggle analyzers per invocation with the command-line flags
``--enable-analyser`` and ``--disable-analyser``.

Python API analyser
-------------------

The default analyser inspects Python modules to track changes to the public
API. If a module defines ``__all__``, those names form the public interface.
Otherwise, all module- or class-level members whose names do not start with
``_`` are considered public. Names with leading underscores, including dunder
methods, are ignored.

.. code-block:: python

   __all__ = ["foo", "Bar"]

   def foo(): ...
   def _hidden(): ...

   class Bar:
       def baz(self): ...
       def _private(self): ...

The analyser includes ``foo`` and ``Bar.baz`` in the public API, while
``_hidden`` and ``Bar._private`` are excluded.

.. toctree::
   :caption: Analysers
   :maxdepth: 1

   cli
   grpc
   web_routes
   migrations
   openapi
   graphql

- :doc:`cli` – Track command-line interface changes.
- :doc:`grpc` – Detect gRPC service or method updates.
- :doc:`web_routes` – Monitor HTTP route and parameter changes.
- :doc:`migrations` – Scan database migrations for schema impacts.
- :doc:`openapi` – Compare OpenAPI specs for endpoint drift.
- :doc:`graphql` – Flag GraphQL schema alterations.
