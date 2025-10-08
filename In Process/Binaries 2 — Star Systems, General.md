Solar analog stars are more often than not found in binary or multiple systems than not, with over half exhibiting multiplicity.

- **Duquennoy & Mayor (1991)** originally found that approximately **57%** of solar-type stars (spectral types F6-K3 — more-or-less what WCB calls **Solar Cognates**) in the solar neighborhood are part of binary or higher-order systems.

- **Raghavan et al. (2010)** updated this with modern data for the same spectral class range, reporting:    
    - **~44%** as binaries        
    - **~11%** as triples or higher        
    - → Yielding a total multiplicity fraction of **~55%** for solar-type stars.       

This tendency toward multiplicity defines a pattern that profoundly influences system architecture, orbital stability zones, and the landscape of potential habitability.

### Companion Mass Trends by Primary Type

From the combined statistical analyses of **Duquennoy & Mayor (1991)**, **Raghavan et al. (2010)**, **Moe & Di Stefano (2017)**, and **Li et al. (2022, LAMOST)**, a clear pattern of Primary-to-Secondary spectral type pairings emerges: the **spectral class of the primary star** strongly constrains the **range of companion masses** likely to occur. In other words, binary pairing is _not_ random across the mass spectrum.

- **Early-type primaries (A–F)** tend to draw secondaries from a **narrow, high-mass corridor**, favoring near-equal companions—what observers call the _twin excess_.    
- **Solar-type primaries (G-class)** exhibit a **broader, moderately declining distribution**, allowing both near-equal companions and somewhat smaller partners (typically late G or K types).    
- **Cooler primaries (K–M)** show a **progressively wider, low-mass-biased spread**, where secondaries are often much smaller—late K, M, or even substellar companions.    

This trend can be summarized as:

> Earlier, hotter stars → **narrow, high-q pairing range** (favoring twins).  
> Later, cooler stars → **broad, low-q range** (favoring lighter companions).

In the WCB framework, this is captured algebraically as:
$$
M_2 = M_1 \times ⟨⟨a ∧ b⟩⟩^P
$$
where the interval ⟨⟨a ∧ b⟩⟩ and weighting exponent _p_ both shrink or expand systematically with spectral type—reflecting the real statistical narrowing of possible companion masses seen in stellar surveys.

Calculating a Secondary star's mass ($M_2$) based on the mass of the Primary ($M_1$):

### Why the Trends Exist — Formation and Fragmentation

The narrowing of companion mass ranges with earlier spectral types appears to arise from how **stellar systems form** and how **mass is partitioned** during collapse. Current theory points to several overlapping mechanisms:

1. **Core Fragmentation Efficiency**    
    - In more massive, hotter molecular cores (the progenitors of A–F stars), the collapse tends to fragment into a _small number_ of roughly equal-mass condensations.        
    - These fragments accrete from the same envelope, producing **near-equal-mass binaries** (“twins”) with small separations.        
    - In contrast, lower-mass cores (forming G–M stars) fragment less efficiently and often leave a single dominant protostar plus several much smaller condensations — yielding **low-mass companions** or none at all.
        
2. **Accretion and Disk Mass Scaling**    
    - Disk mass scales roughly with the mass of the protostar ($M_{disk} \sim 0.01 – 0.1 M_\star$).        
    - High-mass primaries therefore sustain _massive disks_ capable of feeding substantial secondaries; low-mass primaries cannot.        
    - As a result, secondary masses are capped by the available accretion reservoir, reinforcing the trend toward smaller $\frac{M_2}{M_1}$​ ratios for late-type stars.
        
3. **Dynamical Evolution and Ejection Bias**    
    - In nascent clusters, wide, unequal-mass pairs are dynamically fragile. Encounters preferentially disrupt them, leaving behind tighter and more equal-mass survivors for massive primaries (which tend to form in denser environments).        
    - Lower-mass primaries often form in less crowded regions, where wide, unequal pairs can survive — adding to the broad low-q tail seen among K and M dwarfs.
        
