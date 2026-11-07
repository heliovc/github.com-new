# EP05 — The Largest Star vs the Sun
# Structure NEW: "five ways to feel one giant" — lineup, solar-system test, the flight, the jar, the beam of light,
# with two interludes (how we measure a star / why a star can't get bigger) and the twist (the record holder changed).
# Palette: supergiant crimson / mint. New scene types: lineup, engulf, flight, density, interfero, ceiling
# Own calculations (Python): Sun diameter 1.392 million km; a 1,500x star has radius ~6.98 AU (between Jupiter 5.2 and Saturn 9.5 AU),
# volume 1500^3 = 3.375 billion Suns = ~4.4 quadrillion Earths (x1.3 million); light crosses the Sun in 4.6 s and the giant in ~1.9 h;
# a 900 km/h jet circles the Sun in ~202 days and the giant in ~830 years; mean density of a 20-Sun-mass, 1,500x star
# = 1.41 g/cm3 x 20 / 1500^3 = 8.4e-9 g/cm3, ~150,000x thinner than sea-level air (1.225e-3 g/cm3);
# Betelgeuse 764 Rsun = 3.55 AU; Michelson-Pease angle 0.047" = a 2 cm coin seen from ~88 km; Earth's equator ~1,670 km/h.
TITLE = "The Largest Star vs the Sun"
RSG = [232, 67, 74]
MINT = [111, 242, 200]

