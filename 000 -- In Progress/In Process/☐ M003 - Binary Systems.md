**Solar analog stars are more often found in binary or multiple systems than not, with over half exhibiting multiplicity.**

- **Duquennoy & Mayor (1991)** originally found that approximately **57%** of solar-type stars (spectral types F6–K3) in the solar neighborhood are part of binary or higher-order systems.    
- **Raghavan et al. (2010)** updated this with modern data, reporting:    
    - **~44%** as binaries        
    - **~11%** as triples or higher        
    - → Yielding a total multiplicity fraction of **~55%** for solar-type stars.       

**Statistically, stars comparable to the Sun are more likely than not to belong to binary or multiple systems**—a pattern that profoundly influences system architecture, orbital stability zones, and the landscape of potential habitability.

This section focuses on binary systems, both stellar and planemo. While higher-multiplicity arrangements are common and fascinating, they introduce significant mathematical and physical complexity beyond the current scope of practical thesiastics. Even binaries alone present formidable obstacles to stable, life-supporting worlds—but to omit them would be to overlook one of the most consequential configurations in stellar system design.
# The Basics
Binary systems consist of two bodies bound in mutual gravitational relationship, each tracing an orbital path around a shared center of mass known as the **barycenter** (_ḅ_). This point, shown as a black X in the figure, _always_ lies along the line connecting the centers of the two bodies and is not a massive object itself, but a calculated position determined by the masses and separation of the components.

The more massive object (the **primary body**) orbits closer to the barycenter, while the **secondary body** traces a larger path on the opposite side. Both orbits are elliptical, share the same eccentricity (ϵ), and are synchronized in period, preserving the balance of angular momentum.

![[Binary System Basics.png|400]]

A binary system is described by a total of nine dimensions (average dimensions not illustrated):
- $T_{min}$ ,  $\mathcal{A}$ ,  $T_{max}$ :  The minimum, average, and maximum separations of the two bodies from one another
- $P_{min}$ ,  $P_{avg}$ ,  $P_{max}$: The minimum, average, and maximum separations of the **primary** body (*P*) from the **barycenter** (*ḅ*)
- $S_{min}$ ,  $S_{avg}$ ,  $S_{max}$ :  The minimum, average, and maximum separations of the **secondary** body (*P*) from the **barycenter** (*ḅ*)

![[Binary System Dimensions.png|400]]

These are related through a series of equations which may seem daunting at first, but are quite straightforward once they are understood.

### Primary Dimensions
$$
\begin{align}
P_{avg} &= \mathcal{A} \cdot\dfrac{M_S}{M_P+M_S} \\[1em]
P_{min} &= P_{avg}(1 - e) \\[1em]
P_{max} &= P_{avg}(1 + e)\\[1em]
\end{align}
$$
### Secondary Dimensions
$$
\begin{align}
S_{avg} &= \mathcal{A} \cdot\dfrac{M_P}{M_P+M_S} \\[1em]
S_{min} &= S_{avg}(1 - e) \\[1em]
S_{max} &= S_{avg}(1 + e)\\[1em]
\end{align}
$$
### Total (Overall) Dimensions

$$
\begin{gather}
T_{min} = \mathcal{A}(1 - e)
= P_{min} + S_{min} = T_{max}\left(\dfrac{1 - e}{1 + e}\right) \\
T_{max} = \mathcal{A}(1 + e)
= P_{max} + S_{max} = T_{min}\left(\dfrac{1 + e}{1 - e}\right) \\
\mathcal{A} = \dfrac{T_{min}}{1 - e}
= \dfrac{T_{max}}{1 + e}
= P_{avg} + S_{avg}\\[0.5em]
\end{gather}
$$

### Eccentricity Relationships
In the equations below a subscript dot $_{\bullet}$ means any two matching parameters; e.g. if $Max_{\bullet} - Min{\bullet}$ means any maximum value minus any minimum value of the same, such as $P_{max} - P_{min}$ .
#### System Eccentricity
$$
\begin{align}
e &= \dfrac{Max_\bullet - Min_{\bullet}}{Max_\bullet + Min_{\bullet}}
= \left[1 - \dfrac{Min_{\bullet}}{Avg_{\bullet}}\right]
= \left[\dfrac{Max_{\bullet}}{Avg_{\bullet}} - 1\right] \\[1em]
&= \left(P_{max} \cdot \dfrac{M_P + M_S}{\mathcal{A} \cdot M_S}\right) - 1
= 1 - \left(P_{min} \cdot \dfrac{M_P + M_S}{\mathcal{A} \cdot M_S}\right) \\[1em]
&= \left(S_{max} \cdot \dfrac{M_P + M_S}{\mathcal{A} \cdot M_P}\right) - 1
= 1 - \left(S_{min} \cdot \dfrac{M_P + M_S}{\mathcal{A} \cdot M_P}\right) \\[1em]
\end{align}
$$
#### Crossing Orbit Parameter
The circle $_{\circ}$ subscript is used to indicate expressions in which all terms share the **same positional magnitude** (e.g., max, min, or average), regardless of parameter type.
$$
\begin{align}
\acute{e} = \dfrac{M_P - M_S}{M_P + M_S}
= \dfrac{|S_{\circ} - P_{\circ}|}{S_{\circ} + P_{\circ}} 
= \dfrac{|S_{\circ} - P_{\circ}|}{T_{\circ}}
\end{align}
$$
- $é$ (e-prime) is the system eccentricity value at which the orbits of the stars become *_adjoined tangential_* $(e \gt 0; M_P \neq M_S)$
- For a mass ratio of $^{M_S}/_{M_P} = 0.8$, the system requires $\acute{e} \geq 0.8519$ for the primary and secondary orbits to adjoin tangentially.
#### Limiting Eccentricity
$$
\begin{align}
\bar{e} = \dfrac{T_{max} - 0.100}{T_{max} + 0.100} \\[1em]
T_{max} \geq 0.100\left(\dfrac{1 + \bar{e}}{1 - \bar{e}}\right)
\end{align}
$$
- $ē$ (e-bar) is the largest system eccentricity that can be used with a given $T_{max}$ , while ensuring that $T_{min} ≥ 0.100$.
#### System Limiting Parameter ($T_{lim}$)
The $T_{lim}$ parameter is closest any object can orbit to the system barycenter, and is simply defined as:
$$
T_{lim} = 4 T_{max}
$$
… 4 times the system $T_{max}$ parameter.
#### Forbidden Eccentricity
$$
\begin{gather}
e_\times \leq \dfrac{B_0 - T_{lim}}{B_0 + T_{lim}} \quad | \quad 
e_\times \leq \dfrac{B_\mathcal{P} - T_{lim}}{B_\mathcal{P} + T_{lim}} \quad | \quad 
e_\times \leq \dfrac{B_\mathcal{N} - T_{lim}}{B_\mathcal{N} + T_{lim}} \\[1em]
T_{lim} = 4 T_{max} = 4 \mathcal{A}(1 + e) = 4 T_{min}\left(\dfrac{1 + e}{1 - e}\right)
\end{gather}
$$
- $e_\times$ is the largest system eccentricity that can be used with a given $T_{min}$ , ensuring that either the innermost habitable orbit ($B_0$), the perannual orbit ($\mathcal{P}$), or the nucleal orbit ($\mathcal{N}$) lies beyond $T_{lim}$.

