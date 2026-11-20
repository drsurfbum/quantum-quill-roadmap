# Quantum Quill feature roadmap

Status checked November 20, 2026. Feature checkpoint: November 20, 2026 (`0e5f7b2dd3a5feb779494eefa98422effd28403c`).

A dependable place to plan a story, build its world, and keep writing. Novel writing comes first; the foundations should also serve other kinds of storytelling.

Canonical app repository: https://github.com/drsurfbum/quantum-quill-app

This is a manually maintained snapshot, not live sync. Working locally is not a deployment or main-branch merge claim. No delivery dates or percentage-complete estimate are assigned.

November 20 release: Duplicate Chapter and the iPad/Android Home Screen guide are deployed at https://quantquill.io as 0e5f7b2 through app PR #7. All four candidate-head GitHub checks passed; the merged file tree exactly matches that tested candidate. Verification includes 527 tests/50 suites, PostgreSQL copy/history/concurrency/rollback, synthetic production startup and 19-table paired restore, and Chromium/WebKit copy/editor/history/save/recovery checks. The chapter menu/dialog pointer-lock defect found during integration is fixed. Live health, public guide/Login navigation, anonymous copy/history-access denial and exact deployed assets were verified. No hosted manuscript was edited for verification. No schema, dependency, retention or hosting-plan change. MCP remains a separate local-only candidate: all four checks pass at 7101b07 against its November 16 base, but actual desktop conversations and current-release compatibility review remain pending. Hosted assistant transport is separate work. Physical device installation and software-keyboard acceptance remain open.

## Milestones

- **M0 — Protect the writing · Foundation working**: Reliable saves, recoverable drafts, ownership and compatible data reads.
- **M1 — Finish the novel workflow · Workflow working**: Plan, organize, write and export without losing momentum.
- **M2 — Make the world easier to build · Guided entries in alpha**: Guided entries and improved library search are in the alpha; character development, research and broader world-building work remain ahead.
- **M3 — Open alpha & feedback · Alpha live; hardening continues**: Real-world testing with private reports, dependable hosting and restore rehearsals.
- **M4 — More ways to tell stories · Later**: Broader formats and optional advanced tools, after the novel foundation.

## Keep in view

- **Duplicate chapters and Home Screen help are live**: Use a chapter’s options menu to create an independent copy with its prose, scenes and references. Help now opens illustrated iPad/Android Home Screen instructions in a separate tab. Writing history, Word Finder and save protections remain in place.
- **Keep legacy conversion deliberate**: Four older entries still need a destination decision; two classification conflicts and orphan planning records remain preserved. Compatibility reads work. No destructive migration is approved.
- **Watch history growth; keep testing real writing**: Storage has headroom and the paired backup restore passed. History cleanup is still dry-run only: nothing expires automatically. Monday reviews include storage and backup freshness; physical iPad/software-keyboard and sustained real-story acceptance remain open.
- **Local assistant checks pass; desktop acceptance remains**: All four exact-head checks pass for the local MCP candidate. Actual Claude/ChatGPT desktop setup and conversations still need owner-assisted testing. Hosted assistant access requires a separate secure connection; it is not enabled by this release.
- **Build a read-only workspace companion**: A new feature chat is implementing the approved assistant direction across all five workspaces. It will answer and suggest with selected context while leaving story records unchanged. Provider configuration, usage limits, writing-protection checks and PR review are part of delivery.

## Features

### QQ-01 — Writing you can recover

**Available in alpha · Writing & safety**

Keep drafts through failed saves and reloads, with explicit choices when another tab or device has newer writing.

- Account/project-scoped durable draft journals and serialized autosave.
- Server revisions, restore/discard review and protected navigation/export.

**Boundary:** Draft recovery protects unsaved work; durable saved-version browsing is now available separately in QQ-31. This is not full offline app loading.

**Acceptance:** Offline edits remain recoverable; reconnect cannot silently replace newer server writing; switching accounts cannot reveal another account's drafts.

**Prerequisites:** None.

**Evidence / basis:** docs/DRAFT_RECOVERY_AND_DATA_INTEGRITY.md; save, recovery and conflict suites; included in verified alpha release d610409. November 15 regression testing used fictional fixtures; this is not a new per-feature hosted manuscript edit.

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

