# Scale Short #9 — Every Other Planet Fits Inside Jupiter (Cosmic Scale)
# Format: "X inside Y" — pour all seven other planets into Jupiter BY VOLUME: Saturn alone fills 58%, the ice giants take it to 67%, the four
# rocky worlds add 0.16%, and a third is still empty (room for about 435 more Earths). Visual NEW: "jupfill" (glass-globe Jupiter filled
# with coloured layers; planets fall in to scale). Loop: the closing question flows back into the hook line.
# Volumes (NASA Planetary Fact Sheet, 10^10 km³): Jupiter 143,128; Saturn 82,713; Uranus 6,833; Neptune 6,254; Earth 108.321; Venus 92.843;
# Mars 16.318; Mercury 6.083. Own calc: Jupiter / Earth = 1,321; Saturn / Jupiter = 57.8%; + Uranus + Neptune = 66.9%; rocky four = 223.6
# = 0.156%; all seven = 96,024 = 67.1%; empty 47,104 / 108.321 = 435 Earths.
TITLE = "Every Other Planet Fits Inside Jupiter"
THEME = {"accent": (255, 190, 110), "accent2": (150, 225, 230), "tint": (60, 34, 12)}
BIG = {"num": "67%", "top": "ALL 7 OTHER PLANETS INSIDE JUPITER"}

BEATS = [
 {"say": "Every other planet fits inside Jupiter.", "vis": {"type": "jupfill", "mode": "hook"}},
 {"say": "Jupiter is so big it could hold thirteen hundred Earths. So let's pour. Saturn alone fills more than half of it.",
  "vis": {"type": "jupfill", "mode": "pour", "add": ["Saturn"], "head": {"num": "57.8%", "top": "SATURN ALONE"}}},
 {"say": "Add Uranus and Neptune, and we're at two thirds.",
  "vis": {"type": "jupfill", "mode": "pour", "before": ["Saturn"], "add": ["Uranus", "Neptune"], "head": {"num": "66.9%", "top": "+ URANUS + NEPTUNE"}}},
 {"say": "Now Venus, Earth, Mars and Mercury. The level barely moves. All four add less than a fifth of a percent.",
  "vis": {"type": "jupfill", "mode": "pour", "before": ["Saturn", "Uranus", "Neptune"], "add": ["Venus", "Earth", "Mars", "Mercury"], "head": {"num": "+0.16%", "top": "ALL 4 ROCKY PLANETS"}}},
 {"say": "And a third of Jupiter is still empty. Room for about four hundred thirty five more Earths.",
  "vis": {"type": "jupfill", "mode": "room", "head": {"num": "435 EARTHS", "top": "STILL FIT IN THE EMPTY THIRD"}}},
 {"say": "Did you expect that much room? Tell me below. Because every other planet fits inside Jupiter.",
  "vis": {"type": "jupfill", "mode": "hook"}},
]

SOURCES = ["NASA Planetary Fact Sheet (NSSDC): volumes in 10^10 km³ — Jupiter 143,128; Saturn 82,713; Uranus 6,833; Neptune 6,254; Earth 108.321; Venus 92.843; Mars 16.318; Mercury 6.083",
           "Own calculations: Jupiter holds 143,128 / 108.321 ≈ 1,321 Earths by volume; Saturn = 57.8% of Jupiter; with Uranus and Neptune 66.9%; the four rocky planets 223.6 = 0.16%; all seven 96,024 = 67.1%; empty 47,104 ≈ 435 Earths (volumes only, as if melted and poured; real planets are not compressible like this)"]