SCENES = [
 # ---------- HOOK ----------
 {"say": "If the largest stars we know took the Sun's place, you would be living inside one. Earth, Mars, even Jupiter, all orbiting deep inside a single star. And here's the strange part. Most of that star is thinner than the air in your room.",
  "vis": {"type": "engulf", "r_au": 6.98, "fast": True, "head": "Your home, inside a star"}},
 {"say": "Today we put our Sun next to the biggest stars ever measured, and we'll feel the difference in five ways. A lineup, a flight, a jar, a beam of light, and a solar system swallowed whole. Then the two questions nobody asks. How do you even measure a star you can't reach? And why can't a star grow any bigger?",
  "vis": {"type": "bullets", "title": "Five ways to feel a giant", "items": ["The lineup", "The solar-system test", "The flight", "The jar", "The beam of light"], "col": MINT, "highlight": -1}},
 {"say": "The Largest Star versus the Sun.",
  "vis": {"type": "title", "title": "The Largest Star\nvs the Sun", "sub": "COSMIC SCALE", "brand": True, "subcol": RSG}},

 # ---------- THE SUN FIRST ----------
 {"say": "First, give the Sun some respect. It's about one point four million kilometers across. About one point three million Earths would fit inside it. NASA calls it an average star in size. But most stars in our galaxy are red dwarfs, smaller and dimmer than the Sun. In a random crowd of stars, our Sun would stand out as one of the big ones.",
  "vis": {"type": "lineup", "stage": 0, "caption": "1.4 million km across · 1.3 million Earths inside"}},

 # ---------- HOW WE MEASURE ----------
 {"say": "Now the problem. Every star except the Sun is so far away that, even in the biggest telescopes, it looks like a point of light. So how do you measure the width of a point? In December nineteen twenty, Albert Michelson and Francis Pease tried something clever on the giant telescope at Mount Wilson. They caught the light of Betelgeuse with two small mirrors set several meters apart, and combined the two beams.",
  "vis": {"type": "interfero", "stage": 0, "head": "Mount Wilson · December 1920"}},
 {"say": "When the two beams line up, they make a pattern of stripes. Move the mirrors farther apart, and for a star with a real width, the stripes fade away. The distance where they vanish tells you how wide the star looks. For Betelgeuse, about zero point zero four seven arcseconds. That's like spotting the width of a coin from almost ninety kilometers away. It was the first time anyone measured the size of a star other than the Sun.",
  "vis": {"type": "interfero", "stage": 1, "head": "The stripes vanish → the star has a width", "angle": "0.047″ = a coin seen from ~88 km"}},
 {"say": "The trick still works today, only much bigger. The European Southern Observatory's Very Large Telescope Interferometer combines four telescopes in Chile. In twenty twenty four, it took the first close up image of a star in another galaxy.",
  "vis": {"type": "interfero", "stage": 2, "head": "Today: four telescopes combined (ESO VLTI)"}},

 # ---------- WAY 1: THE LINEUP ----------
 {"say": "So, way number one. The lineup. Here is the Sun. Next to it, R one three six a one, the most massive star we know, around two hundred times the Sun's mass. You'd expect it to be the biggest. It isn't. It's only a few dozen times wider than the Sun.",
  "vis": {"type": "lineup", "stage": 1}},
 {"say": "Now Betelgeuse, the red shoulder of Orion, a star you can see tonight with your own eyes. A 2020 study puts it at about seven hundred and fifty times the radius of the Sun. Then V Y Canis Majoris, measured at around fourteen hundred times. And finally W O H G sixty four, in the Large Magellanic Cloud, which the European Southern Observatory describes as about two thousand times the size of the Sun. At this scale, the Sun is a dot you can barely see.",
  "vis": {"type": "lineup", "stage": 2}},

 # ---------- WAY 2: THE SOLAR-SYSTEM TEST ----------
 {"say": "Way number two. Drop them into our solar system. Betelgeuse, placed where the Sun is, would swallow Mercury, Venus, Earth, and Mars, with its surface out in the asteroid belt.",
  "vis": {"type": "engulf", "r_au": 3.55, "head": "Betelgeuse in the Sun's place", "sub": "≈ 750 × the Sun's radius"}},
 {"say": "V Y Canis Majoris goes further. NASA says it would reach out between the orbits of Jupiter and Saturn. Jupiter would be orbiting inside the star. From here on, let's use one round giant for our tests. A star fifteen hundred times wider than the Sun, the size of the record holders.",
  "vis": {"type": "engulf", "r_au": 6.98, "head": "A 1,500× star in the Sun's place", "sub": "surface between Jupiter and Saturn"}},

 # ---------- WAY 3: THE FLIGHT ----------
 {"say": "Way number three. Take a passenger jet, cruising at nine hundred kilometers an hour, and fly it once around the Sun's equator without stopping. By our calculation, that trip takes about two hundred and two days. Seven months in a plane, just to go around our star once.",
  "vis": {"type": "flight", "mult": 1, "head": "Around the Sun by jet", "res": "≈ 202 days"}},
 {"say": "Now fly around the giant. Same jet, same speed. About eight hundred and thirty years. If a flight had taken off when the first universities were opening in medieval Europe, it would still be in the air today, and it wouldn't have landed yet.",
  "vis": {"type": "flight", "mult": 1500, "head": "Around the giant by jet", "res": "≈ 830 years"}},

 # ---------- RE-ENGAGE 1: THE PARADOX ----------  # REENGAJE (~3:00)
 {"say": "But here's the paradox. A star that big must be unimaginably heavy, right? Not really. Our giant has maybe twenty times the mass of the Sun, spread over a volume billions of times larger. Do the math, and its average density is about a hundred and fifty thousand times thinner than the air at sea level.",
  "vis": {"type": "density", "ratio": 150000, "head": "Average density of the giant"}},
 {"say": "Astronomers sometimes call the outer layers of a red supergiant a red hot vacuum. Almost all of its mass is packed into a small, dense core, and around it floats a vast, glowing envelope of thin gas, puffing out like steam. That's why these stars are so fragile. Their outer layers are barely held by gravity, and they leak away into space.",
  "vis": {"type": "density", "ratio": 150000, "core": True, "head": "A tiny dense core, a vast thin envelope"}},

 # ---------- WAY 4: THE JAR ----------
 {"say": "Way number four. The jar. How many Suns would fit inside our giant? Volume grows with the cube of the width. Fifteen hundred, times fifteen hundred, times fifteen hundred. About three point four billion Suns.",
  "vis": {"type": "bignumber", "from": 0, "to": 3375000000, "suffix": "", "col": RSG, "caption": "Suns that would fit inside a star 1,500 times wider"}},
 {"say": "And since one point three million Earths fit in each Sun, that's around four quadrillion Earths. A four followed by fifteen zeros. All inside one star.",
  "vis": {"type": "bignumber", "from": 0, "to": 4.4, "decimals": 1, "suffix": " quadrillion", "col": MINT, "caption": "Earths inside the giant · 4,400,000,000,000,000"}},

 # ---------- WAY 5: THE BEAM OF LIGHT ----------  # REENGAJE 2 (~5:30)
 {"say": "Way number five, and the biggest scale of all. Light. The fastest thing there is. A beam of light crosses the Sun, from one side to the other, in about four and a half seconds.",
  "vis": {"type": "flight", "mult": 1, "light": True, "head": "Light crossing the Sun", "res": "≈ 4.6 seconds"}},
 {"say": "Across our giant, that same beam needs almost two hours. Light could leave the Moon and reach Earth more than five thousand times in the time it takes to cross one star. Two hours, at the fastest speed in the universe.",
  "vis": {"type": "flight", "mult": 1500, "light": True, "head": "Light crossing the giant", "res": "≈ 1.9 hours"}},

 # ---------- THE TWIST ----------
 {"say": "So which star is the largest, exactly? That answer just got complicated. In twenty twenty four, the image of W O H G sixty four showed something odd. The star was wrapped in an egg shaped cocoon of gas and dust, and it had been getting dimmer for a decade.",
  "vis": {"type": "lineup", "stage": 3, "caption": "WOH G64 · 160,000 light-years away · wrapped in a cocoon"}},
 {"say": "Then, in twenty twenty six, a team led from the National Observatory of Athens reported in Nature Astronomy that W O H G sixty four had heated up by more than a thousand degrees, and seems to have turned from a red supergiant into a yellow hypergiant. It may have shed part of its outer layers. One of the biggest stars we ever measured is changing while we watch.",
  "vis": {"type": "lineup", "stage": 4, "caption": "red supergiant → yellow hypergiant (Nature Astronomy, 2026)"}},

 # ---------- WHY NOT BIGGER ----------
 {"say": "That raises the real question. Why do the largest stars all stop around one or two thousand times the Sun? Why not ten thousand? In nineteen seventy nine, astronomers Roberta Humphreys and Kris Davidson noticed an invisible ceiling. Above a certain brightness, cool, bloated supergiants simply don't exist. It's now called the Humphreys Davidson limit.",
  "vis": {"type": "ceiling", "stage": 0}},
 {"say": "The likely reason? The heaviest stars shine so fiercely that their own light pushes their gas away. They blow off their outer layers before they can swell into red giants. A 2026 study from Armagh Observatory traced that ceiling to exactly this kind of runaway mass loss. So the most massive stars stay relatively compact, and the biggest stars are the medium heavyweights that puff up and let go.",
  "vis": {"type": "ceiling", "stage": 1}},

 # ---------- OUR SUN'S TURN ----------
 {"say": "And our Sun? It will have its own giant phase. In about five billion years, NASA says, it will run out of hydrogen in its core and swell into a red giant, big enough to engulf Mercury and Venus, and possibly Earth. A small red giant, compared to the monsters on this list. Big enough to swallow our world.",
  "vis": {"type": "engulf", "r_au": 1.0, "sun": True, "head": "The Sun, in about 5 billion years", "sub": "a red giant: Mercury, Venus… maybe Earth"}},

 # ---------- PAYOFF + NEXT ----------
 {"say": "So, the largest star versus the Sun. Two thousand times wider. Billions of Suns of space inside. Eight centuries to fly around it, two hours for light to cross it, and thinner than air. A giant made mostly of glowing almost-nothing. But you don't need a giant star for extreme physics. Our own planet is spinning right now, at about sixteen hundred and seventy kilometers an hour at the equator. So what would happen if Earth suddenly stopped? That's next.",
  "vis": {"type": "title", "title": "Next:\nWhat If Earth Stopped Spinning?", "sub": "COSMIC SCALE", "brand": False, "subcol": MINT}},
]