**Available in alpha · Story Bible**

Connect all seven entry types by identity, with roles, context, dates and useful backlinks.

- Shared searchable relationship picker, safe stubs and current target names.
- Event participation/consequences, group membership, location governance/history and world-element usage/references.

**Boundary:** Same-project validation, hierarchy cycle checks and archive/delete guards work. A visual graph is a separate later feature.

**Acceptance:** Create, edit, remove and rename-target round trips retain meaning; invalid targets/cycles are rejected; linked deletion has predictable behavior.

**Prerequisites:** QQ-01

**Evidence / basis:** docs/SHARED_RELATIONSHIPS.md; relationship API and field suites; included in verified alpha release d610409. November 15 regression testing used fictional fixtures; this is not a new per-feature hosted manuscript edit.

### QQ-04 — Start with a little guidance

**Available in alpha · Planning**

Use the New Project and Blueprint wizards, or skip planning and go straight to writing.

- Recoverable New Project Wizard and restored Blueprint Wizard.
- Create project structure and scenes without replacing existing prose.
- Eight plot-structure guides with optional embedded explainer videos and external fallbacks; viewing guidance does not change the selected structure.

**Boundary:** Planning remains optional and wizard drafts stay protected. External video availability can vary by publisher or region; every guide retains a fallback. Playback of every source was not recertified in this release.

**Acceptance:** Wizard progress is recoverable and repeatable; direct-to-writing remains a first-class path.

**Prerequisites:** QQ-01

**Evidence / basis:** docs/WIZARDS_AND_SCENES.md; later stabilization closeout supersedes its old limitations; included in verified alpha release d610409. November 15 regression testing used fictional fixtures; this is not a new per-feature hosted manuscript edit. Plot-guide PR #1; combined viewer/selection/close walkthrough passed.

### QQ-05 — From plot point to prose

**Available in alpha · Planning**

Move from Storyboard plot points to Outline scenes, scene story beats and manuscript writing.

- Scene planning and story beats connect the Storyboard, Outline and Write workflows.
- Existing outline notes and chapter-only writing remain available.

**Boundary:** Planning is optional. The complete journey still needs more sustained real-project usability testing.

**Acceptance:** A writer can start at any stage, follow a planned scene into Write and retain plans separately from prose.

**Prerequisites:** QQ-04

**Evidence / basis:** docs/SCENE_OUTLINE_WORKFLOW.md; planning and scene-beat tests; included in verified alpha release d610409. November 15 regression testing used fictional fixtures; this is not a new per-feature hosted manuscript edit.

### QQ-06 — Shape the manuscript safely

**Available in alpha · Planning**

Reorder, move and duplicate chapters and scenes while preserving writing and references.

- Persisted chapter/scene ordering with atomic moves and stale-arrangement checks.
- Safe chapter rename/completion and guarded chapter deletion.
- Duplicate Chapter saves pending writing first, copies chapter prose or all scenes/plans/beats/valid Bible references, and creates independent revisions and saved history. Retries do not create a second copy; the source remains unchanged.

**Boundary:** Both original and copied chapters appear in exports. Plot links stay with the original; shared Story Bible entries remain shared. This is not a hidden alternate draft. Mixed prose ownership and invalid references block copying. Scene deletion and automatic writing-mode conversion remain unavailable.

**Acceptance:** Moving/reordering preserves prose, scene plans and references; conflicting arrangements are rejected without partial updates.

**Prerequisites:** QQ-01, QQ-05

**Evidence / basis:** docs/STABILIZATION_CLOSEOUT.md; manuscript API and PostgreSQL rehearsal; included in verified alpha release d610409. November 15 regression testing used fictional fixtures; this is not a new per-feature hosted manuscript edit. November 20: PR #7 deployed as 0e5f7b2; 527 tests/50 suites, PostgreSQL atomic rollback/idempotency/concurrency and independent history, plus Chromium/WebKit pending-save/copy/undo/redo/restore/source-isolation checks passed. See docs/RELEASE_DUPLICATE_GUIDE_NOV20.md.

### QQ-07 — A writer's formatting toolkit

**Available in alpha · Writing & safety**

