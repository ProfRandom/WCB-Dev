## Abstract  
**Major Topics:**  
- Explores calculation of habitable zones (thermozones) around **giant and supergiant stars**.  
- Notes that HZ limits depend on **luminosity**, but actual distances must be measured from the **stellar surface** — giant radii become a critical factor.  
- Worked example: **Aldebaran (K5 III)** with R = 44.2 ⊙, L = 439 ⊙, M = 1.16 ⊙ → nucleal orbit N ≈ 20.95 AU with orbital period ≈ 89 yr.  
- Discusses why main-sequence scaling laws fail for evolved stars (incorrect masses from radius–mass or luminosity–mass relations).  
- Extends to theoretical **200 M⊙ stars** (upper stellar mass limit), comparing MS scaling vs. the **Eddington limit**.  
- Worked example: **Stephenson 2-18**, largest known star (R ≈ 2150 ⊙, L ≈ 440,000 ⊙, M ≈ 45 ⊙) → nucleal orbit ≈ 663 AU.  
- Concludes that while thermozones can be calculated, giant/supergiant systems are **not Terran-hospitable**: their short lifetimes, unstable envelopes, and huge radii preclude long-term habitability.  

**Key Terms & Symbols:**  
- **Thermozone** — Habitable zone (HZ) limits derived from √L scaling.  
- **Nucleal Orbit (N)** — Central HZ reference orbit (√L).  
- **Lₑdd (Eddington limit)** — Maximum luminosity scaling for massive stars.  
- **Perannual Orbit (𝓟)** — Orbital distance yielding a one-year (Earth sidereal) period.  
- **Terran-hospitable** — Worlds truly habitable by unmodified humans.  
- **Mathematically parahabitable** — Worlds calculable as within HZs but uninhabitable in practice.  

**Cross-Check Notes:**  
- Expands habitable zone framework by highlighting limitations of **stellar lifetimes and radii**.  
- Connects to **Stellar Lifetimes and System Habitability** (short giant lifespans).  
- Introduces terminology to distinguish **theoretical HZs** from **practical human-centered habitability**.  
---
---


# 'Habitable Zones' of Giant Stars
Remember that although the habitable zone limits are *calculated* using the luminosity of the star, they are *measured* in distance from its center of mass. Thus, a giant star like Aldebaran, with a radius of $44.2$⊙ and a luminosity of $439$⊙, will have much larger fundamental orbits than the Sun.

## Stellar Radius Becomes a Significant Factor
Aldebaran's radius is the Sun's radius of $695,700$ km $\times 44.2 = 30,749,940$ km. One astronomical unit is $149.6$ million kilometers, which means that Aldebaran's radius measures $0.206$ astronomical units.

Thus, were Aldebaran to replace the Sun in the Solar system, its surface would fall only about $0.387 – 0.206 = 0.181$ AU (≈ $27$ million km) inside Mercury's orbit.

>Aldebaran’s true mass is measured at $1.16 M⊙$​. If, however, we incorrectly applied the main-sequence radius–mass scaling, we’d get $M \approx 67.34⊙$\​; the main-sequence luminosity–mass scaling would give $M \approx 4.959⊙$​. Both are wildly wrong — illustrating why Main Sequence relations must only be applied to Main Sequence stars; using them on evolved stars like Aldebaran gives wildly misleading results.

Using Aldebaran's correct (measured) mass value, its perannual orbit falls at $\mathcal{P} =\sqrt[3]{1.16} = 1.051$ AU, which is only $0.845$ AU beyond the star’s surface.

Aldebaran’s habitable zone limits and nucleal orbit calculate to be:
$$
\begin{align}
H_0 = 0.500\sqrt{439} = 10.476 \\
H_1 = 0.750\sqrt{439} = 15.714 \\
H_2 = 0.950\sqrt{439} = 19.905 \\
N = \sqrt{439} = 20.952 \\
H_3 = 1.385\sqrt{439} = 29.019 \\
H_4 = 1.770\sqrt{439} = 37.086 \\
H_5 = 4.850\sqrt{439} = 101.619 \\
\end{align}
$$
The orbital period of the nucleal orbit is:
$$
\mathcal{N}_p = \sqrt{\dfrac{20.952^3}{1.16}} = \sqrt{\dfrac{9197.94}{1.16}} = \sqrt{7929} = 89.05 \text{ years}
$$
… or about $54\%$ of Neptune's orbital period.

