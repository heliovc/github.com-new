# Ranking #9 — Top 5 Coldest Places in the Universe (Cosmic Scale)
# Ranked by lowest measured/inferred temperature. Twist: #2 is on our own Moon; #1 is colder than empty space itself (below the 2.7 K
# cosmic microwave background). Visual NEW: "kelvin" (Kelvin ruler 0–60 K, ice wall at absolute zero, 2.7 K line, the object frosts over).
# Hook: big number in frame 0 ("−272 °C") + frosted "?" nebula. Outro: full ruler + question "Which place should we put next?".
# Theme NEW: glacier white / violet. Own calc: K = °C + 273.15 (Uranus 49 K = −224 °C; Pluto −232 °C ≈ 41 K; Triton −235 °C ≈ 38 K;
# Hermite 26 K ≈ −247 °C; Boomerang ≈ 1 K ≈ −272 °C).
TITLE = "Top 5 Coldest Places in the Universe"
THEME = {"accent": (175, 150, 255), "accent2": (140, 235, 255), "star_col": (200, 230, 255), "tint": (20, 30, 70),
         "bar": "THE 5 COLDEST PLACES WE KNOW", "hook": "kelvin", "outro": "kelvin",
         "outro_note": "#1 is colder than empty space"}

HOOK = {"say": "Minus two seventy two. Colder than empty space itself. These are the five coldest places we know.",
        "big": "−272 °C", "top": "colder than empty space", "sub": "and #2 is on our own Moon"}

ITEMS = [
 {"rank": 5, "name": "Uranus", "short": "Uranus", "tag": "the coldest planet's air", "num": -224, "dec": 0, "suffix": " °C", "unit": "coldest planetary atmosphere",
  "source": "NASA / Voyager 2", "vis": {"type": "kelvin", "k": 49, "kind": "planet", "col": (150, 215, 225), "ring": True},
  "say": "Number five. Uranus. Its atmosphere dips to minus two twenty four degrees Celsius, the coldest of any planet, even though Neptune is farther out."},
 {"rank": 4, "name": "Pluto", "short": "Pluto", "tag": "the dwarf planet", "num": -232, "dec": 0, "suffix": " °C", "unit": "on its frozen surface",
  "source": "NASA / New Horizons", "vis": {"type": "kelvin", "k": 41, "kind": "planet", "col": (215, 190, 165)},
  "say": "Number four. Pluto. Its surface falls to about minus two thirty two, cold enough to freeze nitrogen solid."},
 {"rank": 3, "name": "Triton", "short": "Triton", "tag": "Neptune's largest moon", "num": -235, "dec": 0, "suffix": " °C", "unit": "measured by Voyager 2 in 1989",
  "source": "NASA / Voyager 2", "vis": {"type": "kelvin", "k": 38, "kind": "planet", "col": (225, 200, 205)},
  "say": "Number three. Triton, Neptune's biggest moon. Voyager two measured minus two thirty five, and still found geysers erupting."},
 {"rank": 2, "name": "Hermite Crater", "short": "Moon crater", "tag": "on our own Moon", "num": -247, "dec": 0, "suffix": " °C", "unit": "coldest ever measured in the solar system",
  "source": "NASA LRO / Diviner, 2009", "vis": {"type": "kelvin", "k": 26, "kind": "crater", "col": (190, 190, 200), "note": "about 26 K, in permanent shadow"},
  "say": "Number two is on our own Moon. Hermite crater, near the north pole, never sees sunlight. NASA's Lunar Reconnaissance Orbiter measured minus two forty seven."},
 {"rank": 1, "name": "Boomerang Nebula", "short": "Boomerang", "tag": "a dying star, 5,000 light-years away", "num": -272, "dec": 0, "suffix": " °C", "unit": "just 1 degree above absolute zero",
  "source": "ESA / NASA, ALMA (Sahai et al. 2013)", "vis": {"type": "kelvin", "k": 1, "kind": "nebula", "col": (150, 200, 255), "note": "colder than the 2.7 K glow of space"},
  "say": "And number one. The Boomerang Nebula. Gas blasting away from a dying star cools to minus two seventy two, colder than the glow of empty space."},
]

OUTRO = {"say": "Colder than empty space. Which place should we put next? Subscribe to Cosmic Scale."}

SOURCES = ["NASA Science, Uranus: minimum atmospheric temperature 49 K (−224 °C), the coldest planetary atmosphere in the solar system",
           "NASA Science, Pluto: surface temperatures of about −232 to −223 °C; nitrogen ice on the surface",
           "NASA Science, Triton: surface about −235 °C measured by Voyager 2 (1989); active geyser-like plumes",
           "NASA LRO / Diviner (Paige et al., 2009): Hermite crater floor about 26 K (≈ −247 °C), the coldest temperature measured in the solar system",
           "ESA / NASA Hubble and ALMA (Sahai et al., 2013): Boomerang Nebula about 1 K, about 5,000 light-years away, colder than the 2.7 K cosmic microwave background",
           "Own calculations: kelvin = °C + 273.15"]
