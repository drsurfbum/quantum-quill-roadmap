# Quantum Quill feature roadmap

Status checked October 24, 2026. Feature checkpoint: October 24, 2026 (`7a3f09d5193eb57a3a8e5c5d4f5786568af1ad30`).

A dependable place to plan a story, build its world, and keep writing. Novel writing comes first; the foundations should also serve other kinds of storytelling.

Canonical private repository: https://github.com/drsurfbum/quantum-quill-app

This is a manually maintained snapshot, not live sync. Working locally is not a deployment or main-branch merge claim. No delivery dates or percentage-complete estimate are assigned.

October 24: 391 tests across 38 suites, TypeScript, production build, and an 18-table paired restore rehearsal passed locally, including admin access and status persistence. The public alpha and private maintainer inbox are live, with owner access explicitly enabled. Source remains on feature branches, not merged to main.

## Milestones

- **M0 — Protect the writing · Foundation working**: Reliable saves, recoverable drafts, ownership and compatible data reads.
- **M1 — Finish the novel workflow · Workflow working**: Plan, organize, write and export without losing momentum.
- **M2 — Make the world easier to build · Next focus**: Guided entries, useful connections, character development and research.
- **M3 — Open alpha & feedback · Alpha live; hardening continues**: Real-world testing with private reports, dependable hosting and restore rehearsals.
- **M4 — More ways to tell stories · Later**: Broader formats and optional advanced tools, after the novel foundation.

## Keep in view

- **The open alpha is live**: Create a new account to try Quantum Quill. Use Feedback inside the app for private reports; no GitHub account is needed. Local accounts and recovered manuscripts were not copied to the alpha.
- **Keep legacy conversion deliberate**: Four older entries still need a destination decision; two classification conflicts and orphan planning records remain preserved. Compatibility reads work. No destructive migration is approved.
- **A local alpha, with clear boundaries**: The save protections and core workflow are working locally. Full offline app loading, collaboration, a general Notion sync and public deployment are not complete.

## Features

### QQ-01 — Writing you can recover

**Working locally · Writing & safety**

Keep drafts through failed saves and reloads, with explicit choices when another tab or device has newer writing.

- Account/project-scoped durable draft journals and serialized autosave.
- Server revisions, restore/discard review and protected navigation/export.

**Boundary:** Draft recovery is implemented. It is not full offline app loading or a complete version-history browser.

**Acceptance:** Offline edits remain recoverable; reconnect cannot silently replace newer server writing; switching accounts cannot reveal another account's drafts.

**Prerequisites:** None.

**Evidence / basis:** docs/DRAFT_RECOVERY_AND_DATA_INTEGRITY.md; save, recovery and conflict suites

### QQ-02 — One dependable data contract

**First slice working · Writing & safety**

Use shared validation and classification while retaining every original field and legacy payload.

- Shared catalog, type-specific validation and compatibility readers are in place.
- Versioned v2 documents and a disposable migration/rollback rehearsal are prepared.

**Boundary:** 47 recovered records and 828 audited field paths were retained in rehearsal. Activation and ambiguous conversions have not been applied.

**Acceptance:** Each recovered field has a documented destination or retained payload; reviewed migration and rollback preserve counts and values.

**Prerequisites:** QQ-01, QQ-19

**Evidence / basis:** docs/DATA_CONTRACT.md; docs/DATA_CONTRACT_REHEARSAL.md

### QQ-03 — Relationships that stay connected

**Working locally · Story Bible**

Connect all seven entry types by identity, with roles, context, dates and useful backlinks.

- Shared searchable relationship picker, safe stubs and current target names.
- Event participation/consequences, group membership, location governance/history and world-element usage/references.

**Boundary:** Same-project validation, hierarchy cycle checks and archive/delete guards work. A visual graph is a separate later feature.

**Acceptance:** Create, edit, remove and rename-target round trips retain meaning; invalid targets/cycles are rejected; linked deletion has predictable behavior.

