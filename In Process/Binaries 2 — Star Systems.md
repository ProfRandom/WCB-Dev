**Solar analog stars are more often found in binary or multiple systems than not, with over half exhibiting multiplicity.**

- **Duquennoy & Mayor (1991)** originally found that approximately **57%** of solar-type stars (spectral types F6∧K3) in the solar neighborhood are part of binary or higher-order systems.    
- **Raghavan et al. (2010)** updated this with modern data, reporting:    
    - **~44%** as binaries        
    - **~11%** as triples or higher        
    - → Yielding a total multiplicity fraction of **~55%** for solar-type stars.       

**Statistically, stars comparable to the Sun are more likely than not to belong to binary or multiple systems**—a pattern that profoundly influences system architecture, orbital stability zones, and the landscape of potential habitability.

%%***|| Add in here content about weighting the randomization toward either bound ||***%%

> > From the combined results of **Duquennoy & Mayor (1991)**, **Raghavan et al. (2010)**, **Moe & Di Stefano (2017)**, and **Li et al. (2022, LAMOST)**


Calculating a Secondary star's mass ($M_2$) based on the mass of the Primary ($M_1$):

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
### Weighted
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
#### Limiting Eccentricity ($\bar{e}$)
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
