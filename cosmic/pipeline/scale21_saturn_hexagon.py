# Scale Short #21 — Two Earths Fit Inside a Hexagon on Saturn (Cosmic Scale)
# Format: "X inside Y". NASA/JPL (Cassini, Dec 2013): the hexagon is a six-sided jet stream on Saturn's north pole, about 20,000 miles
# (30,000 km) across, with winds of about 200 mph (322 km/h); first seen by Voyager 1 and 2 in 1980–1981. NASA SVS: it could encompass
# Earth twice. NASA: Cassini saw the region change colour from bluish to golden between 2012 and 2016. Earth 12,742 km (NASA).
# Own calc: 30,000 / 12,742 = 2.35 Earths across; a regular hexagon's side = half its corner-to-corner width = 15,000 km, longer than Earth.
# Visual NEW: "hexagon". Loop: the tail returns to the hook composition.
TITLE = "Two Earths Fit Inside a Hexagon on Saturn"
THEME = {"accent": (120, 220, 255), "accent2": (255, 205, 120), "tint": (10, 24, 40)}
BIG = {"num": "30,000 KM", "top": "A HEXAGON ON SATURN"}

BEATS = [
 {"say": "Two Earths fit inside this hexagon.", "vis": {"type": "hexagon", "mode": "hook"}},
 {"say": "It sits on Saturn's north pole. A six sided jet stream, about thirty thousand kilometers across.",
  "vis": {"type": "hexagon", "mode": "globe", "head": {"num": "NORTH POLE", "top": "SATURN"}}},
 {"say": "Each side is longer than our whole planet is wide. And the wind runs along the edges at over three hundred kilometers an hour.",
  "vis": {"type": "hexagon", "mode": "side", "head": {"num": "15,000 KM", "top": "EACH SIDE"}}},
 {"say": "Voyager spotted it in nineteen eighty one. Twenty five years later, Cassini found it still there. It even changed color, from blue to gold.",
  "vis": {"type": "hexagon", "mode": "years", "head": {"num": "40+ YEARS", "top": "STILL SPINNING"}}},
 {"say": "A storm with six straight sides, wider than two Earths. What should we fit inside it next?",
  "vis": {"type": "hexagon", "mode": "tail", "head": {"num": "30,000 KM", "top": "A HEXAGON ON SATURN"}}},
]

SOURCES = ["NASA/JPL, Cassini (Dec 2013): Saturn's hexagon is a six-sided jet stream about 20,000 miles (30,000 km) across, with winds of about 200 mph (322 km/h)",
           "NASA: the hexagon was first observed when Voyager 1 and 2 flew past Saturn in 1980 and 1981; Cassini arrived in 2004 and imaged it from 2006 to 2017",
           "NASA Scientific Visualization Studio: the jet stream could encompass Earth twice",
           "NASA/JPL: the north polar region changed colour from bluish to golden between 2012 and 2016",
           "Own calculations: 30,000 / 12,742 km = 2.35 Earths across; side of a regular hexagon = half its width = 15,000 km"]
