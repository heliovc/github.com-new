# Ranking #23 — Top 5 Planets With the Most Moons (Cosmic Scale)
# Known moons as of 2026 (IAU Minor Planet Center; Jupiter and Saturn updated by MPECs 2026-F09..F14, 16 March 2026):
# Saturn 285, Jupiter 101, Uranus 29 (S/2025 U1 found with JWST, announced by NASA Aug 2025), Neptune 16, Mars 2 (Phobos, Deimos).
# NASA: Phobos is drawing closer to Mars by about 1.8 m per century and should crash or break apart in roughly 50 million years;
# Triton holds more than 99.5% of all the mass orbiting Neptune; Uranus' moons are named after characters by Shakespeare and Pope.
# Own calc: all other planets combined = 101 + 29 + 16 + 2 + 1 (Earth) = 149; 285 / 149 = 1.9.
# Visual NEW: "swarm" (each moon a dot circling its planet; outro = one square per moon).
TITLE = "Top 5 Planets With the Most Moons"
THEME = {"accent": (180, 255, 170), "accent2": (255, 200, 140), "star_col": (210, 255, 210), "tint": (10, 30, 20),
         "bar": "TOP 5 MOST MOONS", "hook": "swarm", "outro": "swarm"}

HOOK = {"say": "Two hundred eighty five moons. One planet.",
        "big": "285", "top": "moons around one planet", "sub": "more than all the others combined"}

ITEMS = [
 {"rank": 5, "name": "Mars", "tag": "two tiny moons", "num": 2, "unit": "known moons",
  "source": "NASA / IAU Minor Planet Center", "vis": {"type": "swarm", "kind": "rock", "col": (200, 100, 60), "n": 2, "r": 130,
  "names": [("Phobos", 1.9), ("Deimos", 3.0)], "note": "Phobos is slowly falling toward Mars"},
  "say": "Number five. Mars. Just two tiny moons. And one of them, Phobos, is slowly spiraling in toward the planet."},
 {"rank": 4, "name": "Neptune", "tag": "one giant, fifteen crumbs", "num": 16, "unit": "known moons",
  "source": "NASA / IAU Minor Planet Center", "vis": {"type": "swarm", "kind": "ice", "col": (80, 120, 240), "n": 16, "r": 150,
  "note": "Triton holds over 99% of their mass"},
  "say": "Number four. Neptune. Sixteen moons. But one of them, Triton, holds more than ninety nine percent of all their mass."},
 {"rank": 3, "name": "Uranus", "tag": "named after Shakespeare", "num": 29, "unit": "known moons",
  "source": "NASA (JWST, 2025) / IAU Minor Planet Center", "vis": {"type": "swarm", "kind": "ice", "col": (150, 215, 225), "n": 29, "r": 150,
  "note": "the newest was found by the Webb telescope"},
  "say": "Number three. Uranus. Twenty nine, mostly named after characters from Shakespeare. The newest one was spotted by the Webb telescope."},
 {"rank": 2, "name": "Jupiter", "tag": "it just passed 100", "num": 101, "unit": "known moons",
  "source": "IAU Minor Planet Center, March 2026", "vis": {"type": "swarm", "kind": "jupiter", "col": (215, 175, 130), "n": 101, "r": 150,
  "note": "many are only a few km wide"},
  "say": "Number two. Jupiter. One hundred and one. It only crossed one hundred this year, and many of them are just a few kilometers wide."},
 {"rank": 1, "name": "Saturn", "tag": "the moon king", "num": 285, "unit": "known moons",
  "source": "IAU Minor Planet Center, March 2026", "vis": {"type": "swarm", "kind": "ringed", "col": (225, 200, 150), "n": 285, "r": 140,
  "note": "almost twice all the other planets combined"},
  "say": "And number one. Saturn. Two hundred eighty five. Almost twice as many as every other planet put together."},
]

OUTRO = {"say": "We have one Moon. Saturn has two hundred eighty five. Which planet should we measure next? Subscribe to Cosmic Scale."}

SOURCES = ["IAU Minor Planet Center (MPECs 2026-F09 to F14, March 2026): Saturn 285 and Jupiter 101 known moons",
           "NASA (Aug 2025): the Webb telescope found a new moon of Uranus, S/2025 U1, bringing Uranus to 29; Neptune 16; Mars 2 (Phobos and Deimos)",
           "NASA Science: Phobos is getting closer to Mars by about 1.8 m every hundred years",
           "NASA Science: Triton holds more than 99.5 percent of all the mass known to orbit Neptune; Uranus' moons are named after characters from Shakespeare and Alexander Pope",
           "Own calculations: all other planets combined = 101 + 29 + 16 + 2 + 1 (Earth) = 149; 285 / 149 = 1.9"]
