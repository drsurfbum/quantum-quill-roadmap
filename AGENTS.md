# Quantum Quill roadmap working policy

- Every repository change needs at least a draft pull request. Review the diff, run appropriate checks, push its feature branch, and create or update the PR. Do not push routine changes directly to main. A specific later local-only instruction takes precedence.
- PR creation does not authorize merging or publishing. GitHub Pages publishes the approved main/docs content; keep unapproved changes on their review branch.
- Use a separate chat for each new product feature and reuse its chat for updates. Preserve existing ownership, branches, worktrees, uncommitted changes and previews. Do not reset, rebase, force-push or rewrite history as routine maintenance.
- The PM chat coordinates the roadmap and recurring checks. Reports should distinguish local-only work, published branches, draft PRs, merged changes and live releases, with evidence and limitations in plain language.
- Edit roadmap.json, then run python3 build.py and review the generated ROADMAP.md and docs/index.html. Preserve existing feature IDs and historical notes. Do not claim fresh end-to-end validation based only on an availability check or old test results.
- App source is public at https://github.com/drsurfbum/quantum-quill-app. Keep manuscripts, accounts, imports, backups, uploads and secrets out of this public roadmap. Canonical alpha: https://quantquill.io.
