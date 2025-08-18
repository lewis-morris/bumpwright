Real-world example: Semantic release with GitHub Actions
=======================================================

This brief walkthrough shows how Bumpwright can automate semantic releases in
an everyday project. The workflow runs tests, bumps the version based on commit
history, updates the changelog, and tags the release.

1. Write commits following the ``Conventional Commits`` specification.
2. Merge to ``main`` to trigger the CI workflow.
3. The workflow installs Bumpwright, runs tests, applies the bump, and pushes
   the updated files and tag.

Example ``.github/workflows/release.yml``:

.. code-block:: yaml

   name: Release
   on:
     push:
       branches: [main]
   permissions:
     contents: write

   jobs:
     release:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v5
           with:
             fetch-depth: 0
             fetch-tags: true
         - uses: actions/setup-python@v5
           with:
             python-version: '3.x'
         - run: pip install bumpwright
         - run: bumpwright bump --commit --tag

This configuration automatically bumps the project version and publishes a tag
whenever changes land on ``main``, illustrating how Bumpwright fits into a
typical continuous delivery pipeline.

