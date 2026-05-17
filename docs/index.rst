Bumpwright
==========

Bumpwright checks your project's public API and related interfaces to suggest the correct release impact. It compares your code to a baseline, decides whether the change is patch-, minor-, or major-level, and then applies that decision using your configured version scheme.

Why
---
- Avoid missed breaking changes when commit messages fall short.
- Automate version numbers and changelog generation across Python and Node-style metadata files.

How
---
- Compare the current commit to a recorded baseline.
- Optional analysers inspect CLIs, web routes, migrations, OpenAPI, GraphQL, gRPC, and JavaScript/TypeScript exports.

Pros
----
- Accurate bump suggestions based on the public API.
- Flexible configuration and pluggable analysers.
- Supports SemVer and CalVer version updates and can generate release notes for you.

Cons
----
- Requires a Git baseline commit.
- Static analysis can't cover runtime behaviour.
- Python 3.11+ runtime for the CLI and analysers.

New to Bumpwright? Start with the :doc:`quickstart`.

.. toctree::
   :caption: Quickstart
   :maxdepth: 1

   quickstart

.. toctree::
   :caption: CLI Reference
   :maxdepth: 1

   cli_reference

.. toctree::
   :caption: Configuration Reference
   :maxdepth: 1

   concepts/configuration
   configuration_summary

.. toctree::
   :caption: Analysers Guide
   :maxdepth: 1

   analysers/index

.. toctree::
   :caption: Versioning Concepts
   :maxdepth: 1

   concepts/versioning

.. toctree::
   :caption: Changelog & Templates
   :maxdepth: 1

   changelog/index

.. toctree::
   :caption: Recipes / How-To Guides
   :maxdepth: 2

   guides/index

.. toctree::
   :caption: FAQ / Troubleshooting
   :maxdepth: 1

   faq

.. toctree::
   :caption: Contributing & Roadmap
   :maxdepth: 1

   contributing
   roadmap
