# Scale Short #2 — Earth Fits Inside a Storm on Jupiter (Barely) (Cosmic Scale)
# Format: "X inside Y" — Earth dropped, TO SCALE, inside Jupiter's Great Red Spot. Twist: the storm used to hold about 3 Earths and is shrinking.
# Visual NEW: "storm" (procedural banded Jupiter, zoom planet -> spot, spot width tied to a year counter). Loop: the closing question
# flows back into the hook line ("...this storm. Barely." -> "Earth fits inside this storm.").
# Numbers: GRS ≈ 16,000 km wide (NASA/Juno 2017, ~1.3 Earths); late 1800s up to ≈ 41,000 km (NASA/Hubble 2014) ≈ 3.2 Earths;
# Jupiter 142,984 km = 11.2 Earths wide. Own calc: 16,000 / 12,742 = 1.26; 41,000 / 12,742 = 3.2.
TITLE = "Earth Fits Inside a Storm on Jupiter"
THEME = {"accent": (255, 150, 100), "accent2": (255, 225, 170), "tint": (50, 24, 14)}
BIG = {"num": "1.3 EARTHS", "top": "FIT INSIDE ONE STORM"}

BEATS = [
 {"say": "Earth fits inside this storm.", "vis": {"type": "storm", "z0": 1.0, "earths": 1}},
 {"say": "It's on Jupiter. The Great Red Spot, a storm that has been raging for at least a hundred and fifty years.",
  "vis": {"type": "storm", "z0": 1.0, "z1": 0.0, "label_planet": True, "head": {"num": "JUPITER", "top": "11 EARTHS WIDE"}}},
 {"say": "Zoom in. It's about sixteen thousand kilometers wide. Drop Earth in, and it fits.",
  "vis": {"type": "storm", "z0": 0.0, "z1": 1.0, "earths": 1, "drop": True, "head": {"num": "16,000 KM", "top": "WIDE. EARTH: 12,742 KM"}}},
 {"say": "But in the late eighteen hundreds, it was up to forty one thousand kilometers wide. Room for three Earths.",
  "vis": {"type": "storm", "z0": 1.0, "z1": 0.72, "y0": 2017, "y1": 1880, "earths": "auto", "show_year": True, "head": {"num": "3 EARTHS", "top": "IN THE 1800s"}}},
 {"say": "It has been shrinking ever since, and nobody knows exactly why.",
  "vis": {"type": "storm", "z0": 0.72, "z1": 1.0, "y0": 1880, "y1": 2017, "earths": "auto", "show_year": True, "head": {"num": "SHRINKING", "top": "AND NO ONE KNOWS WHY"}}},
 {"say": "Will it still fit Earth in fifty years? Tell me below. Because right now, Earth fits inside this storm. Barely.",
  "vis": {"type": "storm", "z0": 1.0, "earths": 1, "loop": True}},
]

SOURCES = ["NASA / JPL (Juno, 2017): the Great Red Spot measured about 16,000 km (10,159 miles) wide, about 1.3 times Earth's width",
           "NASA / Hubble (2014): historic observations from the late 1800s gauged the storm as large as about 41,000 km (25,500 miles) on its long axis; observed continuously since at least the 1870s (Simon et al. 2018, Astronomical Journal)",
           "NASA Planetary Fact Sheets: Jupiter diameter 142,984 km, Earth 12,742 km (Jupiter ≈ 11 Earths wide)",
           "Own calculation: 16,000 / 12,742 ≈ 1.3 Earths; 41,000 / 12,742 ≈ 3.2 Earths"]
