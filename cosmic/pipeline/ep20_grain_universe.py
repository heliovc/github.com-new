# EP20 — If the Sun Were a Grain of Sand, the Universe Would Fit Inside Our Solar System
# Structure NEW: "the walk" — one fixed scale (the Sun = a 1 mm grain of sand, 1 mm = 1,391,400 km) and a walk from a tabletop to the edge
# of the observable universe. Every chapter opens on a wooden trail signpost (signpost) whose planks list the next destinations and their
# distance AT THIS SCALE; the walker's odometer and walking time (5 km/h, nonstop) grow chapter by chapter. Reveal: the whole observable
# universe at this scale (4,227 AU wide) would sit inside the REAL solar system's Oort cloud. Twist: flip the scale (universe = Earth-sized).
# Keeps EP19's promise (shrink the universe until the Sun is a grain of sand, then walk to the edge). Different from scale16 (a Short on the
# same scale): here the walk goes all the way to the edge, adds the light-is-slower-than-a-snail beat, stars vs galaxies spacing and the flip.
# Palette: sand beige / trail green / dusk violet on deep indigo.
# New scenes: signpost, tabletop, fieldmap, snailrace, fitinside.
# Own calculations (Python): scale 1 mm = 1,391,400 km (NASA Sun diameter).
#   Earth 12,742 km -> 9.2 µm; Moon 3,474.8 km -> 2.5 µm, 384,400 km -> 0.28 mm from Earth; Jupiter 142,984 km -> 0.10 mm.
#   1 AU -> 10.75 cm; Jupiter 5.2 AU -> 56 cm; Neptune 30.07 AU -> 3.23 m; Voyager 1 173 AU (1 light-day, Nov 2026) -> 18.6 m.
#   Oort cloud 2,000-100,000 AU -> 215 m to 10.75 km. 1 light-year -> 6.80 km; Proxima Centauri 4.2465 ly -> 28.9 km (5.8 h walk at 5 km/h).
#   Milky Way ~100,000 ly -> 680,000 km = 1.77 × Earth-Moon distance, 15.5 years walking. Andromeda 2.5 million ly -> 17.0 million km = 44 ×
#   Earth-Moon, 388 years walking. Light: 299,792 km/s -> 0.215 mm/s = 78 cm per hour; 10.75 cm in 8 min 19 s (same as real time).
#   Observable universe radius 46.5 billion ly -> 316 billion km = 2,113 AU; diameter 4,227 AU = 0.067 ly = 24 × Voyager 1's distance;
#   walk to the edge 7.2 million years. Flip: universe 8.8e26 m -> Earth 12,742 km (factor 6.9e19): Sun 0.02 nm, Milky Way 13.7 m.
# EP20 promises EP21: how many Earths fit inside the biggest things in the universe.
TITLE = "If the Sun Were a Grain of Sand, the Universe Would Fit Inside Our Solar System"
SAND = [240, 210, 150]
TRAIL = [130, 215, 150]
DUSK = [175, 145, 255]

