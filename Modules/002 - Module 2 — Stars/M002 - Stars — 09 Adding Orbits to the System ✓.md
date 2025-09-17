# Fleshing Out A Star System

We've established spectral classes and types, thermozones, ontozones, habitability indices, and the two critical orbital distances, *nucleal* ($\mathcal{N}$) and *perannual* ($\mathcal{P}$).

But planemos don't orbit only at these discreet distances  – they're all over the place.  Here's a breakdown of our own Solar system's planemo orbit data:

| <center>planemo</center> | <center>α<br>(AU)</center> | <center>ϵ</center> | Ontozone    |
| ----------------------- | -------------------------: | ------------------ | ----------- |
| Mercury                 |                      0.387 | 0.2056             | Igniozone   |
| Venus                   |                      0.723 | 0.0068             | Calorozone  |
| Earth                   |                      1.000 | 0.0167             | Solarazone  |
| Mars                    |                      1.524 | 0.0934             | Hiberozone  |
| *Asteroids*             |     *⟨2.2 ∧ 3.2⟩; μ = 2.7* | *μ = 0.15*         | *Brumazone* |
| Jupiter                 |                      5.204 | 0.0489             | Cryozone    |
| Saturn                  |                      9.583 | 0.0565             | Cryozone    |
| Uranus                  |                     19.191 | 0.0472             | Cryozone    |
| Neptune                 |                     30.070 | 0.0087             | Cryozone    |
## Orbital Parameters
Ignoring the asteroid belt for the moment and inserting Ceres as the largest member of the belt:

| <center>planemo</center> | <center>α<br>(AU)</center> | <center>ϵ</center> | <center>Gap¹<br>(AU)</center> | <center>Interval²<br>(AU)</center> |
| ----------------------- | -------------------------: | -----------------: | ----------------------------: | ---------------------------------: |
| Mercury                 |                      0.387 |             0.2056 |                               |                                    |
| Venus                   |                      0.723 |             0.0067 |                        0.3362 |                             1.8686 |
| Earth                   |                      1.000 |             0.0167 |                        0.2767 |                             1.3825 |
| Mars                    |                      1.524 |             0.0934 |                        0.5237 |                             1.5237 |
| Ceres                   |                      2.700 |             0.1500 |                        0.1763 |                             1.7720 |
| Jupiter                 |                      5.204 |             0.0489 |                        2.5038 |                             1.9273 |
| Saturn                  |                      9.583 |             0.0565 |                        4.3788 |                             1.8415 |
| Uranus                  |                     19.191 |            0.04727 |                        9.6087 |                             2.0027 |
| Neptune                 |                     30.070 |             0.0088 |                       10.8787 |                             1.5669 |
>Notes:
>1. The orbital **gap** is calculated by subtracting the planemo's orbital distance from the next closer-in planemo's orbital distance
>   $$G = O_n - O_{n-1}$$>2. The orbital **interval** is calculated by dividing the planemo's orbital distance by the next closer-in planemo's orbital distance:
>   $$I = \dfrac{O_n}{O_{n-1}}$$

What we are concerned with is the *orbital intervals*
- The minimum interval is between Venus and Earth: $I = 1.3825\;AU$
- The maximum interval is between Uranus and Neptune: $I = 2.0027\;AU$
- The average interval is $I \approx 1.74\;AU$
- The median interval is $I \approx 1.81\;AU$
- The standard deviation is $\sigma = 0.2051$

This supports defining a **WCB-conservative orbital interval range** of  ⟨1.400  ∧  2.000⟩  AU by rounding up the minimum and rounding down the maximum.

However, a cursory survey of the Exoplanet Catalog seems to reveal a range of ⟨1.000 ∧ 5.000⟩ AU for planetary orbital intervals.  We'll define this as our optimistic orbital interval range, and, for completeness, average the two ranges at ⟨1.200 ∧ 3.500⟩ AU.

**Orbital interval ranges**

| Inner | Outer | Description  |
| ----: | ----: | ------------ |
|   1.4 |     2 | Conservative |
|   1.2 |   3.5 | Medial       |
|     1 |     5 | Optimistic   |
## Calculating Other Orbits
This brings us to methods of calculating other orbits in a star system.  In practice, any method the worldmakerchooses is _valid_, including just putting planemos where "it feels right"; however, even using this method _should_ ideally take into account the above statistics and try to avoid an orbital interval between a given planemo and its nearest neighbor of $< 1.500\;AU$ or $> 2.000\;AU$.

### Starting From A Known Orbit
Most of the time, you'll have pre-established a particular orbit  — usually either the *nucleal* or the *perannual* orbit, and want to arrange other planemos in the system relative to that orbit. Notating this orbit as the **base** orbit, we can set up two processes for calculating orbits inferior to (closer-in than) and superior to (farther-out than) that orbit.

**Intrabasal Orbit Calculation Process**
$$
r_i = B;\; \Omega = \text{«▢»}: \qquad
r_{i-1} = \frac{r_i}{⟨⟨ \text{min} ∧ \text{max} ⟩⟩}
\quad \text{while } r_{i-1} \geq \Omega
$$
**Extrabasal Orbit Calculation Process**
$$
r_i = B;\; \Omega = \text{«▢»}: \qquad
r_{i+1} = r_i \cdot ⟨⟨ \text{min} ∧ \text{max} ⟩⟩
\quad \text{while } r_{i+1} \leq \Omega
$$
Where:
- *B* = basal orbital radius (e.g. the nucleal orbit $\mathcal{N}$)
- *Ω* = orbital distance cuttoff (minimum or maximum allowed orbit based on the star system constraints)

