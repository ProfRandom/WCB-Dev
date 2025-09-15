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
- $T_{min}$ ,  $T_{avg}$ ,  $T_{max}$ :  The minimum, average, and maximum separations of the two bodies from one another
- $P_{min}$ ,  $P_{avg}$ ,  $P_{max}$: The minimum, average, and maximum separations of the **primary** body (*P*) from the **barycenter** (*ḅ*)
- $S_{min}$ ,  $S_{avg}$ ,  $S_{max}$ :  The minimum, average, and maximum separations of the **secondary** body (*P*) from the **barycenter** (*ḅ*)

![[Binary System Dimensions.png|400]]

These are related through a series of equations which may seem daunting at first, but are quite straightforward once they are understood.

### Primary Dimensions
$$
\begin{align}
P_{min} &= P_{avg}(1 - e)
= T_{avg}(1 - e)\left(\dfrac{M_s}{M_p + M_s}\right)
= T_{min}\left(\dfrac{M_s}{M_p + M_s}\right)
= T_{max}\left(\dfrac{M_s}{M_p + M_s}\right)\left(\dfrac{1 - e}{1 + e}\right)\\[0.5em]
P_{max} &= P_{avg}(1 + e)
= T_{avg}(1 + e)\left(\dfrac{M_s}{M_p + M_s}\right)
= T_{max}\left(\dfrac{M_s}{M_p + M_s}\right)
= T_{min}\left(\dfrac{M_s}{M_p + M_s}\right)\left(\dfrac{1 + e}{1 - e}\right)\\[0.5em]
P_{avg} &= \dfrac{P_{min}}{1 - e} = \dfrac{P_{max}}{1 + e} = T_{avg}\left(\dfrac{M_s}{M_p+M_s}\right)
\end{align}
$$
### Secondary Dimensions
$$
\begin{align}
S_{min} &= S_{avg}(1 - e) 
= T_{avg}(1 - e)\left(\dfrac{M_p}{M_p + M_s}\right)
= T_{min}\left(\dfrac{M_p}{M_p + M_s}\right)
= T_{max}\left(\dfrac{M_p}{M_p + M_s}\right)\left(\dfrac{1 - e}{1 + e}\right)\\[0.5em]
S_{max} &= S_{avg}(1 + e)
= T_{avg}(1 + e)\left(\dfrac{M_p)}{M_p + M_s}\right)
= T_{max}\left(\dfrac{M_p}{M_p + M_s}\right)
= T_{min}\left(\dfrac{M_p}{M_p + M_s}\right)\left(\dfrac{1 + e}{1 - e}\right)\\[0.5em]
S_{avg} &= \dfrac{S_{min}}{1 - e} = \dfrac{S_{max}}{1 + e} = T_{avg}\left(\dfrac{M_p}{M_p+M_s}\right)
\end{align}
$$
### Total (Overall) Dimensions
$$
\begin{align}
T_{min} &= T_{avg}(1 - e)
= P_{min} + S_{min} \\[0.5em]
&= T_{avg}\left(\dfrac{1 - e}{1 + e}\right)
= P_{min}\left(\dfrac{M_p}{M_s} + 1\right)
= S_{min}\left(\dfrac{M_s}{M_p} + 1\right) \\[0.5em]
T_{max} &= T_{avg}(1 + e)
= P_{max} + S_{max} \\[0.5em]
&= T_{avg}\left(\dfrac{1 + e}{1 - e}\right)
= P_{max}\left(\dfrac{M_p}{M_s} + 1\right)
= S_{max}\left(\dfrac{M_s}{M_p} + 1\right) \\[0.5em]
T_{avg} &= \dfrac{T_{min}}{1 - e}
= \dfrac{T_{max}}{1 + e}
= P_{avg} + S_{avg}\\[0.5em]
&= P_{avg}\left(\dfrac{M_p}{M_s} + 1\right) 
= S_{avg}\left(\dfrac{M_s}{M_p} + 1\right) \\[0.5em]
&= P_{min}\left(\dfrac{M_p + M_s}{M_s (1 - e)}\right)
= P_{max}\left(\dfrac{M_p + M_s}{M_s (1 + e)}\right) \\[0.5em]
&= S_{min}\left(\dfrac{M_p + M_s}{M_p (1 - e)}\right)
= S_{max}\left(\dfrac{M_p + M_s}{M_p (1 + e)}\right)
\end{align}
$$

