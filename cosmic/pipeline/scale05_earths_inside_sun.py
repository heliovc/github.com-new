# Scale Short #5 — 1.3 Million Earths Fit Inside the Sun (Cosmic Scale)
# Format: "X inside Y" — Earth vs the Sun, to scale. Visual NEW: "fillsun" (hook: Sun + a tiny Earth beside it; row: 109 Earths across the
# diameter; fill: Earths pour into the disc while a counter runs to 1.3 million; door: Sun = 2 m front door, Earth = 18 mm coin).
# Loop: the closing question flows back into the hook line ("...1.3 million Earths fit inside the Sun." -> same line at frame 0).
# Numbers (NASA): Sun diameter about 1,392,000 km, about 109 Earths; about 1.3 million Earths fit inside by volume. Own calc: 1,392,000 /
# 12,742 = 109.2; 109.2³ ≈ 1.30 million; packed as whole balls (≈ 74% at best) ≈ 960,000; 2 m / 109.2 ≈ 18 mm.
TITLE = "1.3 Million Earths Fit Inside the Sun"
THEME = {"accent": (255, 200, 60), "accent2": (90, 200, 255), "tint": (50, 30, 6)}
BIG = {"num": "1,300,000", "top": "EARTHS FIT INSIDE THE SUN"}

BEATS = [
 {"say": "One point three million Earths fit inside the Sun.", "vis": {"type": "fillsun", "mode": "hook"}},
 {"say": "Line Earths up across the Sun's face, and you need one hundred and nine of them.",
  "vis": {"type": "fillsun", "mode": "row", "head": {"num": "109 EARTHS", "top": "ACROSS THE SUN"}}},
 {"say": "But the Sun is a ball. So it's one hundred nine, times one hundred nine, times one hundred nine. About one point three million Earths, by volume.",
  "vis": {"type": "fillsun", "mode": "fill", "head": {"num": "109 × 109 × 109", "top": "≈ 1.3 MILLION"}}},
 {"say": "Packed as whole balls, with gaps between them, it's closer to nine hundred sixty thousand. Still almost a million.",
  "vis": {"type": "fillsun", "mode": "fill", "count": 960000, "head": {"num": "≈ 960,000", "top": "PACKED AS WHOLE BALLS"}}},
 {"say": "Shrink the Sun to the size of a front door, and Earth is a coin, under two centimeters wide.",
  "vis": {"type": "fillsun", "mode": "door", "head": {"num": "2 M vs 18 MM", "top": "THE SUN AS A DOOR"}}},
 {"say": "Did you guess higher, or lower? Tell me below. Because one point three million Earths fit inside the Sun.",
  "vis": {"type": "fillsun", "mode": "hook"}},
]

SOURCES = ["NASA Science, Sun facts: the Sun is about 1,392,000 km (865,000 miles) wide, about 109 Earths, and about 1.3 million Earths could fit inside it",
           "NASA Earth fact sheet: Earth's mean diameter 12,742 km",
           "Own calculations: 1,392,000 / 12,742 ≈ 109.2; 109.2³ ≈ 1.30 million (by volume; packed as whole balls, at most about 74% of the space is filled, so about 960,000); Sun as a 2 m door, so Earth ≈ 2,000 mm / 109.2 ≈ 18 mm"]