**Prerequisites:** QQ-01

**Evidence / basis:** docs/SHARED_RELATIONSHIPS.md; relationship API and field suites

### QQ-04 — Start with a little guidance

**Working locally · Planning**

Use the New Project and Blueprint wizards, or skip planning and go straight to writing.

- Recoverable New Project Wizard and restored Blueprint Wizard.
- Create project structure and scenes without replacing existing prose.

**Boundary:** The restored flows work; future guidance improvements should reuse their protected drafts.

**Acceptance:** Wizard progress is recoverable and repeatable; direct-to-writing remains a first-class path.

**Prerequisites:** QQ-01

**Evidence / basis:** docs/WIZARDS_AND_SCENES.md; later stabilization closeout supersedes its old limitations

### QQ-05 — From plot point to prose

**Working locally · Planning**

Move from Storyboard plot points to Outline scenes, scene story beats and manuscript writing.

- Scene planning and story beats connect the Storyboard, Outline and Write workflows.
- Existing outline notes and chapter-only writing remain available.

**Boundary:** Planning is optional. The complete journey still needs more sustained real-project usability testing.

**Acceptance:** A writer can start at any stage, follow a planned scene into Write and retain plans separately from prose.

**Prerequisites:** QQ-04

**Evidence / basis:** docs/SCENE_OUTLINE_WORKFLOW.md; planning and scene-beat tests

### QQ-06 — Shape the manuscript safely

**Working locally · Planning**

Reorder chapters and scenes, move scenes between chapters, and keep their writing intact.

- Persisted chapter/scene ordering with atomic moves and stale-arrangement checks.
- Safe chapter rename/completion and guarded chapter deletion.

**Boundary:** Scene deletion and automatic conversion between chapter writing modes are not exposed.

**Acceptance:** Moving/reordering preserves prose, scene plans and references; conflicting arrangements are rejected without partial updates.

**Prerequisites:** QQ-01, QQ-05

**Evidence / basis:** docs/STABILIZATION_CLOSEOUT.md; manuscript API and PostgreSQL rehearsal

### QQ-07 — A writer's formatting toolkit

**Working locally · Writing & safety**

Use fonts, rich formatting and reusable Quill styles without giving up protected saves.

- Font/size, headings, emphasis, color, paragraph controls, lists, tables, images and find/replace.
- Premade typographic styles and account-level custom saved styles.

**Boundary:** This is not a paginated publishing engine. Footnotes, headers/footers and tracked changes remain outside the current editor.

**Acceptance:** Formatting and custom styles survive save/reload, export within documented limits and draft recovery.

**Prerequisites:** QQ-01

**Evidence / basis:** docs/WRITE_FORMATTING.md; formatting, style and export tests

### QQ-08 — Give the prose room

**Working locally · Workspace**

Keep prose central, with a compact manuscript navigator and separate scene/context panes.

- Shared workspace navigation and a responsive, single-row formatting bar.
- Reserved save-status space and context panels that preserve editor state.
- A discreet roadmap link in workspace navigation and the dashboard sidebar opens a separate tab without leaving the writing session.

**Boundary:** Broader browser, mobile and input-method testing is still needed before a release claim.

**Acceptance:** Opening cards or plans does not push prose down, reset the editor or remove formatting tools.

**Prerequisites:** QQ-07

**Evidence / basis:** docs/WORKSPACE_INTEGRATION.md; workspace writing tests and fixture walkthrough; October 23 roadmap shortcut (0067b97): type check, production build and browser walkthrough

### QQ-09 — A readable Story Bible library

**Working locally · Story Bible**

Find an entry and work in a focused detail pane instead of navigating oversized category dashboards.

- Seven types, search, filters, stars, archive and sorting.
- Overview, Develop, Connections and preserved imported Source views.

**Boundary:** Type-specific editors remain complete, but more field guidance and a guided creation journey are still needed.

