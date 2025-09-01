# Definition

Geotic (from Greek _Gaia_, goddess of the Earth) worlds are those which are **hospitable to humans**; humans can live there "normally" without resort to self-contained habitats or personal protection equipment such as pressure suits.

They are "Earth-like" in the basic sense of the term.  Earth, but arranged differently.  And that is the key: arrangement.  Even within the relatively limiting parameters that define a Geotic world, there is _vast_ ground for variety.

>**Keppy**: Wait...  Limiting parameters?

Good catch, Keplarius.  Yes, limiting parameters.  There are certain ranges of the physical parameters that are both conducive and comfortable for human functioning.  Here is a summary of Earth's core physical parameters — the reference standard for defining Geotics:

| Parameter                 | Value           |
| ------------------------- | --------------- |
| **Mass** (m)              | 5.972 × 10²⁴ kg |
| **Radius** (r)            | 6371 km         |
| **Density** (ρ)           | 5.514 g/cm³     |
| **Surface Gravity** (g)   | 9.8 m/sec²      |
| **Escape Velocity** (vₑ)* | 11.186 km/sec   |
\* Critical to retention of a sufficiently dense atmosphere.

In relative terms, each of these values defines a baseline of **1.000⨁** — where ⨁ indicates _Earth units_. When evaluating Geotic planemos (those broadly Earth-comparable in habitability), we consider values **within ±50% of these norms** to be within the _tolerable (or "hospitable") range_.

In other words:  A Geotic planemo should ideally fall within the range of ⟨**0.500 ∧ 1.500**⟩⨁ in mass, density, gravity, and related traits — beyond this, environmental conditions become increasingly parahabitable or hostile to unaided human life. This ±50% envelope serves as a **first-pass filter** for world plausibility, marking the physical limits of _comfortable strangeness_.

> **The Importance of Density**
> 
> In fact, _density_ is the most critical of these criteria: 
> - ρ = 0.500⨁ = 2.757 g/cm³
> 	- A planemo below this density likely has a very low metallic component. This can severely weaken (or eliminate) the generation of a magnetic field strong enough to shield the surface from harmful stellar radiation.
> - ρ = 1.500⨁ = 8.271 g/cm³. 
> 	- A planemo above this density is likely composed of significantly more metal than Earth. This often results in a **thinner mantle and crust**, which may inhibit or suppress **active tectonics** — a key mechanism in both climate regulation and long-term geochemical cycling.
> - Together, these two factors — **a stable magnetic field** and **active tectonic processes** — are vital for creating and sustaining a life-supporting planemo environment.
## Equations of State
Here is the set of equations which are used to calculate these parameters:
![[Planemo Equations of State ✓]]


