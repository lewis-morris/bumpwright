Changelog configuration and CLI options
=======================================

See :doc:`../concepts/configuration` for general configuration guidance and
:doc:`template` for available template variables.

Each option can be provided as a command-line flag or via the ``[changelog]``
section in ``bumpwright.toml``:

``--changelog [PATH]`` / ``[changelog].path``
    Write release notes to ``PATH`` or ``stdout`` with ``-``.
``--changelog-template PATH`` / ``[changelog].template``
    Use a custom Jinja2 template for the entry.
``--changelog-exclude PATTERN`` / ``[changelog].exclude``
    Exclude commits whose subject matches ``PATTERN`` (repeatable).
``--repo-url URL`` / ``[changelog].repo_url``
    Base repository URL for commit and compare links.
