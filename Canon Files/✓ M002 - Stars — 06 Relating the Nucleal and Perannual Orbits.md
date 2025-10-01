## Abstract  
**Major Topics:**  
- Relationship between the **Nucleal Orbit (𝒩)** and the **Perannual Orbit (𝒫)**.  
- Both are **orbital environs**, not strict limiting distances — they describe contextual properties of a star system.  
- Restatement of definitions:  
  - 𝒩 = $\sqrt{L}$ (AU), where *L* = stellar luminosity (⊙).  
  - 𝒫 = $\sqrt[3]{M+m}$ (AU), or $\sqrt[3]{M}$ if planemo mass *m* is disregarded.  
- Mass–luminosity link: $M = \sqrt[3]{L}$ → allows cross-approximation between 𝒩 and 𝒫.  
- Approximation formulas:  
  - $\mathcal{P} \approx \sqrt[6]{L}$ (perannual from luminosity).  
  - $\mathcal{N} \approx \sqrt{M^3}$ (nucleal from mass).  
  - Cross-relations:  
    - $\mathcal{P} \approx \sqrt[3]{\mathcal{N}}$  
    - $\mathcal{N} \approx \mathcal{P}^3$  
- Caution: these relations are **approximations**; robust calculation of 𝒩 and 𝒫 is recommended for precision:contentReference[oaicite:0]{index=0}.  

**Key Terms & Symbols:**  
- **𝒩 (Nucleal Orbit):** irradiance-based orbital benchmark.  
- **𝒫 (Perannual Orbit):** period-based orbital benchmark.  
- **Approximation relations:** linking 𝒩 and 𝒫 through stellar mass–luminosity scaling.  

**Cross-Check Notes:**  
- No new glossary entries beyond 𝒩 and 𝒫 (already staged in prior files).  
- This section functions as a **bridge note**, unifying the thermal and temporal anchors in WCB orbital design.  
- Emphasizes **approximation vs. precision**: usable shortcuts exist, but exact calculation is preferable.  
---
---



We have explored both [[M002 - Stars — 03 The Nucleal Orbit ✓|The Nucleal Orbit]] and [[M002 - Stars — 05 The Perannual Orbit ✓|The Perannual Orbit]].  These two are not *limiting distances*, but **orbital environs** which both describe and contribute to the ontosomic nature of planemos.

As a quick review:
- **Nucleal Orbit**: that orbit (expressed in AU) at which a planemo receives from its star(s) the same radiant flux as Earth receives from the Sun at one Astronomical Unit distance, calculated by: 
 $$
	\mathcal{N} = \sqrt{L}
$$

Where *L* = Luminosity of the star(s) as expressed in Solar units, ⊙

- **Perannual Orbit**: that orbit (expressed in AU) which has an orbital period of exactly one sidereal Earth year, calculated by:
$$
\mathcal{P} = \sqrt[3]{M+m}
$$
If we disregard the mass of the planemo *m*:
$$
\mathcal{P} = \sqrt[3]{M}
$$
And we saw in [[M002 - Stars — 02 Parameters ✓]] that through relationship:
$$
M = \sqrt[3]{L}
$$
This means that:
- The perannual orbit can be *approximated* directly from the luminosity by:
$$
\mathcal{P} \approx \sqrt[3]{\sqrt[3]{L}} \approx \sqrt[6]{L}
$$
- The nucleal orbit can be *approximated* directly from the mass by:
$$
\mathcal{N} \approx \sqrt{M^3}
$$
And, by extension either can be *approximated* from the other by:
$$
\begin{align}
\mathcal{P} &\approx \sqrt[6]{mathcal{N}^2} \approx \sqrt[3]{\mathcal{N}} \\
\mathcal{N} &\approx \mathcal{P}^3
\end{align}
$$
**REMEMBER**
- Both $\mathcal{N}$ and $\mathcal{P}$ are measured in astronomical units, not time!
- These last four equations are **approximations**; in most cases they'll be "accurate enough", but calculating$\mathcal{N}$ and $\mathcal{P}$ robustly is always advised.