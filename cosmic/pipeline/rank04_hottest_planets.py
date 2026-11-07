# Ranking #4 — Top 5 Hottest Planets Ever Measured (Cosmic Scale)
# Visual NEW: "thermo" — vertical thermometer 0–6,000 °C with reference marks (lead, lava, iron, Sun's surface) + planet glowing in its
# temperature color; hook = thermometer near the top with a "?" planet. Theme lava red / yellow.
TITLE = "Top 5 Hottest Planets Ever Measured"
THEME = {"accent": (255, 110, 50), "accent2": (255, 215, 90), "star_col": (255, 160, 80), "tint": (70, 22, 8),
         "bar": "THE 5 HOTTEST PLANETS EVER MEASURED", "hook": "thermo",
         "outro_note": "#1 is almost as hot as the surface of the Sun"}

HOOK = {"say": "The number one planet on this list is hotter than most stars. These are the five hottest planets ever measured.",
        "top": "Hottest planets ever measured", "sub": "#1 is hotter than most stars"}

ITEMS = [
 {"rank": 5, "name": "Venus", "short": "Venus", "tag": "our neighbor · hotter than Mercury", "num": 475, "suffix": " °C", "unit": "at the surface",
  "source": "NASA", "vis": {"type": "thermo", "c": 475, "r": 150, "note": "hot enough to melt lead"},
  "say": "Number five. Venus. Four hundred and seventy five degrees Celsius at the surface, hot enough to melt lead. It's hotter than Mercury, because its thick atmosphere traps the heat."},
 {"rank": 4, "name": "WASP-12b", "short": "WASP-12b", "tag": "a planet being eaten by its star", "num": 2210, "suffix": " °C", "unit": "estimated temperature",
  "source": "NASA / Hubble", "vis": {"type": "thermo", "c": 2210, "r": 175, "note": "stretched into an egg shape"},
  "say": "Number four. WASP twelve b. About twenty two hundred degrees. It orbits so close that its star is stretching it into an egg shape and slowly eating it."},
 {"rank": 3, "name": "WASP-76b", "short": "WASP-76b", "tag": "where it rains iron", "num": 2400, "suffix": " °C", "unit": "on the day side",
  "source": "ESO / VLT", "vis": {"type": "thermo", "c": 2400, "r": 185, "note": "iron vaporizes, then rains at night"},
  "say": "Number three. WASP seventy six b. Over twenty four hundred degrees on its day side. Hot enough to boil iron, which then rains down on the night side."},
 {"rank": 2, "name": "WASP-189b", "short": "WASP-189b", "tag": "a year lasts 2.7 days", "num": 3200, "suffix": " °C", "unit": "on the day side",
  "source": "ESA / Cheops", "vis": {"type": "thermo", "c": 3200, "r": 195, "note": "20 times closer to its star than Earth"},
  "say": "Number two. WASP one eighty nine b. Thirty two hundred degrees. It's twenty times closer to its star than Earth is to the Sun. A year there lasts under three days."},
 {"rank": 1, "name": "KELT-9b", "short": "KELT-9b", "tag": "hotter than most stars", "num": 4300, "suffix": " °C", "unit": "on the day side",
  "source": "NASA / JPL", "vis": {"type": "thermo", "c": 4300, "r": 210, "note": "molecules are torn apart"},
  "say": "And number one. KELT nine b. Forty three hundred degrees Celsius on its day side. Hotter than most stars in the galaxy. So hot that the molecules in its air are ripped apart."},
]

OUTRO = {"say": "That's almost as hot as the surface of our Sun. Subscribe to Cosmic Scale for more."}

SOURCES = ["NASA Science, Venus facts (surface about 475 °C / 900 °F, hot enough to melt lead; hotter than Mercury because of its thick CO2 atmosphere)",
           "NASA Science, WASP-12b: an egg-shaped planet (about 2,210 °C / 4,000 °F; tidally stretched and being consumed by its star)",
           "ESO press release eso2004 (March 2020): WASP-76b, day side above 2,400 °C, iron vaporizes and rains on the night side",
           "ESA, First results from Cheops (Sept 2020): WASP-189b, about 3,200 °C, ~20 times closer to its star than Earth to the Sun, 2.7-day orbit",
           "NASA JPL (2018), For hottest planet, a major meltdown: KELT-9b day side above 4,300 °C (7,800 °F), hydrogen molecules torn apart",
           "Sun's visible surface about 5,500 °C (NASA)"]