Use fonts, rich formatting and reusable Quill styles without giving up protected saves.

- Font/size, headings, emphasis, color, paragraph controls, lists, tables, images and find/replace.
- Premade typographic styles and account-level custom saved styles.

**Boundary:** This is not a paginated publishing engine. Footnotes, headers/footers and tracked changes remain outside the current editor.

**Acceptance:** Formatting and custom styles survive save/reload, export within documented limits and draft recovery.

**Prerequisites:** QQ-01

**Evidence / basis:** docs/WRITE_FORMATTING.md; formatting, style and export tests; included in verified alpha release d610409. November 15 regression testing used fictional fixtures; this is not a new per-feature hosted manuscript edit.

### QQ-08 — Give the prose room

**Available in alpha · Workspace**

Keep prose central, with a compact manuscript navigator and separate scene/context panes.

- Shared workspace navigation and a responsive, single-row formatting bar.
- Reserved save-status space and context panels that preserve editor state.
- A discreet roadmap link in workspace navigation and the dashboard sidebar opens a separate tab without leaving the writing session.

**Boundary:** Available in alpha. Broad mobile, input-method and physical-device certification remains open; tested compact layouts do not imply full device coverage.

**Acceptance:** Opening cards or plans does not push prose down, reset the editor or remove formatting tools.

**Prerequisites:** QQ-07

**Evidence / basis:** docs/WORKSPACE_INTEGRATION.md; workspace writing tests and fixture walkthrough; October 23 roadmap shortcut (0067b97): type check, production build and browser walkthrough; included in verified alpha release d610409. November 15 regression testing used fictional fixtures; this is not a new per-feature hosted manuscript edit.

### QQ-09 — A readable Story Bible library

**Available in alpha · Story Bible**

Find an entry and work in a focused detail pane instead of navigating oversized category dashboards.

- Seven types, search, filters, stars, archive and sorting.
- Overview, Develop, Connections and preserved imported Source views.
- Tablet-friendly Find dialog with bounded result scrolling, preserved search focus and title-only Boolean filtering; shared pickers retain the same project boundaries.

**Boundary:** Guided creation and field help are now delivered in QQ-14. Search passed WebKit and Chromium coverage; physical iPad and its software keyboard still need a device walkthrough.

**Acceptance:** Filters persist, narrow screens have clear navigation, every field remains available and tab changes preserve unsaved edits.

**Prerequisites:** QQ-01, QQ-03

**Evidence / basis:** docs/STORY_BIBLE_WORKSPACE.md; library and mounted-editor tests; included in verified alpha release d610409. November 15 regression testing used fictional fixtures; this is not a new per-feature hosted manuscript edit. Tablet search PR #3; 14 picker and 6 Boolean browser cases passed.

### QQ-10 — Keep the world beside the writing

**Available in alpha · Workspace**

Link elements inline and use interactive cards without leaving the Write workspace.

- Type @ or link selected words; pin viewpoint, cast, locations and references to a scene.
- Open facts, relationships and scene notes; edit the full entry in place.

**Boundary:** Renaming an entry updates its card, not the author's words. Inline mentions and scene pins remain separate connections.

**Acceptance:** Card edits and prose save independently; links survive undo, formatting and recovery; foreign targets are rejected.

**Prerequisites:** QQ-03, QQ-08

**Evidence / basis:** docs/WORKSPACE_INTEGRATION.md; docs/SCENE_STORY_BIBLE.md; included in verified alpha release d610409. November 15 regression testing used fictional fixtures; this is not a new per-feature hosted manuscript edit.

### QQ-11 — Find missing scene connections

**Available in alpha · Story Bible**

Scan the current scene for mentions of existing entries, then review what should be connected.

- Read live prose, including unsaved text; show excerpts and flag ambiguous names.
- Default to a mentioned reference; the writer may choose cast or setting before adding.

**Boundary:** Current scene only. Literal name/alias matching, not semantic inference. No new entries, automatic linking or prose edits.

**Acceptance:** Linked/archived/foreign entries are excluded, stale scans require review, and approved connections use the existing protected save queue.

**Prerequisites:** QQ-10