### Extending Into The Supergiant Realm
The theoretical maximum mass for a star is 200 M⊙.  We can't use the standard $L=M^{3.8}$ equation for stars above about 20 M⊙, so we have to choose the _lesser_ between:
$$
\begin{align}
L &= k \times M^{1.5}\;, \text{where } k=1.12 \times10^3 \\[1em]
&\text{or} \\
L_{Edd} &= 3.2 \times 10^4 \left(\dfrac{M_*}{M_⊙}\right)L⊙ \quad \text{(The Eddington Limit)} 
\end{align}
$$
In our case the equations return:
$$
\begin{align}
L_{MS} &= 1.12 \times 10^3 \times (200^{1.5}) = 1.12 \times 10^3 \times (2.828 \times 10^3) = 3.168 \times 10^6 \\[1em]
&\text{and} \\
L_{Edd} &= 3.2 \times 10^4 \left(\dfrac{200}{1}\right)L⊙ = 6.4 \times 10^6
\end{align}
$$
… so we'd go with the $L_{MS}$ value, and calculate the thermozone limits by:
$$
\begin{align}
H_0 &= 0.500\sqrt{3.168 \times 10^6} = 889.94 \\
H_1 &= 0.750\sqrt{3.168 \times 10^6} = 1334.92 \\
H_2 &= 0.950\sqrt{3.168 \times 10^6} = 1690.89 \\
N &= \sqrt{3.168 \times 10^6} = 1779.89 \\
H_3 &= 1.385\sqrt{3.168 \times 10^6} = 2465.14 \\
H_4 &= 1.770\sqrt{3.168 \times 10^6} = 3150.40 \\
H_5 &= 4.850\sqrt{3.168 \times 10^6} = 8632.46 \quad \text{(almost 14\% of a lightyear)} \\
\end{align}
$$
… but a perannual orbit of only
$$
\mathcal{P} = \sqrt[3]{M} = \sqrt[3]{200} = 5.848\;\text{AU}
$$
… which is **18.152 AU _inside_** the minimum estimated 24 AU radius of such a star.

### Working With a Known Star
The largest known star currently is Stephenson 2-18, with a radius of $R = 2150⊙\;(9.999AU)$, a measured luminosity of $L = 440000⊙$, and an upper estimated mass value of $M = 45⊙$.  These values yield thermozone limits of:
$$
\begin{align}
H_0 &= 0.500\sqrt{440000} = 331.66 \\
H_1 &= 0.750\sqrt{440000} = 497.49 \\
H_2 &= 0.950\sqrt{440000} = 630.16 \\
N &= \sqrt{440000} = 663.32 \\
H_3 &= 1.385\sqrt{440000} = 918.71 \\
H_4 &= 1.770\sqrt{440000} = 1174.09 \\
H_5 &= 4.850\sqrt{440000} = 3217.13 \\
\end{align}
$$
… and a perannual orbit of:
$$
\mathcal{P} = \sqrt[3]{M} = \sqrt[3]{45} = 3.557\;\text{AU}
$$
… 6.442 AU _inside_ the radius of the star.

>Remember:
>Such hypergiants live only a few million years at most, far too short for Terran-like biospheres to develop.  (See [[Stellar Lifetimes and System Habitability ✓]] for details.)
## Conclusion
You _can_ calculate thermozones (and hence orbital architectures) for giant and supergiant stars, but their immense radii, unstable envelopes, and short lifespans mean those thermozones don’t correspond to genuinely _habitable real estate._ In Protagorean terms, they fail the human-centered test: such systems are not _Terran-hospitable_, though they may be _mathematically parahabitable_ —that is, capable of hosting planets that humans could _use_ (for energy, staging, or resource acquisition) without being worlds where Terran-like life would be expected to evolve. (Of course, whether truly alien **xenotics** might arise under such extreme conditions is another matter entirely.)