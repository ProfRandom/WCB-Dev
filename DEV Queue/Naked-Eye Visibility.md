# Naked-Eye Visibility
$$
F_{rel} = L\;R^2\left(\frac{A}{A_C}\right)\left(\frac{D_{std}}{D}\right)^4
$$
Where:
- $F_{rel}$ = dimensionless relative apparent flux (brightness ratio)- $R$ = radius of the planet in terrans
- $L$ = luminosity of the star in solar units
- $R$ = radius of the planet in terran units
- $A$ = albedo of the planet
- $A_C$​  = the albedo of the chosen standard candle
	- 0.25 — Terrestrial body
	- 0.48 — Gas giant body
- $D_{std}$ = Naked-eye visibility threshold distance in AU
	- 2 AU — Terrestrial body
	- 19 AU — Gas/ice giant body
- $D$ = Actual observer distance from the planet in AU

### Interpretation

- **$F_{rel} = 1$** → the body is *just visible* to the naked eye at the specified $D_{std}$.  
- **$F_{rel} > 1$** → the body is *brighter* (visible beyond $D_{std}$).  
- **$F_{rel} < 1$** → the body is *fainter* (would need to be closer to be seen).  
- The **$L$** term scales with the *incident stellar flux*, so worlds around dimmer stars appear proportionally fainter, and those around brighter stars proportionally brighter.  
- The **$D^{-4}$** term captures both inverse-square effects:  
  - one from the **illumination** of the planet by its star ($1/D^2$), and  
  - one from the **reflected light** spreading out toward the observer ($1/D^2$ again).  
- Together, these define a simple, dimensionless measure of apparent brightness relative to a chosen *standard candle*.

## Naked-Eye Albedo Scaling for Giant Planets
This is based on the fact that a Jupiter-sized planet becomes too dim to see with the naked eye at distances farther than 19 AU for a star with the Sun's Luminosity (L⊙).  For stars with luminosities different than the Sun's, $L$ is expressed in solar units.
$$
\begin{array}{ll}
D_{eye} = 19\;\sqrt{\dfrac{R}{11}}\;\sqrt[4]{\dfrac{A\;L}{0.48\;F_{rel}}}  &\text{Brighter albedo} \\[1em]
D_{eye} = 19\;\sqrt{\dfrac{R}{11}}\;\sqrt[4]{\dfrac{0.48\;F_{rel}}{A\;L}}  &\text{Darker albedo}
\end{array}
$$

Where:
- $D_{eye}$ = maximum distance in AU of naked-eye visibility
- $A$ = albedo of planet
- $L$ = luminosity of the star in solar units
- $R$ = radius of planet in terrans

## Naked-Eye Albedo Scaling for Terrestrial Planets
This is based on the fact that an Earth-sized planet becomes too dim to see with the naked eye at distances farther than 2 AU for a star with the Sun's Luminosity (L⊙).  For stars with luminosities different than the Sun's,  $L$ is expressed in solar units.
$$
\begin{array}{ll}
D_{eye} = 2\;\sqrt{R}\;\sqrt[4]{\dfrac{A\;L}{0.25\;F_{rel}}} & \text{Brighter albedo} \\[1em]
D_{eye} = 2\;\sqrt{R}\;\sqrt[4]{\dfrac{0.25\;F_{rel}}{A\;L}} & \text{Darker albedo}
\end{array}
$$

Where:
- $D_{eye}$ = maximum distance in AU of naked-eye visibility
- $A$ = albedo of planet
- $L$ = luminosity of the star in solar units
- $R$ = radius of planet in terrans

These relationships allow direct comparison of visibility distances for worlds of different size, albedo, and host-star luminosity under the same visual threshold $F_{rel}$​.