# Scale Short #18 — All 8 Billion Humans Fit Inside a Sugar Cube (Cosmic Scale)
# Format: "X inside Y" / small vs giant. UN World Population Prospects 2024: about 8.2 billion people. Walpole et al. 2012 (BMC Public
# Health, "The weight of nations"): average adult body mass 62 kg -> used for EVERYONE (upper bound, children weigh less): 5.1e11 kg.
# Nuclear saturation density ~0.16 nucleons/fm³ = 2.7e17 kg/m³ -> own calc 1.9 cm³ (a sugar cube is about 2 cm³). As flesh (~1,000 kg/m³)
# the same mass fills 0.51 km³ = a cube ~799 m a side (Burj Khalifa 828 m). Atom ~1e-10 m vs nucleus ~1e-15 m -> 1/100,000 the width.
# NASA: a sugar cube of neutron-star material would weigh about a billion tons on Earth (same order as our 0.5 billion t).
# Visual NEW: "sugarcube". Loop: last beat dissolves back into the hook composition.
TITLE = "All 8 Billion Humans Fit Inside a Sugar Cube"
THEME = {"accent": (255, 214, 120), "accent2": (150, 205, 255), "tint": (26, 20, 40)}
BIG = {"num": "8.2 BILLION", "top": "HUMANS IN ONE SUGAR CUBE"}

BEATS = [
 {"say": "Every human alive fits in a sugar cube.", "vis": {"type": "sugarcube", "mode": "hook"}},
 {"say": "Here's the trick. Atoms are almost entirely empty. Blow an atom up to the size of a stadium, and its nucleus is a grain of rice in the middle. The rest is nothing.",
  "vis": {"type": "sugarcube", "mode": "atom", "head": {"num": "99.9999%", "top": "OF AN ATOM IS EMPTY SPACE"}}},
 {"say": "As we are, all eight billion of us would fill a cube eight hundred meters tall. Squeeze out the empty space, and it shrinks to under two cubic centimeters.",
  "vis": {"type": "sugarcube", "mode": "squeeze", "head": {"num": "800 M → 1.2 CM", "top": "ALL OF HUMANITY, SQUEEZED"}}},
 {"say": "But nothing is lost. That cube still weighs half a billion tonnes. Set it on a table, and it punches straight through the table, and the floor.",
  "vis": {"type": "sugarcube", "mode": "weight", "head": {"num": "510 MILLION T", "top": "IN ONE SUGAR CUBE"}}},
 {"say": "That's what neutron stars are made of. So, what should we squeeze next?",
  "vis": {"type": "sugarcube", "mode": "neutron", "head": {"num": "8.2 BILLION", "top": "HUMANS IN ONE SUGAR CUBE"}}},
]

SOURCES = ["United Nations, World Population Prospects 2024: world population about 8.2 billion",
           "Walpole et al. (2012), BMC Public Health, \"The weight of nations\": average adult body mass about 62 kg (used here for everyone, so the result is an upper bound)",
           "Nuclear saturation density: about 0.16 nucleons per cubic femtometre, about 2.7 × 10^17 kg per cubic metre",
           "Atoms are about 10^-10 m across, nuclei about 10^-15 m: the nucleus is about 1/100,000 of the atom's width",
           "NASA: a sugar cube of neutron-star material would weigh about a billion tons on Earth",
           "Own calculations: 8.2 billion × 62 kg = 5.1 × 10^11 kg; at nuclear density that is about 1.9 cubic centimetres; at the density of water it is 0.51 cubic kilometres, a cube about 800 m on a side"]
