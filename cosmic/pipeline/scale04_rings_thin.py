# Scale Short #4 — Saturn's Rings Are Thinner Than a Building (Cosmic Scale)
# Format: "small vs giant" — 273,000 km across vs about 10 m thick. Visual NEW: "thinring" (edge + magnifier with a 3-storey building,
# wide vs Earth–Moon bar, log zoom, paper analogy over a skyline, edge-on tilt 2017 -> 2025).
# Loop: the closing question flows back into the hook line ("...thinner than this building." -> "Saturn's rings are thinner than this building.").
# Numbers: main rings about 273,000 km edge to edge (A ring outer radius 136,775 km), about 10 m thick in most places (NASA); ring-plane
# crossing seen from Earth in March 2025 (NASA). Own calc: 273,550 / 384,400 ≈ 0.71 of the Earth–Moon distance; 273,000 km / 10 m =
# 27 million -> paper (0.1 mm) -> 2.7 km.
TITLE = "Saturn's Rings Are Thinner Than a Building"
THEME = {"accent": (255, 225, 150), "accent2": (130, 220, 255), "tint": (40, 34, 20)}
BIG = {"num": "10 METERS", "top": "THICK. 273,000 KM WIDE."}

BEATS = [
 {"say": "Saturn's rings are thinner than this building.", "vis": {"type": "thinring", "mode": "edge"}},
 {"say": "Edge to edge, they stretch about two hundred seventy thousand kilometers. That's most of the way from Earth to the Moon.",
  "vis": {"type": "thinring", "mode": "wide", "head": {"num": "273,000 KM", "top": "EDGE TO EDGE"}}},
 {"say": "But zoom in on the edge, and in most places they're only about ten meters thick.",
  "vis": {"type": "thinring", "mode": "zoom", "head": {"num": "≈ 10 M", "top": "THICK, IN MOST PLACES"}}},
 {"say": "Make them as thin as a sheet of paper, and they'd still be almost three kilometers wide.",
  "vis": {"type": "thinring", "mode": "paper", "head": {"num": "2.7 KM", "top": "OF PAPER-THIN RING"}}},
 {"say": "That's why, in twenty twenty five, when they turned edge on to Earth, they almost vanished.",
  "vis": {"type": "thinring", "mode": "tilt", "head": {"num": "EDGE-ON", "top": "THE RINGS ALMOST VANISH"}}},
 {"say": "So are they huge, or tiny? Tell me below. Because Saturn's rings are thinner than this building.",
  "vis": {"type": "thinring", "mode": "edge"}},
]

SOURCES = ["NASA Science, Saturn's rings: the main rings span about 273,000 km and are about 10 m thick in most places",
           "NASA Saturnian Rings Fact Sheet: A ring outer edge 136,775 km from Saturn's centre",
           "NASA (2025): Saturn's rings appeared edge-on from Earth in March 2025 (ring-plane crossing) and nearly disappeared in telescopes",
           "Own calculations: 273,550 km / 384,400 km ≈ 0.71 of the Earth–Moon distance; 273,000 km / 10 m = 27 million, so paper-thin (0.1 mm) rings would be about 2.7 km wide"]
