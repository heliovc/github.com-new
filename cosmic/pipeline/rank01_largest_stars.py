# Ranking #1 — Top 5 Largest Stars Ever Measured (Cosmic Scale)
# Visual: each star placed where the Sun is, orbits to scale (1 AU = 46 px). Radius in AU = (times Sun) x 0.00465
TITLE = "Top 5 Largest Stars Ever Measured"
THEME = {"accent": (255, 120, 80), "accent2": (255, 200, 120), "star_col": (235, 90, 50), "tint": (90, 20, 30), "bar": "THE 5 LARGEST STARS EVER MEASURED"}

HOOK = {"say": "Number one would swallow our solar system almost out to Saturn. These are the five largest stars ever measured.",
        "top": "Largest stars ever measured", "sub": "#1 reaches almost to Saturn"}

ITEMS = [
 {"rank": 5, "name": "R Doradus", "tag": "red giant · 180 light-years away", "num": 350, "suffix": "×", "unit": "wider than the Sun",
  "source": "ESO / ALMA (2024)", "vis": {"type": "orbits", "au": 1.63, "note": "Mercury, Venus, Earth and Mars: gone"},
  "say": "Number five. R Doradus. About three hundred and fifty times wider than the Sun. Put it where the Sun is, and it swallows Mercury, Venus, Earth, and Mars."},
 {"rank": 4, "name": "Antares", "tag": "heart of Scorpius", "num": 700, "suffix": "×", "unit": "wider than the Sun",
  "source": "ESO VLTI (2017)", "col": (240, 110, 60), "vis": {"type": "orbits", "au": 3.26, "note": "Its surface reaches the asteroid belt"},
  "say": "Number four. Antares. About seven hundred times wider than the Sun. Its surface would reach all the way into the asteroid belt."},
 {"rank": 3, "name": "Betelgeuse", "tag": "Orion's red shoulder", "num": "Past Jupiter", "unit": "outer atmosphere, if it replaced the Sun",
  "source": "NASA / Hubble", "col": (245, 120, 70), "vis": {"type": "orbits", "au": 5.45, "note": "Jupiter's orbit: inside the star"},
  "say": "Number three. Betelgeuse, the red shoulder of Orion. NASA says its outer atmosphere would stretch past the orbit of Jupiter."},
 {"rank": 2, "name": "VY Canis Majoris", "tag": "red hypergiant", "num": 300000, "suffix": "×", "unit": "brighter than the Sun",
  "source": "NASA / Hubble (2021)", "col": (225, 80, 60), "vis": {"type": "orbits", "au": 6.6, "note": "Reaches between Jupiter and Saturn"},
  "say": "Number two. V Y Canis Majoris. Three hundred thousand times brighter than the Sun, and so bloated it would reach between Jupiter and Saturn."},
 {"rank": 1, "name": "WOH G64", "tag": "in the Large Magellanic Cloud", "num": 2000, "suffix": "×", "unit": "wider than the Sun",
  "source": "ESO VLTI / GRAVITY (2024)", "col": (210, 70, 50), "vis": {"type": "orbits", "au": 9.3, "note": "Almost to Saturn's orbit"},
  "say": "And number one. W O H G sixty four. About two thousand times wider than the Sun. In twenty twenty four, it became the first star outside our galaxy ever photographed up close. Here, it would reach almost to Saturn."},
]

OUTRO = {"say": "And our Sun? On this scale, it's barely a dot. Subscribe to Cosmic Scale for more."}

SOURCES = ["ESO eso2412 (R Doradus, ALMA, 2024)", "ESO eso1726 (Antares, VLTI, 2017)", "NASA Science: Betelgeuse location and size (Hubble)",
           "NASA Hubble: Hubble Solves Mystery of Monster Star's Dimming (VY CMa, 2021)", "ESO eso2417 (WOH G64, first close-up of a star outside the Milky Way, 2024)"]
