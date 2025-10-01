
## Abstract  
**Major Topics:**  
- Demonstrates integration of **thermozones (H₀–H₅)**, **ontozones**, and **orbital generation rules** into a coherent stellar system design.  
- Stepwise calculation:  
  - Thermozone limits derived from the nucleal orbit ($𝒩 = 0.834$ AU).  
  - Placement of generated orbits into both thermozone and ontozone categories.  
- Worked example tables:  
  - Case with both nucleal (𝒩) and perannual (𝒫) orbits → reveals interval violation ($I = 1.162$ < minimum 1.5).  
  - Case with **perannual planemo only** → valid intervals maintained (1.574–1.927 AU).  
- Demonstrates **design trade-offs**: some orbital anchors (𝒩 vs. 𝒫) may be mutually exclusive depending on stellar mass/luminosity.  
- Stellar parameter recalculation (luminosity, temperature, spectral type, subclass index) validates the system’s spectral class (G4.701).  
- Orbital habitability evaluation:  
  - Perannual orbit receives ~74.1% of nucleal flux.  
  - Corresponding Orbital Habitability Index (OHI) = 0.958 (95.8% of nucleal).  
- Emphasis: WCB design enforces **minimum orbital spacing (I ≥ 1.5)** as a hard rule, while maximum spacing (I ≤ 2.0) is treated as flexible.  

**Key Terms & Symbols:**  
- **Δ (Delta):** factor expressing relative distance offset between perannual and nucleal orbits.  
- **F (Flux):** relative stellar irradiance at a given orbital distance, normalized to 1.0 at 𝒩.  
- **OHI (Orbital Habitability Index):** previously defined, applied here in practice.  

**Cross-Check Notes:**  
- **New glossary entries needed:** Δ (distance ratio), F (stellar flux).  
- Reinforces prior entries: thermozones, ontozones, 𝒩, 𝒫, orbital intervals.  
- Serves as a practical example of reconciling WCB rules with real stellar constraints.  
---
---


# Calculating the Thermozones
Since we know our nucleal orbit is $\mathcal{N} = 0.834\;AU$, we can calculate the thermozone limits:
$$
\begin{align}
H_0 = 0.500\mathcal{N} &= 0.500(0.834) = 0.417\;AU \\
H_1 = 0.750\mathcal{N} &= 0.750(0.834) = 0.626\;AU \\
H_2 = 0.950\mathcal{N} &= 0.950(0.834) = 0.792\;AU \\
H_3 = 1.385\mathcal{N} &= 1.385(0.834) = 1.115\;AU \\
H_4 = 1.770\mathcal{N} &= 1.770(0.834) = 1.476\;AU \\
H_5 = 4.850\mathcal{N} &= 4.850(0.834) = 4.045\;AU \quad \text{Frost Line} \\
\end{align}
$$
And we can add these to our orbits table from above and determine the thermozones and ontozones of the orbits:

|       Orbit        | Distance | <center>Thermozone</center> | <center>Ontozone</center> |
| :----------------: | :------: | --------------------------- | ------------------------- |
|         1          |  0.101   | Igniozone                   | Xenotic                   |
|         2          |  0.190   | Igniozone                   | Xenotic                   |
|         3          |  0.298   | Ignoizone                   | Xenotic                   |
|       $H_0$        |  0.417   |                             |                           |
|         4          |  0.482   | Calorozone                  | Inner Parahabitable       |
|       $H_1$        |  0.626   |                             |                           |
|       $H_2$        |  0.792   |                             |                           |
| 5 (*$\mathcal{N}$) |  0.834   | Solarazone                  | Hospitable                |
|       $H_3$        |  1.115   |                             |                           |
|       $H_4$        |  1.476   |                             |                           |
|         6          |  1.525   | Brumazone                   | Outer Parahabitable       |
|         7          |  3.003   | Brumazone                   | Outer Parahabitable       |
|       $H_5$        |  4.045   |                             |                           |
|         8          |  4.739   | Cryozone                    | Xenotic                   |
|         9          |  11.379  | Cryozone                    | Xenotic                   |
|         10         |  18.298  | Cryozone                    | Xenotic                   |
|         11         |  33.357  | Cryozone                    | Xenotic                   |
And, we can calculate the perannual orbital distance and the star's spectral type by:
**Perannual Orbit**
$$
\begin{align}
L &= \mathcal{N}^2 = 0.834^2 = 0.696 \\
M &= \sqrt[3.8]{L} = \sqrt[3.8]{0.696} = 0.909 \\
A &= \sqrt[3]{0.909} = 0.969\;AU\;✓
\end{align}
$$
The perannual orbit in this system is at $A = 0.969\;AU$.

