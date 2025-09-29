The Euclidean Algorithm provides an elegant and efficient (if somewhat involved) way to compute the greatest common divisor (GCD) of two integers.  This is especially useful for simplifying ratios or finding integer relationships when work with synodic systems

## The Algorithm
The algorithm itself is deceptively short and simple:
1. Start with two integers $a$ and $b$, such that $a>b$.
2. Divide $a$ by $b$, and note the _remainder_, $r$.
	- $r = a\; MOD\; b$
3. Replace $a$ with $b$ and $b$ with $r$.
4. Repeat steps 2 - 3 until $f = 0$.

The last _non-zero remainder_ is the greatest common divisor between $a$ and $b$.

### Example
$$
\begin{gather}
a = 2436 \qquad b = 1172 \\
r = a\;mod\;b = 92 \\[1em]
a = 1172 \qquad b = 92 \\
r = a\;mod\;b = 68 \\[1em]
a = 92 \qquad b = 68 \\
r = a\;mod\;b = 24 \\[1em]
a = 68 \qquad b = 24 \\
r = a\;mod\;b = 20 \\[1em]
a = 24 \qquad b = 20 \\
r = a\;mod\;b = 4\; ✓ \\[1em]
a = 20 \qquad b = 4 \\
⟶ r = a\;mod\;b = 0 \\
\end{gather}
$$
If you don't have a tool that directly calculates modulos, $r$ can manually be calculated by:
$$
r = a - \left( b \times \left\lfloor \dfrac{a}{b} \right\rfloor \right)
$$
Here is an admittedly clunky longhand version for clarity
$$
\begin{array}{r@{}l}
   2 \quad &\text{\scriptsize(Quotient)} \\[-0.2ex]
1172\,)\,\overline{2436}  \quad &\text{\scriptsize(Dividend)} \\[-0.4ex]
\underline{-2344}  \quad &\text{\scriptsize(Subtracted: $2\times1172$)} \\[-0.3ex]
\phantom{ }\,\,92 \quad &\leftarrow \text{\scriptsize(Remainder)}
\end{array}
$$
$$
\begin{array}{r@{}l}
   12 \quad &\text{\scriptsize(Quotient)} \\[-0.2ex]
92\,)\,\overline{1172}  \quad &\text{\scriptsize(Dividend)} \\[-0.4ex]
\underline{-1104}  \quad &\text{\scriptsize(Subtracted: $12\times92$)} \\[-0.3ex]
\phantom{}\,\,68 \quad &\leftarrow \text{\scriptsize(Remainder)}
\end{array}
$$
$$
\begin{array}{r@{}l}
   1 \quad &\text{\scriptsize(Quotient)} \\[-0.2ex]
68\,)\,\overline{92}  \quad &\text{\scriptsize(Dividend)} \\[-0.4ex]
\underline{-68}  \quad &\text{\scriptsize(Subtracted: $1\times68$)} \\[-0.3ex]
\phantom{}\,\,24 \quad &\leftarrow \text{\scriptsize(Remainder)}
\end{array}
$$
$$
\begin{array}{r@{}l}
   2 \quad &\text{\scriptsize(Quotient)} \\[-0.2ex]
24\,)\,\overline{68}  \quad &\text{\scriptsize(Dividend)} \\[-0.4ex]
\underline{-48}  \quad &\text{\scriptsize(Subtracted: $2\times24$)} \\[-0.3ex]
\phantom{}\,\,20 \quad &\leftarrow \text{\scriptsize(Remainder)}
\end{array}
$$
$$
\begin{array}{r@{}l}
   1 \quad &\text{\scriptsize(Quotient)} \\[-0.2ex]
20\,)\,\overline{24}  \quad &\text{\scriptsize(Dividend)} \\[-0.4ex]
\underline{-20}  \quad &\text{\scriptsize(Subtracted: $1\times20$)} \\[-0.3ex]
\phantom{}\,\,\mathbf{4} \; \boldsymbol{\checkmark} &\leftarrow \text{\scriptsize(Remainder)}
\end{array}
$$
$$
\begin{array}{r@{}l}
   5 \quad &\text{\scriptsize(Quotient)} \\[-0.2ex]
4\,)\,\overline{20}  \quad &\text{\scriptsize(Dividend)} \\[-0.4ex]
\underline{-20}  \quad &\text{\scriptsize(Subtracted: $5\times4$)} \\[-0.3ex]
\phantom{}\,\,0 \quad &\leftarrow \text{\scriptsize(Remainder)}
\end{array}
$$
$$
\text{Since this remainder is } 0 \text{, the previous remainder is the GCD}
$$
$$
\begin{array}{c c c}
\therefore \; \gcd(2436,1172) = 4 
\end{array}
$$

