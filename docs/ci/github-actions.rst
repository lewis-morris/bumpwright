:orphan:

GitHub Actions
==============

These examples show how to integrate Bumpwright with GitHub Actions
without duplicating coverage jobs. They can be adapted for other
providers such as GitLab or Jenkins.

Tags are prefixed with ``v`` to match the release workflow's tag
trigger.

The auto-bump workflow runs ``bumpwright bump --changelog CHANGELOG.md --commit --tag --format md``
to update the changelog, commit the change, and create a tag.

.. tab-set::

   .. tab-item:: Auto bump

      .. code-block:: yaml
         :caption: Workflow

         name: Bumpwright Auto Bump
         on:
           push:
             branches: [main, master]
         concurrency:
           group: bumpwright-bump-${{ github.ref }}
           cancel-in-progress: true
         permissions:
           contents: write
         jobs:
           bump:
             if: ${{ github.actor != 'github-actions[bot]' }}
             runs-on: ubuntu-latest
             steps:
               - name: Checkout (full history + tags)
                 uses: actions/checkout@v5
                 with:
                   fetch-depth: 0
                   fetch-tags: true
               - name: Set up Python
                 uses: actions/setup-python@v5
                 with:
                   python-version: '3.x'
                   cache: 'pip'
               - name: Install project
                 run: |
                   python -m pip install --upgrade pip
                   pip install -e .
               - name: Configure git author
                 run: |
                   git config user.name "github-actions[bot]"
                   git config user.email "github-actions[bot]@users.noreply.github.com"
               - name: Bump version, update changelog, commit & tag
                 run: |
                   bumpwright bump --changelog CHANGELOG.md --commit --tag --format md
               - name: Push commit and tags
                 run: |
                   git push origin HEAD:${{ github.ref_name }}
                   git push --tags

   .. tab-item:: Release & publish on tag

      .. code-block:: yaml
         :caption: Workflow

         name: Release & Publish
         on:
           push:
             tags: ['v*']
         permissions:
           contents: write
           id-token: write
         jobs:
           release:
             runs-on: ubuntu-latest
             steps:
               - name: Checkout (full history + tags)
                 uses: actions/checkout@v5
                 with:
                   fetch-depth: 0
                   fetch-tags: true
               - name: Set up Python
                 uses: actions/setup-python@v5
                 with:
                   python-version: '3.x'
                   cache: 'pip'
               - name: Build package
                 run: |
                   python -m pip install --upgrade pip
                   pip install build
                   python -m build
               - name: Publish to PyPI
                 uses: pypa/gh-action-pypi-publish@release/v1
               - name: Create GitHub release
                 uses: softprops/action-gh-release@v2
                 with:
                   files: dist/*

Decision only
-------------

Generates a JSON report with the suggested version bump. Useful when
another job or manual gate decides whether to release.

.. code-block:: yaml
   :caption: Workflow

   name: Bumpwright Decision
   on: [push]
   jobs:
     decide:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout (full history + tags)
           uses: actions/checkout@v5
           with:
             fetch-depth: 0
             fetch-tags: true
         - name: Set up Python
           uses: actions/setup-python@v5
           with:
             python-version: '3.x'
         - name: Install bumpwright
           run: pip install bumpwright
         - name: Decide bump
           run: bumpwright decide --format json > decision.json
         - uses: actions/upload-artifact@v4
           with:
             name: bumpwright-decision
             path: decision.json

To apply the decision in a separate job, download the artifact and
parse the level with ``jq``:

.. code-block:: yaml
   :caption: Workflow

   - uses: actions/download-artifact@v4
     with:
       name: bumpwright-decision
   - run: |
       level=$(jq -r '.level' decision.json)
       if [ "$level" != "none" ]; then
          bumpwright bump --commit --tag --repo-url "$GITHUB_SERVER_URL/$GITHUB_REPOSITORY"
         git push origin HEAD:${{ github.ref_name }}
         git push --tags
       fi

Pull request with comment
-------------------------

Creates a pull request with the version bump and posts a comment. Use
this when you prefer a human review before releasing.

.. code-block:: yaml
   :caption: Workflow

   name: Bumpwright Pull Request
   on:
     workflow_dispatch:
   jobs:
     bump:
       runs-on: ubuntu-latest
       permissions:
         contents: write
         pull-requests: write
       steps:
         - name: Checkout (full history + tags)
           uses: actions/checkout@v5
           with:
             fetch-depth: 0
             fetch-tags: true
         - name: Set up Python
           uses: actions/setup-python@v5
           with:
             python-version: '3.x'
             cache: 'pip'
         - name: Install bumpwright
           run: pip install bumpwright
         - name: Bump version and changelog
           run: bumpwright bump --changelog CHANGELOG.md --commit --repo-url "$GITHUB_SERVER_URL/$GITHUB_REPOSITORY"
         - name: Create pull request
           id: cpr
           uses: peter-evans/create-pull-request@v6
           with:
             commit-message: "chore: bump version"
             branch: bumpwright/bump
             title: "chore: bump version"
             body: "Automated version bump."
         - name: Comment on pull request
           if: steps.cpr.outputs.pull-request-number
           uses: actions/github-script@v7
           with:
             script: |
               github.rest.issues.createComment({
                 issue_number: parseInt('${{ steps.cpr.outputs.pull-request-number }}', 10),
                 owner: context.repo.owner,
                 repo: context.repo.repo,
                 body: 'Bumpwright prepared a new release.'
               })

Keyword-triggered bump
----------------------

Only bumps the version when any commit message contains ``[bump]``.

.. code-block:: yaml
   :caption: Workflow

   name: Bumpwright Keyword Bump
   on:
     push:
       branches: [main]
   permissions:
     contents: write
   jobs:
     bump:
       if: |
         github.actor != 'github-actions[bot]' &&
         contains(join(github.event.commits.*.message, ' '), '[bump]')
       runs-on: ubuntu-latest
       steps:
         - name: Checkout (full history + tags)
           uses: actions/checkout@v5
           with:
             fetch-depth: 0
             fetch-tags: true
         - name: Set up Python
           uses: actions/setup-python@v5
           with:
             python-version: '3.x'
             cache: 'pip'
         - name: Install bumpwright
           run: |
             python -m pip install --upgrade pip
             pip install bumpwright
         - name: Configure git author
           run: |
             git config user.name "github-actions[bot]"
             git config user.email "github-actions[bot]@users.noreply.github.com"
         - name: Bump version and update changelog
           run: |
               bumpwright bump --changelog CHANGELOG.md --commit --tag --repo-url "$GITHUB_SERVER_URL/$GITHUB_REPOSITORY"
         - name: Push commit and tags
           run: |
             git push origin HEAD:${{ github.ref_name }}
             git push --tags

