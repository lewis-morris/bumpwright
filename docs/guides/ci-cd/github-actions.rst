CI/CD (GitHub Actions)
========================

Bumpwright integrates easily with GitHub Actions. The following workflows
demonstrate common setups:

* Automatically apply a version bump on pushes to your main branch.
* Suggest the next semantic version in pull requests.
* Publish a release and package on tag push.

Place the selected file in ``.github/workflows`` to use it.

Workflows that create commits or tags require ``permissions: contents: write``
and authenticate using the default ``GITHUB_TOKEN``. When referencing the
current commit, ``${{ github.sha }}`` expands to the workflow's commit SHA.

Automatic version bump on push
------------------------------

The ``bumpwright-auto-bump.yml`` workflow updates your project version and
changelog whenever new commits land on ``main`` or ``master``. It runs
``bumpwright bump --changelog CHANGELOG.md --commit --tag --format md`` to
commit the change and create a matching tag.

.. literalinclude:: ../../_static/workflows/bumpwright-auto-bump.yml
   :language: yaml
   :caption: bumpwright-auto-bump.yml

Download the file: :download:`bumpwright-auto-bump.yml <../../_static/workflows/bumpwright-auto-bump.yml>`.

Pull request check
------------------

The ``bumpwright-check.yml`` workflow runs Bumpwright in read-only mode to
suggest the next version. Trigger it manually with the ``workflow_dispatch``
event, or adapt it to run on pull requests.

.. literalinclude:: ../../_static/workflows/bumpwright-check.yml
   :language: yaml
   :caption: bumpwright-check.yml

Download the file: :download:`bumpwright-check.yml <../../_static/workflows/bumpwright-check.yml>`.

Release & publish on tag
------------------------

The ``bumpwright-release.yml`` workflow builds wheels and an sdist, uploads
them to PyPI using Trusted Publishing, and creates a GitHub Release whenever a
tag prefixed with ``v`` is pushed.

.. literalinclude:: ../../_static/workflows/bumpwright-release.yml
   :language: yaml
   :caption: bumpwright-release.yml

Download the file: :download:`bumpwright-release.yml <../../_static/workflows/bumpwright-release.yml>`.

Keyword-triggered bump
----------------------

The ``bumpwright-keyword-bump.yml`` workflow applies a version bump only when
any commit message in the push contains the ``[bump]`` marker. This lets you
control releases through commit messages while ignoring other changes.

.. literalinclude:: ../../_static/workflows/bumpwright-keyword-bump.yml
   :language: yaml
   :caption: bumpwright-keyword-bump.yml

Download the file: :download:`bumpwright-keyword-bump.yml <../../_static/workflows/bumpwright-keyword-bump.yml>`.
