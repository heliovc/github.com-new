# Ranking #24 — Top 5 Biggest Dwarf Planets (Cosmic Scale)
# The five dwarf planets officially recognised by the IAU, ranked by size (mean diameter):
# Pluto 2,377 km (NASA, New Horizons); Eris 2,326 km (NASA), about 27% more massive than Pluto; Haumea about 2,322 × 1,704 × 1,026 km
# (Ortiz et al. 2017, Nature, which also found its ring), volume-equivalent ~1,590 km, spins once in about 4 hours (NASA);
# Makemake about 1,430 km, has a small moon found by Hubble in 2016 (NASA); Ceres 939 km (NASA Dawn), the only dwarf planet in the
# asteroid belt, visited by Dawn 2015–2018. Average distances from the Sun (NASA): Ceres 2.8 AU, Pluto 39.5, Haumea 43, Makemake 45.8, Eris 68.
# Own calc: (2322 × 1704 × 1026)^(1/3) = 1,590 km; Pluto / Moon = 2,377 / 3,474.8 = 68%; all five side by side 939 + 1,430 + 1,590 + 2,326 +
# 2,377 = 8,662 km, narrower than Earth (12,742 km); sunlight time = AU × 8.317 min.
# Visual NEW: "dwarfs" (each world to scale inside the Moon's outline + square-root distance strip).
TITLE = "Top 5 Biggest Dwarf Planets"
THEME = {"accent": (255, 160, 200), "accent2": (170, 220, 255), "star_col": (255, 220, 235), "tint": (30, 10, 26),
         "bar": "TOP 5 DWARF PLANETS", "hook": "dwarfs", "outro": "dwarfs",
         "outro_note": "all five side by side: narrower than Earth"}

HOOK = {"say": "The biggest dwarf planet is smaller than our Moon.",
        "big": "2,377 KM", "top": "the biggest dwarf planet", "sub": "and it still fits inside our Moon"}

ITEMS = [
 {"rank": 5, "name": "Ceres", "tag": "the one in the asteroid belt", "num": 939, "unit": "km wide", "suffix": "",
  "source": "NASA (Dawn mission)", "vis": {"type": "dwarfs", "kind": "ceres", "km": 939, "au": 2.77, "col": (170, 168, 165),
  "note": "bright salt spots seen by NASA's Dawn"},
  "say": "Number five. Ceres. Nine hundred thirty nine kilometers. The only dwarf planet in the asteroid belt, with bright salt spots on its surface."},
 {"rank": 4, "name": "Makemake", "tag": "it has a hidden moon", "num": 1430, "unit": "km wide (about)",
  "source": "NASA", "vis": {"type": "dwarfs", "kind": "makemake", "km": 1430, "au": 45.8, "col": (200, 130, 100),
  "note": "Hubble found its small moon in 2016"},
  "say": "Number four. Makemake. About fourteen hundred kilometers. Hubble found a tiny dark moon around it in twenty sixteen."},
 {"rank": 3, "name": "Haumea", "tag": "shaped like an egg", "num": 1590, "unit": "km, average width",
  "source": "Ortiz et al. 2017 (Nature) / NASA", "vis": {"type": "dwarfs", "kind": "haumea", "km": 1590, "au": 43.1, "col": (235, 235, 240),
  "note": "one spin every 4 hours · it has a ring"},
  "say": "Number three. Haumea. It spins so fast, once every four hours, that it's stretched into an egg. And it has a ring."},
 {"rank": 2, "name": "Eris", "tag": "heavier than Pluto", "num": 2326, "unit": "km wide",
  "source": "NASA", "vis": {"type": "dwarfs", "kind": "eris", "km": 2326, "au": 67.8, "col": (225, 225, 232),
  "note": "27% more mass than Pluto"},
  "say": "Number two. Eris. Two thousand three hundred twenty six kilometers. A bit smaller than Pluto, but heavier. Finding it is what cost Pluto its planet title."},
 {"rank": 1, "name": "Pluto", "tag": "the king of the dwarfs", "num": 2377, "unit": "km wide",
  "source": "NASA (New Horizons)", "vis": {"type": "dwarfs", "kind": "pluto", "km": 2377, "au": 39.5, "col": (210, 170, 130),
  "note": "only 68% as wide as our Moon"},
  "say": "And number one. Pluto. Two thousand three hundred seventy seven kilometers. The biggest dwarf planet, and still only two thirds as wide as our Moon."},
]

OUTRO = {"say": "Put all five side by side, and they're still narrower than Earth. Which world should we visit next? Subscribe to Cosmic Scale."}

SOURCES = ["NASA: Pluto is 2,377 km wide (New Horizons); Eris is about 2,326 km wide and about 27 percent more massive than Pluto; its discovery led the IAU to define dwarf planets in 2006",
           "Ortiz et al. (2017), Nature: Haumea measures about 2,322 × 1,704 × 1,026 km and has a ring; NASA: it spins once in about 4 hours",
           "NASA: Makemake is about 1,430 km wide; Hubble found its small moon (MK2) in 2016",
           "NASA (Dawn mission, 2015–2018): Ceres is 939 km wide, the only dwarf planet in the asteroid belt, with bright salt deposits in Occator crater",
           "NASA: average distances from the Sun: Ceres 2.8 AU, Pluto 39.5 AU, Haumea 43 AU, Makemake 45.8 AU, Eris 68 AU; our Moon is 3,474.8 km wide; Earth 12,742 km",
           "Own calculations: Haumea's volume-equivalent width (2,322 × 1,704 × 1,026)^(1/3) = 1,590 km; Pluto / Moon = 68%; all five side by side = 8,662 km, narrower than Earth; sunlight time = distance in AU × 8.3 minutes"]
