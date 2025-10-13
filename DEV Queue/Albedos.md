### 🌌 Step 1. Gather reference albedos (geometric, V-band)

|Planet|Type|Albedo (A)|
|---|---|---|
|Jupiter|Gas giant|0.52|
|Saturn|Gas giant|0.47|
|Uranus|Ice giant|0.51|
|Neptune|Ice giant|0.41|

---

### Step 2. Compute representative averages

- **Gas-giant mean:**
    
    0.50
- **Ice-giant mean:**
    
    0.46
- **All-giant mean:**
    
    0.48

---

### Step 3. Establish category “standard candles”

|Category|Symbol|Representative Albedo|Description|
|---|---|---|---|
|**Gas-Giant Standard Candle**|𝒞ᴳ|0.50|for Jovian-class worlds (H–He envelopes)|
|**Ice-Giant Standard Candle**|𝒞ᴵ|0.46|for Neptunian-class worlds (volatile mantles)|
|**Unified Giant Standard (optional)**|𝒞ᴳᴵ|0.48|mean of all four Solar examples|

---

### Step 4. How to use them

When a designer specifies only radius R and distance D:

$$
F_{rel} = \left(\frac{R}{R_J}\right)^2\left(\frac{A}{A_C}\right)\left(\frac{D_{ref}}{D}\right)^4
$$

where

- $A_C$​ is the albedo of the chosen standard candle,
- $D_{ref} = 19$ AU for the naked-eye threshold (Jupiter-size body at the Solar System limit).
    
### Albedo scaling for Giant Planets
This makes the scaling dead simple:

- Brighter albedo
$$
D_{new} = D_{std}\;\sqrt{\frac{R}{R_{J}}}\;\sqrt[4]{\frac{A}{A_{std}}}
$$

- Darker albedo
$$
D_{new} = D_{std}\;\sqrt{\frac{R}{R_{J}}}\;\sqrt[4]{\frac{A_{std}}{A}}
$$

Where:
- $A_{std} = 0.48$ for giant planets
- $D_{ref}$ = 19 AU
- $R$ = radius of planet
- $R_{J}$ = radius of Jupiter

### For Terrestrials
- Brighter albedo
$$
D_{new} = D_{std}\;\sqrt{\frac{R}{R_⨁}}\;\sqrt[4]{\frac{A}{A_{std}}}
$$

- Darker albedo
$$
D_{new} = D_{std}\;\sqrt{\frac{R}{R_⨁}}\;\sqrt[4]{\frac{A_{std}}{A}}
$$

Where:
- $A_{std} = 0.25$ for giant planets
- $D_{ref}$ = 2 AU
- $R$ = radius of planet
- $R_⨁$ = radius of Earth



    

---

### 🧭 WCB Summary

> **Category Standard Candles:**  
> – Gas-giant reference albedo ≈ 0.50  
> – Ice-giant reference albedo ≈ 0.46
> 
> These serve as _brightness anchors_ for scaling visibility and magnitude among non-self-luminous worlds.  
> Under Sun-like illumination, a Jupiter-radius planet with albedo 0.50 fades below naked-eye detectability beyond ~19 AU.  
> The corresponding limit for an ice-giant (same size, A = 0.46) is slightly nearer, ≈ 18 AU.
