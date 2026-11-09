# Scale Short #1 — Every Planet Fits Between Earth and the Moon (Cosmic Scale)
# Format: "X inside Y" — the 7 other planets stacked, TO SCALE, in the gap between Earth and the Moon (vertical: Earth on top, Moon below).
# Twist: they fit only when the Moon is at its farthest (apogee); on an average night Neptune sticks out. Loop: the closing question
# flows back into the hook line ("...first?" -> "Every planet fits in this gap.").
# Own calc (NASA mean/equatorial diameters, km): Mercury 4,879 + Venus 12,104 + Mars 6,792 + Jupiter 142,984 + Saturn 120,536
# + Uranus 51,118 + Neptune 49,528 = 387,941 km. Surface-to-surface gap = centre distance − 6,371 − 1,737:
# apogee ≈ 405,500 → 397,392 km (9,451 km spare); mean 384,400 → 376,292 km (11,649 km too long).
TITLE = "Every Planet Fits Between Earth and the Moon"
THEME = {"accent": (120, 230, 255), "accent2": (255, 205, 120), "tint": (16, 40, 60), "big_num": "ALL 7 PLANETS"}
BIG = {"num": "ALL 7 PLANETS", "top": "FIT IN THIS GAP"}

BEATS = [
 {"say": "Every planet fits in this gap.", "vis": {"type": "gap", "ghost": True}},
 {"say": "The space between Earth and the Moon, drawn to scale. Let's fill it. Mercury. Venus. Mars.",
  "vis": {"type": "gap", "ghost": True, "add": ["Mercury", "Venus", "Mars"]}},
 {"say": "Now the giants. Jupiter. Saturn. Uranus. And Neptune.",
  "vis": {"type": "gap", "ghost": True, "add": ["Jupiter", "Saturn", "Uranus", "Neptune"]}},
 {"say": "Side by side, they measure about three hundred eighty eight thousand kilometers. And they fit, with nine thousand kilometers to spare.",
  "vis": {"type": "gap", "show_total": True, "head": {"num": "387,941 KM", "top": "OF PLANETS. AND THEY FIT."}}},
 {"say": "But only when the Moon is at its farthest. On an average night, Neptune sticks out.",
  "vis": {"type": "gap", "show_total": True, "moon": "mean", "head": {"num": "ONLY SOMETIMES", "top": "AVERAGE NIGHT: TOO LONG"}}},
 {"say": "So which planet surprised you most? Tell me in the comments. Because every planet fits in this gap.",
  "vis": {"type": "gap", "head": {"num": "ALL 7 PLANETS", "top": "FIT IN THIS GAP"}, "loop": True}},
]

SOURCES = ["NASA Planetary Fact Sheets: diameters Mercury 4,879 km, Venus 12,104 km, Mars 6,792 km, Jupiter 142,984 km, Saturn 120,536 km, Uranus 51,118 km, Neptune 49,528 km; Earth radius 6,371 km; Moon radius 1,737 km",
           "NASA Moon fact sheet: Earth–Moon distance 384,400 km on average, about 405,500 km at apogee",
           "Own calculation: planets side by side 387,941 km; surface-to-surface gap 397,392 km at apogee (fits, about 9,450 km spare) and 376,292 km on average (about 11,650 km too long)"]
