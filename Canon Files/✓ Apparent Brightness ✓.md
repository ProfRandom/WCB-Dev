# Apparent Brightness
How bright something that shines _is_ and how bright it _appears_ to an observer is a function of distance.  The absolute apparent brightness can be calculated by:
$$
B_A = \dfrac{L_W}{4 \pi d^2}
$$
Where:
- $B_A$ = apparent brightness (flux, in Watts/m²)
- $L_W$ = luminosity of the star
- d = distance between the star and the observer in meters

This is a useful equation in general astrophysics, but it is less accessible for thesiastics, because one has to know the actual luminosity of the star in watts, which is not always an easy number to look up — and even harder to calculate.  Also, distance in _meters_?  Do you know how fast those numbers get _insanely large_?
## Relative Apparent Brightness
Here is a more useful equation for thesiastics:
$$
B_{A⊙} = \dfrac{L}{D^2}
$$
Where:
- $B_A$ = the apparent brightness of the star _in solar units_
- $L$ = the luminosity of the star _in solar units_
- $D$ = the distance to the star in AU (i.e. the semi-major axis of the planemo's orbit)

>Note that this is the same form as the _inverse-square law_.  The amount of energy (of _any kind_) detectable from a radiating object decreases with the square of the distance of the observer from that object.  If your campfire feels a certain intensity where you're standing, and you move twice as far away, the intensity will feel less by the inverse-square of the distance you've moved.  Since you're now twice as far away as you were
$$
E = \dfrac{1}{2^2} = \dfrac{1}{4}
$$
… one-fourth as much as before.

### Example 1: How Bright Does The Sun Appear From Mars?
Since we're talking about the Sun, here, $L = 1$.  The distance is Mars' orbital semi-major axis, $D = 1.524$ AU:
$$
B_{A⊙} = \dfrac{L}{D^2} = \dfrac{1}{1.524^2} = \dfrac{1}{2.323} = 0.431
$$
So, the sun is about 43% as bright seen from Mars as it is seen from Earth.
### Example 2
Let's imagine a star called Kalveru which has a luminosity $L=1.618$⊙.  How bright would it appear to an observer on a planet 1 AU away?  Here, the luminosity is what varies not the distance, so our equation becomes:
$$
B_{A⊙} = \dfrac{L}{D^2} = \dfrac{1.618}{1^2} = \dfrac{1.618}{1} = 1.618
$$
So, the apparent brightness in solar units of any star when viewed from 1 AU away is simply the relative luminosity of the star in solar units.
$$
\text{When}\quad D = 1, \quad B_{A⊙} = L⊙
$$
Now, let's put a planet (Dynon) in orbit around Kalveru at $D = 1.524$ AU.  How bright does Kalveru appear from Dynon?
$$
B_{A⊙} = \dfrac{L}{D^2} = \dfrac{1.618}{1.524^2} = \dfrac{1.618}{2.323} = 0.697
$$
So, Kalveru appears about 70% as bright from Dynon as the Sun does from Earth.