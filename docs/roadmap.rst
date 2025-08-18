Roadmap
=======

The following items outline potential directions for improving
``bumpwright``. Contributions and discussion are welcome.

Analyser enhancements
---------------------

* Enhanced GraphQL schema diffing
* Deeper OpenAPI specification comparison
* Python type stub analysis to catch interface drift

Ecosystem features
------------------

* Custom analyser hooks with experimental API tagging (docstring tags or an ``@experimental`` decorator) to prevent temporary code from triggering major version bumps
* User-defined severity mappings and thresholds
* Machine-readable (JSON) and rich HTML reports
* Built-in changelog templating and defaults
* Pre-commit integration with sensible defaults
* IDE extensions to surface API changes directly in editors

This roadmap is not exhaustive; ideas and feedback can be proposed
through issue reports or pull requests.

