## Abstract
**Major Topics:**  
- Five core planemo parameters: mass (m), density (ρ), surface gravity (g), escape velocity (vₑ), and radius (r).  
- Distinction between **physical properties** (m, ρ) and **emergent properties** (g, vₑ, r).  
- WCB convention: density (ρ) treated as **uncompressed density** to avoid recursive modeling.  
- Symbolic precedence hierarchy:  
  1. Mass (m), Uncompressed Density (ρ) — composition-driven.  
  2. Surface Gravity (g), Escape Velocity (vₑ) — experiential.  
  3. Radius (r) — emergent.  
- Validation: computed values for g, vₑ, and r from Geotic-range m and ρ remain within acceptable Geotic bounds.  

**Key Terms & Symbols:**  
- m = mass.  
- ρ = uncompressed density.  
- g = surface gravity.  
- vₑ = escape velocity.  
- r = radius (emergent).  
- Geotic range: ⟨0.5 ∧ 1.5⟩⨁.  
- Order of calculation: begin with m and ρ for valid outputs.  

**Cross-Check Notes:**  
- Canonical clarification: radius (r) is *not* arbitrarily chosen — it emerges from m and ρ.  
- Replaces recursive compression modeling with a WCB-friendly simplification.  
- Geotic range justification links to habitability framework.  
- Integrates with prior note **Example: When Good Values Go Bad** (edge-case validation).  
- Ensure consistent update: “WCB” → “WCB” across this file and related notes.  

---
---


# Close-focus on Parameter Precedence
Elsewhere, I stated that

> "Radius is an _emergent property — the most flexible of the five core planemo parameters*."

Here, we learn _why_ that's the case.

WCB defines five core parameters for modeling planemos:
- Mass (m)
- Density (ρ)
- Surface Gravity (g)
- Escape Velocity (vₑ)
- Radius (r)

## Physical vs Emergent Properties
The first two — **mass** and **density** — are fundamental **physical properties**. If an object is composed of a specific material (e.g., pure iron), then:
- Its **density** reflects the compactness of that material under standard conditions.    
- Its **mass** is the product of that density and volume.
These values are not “fuzzy” — they are _determined_ by composition. But there’s a complicating factor:

### Uncompressed Density in WCB
In reality, high-mass planemos **compress themselves** under their own gravity. This self-compression:
- Increases core pressure    
- Reduces actual volume    
- Nudges the average (measured) density _upward_
Unfortunately, the feedback between mass, gravity, and compression is:
- This feedback loop is **nonlinear**    
- The corrections vary by **material type**    
- And modeling it accurately requires **complex equations of state**
WCB intentionally avoids this complexity in favor of **practical worldcrafting**.

> **WCB Convention:**  
> We treat _ρ_ (density) as the **uncompressed density** of the planemo — the intrinsic density of its materials assuming no internal gravitational compression.

This keeps _ρ_ symbolically **independent** from _m_ and allows us to calculate _r_, _g_, and _vₑ_ without recursive modeling.  Compression effects are minimal within the Geotic range ⟨0.5 ∧ 1.5⟩⨁, so this simplification is physically tolerable and worldcrafter-friendly.

### Parameter Precedence: A Symbolic Hierarchy
In WCB, we adopt a symbolic precedence system to clarify **what depends on what**.
#### First Precedence: Composition-Driven Parameters
- **Mass** (_m_)    
- **Uncompressed Density** (_ρ_)
These are **primary constraints**, based on:
- Material class    
- Planetary category    
- Biospheric plausibility    
- Narrative or symbolic intention 
#### Second Precedence: Experiential Parameters
- **Surface Gravity** (_g_)    
- **Escape Velocity** (_vₑ_)
These depend on _m_ and _ρ_, and describe how a being would **experience** the world. They answer:
- _“How heavy do things feel?”_    
- _“How hard is it to launch something into space?”_
Because they’re **experiential**, _g_ and _vₑ_ serve as **thresholds for habitability** and **filters for narrative design**.

