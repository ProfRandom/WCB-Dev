# Range Constraints & Random Assignment

## 🧱 Core Constraint Classes

| Type         | Symbol Form     | Meaning                         | Example                     |
|--------------|------------------|----------------------------------|-----------------------------|
| Evaluative   | `x < y`, `x !≈ y`| Truth test                      | Does x satisfy a condition? |
| Comparative  | `ΔT > 0`         | Descriptive comparison          | Not used for enforcement    |
| Prescriptive | `x ≤. y`         | Should (soft rule)              | Preferred but not required  |
| Mandative    | `x .≤ y`         | Must (hard rule)                | Required for validity       |

## ✴️ Modifiers

- `!` — logical negation (`!=`, `!∈`, `!≈`)
- `.` prefix — **mandative** (`.≤`, `.∈`)
- `.` suffix — **prescriptive** (`≤.`, `∈.`)

⚠️ Do not combine `!` with dot-prefixed/suffixed forms. Use the logical inverse instead (e.g., `.>`, `>.`).

---

## 📏 Range Connectives

| Symbol | Meaning                  | Logical Form   | Range Type               |
| ------ | ------------------------ | -------------- | ------------------------ |
| ∧      | Inclusive interior       | a ≤ ▢ ≤ b      | Closed range             |
| ∨      | Exclusive interior       | a < ▢ < b      | Open range               |
| ⩜      | Inclusive exterior       | ▢ ≤ a or ▢ ≥ b | Outside, includes bounds |
| ⩝      | Exclusive exterior       | ▢ < a or ▢ > b | Strictly outside         |
| ⊼      | Left-exclusive interior  | a < ▢ ≤ b      | Half-open                |
| ⩟      | Right-exclusive interior | a ≤ ▢ < b      | Half-open                |
| ⊽      | Left-exclusive exterior  | ▢ < a or ▢ ≥ b | Edge-grazing exterior    |
| ⩡      | Right-exclusive exterior | ▢ ≤ a or ▢ > b | Edge-grazing exterior    |

---

## 🎲 Random Assignment Syntax

### Basic Rule:
Use `⟨⟨ ⟩⟩` to indicate **random value assignment** from a specified range.

| Expression     | Meaning                                              |
| -------------- | ---------------------------------------------------- |
| x = ⟨⟨a ∧ b⟩⟩  | Assign random value from a to b (inclusive)          |
| x .= ⟨⟨a ⩝ b⟩⟩ | Must assign value outside strict range               |
| x = ⟨⟨a ⩟ b⟩⟩  | Assign value in left-inclusive, right-excluded range |

- = → assignment
- .= → mandated assignment (value must be generated)

---

## 🔬 Precision Inference Rule

> The **decimal precision of a randomized result** is inferred from the **most precise** range endpoint.

| Syntax            | Result Precision |
| ----------------- | ---------------- |
| ⟨⟨1.4 ∧ 2.2⟩⟩     | 1 decimal place  |
| ⟨⟨1.40 ∧ 2.2⟩⟩    | 2 decimal places |
| ⟨⟨1.400 ∧ 2.200⟩⟩ | 3 decimal places |

This rule applies **even if the endpoints are excluded** from the valid output range.

---

## ❌ Invalid Forms

| Expression    | Reason                              |
| ------------- | ----------------------------------- |
| x = ⟨⟨1.414⟩⟩ | ❌ Invalid: one-value range          |
| x ∈ !⟨a ∧ b⟩  | ❌ Ambiguous: use `⩜` or `⩝` instead |
| x !.∈ ...     | ❌ Invalid modifier stacking         |

---

## 📜 Axioms

### WBN Axiom 7.1 — The Symbolcrafter’s Creed  
> *“Better to have it and not need it than need it and not have it.”*

All range connectives, including obscure ones like `⩡`, are retained in W101 to ensure semantic closure and support future or edge-case modeling needs.

---

## 🌌 Example Use

markdown
K₁ .∈ ⟨a ⩜ b⟩
 Kirkwood Gap 1 must lie strictly between a and b (excluding both endpoints)

r .= ⟨⟨a ⩝ b⟩⟩
 Assign a randomized orbital radius outside a forbidden band



[[Orbit Randomization ✓]]