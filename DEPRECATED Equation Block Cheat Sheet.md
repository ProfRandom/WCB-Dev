# LaTeX Equation Environments — Quick Reference

This note collects the most useful LaTeX math environments that also render in Markdown (Obsidian, Jupyter, etc.).

---
### 📌 General Notes
- In **Markdown/MathJax** → always wrap blocks in `$$ ... $$` (equation numbering is off by default).    
- In **LaTeX proper** → no `$$`; environments provide numbering.    
-  **Best practice:** Always use full LaTeX syntax (`equation`, `align`, etc.). Works in Markdown, and keeps your notes copy–pasteable into `.tex` without edits.

---
### Single equation
```latex
\begin{equation}
E = m c^2
\end{equation}
```
or
```
$$
E = m c^2
$$
```
$$
\begin{equation}
E = m c^2
\end{equation}
$$
### Align multiple equations (each gets a number in LaTeX)
```latex
\begin{align}
F &= ma \\
E &= mc^2
\end{align}
```
$$
\begin{align}
F &= ma \\
E &= mc^2
\end{align}
$$
- Use for _separate equations_.    
- Don’t use for multi-step derivations (that’s `split`).
- ❗️Numbers _every line_ (suppress with `\notag`)
### Gather (multi-line, no alignment points)
```latex
\begin{gather}
x^2 + y^2 = r^2 \\
y = mx + b
\end{gather}
```
$$
\begin{gather}
x^2 + y^2 = r^2 \\
y = mx + b
\end{gather}
$$
- Use when you want _stacked equations_ without alignment.
- ❗️Numbers _every line_ (suppress with `\notag`)
### Multline (long equation, automatic alignment)
```latex
\begin{multline}
a + b + c + d + e + f + g + h \\
+ i + j + k + l + m + n \\
+ o + p + q + r + s + t + u \\
+ v + w + x + y + z
\end{multline}
```
$$
\begin{multline}
a + b + c + d + e + f + g + h \\
+ i + j + k + l + m + n \\
+ o + p + q + r + s + t + u \\
+ v + w + x + y + z
\end{multline}
$$
-Use for _one long equation_ too wide for a line.    
- First line = left, last line = right, middle = centered.
- ❗️One number for the whole block.   
### Split (one equation, multiple aligned steps)
```latex
\begin{equation}
\begin{split}
f(x) &= a + b + c + d \\
     &= e + f + g + h
\end{split}
\end{equation}
```
$$
\begin{equation}
\begin{split}
f(x) &= a + b + c + d \\
     &= e + f + g + h
\end{split}
\end{equation}
$$
- Use for _step-by-step derivation of one equation_.    
- Cannot beUsed by itself — must be inside `equation` (or `equation*`).
- ❗️One number for _all lines_ (requires `equation`). 
### Aligned (block of related formulas)
```latex
\begin{aligned}
\Sigma &= \frac{P_\alpha P_\beta}{|P_\alpha - P_\beta|}
& P_\alpha &= \frac{\Sigma P_\beta}{\Sigma - P_\beta}
& P_\beta &= \frac{\Sigma P_\alpha}{\Sigma + P_\alpha}
\end{aligned}
```
$$
\begin{aligned}
\Sigma &= \frac{P_\alpha P_\beta}{|P_\alpha - P_\beta|}
& P_\alpha &= \frac{\Sigma P_\beta}{\Sigma - P_\beta}
& P_\beta &= \frac{\Sigma P_\alpha}{\Sigma + P_\alpha}
\end{aligned}
$$
- Use for _parallel formulas_ or _compact blocks_.    
- ❗️Doesn’t number by itself; wrap in `equation` if you need a number.
### Array (tabular math layout)
```latex
\begin{array}{rcl}
Q &= \dfrac{P_\beta}{P_\alpha} 
&&&P_\alpha = P_\beta \times R = \dfrac{P_\beta}{Q} 
= \left(\dfrac{\Sigma}{Q} - \Sigma\right) = \Sigma(R - 1) \\[1em]
R &= \dfrac{P_\alpha}{P_\beta} 
&&&P_\beta = P_\alpha \times Q = \dfrac{P_\alpha}{R}
= \left(\Sigma - \dfrac{\Sigma}{R}\right) = \Sigma(1-Q)
\end{array}
```
$$
\begin{array}{rcl}
Q &= \dfrac{P_\beta}{P_\alpha} 
&&&P_\alpha = P_\beta \times R = \dfrac{P_\beta}{Q} 
= \left(\dfrac{\Sigma}{Q} - \Sigma\right) = \Sigma(R - 1) \\[1em]
R &= \dfrac{P_\alpha}{P_\beta} 
&&&P_\beta = P_\alpha \times Q = \dfrac{P_\alpha}{R}
= \left(\Sigma - \dfrac{\Sigma}{R}\right) = \Sigma(1-Q)
\end{array}
$$
- Use when equations naturally form a _grid_ or when you want long forms to sit side-by-side.    
- More typing (`{rcl}` specifiers), but very clean for “two-column math tables.”
- ❗️Doesn’t number by itself; wrap in `equation` if you need a number.
### Piecewise / Cases
```latex
f(x) =
\begin{cases}
  x^2 & x \geq 0 \\
  -x  & x < 0
\end{cases}
```
$$
f(x) =
\begin{cases}
  x^2 & x \geq 0 \\
  -x  & x < 0