SCENES = [
 # ---------- HOOK ----------
 {"say": "This is the Sun. Shrunk to a single grain of sand. Keep that scale, and something impossible happens. The entire observable universe, every galaxy we can see, would fit inside our own solar system.",
  "vis": {"type": "fitinside", "mode": "hook"}},
 {"say": "Today we take that grain of sand, and we walk. From a tabletop, to the nearest star, to the edge of everything. And we'll keep a stopwatch running the whole way.",
  "vis": {"type": "title", "title": "If the Sun Were\na Grain of Sand", "sub": "COSMIC SCALE", "brand": True, "subcol": SAND}},
 {"say": "The rule. The real Sun is about one point three nine million kilometers wide. Our grain is one millimeter. So every millimeter on our walk stands for almost one point four million kilometers. We never change that rule. Not once.",
  "vis": {"type": "compare", "left": ["THE SUN", "1,391,400 km wide", "333,000 Earths of mass", "8 light-minutes away"], "right": ["OUR GRAIN", "1 millimeter wide", "fits on a fingertip", "1 mm = 1.39 million km"], "cols": [SAND, TRAIL], "strike": False}},
 {"say": "Here's our trail sign. Five stops. The Earth, the edge of the solar system, the nearest star, our galaxy, and the edge of the observable universe. First stop. Our own desk.",
  "vis": {"type": "signpost", "n": 0, "km": 0, "title": "THE TRAIL", "sub": "1 mm = 1,391,400 km · walking at 5 km/h"}},

 # ---------- STOP 1: THE DESK ----------
 {"say": "Put the grain on a table. Where is Earth? Not touching it. Earth sits about eleven centimeters away. About the length of your hand. And Earth itself is a speck of nine micrometers. Ten times thinner than a human hair. You could not see it without a microscope. And one whole year, Earth's entire orbit, is a circle about the size of a dinner plate.",
  "vis": {"type": "tabletop", "mode": "earth"}},
 {"say": "Now zoom in on that speck. The Moon is a smaller speck, a quarter of a millimeter away. Every human who ever traveled in space stayed inside that quarter of a millimeter. Every one of them.",
  "vis": {"type": "tabletop", "mode": "moon"}},
 {"say": "Jupiter, the biggest planet, is a tenth of a millimeter wide, and it sits fifty six centimeters from the grain. Across the desk. Saturn is just over a meter out. Neptune, the last planet, is more than three meters away. Across the room.",
  "vis": {"type": "tabletop", "mode": "jupiter"}},
 {"say": "And Voyager one, the farthest spacecraft we ever launched? After forty nine years of flying, it has reached one light day from the Sun. On our table, that's eighteen point six meters. It hasn't even left the building.",
  "vis": {"type": "fieldmap", "z0": 4, "z1": 40, "mode": "house"}},
 {"say": "Stop one, done. Our odometer reads eighteen meters, and the walk has taken about thirteen seconds.",
  "vis": {"type": "signpost", "n": 1, "km": 0.0186, "title": "STOP 1 · THE DESK", "sub": "Earth 10.75 cm · Neptune 3.2 m · Voyager 1 18.6 m"}},

 # ---------- LIGHT IS A SNAIL ----------
 {"say": "Before we go on, here's the strangest thing about this scale. Light. In real life, light from the Sun reaches Earth in about eight minutes. On our table, it still takes eight minutes, but it only has to cross eleven centimeters.",
  "vis": {"type": "snailrace", "mode": "sun"}},
 {"say": "So at this scale, light crawls. Point two millimeters per second. Seventy eight centimeters per hour. A garden snail would beat it. Remember that, because every distance from here on, light needs years to cover.",
  "vis": {"type": "snailrace", "mode": "race"}},

 # ---------- STOP 2: THE OORT CLOUD ----------
 {"say": "Stop two. The real edge of the Sun's family. Far beyond Neptune there's a giant shell of icy bodies called the Oort cloud. Nobody has ever seen it directly, but long period comets come from there.",
  "vis": {"type": "signpost", "n": 2, "km": 0.215, "title": "STOP 2 · THE OORT CLOUD", "sub": "a shell of icy bodies around the Sun"}},
 {"say": "NASA puts its inner edge somewhere between two thousand and five thousand times Earth's distance from the Sun, and its outer edge as far as a hundred thousand. On our walk, the shell starts about two hundred meters from the grain, and reaches almost eleven kilometers out. The size of a whole town, with a grain of sand in the middle.",
  "vis": {"type": "fieldmap", "z0": 40, "z1": 14000, "mode": "oort"}},
 {"say": "Our odometer reads ten point eight kilometers. About two hours of walking. And we haven't reached a single other star yet.",
  "vis": {"type": "signpost", "n": 2, "km": 10.75, "title": "STOP 2 · THE OORT CLOUD", "sub": "outer edge: 10.75 km · 2 h 10 min on foot"}},

 # ---------- STOP 3: THE NEAREST STAR ----------
 {"say": "Stop three. Proxima Centauri, the closest star to the Sun. Four point two four light years away. At our scale, every light year is six point eight kilometers. So Proxima is another grain of sand, about twenty nine kilometers from ours.",
  "vis": {"type": "fieldmap", "z0": 14000, "z1": 40000, "mode": "proxima"}},
 {"say": "That's almost six hours of walking, and the whole way there is empty. Two grains of sand, twenty nine kilometers apart, and almost nothing in between. That's what our part of the galaxy is like. Grains of sand, tens of kilometers apart. Its neighbors, Alpha Centauri A and B, a pair of Sun-like stars, sit just beyond, about thirty kilometers out.",
  "vis": {"type": "signpost", "n": 3, "km": 28.9, "title": "STOP 3 · PROXIMA CENTAURI", "sub": "28.9 km · about 6 hours on foot"}},
 {"say": "And light, our snail, needs four years and three months to crawl that far. Same as in real life. The scale changes the distances. It never changes the time light takes.",
  "vis": {"type": "snailrace", "mode": "proxima"}},

 # ---------- STOP 4: THE MILKY WAY ----------
 {"say": "Stop four. Our galaxy. The Milky Way is about one hundred thousand light years across, with somewhere between one hundred and four hundred billion stars. At our scale, that's six hundred eighty thousand kilometers wide.",
  "vis": {"type": "signpost", "n": 4, "km": 680000, "title": "STOP 4 · THE MILKY WAY", "sub": "680,000 km wide · 100-400 billion grains"}},
 {"say": "Wider than the distance from Earth to the Moon. Almost twice as wide. A disc of sand grains, each one tens of kilometers from its neighbor, that would stretch past the Moon's orbit. Walking across it, nonstop, would take fifteen and a half years.",
  "vis": {"type": "fieldmap", "z0": 4.0e5, "z1": 1.5e6, "mode": "galaxy"}},
 {"say": "And at the center sits its black hole, Sagittarius A star. About four million times the mass of the Sun, with an event horizon about twenty four million kilometers wide. On our walk, it's a dark bead less than two centimeters across, a hundred eighty kilometers from our grain. A long drive, with a black marble at the end.",
  "vis": {"type": "fieldmap", "z0": 1.5e6, "z1": 1.5e6, "mode": "center"}},
 {"say": "Now the next galaxy, Andromeda. Two and a half million light years away. Seventeen million kilometers at our scale. Forty four trips to the Moon. Almost four hundred years on foot.",
  "vis": {"type": "fieldmap", "z0": 1.5e6, "z1": 2.6e7, "mode": "andromeda"}},
 {"say": "And here's the paradox. Stars are tiny compared to the gaps between them. Twenty nine kilometers between two one millimeter grains. But galaxies are big compared to their gaps. Andromeda is only about twenty five Milky Ways away.",
  "vis": {"type": "compare", "left": ["STARS", "grain: 1 mm", "gap: 29 km", "29 million grain-widths"], "right": ["GALAXIES", "Milky Way: 680,000 km", "gap: 17 million km", "25 galaxy-widths"], "cols": [SAND, DUSK], "strike": False}},
 {"say": "That's why stars almost never crash into each other, but galaxies do. Hubble measurements in twenty twelve predicted that Andromeda will collide with us in about four billion years. A newer study in twenty twenty five says it's closer to a coin flip over the next ten billion. Either way, the stars themselves would mostly slide past each other.",
  "vis": {"type": "fieldmap", "z0": 2.6e7, "z1": 2.6e7, "mode": "collide"}},

 # ---------- STOP 5: THE EDGE ----------
 {"say": "Last stop. The edge of the observable universe. Its light set out almost fourteen billion years ago, but space kept stretching, so that edge is now about forty six and a half billion light years away in every direction.",
  "vis": {"type": "signpost", "n": 5, "km": 3.16e11, "title": "STOP 5 · THE EDGE", "sub": "46.5 billion light-years in every direction"}},
 {"say": "At our scale, that's three hundred sixteen billion kilometers. Walking nonstop, at five kilometers per hour, you would arrive in about seven point two million years. About twenty four times longer than our species has existed. In a car at a hundred kilometers an hour, still three hundred sixty thousand years.",
  "vis": {"type": "bignumber", "from": 0, "to": 7.2, "decimals": 1, "suffix": " million years", "col": DUSK, "caption": "walking to the edge at 5 km/h, nonstop, at our scale"}},
 {"say": "And remember, that edge is not a wall. It's only as far as light has had time to reach us. There's almost certainly more universe beyond it. We just can't see it, and we covered why in episode sixteen. Our walk ends at the edge of what we can see.",
  "vis": {"type": "signpost", "n": 5, "km": 3.16e11, "km0": 3.16e11, "title": "THE EDGE IS NOT A WALL", "sub": "only as far as light has reached us"}},
 {"say": "But three hundred sixteen billion kilometers is a distance we can actually picture. It's about two thousand one hundred times the real distance from Earth to the Sun. Which brings us back to the hook.",
  "vis": {"type": "fitinside", "mode": "zoom"}},
 {"say": "So take the shrunken universe, about four thousand two hundred times the Earth Sun distance from side to side, and set it down in the real solar system. Voyager one is at one hundred seventy three. The Oort cloud reaches out to a hundred thousand.",
  "vis": {"type": "fitinside", "mode": "real"}},
 {"say": "Every galaxy we can see, shrunk until the Sun is a grain of sand, would fit inside the Sun's own cloud of comets. The universe, inside our backyard.",
  "vis": {"type": "fitinside", "mode": "reveal"}},

 # ---------- TWIST: FLIP THE SCALE ----------
 {"say": "Now flip it. Shrink the whole observable universe until it's the size of planet Earth. How big is the Milky Way now? About fourteen meters. The size of a bus, parked somewhere on a planet sized universe.",
  "vis": {"type": "compare", "left": ["FLIPPED", "universe = Earth-sized", "Milky Way: 13.7 m", "about a bus"], "right": ["THE SUN", "0.02 nanometers", "smaller than", "one hydrogen atom"], "cols": [TRAIL, SAND], "strike": False}},
 {"say": "And the Sun? Two hundredths of a nanometer. Smaller than a single hydrogen atom. Our whole star, invisible inside one atom's width, in a galaxy the size of a bus.",
  "vis": {"type": "bignumber", "from": 1, "to": 0.02, "decimals": 2, "suffix": " nm", "col": SAND, "caption": "the Sun, if the observable universe were the size of Earth"}},

 # ---------- RECAP ----------
 {"say": "So, our walk. The Earth, eleven centimeters. Voyager, eighteen meters. The Oort cloud, a town. The nearest star, a six hour hike. The Milky Way, wider than the Moon's orbit. And the edge, seven million years away on foot, but small enough to fit in our own solar system.",
  "vis": {"type": "bullets", "title": "The grain-of-sand walk", "items": ["Earth · 10.75 cm", "Oort cloud · up to 10.75 km", "Proxima · 28.9 km", "Milky Way · 680,000 km", "The edge · 316 billion km"], "col": SAND, "highlight": 4}},

 # ---------- NEXT ----------
 {"say": "Next time, we'll count how many Earths fit inside the biggest things in the universe, from the Sun to the largest black hole ever found. Subscribe to Cosmic Scale so you don't miss it. And tell me in the comments, which stop on this walk surprised you most?",
  "vis": {"type": "title", "title": "Next: how many Earths\nfit inside?", "sub": "COSMIC SCALE", "subcol": TRAIL}},
]