**Evidence / basis:** docs/SCENE_STORY_BIBLE.md, October 14 addition; 380 tests / 36 suites recorded; included in verified alpha release d610409. November 15 regression testing used fictional fixtures; this is not a new per-feature hosted manuscript edit.

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

**Available in alpha · Story Bible**

Make it obvious what each element is for, which fields matter first, and how to develop it.

- Explain the purpose of all seven existing types with concrete examples and overlap guidance, including Details versus Research versus World Elements.
- Create an unfinished entry with only a name and type; develop it through Start here and optional field groups, with examples that never become authored content.
- Offer optional connection ideas through the shared picker, retaining specialized fields, imported sources, unknown values and existing save/recovery protections.

**Boundary:** Live through reviewed PR #4. All 265 existing field bindings and retained legacy content remain intact. Character development, chronology, research-library expansion and project-wide scanning are separate work. Original feature branches and older local edits are preserved.

**Acceptance:** A new writer can create and develop an element without guessing field meaning; every existing field, link and recovered original still round-trips.

**Prerequisites:** QQ-09

**Evidence / basis:** Alpha release d610409, https://github.com/drsurfbum/quantum-quill-app/pull/4; docs/GUIDED_STORY_BIBLE.md and docs/RELEASE_2026_11_15.md. Combined release: 464 tests/44 suites, 265-binding comparison, 16 synthetic Chromium checks across all seven entry types, GitHub production-style database/restore and browser checks passed.

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

**Evidence / basis:** Existing integration reports document limited walkthroughs; this is the next wider acceptance pass; November 15 adds combined guided-entry, tablet and prose recovery/conflict fixture walkthroughs. Physical devices and everyday multi-session real-story use remain outstanding.

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

- Open registration is live on Render with a dedicated app, PostgreSQL database and persistent uploads. Local originals remain preserved; hosted stories stay private to their accounts.
- Verified HTTPS sessions, writing saves, conflict rejection, account/image isolation, export and writing/uploads retained across deployment.
- Automatic service releases and Blueprint sync are off. The reviewed base hosting cost is $13.55/month; usage overages remain possible.

**Boundary:** Early alpha: email verification, password-reset email and self-service account deletion are not available. Public database access and storage autoscaling are disabled. Upstream editor/validation dependency upgrades remain tracked with scoped safeguards.

**Acceptance:** Staging passes real writer flows and account isolation; database/uploads restore is proven; costs and rollback are reviewed before release.

**Prerequisites:** QQ-01, QQ-21, QQ-22

**Evidence / basis:** Verified alpha https://quantquill.io, release ce88058 on November 16. PRs #5/#6 and all merged-head checks passed. Migrations 0007/0008 were applied after independent paired backup/restore rehearsal, with original rows and uploads unchanged. Previous code starts against the additive schema for rollback; rolling back code does not capture new history. Database storage was 8.49% of its 1 GB disk at review; uploads were about 16 MB. The three-day provider recovery window was available. Monday PM reviews now include capacity and backup freshness; no new paid resources, automatic pruning or database exposure.

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

### QQ-27 — External assistant access (MCP)

**First slice working · Future formats & tools**

Let a writer explicitly connect an external assistant with narrow, revocable access and reviewable edits.

- Local MCP 0.1.0 candidate with independent project, editing and manuscript permissions; narrow read-only defaults and revocable access.
- Versioned field guide, bounded reads and revision-checked edits; no automatic manuscript changes.
- Assistant chapter/scene edits use the same transactional writing-history and revision checks as ordinary writing; newer edits block stale restoration and revocation is enforced on subsequent calls.
- Separate exploratory plot-review tools remain local and are not part of the published candidate.

**Boundary:** PR #2 at 7101b07 passed all four final-head GitHub checks against the November 16 ce88058 release. Actual Claude Desktop and ChatGPT Desktop conversations remain the acceptance gate. Hosted assistant access is disabled; a secure hosted transport is separate work. MCP is not included in the Duplicate Chapter/Home Screen release and will need a compatibility review against its updated base before merge.

**Acceptance:** Suggestions are opt-in, explain their basis and never overwrite prose or establish story facts automatically.

**Prerequisites:** QQ-14, QQ-21

