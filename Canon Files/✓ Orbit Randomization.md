


# Orbit Randomization Notation
This symbolic system defines how to procedurally generate a sequence of orbital radii using randomized multiplicative (or divisive) steps from a baseline (**basal**) value. It distinguishes between **intrabasal** (moving inward) and **extrabasal** (moving outward) orbit generation.

The notation is fully symbolic and compatible with WBN's randomization and range assignment grammar.

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
