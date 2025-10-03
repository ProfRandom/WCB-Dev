# Warp Drive Is (Woefully) Too Slow
In the Star Trek universe of the *Star Trek: The Original Series* (*ST:TOS*), the speed at which starships could travel was measured in "warp factors", such that warp factor 1 was the exact speed of light. Each succeeding warp factor was calculated by the cube of the warp factor multiplied by the speed of light (c).
$$
v = f^3c
$$
Where:
- $f$ = warp factor number
- v = the speed of the ship in meters/second
- c = the speed of light (299792458 m/s)

If $c$ is taken as 1.0, then $v$ is returned in multiples of lightspeed.  For example

Given:
- $f$ = 3
- $c$ = 1
$$
v = f^3 = 3^3 = 27\; \text{times the speed of light}
$$
- Note that when $c$ = 1, it can be dropped from the equation.

Calculating the warp factor from the speed is a function of the cube-root of the velocity of the ship and the speed of light:
$$
f = \sqrt[3]\frac{v}{c}
$$
- Here, again if one is expressing $v$ as multiples of lightspeed, $c$ is always 1 and the equation can simplify to:
$$
f = \sqrt[3]{v}
$$
## "I'm givin' 'er all she's got, Cap'n!"
The maximum at which Constitution-class ships in *ST:TOS* could travel — and then only for short periods of time — was warp 8, which is a velocity of:
$$
v = f^3 = 8^3 = 512\; \text{times the speed of light}
$$
This seems fast until we start considering actual interstellar distances.

Proxima Centauri is the closest star to the Sun at 4.24 light years distant.  At warp 8, Constitution-class starships take:
$$
T = \frac{4.25}{512} = 0.00828]; \text{years} ≈ 3.025\; \textit{days} 
$$
to make the journey.  Days.  Not minutes; not hours — *days*.

## Boosting The Speed
In *Star Trek: The Next Generation* (*ST:TNG*), the assumption was that warp technology had been improved upon since the days of Kirk and Spock, and warp factors were redefined to be:
$$
v = f^\frac{10}{3}
$$
So now, warp 8 is:
$$
v = f^\frac{10}{3} = 8^\frac{10}{3} = 1024c
$$
… which exactly doubles the old warp 8 velocity and shortens the trip to Proxima Centauri to 1.5124 days, or about 36.3 hours.  Still not an afternoon stroll.

The star Deneb is 2600 lightyears from the Sun.  At *ST:TOS* warp 8, the _Enterprise_ would take
$$
T = \frac{2600}{512} = 5.078\; \textit{years}
$$
to get there.  The *ST:TNG* _Enterprise_, at its warp 8 cuts the trip in half to a mere 2.54 *years*.

And, yet, in the very first episode of *ST:TNG*, "Encounter at Farpoint" (1987), the mission destination is stated to be Deneb IV.  Such a designation is usually assumed to refer to the fourth planet orbiting a star named "Deneb".  Based on this, we can assume Picard and company's destination was the Deneb we just calculated a 2.54 year one-way journey to.

Further more the _Star Trek_ wiki site, Memory Alpha states that "By 2373, the Federation's territory was spread across 8000 lightyears…." Assuming this to be a circular diameter, it would take *ST:TNG Enterprise*
$$
T = \frac{8000}{1024} = 7.8125\; \textit{years}
$$
to traverse the width of the Federation.

- Note: If we take that to mean 8000 *cubic* lightyears, that's a spherical volume of only about
$$
r = \sqrt[3]{\frac{3V}{4\pi}} = \sqrt[3]{\frac{3\cdot8000}{4\pi}} = \sqrt[3]{\frac{24000}{4\pi}} = \sqrt[3]{1909.86} ≈ 12.41\; \text{lightyears}
$$
… in radius, which seems a bit on the small side, doesn't it?

*Star Trek: Voyager (ST:VOY)* used the same warp formula as *ST:TNG*, **up to warp 9**, and then an unspecified exponential curve thereafter, such that warp 10 is infinite velocity.  Most fan sources estimate _Voyager_'s top speed of 9.975 to be 3000c, but that still means that a cross-Federation journey would take:
$$
T = \frac{8000}{3000} = 2.67\; \textit{years}
$$
The Sol-Deneb run mentioned earlier would take:
$$
T = \frac{2600}{3000} = 0.867\; \textit{years} ≈ 316.6\; \textit{days}
$$
… which is just over 10 standard months... and that's *assuming no stops along the course*.

Clearly while _Star Trek_ warp drive is _fast_, interstellar distances make the travel times comparable to steamships crossing the Atlantic in the early 20th Century.