**Evidence / basis:** November 18: PR #2 head 7101b072bc9acd1b88cc3a16028f17e1a2b2ead4; all four GitHub checks pass, including both stabilization runs, guided Bible and combined Chromium/WebKit history checks. Local evidence includes 509 tests/48 suites, 16 MCP tests, protocol-to-history integration, revision/conflict/revocation checks and paired restore across 20 tables. The prior browser setup timeout was fixed with the pinned official Playwright container without reducing coverage. Migration 0009 is undeployed; deployed 0007/0008 and bootstrap are unchanged. Protocol/RPC checks do not certify desktop conversations. https://github.com/drsurfbum/quantum-quill-app/pull/2.

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

### QQ-30 — Find your way around Quantum Quill

**Available in alpha · Workspace**

Find your way around the workspace with an optional tour and illustrated Home Screen instructions.

- Ten steps introduce projects, planning, manuscript navigation, prose, Story Bible, context cards and Help; starting inside a project skips the dashboard step.
- Skip, keyboard controls and Help → Replay tour; an empty account can continue after creating its first project through the existing wizard.
- Account-scoped browser preferences, save/recovery/dialog pauses, responsive target positioning and no tour-created chapters or prose edits.
- Public iPad Safari/Android Chrome Home Screen guide at /help/install, linked from Login and Help. Help opens a separate tab so writing stays open; all instructions remain readable independently of the illustrations.

**Boundary:** Live in the alpha, alongside QQ-14 guided entries. The interface tour and Story Bible guidance remain separate, optional flows. Preferences are local to each browser, not synced across devices. Native screen-reader and broader device certification remain open. The Home Screen guide documents browser shortcuts; it does not add offline support, native/store installation, a guaranteed icon or persistent sign-in. Actual physical iPad/Android installation remains unverified.

**Acceptance:** Navigation advances once after the destination loads; Back and replay work; empty and compact layouts remain usable; missing controls provide an exit; save/recovery flows take priority and existing writing stays unchanged.

**Prerequisites:** QQ-01, QQ-08, QQ-10

**Evidence / basis:** Live release 6ecad66; feature d6fb8f6; docs/INTERFACE_TOUR.md. October 26: exact-release CI passed 403 tests / 40 suites, TypeScript, production build and synthetic database/upload restore. Desktop/390px fixture walkthroughs passed. Live tour, reload/replay/skip, session continuity and unchanged inspected prose/formatting verified without editing hosted writing. November 20: guide released in PR #7 as 0e5f7b2; all ten steps, keyboard controls, responsive/dark/reduced-motion checks pass. Chrome/WebKit verify opening Help while copied-scene writing saves. Public hosted guide and navigation verified anonymously.

### QQ-31 — Revisit and restore writing versions

**Available in alpha · Writing & recovery**

Visible Undo/Redo and durable chapter or scene history are available in the alpha, with preview, comparison and deliberate restoration.

- Visible Undo/Redo, saved prose history, formatted preview/compare and explicit restoration as a new current revision. Existing recovery and account/project/document boundaries remain in force.
- Keep this version and protected restore checkpoints preserve selected, outgoing and restored versions; exact version download is available.
- Tiered retention review shows protected/candidate counts and storage estimates. Cleanup is dry-run only: zero versions deleted, no cleanup job and no reduced capture cadence.
- Named alternate drafts remain future work. Duplicate Chapter is available separately under QQ-06; each copy starts independent saved history on its first changed save.

**Boundary:** Live in ce88058 after shared-editor reconciliation, capacity review, independent paired backup/restore and additive migrations 0007/0008. History begins with changed saves after this release; earlier drafts are not retroactively reconstructed. Retention is dry-run only: actual expiry requires separate review and implementation. Physical iPad/software-keyboard and assistive-technology acceptance remain open. Version history supplements independent backups.

**Acceptance:** A writer can undo/redo edits and inspect/restore a saved version without losing current work, formatting or inline references. Restore creates a new current revision, respects account/project access and conflicts, and survives reload.

**Prerequisites:** QQ-01, QQ-06