4. **Radiative Feedback (Massive-Star Limiter)**    
    - For A–F stars, strong radiation pressure can halt accretion onto small fragments, effectively forcing the system toward a few large components rather than many small ones.        
    - For cool G–M stars, radiative feedback is weak, allowing a continuum of fragment masses and more varied companions.
        

---

### Summary Insight

> **High-mass stars** form in **fragment-rich, radiation-dominated cores** that favor one or two nearly equal siblings.  
> **Low-mass stars** form in **quieter, low-mass disks**, where stochastic accretion and weak feedback yield a much broader and smaller companion distribution.
### Flat Draw Method

$$
M_2 = M_1 \times ⟨⟨a ∧ b⟩⟩
$$
Where:

| **Primary** | <center>**Range<br>(⟨⟨a ∧ b⟩⟩)</center><br>** | <center>**Typical<br>“neutral”<br>value</center><br><br>** |
| :---------: | --------------------------------------------: | ---------------------------------------------------------: |
| **A**       |                                   ⟨0.9 ∧ 1.0⟩ |                                                     ≈ 0.95 |
| **F**       |                                   ⟨0.7 ∧ 0.9⟩ |                                                      ≈ 0.8 |
| **G**       |                                   ⟨0.6 ∧ 0.8⟩ |                                                      ≈ 0.7 |
| **K**       |                                   ⟨0.4 ∧ 0.7⟩ |                                                     ≈ 0.55 |
| **M**       |                                   ⟨0.2 ∧ 0.5⟩ |                                                     ≈ 0.35 |
### Weighted Draw Method
$$
M_2 = M_1 \times ⟨⟨a ∧ b⟩⟩^P
$$
Where:

| **Primary** | <center>**Range<br>(⟨⟨a ∧ b⟩⟩)</center><br>** | <center>**Lower-<br>bias<br>(favor<br>smaller<br>M₂)</center><br><br><br><br>** | <center>**Upper-<br>bias<br>(favor twin<br>M₂)</center><br><br><br>** | <center>**Typical<br>“neutral”<br>bias<br>value</center><br><br><br>** | <center>**Physical rationale**</center>                                                    |
| :---------: | --------------------------------------------: | ------------------------------------------------------------------------------: | --------------------------------------------------------------------: | ---------------------------------------------------------------------: | :----------------------------------------------------------------------------------------- |
| **A**       |                                   ⟨0.9 ∧ 1.0⟩ |                                                                     ⟨0.8 ∧ 0.9⟩ |                                                           ⟨1.2 ∧ 1.5⟩ |                                                                  ≈ 1.2 | High twin fraction; modest upward skew reproduces near-equal masses.                       |
| **F**       |                                   ⟨0.7 ∧ 0.9⟩ |                                                                     ⟨0.6 ∧ 0.8⟩ |                                                           ⟨1.1 ∧ 1.3⟩ |                                                                  ≈ 1.0 | Slight bias toward smaller companions, but twins still possible.                           |
| **G**       |                                   ⟨0.6 ∧ 0.8⟩ |                                                                     ⟨0.5 ∧ 0.8⟩ |                                                           ⟨1.0 ∧ 1.2⟩ |                                                                  ≈ 0.8 | Distribution roughly flat; mild downward bias reproduces the DM91 “flat or falling” trend. |
| **K**       |                                   ⟨0.4 ∧ 0.7⟩ |                                                                     ⟨0.5 ∧ 0.8⟩ |                                                           ⟨1.0 ∧ 1.1⟩ |                                                                  ≈ 0.7 | Clearly skewed toward smaller secondaries; use *p* ≈ 0.6∧0.8 to get that fall-off.         |
| **M**       |                                   ⟨0.2 ∧ 0.5⟩ |                                                                     ⟨0.5 ∧ 0.7⟩ |                                                            ⟨1.0 ∧ 1.1 |                                                                  ≈ 0.6 | Strongly bottom-heavy distribution; small-q companions common.                             |

**How to read this table**
- The “lower-bias” column gives a reasonable p range if you want your generator to prefer small companions.
- The “upper-bias” column gives values that push draws upward (more “twin-like” systems).
- The “typical neutral value” is the mid-case consistent with observed distributions.

