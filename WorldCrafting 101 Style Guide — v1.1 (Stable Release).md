
# WorldCrafting 101 Style Guide — v1.1 (Stable Release)

## Core Modeling Philosophy

> Make the math beautiful, but make the interface humane.

The purpose of this style guide is to maintain consistency, clarity, and legibility across all WorldCrafting 101 materials, while remaining friendly to worldbuilders, educators, and system designers. The guide is designed for use within Markdown-based environments (primarily Obsidian), with clean export to publishable formats.

---

# 1 — Terminology and Term Styling

### 1.1 First-use Definitions

- When introducing a newly defined term, format it as:  
  `***Bold Italic***`
- Example:  
  `A ***planemo*** is...`

### 1.2 Subsequent Mentions

- After first-use, refer to previously defined terms using:  
  `*Italic*`
- Example:  
  `All *planemos* have...`

### 1.3 Sub-definitional Emphasis

- When emphasizing key properties inside definitions, use:  
  `**Bold**`
- Example:  
  `**immediately habitable** by humans`

### 1.4 Colloquial or Conversational Emphasis

- Use `*Italic*` for casual emphasis inside narrative or dialogue.  
- Example:  
  `Micromos *can* be parahabitable.`

---

# 2 — Dialogue Inserts (Hippy/Keppy Conventions)

### 2.1 Dialogue Insert Structure

- Character name formatted as:  
  `**Color Bold Name:**`
- Portrait inserted inline next to the label.
- Dialogue immediately follows.

Example:

```markdown
![Hippy](Hippy-portrait.webp|60)
**Hippy:** So, a *world* is a *planemo*, but not all *planemos* are *worlds*.
```

### 2.2 Color Coding

- Hippy: orange (philosopher voice)
- Keppy: brown (technical voice)

### 2.3 Function

- Use personas to introduce clarifying questions, rule-of-thumb explanations, humorous asides, or common misconceptions.
- Persona dialogue should remain consistent in voice and role throughout.

### 2.4 Persona Insert Frequency Rule

> Use dialogue inserts sparingly, at natural learning inflection points. Avoid inserting Hippy/Keppy dialogue more than once per major concept block unless multiple distinct confusions are anticipated.

---

# 3 — Glossary and Terminology Roundups

### 3.1 Local Glossaries (Terminology Roundup Sections)

- Each major section may include a *Terminology Roundup*.
- Terms are listed in **order of introduction**, not alphabetically.
- Entry terms are formatted as:  
  `**Bold**` label before colon.

### 3.2 Global Glossary (Lexicon)

- The master global glossary will be maintained separately.
- The global glossary will be **alphabetized** for reference.

---

# 4 — Footnotes

### 4.1 Footnote Usage

- Footnotes are reserved **exclusively for source citations**.
- All definitions, explanations, and commentary remain inline.

### 4.2 Footnote Labeling

- Use **named labels** rather than numeric indices:
  - Example:  
    `[^IAU]`  
    `[^Basri]`
- This allows for human-readable Markdown source, simplifies editing, and avoids renumbering when sections are restructured.

---

# 5 — Mathematical Notation

### 5.1 Units and Symbols

- Use direct **Unicode symbols** in narrative text wherever possible:
  - Earth: ⨁ (terran)
  - Sun: ⊙ (solar)
  - Moon: ☽ (lunar)
  - Jupiter: ♃ (jovian)

### 5.2 Inline Formulas

- Avoid inline LaTeX `$...$` when possible.
- Use plain text with Unicode for simple proportional relationships.
- If necessary (e.g. subscripts), limited inline LaTeX is permitted.

### 5.3 Block Equations

- For full equations, use block LaTeX format:  
  `$$...$$`
- Full LaTeX syntax is acceptable inside block equations for proper fraction formatting, subscripts, etc.

### 5.4 Equation Styling Rule Summary

| Context | Preferred Style |
|---------|------------------|
| Inline narrative | Plain text + Unicode |
| Simple numeric comparisons | Plain text |
| Variable subscripts | Inline LaTeX only when necessary |
| Full equations | Block LaTeX (`$$ ... $$`) |

---

# 6 — Export Considerations

- The style system is designed for Markdown-based writing.
- Unicode symbols ensure maximum cross-platform portability.
- Obsidian export engines will properly handle:

  - Footnote numbering
  - Block equations
  - Bold/italic formatting
  - Glossary layout
  - Image inserts
  
- Fonts used for export should support full Unicode symbol rendering for best output (e.g. EB Garamond, Charter, Palatino, etc.).

---

# 7 — Miscellaneous Conventions

### 7.1 Language Rules

- Use _sed ego dico_ for authorial license ("because I say so").
- Use _mundus tuum est_ as guiding creative motto ("it's your world").

### 7.2 Standard Abbreviations

- Avoid ambiguous abbreviations in narrative.
- Always clarify absolute vs relative units when introducing values.

---

# 8 — Summary of "Named Rules"

| Rule Name | Summary |
| --------- | ------- |
| **First-Use Definition Rule** | `***Bold Italic***` on first introduction |
| **Term Mention Rule** | `*Italic*` for subsequent narrative mentions |
| **Sub-Definition Emphasis Rule** | `**Bold**` for sub-definitional qualifiers |
| **Colloquial Emphasis Rule** | `*Italic*` for casual narrative emphasis |
| **Glossary Label Rule** | `**Bold**` for glossary entry labels |
| **Glossary Organization Rule** | Order of introduction locally; alphabetized globally |
| **Footnote Label Rule** | Named labels (`[^IAU]`) only; no numbered references |
| **Footnote Usage Rule** | Source citations only; all definitions remain inline |
| **Equation Formatting Rule** | Unicode inline; LaTeX block for full equations |
| **Persona Insert Frequency Rule** | Limit persona inserts to key learning points |

