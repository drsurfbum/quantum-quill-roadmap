# Quantum Quill feature roadmap

[Open the roadmap](https://drsurfbum.github.io/quantum-quill-roadmap/)

The public feature roadmap for Quantum Quill, a writing workspace for planning stories, building worlds and writing prose. Inspired by the BIMCraft feature tracker. This repository contains only the roadmap; the application and story data remain private.

## Maintain the roadmap

Edit `roadmap.json`, then run `python3 build.py`. Review and commit the source, generated `ROADMAP.md` and `docs/index.html` together, then push. GitHub Pages publishes the `/docs` folder from `main`. `dist/index.html` is a matching local preview and is ignored by Git.

- `roadmap.json`: reviewed planning data, stable feature IDs and accepted-scope evidence.
- `template.html`: search, status/area filters, direct feature links, expandable prerequisites and print styling.
- `build.py`: standard-library generator and validation, including a restrictive CSP with hashed inline scripts/styles.
- `ROADMAP.md`: readable companion generated from the same data.

No external fonts, analytics, API requests, packages or runtime services are required. Filters are read-only. Print / Save PDF includes every feature and its details.

Statuses describe verified local capabilities, partial work, recommended priorities, decisions and later ideas. They do not imply a production release or a main-branch application merge. Update this roadmap after accepted features; do not infer completion from card counts or invent delivery dates.

## Development policy

Completed QQ features are checked, committed and pushed to their feature branches. Merging is separate. Keep private manuscripts, account information, imports, backups and credentials out of this public roadmap.

## Saved for later

Reconstruct Quantum Quill's development history from surviving versions, archives and records after the current alpha preparation. No history research is required for this publication.
