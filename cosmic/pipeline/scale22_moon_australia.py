# Scale Short #22 — The Moon Is Narrower Than Australia (Cosmic Scale)
# Format: "small vs giant" on a map. NASA Moon fact sheet: mean diameter 3,474.8 km, surface area about 37.9 million km².
# Geoscience Australia: the mainland is almost 4,000 km wide east to west (Steep Point to Cape Byron); land area about 7.69 million km².
# Continents (land area): Africa about 30.4 million km², Asia about 44.6 million km².
# Own calc: 37.9 / 7.69 = 4.9 Australias; outline hand-traced (simplified lon/lat), same km scale as the Moon.
# Visual NEW: "moonmap". Loop: the tail is the hook frame.
TITLE = "The Moon Is Narrower Than Australia. Its Surface Is 5 Australias"
THEME = {"accent": (255, 170, 90), "accent2": (150, 220, 255), "tint": (36, 18, 8)}
BIG = {"num": "3,475 KM", "top": "NARROWER THAN AUSTRALIA"}

BEATS = [
 {"say": "The Moon is narrower than Australia.", "vis": {"type": "moonmap", "mode": "hook"}},
 {"say": "Coast to coast, Australia is almost four thousand kilometers wide. The Moon? Three thousand four hundred seventy five.",
  "vis": {"type": "moonmap", "mode": "ruler", "head": {"num": "4,000 VS 3,475", "top": "KILOMETERS WIDE"}}},
 {"say": "Drop it on the map at the same scale, and both coasts still stick out.",
  "vis": {"type": "moonmap", "mode": "edges", "head": {"num": "SAME SCALE", "top": "THE MOON ON THE MAP"}}},
 {"say": "But peel off its surface and lay it flat. Thirty eight million square kilometers. Almost five Australias.",
  "vis": {"type": "moonmap", "mode": "peel", "head": {"num": "38 MILLION KM²", "top": "THE WHOLE SURFACE"}}},
 {"say": "More land than all of Africa, a bit less than Asia. And still narrower than one country. Which world should we drop on a map next?",
  "vis": {"type": "moonmap", "mode": "tail"}},
]

SOURCES = ["NASA Moon Fact Sheet (NSSDC): mean diameter 3,474.8 km; NASA: surface area about 14.6 million square miles (37.9 million km²)",
           "Geoscience Australia, Continental Extremities: the mainland is almost 4,000 km wide from east to west (Steep Point to Cape Byron); area about 7.69 million km²",
           "Continental land areas: Africa about 30.4 million km², Asia about 44.6 million km²",
           "Own calculations: 37.9 / 7.69 = 4.9 Australias; map outline simplified by hand and drawn at the same km scale as the Moon"]
