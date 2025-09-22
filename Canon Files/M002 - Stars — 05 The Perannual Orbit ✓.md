## The Perannual Orbit
There is one remaining essential star system orbit, which I have called the **perannual** orbit.  The word comes from the Latin *per annum*, meaning "per year" or "each year", and the name reflects that this is the orbit in any star system which has an orbital period (*P*) of exactly one Earth year.
##### IMPORTANT
> "One Earth Year" in this case is the duration of Earth's complete orbit around the Sun relative to the larger reference frame of the "fixed" stars; thus this is called the **sidereal year**, from the Latin *sidus*, "star".  This is measured and denoted in terms of **ephemeris days** — which are *defined* to be exactly 86400 _seconds_ in duration. Thus, the sidereal year (and, consequently, the perannual year) has a duration of:
$$\
\begin{gather}
365.256363004 \quad \text{Ephemeris Days} \\
or \\
365^d\;6^h\;9^m\; 9.763545^s
\end{gather}
$$
> This is _not_ a "year" as experienced by inhabitants on the surface of a planemo on this orbit (that is called the **tropical year**, which is in part dependent upon the _rotational period_ of the planemo, itself); this is the **sidereal year**.
> 
> Please see [[Units and Measures of Time ✓]] for a more in-depth discussion of this topic.

We denote the perannual year as $\mathcal{P}$, and its location in the star system _is not constant_ (the same as the *nucleal orbit* ($\mathcal{N}$) but is _determined_ by the mass of the star(s), and – to a small but measurable degree – by the mass of the planemo.

Please see [[M002 - Stars — 06 Relating the Nucleal and Perannual Orbits ✓]] for an in-depth exploration of this relationship.

The perannual orbit is determined not by the luminosity of the star(s) in the system but by **mass**, mostly of the stars(s), but the mass of the planemo can become a calculatory relevant factor if it is a significant fraction of the mass of the star(s).

The perannual orbit is an *orbital distance*, but it is predicated on the **period** of that orbit — how long it takes the planemo to complete one entire orbit (measured in Earth years).  **ANY** planemo orbital period is calculated (in relative terms) by:
$$
\begin{align}
	P &= \sqrt{\dfrac{a^3}{M+m}} \\
	a &= \sqrt[3]{P^2 (M+m)} \\
	M + m &= \dfrac{a^3}{P^2} \qquad \text{Believe it or not, this has its uses}
\end{align}
$$
Where:
- *P* = the planemo's orbital period in Earth sidereal years
- *a* = the measure of the semi-major axis of the planemo's orbit
- *M* = the mass of the star(s) in Solar masses
- *m* = the mass of the planemo (also expressed in _Solar_) masses

In many cases (such as that of Earth), *m* is such a small number that it can be ignored without drastically altering the value of *P*.  In the case of Earth:

- $M = 1⊙$
- $m = 0.000003003$⊙ ($3.003 \times 10^{-6}$) — three *millionths* of the Sun's mass
- $a = 1\;AU$

Calculating with **only** the Sun's mass:
$$
\begin{align}
	P &= \sqrt{\dfrac{a^3}{M}} = \sqrt{\dfrac{1^3}{1}} = \sqrt{\dfrac{1}{1}} = \sqrt{1} = 1\;\text{years}		
\end{align}
$$
Calculating with **both** masses:
$$
\begin{align}
	P &= \sqrt{\dfrac{a^3}{M + m}} \\
	 &= \sqrt{\dfrac{1^3}{1 + 0.000003003}} \\
	 &= \sqrt{\dfrac{1}{1.000003003}} \\
	 &= \sqrt{0.999997} \\
	 P &= 0.9999985\;\text{years}		
\end{align}
$$
… a difference of about 47.384 _seconds_.

> 🔍 **Takeaways**:
> >The *perannual orbit* defines the location in any star system where a planemo would complete one sidereal Earth year.
> >It may be closer-in than the nucleal orbit (**intranucleal**) or farther out than the nucleal orbit (**extranucleal**).
> >If it is ever _the same as the nucleal orbit_, then the star(s)' mass(es) must be $M = 1⊙$, and — ideally — the planemo's mass must be $m = 1⨁$.
> >Unlike the *nucleal orbit* (which depends on *stellar irradiance*), the perannual orbit *depends only the mass of the system* — and serves as a *temporal* rather than *thermal* reference point.

As shown above, the *distance* of any orbit can be calculated from the period and the masses via:
$$
a = \sqrt[3]{P^2 (M+m)}
$$
… but if we already know that $P = 1$, it drops out of the equation:
$$
a = \sqrt[3]{M+m}
$$
… such that the distance of the orbit is simply the cube-root of the sum of the masses.

For clarity, we denote the _distance_ of the perannual orbit with a $\mathcal{P}$ (for _perannual_), so our equation becomes:
$$
\begin{align}
\mathcal{P} &= \sqrt[3]{M+m} &&\text{When taking into account both masses} \\
\mathcal{P} &= \sqrt[3]{M} &&\text{When using only the central mass} \\
\end{align}
$$