\end{cases}
$$
- Use for _piecewise functions_.
- ❗️Doesn’t number by itself; wrap in `equation` if you need a number.
### Matrix-like environments
#### matrix
```latex
\begin{matrix}
a & b \\ c & d
\end{matrix}
```
$$
\begin{matrix}
a & b \\ c & d
\end{matrix}
$$
#### pmatrix
```latex
\begin{pmatrix}
a & b \\ c & d
\end{pmatrix}
```
$$
\begin{pmatrix}
a & b \\ c & d
\end{pmatrix}
$$
#### bmatrix
```latex
\begin{bmatrix}
a & b \\ c & d
\end{bmatrix}
```
$$
\begin{bmatrix}
a & b \\ c & d
\end{bmatrix}
$$
#### Bmatrix
```latex
\begin{Bmatrix}
a & b \\ c & d
\end{Bmatrix}
```
$$
\begin{Bmatrix}
a & b \\ c & d
\end{Bmatrix}
$$
#### vmatrix
```latex
\begin{vmatrix}
a & b \\ c & d
\end{vmatrix}
```
$$
\begin{vmatrix}
a & b \\ c & d
\end{vmatrix}
$$
#### Vmatrix
```latex
\begin{Vmatrix}
a & b \\ c & d
\end{Vmatrix}
```
$$
\begin{Vmatrix}
a & b \\ c & d
\end{Vmatrix}
$$
- Use for matrices, vectors, or “bracketed structures.”
- ❗️Don’t number by themselves; wrap in `equation` if you need a number.
### Array for data-style tables
```latex
\begin{array}{l c}
\text{Synodion} & 22.587\ \text{days} \\
\text{Epochal Aggregate} & 7137.48\ \text{days}
\end{array}
```
$$
\begin{array}{l c}
\text{Synodion} & 22.587\ \text{days} \\
\text{Epochal Aggregate} & 7137.48\ \text{days}
\end{array}
$$
- Use for mixing math + text in tabular form.
- ❗️Doesn’t number by itself; wrap in `equation` if you need a number.
### Phantom Spacing
#### \phantom{} (both width and height)
```latex
$$
\begin{aligned}
1.23\phantom{0}\\
12.3\phantom{00}\\
123.\phantom{000}
\end{aligned}
$$
```
$$
\begin{aligned}
1.23\phantom{0}\\
12.3\phantom{00}\\
123.\phantom{000}
\end{aligned}
$$
```latex
$$
\begin{aligned}
F &= ma \\[-0.25em]
\phantom{F} &= m\,\frac{dv}{dt}
\end{aligned}
$$
```
$$
\begin{aligned}
F &= ma \\[-0.25em]
\phantom{F} &= m\,\frac{dv}{dt}
\end{aligned}
$$
#### \hphantom{} (width only)
```latex
$$
\begin{aligned}
+3.42\\
\hphantom{+}2.15\\
-1.08
\end{aligned}
$$
```
$$
\begin{aligned}
+3.42\\
\hphantom{+}2.15\\
-1.08
\end{aligned}
$$

#### \vphantom{} {height only}
```latex
$$
\left(
\begin{array}{c}
x \\[1em]
y_{\vphantom{T}} \\[1em]
z_T
\end{array}
\right)
$$
```
$$
\left(
\begin{array}{c}
x \\[1em]
y_{\vphantom{T}} \\[1em]
z_T
\end{array}
\right)
$$

# 📌 Cheat Summary — When to Use Which

| Environment   | Best for                     | Numbering        |
|---------------|-------------------------------|------------------|
| `equation`    | One equation                  | 1 per block      |
| `align`       | Many equations                | 1 per line       |
| `split`       | One equation, many steps      | 1 for whole block|
| `aligned`     | Parallel formulas in a block  | Inherits parent  |
| `multline`    | Very long equation            | 1 per block      |
| `array`       | Math tables, grids            | Inherits parent  |
| `cases`       | Piecewise definitions         | Inherits parent  |
| `matrix` etc. | Matrices / bracketed layouts  | Inherits parent  |
