We have explored both [[M002 - Stars — 03 The Nucleal Orbit ✓|The Nucleal Orbit]] and [[M002 - Stars — 05 The Perannual Orbit ✓|The Perannual Orbit]].  These two are not *limiting distances*, but **orbital environs** which both describe and contribute to the ontosomic nature of planemos.

As a quick review:
- **Nucleal Orbit**: that orbit (expressed in AU) at which a planemo receives from its star(s) the same radiant flux as Earth receives from the Sun at one Astronomical Unit distance, calculated by: 
 $$
	N = \sqrt{L}
$$

Where *L* = Luminosity of the star(s) as expressed in Solar units, ⊙

- **Perannual Orbit**: that orbit (expressed in AU) which has an orbital period of exactly one sidereal Earth year, calculated by:
$$
A = \sqrt[3]{M+m}
$$
If we disregard the mass of the planemo *m*:
$$
A = \sqrt[3]{M}
$$
And we saw in [[M002 - Stars — 02 Parameters ✓]] that through relationship:
$$
M = \sqrt[3]{L}
$$
This means that:
- The perannual orbit can be *approximated* directly from the luminosity by:
$$
A \approx \sqrt[3]{\sqrt[3]{L}} \approx \sqrt[6]{L}
$$
- The nucleal orbit can be *approximated* directly from the mass by:
$$
N \approx \sqrt{M^3}
$$
And, by extension either can be *approximated* from the other by:
$$
\begin{align}
A &\approx \sqrt[6]{N^2} \approx \sqrt[3]{N} \\
N &\approx A^3
\end{align}
$$
**REMEMBER**
- Both *N* and *A* are measured in astronomical units, not time!
- These last four equations are **approximations**; in most cases they'll be "accurate enough", but calculating *N* and *A* robustly is always advised.