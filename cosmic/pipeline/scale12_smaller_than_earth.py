# Scale Short #12 — This Star Is Smaller Than Earth. It Weighs as Much as the Sun (Cosmic Scale)
# Format: "small vs giant" — Sirius B (white dwarf): radius 0.0081 solar radii = 5,635 km (11,270 km across vs Earth's 12,742 km),
# mass 1.018 Suns = 339,000 Earths (Bond et al. 2017). Own calc: mean density 2.7 × 10^9 kg/m³ -> a 5 mL teaspoon ≈ 13.5 tonnes;
# surface gravity GM/r² ≈ 433,000 × Earth's (70 kg person -> 30 million kg). Visual NEW: "dwarf". Ties to EP17 (Sirius B swap).
# Loop: the closing question flows back into the hook line.
TITLE = "This Star Is Smaller Than Earth. It Weighs as Much as the Sun"
THEME = {"accent": (150, 200, 255), "accent2": (255, 215, 140), "tint": (10, 16, 38)}
BIG = {"num": "339,000 EARTHS", "top": "OF MASS, SMALLER THAN EARTH"}

BEATS = [
 {"say": "This star is smaller than Earth.", "vis": {"type": "dwarf", "mode": "hook"}},
 {"say": "But it weighs as much as the Sun. Three hundred thirty nine thousand Earths, crushed into one ball that would fit inside our planet.",
  "vis": {"type": "dwarf", "mode": "mass", "head": {"num": "1 SUN", "top": "OF MASS IN SIRIUS B"}}},
 {"say": "A single teaspoon of it would weigh about thirteen tonnes. As much as two full-grown elephants.",
  "vis": {"type": "dwarf", "mode": "spoon", "head": {"num": "13.5 TONNES", "top": "PER TEASPOON (AVERAGE)"}}},
 {"say": "Stand on it, and you'd weigh over four hundred thousand times more than you do right now.",
  "vis": {"type": "dwarf", "mode": "gravity", "head": {"num": "433,000 g", "top": "SURFACE GRAVITY"}}},
 {"say": "It's Sirius B. The dead core of a star, circling Sirius, the brightest star in our night sky. One day, our Sun will end up like this too.",
  "vis": {"type": "dwarf", "mode": "sirius", "head": {"num": "SIRIUS B", "top": "A WHITE DWARF"}}},
 {"say": "Which dead star should we weigh next? Because this star is smaller than Earth.",
  "vis": {"type": "dwarf", "mode": "hook"}},
]

SOURCES = ["Bond et al. 2017 (Astrophysical Journal, Hubble astrometry): Sirius B mass 1.018 solar masses, radius 0.0081 solar radii (about 5,635 km); orbital period about 50 years; Sirius is 8.6 light-years away",
           "NASA Earth Fact Sheet: Earth mean diameter 12,742 km; 1 solar mass = 332,946 Earth masses",
           "Own calculations: average density = mass ÷ volume ≈ 2.7 × 10^9 kg/m³, so a 5 mL teaspoon ≈ 13.5 tonnes (an African elephant weighs about 6 tonnes); surface gravity GM/r² ≈ 433,000 × Earth's; Sun's surface gravity ≈ 28 × Earth's, Jupiter's ≈ 2.5 ×"]