**Spectral Type**
$$
\begin{align}
L &= 0.696 \\
T &= \sqrt[7.6]{L} = \sqrt[7.6]{0.696} = 0.953\odot \\
K &= 5800T = 5800(0.953) = 5529.92 \quad \text{Spectral Class G: κ = 6000; þ = 100} \\[2em]
\mathcal{S} &= \dfrac{\kappa - K}{100} = \dfrac{6000 - 5529.92}{100} = \dfrac{470.08}{100} = 4.701\\
\end{align}
$$
The spectral type of our star is $G4.701$.

> **Hippy**: Uh..... that perannual orbit distance....

Excellent catch!

> **Keppy**: What....?

Check this out: we already know that our nucleal orbit is at $\mathcal{N} = 0.834\;AU$.  *If* we put planemo on the perannual orbit at $A = 0.969\;AU$ the interval between the nucleal orbit and the perannual orbit is only:
$$
I = \dfrac{0.969}{0.834} = 1.162\;AU\;✓
$$
… which is less than our specified minimum $I > 1.500\;AU$.

> **Keppy**: Which means....

> **Hippy**: Either we don't have a planemo on the nucleal orbit, *or* we don't have a planemo on the perannual orbit; those orbits are fixed by the stellar parameters  – neither can be shifte.

EXACTLY!  This is the power  — but also the limitation — of our system.  Some things we can tweak as we please; other things we have to work with, or work around.

In this case, we're forced to choose between a planemo with Earth's stellar flux, or a planemo with Earth's orbital period, but we can't have both.

> **Keppy**: What if we drop the nucleal planemo and go with the parahabitable planemo?

Excellent thought... let's work that through.  Here's a modified orbit table taking that into account:

|       Orbit       | Distance | <center>Thermozone</center> | <center>Ontozone</center> | Interval |
| :---------------: | :------: | --------------------------- | ------------------------- | -------- |
|         1         |  0.101   | Igniozone                   | Xenotic                   |          |
|         2         |  0.190   | Igniozone                   | Xenotic                   | 1.884    |
|         3         |  0.298   | Ignoizone                   | Xenotic                   | 1.573    |
|       $H_0$       |  0.417   |                             |                           |          |
|         4         |  0.482   | Calorozone                  | Inner Parahabitable       | 1.616    |
|       $H_1$       |  0.626   |                             |                           |          |
|       $H_2$       |  0.792   |                             |                           |          |
| 5 ($\mathcal{A}$) |  0.969   | Solarazone                  | Hospitable                | »1.927«  |
|       $H_3$       |  1.115   |                             |                           |          |
|       $H_4$       |  1.476   |                             |                           |          |
|         6         |  1.525   | Brumazone                   | Outer Parahabitable       | »1.574«  |
|         7         |  3.003   | Brumazone                   | Outer Parahabitable       |          |
|       $H_5$       |  4.045   |                             |                           |          |
|         8         |  4.739   | Cryozone                    | Xenotic                   | 1.552    |
|         9         |  11.379  | Cryozone                    | Xenotic                   | 1.608    |
|        10         |  18.298  | Cryozone                    | Xenotic                   | 1.823    |
|        11         |  33.357  | Cryozone                    | Xenotic                   | 1.778    |
The interval between the perannual orbit and the next closer-in orbit is:
$$
I = \dfrac{0.969}{0.482} = 1.927\;AU
$$
… _just_ within our $I = 2.000\;AU$ maximum, and the interval to the next orbit out is:
$$
I = \dfrac{1.525}{0.969} = 1.574\;AU
$$
… which, again, is _just_ within our specified minimum $I = 1.500\;AU$, so, yes we can drop the nucleal planemo and go with the perannual planemo, instead.

> **Hippy**: I am compelled to point out that the maximum interval is not nearly as absolute as the minimum interval...

Good point!  Planemos can certainly have wider intervals between their orbits than $I = 2.000\;AU$  – we just never want them to have an interval *less-than* $I = 1.500\;AU$.

> **Keppy**: But the perannual planemo is farther out than the nucleal orbit, so won't it get less stellar flux?

Well spotted!  And we can calculate that!  Since $A = 0.969\;AU$ and $N = 0.834\;AU$, and we know that the stellar flux at *N* = 1.0, we can calculate that *A* is:
$$
\Delta = \dfrac{0.969}{0.834} = 1.162
$$
… the perannual orbit is $1.162 \times$ farther out than the nucleal orbit, and since intensity decreases with the square of the distance:
$$
F = \dfrac{1}{\Delta^2}
$$
… we can calculate that the perannual planemo receives:
$$
F = \dfrac{1}{1.162^2}= \dfrac{1}{1.350} = 0.741
$$
… about 74.1% of the stellar flux as the nucleal orbit does... but that's still:
$$
\begin{gather}
H_I = -0.26\dfrac{D}{\mathcal{N}} + 1.26 = -0.26\dfrac{0.969}{0.834} + 1.26 = -0.26(1.162) + 1.26 = -0.302 + 1.26 = 0.958
\end{gather}
$$
… an orbital habitability index of 95.8% that of the nucleal orbit.  Slightly cooler, but not drastically so.


