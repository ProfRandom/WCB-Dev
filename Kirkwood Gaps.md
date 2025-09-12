# Kirkwood Gaps
### Sidebar: Calculating Resonant Orbits  

When mapping possible **Kirkwood-style gaps** in an orbital region, use the bracketing orbits as **perturbers**. For each perturber, trial resonances can be found by scaling the orbital period with small integer ratios and converting back to distance with Kepler’s 3rd law.  
### 🔹 Inner Orbit Resonances  
Start from the **inner perturber** with period $P_i$.  
$$
P_x = P_i \times k
$$$$
a_x = \sqrt[3]{\Big(P_x^2 \, M\Big)}
$$  
Where:
- $P_x$ = resonant period  
- $a_x$ = resonant distance (AU)  
- $M$ = stellar mass (in solar units)  
- $k$ = resonance scaler  

Keep only values where $a_x < a_o$ (inside the outer orbit).  

**Combined form:**  
$$
a_x = \sqrt[3]{\Big((P_i \times k)^2 \, M\Big)}
$$
### 🔹 Outer Orbit Resonances  
Start from the **outer perturber** with period $P_o$.  
$$
P_x = \frac{P_o}{k}
$$$$
a_x = \sqrt[3]{\Big(P_x^2 \, M\Big)}
$$Where:
- $P_x$ = resonant period  
- $a_x$ = resonant distance (AU)  
- $M$ = stellar mass (in solar units)  
- $k$ = resonance scaler  

Keep only values where $a_x > a_i$ (outside the inner orbit).  

**Combined form:**  
$$
a_x = \sqrt[3]{\left(\frac{P_o}{k}\right)^2 M}
$$ 
### 🔹 Resonance Scalers  
The most dynamically significant resonances correspond to:  
$$
k \in \{1.333, \; 1.5, \; 1.667, \; 2, \; 2.5, \; 3, \; 4, \; 5\}
$$These are shorthand for the integer ratios:  

| <center>Scaler</center> | <center>Resonance<br>Ratio</center> | <center>Order</center> |      |
| ----------------------: | ----------------------------------: | ---------------------: | ---- |
|                   1.333 |                                 4:3 |                      1 | Trap |
|                   1.500 |                                 3:2 |                      1 | Trap |
|                   1.667 |                                 5:3 |                      2 | Gap  |
|                   2.000 |                                 2:1 |                      1 | Gap  |
|                   2.500 |                                 5:2 |                      3 | Gap  |
|                   3.000 |                                 3:1 |                      2 | Gap  |
|                   4.000 |                                 4:1 |                      3 | Gap  |
|                   5.000 |                                 5:1 |                      4 | Gap  |
>**Note:**
>Preferentially choose resonance ratios with order 1 or 2 whenever possible
> _“Some resonances destabilize small bodies, carving out **gaps**. Others stabilize them, creating long-lived populations or **traps**. In practice, 2:1, 3:1, and 5:2 are classic gap-makers, while 3:2 and 4:3 are trap-makers.”_
### 📖 Worldmaker takeaway  
1. Choose your perturber (inner or outer orbit).  
2. Apply the resonance scaler to its orbital period.  
3. Convert the trial period to AU with Kepler’s law.  
4. Discard resonances that fall outside the gap.  

👉 The surviving $a_x$ values are your **candidate gap-makers** or **resonant trapping zones**.  
