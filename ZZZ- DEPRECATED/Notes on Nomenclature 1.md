---
layout: default
title: "Page Title Goes Here"
---


# 🔢 Numerical Precision and Rounding Conventions

Unless otherwise noted, decimal values in _Worldcrafting 101_ are expressed to **three decimal places**, including trailing zeros (e.g., ⟨1.000 ∧ 0.500⟩. This standard ensures clarity and consistency across all parameter outputs and computational examples.

In some cases, a **fourth decimal place** is included — **not** to imply increased precision, but to clarify the **rounding direction** of the third decimal digit:

- `0.5445` indicates that the third-place digit (`4`) would round **up** to `0.545`, making the standard value a **slight overstatement**.
    
- `0.5454` shows that rounding to `0.545` is a **safe approximation**, as the third-place digit has **not been rounded up**.
# Range Notation
In _Worldcrafting 101_, **continuous value ranges** are expressed using **angle brackets** `⟨ ⟩` and an ellipsis `∧` to indicate **inclusive lower and upper bounds**. This avoids formatting conflicts with Markdown, LaTeX, and HTML, while conveying intuitive mathematical intent.  For example:
$$ \langle a\,\ldots b\rangle$$
### ✴️ Meaning:

- The range includes both endpoints.    
- Equivalent to: `a ≤ x ≤ b`    
- Read as: “from _a_ to _b_, inclusive”

### ✴️ Examples:

- `atm ∈ ⟨0.5 ∧ 2.0⟩` — Valid atmospheric pressures for a Geotic world    
- `T ∈ ⟨260 ∧ 320⟩ K` — Plausible surface temperatures for life-supporting planemos    
- `O₂ ∈ ⟨15% ∧ 30%⟩` — Breathing oxygen range for humanlike life

| Symbol  | Logical Form   | Meaning                         |
|---------|----------------|---------------------------------|
| ⟨a ∧ b⟩ | a ≤ ▢ ≤ b      | Inclusive interior              |
| ⟨a ⩜ b⟩ | a < ▢ < b      | Exclusive interior              |
| ⟨a ⊼ b⟩ | a < ▢ ≤ b      | Left-exclusive, right-inclusive |
| ⟨a ⩟ b⟩ | a ≤ ▢ < b      | Left-inclusive, right-exclusive |
| ⟨a ∨ b⟩ | ▢ ≤ a or ▢ ≥ b | Inclusive forbidden interior    |
| ⟨a ⩝ b⟩ | ▢ < a or ▢ > b | Strictly forbidden interior     |
| ⟨a ⩡ b⟩ | ▢ < a or ▢ ≥ b | Strict left, inclusive right    |
| ⟨a ⊽ b⟩ | ▢ ≤ a or ▢ > b | Inclusive left, strict right    |

∧ ambi-inclusive interior
∨ ambi-exclusive interior
⩜ ambi-inclusive exterior
⩝ ambi-exclusive exterior
⊼ left-exclusive interior _or_ right-inclusive interior
⩟ right-exclusive interior _or_ left-inclusive interior
⊽ left-exclusive exterior _or_ right-inclusive exterior
⩡ right-exclusive exterior _or_ left-inclusive exterior

| Symbol | Name                     | Interior Logic     | Edge Inclusion             | Description                                |
|--------|--------------------------|--------------------|----------------------------|--------------------------------------------|
| ∧      | Ambi-inclusive interior  | ✅ interior valid   | ✅ includes both a and b    | Classic bounded interval (a ≤ ▢ ≤ b)       |
| ∨      | Ambi-exclusive interior  | ✅ interior valid   | ❌ excludes both endpoints  | Pure open interval (a < ▢ < b)             |
| ⩜      | Ambi-inclusive exterior  | ❌ interior invalid | ✅ includes both a and b    | Valid values are ≤ a or ≥ b                |
| ⩝      | Ambi-exclusive exterior  | ❌ interior invalid | ❌ excludes a and b         | Valid only outside bounds (▢ < a or ▢ > b) |
| ⊼      | Left-exclusive interior  | ✅ interior valid   | ❌ excludes a, ✅ includes b | a < ▢ ≤ b (or symmetrical variant)         |
| ⩟      | Right-exclusive interior | ✅ interior valid   | ✅ includes a, ❌ excludes b | a ≤ ▢ < b (or symmetrical variant)         |
| ⊽      | Left-exclusive exterior  | ❌ interior invalid | ❌ excludes a, ✅ includes b | Valid if ▢ < a or ▢ ≥ b                    |
| ⩡      | Right-exclusive exterior | ❌ interior invalid | ✅ includes a, ❌ excludes b | Valid if ▢ ≤ a or ▢ > b                    |
### ✅ On Using `∈` vs `∉` in Range Membership

- Use **`x ∈ ⟨a 𝛼 b⟩`** to describe **valid zones** or **expected conditions**.
- Use **`x ∉ ⟨a 𝛼 b⟩`** when expressing a **rule**, **error state**, or **prohibition**.

This ensures consistent language across W101:
- `x ∈ ⟨a ⩜ b⟩` — x is valid strictly between a and b
- `x ∉ ⟨a ∧ b⟩` — x *must not* fall inside the inclusive interior

Default to `∈` when teaching, explaining, or labeling.  
Reserve `∉` when declaring imperatives or forbidden regions.

