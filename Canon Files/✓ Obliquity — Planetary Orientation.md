# Obliquity — Planetary Orientation  

## Current Obliquity (Axial tilt) ($\varepsilon$) 
Obliquity is the **instantaneous angle** between a planemo’s rotational axis and the perpendicular to its orbital plane.  An up arrow $\uparrow$ or down arrow $\downarrow$ may be appended after the angular measure to indicate whether the obliquity is increasing or decreasing.   

For Earth:  
$$
\varepsilon = 23.5^\circ\downarrow
$$
## Obliquity Envelope ($\mathcal{E}_\varepsilon$) 
$$
\mathcal{E}_\varepsilon =
\begin{bmatrix}
\varepsilon_{min} \\
\varepsilon_{mean} \\
\varepsilon_{max}
\end{bmatrix}
$$
Where:  
- $\varepsilon_x$ = current tilt angle  
- $\varepsilon_{min}$ = minimum obliquity 
- $\varepsilon_{mean}$ = mean obliquity  
- $\varepsilon_{max}$ = maximum obliquity 

Example (Earth):  
$$
\mathcal{E}_\varepsilon = 
\begin{bmatrix}
22.1^\circ \\
23.3^\circ \\
24.5^\circ
\end{bmatrix}
$$
## Obliquity Scope ($\Delta\varepsilon$)
$$
\Delta\varepsilon = \varepsilon_{max} - \varepsilon_{min}
$$
For Earth:
$$
\Delta\varepsilon = 24.5^\circ - 22.1^\circ = 2.5^\circ
$$
## Obliquity Cycle ($T_\varepsilon$) 
The time interval between two maxima (or minima) of obliquity.  

For Earth:  
$$
T_\varepsilon \approx 41{,}000 \text{ years}
$$
## Obliquity  Tempo ($\dot{\varepsilon}$) 
Rate of obliquity change per year:  
$$
\dot{\varepsilon} = \dfrac{\varepsilon_{max} - \varepsilon_{min}}{T_\varepsilon}
$$
For Earth:  
$$
\dot{\varepsilon} = \frac{24.5 - 22.1}{41000} ≈ 0.0000585^\circ/\text{yr} \;=\; 0.00585^\circ/\text{kyr}
$$
## Obliquity Phase ($\phi_\varepsilon$) 
The ratio of the current obliquity to its maximum value, expressed as a percentage, with an arrow showing whether the trend is increasing $\uparrow$ or decreasing $\downarrow$:
$$
\phi_\varepsilon = \dfrac{\varepsilon}{\varepsilon_{max}}\times 100 \; (\uparrow,\downarrow)
$$
For Earth:  
$$
\phi_\varepsilon = \dfrac{23.5}{24.5}\times 100 \approx 95.9\text{\%}\;\downarrow
$$
## Obliquity Azimuth ($\zeta_{n}$) 
The angular orientation of a planemo’s axial tilt relative to its orbit.  Defined as the angle between periapsis (the line of apsides) and the projection of the planet’s north pole on the orbital plane.  
- $\zeta_{0}$ =  (“periaptic zero”): northern solstice occurs at periastron.  
- $\zeta_{90}$ = northern solstice has precessed 90° forward along the orbit.  
- $\zeta_{180}$ =  northern solstice occurs at apastron.  
- $\zeta_{270}$=  northern solstice has precessed 270° forward along the orbit.  
- $\zeta_{n}$ advances anti-clockwise with respect to the orbit, so solstices and equinoxes **precess relative to periastron/apastron**.

- The **obliquity azimuth** precesses around the orbit, shifting the alignment of solstices and equinoxes with periastron and apastron. The **calendar seasons** remain fixed relative to equinoxes/solstices, but their **orbital context** changes over the precessional cycle.
- This precession occurs for all planets with nonzero obliquity ($\varepsilon \neq 0$).  
- The cycle is independent of tilt magnitude: even an $\varepsilon = 90^\circ$ planet precesses in the same way, with solstices tied to periastron/apastron alignment.

**Canonical Cases for $\zeta_n$​**
- $e \neq 0, \varepsilon = 0$    
    - The orbit has a defined **periastron**.        
    - There is no axial tilt, so no solstices or equinoxes exist.        
    - By convention, $\zeta_0$​ may still be defined as the direction of periastron, but it carries **no physical seasonal meaning**.
        
- $e \neq 0, \varepsilon \neq 0$    
    - The orbit has a defined periastron.        
    - The planet has tilt, so solstices and equinoxes exist.        
    - $\zeta_n$​ is measured from periastron, describing the orbital longitude where the **north pole is tilted directly away from the star**.        
        - $\zeta_0$​: that event coincides with periastron.            
        - Other $\zeta_n$​: the event occurs $n^\circ$ along the orbit from periastron.
            
- $e=0, \varepsilon \neq 0$    
    - Orbit is a perfect circle: no physical periastron exists.        
    - Solstices/equinoxes still exist because of axial tilt.        
    - In this case, **a 0° reference direction must be chosen arbitrarily** (often set by convention, e.g. “perihelion by definition”), and $\zeta_n$​ is measured relative to that.
        
- $e=0, \varepsilon = 0$    
    - No tilt, no closest approach.        
    - Neither solstices/equinoxes nor apsidal points exist.        
    - $\zeta_n$​ is undefined, unless an **arbitrary 0° longitude** is adopted purely for bookkeeping.
## Obliquity Azimuth Precession Cycle ($\chi$) 
The length of time it takes the obliquity azimuth ($\zeta_{n}$) to precess through $360^\circ$.
- Defined such that $\zeta_{0}$ occurs when the planet’s north pole is tilted **away** from the star at periastron.  
- At $\zeta_{180}$, the north pole is tilted **toward** the star at periastron.
- For Earth: $\chi ≈ 27000$ y.

Thus, for Earth in ~13,000 years, northern summer will occur near December–February if the current Gregorian framework remains in use unchanged.  

> **Note:** $χ$ is undefined for $\varepsilon = 0$, since there is no obliquity to precess. In practice, some frameworks may assign $\chi = 0$ for bookkeeping, but this has no physical meaning.

---
## Earth’s Current Seasons 
| Season | Start        | End          | Length (days) | Why length differs                  |     |
| ------ | ------------ | ------------ | ------------- | ----------------------------------- | --- |
| Spring | Mar Equinox  | Jun Solstice | 92.75         | Earth slows toward apastron         |     |
| Summer | Jun Solstice | Sep Equinox  | 93.65         | Earth slowest near apastron         |     |
| Autumn | Sep Equinox  | Dec Solstice | 89.85         | Earth accelerates toward periastron |     |
| Winter | Dec Solstice | Mar Equinox  | 88.99         | Earth fastest near periastron       |     |
