# Ranking #16 — Top 5 Biggest Asteroids (Cosmic Scale)
# Mean diameters: Ceres 939.4 km (NASA Dawn), Vesta 525.4 km (NASA Dawn), Pallas ≈ 511 km (Marsset et al. 2020), Hygiea ≈ 434 km (ESO/SPHERE,
# Vernazza et al. 2019), Interamnia ≈ 332 km (Hanuš et al. 2020; older estimates ~306–326 km). Visual NEW: "rocks" (code-drawn lumpy asteroid to
# scale, slow spin, 100 km bar, "drive around it at 100 km/h" counter). Hook: big "939 KM" + Ceres silhouette with "?".
# Own calc: circumference π·d / 100 km/h -> Interamnia 10 h, Hygiea 14 h, Pallas 16 h, Vesta 17 h, Ceres 30 h.
TITLE = "Top 5 Biggest Asteroids"
THEME = {"accent": (255, 175, 95), "accent2": (140, 220, 200), "star_col": (220, 210, 190), "tint": (34, 26, 18),
         "bar": "TOP 5 BIGGEST ASTEROIDS", "hook": "rocks", "outro": "rocks",
         "outro_note": "all five live between Mars and Jupiter"}

HOOK = {"say": "Number one is so big, it's also a dwarf planet. The five biggest asteroids.",
        "big": "939 KM", "top": "wide: the biggest asteroid", "sub": "every one drawn to the same scale"}

ITEMS = [
 {"rank": 5, "name": "Interamnia", "tag": "named after Teramo, Italy", "num": "≈ 332 km", "unit": "across (estimates: 306–332 km)",
  "source": "Hanuš et al. 2020 (ESO VLT)", "vis": {"type": "rocks", "km": 332, "lump": 0.10, "col": (150, 140, 130), "seed": 5, "note": "one of the least-known giants out there"},
  "say": "Number five. Interamnia. About three hundred thirty kilometers. Driving around it would take ten hours."},
 {"rank": 4, "name": "Hygiea", "tag": "might be the smallest dwarf planet", "num": "≈ 434 km", "unit": "across",
  "source": "ESO SPHERE, Vernazza et al. 2019", "vis": {"type": "rocks", "km": 434, "lump": 0.04, "col": (120, 115, 120), "seed": 4, "note": "almost perfectly round"},
  "say": "Number four. Hygiea. Four hundred thirty four kilometers, and so round it might be the smallest dwarf planet we know."},
 {"rank": 3, "name": "Pallas", "tag": "the tilted one", "num": "≈ 511 km", "unit": "across",
  "source": "Marsset et al. 2020", "vis": {"type": "rocks", "km": 511, "lump": 0.09, "col": (170, 170, 180), "seed": 3, "note": "orbit tilted about 35° to the planets"},
  "say": "Number three. Pallas. Five hundred eleven kilometers, on an orbit tilted so steeply that no probe has ever visited it."},
 {"rank": 2, "name": "Vesta", "tag": "visited by NASA's Dawn, 2011", "num": "525 km", "unit": "across",
  "source": "NASA / JPL (Dawn mission)", "vis": {"type": "rocks", "km": 525, "lump": 0.13, "col": (190, 175, 150), "seed": 2, "note": "its south pole peak is about 22 km tall"},
  "say": "Number two. Vesta. Five hundred twenty five kilometers. Its south pole has a mountain about twenty two kilometers tall, more than twice Everest."},
 {"rank": 1, "name": "Ceres", "tag": "asteroid AND dwarf planet", "num": "939 km", "unit": "across: a quarter of the belt's mass",
  "source": "NASA / JPL (Dawn mission)", "vis": {"type": "rocks", "km": 939, "lump": 0.015, "col": (150, 145, 145), "seed": 1, "spot": True, "note": "the bright spots are salt"},
  "say": "And number one. Ceres. Nine hundred thirty nine kilometers. A quarter of the whole asteroid belt's mass, with bright patches of salt on its surface."},
]

OUTRO = {"say": "Which one should we land on? Subscribe to Cosmic Scale."}

SOURCES = ["NASA / JPL (Dawn mission): Ceres is 939.4 km across, the largest object in the asteroid belt, recognized as a dwarf planet, holds about 25% of the belt's mass; its bright spots in Occator crater are salt (sodium carbonate) deposits",
           "NASA / JPL (Dawn mission): Vesta has a mean diameter of 525.4 km; the central peak of its Rheasilvia basin is about 22 km high",
           "Marsset et al. 2020 (Nature Astronomy): Pallas is about 511 km across; its orbit is inclined about 35° to the plane of the planets; no spacecraft has visited it",
           "Vernazza et al. 2019 (ESO VLT/SPHERE, Nature Astronomy): Hygiea is about 434 km across and nearly spherical — a candidate for the smallest dwarf planet",
           "Hanuš et al. 2020 (ESO VLT): Interamnia about 332 km across (older estimates 306–326 km); named after Teramo, Italy (Latin: Interamnia)",
           "Own calculations: time to drive around each one at 100 km/h = π × diameter / 100 (Interamnia ≈ 10 h, Ceres ≈ 30 h)"]
