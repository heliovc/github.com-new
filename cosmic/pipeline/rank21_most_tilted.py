# Ranking #21 — Top 5 Most Tilted Planets (Cosmic Scale)
# Obliquity to orbit from the NASA NSSDC planetary fact sheet (degrees): Venus 177.4, Uranus 97.8, Neptune 28.3, Saturn 26.7, Mars 25.2,
# Earth 23.4 (misses the list), Jupiter 3.1, Mercury 0.03. 177.4° = upside down: Venus spins backward, the Sun rises in the west (NASA).
# Uranus orbits on its side: each pole gets about 42 years of sunlight, then 42 years of dark (NASA; orbit 84 years). Neptune's 165-year
# orbit -> seasons about 41 years long (own calc, 165 / 4). Saturn's rings looked edge-on from Earth in March 2025 (NASA).
# Mars: own calc 25.2 - 23.4 = 1.8°. Visual NEW: "tilt" (protractor from straight-up to the spin axis + Earth ghost axis).
TITLE = "Top 5 Most Tilted Planets"
THEME = {"accent": (255, 120, 170), "accent2": (140, 235, 210), "star_col": (255, 210, 230), "tint": (30, 10, 34),
         "bar": "TOP 5 MOST TILTED PLANETS", "hook": "tilt", "outro": "tilt",
         "outro_note": "Earth: 23.4°. Just off the list."}

HOOK = {"say": "Planet number one is tilted one hundred seventy seven degrees. It spins upside down.",
        "big": "177°", "top": "planet #1 is upside down", "sub": "dashed line: Earth's tilt"}

ITEMS = [
 {"rank": 5, "name": "Mars", "tag": "almost Earth's twin tilt", "num": "25.2°", "unit": "axial tilt · Earth: 23.4°",
  "source": "NASA Mars Fact Sheet", "vis": {"type": "tilt", "kind": "rock", "col": (205, 100, 65), "deg": 25.2, "ghost": True, "note": "just 1.8° more than Earth, so Mars has seasons too"},
  "say": "Number five. Mars. Twenty five degrees. Just a bit more than Earth, so it gets seasons like ours."},
 {"rank": 4, "name": "Saturn", "tag": "its rings vanish edge-on", "num": "26.7°", "unit": "axial tilt",
  "source": "NASA Saturn Fact Sheet", "vis": {"type": "tilt", "kind": "ringed", "col": (225, 200, 150), "deg": 26.7, "ghost": True, "note": "in March 2025 we saw its rings exactly edge-on"},
  "say": "Number four. Saturn. Twenty seven degrees. The tilt is why its rings turned edge-on to us in twenty twenty five."},
 {"rank": 3, "name": "Neptune", "tag": "seasons 41 years long", "num": "28.3°", "unit": "axial tilt · 1 orbit = 165 years",
  "source": "NASA Neptune Fact Sheet", "vis": {"type": "tilt", "kind": "ice", "col": (80, 120, 240), "deg": 28.3, "ghost": True, "note": "165-year orbit: each season lasts about 41 years"},
  "say": "Number three. Neptune. Twenty eight degrees. Its year lasts a hundred sixty five of ours, so one summer lasts forty years. Then the list jumps."},
 {"rank": 2, "name": "Uranus", "tag": "rolling on its side", "num": "97.8°", "unit": "axial tilt",
  "source": "NASA Uranus Fact Sheet", "vis": {"type": "tilt", "kind": "ice", "col": (150, 215, 225), "deg": 97.8, "note": "each pole: 42 years of sun, then 42 years of night"},
  "say": "Number two. Uranus. Ninety eight degrees. It rolls around the Sun on its side. Each pole gets forty two years of daylight, then forty two years of night."},
 {"rank": 1, "name": "Venus", "tag": "flipped upside down", "num": "177.4°", "unit": "axial tilt · it spins backward",
  "source": "NASA Venus Fact Sheet", "vis": {"type": "tilt", "kind": "rock2", "col": (230, 195, 130), "deg": 177.4, "retro": True, "note": "on Venus, the Sun rises in the west"},
  "say": "And number one. Venus. A hundred seventy seven degrees. It's flipped upside down, so it spins backward. On Venus, the Sun rises in the west."},
]

OUTRO = {"say": "One planet upside down, one on its side. Which planet should we measure next? Subscribe to Cosmic Scale."}

SOURCES = ["NASA planetary fact sheets (NSSDC), obliquity to orbit: Venus 177.4°, Uranus 97.8°, Neptune 28.3°, Saturn 26.7°, Mars 25.2°, Earth 23.4°, Jupiter 3.1°",
           "NASA Science: Venus spins backward (retrograde), so the Sun rises in the west",
           "NASA Science: Uranus rotates on its side; each pole gets about 42 years of continuous sunlight followed by 42 years of darkness",
           "NASA: Saturn's rings appeared edge-on from Earth in March 2025",
           "Own calculations: Neptune's 165-year orbit divided by 4 seasons = about 41 years; Mars minus Earth = 1.8°"]
