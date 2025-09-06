## Tilt (Obliquity: $\epsilon$)
#### Notation
$$
\dot{T} = (\epsilon \pm : \epsilon^-, \epsilon^0, \epsilon^+)
$$
Where
 - $\epsilon$ = the current degree measure of the axial tilt
	 - $\pm$ = the trend of the tilt shift
	 - $+$ = the tilt angle is _increasing_ toward maximum
	 - $-$ = the tilt angle is _dereasing_ toward minimum
 - $\epsilon^-$ = the minimum tilt angle in degrees
 - $\epsilon^0$ = the mean (average) tilt angle in degrees
 - $\epsilon^+$ = the maximum tilt angle in degrees

Example (for Earth):
$$
\dot{T} = (23.5^\circ-: 22.1^\circ, 23.32^\circ, 24.5^\circ)
$$
- Current tilt angle: $23.5^\circ-$, and _decreasing_
- Minimum tilt angle: $22.1^\circ$
- Mean tilt angle: $23.3^\circ$
- Maximum tilt angle: $24.5^\circ$
## Tilt Oscillation ($T’$)
The interval of oscillation between two occurrences of the maximum or the minimum axial tilt
Example (for Earth):
$$
T’ = 41000^y
$$
## Tilt Rate of Change ($\dot{T}_{rate}$)

The rate of change of the axial tilt per year[^1]
$$
\dot{T}_{rate} = \pm\dfrac{\epsilon^+ - \epsilon^-}{T\prime}
$$
Example (for Earth):
$$
\dot{T}_{rate} = \pm\dfrac{24.5^\circ - 22.1^\circ}{41000} = \pm0.000058537^\circ / year; $\pm0.0058537^\circ$ / kyr
$$
## Tilt Current Status ($\dot{T}_{cur}$)
The current percentage of maximum tilt
$$
\dot{T}_{cur} = \dfrac{\epsilon\pm}{\epsilon^+} \times 100
$$

Example (for Earth):
$$
	\dot{T}_{cur} = \dfrac{\epsilon}{\epsilon^+} \times 100 = \dfrac{23.5-}{24.5} \times 100 = 95.918\%-
	$$
- $95.918\%$ of maximum tilt and _decreasing_)

## Precession Cycle (ⲯ)

The $\psi = 0^\circ$ direction of the precessional phase is defined as the northern hemisphere of the planet being tilted precisely *away* from the star at the perihelion of its orbit.

The precessional phase follows an anticlockwise circuit such that at $\psi = 180^\circ$ the northern hemisphere of the planet it tilted precisely _toward_ the star at perihelion.

Thus the _seasons precess through the calendar_, while the phase orientation remains static.  This means that at $\psi = 180°$ for Earth, northern _summer_ will be occurring in the December, January, February timeframe, _if the Gregorian calendar is still in use and hasn't been adjusted from its current configuration._

This is the _planetary gyre cycle_ for _all planets with a non-zero obliquity, _regardless of whether the tilt angle also shifts_.  However, if the plaent's orbit is perfectly circular, then "perihelion" simply becomes the term for when the planet is at the $0^\circ$ point its orbital path relative to the objective frame, because it won't be any closer-to or farther-from its star at that point than at any other point in its orbit.

The planetary gyre cycle is also independent of the magnitude of the axial tilt.  A planet with a $90^\circ$ obliquity, no tilt variation, and a non-zero orbital eccentricity is still experiencing $\psi = 0^\circ$ at perihelion, except that the north pole is pointing directly at the star and the planet's axis is colinear with a line connecting the center of the star with the center of the planet.
## Orbital Eccentricity and Seasonal Effects
For a planet with semimajor axis *a* and eccentricity *e*:
- **Perihelion distance**:  
$$
r_p = a (1 - e)
$$
- **Aphelion distance**:
$$
r_a = a (1 + e)
$$

---

### Distance Difference
The fractional difference in distance between perihelion and aphelion is:

$$
x = \frac{1+e}{1-e} - 1 = \frac{2e}{1-e}
$$

- Earth ($e = 0.0167$):  
  $x \approx 0.034 $ → **3.4% closer at perihelion**  
- Rosetta ($e = 0.05$):  
  $x \approx 0.105 $ → **10.5% closer at perihelion**

---

### Insolation (Flux) Difference
Since flux ∝ $1/r^2$, the perihelion/aphelion flux ratio is:

$$
\frac{F_p}{F_a} = \left(\frac{1+e}{1-e}\right)^2
$$
- Earth ($e = 0.0167$):  
  $\dfrac{F_p}{F_a} \approx 1.068$ → **6.8% stronger insolation at perihelion**  
- Rosetta ($e = 0.05$):  
  $\dfrac{F_p}{F_a} \approx 1.23$ → **23% stronger insolation at perihelion**

---

### WCB Note
- **Distance form** → good for intuitive “how much closer/farther” language.  
- **Flux form** → good for climatic impact (“how much hotter/colder”).  
- Both are simple, memorable shortcuts for estimating seasonal asymmetry.


## Spin ($S_{sid}$)
### (Sidereal Day)

The planet's period of rotation around its axis.
#### Notation: $D_{sid}; {}^{ds}$
	
Example (for Earth):

- $1^{ds} = 23^h\; 56^m\; 04^s$
## Apical Day

The time between two instances of the star crossing the variable apex of its path across the sky as seen by any planet-bound observer.0
#### Notation: $D; {}^d$

Example (for Earth):

- $1^d = 24^h$
- Note: for Earth this is also known as the _apparent solar day_ or the _ephemeris day_.
### Sidereal year

The time for the planet to complete one full orbit around its star relative to the objective frame.
#### Notation: $Y; {}^y$

Example (for Earth):
- $1^y = 365.256363004^d$; where $d$ is the local _apical day_.
### Zenithal Year

The time between two instances of the star passing the highest apex of its path across the sky as seen by any planet-bound observer.
#### Notation: $Z; {}^z$
	
Example (for Earth):

- $1^z = 365.24219^d$; where $d$ is the local _apical day_.

[^1]: Usually expressed in Terran years

# Earth's Seasons

| Season  | Start             | End               | Approximate Length | Reason for length difference                                                                                                |
|---------|-------------------|-------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Spring  | March Equinox     | June Solstice     | 92.75 days         | Earth's speed is decreasing as it moves toward its farthest point from the sun (aphelion).                                  |
| Summer  | June Solstice     | September Equinox | 93.65 days         | Earth is moving slowest in its orbit during this time, so it takes longer to travel through this arc.                       |
| Autumn  | September Equinox | December Solstice | 89.85 days         | Earth's speed is increasing as it moves toward its closest point to the sun (perihelion).                                   |
| Winter  | December Solstice | March Equinox     | 88.99 days         | Earth moves fastest in its orbit during this period, covering the required orbital distance in the shortest amount of time. |
