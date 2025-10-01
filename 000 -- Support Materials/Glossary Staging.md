## 📑 v1.221 Staging Set (with Lexicon Tags)

### 🆕 New Entries  
- **Igniozone [NEW]** — innermost thermozone, beginning at ~0.5𝒩; “fiery zone.” *(Neolex, corridor term)*  
- **Calorozone [NEW]** — hot orbital band beyond the Igniozone; uninhabitable. *(Neolex, corridor term)*  
- **Heliozone [NEW]** — transitional band inside Solarazone. *(Neolex, corridor term)*  
- **Solarazone [NEW]** — thermozone containing the Nucleal Orbit (𝒩); flux-equivalence benchmark. *(Neolex, corridor term)*  
- **Hiberozone [NEW]** — cooler corridor beyond Solarazone. *(Neolex, corridor term)*  
- **Brumazone [NEW]** — more distant, midwinter-like orbital band. *(Neolex, corridor term)*  
- **Cryozone [NEW]** — outermost, frigid thermozone. *(Neolex, corridor term)*  
- **Thermozone Limit Notation (H₀–H₅) [NEW]** — standardized subscripts for thermozone cutoffs (0.5𝒩 through 4.85𝒩). *(Neolex, symbolic system)*  

---

### 📌 Totals So Far for v1.221  
- **Updated entries**: 0  
- **New entries**: 8  
- **Old Lexicon Remnants**: 0  
- **Total staged**: 8  

- **Neolexes (symbols/terms)**: 8  
- **Exolexes (adopted astrophysical/physical terms)**: 0  
- **Insulexes**: 0  
---
### Perannual Orbit (𝒫) [v1.221 NEW]  
- **Definition:** The orbital distance around a star at which a planemo completes exactly one Earth sidereal year (365.256363 ephemeris days).  
- **Formula:**  
  - General: $\mathcal{P} = \sqrt[3]{M+m}$  
  - Simplified (ignoring planemo mass): $\mathcal{P} = \sqrt[3]{M}$  
- **Usage:**  
  - Serves as a **temporal benchmark**, anchoring orbital period relative to Earth’s year.  
  - Contrasts with **Nucleal Orbit (𝒩)**, which is irradiance-based.  
- **Cross-Refs:**  
  - Related terms: **Intranucleal, Extranucleal**.  
  - Links to *Stars 06* (relations between 𝒩 and 𝒫).  

---

### Intranucleal [v1.221 NEW]  
- **Definition:** Describes a perannual orbit (𝒫) that lies **inside** the nucleal orbit (𝒩).  
- **Usage:** Identifies stellar systems where orbital timing (𝒫) is shorter than the irradiance-defined flux equivalence (𝒩).  
- **Cross-Refs:** **Perannual Orbit (𝒫), Nucleal Orbit (𝒩), Extranucleal.**  

---

### Extranucleal [v1.221 NEW]  
- **Definition:** Describes a perannual orbit (𝒫) that lies **outside** the nucleal orbit (𝒩).  
- **Usage:** Identifies stellar systems where orbital timing (𝒫) is longer than the irradiance-defined flux equivalence (𝒩).  
- **Cross-Refs:** **Perannual Orbit (𝒫), Nucleal Orbit (𝒩), Intranucleal.**  
---
### Solar Analog [v1.221 NEW]  
- **Definition:** A star whose perannual orbits span the full **Parahabitable Zone** (H₀–H₅), from 0.500–4.850 AU.  
- **Spectral Range:** F2–K9.  
- **Usage:** Broadest category of Sun-like stars in WCB; includes Solar Cognates and Solar Twins.  
- **Cross-Refs:** **Solar Cognate, Solar Twin, Perannual Orbit (𝒫), Thermozones (H₀–H₅).**  

---

### Solar Cognate [v1.221 NEW]  
- **Definition:** A star whose perannual orbits span the full **Habitable Zone** (H₁–H₄), from 0.750–1.770 AU.  
- **Spectral Range:** F7.62–K1.11.  
- **Usage:** Subset of Solar Analogs; includes Solar Twins.  
- **Cross-Refs:** **Solar Analog, Solar Twin, Habitable Zone, Perannual Orbit (𝒫).**  

---