**Acceptance:** Filters persist, narrow screens have clear navigation, every field remains available and tab changes preserve unsaved edits.

**Prerequisites:** QQ-01, QQ-03

**Evidence / basis:** docs/STORY_BIBLE_WORKSPACE.md; library and mounted-editor tests

### QQ-10 — Keep the world beside the writing

**Working locally · Workspace**

Link elements inline and use interactive cards without leaving the Write workspace.

- Type @ or link selected words; pin viewpoint, cast, locations and references to a scene.
- Open facts, relationships and scene notes; edit the full entry in place.

**Boundary:** Renaming an entry updates its card, not the author's words. Inline mentions and scene pins remain separate connections.

**Acceptance:** Card edits and prose save independently; links survive undo, formatting and recovery; foreign targets are rejected.

**Prerequisites:** QQ-03, QQ-08

**Evidence / basis:** docs/WORKSPACE_INTEGRATION.md; docs/SCENE_STORY_BIBLE.md

### QQ-11 — Find missing scene connections

**Working locally · Story Bible**

Scan the current scene for mentions of existing entries, then review what should be connected.

- Read live prose, including unsaved text; show excerpts and flag ambiguous names.
- Default to a mentioned reference; the writer may choose cast or setting before adding.

**Boundary:** Current scene only. Literal name/alias matching, not semantic inference. No new entries, automatic linking or prose edits.

**Acceptance:** Linked/archived/foreign entries are excluded, stale scans require review, and approved connections use the existing protected save queue.

**Prerequisites:** QQ-10

**Evidence / basis:** docs/SCENE_STORY_BIBLE.md, October 14 addition; 380 tests / 36 suites recorded

### QQ-12 — Bring the original story across

**Working locally · Planning**

Use a preserved Notion import as a realistic test of the entire writing organizer.

- 39 Bible entries, 29 chapters, 60 scene records, 29 plot points and 93 scene beats imported into a separate project.
- 233 scene connections across 60 records; source material and images retained.

**Boundary:** This is a reviewed one-story import, not ongoing Notion sync. Thirteen Bible entries are archived examples/templates. One long chapter draft intentionally remains intact.

**Acceptance:** Existing projects and source records remain unchanged; imports and context links retain prose/formatting byte for byte.

**Prerequisites:** QQ-05, QQ-10

**Evidence / basis:** docs/NOTION_WORLD_BIBLE_IMPORT.md covers the first phase; private manuscript/context import receipts cover later phases

### QQ-13 — Take your manuscript with you

**First slice working · Publishing & release**

Export real Word, HTML, plain text, EPUB and original-record JSON files.

- Manuscript-order exports, optional planning/Bible content and authorized local images.
- Preview with browser Print / Save PDF; pending writes and unresolved drafts are guarded.

**Boundary:** The exports work. External EPUB validation, broader reader checks and complex publishing-layout fidelity remain open; PDF is a browser print flow.

**Acceptance:** Export includes the latest saved writing in order, preserves supported formatting and has reviewed limits for each target format.

**Prerequisites:** QQ-01, QQ-06, QQ-07

**Evidence / basis:** docs/STABILIZATION_CLOSEOUT.md; binary export and snapshot tests

### QQ-14 — A more guided Story Bible

**Recommended next · Story Bible**

Make it obvious what each element is for, which fields matter first, and how to develop it.

- Explain purpose and show examples for all seven types, inspired by the WBB workflow.
- Separate essential facts from optional depth; suggest relevant next connections.

**Boundary:** Existing forms and basic guidance work. The complete guided entry-creation experience is not yet implemented.

**Acceptance:** A new writer can create and develop an element without guessing field meaning; every existing field, link and recovered original still round-trips.

**Prerequisites:** QQ-09

**Evidence / basis:** User-approved direction; docs/ANTIGRAVITY_STORY_BIBLE_INTEGRATION.md

### QQ-15 — Develop characters with intention

**Planned · Story Bible**

Connect character goals, needs, beliefs, conflicts and change to their role in the story.

