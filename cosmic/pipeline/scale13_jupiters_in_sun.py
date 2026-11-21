# Scale Short #13 — 986 Jupiters Fit Inside the Sun (Cosmic Scale)
# Format: "X inside Y" — volumes from the NASA fact sheets: Sun 1,412,000 × 10^12 km³, Jupiter 1,431.28 × 10^12 km³ -> 986.5.
# Mean radii 695,700 / 69,911 km -> 9.95 Jupiters across. Jupiter = 1,321 Earths by volume. Mass: Sun 1,988,500 / Jupiter 1,898.1
# (× 10^24 kg) = 1,047.6. Densities 1.408 vs 1.326 g/cm³ -> why the two numbers are so close. Visual NEW: "jupsun". Ties to EP10.
# Loop: the closing question is followed by the hook line "986 Jupiters fit inside the Sun".
TITLE = "986 Jupiters Fit Inside the Sun. Weigh Them and You Get Almost the Same Number"
THEME = {"accent": (255, 200, 90), "accent2": (150, 220, 255), "tint": (40, 18, 8)}
BIG = {"num": "986 JUPITERS", "top": "FIT INSIDE THE SUN"}

BEATS = [
 {"say": "Nine hundred eighty six Jupiters fit inside the Sun.", "vis": {"type": "jupsun", "mode": "hook"}},
 {"say": "Jupiter is the biggest planet we have. But line them up, and it takes almost ten to cross the Sun once.",
  "vis": {"type": "jupsun", "mode": "row", "head": {"num": "ALMOST 10", "top": "JUPITERS, EDGE TO EDGE"}}},
 {"say": "Now fill it. By volume, the Sun swallows nine hundred eighty six of them.",
  "vis": {"type": "jupsun", "mode": "fill"}},
 {"say": "And every one of those Jupiters could hold more than thirteen hundred Earths.",
  "vis": {"type": "jupsun", "mode": "earth", "head": {"num": "1,321 EARTHS", "top": "INSIDE ONE JUPITER"}}},
 {"say": "Here's the twist. Weigh them instead, and the Sun equals one thousand forty eight Jupiters. Almost the same number.",
  "vis": {"type": "jupsun", "mode": "mass", "head": {"num": "1,048", "top": "JUPITER MASSES IN THE SUN"}}},
 {"say": "Because a cup of Sun and a cup of Jupiter weigh about the same. Both are mostly hydrogen and helium. So, what should we pour into the Sun next?",
  "vis": {"type": "jupsun", "mode": "density", "head": {"num": "1.41 vs 1.33", "top": "GRAMS PER CM³, ON AVERAGE"}}},
]

SOURCES = ["NASA Sun Fact Sheet (NSSDC): volume 1,412,000 × 10^12 km³, mean radius 695,700 km, mass 1,988,500 × 10^24 kg, mean density 1,408 kg/m³",
           "NASA Jupiter Fact Sheet (NSSDC): volume 1,431.28 × 10^12 km³ (1,321 Earths), mean radius 69,911 km, mass 1,898.13 × 10^24 kg, mean density 1,326 kg/m³",
           "Own calculations: Sun volume ÷ Jupiter volume ≈ 986; Sun diameter ÷ Jupiter mean diameter ≈ 9.95; Sun mass ÷ Jupiter mass ≈ 1,048",
           "NASA: the Sun and Jupiter are both made mostly of hydrogen and helium"]
