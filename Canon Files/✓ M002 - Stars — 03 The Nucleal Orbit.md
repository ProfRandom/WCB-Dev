 
## Abstract  
**Major Topics:**  
- Defines the **Nucleal Orbit (𝒩)** — orbital distance at which a planemo receives the same stellar irradiance as Earth does at 1 AU.  
- Formula: 𝒩 = √L (where L = stellar luminosity in ⊙ units).  
- Anchors the **habitable zone (HZ)** around a star as ranges proportional to 𝒩.  
- Distinguishes between:  
  - **Habitable Zone** — wider corridor (⟨0.750 ∧ 1.770⟩𝒩).  
  - **Hospitable Zone** — narrower “middle lane” (⟨0.950 ∧ 1.385⟩𝒩).  
- Defines **parahabitable, habitable, hospitable, xenotic** orbital spans as structured “Ontozones.”  
- Introduces the **Frost Line (ϝ)** at 4.850𝒩, beyond which water cannot remain liquid.  
- Specifies notation for inner and outer orbital regimes:  
  - $Z_{IX}$, $Z_{IP}$, $Z_{IH}$, $Z_H$, $Z_{OH}$, $Z_{OP}$, $Z_{OX}$.  

**Key Terms & Symbols:**  
- **𝒩 (Nucleal Orbit)** — central reference orbit for irradiance equivalence.  
- **ϝ (Frost Line)** — outer limit for liquid water (~4.850𝒩).  
- **Ontozones** — structured orbital bands around stars.  
- **Zone Notation:**  
  - $Z_{IX}$ — Inner Xenotic Zone (<0.500𝒩).  
  - $Z_{IP}$ — Inner Parahabitable Zone (0.500–0.750𝒩).  
  - $Z_{IH}$ — Inner Habitable Zone (0.750–0.950𝒩).  
  - $Z_H$ — Hospitable Zone (0.950–1.385𝒩).  
  - $Z_{OH}$ — Outer Habitable Zone (1.385–1.770𝒩).  
  - $Z_{OP}$ — Outer Parahabitable Zone (1.770–4.850𝒩).  
  - $Z_{OX}$ — Outer Xenotic Zone (≥4.850𝒩).  

**Cross-Check Notes:**  
- Builds directly on **Habitable Zone Limits (H₀–H₅)** from v1.219.  
- Adds layered refinement: narrower **Hospitable Zone** within the wider HZ.  
- Introduces **Ontozones** and **zone notation system** for systematic classification.  
- Establishes Frost Line (ϝ) as a formal WCB parameter.  
---
---


## The Nucleal Orbit
The average distance from Earth to the Sun — about $1.496 \times 10^8$ km — is defined as one **astronomical unit (AU)**. Due to Earth’s slightly elliptical orbit, this distance varies by approximately ±2.5 million km between Earth's closest approach to and farthest distance from the Sun.

So, for all practical (and thesiastic) purposes, the Earth's orbital distance (*a*) is a = 1.0AU.  In fact *a* is the commonly used symbol for _any_ orbital distance when it is expressed in Astronomical Units.

For our purposes, I have revived an old word from the dusty backroom shelves of English — *nucleal* — and given it new life:

> **Nucleal Orbit** ($\mathcal{N}$): the orbital distance from any given star at which a planemo receives the same stellar irradiance as Earth receives from the Sun at 1 AU.

… and given it the utterly unimaginative symbol, $\mathcal{N}$.

The important thing to note here is that *$\mathcal{N}$ is not constant*, but varies from star to star, and it is calculated by:
$$
\mathcal{N} = \sqrt{L}
$$
Where:
- *L* = the Luminosity of the star in relative units

Obviously for the Sun:
$$
\mathcal{N} = \sqrt{L} = \sqrt{1} = 1
$$
> **Keppy**: So for a dimmer star N shifts closer to the star?

> **Hippy**: And for a brighter star, it shifts farther out from the star.

Correct on both counts.  And once we know _$\mathcal{N}$_, we can express the **habitable zone** (details coming!) as a proportional range around it.  For instance, for a star of half the Sun's luminosity $L = 0.5⊙$:
$$
\mathcal{N} = \sqrt{L} = \sqrt{0.5} = 0.7071\;AU
$$
### The Nucleal Orbit and the Habitable Zone
A quick survey of the existing literature reveals a commonly held definition for the **habitable zone** as:
$$
\langle0.950 \wedge 1.385\rangle \mathcal{N}
$$
… or, in other words: between 95% of the nucleal orbit distance to 1.385 times (138.5%) the nucleal orbit distance.  In the case of our hypothetical $L = 0.5⊙$ star and its $\mathcal{N}$ nucleal orbit, the range of its habitable zone calculates to:
$$
\begin{gather}
\mathcal{N} = 0.7071\; AU \\
\text{Inner Edge} = 0.950 \mathcal{N} = (0.950)(0.7071) = 0.6717\; AU \\
\text{Outer Edge} = 1.385 \mathcal{N} = (1.385)(0.7071) = 0.9793\; AU
\end{gather}
$$
> **Keppy**: So ... the *outer edge* of this star's habitable zone is *closer to its star* than *Earth orbits from the Sun*.....

Exactly.  But, this region is only a part of a total star system.
### The Ontozones – Two Habitable Zones
To start with, some scientist posit a wider, more "optimistic habitable zone" region, covering:
$$
\langle0.750 \wedge 1.770\rangle \mathcal{N}
$$
For our purposes, we call this *wider spread* the actual **habitable zone** and we call the narrower span the **hospitable zone**, so that the *hospitable zone* comprises a middle lane between the extremes of the *habitable zone*:
$$
\dfrac{1.385 - 0.95}{1.77 - 0.75} = \dfrac{0.435}{1.02} = 0.4265\;AU
$$
… about 42.65% of it, in fact.