SOURCES = ["NASA Sun Fact Sheet (NSSDC): volumetric mean diameter about 1,391,400 km; mass about 333,000 Earths; mean distance 149.6 million km (1 AU), sunlight takes about 8.3 minutes",
           "NASA Earth and Moon Fact Sheets: Earth mean diameter 12,742 km; Moon diameter 3,474.8 km, mean distance 384,400 km; Jupiter equatorial diameter 142,984 km, 5.2 AU; Saturn 9.54 AU, Neptune 30.07 AU",
           "NASA/JPL: Voyager 1 reaches one light-day (about 173 AU) from Earth in November 2026, 49 years after launch",
           "NASA Science, Oort Cloud: inner edge thought to lie between 2,000 and 5,000 AU from the Sun, outer edge between 10,000 and 100,000 AU",
           "ESO / NASA: Proxima Centauri is about 4.24 light-years away, the closest known star to the Sun; Alpha Centauri A and B about 4.37 light-years",
           "NASA: the Milky Way is about 100,000 light-years across and holds an estimated 100 to 400 billion stars; Andromeda is about 2.5 million light-years away",
           "NASA/STScI (2012), Hubble measurements: Andromeda and the Milky Way are predicted to collide in about 4 billion years; Sawala et al. (2025), Nature Astronomy: about a 50 percent chance of a merger within the next 10 billion years",
           "Event Horizon Telescope (2022): Sagittarius A* has about 4 million solar masses and lies about 27,000 light-years away; Schwarzschild radius = 2GM/c² = 2.95 km per solar mass",
           "Guinness World Records: the fastest snail on record (1995) covered 13 inches (33 cm) in 2 minutes, about 2.75 mm per second",
           "Hublin et al. (2017), Nature: the oldest known Homo sapiens fossils are about 300,000 years old",
           "Planck 2018 cosmology: the observable universe is about 46.5 billion light-years in radius (about 93 billion light-years across), the universe is about 13.8 billion years old",
           "Own calculations (Python): 1 mm = 1,391,400 km; Earth 9.2 µm at 10.75 cm; Moon 0.28 mm from Earth; Jupiter 0.10 mm at 56 cm; Saturn 1.03 m; Neptune 3.23 m; Voyager 1 18.6 m; Oort cloud 215 m to 10.75 km; 1 light-year = 6.80 km; Earth's orbit 21.5 cm across; Proxima 28.9 km (5.8 h at 5 km/h), Alpha Centauri A/B 29.7 km; Sagittarius A* horizon 23.6 million km across (4.0 million Suns) = 17 mm, 27,000 light-years = 184 km; Milky Way 680,000 km = 1.77 Earth-Moon distances, 15.5 years on foot; Andromeda 17.0 million km = 44 Earth-Moon distances, 388 years on foot; light 0.215 mm/s = 78 cm per hour; edge 316 billion km = 2,113 AU (4,227 AU across, 24 times Voyager 1's distance), 7.2 million years on foot (24 times 300,000 years), 360,000 years at 100 km/h; flipped scale (universe 93 billion light-years = 12,742 km): Milky Way 13.7 m, Sun 0.02 nm (a hydrogen atom is about 0.1 nm across)"]
