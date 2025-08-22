Bumpwright
==========

Bumpwright checks your project's public API to suggest the correct semantic version bump. It compares your code to a baseline and reports whether the next release should be a patch, minor, or major update.

Why
---
- Avoid missed breaking changes when commit messages fall short.
- Automate version numbers and changelog generation.

How
---
- Compare the current commit to a recorded baseline.
- Optional analysers inspect CLIs, web routes, migrations, and more.

Pros
----
- Accurate bump suggestions based on the public API.
- Flexible configuration and pluggable analysers.
- Generates release notes for you.

Cons
----
- Requires a Git baseline commit.
- Static analysis can't cover runtime behaviour.
- Python 3.11+ only.

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