### Eccentricity Relationships
In the equations below a subscript dot $_{\bullet}$ means any two matching parameters; e.g. if $Max_{\bullet} - Min{\bullet}$ means any maximum value minus any minimum value of the same, such as $P_{max} - P_{min}$ .
#### System Eccentricity
$$
\begin{align}
e &= \dfrac{Max_\bullet - Min_{\bullet}}{Max_\bullet + Min_{\bullet}}
= 1 - \left[\dfrac{Min_{\bullet}}{Avg_{\bullet}}\right]
= \left[\dfrac{Max_{\bullet}}{Avg_{\bullet}}\right] - 1 \\[1em]
&= \dfrac{P_{max}(M_p + M_s)}{M_s T_{avg}} - 1 = 1 - \dfrac{P_{min}(M_p + M_s)}{M_s T_{avg}} \\[1em]
&= \dfrac{S_{max}(M_p + M_s)}{M_p T_{avg}} - 1 = 1 - \dfrac{S_{min}(M_p + M_s)}{M_p T_{avg}} \\[1em]
\end{align}
$$
#### Crossing Orbit Parameter
The circle $_{\circ}$ subscript is used to indicate expressions in which all terms share the **same positional magnitude** (e.g., max, min, or average), regardless of parameter type.
$$
\begin{align}
\acute{e} = \dfrac{M_p - M_s}{M_p + M_s}
= \dfrac{|S_{\circ} - P_{\circ}|}{S_{\circ} + P_{\circ}} 
= \dfrac{|S_{\circ} - P_{\circ}|}{T_{\circ}} \\[1em]
\text{Where } \frac{M_s}{M_p} = 0.8, \acute{e} ≥ 0.8519
\end{align}
$$
$é$ (e-prime) is the system eccentricity value at which the orbits of the stars become *_adjoined tangential_* $(e \gt 0; M_p \neq M_s)$
#### Limiting Eccentricity
$$
\begin{align}
\bar{e} = \dfrac{T_{max} - 0.100}{T_{max} + 0.100} \\[1em]
T_{max} \geq 0.100\left(\dfrac{1 + \bar{e}}{1 - \bar{e}}\right)
\end{align}
$$
$ē$ (e-bar) is the largest system eccentricity that can be used with a given $T_{max}$ , while ensuring that $T_{min} ≥ 0.100$.
#### System Limiting Parameter ($T_{lim}$)
The $T_{lim}$ parameter is closest any object can orbit to the system barycenter, and is simply defined as:
$$
T_{lim} = 4 T_{max}
$$
… 4 times the system $T_{max}$ parameter.
#### Forbidden Eccentricity
$$
\begin{align}
e_\times \leq \dfrac{B_0 - T_{lim}}{B_0 + T_{lim}} \quad | \quad 
e_\times \leq \dfrac{B_A - T_{lim}}{B_A + T_{lim}} \quad | \quad 
e_\times \leq \dfrac{B_N - T_{lim}}{B_N + T_{lim}}
\end{align}
$$
Where:
- $T_{lim} = 4 T_{max} = 4 T_{avg}(1 - e) = 4 T_{min}\left(\dfrac{1 + e}{1 - e}\right)$
$X_e$ is the largest system eccentricity that can be used with a given $T_{min}$ , ensuring that either the innermost habitable orbit ($B_0$), the perannual orbit (*A*), or the nucleal orbit (*N*) lies beyond $T_{lim}$.

#### Quarles' Stability Limit
$$
\begin{align}
\mathcal{Q}_L = 0.08 T_{avg} = 0.08\left(\dfrac{T_{min}}{1 - e}\right) \quad | \quad e = 1 - 0.08\left(\dfrac{T_{min}}{\mathcal{Q}_L}\right)
\end{align}
$$
$\mathcal{Q}_L$ is the maximum distance a planemo can orbit either star in a wide-binary system.
#### Quarles' Eccentricity Limit
$$
\mathcal{Q}_e = 0.92
$$
$\mathcal{Q}_e$ is the maximum eccentricity a wide-binary system can have while keeping $T_{min} ≥ \mathcal{Q}_L$.