<center>↓↓↓↓↓ <b>RESUME HERE</b> ↓↓↓↓↓</center>
#### Limiting Maximum Eccentricity ($\bar{e}$)
$$
\begin{align}
\bar{e} = \dfrac{T_{max} - 0.100}{T_{max} + 0.100} \\[1em]
T_{max} \geq 0.100\left(\dfrac{1 + \bar{e}}{1 - \bar{e}}\right)
\end{align}
$$
- $ē$ (e-bar) is the largest system eccentricity that can be used with a given $T_{max}$ , while ensuring that $T_{min} ≥ 0.100$.
#### System Limiting Parameter ($T_{lim}$)
The $T_{lim}$ parameter is closest any _other_ object can orbit to the system barycenter (for close binary pairs), and is simply defined as:
$$
T_{lim} = 4 T_{max}
$$
… 4 times the system $T_{max}$ parameter.
#### Quarles' Stability Limit ($\mathcal{Q}_L$)
$$
\begin{align}
\mathcal{Q}_L &= 0.08 \mathcal{A} = 0.08\left(\dfrac{T_{min}}{1 - e}\right) \\[1em]
e &= 1 - 0.08\left(\dfrac{T_{min}}{\mathcal{Q}_L}\right)
\end{align}
$$
- $\mathcal{Q}_L$ is the maximum distance a planemo can orbit either star in a wide-binary system.
#### Quarles' Eccentricity Limit ($\mathcal{Q}_e$)
$$
\mathcal{Q}_e = 0.92
$$
- $\mathcal{Q}_e$ is the maximum eccentricity a wide-binary system can have while keeping $T_{min} ≥ \mathcal{Q}_L$.

### ⚙ Physics Note — The Period–Eccentricity Relation

#### 1. **Observed Pattern**

Empirically, binary systems trace a clear trend:

| Regime           | Typical Period P | Typical Eccentricity e         | Behavior                    |
| ---------------- | ---------------- | ------------------------------ | --------------------------- |
| **Short-period** | P ≲ 10 days      | e ≈ 0                          | Nearly circular             |
| **Intermediate** | 10 – 10³ days    | e rises from 0 → 0.6           | Mixed circular / elliptical |
| **Wide**         | P ≳ 10³          | Broad scatter, e often 0.6–0.9 | Dynamically “hot”           |

This relation has been confirmed repeatedly—from **Duquennoy & Mayor (1991)** and **Raghavan et al. (2010)** to **Moe & Di Stefano (2017)** and modern **Gaia DR3** samples.

---

#### 2. **Physical Cause — Tidal Circularization**

Close binaries experience **tidal friction**: each star raises bulges on its companion.  
Friction within those bulges converts orbital energy into heat, draining the system’s eccentricity.

Circularization timescale roughly scales as
$$
t_{circ} \propto \left(\frac{\mathcal{a}}{R}\right)^8 \propto P^{\frac{16}{3}}
$$

so even a modest change in separation produces a huge difference in damping time.  
Systems that are young and close become circular long before wide pairs even notice tides.

---

#### 3. **Residual Eccentricities and Anomalies**

- **“Twin” binaries** (nearly equal-mass, short-period) are most circularized.
    
- **Eccentric short-period outliers** often show evidence of a **third companion** pumping eee through Kozai–Lidov cycles.
    
- **Post-mass-transfer pairs** can re-acquire modest eccentricity as mass loss changes the potential.
    

---

#### 4. **Approximate Empirical Envelope**

For solar-type primaries, the upper bound of observed eccentricities can be sketched as

$$
e_{max} \simeq 1 - \left(\frac{P_{circ}}{P}\right)^\frac{2}{3}
$$

with $P_{circ} \sim 10$ days days for main-sequence systems in the solar neighborhood.  
Beyond $P \approx 1000$ days, the envelope flattens near $e_{max} \approx 0.9$.

---

### 🧭 Summary Insight

> **Short orbits → tidal geometry dominates → circular.**  
> **Long orbits → gravitational memory dominates → eccentric.**
> 
> The period–eccentricity curve is the fossilized record of each system’s early interactions and subsequent tidal sculpting.