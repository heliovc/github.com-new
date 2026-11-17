# Ranking #14 — Top 5 Longest Years in the Solar System (Cosmic Scale)
# A "year" = one full orbit around the Sun. Ranked by orbital period (JPL Small-Body Database / NASA). Sedna is not an official dwarf
# planet (said as "world"). Visual NEW: "orbityear" (each orbit TO SCALE with Earth's orbit drawn at the same scale; one lap with Kepler
# timing + Earth-years counter + "sped up N times"; log ruler of years). Hook: big number "11,400 YEARS" + Sedna crawling on its needle
# orbit with a "?"; spoken hook "A year here lasts eleven thousand years." Outro: all five orbits at one scale + "Which world should we put next?".
# Theme NEW: ice violet / comet mint on an indigo tint. a, e: JPL SBDB (rounded). Own checks: Kepler P = a^1.5 -> 39.5 -> 248, 43.1 -> 283,
# 45.4 -> 306, 67.9 -> 560, 506 -> 11,380 years. Pluto found 1930 + 248 = 2178.
TITLE = "Top 5 Longest Years in the Solar System"
THEME = {"accent": (190, 150, 255), "accent2": (140, 240, 200), "star_col": (210, 190, 255), "tint": (30, 20, 70),
         "bar": "TOP 5 LONGEST YEARS IN THE SOLAR SYSTEM", "hook": "orbityear", "outro": "orbityear",
         "outro_note": "#1's year is 46 times longer than Pluto's"}

HOOK = {"say": "A year here lasts eleven thousand years. These are the five longest years in our solar system.",
        "big": "11,400 YEARS", "top": "one year on this world", "sub": "and it's still orbiting our Sun"}

ITEMS = [
 {"rank": 5, "name": "Pluto", "short": "Pluto", "tag": "dwarf planet · found in 1930", "num": 248, "unit": "Earth years per orbit",
  "source": "NASA", "vis": {"type": "orbityear", "a": 39.5, "e": 0.25, "yr": 248, "col": (225, 195, 160), "ang": 0.3, "note": "found in 1930, it won't finish one year until 2178"},
  "say": "Number five. Pluto. Two hundred forty eight years. We found it in nineteen thirty, and it won't complete a single orbit until twenty one seventy eight."},
 {"rank": 4, "name": "Haumea", "short": "Haumea", "tag": "dwarf planet · shaped like an egg", "num": 285, "unit": "Earth years per orbit",
  "source": "NASA; JPL", "vis": {"type": "orbityear", "a": 43.1, "e": 0.19, "yr": 285, "col": (235, 235, 245), "ang": 0.9, "note": "it spins so fast it's stretched into an egg"},
  "say": "Number four. Haumea. Two hundred eighty five years. It spins so fast that it's stretched into the shape of an egg."},
 {"rank": 3, "name": "Makemake", "short": "Makemake", "tag": "dwarf planet · beyond Neptune", "num": 309, "unit": "Earth years per orbit",
  "source": "JPL Small-Body Database", "vis": {"type": "orbityear", "a": 45.4, "e": 0.16, "yr": 309, "col": (220, 140, 110), "ang": -0.4, "note": "its last year began in the early 1700s"},
  "say": "Number three. Makemake. About three hundred and nine years. One year there began in the early seventeen hundreds."},
 {"rank": 2, "name": "Eris", "short": "Eris", "tag": "dwarf planet · almost Pluto's size", "num": 557, "unit": "Earth years per orbit",
  "source": "JPL Small-Body Database", "vis": {"type": "orbityear", "a": 67.9, "e": 0.44, "yr": 557, "col": (200, 220, 255), "ang": 1.3, "note": "one year here is longer than the USA has existed, twice"},
  "say": "Number two. Eris. Five hundred fifty seven years. A single year there is more than twice as long as the United States has existed."},
 {"rank": 1, "name": "Sedna", "short": "Sedna", "tag": "a red world, far past Pluto", "num": "≈11,400", "unit": "Earth years per orbit",
  "source": "JPL Small-Body Database; NASA", "vis": {"type": "orbityear", "a": 506, "e": 0.85, "yr": 11400, "col": (240, 110, 90), "ang": 0.5, "span": 900, "note": "its last year started before farming did"},
  "say": "And number one. Sedna. About eleven thousand four hundred years. When its current year began, humans hadn't invented farming yet."},
]

OUTRO = {"say": "Forty six times longer than Pluto's year. Which world should we put next? Subscribe to Cosmic Scale."}

SOURCES = ["NASA Science (Pluto): one orbit takes 248 Earth years; Pluto was discovered in 1930",
           "NASA Science (Haumea): one orbit takes about 285 Earth years; its fast spin stretches it into an elongated shape",
           "JPL Small-Body Database: Makemake orbital period about 309 years; Eris about 557 years; Sedna about 11,400 years (semi-major axis about 506 AU, eccentricity about 0.85)",
           "Farming began roughly 12,000 to 11,000 years ago (Neolithic Revolution, Encyclopaedia Britannica)",
           "Own calculations: Kepler's third law P = a^1.5 (years, AU) as a check; 1930 + 248 = 2178; 2026 - 309 = 1717; 557 / 250 (USA since 1776) ≈ 2.2; 11,400 / 248 ≈ 46"]
