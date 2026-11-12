# Scale Short #3 — This Star Fits Inside Jupiter (Cosmic Scale)
# Format: "small vs giant" / "X inside Y" — a REAL star (EBLM J0555-57Ab, Cambridge 2017) drawn to scale inside Jupiter's disc.
# Paradox: 85 Jupiters of mass, smaller than Jupiter (gravity crushes it). Visual NEW: "starinside" (inside / balance / saturn / limit).
# Loop: the closing question flows back into the hook line ("...this star fits inside Jupiter." -> "This star fits inside Jupiter.").
# Numbers: ~85 Jupiter masses, radius ~0.84 Jupiter's (≈ 59,000 km, close to Saturn's 58,232 km), ~600 light-years away, orbits a Sun-like
# star; just above the hydrogen-fusion limit (~80 Jupiter masses). Own calc: 59,000 / 71,492 ≈ 0.83.
TITLE = "This Star Fits Inside Jupiter"
THEME = {"accent": (255, 110, 70), "accent2": (255, 215, 140), "tint": (60, 20, 16)}
BIG = {"num": "85 JUPITERS", "top": "OF MASS. SMALLER THAN JUPITER."}

BEATS = [
 {"say": "This star fits inside Jupiter.", "vis": {"type": "starinside", "mode": "inside"}},
 {"say": "It's real. It's called EBLM J0555-57Ab, about six hundred light years away, and it shines by fusing hydrogen like the Sun.",
  "vis": {"type": "starinside", "mode": "inside", "drop": True, "head": {"num": "A REAL STAR", "top": "FOUND IN 2017"}}},
 {"say": "It weighs as much as eighty five Jupiters put together.",
  "vis": {"type": "starinside", "mode": "balance", "head": {"num": "85×", "top": "THE MASS OF JUPITER"}}},
 {"say": "But it's only about the size of Saturn. All that mass crushes it smaller.",
  "vis": {"type": "starinside", "mode": "saturn", "head": {"num": "SATURN-SIZED", "top": "≈ 0.84 × JUPITER'S WIDTH"}}},
 {"say": "Any lighter, and it couldn't fuse hydrogen at all. It's right at the edge of being a star.",
  "vis": {"type": "starinside", "mode": "limit", "head": {"num": "JUST BARELY", "top": "A STAR"}}},
 {"say": "So is it more like a star or a planet? Tell me below. Because this star fits inside Jupiter.",
  "vis": {"type": "starinside", "mode": "inside", "loop": True}},
]

SOURCES = ["University of Cambridge (July 2017), von Boetticher et al., Astronomy & Astrophysics: EBLM J0555-57Ab, about 85 Jupiter masses, slightly larger than Saturn, about 600 light-years away, orbiting a Sun-like star; just massive enough to fuse hydrogen",
           "NASA Planetary Fact Sheets: Jupiter radius 71,492 km, Saturn radius 58,232 km",
           "Own calculation: star radius ≈ 0.84 Jupiter radii ≈ 59,000 km, so it fits inside Jupiter's disc"]