### Usage Strategy
*Assuming the medial orbital interval range* $I \in ⟨⟨1.200 ∧ 3.500⟩⟩\;AU$:
The **intrabasal** and **extrabasal** forms can be used independently depending on your desired anchoring strategy:

> **Inward-Only Generation**  
  If you begin at the **basal orbit** (innermost, nucleal, perannual, etc.), use the **intrabasal** form to expand inward via divisive steps:
$$
  r_0 = B;\; \Omega = «▢»:
  \quad r_{i-1} = \dfrac{r_i} {⟨⟨1.200 ∧ 3.500⟩⟩}, \text{ while } r_{i-1} \geq \Omega
$$
Where:
- *Ω* = the minimum safe orbital distance  —  usually taken to be $a = 0.100\;AU$.

> **Outward-Only Generation**  
  If you begin at an **innermost orbit** (e.g. a thermal, Roche, or design constraint), use the **intrabasal** form to expand outward via multiplicative steps:
$$
  r_0 = B;\; \Omega = «▢»:
  \quad r_{i+1} = r_i \cdot ⟨⟨1.200 ∧ 3.500⟩⟩, \text{ while } r_{i+1} \leq \Omega
$$
Where:
- *Ω* = the farthest orbit desired for a planemo in the system — based on whatever criterion desired, but physically limited to the Hill Sphere radius of the central mass.

> Applying these methods can fully define a system.
> - If one wanted to start with the innermost safe orbit; e.g. $B = 0.100\;AU$, then one would use only the extrabasal process to calculate orbits outward.
> - Conversely if one wanted to start with the most distant orbit, then one would use only the intrabasal process to calculate orbits inward.

>> **IMPORTANT**
>> *If not starting from the perannual or nucleal orbit, always check randomized orbits against either (or both) to ensure proper interval gaps fall to either side of that orbit, and adjust accordingly!*

## Worked Example
Let us say we've identified our nucleal orbit (N) as $N = 0.834\;AU$, and we want to calculate orbits interior-to and exterior-to that orbit, and we've chosen $a = 0.100\;AU$ as our innermost safe orbit.
### Working Inward
$$
  r_0 = 0.834;\; \Omega = 0.100:
  \quad r_{i-1} = \dfrac{r_i} {⟨⟨1.200 ∧ 3.500⟩⟩}, \text{ while } r_{i-1} \geq 0.100
$$
$$
\begin{align}
r_{i-1} &= \dfrac{0.834} {1.723} = 0.482\;AU \qquad 1.732 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i-1} &= \dfrac{0.482} {1.616} = 0.298\;AU \qquad 1.616 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i-1} &= \dfrac{0.298} {1.573} = 0.190\;AU \qquad 1.573 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i-1} &= \dfrac{0.190} {1.884} = 0.101\;AU \qquad 1.884 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i-1} &= \dfrac{0.101} {1.963} = 0.051\;AU \qquad 1.963 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU}\;✘ \\[1em]
\end{align}
$$
We stop at the fourth randomized orbit, because the next orbit randomly generated fails the $r ≥ 0.100\;AU$ test.
We now have a system of five orbits:

|  Orbit  | Distance |
| :-----: | :------: |
|    1    | 0.101    |
|    2    | 0.190    |
|    3    | 0.298    |
|    4    | 0.482    |
| 5 (*N*) | 0.834    |
We could stop here and have a fully legitimate star system, but let's say we want extranucleal orbits, as well.  Again, beginning with the nucleal orbit $B = 0.834\;AU$, and setting an outermost orbit of $\Omega = 35.0\;AU$:
$$
  r_0 = 0.834;\; \Omega = 35.0:
  \quad r_{i+1} = r_i \cdot ⟨⟨1.200 ∧ 3.500⟩⟩, \text{ while } r_{i+1} \leq 35.0
$$
$$
\begin{align}
r_{i+1} &= 0.834(1.829) = 1.525\;AU \qquad 1.829 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i+1} &= 1.525(1.969) = 3.003\;AU \qquad 1.969 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i+1} &= 3.003(1.578) = 4.739\;AU \qquad 1.578 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i+1} &= 4.739(1.547) = 7.332\;AU \qquad 1.547 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i+1} &= 7.332(1.552) = 11.379\;AU \qquad 1.552 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i+1} &= 11.379(1.608) = 18.298\;AU \qquad 1.608 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i+1} &= 18.298(1.823) = 33.357\;AU \qquad 1.823 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i+1} &= 33.357(1.778) = 59.309\;AU \qquad 1.778 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \; ✘ \\[1em]
\end{align}
$$
We stop at the seventh iteration, as the next value exceeds $\Omega = 35.0\;AU$.

This expands our system to 11 orbits:

|  Orbit  | Distance |
| :-----: | :------: |
|    1    |  0.101   |
|    2    |  0.190   |
|    3    |  0.298   |
|    4    |  0.482   |
| 5 (*N*) |  0.834   |
|    6    |  1.525   |
|    7    |  3.003   |
|    8    |  4.739   |
|    9    |  11.379  |
|   10    |  18.298  |
|   11    |  33.357  |
… and we can proceed to design planemos for each orbit, or eliminate some orbits and install asteroid belts, or adjust orbital intervals to suit our needs.... the sky's the limit.

> **Hippy**: Oh, ha-ha...

C'mon, you had to know I'd use that pun at _some point_ didn't you?

With this method, a worldmaker can quickly generate a full planemo system that is physically plausible, statistically grounded, and symbolically consistent with WBN cosmology.

[[Asteroid Belts and Resonance Gaps — working out]]