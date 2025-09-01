
# WorldCrafting 101 Style Guide — v1.1.1 (Fully Hardened Release)

## Core Modeling Philosophy

> Make the math beautiful, but make the interface humane.

This style guide defines the full writing, authoring, publication, and repository maintenance system for the WorldCrafting 101 project.

---

# 1 — Terminology and Term Styling

### 1.1 First-use Definitions

- Use `***Bold Italic***` for first-use of defined terms.
- Example: `A ***planemo*** is...`

### 1.2 Subsequent Mentions

- Use `*Italic*` for references to previously defined terms.

### 1.3 Sub-definitional Emphasis

- Use `**Bold**` for emphasis within definitions (e.g. qualifiers like **immediately habitable**).

### 1.4 Colloquial Emphasis

- Use `*Italic*` for casual narrative emphasis.

---

# 2 — Dialogue Persona Inserts

### 2.1 Structure

- Persona inserts use bold name labels (e.g., `**Hippy:**`), followed by the dialogue.
- Images inserted inline next to persona label (Obsidian-native syntax `![[filename|width]]`).

### 2.2 Color Coding (authoring-only)

- Hippy: orange (philosopher)
- Keppy: brown (technical)

### 2.3 Persona Insert Frequency Rule

> Use persona inserts at key teaching moments; avoid overuse within a single concept block.

### 2.4 Speaker Label Accessibility Rule

> Always include the speaker label (`**Hippy:**`) even with portraits to ensure screen-reader accessibility.

### 2.5 Persona Image Handling Rule

- Use Obsidian’s `![[portrait|width]]` syntax during authoring.
- Maintain master full-res images in vault.
- Pre-scale images or convert links to standard Markdown for external publication if needed.

---

# 3 — Glossary and Terminology Roundups

### 3.1 Local Roundups

- Each major section may include a *Terminology Roundup* in order of introduction.
- Entry terms in `**Bold**` label before the definition.

### 3.2 Global Lexicon

- Global glossary is alphabetized for reference.

---

# 4 — Footnotes

### 4.1 Usage

- Footnotes used exclusively for source citations.

### 4.2 Labeling

- Use **named labels** (e.g., `[^IAU]`) instead of numeric indices.

---

# 5 — Mathematical Notation

### 5.1 Units and Symbols

- Use Unicode symbols inline:
  - Earth ⨁ (terran), Sun ⊙, Moon ☽, Jupiter ♃.

### 5.2 Inline Formulas

- Prefer plain text + Unicode where possible.
- Use limited inline LaTeX `$...$` only when Unicode can't handle (e.g., subscripts).

### 5.3 Block Equations

- Use full LaTeX inside `$$...$$` blocks for major equations.

### 5.4 Equation Formatting Rule Summary

| Context | Preferred Style |
|---------|------------------|
| Inline narrative | Plain text + Unicode |
| Variable subscripts | Inline LaTeX only if needed |
| Full equations | Block LaTeX (`$$ ... $$`) |

---

# 6 — Export and Publication Workflow

### 6.1 Publication Model Rule

> Authoring is done fully within Obsidian vault using Obsidian-native features. Public-facing repositories only contain final PDF exports; the source Markdown corpus remains private.

### 6.2 Authoring Color Rule

> Author-facing color coding may be used for visual organization. All color cues flatten to black on export. Public-facing formatting uses speaker labels, portraits, and bold/italic structure.

### 6.3 Publication Architecture Rule

> Public repos receive only rendered deliverables (PDF, etc.). Source files and vault remain internal.

### 6.4 Git Ignore Safety Rule

> Verify `.gitignore` is fully configured before initial commit. Use `git rm --cached .` when cleaning existing tracked files.

### 6.5 GitHub Authentication Rule

> Use Personal Access Tokens (PAT) or SSH keys for GitHub authentication; password authentication is deprecated.

---

# 7 — Repository Maintenance

### 7.1 Backup Discipline

> Use a private repository or local Git repo for full vault backup and version control.

### 7.2 Bootstrap Rule (for repo creation)

> Always create the remote repo on GitHub first, then initialize and link the local repository. Avoid GitHub Desktop’s "create from local" workflow to prevent sync inconsistencies.

---

# 8 — Miscellaneous

### 8.1 Language Usage

- Use _sed ego dico_ for creative license ("because I say so").
- Use _mundus tuum est_ as creative motto ("it's your world").

### 8.2 Standard Abbreviations

- Avoid ambiguous abbreviations.
- Always clarify absolute vs relative units.

---

# 9 — Summary of Named Rules

| Rule Name | Summary |
| --------- | ------- |
| **First-Use Definition Rule** | `***Bold Italic***` for first use |
| **Term Mention Rule** | `*Italic*` for mentions |
| **Sub-Definition Emphasis Rule** | `**Bold**` for qualifiers |
| **Colloquial Emphasis Rule** | `*Italic*` for narrative emphasis |
| **Glossary Label Rule** | `**Bold**` for glossary entries |
| **Glossary Organization Rule** | Introduction order locally, alphabetized globally |
| **Footnote Label Rule** | Named labels (`[^IAU]`) |
| **Footnote Usage Rule** | Citations only |
| **Equation Formatting Rule** | Unicode inline, LaTeX block |
| **Persona Insert Frequency Rule** | Use inserts at key teaching moments |
| **Speaker Label Accessibility Rule** | Always include bold speaker labels |
| **Persona Image Handling Rule** | Use Obsidian image sizing; pre-process for external publishing |
| **Authoring Color Rule** | Authoring-only color, flattening on export |
| **Publication Model Rule** | Source stays private; publish rendered deliverables |
| **Publication Architecture Rule** | Single public PUB repo for rendered output |
| **Git Ignore Safety Rule** | Validate .gitignore before initial commit |
| **GitHub Authentication Rule** | Use PAT or SSH |
| **Bootstrap Rule** | Create remote repo first, then link local |
