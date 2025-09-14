# Asteroid Belt Placement and Extents

## Placing The Belt and Identifying Its Dimensions

$$
\begin{align}
a_i &= &&\text{Inner orbit distance} \\
a_o &= &&\text{Outer orbit distance} \\[0.5em]
m_i &= &&\text{Mass of inner body in Terrans} \\
m_o &= &&\text{Mass of outer body in Terrans} \\[0.5em]
M_* & = 333000M⊙ \qquad &&\text{Mass of star in Terrans} \\[0.5em]
a_c &= \frac{a_i + a_o}{2} \qquad &&\text{Average of the two orbits} \\[0.5em]
\Delta a &= a_o - a_i \qquad &&\text{Difference between the two orbits} \\[0.5em]
a_\Delta &= \frac{\Delta a}{2} \qquad &&\text{Midrange of the two orbits} \\[0.5em] 
a_s &= a_c + a_\Delta \left(\frac{m_o - m_i}{m_o + m_i}\right) \qquad &&\text{Asymmetric central orbit} \\[0.5em]
m_\mu &= \frac{m_i + m_o}{M_*} \qquad &&\text{Dimensionless systemic mass ratio} \\[0.5em]
\beta &= 1 - (C \times \sqrt[3]{m_\mu}) \qquad &&\text{Where C} \in \{1, 2, 3\} \\
&&&\text{Belt width scaler} \\[0.5em]
W_{belt} &= \Delta a \times \beta \qquad &&\text{Belt width calculation}\\[0.5em]
w_i &= \frac{m_i}{m_i + m_o} \qquad w_o = \frac{m_o}{m_i + m_o} \quad &&\text{Belt inner and outer edge adjustments} \\[0.5em]
W_i &= W_{belt} \times w_i \qquad W_o = W_{belt} \times w_o \quad && \text{Belt inner and outer edge offset calculations}\\[0.5em]
B_i &= a_s - W_i \qquad B_o = a_s + W_o \qquad &&\text{Belt inner and outer edge calculations}
\end{align}
$$

## Calculating Resonant Orbits  
### Vocabulary Notes
- Perturber: An orbiting object acting to perturb the orbit of other, less massive nearby objects.
- Perturbant: The body exerting perturbing influence.
- Resonant: Any of the resonances that result from the influence of the perturbant.
- Tresonance: A resonance tending to trap orbiting bodies within a narrow orbital region.
- Gresonance: A resonance tending to exclude orbiting bodies from a narrow orbital region.

When mapping resonant gap orbits, use the bracketing orbits as **perturbers**. For each perturber, resonances can be found by scaling the orbital period with small integer ratios and converting back to distance with Kepler’s Third Law ($P^2 \propto a^3$).

1. When both perturbers have equal mass ($m_i = m_o$) calculate resonance orbits only from the mass and orbital distance of the outer perturber.
2. When the perturbers have differenting masses:
	- If their mass ratio ≤ 10:1, calculate resonance orbits for both inner and outer perturbers and pairwise-average them.
	- If their mass ratio > 10:1, calculate resonance orbits using only the mass and orbital distance of the more massive perturber (regardless of location).
### Inner Orbit Resonances
Using the **inner perturber** with period $P_i$.  
$$
P_x = P_i \times k \quad \text{Where: } k \in \{1.67, 2.00, 2.25, 2.33, 2.50, 2.67, 3.00, 3.50, 4.00, 5.00\}
$$$$
a_x = \sqrt[3]{P_x^2 \, M\odot}
$$ 
Where:
- $P_x$ = resonant period  
- $a_x$ = resonant distance (AU)  
- $M\odot$ = stellar mass (in solar units)  
- $k$ = resonance scaler (see below for details)  

Keep only values where $a_x > B_i$ (beyond the inner orbit).  
### Outer Orbit Resonances
Using from the **outer perturber** with period $P_o$.  
$$
P_x = \frac{P_o}{k} \quad \text{Where: } k \in \{1.67, 2.00, 2.25, 2.33, 2.50, 2.67, 3.00, 3.50, 4.00, 5.00\}
$$$$
a_x = \sqrt[3]{P_x^2 \, M\odot}
$$Where:
- $P_x$ = resonant period  
- $a_x$ = resonant distance (AU)  
- $M\odot$ = stellar mass (in solar units)  
- $k$ = resonance scaler  

Keep only values where $a_x < B_o$ (inside the outer orbit).  
#### Combined Equation Forms:

