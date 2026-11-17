# Scale Short #8 — The Moon's Entire Orbit Fits Inside the Sun (Cosmic Scale)
# Format: "X inside Y" — put Earth at the centre of the Sun: the Moon's whole orbit sits inside it, to scale. Visual NEW: "moonorbit"
# (translucent Sun + orbit + Moon circling; log zoom from Earth out; radius bars with the room to spare; Apollo-pace crossing timer).
# Loop: the closing question flows back into the hook line.
# Numbers: NASA: Sun about 1,392,000 km wide (radius about 696,000 km); Moon's mean distance 384,400 km (farthest about 405,500 km).
# Apollo 11: launch 16 July 1969 13:32 UTC, lunar orbit insertion 19 July 17:21 UTC ≈ 76 h ≈ 3.2 days.
# Own calc: 696,000 - 384,400 = 311,600 km to spare; even at 405,500 km, 290,500 km; 1,392,000 / 768,800 ≈ 1.81;
# Apollo pace 384,400 km / 76 h ≈ 5,060 km/h -> 1,392,000 km / 5,060 km/h ≈ 275 h ≈ 11.5 days.
TITLE = "The Moon's Entire Orbit Fits Inside the Sun"
THEME = {"accent": (255, 170, 60), "accent2": (150, 220, 255), "tint": (60, 22, 6)}
BIG = {"num": "1.8×", "top": "THE SUN vs THE MOON'S ORBIT"}

BEATS = [
 {"say": "The Moon's entire orbit fits inside the Sun.", "vis": {"type": "moonorbit", "mode": "hook"}},
 {"say": "Put Earth at the center of the Sun. The Moon circles us about three hundred eighty four thousand kilometers away.",
  "vis": {"type": "moonorbit", "mode": "orbit", "head": {"num": "384,400 KM", "top": "FROM EARTH TO THE MOON"}}},
 {"say": "But the Sun's radius is almost seven hundred thousand. So the whole orbit sits deep inside, with over three hundred thousand kilometers to spare.",
  "vis": {"type": "moonorbit", "mode": "room", "head": {"num": "696,000 KM", "top": "THE SUN'S RADIUS"}}},
 {"say": "Apollo eleven needed about three days to reach the Moon. At that pace, crossing the Sun would take eleven and a half days.",
  "vis": {"type": "moonorbit", "mode": "trip", "head": {"num": "11.5 DAYS", "top": "TO CROSS THE SUN AT APOLLO'S PACE"}}},
 {"say": "Did you picture the Sun this big? Tell me below. Because the Moon's entire orbit fits inside the Sun.",
  "vis": {"type": "moonorbit", "mode": "hook"}},
]

SOURCES = ["NASA Science, Sun facts: the Sun is about 1,392,000 km (865,000 miles) wide, so its radius is about 696,000 km",
           "NASA Science, Moon facts: average distance from Earth 384,400 km (about 405,500 km at its farthest)",
           "NASA, Apollo 11 mission timeline: launch 16 July 1969, entered lunar orbit 19 July 1969 (about 76 hours)",
           "Own calculations: 696,000 - 384,400 = 311,600 km to spare (290,500 km with the Moon at its farthest); 1,392,000 / 768,800 ≈ 1.8; Apollo 11 average pace 384,400 km / 76 h ≈ 5,060 km/h, so 1,392,000 km takes about 275 h ≈ 11.5 days"]
