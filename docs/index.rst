bumpwright documentation
========================

.. |coverage| image:: _static/badges/coverage.svg
   :alt: test coverage
.. |version| image:: _static/badges/version.svg
   :alt: latest version
.. |python| image:: _static/badges/python.svg
   :alt: supported Python versions
.. |license| image:: _static/badges/license.svg
   :alt: license

|coverage| |version| |python| |license|

Introduction
------------

Bumpwright is a static analysis tool that compares two Git references and
recommends the appropriate semantic version bump. Unlike tools such as
``bump2version`` or ``python-semantic-release`` that rely on manual hints or
commit messages, Bumpwright inspects the public API itself, making it ideal for
libraries and services that expose stable interfaces.

To get started immediately, try the following commands:

.. code-block:: bash

   bumpwright init
   bumpwright decide

New to Bumpwright? Start with the :doc:`get-started`.

.. grid:: 1 2 2 2
   :gutter: 2

   .. card:: New to Bumpwright?
      :link: get-started
      :link-type: doc

   .. card:: Need configuration details?
      :link: concepts/configuration
      :link-type: doc

   .. card:: Looking for recipes?
      :link: guides/index
      :link-type: doc

   .. card:: CLI reference
      :link: cli_reference
      :link-type: doc

Who is this for?
-----------------

If you're new to release automation, begin with the :doc:`Get Started guide <get-started>`.
Experienced users can dive into the :doc:`Guides <guides/index>` or consult the
:doc:`CLI reference <cli_reference>` directly.

Release workflow at a glance
----------------------------

.. list-table::
   :header-rows: 1

   * - Task
     - Purpose
   * - :doc:`init <usage/init>`
     - Record the current state as a baseline.
   * - :doc:`decide <usage/decide>`
     - Analyse changes and suggest the bump level.
   * - :doc:`bump <usage/bump>`
     - Apply the version change and update files.
   * - :doc:`history <usage/history>`
     - Review previous bump decisions.

Benefits
~~~~~~~~

- **Simplicity** – run a single command to see how your API changed.
- **Flexibility** – enable analysers and override defaults to fit your workflow.
- **Accuracy** – catch breaking changes that commit messages may miss.

Trade-offs
~~~~~~~~~~

- **Baseline reference** – requires a baseline commit to compare against.
- **Static heuristics** – cannot account for runtime behaviour.

Primary use cases
~~~~~~~~~~~~~~~~~

- Library maintainers verifying API stability before release.
- CI/CD pipelines enforcing semantic versioning.
- Release managers reviewing change impact.

.. toctree::
   :maxdepth: 1
   :caption: Get Started

   get-started

.. toctree::
   :maxdepth: 1
   :caption: Usage

   usage/init
   usage/decide
   usage/bump
   usage/history

.. toctree::
   :maxdepth: 1
   :caption: Versioning

   concepts/versioning

.. toctree::
   :maxdepth: 1
   :caption: Configuration

   concepts/configuration

.. toctree::
   :maxdepth: 2
   :caption: Guides

   guides/index
   troubleshooting

.. toctree::
   :maxdepth: 1
   :caption: CI/CD

   ci/github-actions

.. toctree::
   :maxdepth: 1
   :caption: CLI Reference

   cli_reference

.. toctree::
   :maxdepth: 1
   :caption: Changelog

   changelog/index

.. toctree::
   :maxdepth: 1
   :caption: Analysers

   analysers/index

.. toctree::
   :maxdepth: 1
   :caption: Project

   glossary
   contributing
   roadmap

