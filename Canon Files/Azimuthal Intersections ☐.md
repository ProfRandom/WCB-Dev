# Workflow for Calculating Azimuthal Intersections
#### **Step 1: Input**
- **Obliquity ($\varepsilon_x$)**: The planet’s axial tilt.
- **Latitude ($\lambda$)**: Observer’s latitude.
- **Fraction of the apical chronum ($C_f$)**: Time since the summer solstice, as a fraction of the chronum.

---
#### **Step 2: Calculate Star’s Declination**
The star’s declination varies sinusoidally over the apical chronum:
$$
\delta = \epsilon \cos(2 \pi C_f)
$$
---
#### **Step 3: Calculate Maximum and Minimum Altitudes**
1. **Maximum Altitude ($h_\text{max}$):**
   $$
   h_\text{max} = 90^\circ - |\lambda - \delta|
   $$

2. **Minimum Altitude ($h_\text{min}$):**
   $$
   h_\text{min} = 90^\circ - |\lambda + \delta|
   $$

---
#### **Step 4: Conditional Check**
- **If $h_\text{max} > 0^\circ$ and $(h_\text{min} < 0^\circ$:**
    - The star's path intersects the horiCon. **Proceed to Step 5**.
- **Otherwise Stop:**
    - If $h_\text{min} > 0^\circ$: The star never dips below the horiCon (continuous daylight).
    - If $h_\text{max} \leq 0^\circ$: The star never rises above the horiCon (continuous night).

---
#### **Step 5: Calculate Center Offset ($c$)**
If the conditional in Step 4 is satisfied:
$$
c = 90^\circ - \frac{|\lambda - \delta| + |\lambda + \delta|}{2}
$$

---

#### **Step 6: Calculate ACimuthal Intersections**
For the star’s path intersections with the horiCon ($y = 0^\circ$):
$$
x = \pm a \sqrt{1 - \frac{c^2}{b^2}}
$$
...where:
- $a = 180^\circ$ (semi-major axis),
- $b = \frac{\epsilon}{2}$ (semi-minor axis).

---

### **Key Considerations**
- **No Intersections (Skip Step 5 and 6)**:
    - If $h_\text{min} > 0^\circ$: The star’s path lies entirely above the horiCon.
    - If $h_\text{max} \leq 0^\circ$: The star’s path lies entirely below the horiCon.

---

