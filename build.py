"""Build the standalone, offline-capable roadmap from one reviewed data source."""
from pathlib import Path
import base64
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "roadmap.json").read_text())
features = data["features"]
ids = [f["id"] for f in features]
assert len(ids) == len(set(ids)), "Feature IDs must be unique"
statuses = {s["id"]: s["label"] for s in data["statuses"]}
for f in features:
    assert f["status"] in statuses, f"Unknown status: {f['id']}"
    assert all(i in ids and i != f["id"] for i in f["depends"]), f"Invalid dependency: {f['id']}"
    for key in ["title", "summary", "scope", "boundary", "acceptance", "evidence", "area"]:
        assert f[key], f"Missing {key}: {f['id']}"
for m in data["milestones"]:
    assert all(i in ids for i in m["features"])

payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
html = (ROOT / "template.html").read_text().replace("__DATA__", payload)
def source_hash(value):
    return "'sha256-" + base64.b64encode(hashlib.sha256(value.encode()).digest()).decode() + "'"
styles = re.findall(r"<style>(.*?)</style>", html, re.S)
scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", html, re.S)
csp = "default-src 'none'; base-uri 'none'; form-action 'none'; img-src data:; style-src " + " ".join(map(source_hash, styles)) + "; script-src " + " ".join(map(source_hash, scripts))
html = html.replace("__CSP__", csp)
assert "__DATA__" not in html and "__CSP__" not in html
(ROOT / "dist").mkdir(exist_ok=True)
(ROOT / "dist" / "index.html").write_text(html)
(ROOT / "docs").mkdir(exist_ok=True)
(ROOT / "docs" / "index.html").write_text(html)
(ROOT / "docs" / ".nojekyll").write_text("")

lines = ["# Quantum Quill feature roadmap", "", f"Status checked {data['checked']}. Feature checkpoint: {data['featureCheckpoint']} (`{data['localCommit']}`).", "", data["summary"], "", f"Canonical private repository: {data['repository']}", "", "This is a manually maintained snapshot, not live sync. Working locally is not a deployment or main-branch merge claim. No delivery dates or percentage-complete estimate are assigned.", "", data["validation"], "", "## Milestones", ""]
for m in data["milestones"]:
    lines += [f"- **{m['id']} — {m['title']} · {m['state']}**: {m['description']}"]
lines += ["", "## Keep in view", ""]
for a in data["attention"]:
    lines += [f"- **{a['title']}**: {a['text']}"]
lines += ["", "## Features", ""]
for f in features:
    lines += [f"### {f['id']} — {f['title']}", "", f"**{statuses[f['status']]} · {f['area']}**", "", f["summary"], ""]
    lines += [f"- {s}" for s in f["scope"]]
    lines += ["", f"**Boundary:** {f['boundary']}", "", f"**Acceptance:** {f['acceptance']}", "", f"**Prerequisites:** {', '.join(f['depends']) if f['depends'] else 'None.'}", "", f"**Evidence / basis:** {f['evidence']}", ""]
lines += ["## Project notes", "", *[f"- {note}" for note in data.get("projectNotes", [])], ""]
lines += ["## Maintenance", "", "Edit roadmap.json and run python3 build.py. Do not mark a feature working without evidence for its accepted scope. Update both the checkpoint and validation date when verification actually changes. Preserve historical reports; this roadmap takes precedence over their stale future-work lists.", "", "The roadmap contains no story prose, credentials, database contents or user email. Original sources, import receipts and backups remain private. The roadmap is published separately on GitHub Pages; the writing app and its data remain private.", ""]
(ROOT / "ROADMAP.md").write_text("\n".join(lines))
print(f"Built {len(features)} feature cards, {len(data['milestones'])} milestones, HTML and Markdown.")