- A guided character workbench using existing facts and retained imported prompts.
- Useful references and arc prompts connected to scenes and events.

**Boundary:** Current character fields already store much of this material. The proposed workbench must not create a second competing data model.

**Acceptance:** Existing character data appears in the guided experience without duplication; prompts are optional and edits remain recoverable.

**Prerequisites:** QQ-14, QQ-10

**Evidence / basis:** Antigravity comparison and WBB-inspired product direction; implementation not started

### QQ-16 — See the story's chronology

**Planned · Story Bible**

Arrange events over time while respecting fictional calendars, approximate dates and uncertainty.

- Define date/order rules before adding a timeline view.
- Use existing event relationships and distinguish story chronology from manuscript order.

**Boundary:** Event dates and timeline flags currently store intent; no complete timeline screen or fictional-calendar ordering exists.

**Acceptance:** Uncertain dates remain uncertain, calendars have explicit ordering rules, and links open the underlying event/scene without copied names.

**Prerequisites:** QQ-03, QQ-14

**Evidence / basis:** docs/STORY_BIBLE_ROADMAP.md, remaining section workflows

### QQ-17 — A writer's knowledge organizer

**First slice working · Story Bible**

Collect research and connect useful knowledge to the world and the writing it informs.

- Current Research entries support sources, summaries, topics, notes, next steps and links.
- Extend toward richer notes, quotations, attachments and deliberate application to story elements.

**Boundary:** Basic Research entries work. A complete knowledge library, attachment workflows, reminders and cross-project reuse are not built.

**Acceptance:** Sources stay traceable, quotes and author notes remain distinct, attachments recover cleanly after failures, and applying research never silently overwrites fiction.

**Prerequisites:** QQ-03, QQ-14

**Evidence / basis:** Current Research editor; docs/STORY_BIBLE_ROADMAP.md and user product vision

### QQ-18 — Review connections across a project

**Planned · Story Bible**

Extend the scene scanner into a manageable review across a longer manuscript.

- Project-wide review with progress, scene context and explicit alias management.
- Keep ambiguous names and possible new entries as separate decisions.

**Boundary:** The approved first version matches existing entries one scene at a time. New-entry suggestions would be a further scope decision.

**Acceptance:** Review resumes safely, ignores stale results, avoids duplicates and applies only chosen links without editing prose.

**Prerequisites:** QQ-11

**Evidence / basis:** Follow-up to the existing-entry scanner; not implemented

### QQ-19 — Review the remaining legacy mappings

**Needs a decision · Writing & safety**

Resolve ambiguous recovered records before activating structured conversions.

- Review four lore/timeline records and two classification conflicts.
- Keep orphan planning records and all original payloads until their meaning is established.

**Boundary:** Preview and disposable rehearsal exist. No destructive production conversion is approved; this does not block normal writing through compatibility readers.

**Acceptance:** Each mapping has a reviewed preview, retained original, equal before/after counts and values, and a rehearsed rollback.

**Prerequisites:** None.

**Evidence / basis:** docs/DATA_CONTRACT_REHEARSAL.md; 47 records / 828 audited field paths

### QQ-20 — Reusable, reviewable imports

**Planned · Planning**

Turn the successful one-story import into a clear workflow other projects can use.

- Preview mappings, examples/templates, duplicates, images and manuscript boundaries.
- Support safe retries and retain source provenance and original payloads.

**Boundary:** Import scripts and preserved receipts exist. There is no general import UI or live Notion synchronization.

**Acceptance:** A preview explains every destination; retries cannot duplicate records; failures roll back cleanly and prose stays unchanged unless explicitly transformed.

**Prerequisites:** QQ-12, QQ-14

**Evidence / basis:** Existing world-bible import/rehearsal provides the foundation; reusable UI not started

### QQ-21 — A sustained real-story walkthrough

**Recommended next · Workspace**

Use the imported novel to find friction across planning, writing, world-building and export.

