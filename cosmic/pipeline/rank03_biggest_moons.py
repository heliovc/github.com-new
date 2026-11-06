# Ranking #3 — Top 5 Biggest Moons in the Solar System (Cosmic Scale)
# Visual: "moons to scale" — current moon big (true relative size) inside Mercury's dashed outline + lineup of all 5 to scale
# (unrevealed = "?" silhouettes). Theme amber / teal. km = mean diameter (NASA).
TITLE = "Top 5 Biggest Moons in the Solar System"
THEME = {"accent": (255, 190, 90), "accent2": (120, 230, 210), "star_col": (255, 200, 120), "tint": (10, 60, 62),
         "bar": "THE 5 BIGGEST MOONS IN THE SOLAR SYSTEM", "hook": "moons", "outro": "moons",
         "outro_note": "all five, side by side: almost 2 Earths"}

HOOK = {"say": "Two moons in our solar system are bigger than the planet Mercury. These are the five biggest moons we know.",
        "top": "Biggest moons in the solar system", "sub": "2 of them beat a planet"}

ITEMS = [
 {"rank": 5, "name": "The Moon", "short": "Moon", "tag": "Earth's own · 384,400 km away", "num": 3475, "unit": "km across",
  "source": "NASA", "vis": {"type": "moons", "moon": "Moon", "km": 3475},
  "say": "Number five. Our own Moon. Three thousand four hundred and seventy five kilometers across. That's bigger than Pluto, and it barely makes the list."},
 {"rank": 4, "name": "Io", "short": "Io", "tag": "Jupiter · the most volcanic world", "num": 3643, "unit": "km across",
  "source": "NASA", "vis": {"type": "moons", "moon": "Io", "km": 3643},
  "say": "Number four. Io, a moon of Jupiter. Just a little bigger than our Moon, but covered in hundreds of active volcanoes. Jupiter's gravity squeezes it so hard that its insides melt."},
 {"rank": 3, "name": "Callisto", "short": "Callisto", "tag": "Jupiter · oldest surface we know", "num": 4820, "unit": "km across",
  "source": "NASA", "vis": {"type": "moons", "moon": "Callisto", "km": 4820},
  "say": "Number three. Callisto. Almost exactly the size of Mercury. Its surface is about four billion years old, the most heavily cratered in the whole solar system."},
 {"rank": 2, "name": "Titan", "short": "Titan", "tag": "Saturn · lakes of liquid methane", "num": 5150, "unit": "km across",
  "source": "NASA / Cassini", "vis": {"type": "moons", "moon": "Titan", "km": 5150},
  "say": "Number two. Titan, the giant moon of Saturn. Bigger than Mercury, with an atmosphere so thick that the air pressure on the ground is sixty percent higher than on Earth. It rains methane there."},
 {"rank": 1, "name": "Ganymede", "short": "Ganymede", "tag": "Jupiter · has its own magnetic field", "num": 5260, "unit": "km across",
  "source": "NASA / Hubble", "vis": {"type": "moons", "moon": "Ganymede", "km": 5260},
  "say": "And number one. Ganymede, the biggest moon of Jupiter. Wider than Mercury. It's the only moon with its own magnetic field, and under its ice hides an ocean with more water than all the oceans on Earth."},
]

OUTRO = {"say": "Line up all five and they stretch across almost two Earths. Subscribe to Cosmic Scale for more."}

SOURCES = ["NASA Science, Ganymede: Facts (about 5,260 km across; bigger than Mercury; only moon with its own magnetic field; Hubble evidence of a subsurface ocean with more water than Earth's surface)",
           "NASA Science, Titan: Facts (radius about 2,575 km; larger than Mercury; surface pressure about 60% higher than Earth's; methane rain and lakes)",
           "NASA Science, Callisto: Facts (about the size of Mercury; oldest and most heavily cratered surface, about 4 billion years old)",
           "NASA Science, Io (most volcanically active world in the solar system; hundreds of volcanoes; tidal heating by Jupiter)",
           "NASA Science, Earth's Moon: Facts (radius 1,737.4 km; 384,400 km from Earth); NASA Pluto facts (about 2,377 km across)",
           "Own calculation: sum of the five diameters ≈ 22,350 km ≈ 1.75 × Earth's diameter (12,742 km)"]
