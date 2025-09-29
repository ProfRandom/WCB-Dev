# Workflow for Calculating Azimuthal Intersections
#### **Step 1: Input**
- **Obliquity ($\varepsilon_x$)**: The planet’s axial tilt.
- **Latitude ($\lambda$)**: Observer’s *latitude*, degrees north or south of the equator.
- **Fraction of the apical chronum ($C_f$)**: Time since the summer solstice, as a fraction of the chronum.

---
#### **Step 2: Calculate Star’s Declination**
Over the course of the apical chronum, a star’s declination shifts north and south of the celestial equator in a sinusoidal pattern. This north–south swing is what causes the east–west drift of the star’s rising and setting azimems along the horizon.
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
#### **Step 4: Condition Check**
- **If $h_\text{max} > 0^\circ$ and $h_\text{min} < 0^\circ$:**
    - The star's path intersects the horizon. **Proceed to Step 5**.
- **Otherwise Stop:**
    - If $h_\text{min} > 0^\circ$: The star never dips below the horizon (continuous daylight).
    - If $h_\text{max} \leq 0^\circ$: The star never rises above the horizon (continuous night).

---
#### **Step 5: Calculate Center Offset ($altitudem$)**
If the condition in Step 4 is satisfied:
$$
\text{altitudem} = 90^\circ - \frac{|\lambda - \delta| + |\lambda + \delta|}{2}
$$

---

#### **Step 6: Calculate the Azimuthal Angle and Azimems**
For the star’s path intersections with the horizon ($y = 0^\circ$):
$$
\begin{gather}
Z = \text{ Azimuthem } \cdot \sqrt{1 - \left(\frac{\text{Altitudem}}{\text{Obliquem}}\right)^2} \\
Z_e = +Z \quad\text{;}\quad Z_w = -Z
\end{gather}
$$
...where:
- $Azimuthem$ = the great-circle line that connects due east to due west through the observer’s position (passing through the zenith and nadir). Its angular measure is always $180^\circ$.
- $Altitudem$ = the altitude of the ellipse's center relative to the horizon.
- $Obliquem$ = half the angular measure of the planet's obliquity $\left(\dfrac{\varepsilon_x}{2}\right)$
- $Z$ = the azimuthal angle magnitude between due north and the horizon-intersection of either the rising or setting of a star's path
	- $Z_e$ = the east *Azimem*; the angle from due north along the eastern horizon line at which the star's path intersects the eastern horizon.
	- $Z_w$ = the west *Azimem*; the angle from due north along the western horizon line at which the star's path intersects the western horizon.

---

### **Key Considerations**
- **No Intersections (Skip Step 5 and 6)**:
    - If $h_\text{min} > 0^\circ$: The star’s path lies entirely above the horizon.
    - If $h_\text{max} \leq 0^\circ$: The star’s path lies entirely below the horizon.

---

