# Scale Short #11 — Squeeze Earth Into a Marble and It Becomes a Black Hole (Cosmic Scale)
# Format: "small vs giant" — Earth's Schwarzschild radius r = 2GM/c² = 8.87 mm -> a black hole 17.7 mm across (a marble). Same for the Sun:
# r = 2.95 km -> 5.9 km across (~1 h 10 min on foot at 5 km/h). Squeeze factor 12,742 km / 17.7 mm ≈ 720 million.
# Visual NEW: "marble" (marble-sized black hole on a real-size ruler, balance, log squeeze past Moon/city/field/person, Sun on a walking bar).
# Loop: the closing question flows back into the hook line.
# Constants: G = 6.674e-11, c = 2.998e8 m/s, M_earth = 5.972e24 kg (NASA Earth Fact Sheet), M_sun = 1.989e30 kg (NASA Sun Fact Sheet).
TITLE = "Squeeze Earth Into a Marble and It Becomes a Black Hole"
THEME = {"accent": (255, 185, 90), "accent2": (190, 150, 255), "tint": (26, 14, 44)}
BIG = {"num": "1.77 cm", "top": "EARTH AS A BLACK HOLE"}

BEATS = [
 {"say": "This marble is a black hole.", "vis": {"type": "marble", "mode": "hook"}},
 {"say": "Not just any black hole. It has the entire mass of Earth. Six trillion trillion kilograms.",
  "vis": {"type": "marble", "mode": "mass", "head": {"num": "SAME MASS", "top": "EARTH = THE MARBLE"}}},
 {"say": "To make it, squeeze the whole planet, past the size of the Moon, a city, a person, down to under two centimeters.",
  "vis": {"type": "marble", "mode": "squeeze", "head": {"num": "720 MILLION×", "top": "SMALLER IN WIDTH"}}},
 {"say": "Do the same to the Sun, and it ends up six kilometers wide. You could walk across it in about an hour.",
  "vis": {"type": "marble", "mode": "sun", "head": {"num": "5.9 km", "top": "THE SUN AS A BLACK HOLE"}}},
 {"say": "Nothing can actually crush Earth like that. Only giant stars, far heavier than the Sun, ever collapse this far.",
  "vis": {"type": "marble", "mode": "star", "head": {"num": "NOT EARTH", "top": "ONLY GIANT STARS DO THIS"}}},
 {"say": "What should we squeeze next? Because this marble is a black hole.",
  "vis": {"type": "marble", "mode": "hook"}},
]

SOURCES = ["NASA Earth Fact Sheet: Earth's mass 5.972 × 10^24 kg, mean diameter 12,742 km; NASA Sun Fact Sheet: Sun's mass 1.989 × 10^30 kg",
           "Schwarzschild radius r = 2GM/c² (G = 6.674 × 10^-11, c = 299,792 km/s)",
           "Own calculations: Earth r = 8.87 mm (17.7 mm across, about a marble); Sun r = 2.95 km (5.9 km across, about 70 minutes on foot at 5 km/h); squeeze factor 12,742 km / 17.7 mm ≈ 720 million",
           "NASA: stellar-mass black holes form when massive stars collapse at the end of their lives"]
