# Ranking #8 — Top 5 Brightest Stars in the Night Sky (Cosmic Scale)
# Ranked by apparent magnitude (the Sun excluded; Alpha Centauri A+B counted together, as the eye sees them).
# Twist per item: how bright it LOOKS vs how powerful it REALLY IS (luminosity × Sun, log meter) — Sirius looks brightest but is ~25× the Sun;
# Canopus is ~10,000× the Sun but 36× farther. Visual NEW: "glow" (night horizon + star at its apparent brightness + luminosity meter).
# Hook: big number in frame 0 ("10,000× THE SUN") with five unnamed stars, #2 pulsing. Outro: the meter with all five + question.
# Theme NEW: ice blue / amber. Own calc: Canopus 310 ly / Sirius 8.6 ly ≈ 36×.
TITLE = "Top 5 Brightest Stars in the Night Sky"
THEME = {"accent": (255, 196, 92), "accent2": (150, 205, 255), "star_col": (200, 225, 255), "tint": (12, 30, 60),
         "bar": "THE 5 BRIGHTEST STARS IN THE NIGHT SKY", "hook": "glow", "outro": "glow",
         "outro_note": "Brightest-looking is not most powerful"}

HOOK = {"say": "Ten thousand Suns. That's how powerful the second brightest star in our sky really is. Here are the five brightest stars at night.",
        "big": "10,000× THE SUN", "top": "and it's only #2", "sub": "brightest-looking ≠ most powerful"}

ITEMS = [
 {"rank": 5, "name": "Vega", "short": "Vega", "tag": "the summer star of the north", "num": 0.03, "dec": 2, "suffix": "", "unit": "magnitude (lower = brighter)",
  "source": "NASA / Hipparcos catalogue", "vis": {"type": "glow", "ly": 25, "lum": 40, "col": (190, 215, 255)},
  "say": "Number five. Vega, twenty five light years away. About forty times as powerful as the Sun."},
 {"rank": 4, "name": "Arcturus", "short": "Arcturus", "tag": "an orange giant", "num": -0.05, "dec": 2, "suffix": "", "unit": "magnitude (lower = brighter)",
  "source": "NASA / Hipparcos catalogue", "vis": {"type": "glow", "ly": 37, "lum": 170, "col": (255, 170, 90)},
  "say": "Number four. Arcturus, an orange giant thirty seven light years away, putting out around a hundred and seventy Suns."},
 {"rank": 3, "name": "Alpha Centauri", "short": "Alpha Cen", "tag": "two Sun-like stars", "num": -0.27, "dec": 2, "suffix": "", "unit": "magnitude (lower = brighter)",
  "source": "NASA", "vis": {"type": "glow", "ly": 4.37, "lum": 2, "col": (255, 230, 170)},
  "say": "Number three. Alpha Centauri. Together, barely two Suns of power. It looks bright only because it's our closest neighbor, four point four light years away."},
 {"rank": 2, "name": "Canopus", "short": "Canopus", "tag": "a supergiant of the southern sky", "num": -0.74, "dec": 2, "suffix": "", "unit": "magnitude (lower = brighter)",
  "source": "NASA / Hipparcos catalogue", "vis": {"type": "glow", "ly": 310, "lum": 10000, "col": (235, 240, 255)},
  "say": "Number two. Canopus. About ten thousand times as powerful as the Sun, but three hundred ten light years away. Thirty six times farther than number one."},
 {"rank": 1, "name": "Sirius", "short": "Sirius", "tag": "the Dog Star", "num": -1.46, "dec": 2, "suffix": "", "unit": "magnitude (lower = brighter)",
  "source": "NASA / Hipparcos catalogue", "vis": {"type": "glow", "ly": 8.6, "lum": 25, "col": (200, 225, 255)},
  "say": "And number one. Sirius. Only about twenty five Suns, but just eight point six light years away. The brightest star in the night sky wins by being close."},
]

OUTRO = {"say": "Brightest looking is not most powerful. Which star should we put next? Subscribe to Cosmic Scale."}

SOURCES = ["Hipparcos catalogue (ESA) / NASA: apparent magnitudes Sirius −1.46, Canopus −0.74, Alpha Centauri A+B −0.27, Arcturus −0.05, Vega +0.03",
           "NASA Science / NASA Imagine the Universe: distances Sirius 8.6 ly, Alpha Centauri 4.37 ly, Vega 25 ly, Arcturus about 37 ly, Canopus about 310 ly",
           "Luminosities (approximate, stellar catalogues): Sirius A about 25 Suns, Canopus about 10,000 Suns, Arcturus about 170 Suns, Vega about 40 Suns, Alpha Centauri A+B about 2 Suns",
           "Own calculation: Canopus is about 310 / 8.6 ≈ 36 times farther away than Sirius"]
