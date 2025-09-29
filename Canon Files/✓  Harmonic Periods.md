## Abstract
**Major Topics:**  
- Harmonic period as a synchronization interval of two cycles.  
- Equivalence to the synodic period formula.  
- Application to Earth’s solar day vs. sidereal day (≈ tropical year).  
- Application to Earth’s solar day vs. stellar day (≈ sidereal year).  

**Key Terms & Symbols:**  
- H = harmonic period  
- P₁ = solar day  
- P₂ = sidereal day / stellar day  
- Synodic period (noted as mathematically identical).  

**Cross-Check Notes:**  
- Bridges the concepts of daily cycles and year-length periods.  
- Explicitly links harmonic period to *tropical* and *sidereal year* definitions.  
- Potential overlaps with glossary entries on *solar day*, *sidereal day*, *stellar day*, and *synodic period*.  
- Candidate staging milestone: Glossary v1.215 (Harmonic Period added).  

---
---



_Harmonic periods_ are crucial for understanding how a planet's rotational and orbital cycles synchronize.  The harmonic period $H$ is the time interval over which the two independent motions align in their periodicity.
$$
H = \dfrac{P_1 \times P_2}{|P_1 - P_2|}
$$
Where:
- $P_1$ = length of the solar day
- $P_2$ = length of the sidereal day
- $H$ = harmonic period

> Yes, this is actually the same equation as the synodic period.

## Example
Using Earth's solar day and sidereal day:
$$
\begin{array}{l l}
P_1 = 86400^s &\text{solar day}\\
P_2 = 86164.090531^s &\text{sidereal day}
\end{array}
$$
$$
\begin{equation}
\begin{split}
H &= \dfrac{P_1 \times P_2}{|P_1 - P_2|} \\[0.5em]
&= \dfrac{86400 \times 86164.090531}{|86400 - 86164.090531|} \\[0.5em]
&= \dfrac{7444577422}{235.9094692} \\[0.5em]
H &= 31556924.9854376^s\; \checkmark
\end{split}
\end{equation}
$$
… we find that the harmonic period between the solar day and the sidereal day is approximately the length of the _tropical year_, differing from the official value of $31556925.216^s$ by an excess of only $0.2306^s$.

Similarly, calculating the harmonic period between Earth's solar day and the _stellar day_:

$$
\begin{array}{l l}
P_1 = 86400^s &\text{solar day}\\
P_2 = 86164.0989^s &\text{stellar day}
\end{array}
$$
$$
\begin{equation}
\begin{split}
H &= \dfrac{P_1 \times P_2}{|P_1 - P_2|} \\[0.5em]
&= \dfrac{86400 \times 86164.0989}{|86400 - 86164.0989|} \\[0.5em]
&= \dfrac{7444578145}{235.901096} \\[0.5em]
H &= 31558048.1047344^s\; \checkmark
\end{split}
\end{equation}
$$
… a difference of only $101.65737^s$ longer than the official length of the _sidereal year_: $31558149.7635456^s$.

