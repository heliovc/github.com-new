# Ranking #10 — Top 5 Tallest Mountains in the Solar System (Cosmic Scale)
# Ranked by height from base to summit. Twist: #5 is on Earth but mostly underwater; #1 and #2 are neck and neck depending on how you
# measure. Visual NEW: "peaks" (vertical km ruler 0–26 km TO SCALE, Everest silhouette + airliner cruising line at ~11 km, mountain
# profile by type: ocean | block | ridge | central | shield; the world as a small sphere). Hook: big number in frame 0 ("25 KM") + a "?"
# shield volcano towering over Everest. Outro: all five side by side + "Which mountain should we put next?".
# Theme NEW: mint / terracotta on a basalt-brown tint. Own calc: 25 / 8.849 ≈ 2.8 Everests; Mauna Kea 4,207 m above sea level,
# ≈ 6,000 m below -> ≈ 10.2 km base to summit.
TITLE = "Top 5 Tallest Mountains in the Solar System"
THEME = {"accent": (120, 240, 190), "accent2": (245, 160, 110), "star_col": (240, 200, 170), "tint": (50, 26, 16),
         "bar": "TOP 5 TALLEST MOUNTAINS", "hook": "peaks", "outro": "peaks"}

HOOK = {"say": "Twenty five kilometers. Almost three Everests. These are the five tallest mountains in the solar system.",
        "big": "25 KM", "top": "almost 3 Everests tall", "sub": "and Everest doesn't even make the list"}

ITEMS = [
 {"rank": 5, "name": "Mauna Kea", "short": "Mauna Kea", "tag": "Hawaii, Earth", "num": 10.2, "dec": 1, "suffix": " km", "unit": "from the ocean floor to the summit",
  "source": "USGS / NOAA", "vis": {"type": "peaks", "kind": "ocean", "km": 10.2, "sea": 6.0, "col": (110, 95, 85), "world": "Earth", "world_col": (70, 130, 230), "note": "most of it is underwater"},
  "say": "Number five. Mauna Kea, in Hawaii. Measured from the ocean floor, it's about ten kilometers tall, taller than Everest. Most of it is underwater."},
 {"rank": 4, "name": "Boösaule Montes", "short": "Boösaule", "tag": "Io, a moon of Jupiter", "num": 17.5, "dec": 1, "suffix": " km", "unit": "tallest mountain on Io",
  "source": "Schenk et al. 2001, Voyager / Galileo", "vis": {"type": "peaks", "kind": "block", "km": 17.5, "col": (215, 175, 90), "world": "Io", "world_col": (230, 205, 110), "note": "not a volcano, on the most volcanic world"},
  "say": "Number four. Boösaule Montes, on Jupiter's moon Io. Seventeen and a half kilometers. And it isn't even a volcano."},
 {"rank": 3, "name": "Iapetus Ridge", "short": "Iapetus", "tag": "Saturn's walnut-shaped moon", "num": 20, "dec": 0, "suffix": " km", "unit": "a ridge around the moon's equator",
  "source": "NASA / Cassini", "vis": {"type": "peaks", "kind": "ridge", "km": 20, "col": (175, 165, 150), "world": "Iapetus", "world_col": (170, 160, 145), "note": "it wraps around the equator"},
  "say": "Number three. A ridge on Saturn's moon Iapetus, up to twenty kilometers high, running around its equator like the seam of a walnut."},
 {"rank": 2, "name": "Rheasilvia Peak", "short": "Rheasilvia", "tag": "asteroid Vesta", "num": 22, "dec": 0, "suffix": " km", "unit": "central peak of a giant crater",
  "source": "NASA / Dawn", "vis": {"type": "peaks", "kind": "central", "km": 22, "col": (160, 150, 140), "world": "Vesta", "world_col": (150, 140, 130), "note": "thrown up by a giant impact"},
  "say": "Number two. The central peak of Rheasilvia, a crater on the asteroid Vesta. About twenty two kilometers, pushed up by an impact that nearly shattered Vesta."},
 {"rank": 1, "name": "Olympus Mons", "short": "Olympus", "tag": "Mars", "num": 25, "dec": 0, "suffix": " km", "unit": "about as wide as Arizona",
  "source": "NASA", "vis": {"type": "peaks", "kind": "shield", "km": 25, "col": (200, 110, 80), "world": "Mars", "world_col": (210, 100, 70), "note": "a volcano almost 3 Everests tall"},
  "say": "And number one. Olympus Mons on Mars. About twenty five kilometers high, a volcano almost three times taller than Everest."},
]

OUTRO = {"say": "Everest didn't even make the list. Which mountain should we put next? Subscribe to Cosmic Scale."}

SOURCES = ["USGS / NOAA: Mauna Kea rises about 4,207 m above sea level and more than 10,000 m from its base on the sea floor",
           "Schenk et al. (2001), Journal of Geophysical Research (Voyager and Galileo data): Boösaule Montes on Io about 17.5 km high, a tectonic mountain",
           "NASA / Cassini: Iapetus's equatorial ridge rises up to about 20 km",
           "NASA / Dawn: the central peak of Vesta's Rheasilvia crater rises about 22 km; some measurements put it close to Olympus Mons",
           "NASA: Olympus Mons on Mars is about 25 km high, almost three times Mount Everest, and about the size of Arizona",
           "Nepal and China (2020): Mount Everest 8,849 m above sea level",
           "Own calculation: 25 / 8.849 ≈ 2.8 Everests"]