**Evidence / basis:** November 16: PR #5 (https://github.com/drsurfbum/quantum-quill-app/pull/5) merged as ce88058 and deployed to quantquill.io. Five checks at integration head 134028e and three workflows at the merge passed; 509 tests/48 suites, combined Chromium/WebKit Word Finder/history/save-recovery checks and synthetic 19-table paired restore. The actual pre-release backup restored exactly, both migrations and repeat runs passed, and old/new builds started against the migrated copy. Post-deploy health, auth boundaries, asset checks and unchanged original data/uploads passed. See docs/WRITING_VERSION_HISTORY.md. This does not claim a new hosted-manuscript restore or physical-device test.

### QQ-32 — Find the right word while writing

**Available in alpha · Writing tools**

An English dictionary and thesaurus is available inside Write, with sense-grouped results and explicit, undoable replacement.

- Look up selected text or a typed English word or expression; show definitions, sense-grouped synonyms/antonyms, examples and related concepts.
- Pinned, attributed Open English WordNet 2025 data is self-hosted as static compressed shards. Lookup runs in the browser; requests use a bucket identifier rather than a lookup word or surrounding manuscript.
- Choosing a result previews it. Only Replace selection changes prose, preserves supported formatting and creates its own Undo/Redo step. Stale selections, changed scenes and semantic links block unsafe replacement.
- Word Finder, visible Undo/Redo, History, inline Bible linking and the full formatting controls coexist in the fixed-height toolbar. Combined chapter/scene checks preserve selection guards and save/recovery behavior.

**Boundary:** Live with writing history in ce88058. English only; modern DecompressionStream support is required. Dataset coverage varies; rhymes and sound-based discovery are not delivered. Physical iPad/software-keyboard acceptance remains open. No external lookup provider, new database, hosting service, package dependency or app version bump is included.

**Acceptance:** A writer can find a useful alternative without losing cursor position, formatting, save status or prose space. Results state their source; loading, no-match and unavailable states work. Any replacement is deliberate and undoable.

**Prerequisites:** QQ-07, QQ-08

**Evidence / basis:** November 16: PR #6 (https://github.com/drsurfbum/quantum-quill-app/pull/6) merged as 3daa3fc and released in ce88058 after combined history integration. All final integration/merged-head workflows passed. Chromium/WebKit fixtures cover chapter/scene replacement, formatting, visible undo/redo, history restore, pending/failed saves, stale selections and navigation. Live app assets, dictionary manifest and a lookup bucket exactly match the reviewed build; anonymous history access is denied. See docs/WORD_FINDER.md for data provenance and limitations. Fixture interaction results are not a new hosted manuscript edit.

### QQ-33 — Workspace assistant (read-only)

**Planned · Writing & planning**

Discuss a scene, develop a character or plan the next session from a companion panel inside Quantum Quill.

- An opt-in assistant across Write, Outline, Storyboard, Story Bible and Overview, with workspace-specific prompts and explicitly selected context.
- Read-only answers and suggestions with inspectable sources. Manuscript inclusion is separate and deliberate; no automatic whole-project attachment.
- Use the existing context-panel space so prose stays prominent, with a dismissible narrow-screen panel and usable message composer.
- Account/project-scoped conversations, server-enforced read-only access, bounded provider requests and enforceable usage limits.

**Boundary:** Implementation has started in a dedicated feature chat following an approved fictional design study. No application capability is validated or deployed yet. Mockup preview/apply/undo controls illustrate a later editing capability and are excluded from this read-only release. Provider setup and an initial usage allowance remain release configuration decisions; external MCP remains separate under QQ-27.

**Acceptance:** All five workspaces support a useful contextual conversation without modifying story records. Context and manuscript inclusion are explicit; account/project switches cannot leak conversations or late responses. Existing formatting, autosave, offline recovery, revisions, history, inline links and Word Finder remain intact. Appropriate fixture/browser checks and a reviewed PR precede deployment.

**Prerequisites:** QQ-01, QQ-02, QQ-08, QQ-14, QQ-21

**Evidence / basis:** November 20: owner approved the five-workspace HTML direction and commissioned read-only implementation in a new feature chat. The separate mockup uses fictional content and scripted responses; Chromium/WebKit checks cover its interactions and narrow layouts. Those checks validate the design study only, not a working AI integration. No feature PR, provider call or deployment is claimed.

## Project notes

