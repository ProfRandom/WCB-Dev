# Stellar Parametrics
In [[M002 - Stars — 01 Spectral Classes]], we covered spectral classes and spectral types and their association to the surface temperatures of stars.  Stars, like planemos, have a basic set of parameters that describe them:
- **Temperature** — How hot is the surface?
	- Absolute measure: Kelvin (K)
	- Relative measure: Solar units (T)
- **Mass** — How much material is there? (M)
- **Luminosity** — How bright is it? (L)
- **Radius** — How big is it? (R)
- **Lifetime** — How long does it shine? (Q)
	- Chiefly relevant to _Main Sequence_ stars, particularly stars that are **Solar Cognates** (more on this below.)

> Notes:
> 1. Where we use lower-case letters for the parameters of planemos, we use upper-case letters for stars, so it's easy to tell them apart.
> 2. While **mass** (*m*) is the primary parameter for planemos, with **density** (*ρ*) secondary, for stars **Temperature** (*T*) is the primary parameter, and **radius** (*R*) is secondary.
> 	- While luminosity is **technically derived** from a star's temperature and radius (see *the Stefan-Boltzmann Law*, below), it plays a **central role** in modeling stellar systems — particularly when calculating orbit distances, habitable zones, and irradiance. In practice, it’s often treated as the secondary parameter after termperature for thesisastics.
## Equations of State
A regularized set of empirical relationships can be used to estimate any stellar parameter from the others — assuming a Main Sequence **blackbody**-like star (see [[Sidebar — What Is The Main Sequence]]).

> **Keppy**: And a **blackbod**y is...?

Excellent question!  A **blackbody** is an **idealized physical object** that:
1. **Absorbs all** incoming electromagnetic radiation — no reflection, no transmission.    
2. **Emits radiation** purely based on its temperature — not its material, shape, or color.    
3. Emits a **perfectly smooth, continuous spectrum** (a "thermal spectrum").
In short:
> A blackbody is the theoretical gold standard for radiant heat emission — a perfect radiator and absorber.
#### Why "Blackbody" Matters Here
Most stars (especially Main Sequence stars) behave **approximately like blackbodies**, meaning their energy output can be modeled using **temperature alone**. This makes them excellent candidates for:
- **Temperature-based modeling**    
- **Color-temperature mapping** (blue = hotter, red = cooler)    
- **Spectrum-based classification** (like spectral classes O–M)
- Real-World Deviation
	- planemos, dust clouds, and even stars aren’t _perfect_ blackbodies.
	- Real objects have an **emissivity** ϵ between 0 and 1:
$$ F = \varepsilon \sigma T^4$$
- But stars are close enough that the **blackbody approximation works very well**.

> **Hippy**: Sorry you asked, Keplarius?

Yes, that's a bit technical and complicated, but it's also extremely _important_ to what comes next.

Here are the promised equations:

![[Standard Stellar Equations of State ✓]]

> > **NOTE**:
> > All of the above equations are _approximations_; stars are a much more variable set of objects (after all, they're mostly gas and plasma, so fluid dynamics plays a major role in their characteristics).  These equations work **best _in general_ for main sequence stars** of all classes.

> **Keppy**: You said Luminosity was the second most important parameter for stars, but it doesn't appear in the table...?

Well spotted, Keppy!  There's a reason.
### The Stefan-Boltzmann Law
The Stefan-Boltzmann Law is a formulation that relates the **luminosity** of any luminous object to its **temperature** and **surface area**:
$$
L = 4 \pi R^2 \sigma T^4
$$
Where:
- 4πR²  = the surface area of the body
- T = is the temperature of the body in Kelvin
- σ = the Stefan-Boltzmann constant
	- $\sigma = 5.670374419 \times 10^{-8} W m^{-2}K^{-4}$
		- **Watts** per square meter per Kelvin to the fourth power 1 K⁴
		- It tells you how much **radiant energy per second** (i.e., power) is emitted by a **1 square meter** portion of a **perfect blackbody** at **1 K⁴**.

And this is why we needed the quick aside into the term "blackbody" earlier.

In thesiastics terms, we can simplify the Stefan-Boltzmann equation to:
$$
\dfrac{L_s}{L_{Sun}} = \left(\dfrac{R_s}{R_{Sun}}\right)^2 \left(\dfrac{K_s}{K_{Sun}}\right)^4
$$
Where:
- $L_S$ = the absolute luminosity of the star
- $L_{Sun}$ = the absolute luminosity of the Sun
- $R_S$ = the absolute radius of the star
- $R_{Sun}$ = the absolute radius of the Sun
- $K_S$ = the Kelvin temperature of the star
- $K_{Sun}$ = the Kelvin temperature of the Sun

Because the form $\dfrac{X_s}{X_{Sun}}$ is the standard for converting a parameter to solar units, and $T = \dfrac{K_s}{K_{Sun}}$, this equation becomes:
$$
\begin{align}
L &= R^2T^4, \qquad \text{with derivations of} \\ \\
R &= \dfrac{\sqrt{L}}{T^2}, \qquad
T = \sqrt[4]{\dfrac{L}{R^2}}
\end{align}
$$
## Parameter Calculation Precedence
The above being the case, there is a "best" order for calculating stellar parameters when starting from any given parameter (though it is always best start with *K* or *T* whenever possible).
> All parameters (except K) are expressed in Solar-relative units; that is, T = 1⊙ for 5800 K, R = 1⊙ for the solar radius, etc.
#### Starting with Temperature (*T*) or (*K*)
**Primary dependency chain**: T/K → R → L → M → Q
$$
\begin{gather}
T = \dfrac{K}{5800} \quad or \quad K = 5800T \\
R = T^{1.8} \\
L = R^2T^4 \\
M = T^{1.98} \quad or \quad M = \sqrt[0.9]{R} \\
Q = T^{-5} \quad or \quad Q = M^{-2.5}
\end{gather}
$$
#### Starting with Mass (*M*)
**Primary dependency chain**: M → T/K → R → L → Q
$$
\begin{gather}
T = \sqrt[1.98]{M} \\
K = 5800T \\
R = T^{1.8} \quad or \quad R = M^{0.9} \\
L = R^2T^4 \\
Q = T^{-5} \quad or \quad Q = M^{-2.5}
\end{gather}
$$
#### Starting with Radius (*R*)
**Primary dependency chain**: R → T → K → L → M → Q
$$
\begin{gather}
T = \sqrt[1.8]{R} \\
K = 5800T \\
L = R^2T^4 \\
M = T^{1.98} \\
Q = T^{-5} \quad or \quad Q = M^{-2.5}
\end{gather}
$$
#### Starting With Luminosity (*L*)
**Primary dependency chain**: L → T → K → R → M → Q
$$
\begin{gather}
T = \sqrt[7.6]{L} \\
K = 5800T \\
R = T^{1.8} \\
M = T^{1.98} \\
Q = T^{-5} \quad or \quad Q = M^{-2.5}
\end{gather}
$$
#### Starting with Lifetime (*Q*)
\**As soon as you assume you'd never want to do this, you'll find a case for doing it.*\*
**Primary dependency chain**: Q → T → K → R → L → M
$$
\begin{gather}
T=Q^{-0.2} \\
K = 5800T \\
R=Q^{-0.36} \\
L = R^2T^4 \\
M = \sqrt[3]{L}
\end{gather}
$$      
