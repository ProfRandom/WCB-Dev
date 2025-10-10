# Equation Block Cheat Sheet (Quarto‑Safe Edition)

This reference provides **working, Quarto‑verified equation patterns** tested under **Pandoc 3.6 + LuaLaTeX + MathJax**.  
All examples compile cleanly in both PDF and HTML output.

---

## 1️⃣ Aligned Equations — Multi‑line Math

Use the `aligned` environment inside `$$ … $$` for multi‑line math.  
Do **not** nest `aligned` inside another display block or combine with `equation`.

✅ **Working Example**

```latex
$$
egin{aligned}
E &= mc^2 \[0.5em]
F &= ma \[0.5em]
a &= \dfrac{F}{m}
\end{aligned}
$$
```

🧩 **Why it works**: `aligned` preserves paragraph mode and spacing; Pandoc wraps it safely.  
❌ `{align}` or `{gather}` will trigger *paragraph mode* errors.

---

## 2️⃣ Cases — Piecewise Definitions

Use `cases` for conditional or segmented expressions.

✅ **Working Example**

```latex
$$
f(x) =
egin{cases}
x^2, & x \ge 0 \
-x,  & x < 0
\end{cases}
$$
```

🧩 **Tip**: Always pair `&` before alignment symbols and escape comparisons with Unicode `< >`.

---

## 3️⃣ Arrays — Side‑by‑Side Components

`array` is ideal for tabular math layouts; specify column alignment explicitly.

✅ **Working Example**

```latex
$$
egin{array}{r@{\;}l}
F &= ma \
V &= IR \
E &= mc^2
\end{array}
$$
```

🧩 **Notes**  
- Each column alignment (`r`, `l`, `c`) must match your number of `&` separators.  
- Avoid mixing `{array}` inside `{cases}`.

---

## 4️⃣ Inline Math — Short Expressions

Use single `$ ... $` only for short expressions inside text.  
Never break a paragraph with inline math.

✅ **Examples**
```markdown
The escape velocity is given by $v_e = \sqrt{2GM/r}$.
A planemon with $m = 1$ and $r = 1$ yields $v_e = \sqrt{2G}$.
```

---

## 5️⃣ Comparisons and Symbols

| Symbol | Quarto‑Safe Form | Notes |
|--------|-------------------|-------|
| Less / Greater | `<`, `>` | Use Unicode directly, not `\lt`, `\gt` |
| ≤ / ≥ | `\le`, `\ge` | Standard LaTeX |
| ≠ | `\neq` | Standard LaTeX |
| ≈ / ∼ | `\approx`, `\sim` | Approximation or similarity |
| ≳ / ≲ | `\gtrsim`, `\lesssim` | “Greater/Less or similar” |
| ± / ∓ | `\pm`, `\mp` | Plus‑minus |
| ° | `^\circ` | Use LaTeX command, not Unicode |
| × | `\times` | Avoid the Unicode × |
| ÷ | `\div` | Optional |

---

## 6️⃣ Horizontal Rules and Spacing

✅ **Rules**  
- Use `***` or `___` for horizontal rules.  
- Always include **one blank line before and after**.  

✅ **Example**  
```markdown
Paragraph text.

***

Next paragraph.
```

---

## 7️⃣ Tables

- Always have **one blank line after** a table.  
- Never place math blocks directly under table headers.

✅ **Example**  
```markdown
| Symbol | Meaning |
|---------|----------|
| $m$ | mass |
| $r$ | radius |

Equation follows safely here:
$$
v_e = \sqrt{\dfrac{2GM}{r}}
$$
```

---

## 8️⃣ Nested or Complex Displays

Avoid stacking `$$` or nesting environments.  
Each math display should stand alone.

✅ **Good**
```latex
$$
\begin{aligned}
\nu &= (\phi + 90n) \bmod 360 \\[1em]
n &= 0 \Rightarrow \nu = 0^\circ \text{ (spring equinox)}
\end{aligned}
$$
```

❌ **Bad**
```latex
$$
\begin{aligned}
$$ a = b $$   % nested display — will fail
\end{aligned}
$$
```

---

## 9️⃣ Quick Reference Summary

| Element | Must‑Have Spacing | Safe Form |
|----------|------------------|------------|
| Equation blocks | Blank line before/after | `$$ … $$` |
| Tables | Blank line after | `\|…\|` Markdown tables |
| Horizontal rules | Blank line before & after | `***` or `___` |
| Headers | Blank line before & after | `## Section` |
| Code blocks | Fenced ````` blocks | Never 4‑space indentation |

---

## 🔖 Rule of Thumb

> If it renders in **LuaLaTeX** *and* in **MathJax**, it’s safe in Quarto.  
> If it requires `{align}`, `{gather}`, or inline multi‑line math — rewrite it.

---

*Validated for Quarto 1.8 · Pandoc 3.6 · LuaLaTeX 2025 · TinyTeX v2025.10.*

```bash
git add .
git commit -m "Promote Orbits 3 — Resonances to Canon"
git switch main
git merge draft-dev
quarto render
git tag -a canon_build_v1.1 -m "Second canonical render"
git push --follow-tags
```