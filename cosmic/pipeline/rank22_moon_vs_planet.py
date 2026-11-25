# Ranking #22 — Top 5 Biggest Moons Compared to Their Planet (Cosmic Scale)
# Diameters (NASA NSSDC fact sheets / NASA Science; planets = equatorial): Pluto 2,377 km & Charon 1,212 km; Earth 12,756 km & Moon 3,474.8 km;
# Neptune 49,528 km & Triton 2,706.8 km; Saturn 120,536 km & Titan 5,149.5 km; Jupiter 142,984 km & Ganymede 5,268.2 km.
# Own calc (moon ÷ planet): Charon 51.0%, Moon 27.2%, Triton 5.47%, Titan 4.27%, Ganymede 3.68% (next: Callisto 3.37%, Titania 3.09%).
# NASA: Pluto and Charon orbit a point in the space between them (barycentre outside Pluto); Triton orbits Neptune backward (retrograde);
# Titan has a thick nitrogen atmosphere, thicker than Earth's at the surface (1.5 bar); Ganymede is the largest moon, bigger than Mercury.
# Visual NEW: "pair" (each planet drawn at the same size, the moon to scale with it, so the moon's size IS the ratio).
TITLE = "Top 5 Biggest Moons Compared to Their Planet"
THEME = {"accent": (120, 230, 255), "accent2": (255, 205, 120), "star_col": (200, 235, 255), "tint": (8, 22, 40),
         "bar": "TOP 5 MOONS VS THEIR PLANET", "hook": "pair", "outro": "pair",
         "outro_note": "every planet drawn the same size"}

HOOK = {"say": "Moon number one is half as wide as the world it orbits.",
        "big": "51%", "top": "as wide as its planet", "sub": "every planet drawn the same size"}

ITEMS = [
 {"rank": 5, "name": "Ganymede", "tag": "the biggest moon of all", "num": "3.7%", "unit": "of Jupiter's width",
  "source": "NASA Jupiter & Ganymede fact sheets", "vis": {"type": "pair", "kind": "gas", "col": (215, 175, 130), "mcol": (175, 165, 150), "ratio": 0.0368,
  "pname": "Jupiter", "mname": "Ganymede", "note": "bigger than the planet Mercury, still a speck"},
  "say": "Number five. Ganymede. The biggest moon in the solar system, bigger than Mercury. Next to Jupiter, it's under four percent."},
 {"rank": 4, "name": "Titan", "tag": "a moon with thick air", "num": "4.3%", "unit": "of Saturn's width",
  "source": "NASA Saturn & Titan fact sheets", "vis": {"type": "pair", "kind": "ringed", "col": (225, 200, 150), "mcol": (230, 170, 80), "ratio": 0.0427,
  "pname": "Saturn", "mname": "Titan", "note": "its air is thicker than Earth's"},
  "say": "Number four. Titan. Four percent of Saturn. And it has air thicker than ours."},
 {"rank": 3, "name": "Triton", "tag": "it orbits backward", "num": "5.5%", "unit": "of Neptune's width",
  "source": "NASA Neptune & Triton fact sheets", "vis": {"type": "pair", "kind": "ice", "col": (80, 120, 240), "mcol": (225, 200, 205), "ratio": 0.0547,
  "pname": "Neptune", "mname": "Triton", "note": "it circles Neptune the wrong way"},
  "say": "Number three. Triton. Five and a half percent of Neptune, and it goes around backward. Then the list jumps."},
 {"rank": 2, "name": "Our Moon", "tag": "the biggest for any planet", "num": "27%", "unit": "of Earth's width",
  "source": "NASA Earth & Moon fact sheets", "vis": {"type": "pair", "kind": "earth", "col": (70, 130, 230), "mkind": "moon", "ratio": 0.272,
  "pname": "Earth", "mname": "the Moon", "note": "no other planet has a moon this big"},
  "say": "Number two. Our own Moon. Twenty seven percent of Earth. No other planet has a moon that big."},
 {"rank": 1, "name": "Charon", "tag": "Pluto's twin", "num": "51%", "unit": "of Pluto's width",
  "source": "NASA Pluto & Charon fact sheets", "vis": {"type": "pair", "kind": "dwarf", "col": (210, 180, 150), "mcol": (170, 165, 165), "ratio": 0.510,
  "pname": "Pluto (dwarf planet)", "mname": "Charon", "note": "they circle a point between them"},
  "say": "And number one. Charon. Half as wide as Pluto. They're so close in size, they circle a point in the empty space between them."},
]

OUTRO = {"say": "So our Moon wins among the planets. Which moon should we measure next? Subscribe to Cosmic Scale."}

SOURCES = ["NASA planetary fact sheets (NSSDC), equatorial diameters: Jupiter 142,984 km, Saturn 120,536 km, Neptune 49,528 km, Earth 12,756 km",
           "NASA Science: Ganymede 5,268 km (largest moon, bigger than Mercury), Titan 5,150 km, Triton 2,707 km, the Moon 3,475 km, Pluto 2,377 km, Charon 1,212 km",
           "NASA Science: Triton orbits Neptune in the opposite direction of the planet's rotation (retrograde); Titan's surface pressure is about 1.5 times Earth's",
           "NASA Science: Pluto and Charon orbit a common center of mass in the space between them",
           "Own calculations (moon diameter ÷ planet diameter): Charon 51.0%, Moon 27.2%, Triton 5.5%, Titan 4.3%, Ganymede 3.7%"]
