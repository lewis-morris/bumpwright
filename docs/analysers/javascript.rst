JavaScript and TypeScript Analyser
==================================

The ``javascript`` analyser inspects exported JavaScript and TypeScript
symbols. It is opt-in and does not require Node.js to run. When
``package.json`` declares ``main`` or ``exports`` and no explicit
``entrypoints`` are configured, Bumpwright treats those files as the public
surface instead of scanning every matching file under ``roots``.

Enable it in ``bumpwright.toml``:

.. code-block:: toml

   [analysers]
   javascript = true

   [javascript]
   roots = ["src", "lib", "."]
   extensions = [".js", ".mjs", ".cjs", ".ts", ".tsx", ".d.ts"]
   entrypoints = []

What It Detects
---------------

The analyser recognises common ESM and CommonJS export patterns:

.. code-block:: javascript

   export function run(task, options = {}) {}
   export class Client {}
   export const version = "1.0.0";
   export type User = { id: string };
   export interface Options { dryRun?: boolean }
   export { run as execute };

   exports.run = function (task) {};
   module.exports.stop = (code = 0) => code;
   module.exports = { health, alias: runAlias };

It classifies changes using semantic-version rules:

.. list-table::
   :header-rows: 1

   * - Change
     - Bump
   * - Removed export
     - ``major``
   * - Added export
     - ``minor``
   * - Added required parameter
     - ``major``
   * - Added optional/default/rest parameter
     - ``minor``
   * - Removed accepted parameter
     - ``major``
   * - Changed exported ``type``/``interface``/``enum``
     - ``major``
   * - Implementation-only change to an exported symbol
     - ``patch``

Configuration
-------------

``package_json``
    Default: ``"package.json"``. Used to discover package ``main``,
    ``module``, ``types``, ``typings``, ``browser`` and ``exports`` entrypoints.

``roots``
    Default: ``["src", "lib", "."]``. Directories scanned for public modules.

``extensions``
    Default: ``[".js", ".mjs", ".cjs", ".ts", ".tsx", ".d.ts"]``.
    File extensions included in the scan.

``entrypoints``
    Default: ``[]``. Specific files to include in addition to files under
    ``roots``. When empty, package ``main``/``exports`` metadata can restrict
    scanning to declared package entrypoints.

Limitations
-----------

The first implementation uses static source inspection. It does not run a
bundler, evaluate conditional exports, or resolve re-export graphs across
packages. Dynamic exports may need an explicit ``entrypoints`` setting or may
be missed.