##### Inner Orbit Resonances
$$
a_x = \sqrt[3]{\Big((P_i \times k)^2 \, M\odot\Big)}
$$
##### Outer Orbit Resonances
$$
a_x = \sqrt[3]{\left(\frac{P_o}{k}\right)^2 M\odot}
$$
### Details: Resonance Scalers
*Sorted in order of frequency*
#### Gap Resonances (Gresonances)

|  Notes   | Perturbant | Resonant |  Ratio  | Order | Frequency<br>$\tfrac{\text{Perturbant}}{\text{Resonant}}$ |
| :------: | :--------: | :------: | :-----: | :---: | :-------------------------------------------------------: |
|    4     |     5      |    3     |   5:3   |   2   |                           1.67                            |
| **3, 4** |   **2**    |  **1**   | **2:1** | **1** |                         **2.00**                          |
|          |     9      |    4     |   9:4   |   5   |                           2.25                            |
|    4     |     7      |    3     |   7:3   |   4   |                           2.33                            |
|    4     |     5      |    2     |   5:2   |   3   |                           2.50                            |
|          |     8      |    3     |   8:3   |   5   |                           2.67                            |
|    4     |     3      |    1     |   3:1   |   2   |                           3.00                            |
|          |     7      |    2     |   7:2   |   5   |                           3.50                            |
|    4     |     4      |    1     |   4:1   |   3   |                           4.00                            |
|          |     5      |    1     |   5:1   |   4   |                           5.00                            |
#### Trap Resonances (Tresonances)

| Notes | Perturbant | Resonant | Ratio | Order | Frequency<br>$\tfrac{\text{Perturbant}}{\text{Resonant}}$ |
| :---: | :--------: | :------: | :---: | :---: | :-------------------------------------------------------: |
|   4   | 4          | 3        | 4:3   | 1     |                           1.33                            |
|   4   | 3          | 2        | 3:2   | 1     |                           1.50                            |
|       | 5          | 4        | 5:4   | 1     |                           1.25                            |
|       | 6          | 5        | 6:5   | 1     |                           1.20                            |
|       | 7          | 6        | 7:6   | 1     |                           1.17                            |

> **Notes:**
> 1. The higher the resonant order, the weaker the resonance.
> 2. It is worth noting that all gap resonances have frequencies > 1.50 and all trap resonances have frequencies ≤ 1.50.
> 3. Resonance 2:1 is the only first-order gap resonance, though it can, under certain circumstances, behave as a trap resonance.
> 4. These resonance ratios are all observed in the Solar System asteroid belt, though the framework is generalizable to other systems.

>**Usage:**
>Preferentially choose resonance ratios with order 1 or 2 whenever possible: resonances of order 1 or 2 will have the strongest dynamical signatures (clear gaps or stable traps). Higher orders may be used sparingly to add fine structure, but their effects will be much weaker.

# Width of Gaps
For a resonance gap in an asteroid belt to be significant, it should be ≥ 0.1% of the orbital radius of the gap, itself.
$$
\frac{g}{a}≥10^{-3}
$$


$$
g = a \times \sqrt{\frac{M_{p⨁}}{333000M⊙}}
$$
Thus, given
- $M_p$ = the mass of the planet
- $M_*$ = the mass of the star (in the same units as $M_p$)
$$
\begin{gather}
\sqrt{\frac{M_p}{M_*}} \geq 10^{-3} \quad → \quad \frac{M_p}{M_*} \geq 10^{-6}  \\ \therefore M_p \geq M_* \times 10^{-6} = \frac{M_*}{10^6}
\end{gather}
$$
##### Example:
Given: $M_* = 333000 M_⨁$ (for the Sun):
$$
M_p \geq \frac{333000}{10^6} = 0.333 M_⨁
$$
**Meaning:**
- A body must be **at least 0.333 Earth masses** (~⅓⨁) to carve a **recognizable Kirkwood gap** in a main-belt analogue.
- **Below this** (midimos, small planemos), the “gap width” is so narrow it doesn’t register as a true Kirkwood void.
## Calculating Gap Widths
For each resonant orbit calculated above, calculate a gap width by:
$$
g_w = a \times \sqrt{\frac{m_i + m_o}{333000M⊙}} \qquad \text{Preferred method}
$$
or
$$
\begin{gather}
g_{quad} = \sqrt{g_i^2 + g_o^2} \qquad \text{Requires calculating $g_i$ and $g_o$ first by:} \\[1em]
g_i = a \times \sqrt{\frac{m_i}{333000M⊙}} \quad\text{and}\quad g_o = a \times \sqrt{\frac{m_o}{333000M⊙}}
\end{gather}
$$
Both methods are algebraically equivalent: the $g_{quad}$ form expands ***exactly*** into the $g_w$ expression above.
