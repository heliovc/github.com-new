# EP17 — What If We Swapped the Sun for 5 Other Stars?
# Structure NEW: "star swap" — same Earth, same orbit (1 AU), five replacement stars, one per chapter; each chapter = a trading-card intro,
# the noon sky from a beach (true angular size), Earth's new temperature and where the Earth-like zone moves. Keeps EP16's promise (the
# biggest star in place of the Sun) as the finale, but EP05 already did "grow a star", so here everything is seen FROM EARTH.
# Palette: each star's own blackbody colour (bbcol17) — red dwarf, gold, blue-white, violet-white, orange — on a deep navy sky.
# New scenes: swapsky, starcard, hzmap, earthtemp.
# Own calculations (Python): Earth temperature T = 288 K × L^0.25 (same distance, same air and clouds — a simple estimate);
# Earth-like zone = Kopparapu et al. (2013) conservative 0.99–1.70 AU × √L; year at 1 AU = 1/√M; disc = R × 0.533°.
# Proxima: L 0.00157, R 0.154, M 0.122 → −216 °C, zone 0.039–0.067 AU, year 2.86 yr (1,046 d), disc 0.082° (1/6.5 Sun).
# Alpha Cen A: L 1.52, R 1.22, M 1.1 → +47 °C, zone 1.22–2.10 AU (Mars 1.52 inside), year 348 d.
# Sirius A: L 25, R 1.71, M 2.06 → +371 °C, zone 4.95–8.5 AU (Jupiter 5.2), year 254 d, peak 293 nm.
# Sirius B: L 0.056, R 0.0081 (0.88 Earth radii), M 1.02, 25,000 K → −133 °C, zone 0.23–0.40 AU (Mercury 0.387), disc 15.5", 352× the Sun's surface brightness.
# Stephenson 2-18: R 2,150 (10.0 AU, Saturn 9.54 AU), L ~440,000 (range 90,000–630,000) → zone ~660–1,130 AU, light 3.8 days old.
TITLE = "What If We Swapped the Sun for 5 Other Stars?"
GOLD17 = [255, 200, 90]
RED17 = [255, 120, 80]
BLUE17 = [150, 190, 255]
GRN17 = [120, 230, 150]

PROX = {"name": "Proxima Centauri", "L": 0.00157, "R": 0.154, "T": 3000}
ACEN = {"name": "Alpha Centauri A", "L": 1.52, "R": 1.22, "T": 5790}
SIRA = {"name": "Sirius A", "L": 25.0, "R": 1.71, "T": 9900}
SIRB = {"name": "Sirius B", "L": 0.056, "R": 0.0081, "T": 25000}
ST218 = {"name": "Stephenson 2-18", "L": 440000.0, "R": 2150.0, "T": 3200}
def S(base, **kw): d = dict(base); d.update(kw); return d

