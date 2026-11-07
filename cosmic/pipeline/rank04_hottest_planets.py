# Ranking #4 — Top 5 Hottest Planets Ever Found (Cosmic Scale)
# Visual NEW: "heat" — tall thermometer (0–5,600 °C, linear) with reference marks (lead melts, lava, iron boils, Sun's surface),
# column rising to each planet, planet glowing in its temperature colour. Theme lava red / yellow.
TITLE = "Top 5 Hottest Planets Ever Found"
THEME = {"accent": (255, 92, 40), "accent2": (255, 214, 70), "star_col": (255, 150, 60), "tint": (70, 18, 8),
         "bar": "THE 5 HOTTEST PLANETS EVER FOUND", "hook": "heat", "outro": "heat",
         "outro_note": "from melting lead to hotter than a star"}

HOOK = {"say": "Number one on this list is hotter than most stars. These are the five hottest planets ever found.",
        "top": "Hottest planets ever found", "sub": "#1 is hotter than most stars"}

ITEMS = [
 {"rank": 5, "name": "Venus", "short": "Venus", "tag": "our solar system · hotter than Mercury", "num": 475, "suffix": " °C", "unit": "at the surface",
  "source": "NASA", "vis": {"type": "heat", "temp": 475, "look": "venus"},
  "say": "Number five. Venus, the hottest planet in our solar system. About four hundred and seventy five degrees Celsius, hot enough to melt lead, even though Mercury is closer to the Sun. Its thick air traps the heat."},
 {"rank": 4, "name": "55 Cancri e", "short": "55 Cnc e", "tag": "super-Earth · 41 light-years away", "num": 1540, "suffix": " °C", "unit": "on the day side",
  "source": "NASA / JWST (2024)", "vis": {"type": "heat", "temp": 1540, "look": "lava"},
  "say": "Number four. Fifty five Cancri e, a super Earth forty one light years away. The James Webb telescope measured its day side at about fifteen hundred degrees. Its surface is probably an ocean of magma."},
 {"rank": 3, "name": "WASP-121b", "short": "WASP-121b", "tag": "football-shaped · 900 light-years", "num": 2500, "suffix": " °C", "unit": "in the upper atmosphere",
  "source": "NASA / Hubble (2019)", "vis": {"type": "heat", "temp": 2500, "look": "football"},
  "say": "Number three. WASP one twenty one b. Its upper atmosphere reaches about twenty five hundred degrees. It's so close to its star that it's stretched into a football shape, and it's leaking iron into space."},
 {"rank": 2, "name": "WASP-189b", "short": "WASP-189b", "tag": "20× closer to its star than Earth", "num": 3200, "suffix": " °C", "unit": "on the day side",
  "source": "ESA CHEOPS (2020)", "vis": {"type": "heat", "temp": 3200, "look": "gas"},
  "say": "Number two. WASP one eighty nine b. About thirty two hundred degrees, measured by the European CHEOPS telescope. It orbits twenty times closer to its star than we are to the Sun."},
 {"rank": 1, "name": "KELT-9b", "short": "KELT-9b", "tag": "a year lasts 1.5 days", "num": 4300, "suffix": " °C", "unit": "on the day side · hotter than most stars",
  "source": "NASA JPL", "vis": {"type": "heat", "temp": 4300, "look": "gas"},
  "say": "And number one. KELT nine b. A day side of about forty three hundred degrees, hotter than most stars. A year there lasts less than two days, and its star may be boiling its atmosphere away."},
]

OUTRO = {"say": "From melting lead to hotter than a star. Subscribe to Cosmic Scale for more."}

SOURCES = ["NASA Science, Venus: Facts (surface about 475 °C / 900 °F; hottest planet in the solar system; thick CO2 atmosphere traps heat)",
           "NASA JPL (May 2024), Webb hints at possible atmosphere around 55 Cancri e (day side about 1,540 °C / 2,800 °F; 41 light-years; likely magma ocean)",
           "NASA Hubble (Aug 2019), WASP-121b 'heavy metal' exoplanet (upper atmosphere about 2,500 °C / 4,600 °F; football-shaped; iron and magnesium escaping; ~900 light-years)",
           "University of Geneva / ESA CHEOPS (Sept 2020), WASP-189b (day side about 3,200 °C; 20 times closer to its star than Earth to the Sun; 322 light-years)",
           "NASA JPL (June 2017), KELT-9b: planet hotter than most stars (day side about 4,300 °C / 7,800 °F; orbit about 1.5 days; may be evaporating)",
           "Reference marks: lead melts at 327 °C; iron boils at 2,862 °C; NASA: Sun's surface about 5,500 °C"]
