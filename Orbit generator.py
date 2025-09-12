import random

# --- Global Settings ---
mode = "medial"    # choose: "conservative", "medial", or "optimistic"
seed = 1962          # set to None for random results
basal_orbit = 1.3725
inner_cutoff = 0.011
outer_cutoff = 35.0

# --- Interval ranges by mode ---
interval_modes = {
    "optimistic": (1.0, 5.0),
    "medial": (1.2, 3.5),
    "conservative": (1.4, 2.0),
}

# --- Apply mode ---
if mode not in interval_modes:
    raise ValueError(f"Invalid mode: {mode}. Choose conservative, medial, or optimistic.")
min_interval, max_interval = interval_modes[mode]

# --- Apply seed if set ---
if seed is not None:
    random.seed(seed)

# --- Orbit generation functions ---
def intrabasal(base, cutoff=0.011):
    """Generate inward orbits from base down to cutoff AU."""
    orbits = [base]
    current = base
    while True:
        interval = random.uniform(min_interval, max_interval)
        next_orbit = current / interval
        if next_orbit < cutoff:
            break
        orbits.append(round(next_orbit, 3))
        current = next_orbit
    return list(reversed(orbits))

def extrabasal(base, cutoff=35.0):
    """Generate outward orbits from base up to cutoff AU."""
    orbits = [base]
    current = base
    while True:
        interval = random.uniform(min_interval, max_interval)
        next_orbit = current * interval
        if next_orbit > cutoff:
            break
        orbits.append(round(next_orbit, 3))
        current = next_orbit
    return orbits

# --- Build system ---
inner = intrabasal(basal_orbit, cutoff=inner_cutoff)
outer = extrabasal(basal_orbit, cutoff=outer_cutoff)
system_orbits = inner + outer[1:]

# --- Excel-friendly output ---
print("Orbit\tDistance (AU)")
for i, orbit in enumerate(system_orbits, start=1):
    print(f"{i}\t{orbit}")
