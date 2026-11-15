# Scale Short #6 — Pluto Is Smaller Than the United States (Cosmic Scale)
# Format: "small vs giant" — Pluto vs the contiguous US, to scale. Visual NEW: "mapfit" (hand-traced simplified outline of the lower 48
# states, Pluto dropped on it; ruler bars; Moon vs Pluto over the map; Earth -> Pluto with the New Horizons year counter).
# Loop: the closing question flows back into the hook line ("...Pluto is smaller than the United States." -> same line at frame 0).
# Numbers: NASA: Pluto 2,377 km wide (about half the width of the US, about 2/3 of the Moon); contiguous US about 4,500 km east to west.
# Own calc: 2,377 / 4,500 ≈ 0.53; 2,377 / 3,475 ≈ 0.68; New Horizons 19 Jan 2006 -> 14 Jul 2015 = 9.5 years.
TITLE = "Pluto Is Smaller Than the United States"
THEME = {"accent": (255, 190, 140), "accent2": (120, 220, 255), "tint": (40, 22, 30)}
BIG = {"num": "2,377 KM", "top": "PLUTO vs THE USA"}

BEATS = [
 {"say": "Pluto is smaller than the United States.", "vis": {"type": "mapfit", "mode": "hook"}},
 {"say": "Pluto is two thousand three hundred seventy seven kilometers wide. The lower forty eight states, coast to coast, are about four thousand five hundred.",
  "vis": {"type": "mapfit", "mode": "ruler", "head": {"num": "2,377 vs 4,500", "top": "KILOMETERS WIDE"}}},
 {"say": "Drop Pluto on the map, and both coasts stick out. It covers only about half the country's width.",
  "vis": {"type": "mapfit", "mode": "hook", "drop": True, "head": {"num": "≈ HALF", "top": "THE WIDTH OF THE USA"}}},
 {"say": "It's even smaller than our own Moon. About two thirds as wide.",
  "vis": {"type": "mapfit", "mode": "moon", "head": {"num": "68%", "top": "OF THE MOON'S WIDTH"}}},
 {"say": "And this tiny world is so far away that New Horizons, launched faster than any spacecraft before it, still needed nine and a half years to get there.",
  "vis": {"type": "mapfit", "mode": "trip", "head": {"num": "9.5 YEARS", "top": "TO REACH IT"}}},
 {"say": "Would you still call it a planet? Tell me below. Because Pluto is smaller than the United States.",
  "vis": {"type": "mapfit", "mode": "hook"}},
]

SOURCES = ["NASA Science, Pluto facts: Pluto is about 2,377 km (1,477 miles) wide, about half the width of the United States and about two thirds the width of Earth's Moon",
           "NASA: Earth's Moon is about 3,475 km wide",
           "Contiguous United States: about 4,500 km (2,800 miles) from east to west",
           "NASA: New Horizons launched 19 January 2006, the fastest launch speed of any spacecraft, and flew past Pluto on 14 July 2015",
           "Own calculations: 2,377 / 4,500 ≈ 0.53; 2,377 / 3,475 ≈ 0.68; 19 Jan 2006 to 14 Jul 2015 ≈ 9.5 years; US outline simplified and drawn by hand, to the same scale as Pluto"]
