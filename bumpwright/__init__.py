"""Top-level package for :mod:`bumpwright`.

Exposes the ``main`` entry point used by the command-line interface. The
package is intended primarily for CLI usage rather than direct imports.
"""

from __future__ import annotations

# Import frequently used subpackages so they are exposed as attributes on
# :mod:`bumpwright`.  This allows tests and downstream consumers to monkeypatch
# internals using dotted paths like ``bumpwright.cli.bump`` without triggering
# attribute errors.
from . import cli, versioning
from .api import BumpDecision, decide_project_bump
from .cli import main

__all__ = [
    "__version__",
    "main",
    "cli",
    "versioning",
    "BumpDecision",
    "decide_project_bump",
]

__version__ = "0.3.0"
