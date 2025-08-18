PR check workflow
=================

Validate pull requests with an automated check.

#. Add a CI job that runs bumpwright.

    .. code-block:: yaml
       :caption: GitHub Actions

       name: pr-check
       on:
         pull_request:
       jobs:
         decide:
           runs-on: ubuntu-latest
           steps:
             - uses: actions/checkout@v5
               with:
                 fetch-depth: 0
                 fetch-tags: true
             - run: bumpwright decide --format md

#. Run the workflow locally to preview the output.

    .. code-block:: console
       :caption: Console

       $ bumpwright decide --format md

   The command mirrors the CI step and is documented in :doc:`../../cli_reference`.