SCENES = [
 # ---------- HOOK ----------
 {"say": "This is a normal day at the beach. Now, without moving Earth an inch, we swap the Sun for the closest star to us. In about eight minutes, the sky goes dark. The ocean starts to freeze. And within weeks, the air itself snows onto the ground.",
  "vis": {"type": "swapsky", **S(PROX, from_sun=True), "head": "Same Earth. Different star."}},
 {"say": "Our Sun is just one star out of hundreds of billions. So what if Earth had gotten a different one? Today we try five of them. Same planet, same orbit, five very different skies. And the last one is so big, Earth ends up inside it.",
  "vis": {"type": "title", "title": "What If We Swapped the Sun\nfor 5 Other Stars?", "sub": "COSMIC SCALE", "brand": True, "subcol": GOLD17}},
 {"say": "First, the rules. Earth stays exactly where it is, one hundred and fifty million kilometers from the center. We keep the same air, the same oceans, the same clouds. Only the star changes. Then we ask three questions. What does the sky look like? How warm does Earth get? And where would a planet need to be, to stay like home?",
  "vis": {"type": "bullets", "title": "The rules of the swap", "items": ["Earth stays at 150 million km", "same air, oceans and clouds", "1. what does the sky look like?", "2. how warm is Earth?", "3. where is the Earth-like zone?"], "col": GOLD17}},

 # ---------- SWAP 1: PROXIMA ----------
 {"say": "Swap number one. Proxima Centauri, the nearest star to the Sun, four point two four light years away. It's a red dwarf. About one seventh the width of the Sun, and around three thousand degrees at the surface, almost half as hot.",
  "vis": {"type": "starcard", **PROX, "kicker": "SWAP 1 OF 5", "sub": "a red dwarf, our nearest neighbour", "dist": "4.24 light-years from us"}},
 {"say": "From the beach, it's a tiny red disc. Six and a half times narrower than the Sun. And it's weak. Proxima gives off less than a sixth of one percent of the Sun's energy, and most of that is infrared, which your eyes can't see. Noon would look like deep twilight. You'd see stars in the middle of the day.",
  "vis": {"type": "swapsky", **PROX, "head": "Noon under Proxima Centauri", "caption": "0.16% of today's sunlight, mostly infrared"}},
 {"say": "So how cold? A simple estimate, scaling today's average temperature to the new starlight, gives about minus two hundred and sixteen degrees. Cold enough that nitrogen, most of the air you breathe, freezes solid. Earth's sky would literally fall as snow.",
  "vis": {"type": "earthtemp", "temp": -216, "head": "Proxima: the air freezes"}},
 {"say": "To be comfortable around Proxima, a planet would have to hug it. Its Earth-like zone sits around four to seven percent of our distance from the Sun. That's six times closer than Mercury. And there really is a planet there. Proxima b, with a year that lasts just eleven days.",
  "vis": {"type": "hzmap", **PROX, "max": 1.6, "kicker": "SWAP 1 · EARTH-LIKE ZONE", "note": "6× closer than Mercury"}},
 {"say": "Even then, there's a catch. Red dwarfs are violent. In twenty nineteen, astronomers caught Proxima flaring so hard that it brightened fourteen thousand times in ultraviolet light, in just seconds. Living next to Proxima means living next to a star that sneezes radiation.",
  "vis": {"type": "bignumber", "from": 1, "to": 14000, "suffix": "×", "col": RED17, "caption": "Proxima's 2019 flare, far-ultraviolet brightening (MacGregor et al. 2021)"}},
 {"say": "One more strange thing. Proxima has only an eighth of the Sun's mass, so its pull is weaker. At our distance, Earth would orbit more slowly. One year would last almost three of our years. About one thousand and forty six days between birthdays.",
  "vis": {"type": "bignumber", "from": 365, "to": 1046, "suffix": " days", "col": RED17, "caption": "one year at Earth's distance from Proxima (our calculation)"}},

 # ---------- SWAP 2: ALPHA CEN A ----------
 {"say": "Swap number two should be the easy one. Alpha Centauri A, Proxima's big sister, four point three seven light years away. It's almost a twin of the Sun. Nearly the same color, about ten percent more mass.",
  "vis": {"type": "starcard", **ACEN, "kicker": "SWAP 2 OF 5", "sub": "the Sun's near-twin", "dist": "4.37 light-years from us"}},
 {"say": "From the beach, you'd barely notice. The disc is twenty two percent wider. The light is the same golden white. But it's fifty two percent brighter. And that is a big deal.",
  "vis": {"type": "swapsky", **S(ACEN, from_sun=True), "head": "Noon under Alpha Centauri A", "caption": "152% of today's sunlight"}},
 {"say": "Our simple estimate puts the average temperature near forty seven degrees. But the real problem is water. Climate models suggest that just a few percent more sunlight, around six percent, could tip Earth into a runaway greenhouse. Warmer oceans put more water vapor in the air, which traps more heat, which puts in more water vapor. Fifty two percent more, and the oceans would slowly boil away into the sky.",
  "vis": {"type": "earthtemp", "temp": 47, "head": "The twin that boils the oceans"}},
 {"say": "Where's the safe spot now? It slides outward, to about one point two to two point one times our distance. And look who's sitting in it. Mars. Around Alpha Centauri A, Mars would be the planet in the Goldilocks zone, and Earth would be the new Venus.",
  "vis": {"type": "hzmap", **ACEN, "max": 6, "hl": "Mars", "kicker": "SWAP 2 · EARTH-LIKE ZONE", "note": "Mars moves into the zone"}},

 # ---------- SWAP 3: SIRIUS A ----------
 {"say": "Swap number three. Sirius, the brightest star in our night sky, eight point six light years away. Sirius is actually two stars. We start with the big one, Sirius A. Twice the Sun's mass, almost ten thousand degrees at the surface, and about twenty five times brighter.",
  "vis": {"type": "starcard", **SIRA, "kicker": "SWAP 3 OF 5", "sub": "the brightest star in our night sky", "dist": "8.6 light-years from us"}},
 {"say": "Now the beach changes completely. The disc is almost twice as wide as the Sun, and blue white. The whole sky turns into a blinding pale glare. And the light is different. Sirius is so hot that its output peaks in the ultraviolet, around two hundred and ninety nanometers. Sunburn would take seconds, not minutes.",
  "vis": {"type": "swapsky", **S(SIRA, from_sun=True), "head": "Noon under Sirius A", "caption": "25 times today's sunlight, peaking in ultraviolet"}},
 {"say": "Temperature? Our estimate lands around three hundred and seventy degrees. Hot enough to melt lead. Oceans gone, rocks glowing in the dark side's twilight. Earth wouldn't become the new Venus. It would be on its way to becoming the new Mercury.",
  "vis": {"type": "earthtemp", "temp": 371, "head": "Sirius A: lead melts"}},
 {"say": "To get Earth's weather back, you'd have to move out to about five times our distance. Which is almost exactly where Jupiter orbits. Around Sirius, the comfortable seat belongs to Jupiter's orbit. And with Sirius's stronger gravity, a year at our distance would last just two hundred and fifty four days.",
  "vis": {"type": "hzmap", **SIRA, "max": 12, "hl": "Jupiter", "kicker": "SWAP 3 · EARTH-LIKE ZONE", "note": "Jupiter's orbit is the new home"}},

 # ---------- SWAP 4: SIRIUS B ----------
 {"say": "Swap number four is the strangest. Sirius A's tiny partner, Sirius B. It's a white dwarf, the leftover core of a star that already died. It holds about as much mass as the Sun, crushed into a ball slightly smaller than Earth.",
  "vis": {"type": "starcard", **SIRB, "kicker": "SWAP 4 OF 5", "sub": "a dead star's core, smaller than Earth", "dist": "8.6 light-years from us"}},
 {"say": "From the beach, there's no disc at all. Just a point, fifteen arcseconds wide. Smaller in the sky than Venus can look through binoculars. But every patch of its surface, at about twenty five thousand degrees, shines over three hundred times harder than the same patch of the Sun. A tiny, violet white welding spark that you could never look at.",
  "vis": {"type": "swapsky", **S(SIRB, from_sun=True), "head": "Noon under Sirius B", "caption": "a point of light giving 5.6% of today's sunlight"}},
 {"say": "Overall, it's so small that it gives off only about five and a half percent of the Sun's energy. The days would be dim and harsh at the same time. And Earth would freeze to about minus one hundred and thirty degrees. Water ice everywhere. The air stays, barely.",
  "vis": {"type": "earthtemp", "temp": -133, "head": "Sirius B: a frozen Earth"}},
 {"say": "Here's the twist. Sirius B has almost exactly the Sun's mass. So if you swapped them, Earth's orbit would hardly change. The year would still be about three hundred and sixty two days. And the warm zone? It shrinks inward to about a quarter to four tenths of our distance. Right on top of Mercury.",
  "vis": {"type": "hzmap", **SIRB, "max": 1.6, "hl": "Mercury", "kicker": "SWAP 4 · EARTH-LIKE ZONE", "note": "Mercury would be the lucky one"}},

 # ---------- SWAP 5: STEPHENSON 2-18 ----------
 {"say": "And now, as promised, swap number five. Stephenson two eighteen, one of the largest stars ever measured, nearly nineteen thousand light years away. Some estimates put it at around two thousand one hundred and fifty times the width of the Sun.",
  "vis": {"type": "starcard", **ST218, "kicker": "SWAP 5 OF 5", "sub": "a red supergiant, one of the largest known", "dist": "about 19,000 light-years from us"}},
 {"say": "Put that in the Sun's place, and there is no sky. Its surface would reach about ten times our distance from the Sun. Past Mercury, Venus, Earth, Mars, Jupiter, and out beyond the orbit of Saturn. Earth wouldn't orbit Stephenson two eighteen. Earth would be inside it.",
  "vis": {"type": "hzmap", **ST218, "max": 40, "kicker": "SWAP 5 · WHERE THE SURFACE ENDS", "note": "its surface passes Saturn"}},
 {"say": "Not inside a solid ball, though. The outer layers of a red supergiant are thinner than the best vacuum we can make in many labs. But they're hot, thousands of degrees, and glowing in every direction. Earth would plow through a red-hot fog, dragging against it, spiraling deeper. It would vaporize long before reaching the core.",
  "vis": {"type": "swapsky", **ST218, "mode": "inside", "big": "EARTH IS INSIDE THE STAR", "sub": "a glowing fog at thousands of degrees, in every direction"}},
 {"say": "So where would Earth need to be? This star may shine hundreds of thousands of times brighter than the Sun. One published estimate is about four hundred and forty thousand. If that's right, the Earth-like zone sits around six hundred and sixty to eleven hundred times our distance. Seventeen times farther than Pluto. Out there, the sunlight on your face would have left the star almost four days earlier.",
  "vis": {"type": "hzmap", **ST218, "max": 1300, "kicker": "SWAP 5 · EARTH-LIKE ZONE", "note": "17× farther than Pluto"}},
 {"say": "And it wouldn't last. Stars this big burn fast, living only a few million years before they collapse and explode. Our Sun has been shining steadily for about four and a half billion years. Life on Earth needed most of that time.",
  "vis": {"type": "compare", "left": ["THE GIANT", "lives a few million years", "ends as a supernova", "way too short for life"], "right": ["OUR SUN", "4.6 billion years so far", "about 5 billion to go", "time for life to evolve"], "cols": [RED17, GOLD17], "strike": False}},

 # ---------- THE TWIST ----------
 {"say": "So, five swaps, and not one of them works. Frozen air. Boiling oceans. Melting lead. A frozen Earth under a pinprick. And a planet swallowed whole.",
  "vis": {"type": "bullets", "title": "Five swaps, zero winners", "items": ["1. Proxima: the air freezes", "2. Alpha Centauri A: oceans boil", "3. Sirius A: lead melts", "4. Sirius B: a frozen Earth", "5. Stephenson 2-18: Earth inside"], "col": GOLD17}},
 {"say": "But here's the part that really surprised me. If you picked a star at random from the Milky Way, it probably wouldn't look like the Sun at all. About three out of every four stars in our galaxy are red dwarfs, like Proxima. So a random swap would most likely leave Earth frozen, under a dim red dot.",
  "vis": {"type": "bignumber", "from": 0, "to": 75, "suffix": "%", "col": RED17, "caption": "share of Milky Way stars that are red dwarfs (NASA)"}},
 {"say": "Our ordinary yellow Sun is not so ordinary. It's brighter than most stars, calm, long-lived, and Earth sits right in its narrow comfortable zone. Change the star, and the same planet becomes a snowball, an oven, or a memory.",
  "vis": {"type": "hzmap", "name": "Our Sun", "L": 1.0, "R": 1.0, "T": 5772, "max": 6, "kicker": "THE ORIGINAL", "note": "Earth sits right inside it"}},

 # ---------- NEXT ----------
 {"say": "Next time, we drop something into the biggest planet we have. What would actually happen if you fell into Jupiter? There's no ground to land on, and the answer gets stranger the deeper you go. Subscribe to Cosmic Scale so you don't miss it. And tell me in the comments, which star would you swap our Sun for?",
  "vis": {"type": "title", "title": "Next: what if you\nfell into Jupiter?", "sub": "COSMIC SCALE", "subcol": GOLD17}},
]

