### κ (Kappa) [v1.220 NEW]  
- **Definition**: The **high temperature bound** of a stellar spectral class.  
- **Usage:**  
  - Provides the upper reference limit when calculating spectral subclasses (0–9).  
  - Used in formulae: 𝒮 = (κ – K)/þ.  
- **Cross-Check Notes:**  
  - Complements **þ (thorn)** as the class interval constant.  
  - Defines the scaling for interpolation within spectral classes.  

---

### þ (Thorn) [v1.220 NEW]  
- **Definition**: The **thermal interval constant** of a spectral class.  
- **Formula:** þ = (κ – low) ÷ 10  
- **Usage:**  
  - Defines the step size of spectral subclasses within a class.  
  - Enables interpolation between integer spectral types.  
- **Cross-Check Notes:**  
  - Works with **κ (kappa)** to provide a linearized temperature scale.  
  - Supports decimal type notation (e.g., G2.3, F3.65).  

---

### 𝒮 (Spectral Type Number) [v1.220 NEW]  
- **Definition**: Canonical WCB symbol for the **spectral subclass index** within a class (0–9).  
- **Usage:**  
  - 0 = hottest; 9 = coolest.  
  - Can take decimal values for interpolation (e.g., G2.5).  
- **Cross-Check Notes:**  
  - Supersedes earlier draft notation Ƨ.  
  - Paired with **κ** and **þ** in temperature conversion equations.  

---

### Spectral Class L [v1.220 NEW]  
- **Definition**: Stellar spectral class of ultra-cool red dwarfs and brown dwarfs.  
- **Temperature Range:** ≈ 2400–1300 K.  
- **Cross-Check Notes:**  
  - Extends main O–M sequence into cooler regimes.  
  - Often substellar; overlaps with giant planet temperatures.  

---

### Spectral Class T [v1.220 NEW]  
- **Definition**: Stellar spectral class of methane-rich brown dwarfs.  
- **Temperature Range:** ≈ 1300–700 K.  
- **Cross-Check Notes:**  
  - Defined spectroscopically by strong methane absorption bands.  
  - Bridges the gap between L dwarfs and colder Y dwarfs.  

---

### Spectral Class Y [v1.220 NEW]  
- **Definition**: Stellar spectral class of the coldest known brown dwarfs.  
- **Temperature Range:** <700 K (down to ~250 K).  
- **Cross-Check Notes:**  
  - Completes the modern spectral sequence.  
  - Includes substellar objects with temperatures comparable to planets.  
---
### Q (Stellar Lifetime) [v1.220 NEW]  
- **Definition**: Stellar lifetime, expressed in units relative to the Sun’s main-sequence lifetime.  
- **Usage:**  
  - Provides an estimate of how long a star remains stable on the main sequence.  
  - Derived from stellar mass–luminosity relations: $Q \propto M / L$.  
- **Cross-Check Notes:**  
  - Complements the five-planemo parameter set (m, r, ρ, g, vₑ).  
  - Stellar system parameters: **T primary, R secondary**, with Q as a key derivative.  

---

### ϵ (Epsilon) [v1.220 NEW]  
- **Definition**: Stellar **emissivity** — the fraction of radiation output relative to an ideal blackbody (0–1).  
- **Usage:**  
  - Corrects the blackbody assumption when calculating stellar luminosity.  
  - Applied in the Stefan–Boltzmann Law: $L = 4πR^2ϵσT^4$.  
- **Cross-Check Notes:**  
  - Typically close to 1.0 for most main-sequence stars.  
  - Introduced here as a correction factor for worldbuilding precision.  

---

### σ (Stefan–Boltzmann Constant) [v1.220 NEW]  
- **Definition**: Physical constant in the Stefan–Boltzmann Law, defining blackbody energy flux.  
- **Value:**  
  - $σ = 5.670374419 × 10^{-8} \ W·m^{-2}·K^{-4}$  
- **Usage:**  
  - Fundamental constant for computing stellar luminosity from temperature and radius.  
  - Simplifies in solar-relative equations: $L = R^2T^4$.  
- **Cross-Check Notes:**  
  - Distinguishes between the exact physical law and its normalized WCB form.  
---
### ϝ (Frost Line) [v1.220 NEW]  
- **Definition**: Orbital distance at which volatile compounds (primarily water) can no longer remain liquid, typically ~4.850𝒩.  
- **Usage:**  
  - Marks the transition between inner (temperate) and outer (icy) planetary system regimes.  
  - Sets a natural divider for planet formation: rocky worlds inside, gas/ice giants beyond.  
- **Cross-Check Notes:**  
  - Complements the **Habitable Zone Limits (H₀–H₅)**.  
  - Used in WCB as a formalized parameter, symbolized by ϝ.  

---

### Ontozones [v1.220 NEW]  
- **Definition**: Structured orbital bands defined relative to the **Nucleal Orbit (𝒩)**, classifying habitability potential around stars.  
- **Types:**  
  - Inner Xenotic, Inner Parahabitable, Inner Habitable, Hospitable, Outer Habitable, Outer Parahabitable, Outer Xenotic.  
- **Usage:**  
  - Provides a systematic orbital lexicon to replace ambiguous “inner/outer HZ” phrasing.  
  - Supports both quantitative and symbolic classification.  
- **Cross-Check Notes:**  
  - Directly builds on the **Habitable Zone Limits** system.  
  - Distinguishes between “habitable” and “hospitable” corridors.  

---

### Zone Notation ($Z_{..}$) [v1.220 NEW]  
- **Definition**: Symbolic shorthand for orbital regions relative to the Nucleal Orbit (𝒩).  
- **Notation Set:**  
  - $Z_{IX}$ — Inner Xenotic Zone (<0.500𝒩).  
  - $Z_{IP}$ — Inner Parahabitable Zone (0.500–0.750𝒩).  
  - $Z_{IH}$ — Inner Habitable Zone (0.750–0.950𝒩).  
  - $Z_H$ — Hospitable Zone (0.950–1.385𝒩).  
  - $Z_{OH}$ — Outer Habitable Zone (1.385–1.770𝒩).  
  - $Z_{OP}$ — Outer Parahabitable Zone (1.770–4.850𝒩).  
  - $Z_{OX}$ — Outer Xenotic Zone (≥4.850𝒩).  
- **Usage:**  
  - Provides compact notation for use in equations, diagrams, and comparative tables.  
- **Cross-Check Notes:**  
  - Complements **Ontozones** as the symbolic layer.  
  - Extends the HZ notation system beyond H₀–H₅.  
---