|        Orbital Range         | <center>Ontozones</center> |
| :--------------------------: | -------------------------- |
| ⟨0.750 ∧ 0.950⟩$\mathcal{N}$ | Habitable Zone             |
| ⟨0.950 ∧ 1.385⟩$\mathcal{N}$ | Hospitable Zone            |
| ⟨1.385 ∧ 1.770⟩$\mathcal{N}$ | Habitable Zone             |
It has also been suggested that "desert" planemos (think Dune, Tattooine) might orbit in the zone between ⟨0.500 ∧ 0.750⟩N and we might call this the "desert planemo zone", which would be, by definition, **parahabitable** to **habitable** (but mostly the former).

|        Orbital Range         | <center>Ontozones</center> |
| :--------------------------: | -------------------------- |
| ⟨0.500 ∧ 0.750⟩$\mathcal{N}$ | Parahabitable              |
| ⟨0.750 ∧ 0.950⟩$\mathcal{N}$ | Habitable Zone             |
| ⟨0.950 ∧ 1.385⟩$\mathcal{N}$ | Hospitable Zone            |
| ⟨1.385 ∧ 1.770⟩$\mathcal{N}$ | Habitable Zone             |
### The Frost Line (ϝ)
Research indicates that beyond a distance of about $a = 4.850\;AU$ in our Solar system, water cannot remain liquid due to insufficient irradiance from the Sun.  This distance is sometimes termed the "Frost Line" or "Ice Line", and an orbital distance of $a = 4.850N$ is the value we set for this outer limit.

For instance:
- Mars' orbit in our own Solar system is $a = 1.524\;AU$, well within the $1.770N$ limit
- The asteroid belt is ≈ ⟨2.2 ∧ 3.2⟩AU, beyond $1.77\mathcal{N}$, but still within the $4.850\;AU$ ϝ limit.  This region in our Solar system does not host a sizeable planemo (and likely never did), but if one were to exist there, it would probably be parahabitable due to the orbital distance from the Sun.

This gives us another range of orbits we can add to our accounting:

|        Orbital Range         | <center>Ontozones</center> |
| :--------------------------: | -------------------------- |
| ⟨0.500 ∧ 0.750⟩$\mathcal{N}$ | Parahabitable              |
| ⟨0.750 ∧ 0.950⟩$\mathcal{N}$ | Habitable Zone             |
| ⟨0.950 ∧ 1.385⟩$\mathcal{N}$ | Hospitable Zone            |
| ⟨1.385 ∧ 1.770⟩$\mathcal{N}$ | Habitable Zone             |
| ⟨1.770 ∧ 4.850⟩$\mathcal{N}$ | Parahabitable              |

Jupiter's orbit is at $a = 5.204\;AU$, well _beyond_ the $4.850\;AU$ limit, and things just get colder from there, so we can specify that if any kind of "life" does exist in this region it is likely to be extremophile by Earth standards, which WCB denotes as "***xenotic***".

|         Orbital Range         | <center>Ontozones</center> |
| :---------------------------: | -------------------------- |
| ⟨0.500 ∧ 0.750⟩$\mathcal{N}$  | Parahabitable              |
| ⟨0.750 ∧ 0.950⟩$\mathcal{N}$  | Habitable Zone             |
| ⟨0.950 ∧ 1.385⟩$\mathcal{N}$  | Hospitable Zone            |
| ⟨1.385 ∧ 1.770⟩$\mathcal{N}$  | Habitable Zone             |
| ⟨1.770 ∧ 4.850⟩$\mathcal{N}$N | Parahabitable              |
|     4.850$\mathcal{N}$ →      | Xenotic                    |
Similarly, any "life" that might come to be on a body orbiting closer than 0.500N would also be xenotic:

|        Orbital Range         | <center>Ontozones</center> |
| :--------------------------: | -------------------------- |
|     ← 0.500$\mathcal{N}$     | Xenotic                    |
| ⟨0.500 ∧ 0.750⟩$\mathcal{N}$ | Parahabitable              |
| ⟨0.750 ∧ 0.950⟩$\mathcal{N}$ | Habitable Zone             |
| ⟨0.950 ∧ 1.385⟩$\mathcal{N}$ | Hospitable Zone            |
| ⟨1.385 ∧ 1.770⟩$\mathcal{N}$ | Habitable Zone             |
| ⟨1.770 ∧ 4.850⟩$\mathcal{N}$ | Parahabitable              |
|     4.850$\mathcal{N}$ →     | Xenotic                    |
Finally, we differentiate between inner and outer zones, and define notations for each:

|        Orbital Range         | <center>Ontozones</center> | Notation |
| :--------------------------: | -------------------------- | -------- |
|     ← 0.500$\mathcal{N}$     | Inner Xenotic Zone         | $Z_{IX}$ |
| ⟨0.500 ∧ 0.750⟩$\mathcal{N}$ | Inner Parahabitable Zone   | $Z_{IP}$ |
| ⟨0.750 ∧ 0.950⟩$\mathcal{N}$ | Inner Habitable Zone       | $Z_{IH}$ |
| ⟨0.950 ∧ 1.385⟩$\mathcal{N}$ | Hospitable Zone            | $Z_{H}$  |
| ⟨1.385 ∧ 1.770⟩$\mathcal{N}$ | Outer Habitable Zone       | $Z_{OH}$ |
| ⟨1.770 ∧ 4.850⟩$\mathcal{N}$ | Outer Parahabitable Zone   | $Z_{OP}$ |
|     4.850$\mathcal{N}$ →     | Outer Xenotic Zone         | $Z_{OX}$ |
This gives us a full inventory of orbital limits for any star system we choose to devise.