SOURCES = ["Proxima Centauri: radius 0.154 solar radii, mass 0.122 solar masses, luminosity about 0.0016 of the Sun, surface about 3,000 K, distance 4.24 light-years (ESO; Ribas et al. 2017; Wikipedia summary of published values)",
           "Proxima b: orbital period 11.2 days, about 0.049 AU from its star (Anglada-Escudé et al. 2016, Nature)",
           "MacGregor et al. (2021), Astrophysical Journal Letters: a 2019 flare on Proxima Centauri brightened about 14,000 times in far-ultraviolet light within seconds",
           "Alpha Centauri A: radius 1.22 solar radii, mass about 1.1 solar masses, luminosity about 1.52 suns, surface about 5,790 K, distance 4.37 light-years (Kervella et al. 2017, VLTI/PIONIER)",
           "Sirius A: radius 1.71 solar radii, mass 2.06 solar masses, luminosity about 25 suns, surface about 9,900 K; Sirius B: white dwarf, about 1.02 solar masses, radius about 0.0081 solar radii (0.88 Earth radii), surface about 25,000 K, luminosity about 0.056 suns; distance 8.6 light-years (Bond et al. 2017, HST astrometry)",
           "Stephenson 2-18: estimated radius about 2,150 solar radii; luminosity estimates from about 90,000 to 630,000 suns (440,000 used here); distance about 19,000 light-years; both depend on its assumed membership in the Stephenson 2 cluster",
           "Kopparapu et al. (2013), Astrophysical Journal: conservative habitable zone for the Sun about 0.99 to 1.70 AU; runaway greenhouse at about 6% more sunlight than Earth receives today",
           "NASA: about three out of four stars in the Milky Way are red dwarfs; the Sun is about 4.6 billion years old",
           "Nitrogen freezes at about −210 °C; lead melts at 327 °C; Venus's average surface temperature about 464 °C (NASA)",
           "Own calculations (Python): average temperature = 288 K × (luminosity)^0.25 at Earth's distance, keeping the same air and clouds (a simple estimate, not a climate model); Earth-like zone scaled by the square root of luminosity; year at 1 AU = 1/√(mass); disc size = radius × 0.533°; Stephenson 2-18 radius = 10.0 AU; light travel time to 663 AU = 3.8 days"]