### Solar Twin [v1.221 NEW]  
- **Definition:** A star whose perannual orbits span the **Hospitable Zone** (H₂–H₃), from 0.950–1.385 AU.  
- **Spectral Range:** G1.04–G7.73.  
- **Usage:** Most restrictive Sun-like category in WCB; nested within Solar Cognates.  
- **Cross-Refs:** **Solar Analog, Solar Cognate, Hospitable Zone, Perannual Orbit (𝒫).**  

---

### Orbital Habitability Index (OHI) [v1.221 NEW]  
- **Definition:** A scalar index (0.00–1.00) expressing relative habitability of an orbit based on its distance from the **Nucleal Orbit (𝒩)**.  
- **Formula:**  
  - $OHI = 1 - \dfrac{|D - 𝒩|}{(H₀–H₅ \text{ limit distance})}$  
  - Piecewise: separate treatments for intranucleal vs. extranucleal cases.  
- **Usage:**  
  - $OHI = 1.00$ at $D = 𝒩$.  
  - $OHI = 0.00$ at thermozone limits (H₀ or H₅).  
- **Cross-Refs:** **Nucleal Orbit (𝒩), Perannual Orbit (𝒫), Thermozones (H₀–H₅).**  
---
### Orbital Interval (I) [v1.221 NEW]  
- **Definition:** Ratio of successive orbital distances.  
- **Formula:** $I = O_n / O_{n-1}$  
- **Usage:** Used to measure and generate spacing between planemo orbits.  
- **Cross-Refs:** **Orbital Gap, Basal Orbit, Intrabasal, Extrabasal.**  

---

### Orbital Gap (G) [v1.221 NEW]  
- **Definition:** Difference between successive orbital distances.  
- **Formula:** $G = O_n - O_{n-1}$  
- **Usage:** Provides linear measure of spacing between adjacent orbits.  
- **Cross-Refs:** **Orbital Interval, Basal Orbit.**  

---

### Intrabasal Orbit Calculation [v1.221 NEW]  
- **Definition:** Process of generating **inward orbits** by dividing a chosen base orbit radius by an orbital interval.  
- **Usage:** Creates inner system orbits relative to a basal orbit (𝒩, 𝒫, etc.).  
- **Cross-Refs:** **Extrabasal, Basal Orbit, Orbital Interval.**  

---

### Extrabasal Orbit Calculation [v1.221 NEW]  
- **Definition:** Process of generating **outward orbits** by multiplying a chosen base orbit radius by an orbital interval.  
- **Usage:** Creates outer system orbits relative to a basal orbit (𝒩, 𝒫, etc.).  
- **Cross-Refs:** **Intrabasal, Basal Orbit, Orbital Interval.**  

---

### Basal Orbit (B) [v1.221 NEW]  
- **Definition:** A chosen anchor orbit from which other orbital distances are generated inward or outward.  
- **Examples:** Nucleal Orbit (𝒩), Perannual Orbit (𝒫).  
- **Cross-Refs:** **Intrabasal, Extrabasal, Orbital Interval, Orbital Gap.**  

---

### Ω (Omega) [v1.221 NEW]  
- **Definition:** Symbol representing the **system cutoff distance**: either the innermost safe orbit or the outer limit of stable orbits.  
- **Usage:** Defines the effective bounds of a star system for orbit generation.  
- **Cross-Refs:** **Basal Orbit, Intrabasal, Extrabasal.**  
---
### Δ (Delta) [v1.221 NEW]  
- **Definition:** Symbol representing the relative distance offset between the **Perannual Orbit (𝒫)** and the **Nucleal Orbit (𝒩)**.  
- **Formula:** $\Delta = \dfrac{𝒫}{𝒩}$  
- **Usage:** Expresses how far inward or outward the perannual orbit lies compared to the nucleal orbit.  
- **Cross-Refs:** **Perannual Orbit (𝒫), Nucleal Orbit (𝒩).**  

---

### F (Flux) [v1.221 NEW]  
- **Definition:** Relative stellar irradiance at a given orbital distance, normalized to 1.0 at the **Nucleal Orbit (𝒩)**.  
- **Formula:** $F = \dfrac{L}{D^2}$ (in ⊙-relative units, scaled to flux at 𝒩).  
- **Usage:**  
  - $F = 1.0$ at 𝒩 by definition.  
  - Used to compare flux received at perannual orbits and other orbital distances.  
- **Cross-Refs:** **Nucleal Orbit (𝒩), Perannual Orbit (𝒫), Orbital Habitability Index (OHI).**  