- Follow a real chapter through every relevant workspace, including long forms and manuscript navigation.
- Broaden keyboard, compact-screen, browser and input-method checks while retaining the fixture suite.

**Boundary:** Focused synthetic and imported-project walkthroughs passed. Everyday multi-session use and broad device coverage remain open.

**Acceptance:** Critical tasks are clear without coaching, prose keeps its space, and navigation/reload/failure cases retain writing and context.

**Prerequisites:** QQ-08, QQ-09, QQ-12

**Evidence / basis:** Existing integration reports document limited walkthroughs; this is the next wider acceptance pass

### QQ-22 — Publishing quality you can check

**Planned · Publishing & release**

Validate longer manuscripts and realistic formatting in the tools readers and writers actually use.

- External EPUB validation/reader checks and representative Word/HTML/print review.
- Document fonts, lists, tables, images and supported publishing-layout limits.

**Boundary:** Real export is already delivered. This milestone validates quality and resolves observed defects; it does not promise a full desktop publishing engine.

**Acceptance:** Representative exports open correctly, retain content/order and pass agreed format checks with visible limitations.

**Prerequisites:** QQ-13, QQ-21

**Evidence / basis:** docs/STABILIZATION_CLOSEOUT.md, publishing QA boundaries

### QQ-23 — An open alpha on Render

**Available in alpha · Publishing & release**

A separate hosted app where testers can register their own accounts and try Quantum Quill.

- Open registration is live on Render with a dedicated app, PostgreSQL database and persistent uploads. Recovered manuscripts stay local.
- Verified HTTPS sessions, writing saves, conflict rejection, account/image isolation, export and writing/uploads retained across deployment.
- Automatic service releases and Blueprint sync are off. The reviewed base hosting cost is $13.55/month; usage overages remain possible.

**Boundary:** Early alpha: email verification, password-reset email and self-service account deletion are not available. Public database access and storage autoscaling are disabled. Upstream editor/validation dependency upgrades remain tracked with scoped safeguards.

**Acceptance:** Staging passes real writer flows and account isolation; database/uploads restore is proven; costs and rollback are reviewed before release.

**Prerequisites:** QQ-01, QQ-21, QQ-22

**Evidence / basis:** Live October 24 at https://quantum-quill-alpha.onrender.com; release f0b8bba; docs/HOSTED_ALPHA.md and synthetic launch verification

### QQ-24 — Write with a full offline workspace

**Later · Writing & safety**

Go beyond durable draft recovery so the application itself can reopen without a network connection.

- Define secure offline caching and account-scoped local availability.
- Resume sync with explicit conflict handling and clear storage limits.

**Boundary:** Offline drafts are protected today if the app loads. Full offline loading and a complete version-history browser are not implemented.

**Acceptance:** The app loads offline, account changes never expose another account's content, and reconnect preserves newer writing on both sides.

**Prerequisites:** QQ-01, QQ-23

**Evidence / basis:** Explicit future boundary in recovery and workspace reports

### QQ-25 — Share and collaborate deliberately

**Later · Publishing & release**

Invite readers or collaborators with clear access and safe editing behavior.

- Define roles, invitations and project/file access before enabling sharing.
- Plan history and collaborative editing separately from today's conflict review.

**Boundary:** Sharing is labeled as planned in the app. Current revision checks are not multiplayer editing or collaborator permissions.

**Acceptance:** Access can be granted/revoked predictably, private files remain protected, and concurrent edits cannot silently lose writing.

**Prerequisites:** QQ-23

**Evidence / basis:** Deferred product scope; no delivery date or implementation claim

### QQ-26 — Explore the world as a graph

**Later · Story Bible**

Explore established relationships visually once the library, backlinks and chronology are useful.

- Navigate the shared ID-based links with filters and readable context.
- Keep the existing list/picker interfaces usable without the graph.

**Boundary:** Relationships and backlinks already work. A graph view and the legacy whiteboard are not active features.

