
## Abstract  
**Major Topics:**  
- Introduces methods for **estimating the strength and extent of planetary magnetospheres** using simplified dynamo scaling laws.  
- Defines the planetary **magnetic moment (M)** as the primary parameter, derived from core radius (rc), core density (ρc), and rotation period (d).  
- Relates magnetic moment to **surface magnetic field strength (Bsurf)** through empirical scaling relations.  
- Discusses how **exponents (p, q, r)** in these formulas vary across different dynamo models (e.g., Stevenson, Driscoll & Olson).  
- Emphasizes the protective role of magnetospheres in shielding planetary atmospheres from stellar wind and cosmic radiation, with implications for long-term **habitability**.  
- Provides normalized formulas for use in worldbuilding, with Terran values as benchmarks.  

**Key Terms & Symbols:**  
- **M (Magnetic Moment):** Strength of a planet’s magnetic field.  
- **Bsurf (Surface Magnetic Field Strength):** Field strength at planetary surface.  
- **rc (Core Radius):** Planetary core radius (relative to Earth).  
- **ρc (Core Density):** Planetary core density (relative to Earth).  
- **d (Day Length):** Rotation period of the planet.  
- **p, q, r:** Exponents in dynamo scaling laws.  

**Cross-Check Notes:**  
- No duplicate abstract exists; this is the **canonical magnetosphere reference**.  
- Glossary updates required for **M, Bsurf, and dynamo scaling exponents (p, q, r)**.  
- Closely related to notes on **habitability envelopes, atmospheric retention, and stellar wind interaction**.  
---
---

# Estimating Planetary Magnetospheres

- **Magnetic moment (M)** and how it relates to $B_{surf}$    
- Empirical scaling relationships (e.g., from Stevenson or Driscoll & Olson models)    
- A simplified proportional form like:

$$
B_{surf} \propto \left(\dfrac{\rho_c}{\rho_\oplus}\right)^p \times \left(\dfrac{r_c}{r_\oplus}\right)^q \times \left(\dfrac{1}{d}\right)^r
$$

   Where:
-  $r_c$ = core radius
- $\rho_c$ = core density     
- $d$ = day length (rotation period)        
- $p, q, r$ are empirical exponents from dynamo scaling studies

This is a **scaling law approximation** from planemo dynamo theory — useful, but absolutely needing context.

 🧪 **Where This Comes From (Briefly)**

This form is adapted from scaling relations used by geophysicists and planemo scientists (e.g., Olson & Christensen, Stevenson, Driscoll & Bercovici), who try to predict magnetic field strength based on **internal structure and heat flow**.

Values of $p$, $q$, and $r$ vary depending on assumptions about:
- Core thermal convection mode (thermal vs. compositional)    
- Rotational regime (rapid vs. slow)    
- Efficiency of magnetic field generation
    
 🧭 **Rule-of-Thumb Exponent Ranges**

| Exponent | Typical Value (approx.) | Notes                                                                  |
| -------- | ----------------------- | ---------------------------------------------------------------------- |
| $p$      | ⟨1.0 ∧ 1.3⟩            | Reflects that higher-density cores produce stronger magnetic energy    |
| $q$      | ⟨2.0 ∧ 2.5⟩            | Core radius has a strong effect — bigger cores mean more dynamo volume |
| $r$      | ⟨1.0 ∧ 1.5⟩            | Faster spin increases field strength, up to saturation                 |

These aren't exact, but they give a ballpark for building **comparative models** — e.g.:

> “A world with a core 1.2× Earth’s radius, 1.1× Earth’s core density, and a 16-hour day could have a magnetic field **2–3× stronger** than Earth’s, all else equal.”

---

Or simply provide example profiles:

- Earth: ρ = 1.0⨁, d = 24h → $B_{surf}$ ∈ ⟨25 ∧ 65> μT    
- Super-Earth: ρ = 1.3⨁, d = 16h → $B_{surf}$ ∈ ⟨80 ..120⟩ μT    
- Mars: ρ = 0.71⨁, d = 24.6h → $B_{surf}$ ≈ 0 μT (solid core)