# Calculating Stellar Sky Paths
Diurn (D): One complete 360° rotation of the planet — 
- Sidereal: around its axis relative to the inertial frame.
- Apical: around its axis relative to the sun.

Chronum (C): One complete revolution of the planet around its star — 
- Sidereal: relative to the inertial frame.
- Apical: relative to the sun.
## For any obliquity:
- The sun’s path traces an **ellipse** on the sky with:
    - **Semi-minor axis** of $\dfrac{\varepsilon_x}{2}$ (vertical extent); where $\varepsilon_x$ = the axial obliquity of the planet.
    - **Major axis** of $\large 180^\circ$ (azimuthal extent).
- Whether the sun's full path lies above the horizon depends on the observer’s **latitude ($\lambda$)** and the sun’s **declination ($\delta$)**.

---
### **Workflow for Calculating Stellar Path Parameters**

#### **Step 1: Input**
- **Obliquity ($\varepsilon_x$)**: The planet’s axial tilt.
- **Latitude ($\lambda$)**: Observer’s latitude.
- **Fraction of the apical chronum ($C_f$)**: Time since the northern hemisphere summer solstice, as a fraction of the total apical chronum ($C$).

---
#### **Step 2: Calculate the Fraction of the apical chronum ($C_f$)**

1. **What is $C$?**
   - $C$ is the total length of the planet’s apical chronum (one full cycle of the star's declination).

2. **Standard Reference Points for $C_f$:**
   - $C_f = 0$: Northern hemisphere **summer solstice**.
   - $C_f = 0.25C$: Northern hemisphere **autumnal equinox**.
   - $C_f = 0.5C$: Northern hemisphere **winter solstice**.
   - $C_f = 0.75C$: Northern hemisphere **vernal equinox**.
   - $C_f = C$: Northern hemisphere **summer solstice** (completing one full apical chronum).

3. **How to Calculate $C_f$:**
   If the current day of the apical chronum is known ($t_\text{current}$), calculate $C_f$ as:
   $$
   C_f = \frac{t_\text{current}}{C}
   $$Where:
   - $t_\text{current}$ is the number of days (or time fraction) since the summer solstice.
   - $C$ is the total length of the apical chronum.
---
#### **Step 3: Calculate Star’s Declination**
The star’s declination varies sinusoidally over the apical chronum:
$$
\delta = \varepsilon_x \cos\left(2 \pi C_f\right)
$$
---
#### **Step 4: Calculate Maximum and Minimum Altitudes**
1. **Maximum Altitude ($h_\text{max}$):**
   $$
   h_\text{max} = 90^\circ - |\lambda - \delta|
   $$
2. **Minimum Altitude ($h_\text{min}$):**
   $$
   h_\text{min} = 90^\circ - |\lambda + \delta|
   $$
---
#### **Step 5: Conditional Check**
- **If $h_\text{max} > 0^\circ$ and $h_\text{min} < 0^\circ$:**
    - The star's path intersects the horizon. **Proceed to Step 6**.
- **Otherwise, STOP:**
    - If $h_\text{min} > 0^\circ$: The star never dips below the horizon (continuous daylight).
    - If $h_\text{max} \leq 0^\circ$: The star never rises above the horizon (continuous night).

---
#### **Step 6: Calculate Center Offset ($c$)**
If the conditional in Step 5 is satisfied:
$$
c = 90^\circ - \frac{|\lambda - \delta| + |\lambda + \delta|}{2}
$$
---
#### **Step 7: Calculate Azimuthal Intersections**
For the star’s path intersections with the horizon ($y = 0^\circ$):
$$
x = \pm a \sqrt{1 - \frac{c^2}{b^2}}
$$
...where:
- $a = 180^\circ$ (semi-major axis, azimuthal extent),
- $b = \dfrac{\varepsilon_x}{2}$ (semi-minor axis, vertical extent).

---