- Later: reconstruct the history of Quantum Quill from its surviving versions, archives and development records. This is a separate storytelling project, not a prerequisite for the alpha.
- October 23: public GitHub Pages roadmap published; eight actual-app screenshots prepared using original fictional sample content for alpha recruitment. The application itself remains a local alpha.
- October 24: public GitHub introduction, actual-app screenshots and tester feedback guide published. Open-registration Render alpha is prepared and locally checked; launch is on hold. No live app URL is advertised before verification.
- October 24: open-registration alpha launched on Render, with private in-app feedback. The user approved $13.55/month base hosting after an earlier hold. SDH Studio, original sources and recovered manuscripts remain unchanged.
- October 24: private maintainer inbox activated in the hosted alpha. Feedback can be reviewed and its status updated inside QQ; account permissions remain explicitly controlled.
- October 24: QQ-14 guided Story Bible implemented and backed up on a private feature branch, with full validation and synthetic desktop/compact browser evidence. The public alpha has not been updated with QQ-14; main is unchanged.
- October 26: first-use interface tour validated locally and pushed to its separate feature branch. Save/recovery guards remain intact. QQ-14 work is preserved separately; neither feature is merged or deployed by this update.
- October 26: user-approved tour integration released to the live alpha as 6ecad66. QQ-30 is available through the first-use invitation or Help → Replay tour. No schema/configuration change; existing writing and the separate QQ-14 feature branch remain intact.
- October 26: quantquill.io is the verified primary alpha address, with HTTPS and a www redirect. The original Render address remains available; application code and writing are unchanged.
- November 15 PM checkpoint: canonical app repository is public; private manuscripts, account data, backups and credentials remain excluded. Every repository change needs at least a draft PR. New features use separate chats; feature updates reuse their owner chat. Merging and deployment remain separate decisions.
- November 14–15 release queue: expert plot guides/videos merged in PR #1 but not deployed. Tablet Story Bible search and Boolean filtering are in draft PR #3, with 445 tests and 20 browser cases recorded; physical iPad testing remains open. Local MCP candidate is in draft PR #2; full desktop conversational acceptance remains pending.
- Local-only queue: Duplicate Chapter, iPad/Android Home Screen help, README screenshot updates and app 1.0.1 bump are prepared but not published or deployed. Separate plot-review experiments remain outside the MCP candidate. Existing publication holds and feature ownership are preserved.
- November 15: requested durable writing version history/clear undo-redo (QQ-31) and creative dictionary/thesaurus (QQ-32). Discovery is separate from implementation; neither is advertised as available.
- November 15 release: tablet search PR #3 and guided Story Bible PR #4 merged through review, then deployed with plot-video PR #1 as d610409. The deployed tree matches the tested candidate. No writing/save/server/schema/dependency changes were introduced by this integration; previous live 6ecad66 remains the code rollback point.
- November 15 validation: 464 tests/44 suites; TypeScript/build; 16 guided-entry, 20 search and 4 combined writer/video browser checks; GitHub production-style PostgreSQL and paired restore. Live checks are read-only health/auth/asset verification. Fresh browser writing checks used fictional loopback data; no hosted manuscripts were edited.
- PM owns roadmap upkeep after releases and scope changes. Weekly Monday reviews run at 9 a.m. America/Chicago and prepare correction PRs when needed. Recurring reviews do not independently authorize feature merges, deployments or new charges.
- Remaining release follow-ups: physical iPad/software-keyboard acceptance, sustained everyday writer testing and existing dependency advisories. The production audit reports one high Zod and 33 moderate advisories; the existing input-structure limit remains a mitigation, not a resolved dependency upgrade. Track upgrades separately through review.
- Current availability labels reflect deployed scope and existing verification. Some older foundation cards were previously still labeled local; they are now labeled available in alpha. This does not claim broad device certification or replace the remaining acceptance work.
- November 16 PM review: live release and release-source branch remain d610409; the published roadmap remains the November 15 release snapshot until this correction PR is approved. Public health/login passed, anonymous access remained denied and no application errors were returned since deployment. No new feature merge, deployment or live-data change was made.
- November 15 afternoon work, reviewed November 16: QQ-31 advanced from discovery to draft PR #5 with visible undo/redo, durable history, Keep this version and protected restore checkpoints. Its retention policy is dry-run only and the explicit no-merge/no-deploy instruction remains. All five exact-head checks passed at 3e082f0.
- QQ-32 advanced from discovery to draft PR #6 with self-hosted English WordNet lookup and explicit undoable replacement. All three exact-head GitHub checks are now successful at db3ea95, resolving the pending CI noted in the feature chat. Not merged or deployed.
- PRs #5 and #6 both change rich-text-editor/index.tsx and menu-bar.tsx. Separate passing checks do not validate their combined toolbar, selection, history and save behavior; integrate only in an approved review branch and preserve both feature owners. MCP PR #2 remains separate, with user-assisted desktop conversational acceptance pending.
- Next PM priorities: a physical iPad and sustained real-story walkthrough; review history retention/capacity/backup readiness without applying expiry; review Word Finder and the shared editor integration. Existing dependency maintenance and the local-only Duplicate Chapter/Home Screen candidates remain tracked, with their original holds.
- November 16 ready-PR follow-up: owner authorized advancing ready PRs. Word Finder PR #6 passed review and merged normally as 3daa3fc, with exact tree equality to the tested feature. App deployment remains separate and Render stays on d610409. Writing history PR #5 is still draft with shared-editor conflicts and release gates; MCP PR #2 still awaits desktop acceptance. Roadmap corrections are being published through roadmap PR #2, with no application/database/account changes or new charges.
- Historical dated notes above describe their original checkpoints. Current release availability is stated in the latest validation and feature boundaries; this roadmap is a snapshot rather than a live deployment feed.
- November 16 evening: writing history PR #5 merged after all checks passed; combined release ce88058 is live with Word Finder. The actual independent database/upload backup was restored before reviewed migrations 0007/0008, and original writing/accounts/uploads match after deployment. Storage and provider recovery were reviewed without plan changes; no history deletion or automatic expiry is enabled. Monday PM review now checks capacity and backup freshness. Physical iPad and sustained writer acceptance remain follow-up work.
- November 18: owner resumed the existing MCP agent to resolve current-release conflicts, rerun tests and prepare the desktop testing handoff. PM owns roadmap updates. No MCP merge, hosted transport, production migration, release tag or deployment is part of this assignment; existing writing safeguards and feature ownership remain in force.
- November 18 policy update: the owner removed separate publication approvals for routine roadmap/project-status/roadmap-maintenance updates. PM now reviews, validates, opens or updates the PR, normally merges and verifies publication under standing authorization. PRs, checks, private-data safeguards and explicit change-specific holds remain in force; the Monday review uses the same policy.
- November 18 MCP follow-through: current release merged normally into the existing feature branch as d6b77b5; conflicts resolved and new local writing-history, conflict, permission, browser and paired restore checks passed. Three GitHub checks pass; combined browser CI is retrying an environment dependency-download timeout. No MCP app merge, deployment or desktop conversation acceptance is claimed.
- November 20: owner authorized the two-feature release, superseding the older Duplicate Chapter/Home Screen local-only publication holds. Normal merges preserve c11753e and b678b72, then PR #7 released as 0e5f7b2. No MCP code or migrations were included; originals, feature ownership and private backups remain intact. Local-only README-image and patch-version work and exploratory plot-review tools remain separate. The November 18 MCP browser setup timeout is resolved: all four checks pass at 7101b07; desktop acceptance is still pending.
- November 20: owner approved the embedded-assistant mockups and requested a dedicated feature chat to build a read-only companion across Write, Outline, Storyboard, Story Bible and Overview. QQ-33 tracks this work separately from QQ-27 external MCP access. No editing/apply tools are included. Existing writing/save protections and PR-before-deployment workflow are mandatory; the design study is not a live AI feature.

## Maintenance

Edit roadmap.json and run python3 build.py. Do not mark a feature working without evidence for its accepted scope. Update both the checkpoint and validation date when verification actually changes. Preserve historical reports; this roadmap takes precedence over their stale future-work lists.

The roadmap contains no story prose, credentials, database contents or user email. Original sources, import receipts and backups remain private. The roadmap is published separately on GitHub Pages; the application source is public, while each writer’s account and story data remain private.