This may seem daunting at first but it needn't be intimidating.
1. We use lowercase letters/symbols for planemos to avoid confusion with similar parametric nomenclature for stars (we'll get to those, never fear).
2. For planemos, any given parameter is calculated as the relationship between **two other known** parameters.
3. _If any two parameters are 1.0⨁, all the others must be as well._

Point 2, above, means that we have to start by making a decision; e.g., what mass, density, radius, etc. we want our planemo to have.  You can start with _any_ parameter, as suits your design needs; but, if you're just "throwing together a world", my recommendation is to always start with **density**, for the reasons outlined in [[#The Importance of Density]].
## A Basic Geotic Planemo
So let's start with a planemo of density ρ = 0.925⨁.  It has slightly less metallic content than Earth, but is well within our ±50% range.  What next?

> **Hippy**: We're using Earth-normal units throughout?

Great interjection, H; yes, unless otherwise specified, from here on out we're using "terran" units, denoted ⨁.   Well, we can specify an exact value for another parameter; for instance, mass m = 1.100⨁.  Now we can calculate any-and-all parameters that receive density and mass as inputs; gravity, for instance:
$$g=\sqrt[3]{\dfrac{m}{\rho^2}} = \sqrt[3]{\dfrac{1.1}{0.925^2}} = \sqrt[3]{\dfrac{1.1}{0.8556}} = \sqrt[3]{1.2856} = 1.0874\oplus$$
So far, so good; our density, mass, and gravity all fall within parameter limits:
- ρ = 0.925 ∈ ⟨0.5 ∧ 1.5⟩
- m = 1.1 ∈ ⟨0.5 ∧ 1.5⟩
- g = 1.0875 ∈ ⟨0.5 ∧ 1.5⟩

What about the radius? We have three choices for calculating radius from combinations of density, mass, andgravity, but radius from gravity and density is the most straightforward:
$$
r = \dfrac{g}{\rho} = \dfrac{1.0874}{0.925} = 1.1744\oplus 
$$
And this parameter is also within limits, so now we have:
- ρ = 0.925 ∈ ⟨0.5 ∧ 1.5⟩
- m = 1.1 ∈ ⟨0.5 ∧ 1.5⟩
- g = 1.0875 ∈ ⟨0.5 ∧ 1.5⟩
- r = 1.1744 ∈ ⟨0.5 ∧ 1.5⟩

This leaves only escape velocity.  Our choice of equations provides none as simple as the radius equation, but a couple are easier than the others: vₑ ← gravity and radius, and vₑ ← mass and radius.  Let's choose the latter:
$$
v_e = \sqrt{\dfrac{m}{r}} = \sqrt{\dfrac{1.1}{1.1744}} = \sqrt{0.9358} = 0.9673\oplus
$$
And now we have a full set of in-limit parameters:
- ρ = 0.925 ∈ ⟨0.5 ∧ 1.5⟩
- m = 1.1 ∈ ⟨0.5 ∧ 1.5⟩
- g = 1.0875 ∈ ⟨0.5 ∧ 1.5⟩
- r = 1.1744 ∈ ⟨0.5 ∧ 1.5⟩
- vₑ = 0.9673 ∈ ⟨0.5 ∧ 1.5⟩

And it's really as simple as that.  We have a planemo which is very close to Earth in all it's critical physical parameter.
# 🔺 Danger, Will Robinson!
_The Parameters Play Together — However They Like, Despite What You Might Want_

We’ve said that the “safe” range for core **Geotic parameters** is:
$$
 x \in \langle0.5 \wedge 1.5\rangle\oplus
$$
... and that's true — _for each parameter individually_.  But once you start combining them, you’re stepping into the realm of **derived parameters**.  And not all combinations play nice.

> Note: It's not necessarily that some combinations produce _physically impossible_ dependent parameters — pretty much any kind of planemo is _possible_.  It's just that *some* combinations of parameters produce _some_ **non-Geotic** dependent parameters.
## 🚨 Example: When Good Values Go Bad
Suppose we specify:
- Density: ρ = 0.500⨁
- Gravity: g = 1.500⨁

Plug these inputs into the equations of state, and out pop:
-  $v_e = \dfrac{g}{\sqrt{\rho}} = \dfrac{1.500}{\sqrt{0.500}} = \dfrac{1.500}{0.707} = 2.121\oplus$
- $r = \dfrac{g}{\rho} = \dfrac{1.500}{0.500} = 3.000\oplus$
- $m = \dfrac{g^3}{\rho^2} = \dfrac{3.375}{0.250} = \textit{13.500}\oplus$

None of these results are in the Geotic range, and check out that resultant mass!

- An escape velocity of 2.121⨁ would make leaving the planemo more difficult, but it would also better ensure retention of a life-supporting atmosphere.
- A radius of r = 3.000⨁ _might_ be justified, since radius is the most flexible of the parameters
- BUT that mass is most certainly _not_ justifiable for a Geotic world.
### 🧠 Why This Happens: Exponential Math
The equations that link escape velocity, radius, and mass are **nonlinear**:
-  $v_e = \dfrac{g}{\sqrt{\rho}}$
- $r = \dfrac{g}{\rho}$
- $m = \dfrac{g^3}{\rho^2}$
When a division is involved, as it is in _all_ of these cases, the _smaller_ the denominator, the larger the result for the same numerator.  So, a modest shift in one input can cause a **cascading blowout** in the outputs.  Welcome to the world of power laws.  In the case of *mass* we're taking an already small number (0.500) and _squaring it_ which makes it even smaller (0.250).  Dividing by ¼ is the same thing as multiplying by 4.000, so:
$$
m = \dfrac{g^3}{\rho^2} = \dfrac{3.375}{0.250} = 3.375 \times 4.000 = \it{13.500}\oplus
$$
Either the gravity needs to be lowered or the density needs to be raised.

> **Keppy**: How do we know which?

Well, we can't _know_, exactly, but we can get a hint.  Instead of just calculating one mass value, calculate all the possible mass outcomes of all combinations of the input parameters g ∈ ⟨0.500 ∧ 1.500⟩ and ρ ∈ ⟨0.500 ∧ 1.500⟩:

| m   |       |   ρ    |   ρ    |
| :-: | :---: | :----: | :----: |
|     |       | 0.500  | 1.500  |
| g   | 0.500 | 0.500  | 0.0556 |
| g   | 1.500 | 13.500 | 1.500  |
Now, we see that:
- g = 0.500; ρ = 0.500; m = 0.500
	- Mass at the minimum Geotic range
- g = 0.500; ρ = 1.500; m = 0.0556
	- Mass 0.444 below the Geotic range
- g = 1.500; ρ = 0.500; m = 13.500
	- Mass 12.0 above the Geotic range
- g = 1.500; ρ = 1.500; m = 1.500
	- Mass equals the upper bound of the Geotic range

This means that
- If we keep the gravity as originally specified (1.500⨁), _no density below 1.500⨁_ will produce a Geotic mass.
- If we keep the density as originally specified (0.500⨁), _some value for gravity between ⟨0.500 ∧ 1.500⟩⨁_ is the upper limit on gravity, **and we can calculate what that value is**.

> **Hippy**: How?

I knew you'd ask.

We know that we don't want the mass to exceed m = 1.500⨁, and we know that we want the density to be ρ = 0.5⨁, so we calculate the gravity necessary to produce these results by:
$$
g = \sqrt[3]{m \rho^2} = \sqrt[3]{1.500 \times 0.500^2} = \sqrt[3]{1.500 \times 0.250} = \sqrt[3]{0.375} = 0.721 \oplus
$$
... and now we know that for a specified density of 0.5⨁, _no gravity above 0.721⨁_ will produce a mass below the Geotic upper bound, and we already know from our table that no value for gravity below g = 0.500⨁ will produce a mass above the lower bound for Geotics... so our _permissible_ range of gravity inputs is g ∈ ⟨0.500 ∧ 0.721⟩⨁.

> **Keppy**: So, we have to abandon our original requirement of g = 1.500⨁....

> **Hippy**: Not so fast.  We should check whether we can keep gravity and flex on _density_, shouldn't we?

Nooooo... look again at the tabulation:

|  m  |       |   ρ    |   ρ   |
| :-: | :---: | :----: | :---: |
|     |       | 0.500  | 1.500 |
|  g  | 0.500 | 0.500  | 0.056 |
|  g  | 1.500 | 13.500 | 1.500 |
The last row tells us that any density ρ ≤ 1.500⨁ will produce masses m > 1.500⨁, up to m = 13.500⨁ when ρ = 0.500⨁.

∴ to get any mass m < 1.500⨁, the input density must be ρ > 1.500⨁. 

We can demonstrate this by calculating the minimum density necessary to produce m = 0.500⨁ combined with a gravity of g = 1.500⨁.  We solve for density using these two mass and gravity inputs:
- m = 0.500⨁
- g = 1.500⨁
$$
\rho = \sqrt{\dfrac{g^3}{m}} = \sqrt{\dfrac{1.500³}{0.500}} = \sqrt{\dfrac{3.375}{0.500}} = \sqrt{6.750} = 2.5981\oplus
$$
... which is 1.0981⨁ over our 0.500⨁ < ρ < 1.500⨁ limitation.

> **Keppy**: Can we stretch on the density?

Possibly; a density of basically ρ = 2.600⨁ equates to an absolute density of 14.336 g/cm³, which would indicate a _significantly_ higher planemo content of iron and other heavy metals, so there are caveats to be observed.  The [[Justifying The Geotic and Gaean Parameter Envelopes ✓]] goes into more detail, if you're interested.

[[Close-focus on Parameter Precedence ✓]]