SOURCES = [
 "NASA Science, Sun: Facts (about 1.4 million km across; about 1.3 million Earths fit inside; an average star in size; red giant in about 5 billion years could engulf Mercury, Venus and possibly Earth)",
 "Michelson & Pease (1921), Astrophysical Journal 53: Measurement of the diameter of Alpha Orionis with the interferometer (Mount Wilson, December 1920; 0.047 arcseconds)",
 "ESO press release eso2417 (Nov 21, 2024), Ohnaka et al., A&A: first close-up image of a star outside our galaxy, WOH G64, about 2,000 times the Sun's size, 160,000 light-years, VLTI/GRAVITY, egg-shaped cocoon, dimming over the past decade",
 "Muñoz-Sanchez et al. (2026), Nature Astronomy (via Sci.News, March 2026): WOH G64 warmed by more than 1,000 °C and transitioned from red supergiant to yellow hypergiant",
 "NASA Hubble (March 2021): VY Canis Majoris would extend between the orbits of Jupiter and Saturn; 300,000 times brighter than the Sun",
 "Wittkowski et al. (2012), A&A: VY CMa radius about 1,420 solar radii",
 "Joyce et al. (2020), ApJ: Betelgeuse radius about 750 (764) solar radii",
 "NOIRLab / Gemini South (Aug 2022): R136a1, 170–230 solar masses",
 "Humphreys & Davidson (1979), ApJ: upper luminosity limit for cool supergiants; Sabhahit & Vink (2026), arXiv:2607.28013, Armagh Observatory: origin of the maximum stellar size in enhanced mass loss",
 "Own calculations: volume ratio 1500³, light-crossing time, jet circumnavigation at 900 km/h, mean density for 20 solar masses vs sea-level air",
]
