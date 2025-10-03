
## Abstract  
**Major Topics:**  
- Establishes a **symbolic system** for generating orbital radii procedurally via multiplicative steps.  
- Defines **intrabasal** (inward from baseline) and **extrabasal** (outward from baseline) orbit generation.  
- Uses **basal orbital radius (B)** and **system cutoff (Ω)** as anchors, with optional use of nucleal orbit (𝒩) as B.  
- Expresses orbital placement through **randomized multiplicative factors** (⟨⟨min ∧ max⟩⟩).  
- Describes strategies: outward-only, inward-only, or bidirectional scaffolding from a central anchor.  

**Key Terms & Symbols:**  
- **Intrabasal [EXPANDED neo]:** Now canonized as any orbit inside a basal reference (broader than just calculations).  
- **Extrabasal [EXPANDED neo]:** Any orbit outside a basal reference.  
- **B (Basal orbital radius) [NEW ins].**  
- **Ω (System cutoff) [NEW ins].**  
- Random assignment operator (⟨⟨ ⟩⟩) [ins].  

**Cross-Check Notes:**  
- **[EXPANDED]** Intrabasal/Extrabasal promoted from calculation-only to general relational terms.  
- **[NEW]** Basal radius (B) and cutoff (Ω).  
- No conflicts with existing canon.  
- Extends *Range Constraints & Random Assignment*; best read together.  
---
---


# Orbit Randomization Notation
This symbolic system defines how to procedurally generate a sequence of orbital radii using randomized multiplicative (or divisive) steps from a baseline (**basal**) value. It distinguishes between **intrabasal** (moving inward) and **extrabasal** (moving outward) orbit generation.

The notation is fully symbolic and compatible with WCB's randomization and range assignment grammar.

---

**Intrabasal**
$$
r_i = B;\; \Omega = \text{«▢»}: \qquad
r_{i-1} = \frac{r_i}{⟨⟨ \text{min} ∧ \text{max} ⟩⟩}
\quad \text{while } r_i \geq \Omega
$$

**Extrabasal**
$$
r_i = B;\; \Omega = \text{«▢»}: \qquad
r_{i+1} = r_i \cdot ⟨⟨ \text{min} ∧ \text{max} ⟩⟩
\quad \text{while } r_i \leq \Omega
$$
Where:
- B = basal orbital radius (e.g. the nucleal orbit $\mathcal{N}$)
- Ω = orbital distance cuttoff (minimum or maximum allowed orbit based on the star system constraints)

## 🔄 Usage Strategy

The **intrabasal** and **extrabasal** forms can be used independently depending on your desired anchoring strategy:

- 🧭 **Outward-Only Generation**  
  If you begin at the **innermost permissible orbit** (e.g. a thermal, Roche, or design constraint), use the **extrabasal** form to expand outward via multiplicative steps:
$$
  r_0 = «inner limit»;\; L = «system edge»:
  \quad r_{i+1} = r_i \cdot ⟨⟨min ∧ max⟩⟩, \text{ while } r_{i+1} \leq L
$$
- 🧭 **Outward-Only Generation**  
  If you begin at the **outermost permissible orbit** (e.g. a thermal or design constraint), use the **extrabasal** form to expand outward via multiplicative steps:
$$
  r_0 = «inner limit»;\; L = «system edge»:
  \quad r_{i-1} = \dfrac{r_i} {⟨⟨min ∧ max⟩⟩}, \text{ while } r_{i+1} \leq L
$$

> Either method can fully define a system — or both can be combined with a central anchor (e.g. nucleal orbit) to scaffold a bidirectional structure.
