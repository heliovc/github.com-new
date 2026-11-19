# Scale Short #10 — If Earth Were a Basketball, the Space Station Would Fly 7 mm Above It (Cosmic Scale)
# Format: "small vs giant" — shrink Earth (12,742 km) to a basketball (size 7, 23.9 cm): 1 mm = 53.3 km. Edge of space (Kármán line, 100 km)
# = 1.9 mm (a coin is 1.75 mm thick); ISS at ~400 km = 7.5 mm (a pencil is ~7 mm wide); the Moon (384,400 km) = 7.2 m away and the
# size of a tennis ball (6.5 cm). Visual NEW: "ballearth" (ball Earth + magnifier on the rim with to-scale references + 7 m camera pan).
# Loop: the closing question flows back into the hook line.
# Own calc: k = 23.9 cm / 12,742 km; 100 km -> 1.88 mm; 400 km -> 7.50 mm; 384,400 km -> 7.21 m; 3,474.8 km -> 6.5 cm.
TITLE = "If Earth Were a Basketball, the Space Station Would Fly 7 mm Above It"
THEME = {"accent": (255, 160, 70), "accent2": (120, 220, 255), "tint": (40, 22, 8)}
BIG = {"num": "7.5 mm", "top": "ABOVE A BASKETBALL EARTH"}

BEATS = [
 {"say": "The space station: seven millimeters up.", "vis": {"type": "ballearth", "mode": "hook"}},
 {"say": "Shrink Earth, all twelve thousand seven hundred kilometers, down to one basketball.",
  "vis": {"type": "ballearth", "mode": "shrink", "head": {"num": "24 cm", "top": "EARTH, SHRUNK TO A BASKETBALL"}}},
 {"say": "The edge of space, a hundred kilometers up, is now under two millimeters. About the thickness of a coin.",
  "vis": {"type": "ballearth", "mode": "edge", "head": {"num": "1.9 mm", "top": "THE EDGE OF SPACE"}}},
 {"say": "The space station flies four hundred kilometers up. On the ball, seven and a half millimeters. A pencil would barely fit underneath.",
  "vis": {"type": "ballearth", "mode": "iss", "head": {"num": "7.5 mm", "top": "THE SPACE STATION'S ORBIT"}}},
 {"say": "And the Moon? A tennis ball, seven meters away, across the room.",
  "vis": {"type": "ballearth", "mode": "moon", "head": {"num": "7.2 m", "top": "TO A TENNIS-BALL MOON"}}},
 {"say": "What should we shrink next? Remember, on a basketball Earth, the space station flies seven millimeters up.",
  "vis": {"type": "ballearth", "mode": "hook"}},
]

SOURCES = ["NASA Earth Fact Sheet: Earth's mean diameter 12,742 km; Moon mean distance 384,400 km; Moon diameter 3,474.8 km",
           "NASA: the International Space Station orbits at about 400 km (roughly 250 miles) altitude",
           "Kármán line: the commonly used boundary of space at 100 km altitude (FAI)",
           "Size 7 basketball: about 75 cm circumference, 23.9 cm diameter",
           "Own calculations at 23.9 cm per 12,742 km: 100 km = 1.9 mm, 400 km = 7.5 mm, Moon distance = 7.2 m, Moon diameter = 6.5 cm (tennis ball ≈ 6.7 cm)"]
