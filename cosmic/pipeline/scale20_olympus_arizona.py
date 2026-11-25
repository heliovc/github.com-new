# Scale Short #20 — This Volcano Is as Wide as Arizona. It's 2.5 Everests Tall (Cosmic Scale)
# Format: "small vs giant" on a map. NASA: Olympus Mons on Mars is about 600 km across (NASA gives 585–624 km), wider than / about the size
# of Arizona; its slopes are gentle, typically 2–5 degrees; it rises about 22 km above the Martian datum (MOLA 21.9 km; NASA quotes 25–26 km
# above the surrounding plains). Everest 8,849 m. Own calc: 21.9 / 8.85 = 2.5 Everests; base to summit ≈ 300 km; at 30 km a day ≈ 10 days
# of walking; true-scale profile is 27 times wider than tall; Arizona outline simplified by hand (lon/lat), same km scale as the volcano.
# Visual NEW: "olympus". Loop: last beat dissolves into the hook.
TITLE = "This Volcano Is as Wide as Arizona. It's 2.5 Everests Tall"
THEME = {"accent": (255, 150, 90), "accent2": (130, 200, 255), "tint": (40, 16, 12)}
BIG = {"num": "600 KM WIDE", "top": "ONE VOLCANO"}

BEATS = [
 {"say": "This one volcano is as wide as Arizona.", "vis": {"type": "olympus", "mode": "hook"}},
 {"say": "It's Olympus Mons, on Mars. About six hundred kilometers across, on a planet half the width of Earth.",
  "vis": {"type": "olympus", "mode": "mars", "head": {"num": "OLYMPUS MONS", "top": "MARS"}}},
 {"say": "It rises about twenty two kilometers. Two and a half Mount Everests. But draw it to true scale, and it's almost flat, like a pancake.",
  "vis": {"type": "olympus", "mode": "flat", "head": {"num": "22 KM TALL", "top": "2.5 EVERESTS"}}},
 {"say": "The slope is so gentle, you could walk up it. From the edge to the top, about three hundred kilometers. Ten days of hiking, and you'd barely feel the climb.",
  "vis": {"type": "olympus", "mode": "walk", "head": {"num": "300 KM", "top": "EDGE TO SUMMIT"}}},
 {"say": "One volcano, the size of a whole state. So, what giant should we drop on a map next?",
  "vis": {"type": "olympus", "mode": "tail", "head": {"num": "600 KM WIDE", "top": "ONE VOLCANO"}}},
]

SOURCES = ["NASA Science: Olympus Mons is about 600 km (374 miles) across, roughly the size of Arizona, with gentle slopes of about 2 to 5 degrees",
           "NASA Mars Global Surveyor MOLA: summit about 21.9 km above the Martian datum (often quoted as 22–26 km)",
           "NASA Mars Fact Sheet: Mars mean diameter 6,779 km (Earth 12,742 km)",
           "Mount Everest 8,849 m (2020 survey)",
           "Own calculations: 21.9 / 8.85 = 2.5 Everests; edge to summit ≈ 300 km, about 10 days at 30 km per day; true-scale profile 600 × 22 km"]
