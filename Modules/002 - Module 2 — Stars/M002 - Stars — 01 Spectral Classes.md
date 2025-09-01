
![[Spectral Class Graphic.png]]

# Stars and Spectral Classes: The Fusion-Fueled Continuum

First: The spectral class system used throughout this guide — the sequence **O, B, A, F, G, K, M** — is historically rooted in the observational astronomy of the late 19th and early 20th centuries. Its peculiar alphabetical order reflects the evolution of stellar classification from empirical cataloging to physical understanding.

> For readers curious about its origins — including the critical work of **Annie Jump Cannon**, **Cecilia Payne-Gaposchkin**, and the less brilliant men who received most of the credit — see **[[Sidebar: The Spectral System and the Women Who Built It]]**.

Second: The spectral classes used in WBN are based on a **linearized temperature model**. This approach smooths over the irregularities of the traditional system to support clean interpolation, symbolic clarity, and consistent orbital modeling.

> If you're curious about the limitations of the classical OBAFGKM system — and why we’ve chosen to “straighten the curve” — see **[[Sidebar Module: _Mind the Gap — The Shortcomings of the Traditional Spectral Scale_]]**.

## Spectral Class Table
Here are the spectral classes we'll be working with.

![[Spectral Class Base Table ✓]]

> Notes:
> - Spectral Classes L, T, and Y are "special cases" which are covered in detail in another module ⟨⟨ insert module name here ⟩⟩
> - Each range reflects a star's **surface temperature**, typically noted as $T_{\text{eff}}$ in astronomical literature.
> - In WBN:
> 	- **K** = temperature in Kelvin 
> 	- **T** = temperature _relative to the Sun_ (i.e., ⊙ = 5800K ⇒ T = 1.0)
### Spectral *Type*
Each spectral class is subdivided into 10 **spectral types**, numbered **0** (hottest) to **9** (coolest).

> **Hippy**: Wait, that's  – 

