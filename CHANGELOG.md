## [Unreleased]
- remove external `tomli` dependency; rely on Python's `tomllib`.
- add `--purge` flag to `history` to remove bumpwright releases.

## [v2.0.0] - 2025-08-16
- 2ebd374 Merge pull request #227 from lewis-morris/arched/move-badge_utils.py-and-scripts-to-docs-folder-8c24ix
- 1b08131 chore(ci): update badge generation path
- a867d9a Merge pull request #226 from lewis-morris/arched/extend-_parse_spec-and-enhance-diff_specs
- 50457fa feat(openapi): detect parameter and response schema changes
- 3561160 Merge pull request #225 from lewis-morris/arched/add-param-annotation-changes-helper
- cf47d0b feat(compare): detect parameter annotation changes
- a600e18 Merge pull request #224 from lewis-morris/arched/revise-bumpwright-documentation-for-clarity
- f44fff2 docs(docs): reorganize and clarify documentation
- 6be624b workflow changes
- cd8db79 Merge pull request #223 from lewis-morris/arched/fix-graphql-import-error-and-rename-file
- 9be6a26 fix(analysers): rename GraphQL analyser and add dependency
- 1ab2a56 Merge pull request #222 from lewis-morris/arched/move-badge_utils.py-and-scripts-to-docs-folder
- e356d49 refactor(docs): relocate badge utilities into docs tree
- e51fb8b Merge pull request #221 from lewis-morris/arched/update-readme-and-docs-with-analyser-dependencies
- cacee80 Merge branch 'master' into arched/update-readme-and-docs-with-analyser-dependencies
- a131031 Merge pull request #220 from lewis-morris/arched/update-documentation-for-built-in-analysers
- 15756d1 Merge pull request #219 from lewis-morris/arched/replace-template-with-changelog-template
- 13d2306 Merge pull request #218 from lewis-morris/arched/update-configuration-documentation-for-analysers
- 8dfeb9f docs(analysers): document analyser dependencies and CLI requirements
- 120ae0c docs(analysers): enumerate built-in analysers
- 6553231 docs(troubleshooting): clarify changelog template option
- 734a648 docs(configuration): document openapi and graphql analysers
- 70f8be7 Merge pull request #216 from lewis-morris/arched/add-leading-underscore-for-internal-functions
- a6fb73c feat(public-api): allow configuring private symbol prefixes
- b2092b2 Merge pull request #215 from lewis-morris/arched/restructure-guides-section-for-clarity
- 26b4717 docs(guides): reorganize and expand how-to guides
- f5821a0 Merge pull request #214 from lewis-morris/arched/add-grpc-analyser-and-tests
- e765a30 Merge branch 'master' into arched/add-grpc-analyser-and-tests
- 9d5667b Merge pull request #213 from lewis-morris/arched/implement-openapi-document-analyser
- c9fd5f0 Merge branch 'master' into arched/implement-openapi-document-analyser
- 5b3a212 Merge pull request #212 from lewis-morris/arched/add-graphql-analyser-implementation
- 724f91a feat(grpc): add analyser for gRPC services
- 24ab6b1 feat(openapi): add OpenAPI analyser
- 487967d feat(graphql-analyser): add GraphQL schema analyser
- 3b1e6fc Merge pull request #208 from lewis-morris/arched/add-dynamic-badges-to-documentation
- d6945dd Merge pull request #211 from lewis-morris/arched/update-json-snippet-in-bump.rst
- 5a26aca Merge pull request #210 from lewis-morris/arched/update-decide-example-in-cli_reference.rst
- 3ef36d8 Merge pull request #209 from lewis-morris/arched/locate-and-update-bumpwright-example
- aabde7d docs(usage): document dry-run JSON fields
- 93c0396 docs(cli): clarify decide example
- ea0b5bb docs(readme): clarify bump suggestion wording
- df40dea feat(badges): add automated badge generation
- 90cfb1c Merge pull request #202 from lewis-morris/arched/create-test-for-last_release_commit
- 2ed2ce3 Merge branch 'master' into arched/create-test-for-last_release_commit
- eac4c4b Merge pull request #205 from lewis-morris/arched/test-filenotfounderror-in-test_cli_bump_helpers
- 27b62eb Merge pull request #206 from lewis-morris/arched/add-test-case-for-post-and-put-/a
- cf5728f Merge pull request #207 from lewis-morris/arched/replace-any-.-with-exact-impact-comparisons
- 544aed7 Merge pull request #203 from lewis-morris/arched/add-tests-for-read_files_at_ref-functionality
- 9724079 test(cli): assert explicit impact comparisons
- 0e73442 test(web-routes): add coverage for flask multi-method routes
- 39f81a0 test(cli): cover missing pyproject case
- 56b91f1 test(gitutils): cover read_files_at_ref caching and errors
- 26a68c8 Merge pull request #201 from lewis-morris/arched/create-and-test-pyproject.toml-configurations
- a32bad8 test(gitutils): verify last release commit detection
- 02445ec test(versioning): verify write_project_version errors
- 82d1c9d Merge pull request #200 from lewis-morris/arched/simplify-and-reorganize-documentation
- 78f2e53 Merge branch 'master' into arched/simplify-and-reorganize-documentation
- 65c1ccb docs(cli): streamline CLI docs and remove library references
- 63fd410 Merge pull request #198 from lewis-morris/arched/add-helper-for-parameter-default-changes
- 6f2c660 Merge pull request #199 from lewis-morris/arched/add-__post_init__-to-rules-dataclass
- f3085bb feat(config): validate return type change rule
- 7dad3e2 feat(compare): detect parameter default changes
- 8ee2c84 Merge pull request #196 from lewis-morris/arched/modify-imports-in-utils.py
- 49dfc2c fix(analysers): import read_file_at_ref
- 069c4b8 Merge pull request #194 from lewis-morris/arched/revise-quickstart-documentation-format
- 7807870 docs(quickstart): restructure quickstart guide
- 71753b2 Merge pull request #193 from lewis-morris/arched/update-project-documentation
- da4a869 docs(index): expand overview and comparisons
- 99e4301 Merge pull request #192 from lewis-morris/arched/update-documentation-structure-and-content
- 06f125f docs(index): add intro and restructure toctree
- a71456e Merge remote-tracking branch 'origin/master'
- d00934b formatting etc
- d140b09 Merge pull request #191 from lewis-morris/arched/introduce-memoized-parse-helper
- 0a2415f feat(analysers): cache parsed sources for faster analyses
- d8cdef1 Merge remote-tracking branch 'origin/master'
- 839df22 Merge pull request #190 from lewis-morris/arched/refactor-logging-configuration-in-cli-modules
- e5bd5aa Merge pull request #188 from lewis-morris/arched/refactor-character-check-to-use-glob
- 02ce21d Merge pull request #189 from lewis-morris/arched/refactor-iter_py_files_at_ref-for-bulk-reading
- a1d8dcc test(cli): ensure centralized logging is configurable
- 1865998 refactor(utils): batch read Python files
- 32a91fc fix(cli): use glob.has_magic for wildcard paths
- 927d125 formatting etc
- b098790 Merge pull request #187 from lewis-morris/arched/add-summary-table-for-bump-levels
- ba41e7a docs(versioning): clarify bump levels and return type severity
- f2df734 Merge pull request #186 from lewis-morris/arched/expand-usage-documentation-for-flags
- 7d89af5 Merge pull request #185 from lewis-morris/arched/add-examples-for-format-md-and-json
- 22b3e77 docs(usage): expand changelog options
- 3ec150c docs(quickstart): clarify comparison and output formats
- 88d197a Merge remote-tracking branch 'origin/master'
- 47c9269 formatting etc
- 5a44270 Merge pull request #181 from lewis-morris/arched/update-configuration-documentation-for-version.ignore
- 34f2272 Merge pull request #184 from lewis-morris/arched/update-cli-reference-examples
- f79dbc5 Merge pull request #183 from lewis-morris/arched/add-troubleshooting-entries-for-changelog-issues
- 8692d46 Merge pull request #182 from lewis-morris/arched/add-notes-on-github.sha-and-permissions
- d79bf9b Merge pull request #180 from lewis-morris/arched/update-cli-and-web-routes-for-async-support
- 329e32d docs(cli): expand bump command examples
- 00e16e0 docs(troubleshooting): document changelog and template issues
- 29ecf61 docs(ci): document github sha and permissions
- 0e0fc1c docs(config): document analyser lookup and version overrides
- bc61c24 feat(analysers): detect async CLI commands and routes
- fe1b77f Merge pull request #179 from lewis-morris/arched/add-test-cases-for-versioning
- bc0854c Merge pull request #178 from lewis-morris/arched/add-configuration-validation-for-unknown-keys
- 285fdc3 test(versioning): cover mixed ignore patterns and multiple matches
- 9e0f8a5 Merge pull request #177 from lewis-morris/arched/refactor-read_file_at_ref-and-update-tests
- 6a4761a Merge pull request #176 from lewis-morris/arched/refactor-compare_funcs-into-helper-functions
- 9ad8a4f Merge pull request #175 from lewis-morris/arched/add-module-docstrings-to-public_api-and-web_routes
- 924e7b4 feat(config): validate unknown config keys
- b1aefbe test(gitutils): verify caching through batch file reads
- f73a73c test(compare): fix removed parameter coverage
- 9f591c7 docs(api): expand module docstrings for public API and web-route analysers
- ec5f7a1 formatting etc
- 341422e Merge pull request #174 from lewis-morris/arched/refactor-template-handling-in-bump.py
- b0cad3d refactor(changelog): lazily load changelog template
- a85acae Merge pull request #172 from lewis-morris/arched/remove-_default_cfg-assignment-in-versioning.py
- 10fb852 Merge pull request #173 from lewis-morris/arched/fix-assertion-errors-in-versioning-tests
- ee0c35d test(versioning): remove invalid prerelease expectations
- 8fd20bd refactor(versioning): remove unused default config
- b4eee2c Merge pull request #171 from lewis-morris/arched/refactor-_render_expr-and-_render_type
- 6df4079 Merge pull request #170 from lewis-morris/arched/update-config.py-for-dataclass-defaults
- c279a1f refactor(public_api): consolidate AST rendering helper
- 4e8c28f refactor(config): derive defaults from dataclasses
- f0d16c6 Merge pull request #169 from lewis-morris/arched/update-bumpwright-documentation-for-clarity
- 7e243d3 docs(docs): refresh usage and versioning guides
- f2c0780 Merge pull request #168 from lewis-morris/arched/refactor-file-path-collection-and-fetching
- e23f07c Merge branch 'master' into arched/refactor-file-path-collection-and-fetching
- 4a815b9 refactor(migrations): batch read migration files
- 293d893 Merge pull request #167 from lewis-morris/arched/remove-repo-url-from-usage-documentation
- 5995420 docs(usage): drop repo-url option in decide mode
- de7fd78 Merge pull request #166 from lewis-morris/arched/modify-_parse_exports-for-basic-expressions
- 2d6459c feat(public-api): evaluate simple __all__ expressions
- 71b91c3 Merge pull request #165 from lewis-morris/arched/refactor-_run-to-use-subprocess.run
- 001e0fb Merge pull request #164 from lewis-morris/arched/update-readme.md-with-default-ignore-patterns
- e729277 Merge pull request #163 from lewis-morris/arched/update-usage.rst-for-uk-spelling
- a00a0de refactor(gitutils): let subprocess.run raise errors
- 8eec97d docs(readme): document default ignore patterns
- 992ffe5 docs(usage): prefer UK spelling for artefacts
- bf05937 Merge pull request #162 from lewis-morris/arched/update-changelog-options-in-usage.rst
- c93bdb2 docs(usage): document changelog configuration defaults
- dd620af Merge pull request #161 from lewis-morris/arched/update-print-calls-to-logging-in-scripts
- d2519a8 refactor(cli): replace prints with logging
- e11122d Merge pull request #159 from lewis-morris/arched/decorate-read_file_at_ref-with-lru_cache
- 1118a39 Merge pull request #160 from lewis-morris/arched/remove-_default_cfg-global-and-cache-config
- b23e7fd Merge branch 'master' into arched/remove-_default_cfg-global-and-cache-config
- 1babdbe Merge pull request #158 from lewis-morris/arched/refactor-_replace_version-to-use-compiled-regex
- 57357d4 refactor(versioning): cache default config without global state
- 0b5399d feat(gitutils): cache read_file_at_ref
- ad0d6db refactor(versioning): precompile version replacement regex patterns
- 4a4d27c Merge pull request #157 from lewis-morris/arched/modify-apply_bump-to-accept-config-object
- f4c640d Merge branch 'master' into arched/modify-apply_bump-to-accept-config-object
- c9d20d4 docs(configuration): clarify config path usage
- 901966a Merge pull request #155 from lewis-morris/arched/add-optional-cached-config-for-bump_string
- 9cc112e Merge branch 'master' into arched/add-optional-cached-config-for-bump_string
- e80ab59 Merge pull request #156 from lewis-morris/arched/update-version-scheme-bump-behaviors
- 35f3c76 Merge branch 'master' into arched/update-version-scheme-bump-behaviors
- c5ffe8c feat(versioning): reset prerelease metadata on release bump
- 9c5a151 test(versioning): verify config caching
- ced8739 Merge pull request #154 from lewis-morris/arched/adjust-version-regex-for-numeric-components
- a4778ed Merge branch 'master' into arched/adjust-version-regex-for-numeric-components
- 21d15d0 fix(versioning): reject leading-zero semver components
- 25f8754 Merge pull request #153 from lewis-morris/arched/collect-matches-in-set-before-sorting
- 409d0a2 fix(versioning): deduplicate resolved file paths
- 8ef7a0d Merge pull request #152 from lewis-morris/arched/update-quickstart.rst-cli-example
- e0dadee docs(quickstart): reflect CLI suggestion and impacts
- 9245690 Merge remote-tracking branch 'origin/master'
- 8ab35a8 formatting etc
- d4770c5 Merge pull request #148 from lewis-morris/arched/add-migrations-configuration-to-docs
- 00d81d0 Merge pull request #149 from lewis-morris/arched/update-troubleshooting-documentation-for-analyser
- b688135 Merge pull request #150 from lewis-morris/arched/add-note-about-prerelease-increments-in-docs
- d6333c5 docs(versioning): clarify prerelease and build increments
- 544f941 docs(troubleshooting): clarify analyser inspection guidance
- 6bccd46 docs(configuration): document migrations analyser
- 7bcc24c auto release and push top pypi
- 4237ccf Merge pull request #144 from lewis-morris/arched/modify-_commit_tag-to-accept-updated-files
- 1a41ccb Merge branch 'master' into arched/modify-_commit_tag-to-accept-updated-files
- 0b9aa57 Merge pull request #147 from lewis-morris/arched/add-changelog-option-to-cli
- c047aad Merge pull request #146 from lewis-morris/arched/extend-_defaults-with-web_routes-and-migrations
- 8fddc57 Merge pull request #145 from lewis-morris/arched/update-example-configuration-defaults
- c56ad77 docs(cli): support optional changelog argument
- fb23c9b feat(config): add web_routes and migrations analyser defaults
- 882a634 docs(configuration): document full default ignore patterns
- 0868a1a feat(cli): stage all updated files before tagging
- fe35347 formatting and more
- b20beed Merge remote-tracking branch 'origin/master'
- aab4df8 cli docs reword
- 5dfbf4e Merge pull request #143 from lewis-morris/arched/add-github-action-for-version-bump-and-changelog
- d3c9f7e chore(ci): add auto version bump workflow
- 3bbf252 Merge pull request #142 from lewis-morris/arched/update-python-version-requirements
- 0f4bf63 Merge branch 'master' into arched/update-python-version-requirements
- 7613389 chore(python): update supported Python versions
- 50f82a0 Merge pull request #141 from lewis-morris/arched/extend-semverscheme-for-pre-release-management
- b83781d feat(versioning): support prerelease and build bumps
- 2dd0a13 Merge pull request #140 from lewis-morris/arched/update-documentation-for-opt-in-analysers
- 6dd33a0 Merge branch 'master' into arched/update-documentation-for-opt-in-analysers
- f948098 test(analysers): ensure analysers are inactive by default
- ae4f8df Merge pull request #139 from lewis-morris/arched/abort-tag-creation-if-tag-exists
- 68c06c3 Merge pull request #138 from lewis-morris/arched/add-git-status-check-before-commit
- 2729989 Merge pull request #137 from lewis-morris/arched/remove-tests-from-extend-exclude-in-pyproject.toml
- 11f4313 Merge pull request #136 from lewis-morris/arched/add-pre-commit-hooks-for-ruff,-black,-isort
- 8058ca5 fix(bump): abort when tag already exists
- 10b7755 feat(cli): abort on dirty working directory before commit
- 117bbf3 style(tests): enable linting and fix style issues
- 5c4018e docs(pre-commit): document setup and usage
- 098f2eb Merge pull request #135 from lewis-morris/arched/find-why-bump-command-didn-t-update-version
- d5d2581 feat(cli): report skipped files during version bump
- 7ced365 Merge pull request #134 from lewis-morris/arched/update-cli-documentation-for-click-usage
- f2e4d96 docs(cli): improve command documentation
- 338d1e7 Merge remote-tracking branch 'origin/master'
- d52b17d Merge pull request #133 from lewis-morris/arched/update-versionfiles.ignore-patterns
- 8b7ceda Merge branch 'master' into arched/update-versionfiles.ignore-patterns
- b28784e Merge pull request #132 from lewis-morris/arched/modify-versioning-logic-and-add-tests
- cafbf5c Merge branch 'master' into arched/modify-versioning-logic-and-add-tests
- 0414b1d feat(config): add default version ignore patterns
- 999ab98 fix(versioning): skip unchanged files in version replacement
- 9299191 Merge remote-tracking branch 'origin/master'
- 3c883f6 cli docs reword
- bfabce7 Merge pull request #131 from lewis-morris/arched/implement-version-scheme-configuration-and-support
- 9b3e30f feat(versioning): add version scheme abstraction
- 54173fd Merge pull request #130 from lewis-morris/arched/add-configurable-changelog-template-support
- ea81f16 feat(changelog): add configurable Jinja template
- 6be14c0 Merge pull request #128 from lewis-morris/arched/review-and-update-unit-tests-for-coverage
- 24983ad Merge pull request #129 from lewis-morris/arched/refactor-bump_command-into-smaller-helpers
- 222343e test(cli): add unit tests for bump helpers
- 4c94c90 test(core): add missing path coverage
- f0fcd9c Merge pull request #127 from lewis-morris/arched/add-_is_const_str-helper-function
- 94cac7d refactor(analysers): centralize constant string checks
- 81d7cd6 Merge pull request #126 from lewis-morris/arched/add-bumplevel-type-and-refactor-imports
- a06b1af feat(types): centralize bump level type alias
- 866abd6 Merge pull request #125 from lewis-morris/arched/refactor-_param_list-into-smaller-helpers
- 6daa6cd Merge pull request #124 from lewis-morris/arched/decide-on-project.index_file-necessity
- 7f901ee test(public_api): cover helper-based parameter parsing
- d404a37 feat!(config): remove unused project.index_file option
- 0a89fd0 Merge pull request #123 from lewis-morris/arched/review-caching-in-versioning-functions
- cfdf2b1 Merge branch 'master' into arched/review-caching-in-versioning-functions
- cb1f5cb refactor(versioning): reuse cached file resolution
- 3fc03bb Merge pull request #122 from lewis-morris/arched/move-troubleshooting-guide-to-top-level
- e585f1b docs(troubleshooting): add top-level troubleshooting guide with FAQ
- e9f32d9 Merge pull request #121 from lewis-morris/arched/add-imports-in-test_compare.py
- f091d31 test(compare): import compare utilities
- 707fa03 Merge pull request #120 from lewis-morris/arched/update-quickstart-with-minimal-repository-example
- 71667e5 docs(quickstart): expand minimal setup and bump example
- ff15953 Merge pull request #119 from lewis-morris/arched/update-to-uk-english-terminology
- f83684a refactor(spelling): switch to UK English 'analyser'
- c9199b6 Merge pull request #117 from lewis-morris/arched/enhance-documentation-with-faqs-and-cross-links
- 4aaad8a Merge pull request #115 from lewis-morris/arched/create-quickstart-guide-in-docs
- b3d79b1 docs(troubleshooting): expand guidance and add FAQ
- e3a705c Merge pull request #116 from lewis-morris/arched/replace-autoprogram-with-sphinx-click-directives
- fbe2f44 docs(cli): document CLI with sphinx-click
- 06dd807 docs(quickstart): add quickstart guide and references
- c3cce98 Merge pull request #114 from lewis-morris/arched/add-tests-for-_resolve_files-function
- fa4c30f Merge branch 'master' into arched/add-tests-for-_resolve_files-function
- 09703a0 Merge pull request #113 from lewis-morris/arched/add-caching-for-_resolve_files-in-versioning.py
- 8c07f28 Merge pull request #112 from lewis-morris/arched/add-helper-functions-for-argument-parsing
- 43fac61 test(versioning): add resolve files path handling tests
- 2c30274 feat(versioning): cache file resolution results
- a215a22 refactor(cli): centralize analyzer and ref options
- 7236986 Merge pull request #111 from lewis-morris/arched/define-severity-type-and-update-impact
- 7f5b77b feat(compare): add severity type for API impacts
- 376058f Merge pull request #110 from lewis-morris/arched/add-test-cases-for-changelog-options
- 04391a7 test(cli): cover changelog destination cases
- 9b91c6e Merge pull request #109 from lewis-morris/arched/add-shared-utility-for-file-operations
- 655835e refactor(analyzers): centralize python file retrieval
- c86d2ef Merge pull request #108 from lewis-morris/arched/add-caching-to-list_py_files_at_ref
- 2e695bc Merge pull request #107 from lewis-morris/arched/add-fields-to-pyproject.toml
- 5cac328 feat(gitutils): cache list_py_files_at_ref results
- f0bea75 chore(pyproject): add project metadata
- dece51e Merge pull request #106 from lewis-morris/arched/replace-flake8-with-ruff-in-workflows
- 269323c chore(lint): migrate to ruff
- 38b27c5 Merge pull request #105 from lewis-morris/arched/add-parameterized-tests-for-bump_string
- 0a414e8 test(versioning): add invalid input cases
- c35e78a Merge pull request #104 from lewis-morris/arched/refactor-command-functions-into-submodules
- 021a15d refactor(cli): modularize command handlers
- 89eb65e Merge pull request #103 from lewis-morris/arched/refactor-decide_bump-to-return-detailed-object
- f919ebd docs(decide): document enriched decision payload
- ed8b2aa roadmap updates
- 98955ba Merge pull request #102 from lewis-morris/arched/fix-nameerror-in-sphinx-build
- 3fdf92b docs(cli): fix CLI reference parser import
- afa9ef8 test fix
- 0a36204 Merge pull request #100 from lewis-morris/arched/update-github-workflow-documentation-for-version-bumping
- 6c5c6a1 docs(workflow): showcase automatic version bump in GitHub Actions
- d955fc3 Merge pull request #99 from lewis-morris/arched/update-config-to-use-deepcopy-and-add-tests
- 3793e6b fix(config): deep copy defaults to prevent mutation
- 10bfcc1 Merge pull request #98 from lewis-morris/arched/add-license-file-and-references
- 43c1252 chore(license): add MIT license and references
- 90a4c54 Merge pull request #97 from lewis-morris/arched/add-tests-for-subprocess.run-mock
- 509424a Merge pull request #96 from lewis-morris/arched/edit-_run_analyzers-behavior-and-tests
- 0773d1a test(gitutils): add upstream inference tests
- 6d0fc11 fix(cli): warn on unknown analyzers
- 4822641 Merge pull request #95 from lewis-morris/arched/add-module-docstrings-with-linting
- 6cacedb docs(modules): add concise module docstrings
- 3928496 Merge pull request #94 from lewis-morris/arched/simplify-table-layout-for-command-purposes
- 55ecd4a docs(readme): simplify CLI command table
- e8063da Merge pull request #93 from lewis-morris/arched/update-readme.md-and-configuration.rst
- 13baaff docs(configuration): sync defaults with _DEFAULTS
- 333712d docs automation fix
- 6050312 Merge pull request #92 from lewis-morris/arched/merge-changelog-documentation-section
- d65e2e5 docs(usage): document --changelog option for bump
- 75cae45 Merge pull request #91 from lewis-morris/arched/update-sphinx-documentation-configuration
- c61fe21 docs(docs): document CLI via autoprogram and link source code
- 4ac648d Merge pull request #90 from lewis-morris/arched/add-sphinx-argparse-extension-and-cli-docs
- 7cb4cb1 feat(cli): expose parser factory and document CLI
- 8745fe4 Merge remote-tracking branch 'origin/master'
- 3379af6 docs automation fix
- 291a6d7 Merge pull request #89 from lewis-morris/arched/add-command-line-arguments-for-analyzer-k99hsp
- d4c7aa5 Merge branch 'master' into arched/add-command-line-arguments-for-analyzer-k99hsp
- c651656 test(cli): verify analyzer override flags
- 0935e7d Merge pull request #88 from lewis-morris/arched/add-migrationsanalyzer-plugin-and-update-docs
- 23ce948 feat(analyzers): add migrations analyzer plugin
- dfdf81c Merge pull request #87 from lewis-morris/arched/combine-duplicate-bumpwright-examples
- d6c3e6e docs(usage): consolidate decide example
- cf46b24 bumpwright config
- 7f136d6 Merge pull request #85 from lewis-morris/arched/refactor-type-annotations-to-lowercase
- 48f6c7e refactor(typing): replace typing collections with built-ins
- 0ca0150 Merge pull request #83 from lewis-morris/arched/change-initialize-to-initialise
- 5b9f0fb style(cli): adopt British 'initialise' spelling
- f68dc67 Merge pull request #82 from lewis-morris/arched/update-usage-documentation-for-dry-run-example
- d009451 docs(usage): remove duplicate dry-run example
- ceeb7c2 Merge pull request #80 from lewis-morris/arched/add-changelog-dataclass-and-update-config
- 8501541 feat(changelog): support default changelog path
- 4a90234 Merge pull request #79 from lewis-morris/arched/sort-output-list-in-_resolve_files
- acd2f7f fix(versioning): sort resolved files deterministically
- 6495f8a Merge pull request #78 from lewis-morris/arched/update-compare_funcs-for-major-impact
- c3c59d1 fix(compare): flag added required parameters as major
- cdc9f7e Merge pull request #77 from lewis-morris/arched/improve-documentation-clarity-and-examples
- c77ec00 docs(docs): polish examples and enable Sphinx helpers
- 170d73d Merge pull request #76 from lewis-morris/arched/update-top-docstring-in-web_routes.py
- c248472 docs(analyzers): concise web routes docstring
- d0b971c Merge pull request #75 from lewis-morris/arched/refactor-module_name_from_path-in-public_api.py
- 20c6af0 refactor(public-api): simplify module path resolution
- 2602a93 Merge pull request #74 from lewis-morris/arched/update-compare.py-for-optional-parameters
- 978cdc4 feat(compare): record minor impact for optional parameter removal
- 4d850a6 Merge pull request #73 from lewis-morris/arched/update-roadmap-with-additional-items
- 7910c44 docs(roadmap): expand roadmap for world-class features
- e4223fd Merge remote-tracking branch 'origin/master'
- 7caebef bumpwright config
- 9779f08 Merge pull request #72 from lewis-morris/arched/nest-sidebar-options-for-clarity-1m2wjw
- 3be8431 Merge branch 'master' into arched/nest-sidebar-options-for-clarity-1m2wjw
- ac2cf61 docs(docs): nest guides into subsections
- 329c154 Merge pull request #71 from lewis-morris/arched/nest-sidebar-options-for-clarity
- 05d76a9 docs(docs): nest sidebar for analyzers
- b67c9d1 Merge pull request #70 from lewis-morris/arched/add-example-github-workflow-files-to-documentation
- 2ba9b05 docs(workflows): add GitHub Actions examples
- 589f188 Merge pull request #69 from lewis-morris/arched/improve-code-readability-and-robustness
- 95b142d refactor(versioning): tighten type hints and docstring
- 69c3978 Merge remote-tracking branch 'origin/master'
- 47bfad4 bumpwright config
- c0c1c45 Merge pull request #68 from lewis-morris/arched/tidy-up-documentation-and-verify-code
- a5905e7 docs(analyzers): standardize analyzer naming
- 50e5627 Merge pull request #67 from lewis-morris/arched/update-and-correct-docstrings-and-type-hints
- 09821c3 docs(core): improve docstrings and type hints
- c8ff9bc Merge pull request #66 from lewis-morris/arched/fix-pylint-warnings-in-code
- 0149112 Merge branch 'master' into arched/fix-pylint-warnings-in-code
- b2724f7 Merge pull request #65 from lewis-morris/arched/update-version-handling-in-setup.py-and-init
- 7640107 refactor(cli,versioning): resolve pylint warnings
- c7432af feat(versioning): expand default version file updates
## [v0.1.1] - 2025-08-22
- [e85cdc5](https://github.com/lewis-morris/bumpwright/commit/e85cdc5) Merge remote-tracking branch 'origin/master'
- [
d5011a2](https://github.com/lewis-morris/bumpwright/commit/
d5011a2) Merge pull request #16 from lewis-morris/arched/add-introduction-and-organize-configuration-docs
- [
ea65630](https://github.com/lewis-morris/bumpwright/commit/
ea65630) docs(configuration): summarize configuration sections
- [
9c736ec](https://github.com/lewis-morris/bumpwright/commit/
9c736ec) Merge pull request #15 from lewis-morris/arched/standardize-spelling-of-analyser/analyzer
- [
8c8380c](https://github.com/lewis-morris/bumpwright/commit/
8c8380c) docs(docs): standardise analyser spelling
- [
6eced7c](https://github.com/lewis-morris/bumpwright/commit/
6eced7c) Merge pull request #14 from lewis-morris/arched/edit-quickstart-documentation-for-clarity
- [
d95c1ae](https://github.com/lewis-morris/bumpwright/commit/
d95c1ae) Merge pull request #13 from lewis-morris/arched/update-readme.md-for-clarity
- [
13a99b5](https://github.com/lewis-morris/bumpwright/commit/
13a99b5) docs(quickstart): add prerequisites and guidance
- [
3fad466](https://github.com/lewis-morris/bumpwright/commit/
3fad466) docs(readme): clarify introduction
- [
2dc2d05](https://github.com/lewis-morris/bumpwright/commit/
2dc2d05) Merge pull request #12 from lewis-morris/arched/add-grpc-analyser-entry-to-readme
- [
97ede03](https://github.com/lewis-morris/bumpwright/commit/
97ede03) Merge pull request #11 from lewis-morris/arched/decide-documentation-domain-and-update-references
- [
7e45583](https://github.com/lewis-morris/bumpwright/commit/
7e45583) Merge pull request #10 from lewis-morris/arched/update-init.rst-documentation
- [
589e682](https://github.com/lewis-morris/bumpwright/commit/
589e682) docs(readme): add gRPC analyser entry
- [
db82a52](https://github.com/lewis-morris/bumpwright/commit/
db82a52) docs(urls): set canonical documentation domain
- [
8c74066](https://github.com/lewis-morris/bumpwright/commit/
8c74066) docs(init): require explicit summary format
- [
e27f2a6](https://github.com/lewis-morris/bumpwright/commit/
e27f2a6) Merge pull request #9 from lewis-morris/arched/update-documentation-for-primary-options
- [
401ac0b](https://github.com/lewis-morris/bumpwright/commit/
401ac0b) docs(decide): document changelog options
- [
2e99fa9](https://github.com/lewis-morris/bumpwright/commit/
2e99fa9) Merge pull request #8 from lewis-morris/arched/add-sample-output-for-explain-feature
- [
ae081ea](https://github.com/lewis-morris/bumpwright/commit/
ae081ea) docs(decide): showcase explain decision anatomy
- [
1b78a99](https://github.com/lewis-morris/bumpwright/commit/
1b78a99) Merge pull request #7 from lewis-morris/arched/use-clear-heading-hierarchy-in-documentation
- [
da5b546](https://github.com/lewis-morris/bumpwright/commit/
da5b546) docs(quickstart): clarify heading hierarchy
- [
8877280](https://github.com/lewis-morris/bumpwright/commit/
8877280) Merge pull request #6 from lewis-morris/arched/add-usage-example-to-cli-reference
- [
9de35a4](https://github.com/lewis-morris/bumpwright/commit/
9de35a4) docs(bump): start CLI reference with example
- [
7e0db27](https://github.com/lewis-morris/bumpwright/commit/
7e0db27) Merge pull request #5 from lewis-morris/arched/restructure-documentation-into-defined-format
- [
578bf28](https://github.com/lewis-morris/bumpwright/commit/
578bf28) docs(restructure): reorganize documentation
- [
a9a73d6](https://github.com/lewis-morris/bumpwright/commit/
a9a73d6) Merge pull request #4 from lewis-morris/arched/improve-bumpwright-documentation-quality
- [
5b1df61](https://github.com/lewis-morris/bumpwright/commit/
5b1df61) docs(intro): refine project introduction and overview
- [
37225dc](https://github.com/lewis-morris/bumpwright/commit/
37225dc) Merge pull request #3 from lewis-morris/arched/rename-format_-to-output_fmt
- [
8473f72](https://github.com/lewis-morris/bumpwright/commit/
8473f72) fix(cli): rename format arg to output_fmt
- [
2e1b817](https://github.com/lewis-morris/bumpwright/commit/
2e1b817) Merge pull request #2 from lewis-morris/arched/unify-navigation-labels-and-sidebar-structure
- [
e1933ba](https://github.com/lewis-morris/bumpwright/commit/
e1933ba) docs(nav): unify navigation labels and toctree
- [
b265c2a](https://github.com/lewis-morris/bumpwright/commit/
b265c2a) Merge pull request #1 from lewis-morris/arched/investigate-failing-unit-tests-in-ci
- [
af90700](https://github.com/lewis-morris/bumpwright/commit/
af90700) fix(changelog): handle contributor errors gracefully


### Contributors
- [Lewis Morris](https://github.com/lewis-morris)
- Lewis Morris
## [v0.1.2] - 2025-08-23
- [0e52669](https://github.com/lewis-morris/bumpwright/commit/0e52669) gitignore changes
- [
102e6dd](https://github.com/lewis-morris/bumpwright/commit/
102e6dd) Merge pull request #17 from lewis-morris/arched/add-configuration-summary-documentation-page
- [
e576412](https://github.com/lewis-morris/bumpwright/commit/
e576412) docs(configuration): document CLI and environment variable mappings
- [
bfa2683](https://github.com/lewis-morris/bumpwright/commit/
bfa2683) workflows
- [
e85cdc5](https://github.com/lewis-morris/bumpwright/commit/
e85cdc5) Merge remote-tracking branch 'origin/master'
- [
d5011a2](https://github.com/lewis-morris/bumpwright/commit/
d5011a2) Merge pull request #16 from lewis-morris/arched/add-introduction-and-organize-configuration-docs
- [
ea65630](https://github.com/lewis-morris/bumpwright/commit/
ea65630) docs(configuration): summarize configuration sections
- [
9c736ec](https://github.com/lewis-morris/bumpwright/commit/
9c736ec) Merge pull request #15 from lewis-morris/arched/standardize-spelling-of-analyser/analyzer
- [
8c8380c](https://github.com/lewis-morris/bumpwright/commit/
8c8380c) docs(docs): standardise analyser spelling
- [
6eced7c](https://github.com/lewis-morris/bumpwright/commit/
6eced7c) Merge pull request #14 from lewis-morris/arched/edit-quickstart-documentation-for-clarity
- [
d95c1ae](https://github.com/lewis-morris/bumpwright/commit/
d95c1ae) Merge pull request #13 from lewis-morris/arched/update-readme.md-for-clarity
- [
13a99b5](https://github.com/lewis-morris/bumpwright/commit/
13a99b5) docs(quickstart): add prerequisites and guidance
- [
3fad466](https://github.com/lewis-morris/bumpwright/commit/
3fad466) docs(readme): clarify introduction
- [
2dc2d05](https://github.com/lewis-morris/bumpwright/commit/
2dc2d05) Merge pull request #12 from lewis-morris/arched/add-grpc-analyser-entry-to-readme
- [
97ede03](https://github.com/lewis-morris/bumpwright/commit/
97ede03) Merge pull request #11 from lewis-morris/arched/decide-documentation-domain-and-update-references
- [
7e45583](https://github.com/lewis-morris/bumpwright/commit/
7e45583) Merge pull request #10 from lewis-morris/arched/update-init.rst-documentation
- [
589e682](https://github.com/lewis-morris/bumpwright/commit/
589e682) docs(readme): add gRPC analyser entry
- [
db82a52](https://github.com/lewis-morris/bumpwright/commit/
db82a52) docs(urls): set canonical documentation domain
- [
8c74066](https://github.com/lewis-morris/bumpwright/commit/
8c74066) docs(init): require explicit summary format
- [
e27f2a6](https://github.com/lewis-morris/bumpwright/commit/
e27f2a6) Merge pull request #9 from lewis-morris/arched/update-documentation-for-primary-options
- [
401ac0b](https://github.com/lewis-morris/bumpwright/commit/
401ac0b) docs(decide): document changelog options
- [
2e99fa9](https://github.com/lewis-morris/bumpwright/commit/
2e99fa9) Merge pull request #8 from lewis-morris/arched/add-sample-output-for-explain-feature
- [
ae081ea](https://github.com/lewis-morris/bumpwright/commit/
ae081ea) docs(decide): showcase explain decision anatomy
- [
1b78a99](https://github.com/lewis-morris/bumpwright/commit/
1b78a99) Merge pull request #7 from lewis-morris/arched/use-clear-heading-hierarchy-in-documentation
- [
da5b546](https://github.com/lewis-morris/bumpwright/commit/
da5b546) docs(quickstart): clarify heading hierarchy
- [
8877280](https://github.com/lewis-morris/bumpwright/commit/
8877280) Merge pull request #6 from lewis-morris/arched/add-usage-example-to-cli-reference
- [
9de35a4](https://github.com/lewis-morris/bumpwright/commit/
9de35a4) docs(bump): start CLI reference with example
- [
7e0db27](https://github.com/lewis-morris/bumpwright/commit/
7e0db27) Merge pull request #5 from lewis-morris/arched/restructure-documentation-into-defined-format
- [
578bf28](https://github.com/lewis-morris/bumpwright/commit/
578bf28) docs(restructure): reorganize documentation
- [
a9a73d6](https://github.com/lewis-morris/bumpwright/commit/
a9a73d6) Merge pull request #4 from lewis-morris/arched/improve-bumpwright-documentation-quality
- [
5b1df61](https://github.com/lewis-morris/bumpwright/commit/
5b1df61) docs(intro): refine project introduction and overview
- [
37225dc](https://github.com/lewis-morris/bumpwright/commit/
37225dc) Merge pull request #3 from lewis-morris/arched/rename-format_-to-output_fmt
- [
8473f72](https://github.com/lewis-morris/bumpwright/commit/
8473f72) fix(cli): rename format arg to output_fmt
- [
2e1b817](https://github.com/lewis-morris/bumpwright/commit/
2e1b817) Merge pull request #2 from lewis-morris/arched/unify-navigation-labels-and-sidebar-structure
- [
e1933ba](https://github.com/lewis-morris/bumpwright/commit/
e1933ba) docs(nav): unify navigation labels and toctree
- [
b265c2a](https://github.com/lewis-morris/bumpwright/commit/
b265c2a) Merge pull request #1 from lewis-morris/arched/investigate-failing-unit-tests-in-ci
- [
af90700](https://github.com/lewis-morris/bumpwright/commit/
af90700) fix(changelog): handle contributor errors gracefully


### Contributors
- [Lewis Morris](https://github.com/lewis-morris)
- Lewis Morris
