# Scale Short #17 — 15 Suns Fit Across Jupiter's Invisible Bubble (Cosmic Scale)
# Format: "X inside Y". Jupiter's magnetosphere: ESA calls it nearly 15 times bigger than the Sun; dayside magnetopause 45–100 Jupiter radii
# from the planet (1 RJ = 71,492 km -> 3.2–7.1 million km); NASA: if it glowed in visible light it would look 2–3 times the size of the
# full Moon from Earth; NASA/JPL: the magnetotail stretches as far as Saturn's orbit. Own calc: Sun diameter 1,391,400 km -> 2.3–5.1 Suns
# fit between Jupiter and the sunward edge. Field made by metallic hydrogen (EP18). Visual NEW: "magbubble". Loop: last frame = hook.
TITLE = "15 Suns Fit Across Jupiter's Invisible Bubble"
THEME = {"accent": (255, 200, 90), "accent2": (120, 220, 255), "tint": (8, 22, 40)}
BIG = {"num": "15 SUNS", "top": "ACROSS JUPITER'S BUBBLE"}

BEATS = [
 {"say": "This bubble is fifteen Suns wide.", "vis": {"type": "magbubble", "mode": "hook"}},
 {"say": "It's Jupiter's magnetic field, made by an ocean of liquid metal deep inside, pushing back the wind from the Sun.",
  "vis": {"type": "magbubble", "mode": "field", "head": {"num": "INVISIBLE", "top": "JUPITER'S MAGNETIC BUBBLE"}}},
 {"say": "The edge facing the Sun sits three to seven million kilometers out. Room for up to five Suns in that gap alone.",
  "vis": {"type": "magbubble", "mode": "front", "head": {"num": "7.1 MILLION KM", "top": "TO THE SUNWARD EDGE, AT MOST"}}},
 {"say": "If you could see it from Earth, it would look two to three times wider than the full Moon.",
  "vis": {"type": "magbubble", "mode": "sky", "head": {"num": "2–3 MOONS", "top": "WIDE, IN OUR NIGHT SKY"}}},
 {"say": "And its tail reaches all the way to Saturn's orbit. So, what invisible giant should we measure next?",
  "vis": {"type": "magbubble", "mode": "tail", "head": {"num": "15 SUNS", "top": "ACROSS JUPITER'S BUBBLE"}}},
]

SOURCES = ["ESA (2023): Jupiter's magnetosphere is nearly 15 times bigger than the Sun",
           "Jupiter's sunward magnetopause lies about 45–100 Jupiter radii from the planet (published Juno-era and Galileo-era measurements), i.e. about 3.2–7.1 million km",
           "NASA Science: if Jupiter's magnetosphere glowed in visible light it would appear two to three times the size of the full Moon from Earth",
           "NASA/JPL: Jupiter's magnetotail extends as far as the orbit of Saturn",
           "Own calculations: 1 Jupiter radius = 71,492 km; Sun diameter 1,391,400 km, so 2.3–5.1 Suns fit between Jupiter and the sunward edge"]
