
# WorldCrafting 101 Style Guide — v1.1.3 (Hardened Authoring System Release)

## Core Modeling Philosophy

> Make the math beautiful, but make the interface humane.

This style guide defines the full writing, authoring, publication, repository management, disaster recovery, and safe Git discipline system for the WorldCrafting 101 project.

---

# 1 — Terminology and Term Styling

### 1.1 First-use Definitions

- Use `***Bold Italic***` for first-use of defined terms.

### 1.2 Subsequent Mentions

- Use `*Italic*` for references to previously defined terms.

### 1.3 Sub-definitional Emphasis

- Use `**Bold**` for emphasis within definitions.

### 1.4 Colloquial Emphasis

- Use `*Italic*` for casual narrative emphasis.

---

# 2 — Dialogue Persona Inserts

### 2.1 Structure

- Persona inserts use bold name labels (e.g., `**Hippy:**`), followed by dialogue.
- Portrait images inserted inline via Obsidian-native syntax `![[filename|width]]`.

### 2.2 Color Coding (authoring-only)

- Hippy: orange (philosopher voice)
- Keppy: brown (technical voice)

### 2.3 Persona Insert Frequency Rule

> Use inserts at natural teaching moments. Avoid oversaturating any single section.

### 2.4 Speaker Label Accessibility Rule

> Always include speaker label text (`**Hippy:**`) to ensure accessibility regardless of image rendering.

### 2.5 Persona Image Handling Rule

- Use Obsidian `![[portrait|width]]` for writing.
- Maintain master full-res images.
- Pre-process for web publishing if necessary.

---

# 3 — Glossary and Terminology Roundups

### 3.1 Local Roundups

- Use "Terminology Roundup" sections, organized by order of introduction.

### 3.2 Global Lexicon

- Master global glossary maintained alphabetically.

---

# 4 — Footnotes

### 4.1 Usage

- Footnotes reserved for source citations only.

### 4.2 Labeling

- Use **named labels** (e.g. `[^IAU]`), never numeric indices.

---

# 5 — Mathematical Notation

### 5.1 Units and Symbols

- Unicode symbols inline:
  - Earth ⨁, Sun ⊙, Moon ☽, Jupiter ♃.

### 5.2 Inline Formulas

- Prefer plain text + Unicode.
- Limited inline LaTeX allowed for subscripts as needed.

### 5.3 Block Equations

- Use full LaTeX in block `$$...$$` formatting.

### 5.4 Equation Formatting Rule Summary

| Context | Preferred Style |
|---------|------------------|
| Inline narrative | Plain text + Unicode |
| Variable subscripts | Inline LaTeX if necessary |
| Full equations | Block LaTeX (`$$ ... $$`) |

---

# 6 — Export and Publication Workflow

### 6.1 Publication Model Rule

> Authoring stays private inside Obsidian. Public repos contain only final rendered PDFs or published exports.

### 6.2 Authoring Color Rule

> Author-facing color for clarity. Flattened to black for public export.

### 6.3 Publication Architecture Rule

> Single public PUB repo receives only exported deliverables.

### 6.4 Git Ignore Safety Rule

> Always verify `.gitignore` is complete before initial commit. Use `git rm --cached .` to clear staged files if needed.

### 6.5 GitHub Authentication Rule

> Use Personal Access Tokens (PAT) or SSH keys for GitHub access.

### 6.6 Bootstrap Rule

> Always create remote repo on GitHub first, then connect local repo.

### 6.7 Repository Reset Rule

> Fully delete local `.git/` directory to clean all prior history before recreating new repo.

### 6.8 Command-Line Authoring Workflow Rule

> Routine commits may be performed via terminal:

```bash
git add .
git commit -m "message"
git push
```

Use `git status` before committing to verify staged changes.

---

# 7 — Repository Maintenance and Disaster Recovery

### 7.1 Backup Discipline

> Always maintain full vault backups before any major repo surgery.

### 7.2 Disaster Recovery Rule

> If files are accidentally deleted locally, restore via:

- `git restore .` — for unstaged deletions.
- `git restore path/to/file.md` — for individual file recovery.
- GitHub web interface — to retrieve files from previous commits.
- `git reset --hard origin/main` — to fully reset local repo to remote state (dangerous: wipes uncommitted local changes).

### 7.3 Repository Navigation Rule

> Git commands must be executed from terminal in correct repo folder (`cd` to vault root where `.git/` lives).

---

# 8 — Language Usage and Abbreviations

### 8.1 Latin Usage

- _sed ego dico_: creative license
- _mundus tuum est_: creative ownership

### 8.2 Abbreviations

- Avoid ambiguous abbreviations.
- Always clarify absolute vs relative units.

---

# 9 — Summary of Named Rules

| Rule Name | Summary |
| --------- | ------- |
| First-Use Definition Rule | `***Bold Italic***` for first appearance |
| Term Mention Rule | `*Italic*` for term mentions |
| Sub-Definition Emphasis Rule | `**Bold**` for qualifiers |
| Colloquial Emphasis Rule | `*Italic*` for casual emphasis |
| Glossary Label Rule | `**Bold**` glossary entry labels |
| Glossary Organization Rule | Intro order locally; alphabetized globally |
| Footnote Label Rule | Named labels only (`[^IAU]`) |
| Footnote Usage Rule | Citations only |
| Equation Formatting Rule | Unicode inline; LaTeX block |
| Persona Insert Frequency Rule | Natural insertion points only |
| Speaker Label Accessibility Rule | Always include speaker labels |
| Persona Image Handling Rule | Obsidian image sizing; pre-process for web |
| Authoring Color Rule | Author-only color; export flattened |
| Publication Model Rule | Only publish rendered exports |
| Publication Architecture Rule | Single PUB repo for public deliverables |
| Git Ignore Safety Rule | Validate `.gitignore` before commit |
| GitHub Authentication Rule | Use PAT or SSH |
| Bootstrap Rule | Create remote first |
| Repository Reset Rule | Fully delete `.git/` to fully reset |
| Command-Line Authoring Workflow Rule | Use add/commit/push cycle |
| Backup Discipline Rule | Always backup before risky operations |
| Disaster Recovery Rule | Multiple recovery pathways for deletion |
| Repository Navigation Rule | Terminal context-sensitive to repo root |
