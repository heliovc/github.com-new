# Scale Short #7 — Our Entire Solar System Fits Inside This Black Hole (Cosmic Scale)
# Format: "X inside Y" — the solar system (orbits out to Neptune) inside the event horizon of M87*, to scale. Visual NEW: "bhfit" (black hole
# with photon ring + orbits to scale inside; zoom from the planets out to the horizon; mass counter; Voyager 1 line; light-crossing timer).
# Loop: the closing question flows back into the hook line ("...our entire solar system fits inside this black hole." -> same line at frame 0).
# Numbers: EHT / NASA: M87* has about 6.5 billion solar masses; first black hole image (April 2019).
# Own calc (Schwarzschild radius 2GM/c², non-spinning): r = 1.92e10 km = 128.3 AU, diameter ≈ 38.4 billion km = 257 AU; Neptune's orbit is
# 60.1 AU across -> 4.3 times; light crosses 38.4e9 km in 35.6 h; Voyager 1 ≈ 1 light-day = 173 AU from the Sun in Nov 2026 = 1.35 × r.
TITLE = "Our Entire Solar System Fits Inside This Black Hole"
THEME = {"accent": (255, 150, 70), "accent2": (130, 210, 255), "tint": (40, 14, 8)}
BIG = {"num": "38 BILLION KM", "top": "ACROSS ONE BLACK HOLE"}

BEATS = [
 {"say": "Our entire solar system fits inside this black hole.", "vis": {"type": "bhfit", "mode": "hook"}},
 {"say": "It's M87 star, the first black hole ever photographed. It holds the mass of six and a half billion Suns.",
  "vis": {"type": "bhfit", "mode": "mass", "head": {"num": "6.5 BILLION", "top": "TIMES THE SUN'S MASS"}}},
 {"say": "Start with our planets, and zoom out. Its event horizon, the point of no return, is about thirty eight billion kilometers across.",
  "vis": {"type": "bhfit", "mode": "zoom", "head": {"num": "38 BILLION KM", "top": "THE POINT OF NO RETURN"}}},
 {"say": "Neptune's whole orbit would fit across it more than four times.",
  "vis": {"type": "bhfit", "mode": "hook", "rows": True, "head": {"num": "4×", "top": "NEPTUNE'S ORBIT, SIDE BY SIDE"}}},
 {"say": "Put the Sun at its center, and Voyager one, after forty nine years of flight, would only just be outside the edge.",
  "vis": {"type": "bhfit", "mode": "voyager", "head": {"num": "49 YEARS", "top": "OF FLIGHT TO GET OUT"}}},
 {"say": "Even light would need a day and a half to cross it.",
  "vis": {"type": "bhfit", "mode": "light", "head": {"num": "35.6 HOURS", "top": "AT THE SPEED OF LIGHT"}}},
 {"say": "Bigger than you pictured? Tell me below. Because our entire solar system fits inside this black hole.",
  "vis": {"type": "bhfit", "mode": "hook"}},
]

SOURCES = ["Event Horizon Telescope Collaboration (2019), Astrophysical Journal Letters: M87* has about 6.5 billion times the mass of the Sun; first image of a black hole, released 10 April 2019",
           "NASA: Neptune orbits about 30.07 AU from the Sun (1 AU = 149.6 million km)",
           "NASA/JPL: Voyager 1 launched 5 September 1977 and reaches one light-day (about 25.9 billion km) from Earth in November 2026",
           "Own calculations: Schwarzschild radius 2GM/c² for 6.5 billion solar masses ≈ 19.2 billion km (128 AU), diameter ≈ 38.4 billion km; Neptune's orbit 60.1 AU across, 257 / 60.1 ≈ 4.3; light crossing 38.4 billion km / 299,792 km/s ≈ 35.6 hours; Voyager 1 at about 173 AU ≈ 1.35 times the radius (illustration with the Sun placed at the centre)"]
