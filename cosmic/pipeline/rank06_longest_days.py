# Ranking #6 — Top 5 Longest Days in the Solar System (Cosmic Scale)
# "Day" = solar day (sunrise to sunrise), among planets, dwarf planets and major moons.
# Visual NEW: "daylight" — the world with a live day/night terminator while a Sun circles it (one loop = one solar day),
# + a linear ruler 0–180 Earth days where Earth's day is a hairline. Hook = Mercury "?" barely turning vs Earth spinning; outro = 5 bars.
# Theme NEW lime / graphite.
# Twist at #1: Venus spins slowest (243 d) but Mercury's solar day (176 d) is longer — 2 Mercury years (88 d each).
TITLE = "Top 5 Longest Days in the Solar System"
THEME = {"accent": (200, 250, 80), "accent2": (235, 240, 225), "star_col": (200, 250, 80), "tint": (30, 36, 30),
         "bar": "THE 5 LONGEST DAYS IN THE SOLAR SYSTEM", "hook": "daylight", "outro": "daylight",
         "outro_note": "On Mercury, the daylight alone lasts a full year"}

HOOK = {"say": "On one world in our solar system, a single day lasts longer than two of its years. These are the five longest days in the solar system.",
        "top": "Longest days in the solar system", "sub": "#1: one day = two of its years"}

ITEMS = [
 {"rank": 5, "name": "Eris", "short": "Eris", "tag": "dwarf planet beyond Pluto", "num": 15.8, "dec": 1, "suffix": " DAYS", "unit": "from sunrise to sunrise (in Earth days)",
  "source": "Szakáts et al., Astronomy & Astrophysics (2023)", "vis": {"type": "daylight", "days": 15.8, "col": (215, 215, 225), "note": "locked face to face with its moon Dysnomia"},
  "say": "Number five. Eris, a dwarf planet far beyond Pluto. One day there lasts fifteen point eight Earth days, because Eris is locked face to face with its own small moon, Dysnomia."},
 {"rank": 4, "name": "Our Moon", "short": "Moon", "tag": "the one in your sky", "num": 29.5, "dec": 1, "suffix": " DAYS", "unit": "from sunrise to sunrise (in Earth days)",
  "source": "NASA", "vis": {"type": "daylight", "days": 29.5, "col": (175, 172, 168), "note": "two weeks of daylight, then two weeks of night"},
  "say": "Number four. Our own Moon. From one sunrise to the next takes twenty nine and a half days. That's two weeks of blazing daylight, then two weeks of night."},
 {"rank": 3, "name": "Iapetus", "short": "Iapetus", "tag": "a moon of Saturn", "num": 79, "suffix": " DAYS", "unit": "from sunrise to sunrise (in Earth days)",
  "source": "NASA / Cassini", "vis": {"type": "daylight", "days": 79, "col": (225, 220, 205), "note": "one half is as dark as a blackboard"},
  "say": "Number three. Iapetus, a moon of Saturn. Its day lasts seventy nine Earth days. And one half of Iapetus is as dark as a blackboard, while the other half is bright and icy."},
 {"rank": 2, "name": "Venus", "short": "Venus", "tag": "it spins backwards", "num": 117, "suffix": " DAYS", "unit": "from sunrise to sunrise (in Earth days)",
  "source": "NASA", "vis": {"type": "daylight", "days": 117, "col": (235, 205, 140), "note": "the Sun rises in the west"},
  "say": "Number two. Venus. Sunrise to sunrise takes about a hundred and seventeen Earth days. And because Venus spins backwards, the Sun rises in the west."},
 {"rank": 1, "name": "Mercury", "short": "Mercury", "tag": "closest to the Sun", "num": 176, "suffix": " DAYS", "unit": "from sunrise to sunrise = 2 Mercury years",
  "source": "NASA", "vis": {"type": "daylight", "days": 176, "col": (160, 150, 140), "note": "Venus spins slower. Mercury's day is still longer."},
  "say": "And number one. Mercury. Here's the twist. Venus actually spins slower. But Mercury's day is longer. One sunrise to the next takes one hundred and seventy six Earth days. That's two full Mercury years, for a single day."},
]

OUTRO = {"say": "On Mercury, the daylight alone lasts a full year. Subscribe to Cosmic Scale."}

SOURCES = ["Szakáts et al. (2023), Astronomy & Astrophysics 669, L3: Eris rotates in 15.8 days, tidally locked to the orbit of its moon Dysnomia",
           "NASA Science, Earth's Moon: one lunar day (sunrise to sunrise) lasts about 29.5 Earth days",
           "NASA / Cassini (via BBC Sky at Night): Iapetus orbits Saturn in 79 days and rotates in the same time; its leading side is as dark as a blackboard",
           "NASA Venus fact sheet (Venus lithograph): rotation 243.02 Earth days, retrograde; 116.75 days between successive sunrises",
           "NASA / BBC Sky at Night: Mercury rotates in about 59 Earth days, orbits in 88 days; one solar day lasts 176 Earth days (two Mercury years)"]
