# Scale Short #16 — If the Sun Were a Grain of Sand, the Next Star Would Be 29 km Away (Cosmic Scale)
# Format: "small vs giant" (a scale model). Sun mean diameter 1,391,400 km (NASA fact sheet, radius 695,700) -> 1 mm.
# Own calc: Earth 12,742 km -> 0.009 mm (9 µm; a human hair is roughly 50–100 µm); Earth–Sun 149.6 million km -> 10.8 cm;
# Neptune 30.07 AU -> 3.2 m; Voyager 1 ~173 AU (one light-day, Nov 2026) -> 18.6 m; Proxima Centauri 4.25 ly -> 28.9 km;
# Milky Way ~100,000 ly (NASA) -> 680,000 km = 1.77 × the Earth–Moon distance (384,400 km). 1 ly = 9.4607 × 10^12 km.
# Hook ≤ 2 s; number on frame 0; the closing question loops into the hook. Visual NEW: "sand". Ties to EP15 (Voyager 1).
TITLE = "Shrink the Sun to a Grain of Sand. The Next Star Is 29 km Away"
THEME = {"accent": (255, 200, 90), "accent2": (150, 230, 255), "tint": (10, 20, 40)}
BIG = {"num": "29 KM", "top": "TO THE NEXT GRAIN OF SAND"}

BEATS = [
 {"say": "Make the Sun a grain of sand.", "vis": {"type": "sand", "mode": "hook"}},
 {"say": "Earth becomes a speck, thinner than a human hair, about ten centimeters from the grain.",
  "vis": {"type": "sand", "mode": "earth", "head": {"num": "9 MICRONS", "top": "EARTH, AT THIS SCALE"}}},
 {"say": "Neptune, the last planet, three meters out. Voyager 1, the farthest thing we ever built, after forty nine years of flying: under twenty meters.",
  "vis": {"type": "sand", "mode": "ruler", "head": {"num": "18.6 M", "top": "OUR FARTHEST SPACECRAFT"}}},
 {"say": "Then nothing at all. Twenty nine kilometers of empty dark, about a six hour walk, before the next grain: Proxima Centauri.",
  "vis": {"type": "sand", "mode": "gap"}},
 {"say": "And our whole galaxy, at this scale, is wider than the trip to the Moon. So, what should we shrink next?",
  "vis": {"type": "sand", "mode": "galaxy", "head": {"num": "680,000 KM", "top": "THE MILKY WAY, SHRUNK"}}},
]

SOURCES = ["NASA Sun Fact Sheet (NSSDC): mean radius 695,700 km (diameter 1,391,400 km, scaled to 1 mm)",
           "NASA: Earth diameter 12,742 km; Earth–Sun distance 149.6 million km; Neptune about 30.07 times the Earth–Sun distance",
           "NASA/JPL: Voyager 1 reached one light-day (about 173 times the Earth–Sun distance) in November 2026; launched 1977",
           "NASA: Proxima Centauri about 4.2 light-years away; the Milky Way's disk about 100,000 light-years across",
           "Own calculations: 1 mm = 1,391,400 km, so Earth 0.009 mm at 10.8 cm, Neptune 3.2 m, Voyager 1 18.6 m, Proxima 28.9 km, Milky Way 680,000 km (1.8 × the 384,400 km Earth–Moon distance)"]