#### Quarles' Stability Limit
$$
\begin{align}
\mathcal{Q}_L &= 0.08 \mathcal{A} = 0.08\left(\dfrac{T_{min}}{1 - e}\right) \\[1em]
e &= 1 - 0.08\left(\dfrac{T_{min}}{\mathcal{Q}_L}\right)
\end{align}
$$
- $\mathcal{Q}_L$ is the maximum distance a planemo can orbit either star in a wide-binary system.
#### Quarles' Eccentricity Limit
$$
\mathcal{Q}_e = 0.92
$$
- $\mathcal{Q}_e$ is the maximum eccentricity a wide-binary system can have while keeping $T_{min} ≥ \mathcal{Q}_L$.

# Relative Orbit of the Secondary
There are times (such as when the Secondary is much less massive than the Primary — typically $\frac{M_{star}}{m_{planet}} \gtrsim 4000$, the approximate star/brown dwarf mass dividing line — it is convenient to treat the Primary as stationary and the Secondary as following the relative orbit alone.  Therefore,
$$
\begin{gather}
R_{min} = T_{min} \\[0.5em]
R_{avg} = \mathcal{A} \\[0.5em]
R_{max} = T_{max} \\
\end{gather}
$$
For instance, in the case of the Earth-Sun system:
$$
\begin{align}
\mathcal{A} &= 1.0 AU \\[0.5em]
P_{avg} &= \mathcal{A} \cdot\dfrac{M_S}{M_P+M_S} \\[1em]
&= 1.0 \cdot \frac{1}{333000+1} \\[1em]
&= 1.0 \cdot \frac{1}{333001} = 3.009299 \times 10^{-6} AU \\[1.5em]
1 \text{ AU } &= 1.496 \times 10^6 \text{ km} \\
\therefore P_{avg} &= 3.009299 \times 10^{-6} \times 1.496 \times 10^8 ≈ 449 \text{ km}  
\end{align}
$$

Considering that the Sun’s radius is $696{,}340$ km, a wobble of only ≈450 km ($\approx 0.065\%$) is justifiably negligible.

# Barycentrics
$$
\begin{align}
B_{min} &= \mathcal{A} \cdot \frac{M_S (1 - e)}{M_P + M_S} \\[0.5em]
&= B_{avg}(1 - e) \\[1em]
B_{avg} &= \mathcal{A} \cdot \frac{M_S}{M_P + M_S} \\[1em]
B_{max} &= \mathcal{A} \cdot \frac{M_S (1 + e)}{M_P + M_S} \\[0.5em]
&= B_{avg}(1 + e)
\end{align}
$$
These equations are useful when working with a planet-moon or double-planet system where the two masses are closer to parity.  It becomes simpler to think of the two bodies as stationary and the barycenter as orbiting between then (***there will be several illustrations making this abundantly clear***)

# Constant Equalities
$$
\begin{align}
&\frac{S_\circ}{P_\circ} = \frac{M_P}{M_S} \qquad
&&\frac{P_\circ}{S_\circ} = \frac{M_S}{M_P} \\[1em]
&\frac{P_\circ}{T_\circ} = \frac{M_S}{M_P + M_S}   \qquad
&&\frac{S_\circ}{T_\circ} = \frac{M_P}{M_P + M_S} \\[1em]
&\frac{T_\circ}{P_\circ} = \frac{M_P}{M_S} + 1   \qquad
&&\frac{T_\circ}{S_\circ} = \frac{M_S}{M_P} + 1 \\[3em]
&\frac{Min_\bullet}{Max_\bullet} = \frac{1 - e}{1 + e} \qquad
&&\frac{Max_\bullet}{Min_\bullet} = \frac{1 + e}{1 - e}
\end{align}
$$



