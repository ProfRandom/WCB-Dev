![[Ellipse Parameter Illustration.png]]

 # 🧭 Ellipse Geometry Solver — WBN Reference

This reference provides a complete algebraic toolkit for solving any ellipse — geometric or orbital — from any two independent parameters. All terms match the diagram above.  
## 📘 Glossary of Ellipse Parameters
  All variables match the labeled diagram above.
### 🔹 Core Axes & Foci
- **a** — semi-major axis  
- **b** — semi-minor axis  
- **c** — linear eccentricity (center to focus)  
- **e** — eccentricity (dimensionless) = $\dfrac{c}{a}$  
	  - Describes how "stretched" the ellipse is.  
		  - $e = 0$ → perfect circle  
		  - $0 < e < 1$ → ellipse  
		  - $e = 1$ → parabola (degenerate case)  
		  - $e > 1$ → hyperbola (not an ellipse)  
	- Eccentricity is **unitless** and invariant under scale.  
	-  It also defines the ellipse as a conic:   $$
  \dfrac{\text{distance to focus}}{\text{distance to directrix}} = e
$$
- **f** — flattening $b = 1 - \dfrac{b}{a}$  
- **i** — major axis $=2a$  
- **j** — minor axis $=2b$  
- **P, A** — primary vertices
- **X, Y** — co-vertices (±b along minor axis)  
- **C** — center of ellipse  
- **f₁, f₂** — the two foci  
### 🔹 Derived Lengths  
- **d** — focus-maximus = vertex to opposite focus $= a + c$  
- **g** — focus-minimus = focus to nearest vertex  $= a - c$ (e.g. $f_1P$)  
- **h** — focal span $=2c$  
- **ℓ** — semi-latus rectum $=\dfrac{1}{2} q$  
- **q** — latus rectum $= 2ℓ$
### 🔹 Directrix System  
- **m** — center-to-directrix $=\dfrac{a}{e}$  
- **n** — focus-to-directrix $=m - c$
- **s** — vertex-to-directrix $=m - a = \dfrac{c}{e} - a$  
## 🧮 Canonical Equations
### 🔹 Geometric
- $c = ae$  
- $b = a\sqrt{1 - e^2}$
- $a = \sqrt{b^2 + c^2}$
### 🔹 Orbital Geometry
- $f = a(1 - e^2) = \dfrac{b^2}{a}$  
- $r(\theta) = \dfrac{a(1 - e^2)}{1 + e \cos \theta}$  
- $r_p = a(1 - e)$ 
### 🔹 Directrix Relationships
- $m = \dfrac{a}{e}$  
- $s = m - a = \dfrac{c}{e} - a$  
- $n = m - c = \dfrac{a}{e} - c$
## 📐 What Is the Directrix?
For an ellipse, the **directrix** is:

> A fixed vertical line such that, for any point PPP on the ellipse,  
> the ratio of the distance from PPP to a **focus** and the distance from PPP to the **directrix** is equal to the **eccentricity** eee.

Formally:
$$\dfrac{\text{distance to focus}}{\text{distance to directrix}} = e$$
*This defines the ellipse!*
## 📏 Where Is the Directrix?

There are **two directrices**, one on each side of the center, at a distance:
$$m = \dfrac{a}{e}$$
… from the center, where:
- *a* is the semi-major axis    
- *e* is the eccentricity    

So:
- Right-side directrix: $x = \dfrac{a}{e}$    
- Left-side directrix: $x = -\dfrac{a}{e}$​
    If *e* → 0, the directrix moves off to infinity — which makes sense, because a circle (eccentricity 0) has no directrix-like behavior.
## 🎯 How the Directrix Relates to the Ellipse
You can think of the ellipse as a **set of points** where:
$$\dfrac{PF}{PD} = e$$
Where:
- PF is the distance from a point P on the ellipse to a **focus**    
- PD is the distance from that same point P to the **directrix**   

This definition is symmetric and constructive: it's how conics are _defined_ in classic geometry.
## 💡 So What Does It _Do_?
The directrix is mostly a **definitional and constructional tool** — not something we see in physical orbits, but:
- It gives us a clean formula for an ellipse in Cartesian coordinates:
$$r(\theta) = \dfrac{p}{1 + e \cos \theta} \quad \text{where } p = \dfrac{b^2}{a}$$
- It shows up in **ray-tracing**, **parabolic reflectors**, **classical mechanics**, and **procedural shape generation**.
## 🔍 Quick Facts

| Concept                      | Value / Equation               |
| ---------------------------- | :------------------------------: |
| Directrix location           | $x= \pm \dfrac{a}{e}$​         |
| Distance center to directrix | $m = \dfrac{a}{e}$​            |
| Distance vertex to directrix | $s = m - a = \dfrac{c}{e}-a$   |
| Distance focus to directrix  | $n = m - c = \dfrac{a}{e} - c$ |
| Eccentricity via directrix   | $e = \dfrac{PF}{PD}$​          |
## 🧩 “Given Any Two, Solve the Rest” Matrix
Each row lists two known parameters and what you can solve from them using canonical identities.

|     Known Pair     | Solve For          |                                    Method / Equation(s)                                    |
| :----------------: | :----------------: | :----------------------------------------------------------------------------------------: |
|        a, e        | b, c, f, m, s, n   | $b = a\sqrt{1 - e^2},\ c = ae,\ f = a(1 - e^2),\ m = \dfrac{a}{e},\ s = m - a,\ n = m - c$ |
| a, b               | c, e, f            |       $c = \sqrt{a^2 - b^2},\ e = \sqrt{1 - \dfrac{b^2}{a^2}},\ f = \dfrac{b^2}{a}$        |
| a, c               | b, e, m, s, n      |    $e = \dfrac{c}{a},\ b = \sqrt{a^2 - c^2},\ m = \dfrac{a}{e},\ s = m - a,\ n = m - c$    |
| b, c               | a, e               |                         $a = \sqrt{b^2 + c^2},\ e = \dfrac{c}{a}$                          |
| e, b               | a, c               |                          $a = \dfrac{b}{\sqrt{1 - e^2}},\ c = ae$                          |
| rₚ, rₐ             | a, c, e, b         | $a = \dfrac{rₚ + rₐ}{2},\ c = \dfrac{rₐ - rₚ}{2},\ e = \dfrac{c}{a},\ b = a\sqrt{1 - e^2}$ |
| a, f               | b, e               |                     $b = \sqrt{af},\ e = \sqrt{1 - \dfrac{b^2}{a^2}}$                      |
| a, m               | e, c               |                                $e = \dfrac{a}{m},\ c = ae$                                 |
| c, e               | a, b, m            |                $a = \dfrac{c}{e},\ b = a\sqrt{1 - e^2},\ m = \dfrac{a}{e}$                 |
| a, s               | m, e, c, b         |               $m = a + s,\ e = \dfrac{a}{m},\ c = ae,\ b = a\sqrt{1 - e^2}$                |
| a, n               | m, c, e, b         |              $m = n + c,\ c = m - n,\ e = \dfrac{a}{m},\ b = a\sqrt{1 - e^2}$              |
> 🔍 *Note: This matrix is designed for symbolic manipulation. Some results require substitution into multiple chained equations.*