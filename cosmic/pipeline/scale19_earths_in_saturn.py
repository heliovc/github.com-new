# Scale Short #19 — 764 Earths Fit Inside Saturn. It Would Still Float (Cosmic Scale)
# Format: "X inside Y" + paradox. NASA NSSDC Saturn fact sheet: mean radius 58,232 km, volume 763.59 × Earth's (own calc (58,232/6,371)³
# = 763.6), mean density 687 kg/m³ (water 1,000; Earth 5,514). Mean diameter = 9.1 Earths (equatorial 9.45). NASA: Saturn is the only
# planet less dense than water; it could float in a big enough bathtub. Floating fraction = 687/1,000 = 69% under the waterline.
# Visual NEW: "saturnfloat". Loop: last beat dissolves into the hook.
TITLE = "764 Earths Fit Inside Saturn. It Would Still Float"
THEME = {"accent": (255, 200, 120), "accent2": (120, 210, 255), "tint": (14, 26, 44)}
BIG = {"num": "764 EARTHS", "top": "FIT INSIDE SATURN"}

BEATS = [
 {"say": "Seven hundred sixty four Earths fit inside Saturn.", "vis": {"type": "saturnfloat", "mode": "hook"}},
 {"say": "Line Earths up across it, and it takes more than nine, from one side to the other.",
  "vis": {"type": "saturnfloat", "mode": "row", "head": {"num": "9.1 EARTHS", "top": "ACROSS SATURN"}}},
 {"say": "Now fill it up. Seven hundred sixty four Earths vanish inside. And there's still no solid ground to stand on.",
  "vis": {"type": "saturnfloat", "mode": "fill", "head": {"num": "764 EARTHS", "top": "BY VOLUME"}}},
 {"say": "But Saturn is mostly hydrogen and helium. Put a litre of it on a kitchen scale, and it weighs less than a litre of water. A litre of Earth? Five and a half kilos.",
  "vis": {"type": "saturnfloat", "mode": "density", "head": {"num": "0.69 KG", "top": "ONE LITRE OF SATURN"}}},
 {"say": "So drop Saturn into a big enough ocean, and it would float, with about a third of it sticking out. Earth would sink like a stone. So, what giant should we drop in next?",
  "vis": {"type": "saturnfloat", "mode": "float", "head": {"num": "764 EARTHS", "top": "FIT INSIDE SATURN"}}},
]

SOURCES = ["NASA Saturn Fact Sheet (NSSDC): mean radius 58,232 km, volume 763.59 times Earth's, mean density 687 kg per cubic metre",
           "NASA Earth Fact Sheet: mean radius 6,371 km, mean density 5,514 kg per cubic metre",
           "NASA Science: Saturn is the only planet in our solar system less dense than water",
           "Own calculations: (58,232 / 6,371)³ = 763.6 Earths; mean diameter = 9.1 Earths; a floating Saturn would sit 69% under the waterline (687 / 1,000)"]