**Acceptance:** The graph reads the same link model, stays navigable on large projects and never becomes the only way to edit connections.

**Prerequisites:** QQ-03, QQ-16

**Evidence / basis:** Deferred after shared relationships and chronology

### QQ-27 — Optional story assistance

**Later · Future formats & tools**

Explore assistance that supports the writer's decisions without taking ownership of the story.

- Begin with explicit, reviewable use cases and data/privacy choices.
- Separate suggestions from authored facts and manuscript text.

**Boundary:** No external AI generation or semantic scanner is active. Existing connection scanning is local name matching.

**Acceptance:** Suggestions are opt-in, explain their basis and never overwrite prose or establish story facts automatically.

**Prerequisites:** QQ-14, QQ-21

**Evidence / basis:** Later exploration, not a scheduled implementation

### QQ-28 — Beyond the novel

**Later · Future formats & tools**

Adapt the writing organizer for RPG campaigns, scripts, plays and historical storytelling.

- Identify the shared world, scene, reference and planning capabilities.
- Add format-specific workflows only after testing them with real examples.

**Boundary:** Novel writing is the current focus. These formats are product possibilities, not supported end-to-end workflows today.

**Acceptance:** Each new format has a demonstrated complete workflow without complicating or weakening novel writing.

**Prerequisites:** QQ-21, QQ-23

**Evidence / basis:** User's long-term product vision

### QQ-29 — Private tester feedback

**Available in alpha · Publishing & release**

Report bugs, confusing experiences and ideas from inside QQ without leaving your writing.

- Private report form with category, summary, details and app area; optional browser information and email follow-up.
- Account-scoped report receipts and recent history. Unsent feedback survives reload in the current browser tab; retries avoid duplicate reports.
- No prose, project names, screenshots or account secrets are attached automatically. Reports are visible only to their writer and the maintainer.
- Private admin inbox with report search, category/status filters, pagination and detailed review. Status updates appear in the tester’s own report history; stale changes are rejected.

**Boundary:** Admin inbox is live with explicitly provisioned maintainer access. This permission covers feedback only; it does not grant access to other writers’ manuscripts. No automatic email notifications or live-support response promise. Twenty new reports per account per day.

**Acceptance:** Live submission, privacy between accounts, idempotent retry, persisted history and unchanged writing verified; feedback survives the paired database restore.

**Prerequisites:** QQ-01, QQ-23

**Evidence / basis:** Private report release f0b8bba; admin inbox feature 7a3f09d. 391 tests / 38 suites, production PostgreSQL checks, 18-table restore and synthetic browser review passed. Owner access activated on October 24; anonymous access denied. See docs/FEEDBACK.md.

## Project notes

- Later: reconstruct the history of Quantum Quill from its surviving versions, archives and development records. This is a separate storytelling project, not a prerequisite for the alpha.
- October 23: public GitHub Pages roadmap published; eight actual-app screenshots prepared using original fictional sample content for alpha recruitment. The application itself remains a local alpha.
- October 24: public GitHub introduction, actual-app screenshots and tester feedback guide published. Open-registration Render alpha is prepared and locally checked; launch is on hold. No live app URL is advertised before verification.
- October 24: open-registration alpha launched on Render, with private in-app feedback. The user approved $13.55/month base hosting after an earlier hold. SDH Studio, original sources and recovered manuscripts remain unchanged.
- October 24: private maintainer inbox activated in the hosted alpha. Feedback can be reviewed and its status updated inside QQ; account permissions remain explicitly controlled.

## Maintenance

Edit roadmap.json and run python3 build.py. Do not mark a feature working without evidence for its accepted scope. Update both the checkpoint and validation date when verification actually changes. Preserve historical reports; this roadmap takes precedence over their stale future-work lists.

The roadmap contains no story prose, credentials, database contents or user email. Original sources, import receipts and backups remain private. The roadmap is published separately on GitHub Pages; application source and each writer’s data remain private.