> For writers of SF, escape velocity might be of slightly greater import, as they are often more concerned with getting characters out of the planemo's gravity well.
#### Third Precedence: Emergent Parameter
- **Radius** (_r_)
We treat radius as an **emergent quantity**, derived from the interplay between _m_ and _ρ_. Once those are specified, _r_ is computed using:
$$
\begin{align}
r &= \sqrt[3]{\frac{3 m}{4 \pi \rho}} &&\qquad \text{Absolute Calculation} \\
r &= \sqrt[3]{\frac{m}{\rho}} &&\qquad \text{Relative calculation}
\end{align}
$$
By defining _ρ_ as uncompressed, we sidestep recursive compression modeling and free _r_ to play its proper role as a derived result.

> **In short:** Radius is not arbitrarily assigned in WCB — it emerges from first principles, and that’s exactly what gives it flexibility.

However, if a planemo meets all other Geotic criteria but falls slightly outside the ⟨0.5 ∧ 1.5⟩⨁ radius guideline, **there is room for flex** — especially when symbolic or experiential factors support it.
### Surface Gravity, Escape Velocity, and Radius "Flexibility"
We maintain the general **Geotic envelope** of ⟨0.5 ∧ 1.5⟩⨁ for all five core parameters. However — as discussed in **Example: When Good Values Go Bad** — not all combinations of any two parameters will yield outputs that remain Geotic.

To test this, we evaluated all combinations of **mass** (_m_) and **uncompressed density** (_ρ_) within the Geotic range (⟨0.5 ∧ 1.5⟩⨁), using an increment of 0.05⨁ for each. From these, we calculated the corresponding:
- **Surface Gravity** (_g_)    
- **Escape Velocity** (_vₑ_)    
- **Radius** (_r_)

 #### Results from Evaluated Combinations:
- **Gravity** (_g_) — derived from _m_ and _ρ_:    
    - All values fell within the expected ⟨0.5 ∧ 1.5⟩⨁ range.        
- **Escape Velocity** (_vₑ_) — derived from _m_ and _ρ_:    
    - Calculated range was ⟨0.7071 ∧ 1.2247⟩⨁.        
- **Radius** (_r_) — derived from _m_ and _ρ_:    
    - Calculated range was ⟨0.6934 ∧ 1.4423⟩⨁.
**Conclusion:**  
All outputs for _g_, _vₑ_, and _r_ computed from Geotic-range values of _m_ and _ρ_ **remain within or closely near** the ⟨0.5 ∧ 1.5⟩⨁ constraint window.

> **Reminder:**  
> While _mass_ and _density_ serve as **primary constraints**, the values they generate for _gravity_, _escape velocity_, and _radius_ are **emergent** — and may push right up to the edges of Geotic acceptability. Planemos with marginal values on one or more of these outputs may still qualify symbolically, depending on biospheric or narrative justification.

## Order of Parameter Calculation
WCB allows you to begin with **any two** of the five core planemo parameters and calculate the remaining three. For example:
- You might specify a desired **gravity** (_g_) and **radius** (_r_) to match narrative or symbolic needs — and then calculate **mass**, **density**, and **escape velocity** from those.
However:

> ⚠️ **Caution:**  
> **Mass** (_m_) and **uncompressed density** (_ρ_) are treated as **inflexible physical constraints** in WCB. They must fall within the Geotic envelope ⟨0.5 ∧ 1.5⟩⨁ to yield plausibly habitable worlds.

### WCB Recommendation
> **Start with mass and uncompressed density.**  
> These two parameters:> 
> - Reflect the physical composition of your planemo
> - Are symbolically independent
> - Guarantee valid outputs for _g_, _vₑ_, and _r_ if kept within the Geotic range    

By anchoring your model in _m_ and _ρ_, you ensure that all derived parameters remain within acceptable bounds — streamlining your creative process and avoiding invalid combinations.