Yes, it runs _backwards_. No, we’re not happy about it, either (don't shoot the messenger).

For example:  
- The Sun, at **5800K**, is classified as a **G2** star —  
	- Spectral **Class**: G  
	- Spectral **Type**: 2

> #### Note on Spectral Type Precision in WBN
> In this system, a **spectral type** is defined by its **numerical position** within a spectral class.  For example:
> - **G2**, **G2.3**, and **G2.9** are all **Type 2**    
> - The decimal simply adds interpolation precision — it does **not** define a new type.
> - Therefore, **Type 2** refers to the full range ⟨2.0 ∧ 2.999···⟩ within class *G*.

This allows for relatively simple mathematical treatment of the relationship between spectral type (T) and surface temperature (K).
$$
\begin{align}
Ƨ &= \dfrac{\kappa - K}{þ} \\ \\
\kappa & = Ƨ þ + K \\ \\
K &= \kappa - Ƨ þ \\ \\
þ &= \dfrac{\kappa - K}{Ƨ} \\
\end{align}
$$

Where:
- K = the star's surface temperature in Kelvin
- κ = the _upper bound_ temperature of the relevant spectral class
- þ = the thermal interval constant for the relevant spectral class
- Ƨ = the spectral *type* number
#### The Thermal Interval Constant (þ)
Where does þ come from?
For a given spectral class þ can be calculated by:
$$
þ = \dfrac{high\;temp - low\;temp}{10}
$$

Here is the above table with these constants added:


| Spectral<br>Class | <center>Low<br>Temp.<br>(Kelvin)</center> | <center>High<br>Temp.<br>(Kelvin)</center> | <center>Thermal<br>Interval<br>Constant<br>(þ)</center> |
| :---------------: | ----------------------------------------: | -----------------------------------------: | ------------------------------------------------------: |
|         O         |                                     25000 |                                      55000 |                                                    3000 |
|         B         |                                     10000 |                                      25000 |                                                    1500 |
|         A         |                                      7500 |                                      10000 |                                                     250 |
|         F         |                                      6000 |                                       7500 |                                                     150 |
|         G         |                                      5000 |                                       6000 |                                                     100 |
|         K         |                                      3500 |                                       5000 |                                                     150 |
|         M         |                                      2400 |                                       3500 |                                                     110 |
|         L         |                                      1300 |                                       2400 |                                                     110 |
|         T         |                                       600 |                                       1300 |                                                      70 |
|         Y         |                                       300 |                                        600 |                                                      30 |
|                   |                                           |                                            |                                                         |
|                   |                                           |                                            |                                                         |
#### Example
Let's run the numbers for the Sun
- Known surface temperature: 5800K
- Checking the table, 5800K falls between 5000K and 6000K, so the Sun is spectral class G
- The high temperature (κ) for spectral class G is κ 6000K
- The thermal interval constant (þ) for spectral class G is þ = 100
- What is the Sun's spectral type (Ƨ)
Running the numbers:
$$
\begin{align}
Ƨ &= \dfrac{\kappa - K}{þ} \\
Ƨ &= \dfrac{6000 - 5800}{100} \\
Ƨ &= \dfrac{200}{100} \\
Ƨ &= 2\;✓
\end{align}
$$
The Sun is spectral type *G2*.

**Reversing the process:**
- The known spectral class of the Sun is G
- The known spectral type of the Sun is Ƨ = 2
- The high temperature (κ) for spectral class G is κ 6000K
- The thermal interval constant (þ) for spectral class G is þ = 100
- What is the Sun's Kelvin temperature (K)
Running the numbers:
$$
\begin{align}
K &= \kappa - Ƨ þ \\
K &= 6000 - (2)(100) \\
K &= 6000 - 200 \\
K &= 5800\;✓
\end{align}
$$
The surface temperature of the Sun is *5800K*.

### Converting Between Absolute Kelvin (K) And Solar Relative (T)
Nothing could be simpler:
$$
\begin{align}
T &= \dfrac{K}{5800} \\ \\
K &= 5800T
\end{align}
$$
For instance: the Sun's surface temperature is K = 5800:
$$
T = \dfrac{K}{5800} = \dfrac{5800}{5800} = 1\;✓
$$
Conversely, the Sun's relative temperature is T = 1.0:
$$
K = 5800 T = (5800)(1) = 5800\;✓
$$
### Fictional Examples
Let's say we have a star called Essem that we want to be spectral type *F3.65*.  What is its Kelvin temperature?
- The surface temperature for spectral class F is K ∈ ⟨6000 ∧ 7500⟩.
- The thermal interval constant for spectral class F is þ = 150.
Working through the equation:
$$
\begin{align}
K &= \kappa - Ƨ þ \\
K &= 7500 - (3.65)(150) \\
K &= 7500 - 547.5 \\
K &= 6952.5\;✓
\end{align}
$$
What is Essem's relative surface temperature?
$$
\begin{align}
T = \dfrac{K}{5800} \\ \\
T = \dfrac{6952.5}{5800} \\ \\
T = 1.199\;✓
\end{align}
$$
Essem's relative temperature is *T = 1.199*⊙.

**Working The Other Direction**

Let us say that Essem has a near neighbor, Essel, and we know that its relative temperature is T = 0.876⊙.  What is its spectral type?

First, convert T to K by:
$$ K = 5800T = (5800)(0.876) = 5080.8\;✓ $$
Looking at our table we see that this value falls in spectral class G:

| Spectral<br>Class | <center>Low<br>Temp.<br>(Kelvin)</center> | <center>High<br>Temp.<br>(Kelvin)</center> | <center>Thermal<br>Interval<br>Constant<br>(þ)</center> |
| :---------------: | ----------------------------------------: | -----------------------------------------: | ------------------------------------------------------: |
|         G         |                                      5000 |                                       6000 |                                                     100 |

… which gives us all the other information we need:
- G-class high temperature is κ = 6000
- G-class thermal interval constant is þ = 100

The spectral type is:
$$
\begin{align}
Ƨ &= \dfrac{\kappa - K}{þ} \\ \\
Ƨ &= \dfrac{6000 - 5080.8}{100} \\ \\
Ƨ &= \dfrac{919.2}{100} \\ \\
Ƨ &= 9.192\;✓
\end{align}
$$
Essel's spectral type is *G9.192*.
### Parameter Ranges By Spectral Class

![[Parameter Ranges By Spectral Class ✓]]

