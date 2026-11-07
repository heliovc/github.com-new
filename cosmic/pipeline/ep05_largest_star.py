# EP05 — The Largest Star vs the Sun
# Structure NEW: "grow a star" ladder — the Sun -> Betelgeuse -> (how we measure / the distance catch) -> re-engage 1: thinner than air
# -> biggest isn't heaviest (R136a1) -> VY CMa -> why stars can't grow forever -> re-engage 2: Stephenson 2-18 (Saturn's orbit)
# -> the twist: WOH G64 shrank (Nature Astronomy 2025) -> our Sun's own red-giant future -> payoff -> EP06 (Earth stops spinning).
# Palette crimson / cream. New scenes: inflate, flight, measure, density, heavyvsbig, balance.
# Own calculations (Python, R_sun=696,000 km, 1 AU=1.496e8 km, jet 900 km/h): jet around the Sun 202 days; Betelgeuse 700 R_sun = 3.3 AU,
# jet 388 yr; VY CMa 1,420 = 6.6 AU, jet 787 yr, light around 5.75 h; Stephenson 2-18 2,150 = 10.0 AU, jet 1,192 yr, light 8.7 h, volume 9.9e9 Suns;
# Betelgeuse mean density (18 Msun, 700 R) = 7.4e-5 kg/m3 ≈ 16,000x thinner than air (1.2); R136a1 (200 Msun, 35 R) ≈ 6.6 kg/m3; Sun 1,410.
TITLE = "The Largest Star vs the Sun"
CRIM = [255, 77, 109]
CREAM = [255, 226, 154]
GOLDC = [255, 194, 75]
YEL = [255, 214, 90]

SCENES = [
 # ---------- HOOK ----------
 {"say": "Put one of the largest stars we know in place of the Sun, and Earth wouldn't orbit it. Earth would be deep inside it. So would Mars. So would Jupiter. A passenger jet flying around it nonstop would need more than a thousand years. And here's the strange part. Astronomers can't agree on which star holds the record. And one of the most famous giants may have just shrunk.",
  "vis": {"type": "inflate", "r0": 1, "r1": 1500, "maxau": 7.6, "name": "A record giant", "sub": "in place of our Sun", "head": "Earth would be INSIDE it"}},
 {"say": "So let's grow a star, step by step, from our Sun to the biggest monster ever measured. By the end, you'll know how we measure something that looks like a single dot, why a star can't grow forever, and why the biggest stars in the universe are, in a strange way, almost empty.",
  "vis": {"type": "bullets", "title": "Grow a star, step by step", "items": ["Our Sun", "Betelgeuse", "VY Canis Majoris", "The record holder…", "…and the giant that shrank"], "col": CRIM, "highlight": 4}},
 {"say": "The Largest Star versus the Sun.",
  "vis": {"type": "title", "title": "The Largest Star\nvs the Sun", "sub": "COSMIC SCALE", "brand": True, "subcol": CRIM}},

 # ---------- STEP 0: THE SUN ----------
 {"say": "Start with our Sun. It's about one point four million kilometers wide. A hundred and nine Earths, side by side. Hollow it out, and you could pour in about one point three million Earths. Now imagine a passenger jet cruising at nine hundred kilometers an hour, flying nonstop around it. By our calculation, one lap takes about two hundred days. Almost seven months. Hold on to that number. It's about to explode.",
  "vis": {"type": "flight", "name": "SUN", "col": GOLDC, "value": 202, "unit": "days", "notes": ["≈ 7 months for one lap", "109 Earths wide"]}},

 # ---------- STEP 1: BETELGEUSE ----------
 {"say": "Step one. Betelgeuse, the red shoulder of Orion, roughly five hundred and fifty light years away. You can see it tonight without a telescope. It's around seven hundred times wider than the Sun. Put it in the Sun's place, and its surface would reach past Mercury, past Venus, past Earth, past Mars, and out into the asteroid belt.",
  "vis": {"type": "inflate", "r0": 1, "r1": 700, "maxau": 5.6, "name": "Betelgeuse", "sub": "the red shoulder of Orion"}},
 {"say": "And in twenty twenty five, astronomers using the Gemini North telescope finally spotted something long suspected. A small companion star, circling Betelgeuse about four times farther out than Earth is from the Sun. That's barely outside Betelgeuse's swollen surface. The companion is doomed. Within about ten thousand years, it's expected to spiral in and be swallowed.",
  "vis": {"type": "inflate", "r0": 700, "r1": 700, "maxau": 5.6, "name": "Betelgeuse", "sub": "+ a doomed companion (Gemini North, 2025)", "companion": 4.0, "hide_swallowed": True, "caption": "companion ≈ 4× the Earth–Sun distance from Betelgeuse"}},
 {"say": "Now fly our jet around Betelgeuse. Not seven months anymore. About three hundred and ninety years. If you had taken off in the sixteen thirties, around the time Galileo was put on trial, you would only be landing about now.",
  "vis": {"type": "flight", "name": "BETELGEUSE", "col": CRIM, "value": 388, "unit": "years", "notes": ["take off in the 1630s…", "…land about now"]}},

 {"say": "Betelgeuse is also restless. In late twenty nineteen, it dimmed so much that people noticed it with the naked eye. Some wondered if it was about to explode. Hubble later showed what really happened: the star had blasted a huge chunk of its surface into space, and that material cooled into a dust cloud that blocked part of its light. Betelgeuse will explode one day, as a supernova, probably within the next hundred thousand years. When it does, it should shine in our sky bright enough to see in daylight, for weeks.",
  "vis": {"type": "bignumber", "from": 0, "to": 100000, "suffix": " yrs", "col": CRIM, "caption": "Betelgeuse will likely go supernova within ~100,000 years (NASA)"}},

 # ---------- HOW DO WE KNOW? ----------
 {"say": "But wait. Apart from the Sun, every star is just a point of light. So how do you measure the width of a dot? There are two main ways. The first is to link telescopes together. Combine the light from telescopes spread far apart, and they act like one giant mirror. That's how the European Southern Observatory's Very Large Telescope Interferometer has resolved the actual disks of giant stars. The second way is a formula. If you know how much light a star really gives off, and how hot its surface is, physics tells you how much surface it needs to shine like that. A cool, red star that's still blindingly bright has only one option. It has to be enormous.",
  "vis": {"type": "measure", "head": "How do you measure a dot?", "lines": ["1. Link telescopes together", "they act like one giant mirror", "2. Use brightness + temperature", "cool but bright = enormous"], "formula": True}},
 {"say": "There's a catch. Both methods depend on the distance. Get the distance wrong, and the size is wrong too. UY Scuti was once crowned the largest known star, at around seventeen hundred times the width of the Sun. Then the Gaia space telescope measured its distance more precisely, and the estimate dropped to roughly nine hundred. It lost almost half its width, on paper, almost overnight.",
  "vis": {"type": "inflate", "r0": 1700, "r1": 909, "maxau": 8.6, "name": "UY Scuti", "sub": "before vs after a better distance (Gaia)", "caption": "same star, new distance: the size estimate nearly halves"}},

 # ---------- RE-ENGAGE 1: THINNER THAN AIR ----------  # REENGAJE (~3:00)
 {"say": "So these stars are gigantic. Here's the paradox. They're also almost nothing. Betelgeuse holds roughly eighteen times the mass of the Sun. But spread that over a ball seven hundred times wider, and its average density comes out, by our calculation, about sixteen thousand times thinner than the air you're breathing right now. Its outer layers are thinner still. Fly a spaceship into Betelgeuse, and for a very long way, you'd be crossing a hot, glowing fog, thinner than any air on Earth.",
  "vis": {"type": "density", "title": "Average density", "items": [["Betelgeuse ≈ 0.00007", 7.4e-5, CRIM], ["Air 1.2", 1.2, [200, 210, 235]], ["R136a1 ≈ 7", 6.6, [170, 205, 255]], ["Water 1,000", 1000, [91, 141, 239]], ["Sun 1,410", 1410, GOLDC]], "verdict": "≈ 16,000× thinner than air"}},
 {"say": "Which means the biggest star and the heaviest star are not the same thing at all. The heaviest star known, R one thirty six a one, in a neighboring galaxy, packs somewhere around two hundred times the mass of the Sun. Yet it's only about thirty five times wider than the Sun. Next to Betelgeuse, it's a tiny blue-white marble. Big stars are puffed-up stars. Heavy stars are compact, blazing furnaces.",
  "vis": {"type": "heavyvsbig", "caption": "biggest ≠ heaviest"}},

 # ---------- STEP 2: VY CANIS MAJORIS ----------
 {"say": "Step two. VY Canis Majoris, about fourteen hundred times wider than the Sun. In our solar system, its surface would swallow the orbit of Jupiter and stop partway to Saturn. And it's falling apart. Hubble images show this star wrapped in huge arcs and knots of gas, thrown off in giant outbursts, as if it can barely hold itself together.",
  "vis": {"type": "inflate", "r0": 700, "r1": 1420, "maxau": 10.4, "name": "VY Canis Majoris", "sub": "≈ 1,420× the Sun's width"}},
 {"say": "Our jet? About seven hundred and ninety years for one lap. And light itself, the fastest thing there is, would need almost six hours to circle it once. Light gets from the Sun to Earth in about eight minutes.",
  "vis": {"type": "flight", "name": "VY CMa", "col": CRIM, "value": 787, "unit": "years", "notes": ["light: ≈ 5 h 45 min per lap", "Sun → Earth: 8 min"]}},

 # ---------- WHY NOT BIGGER? ----------
 {"say": "So why stop there? Why isn't there a star as big as the whole solar system? Because every star is a tug of war. Gravity squeezes inward. Heat and light from the core push outward. Make a cool supergiant bigger and brighter, and its outer layers get so loosely held that they start drifting off into space, carried away by powerful winds. Studies of large samples of red supergiants point to a ceiling, somewhere around fifteen hundred times the Sun's width. Past that, the star simply can't hold on to itself.",
  "vis": {"type": "balance", "head": "Why a star can't grow forever", "lines": ["bigger + brighter →", "outer layers drift away", "ceiling ≈ 1,500× the Sun"], "blow": True}},

 # ---------- RE-ENGAGE 2: THE BIGGEST SCALE ----------  # REENGAJE (~6:00)
 {"say": "And yet, one star seems to break the rule. Stephenson two eighteen, nearly nineteen thousand light years away, hidden behind dust in the constellation Scutum. Some estimates put it at around two thousand one hundred and fifty times the width of the Sun. Drop that into our solar system, and its surface would reach all the way to the orbit of Saturn. You could fit about ten billion Suns inside it.",
  "vis": {"type": "inflate", "r0": 1, "r1": 2150, "maxau": 10.6, "name": "Stephenson 2-18", "sub": "a contested estimate", "head": "Out to Saturn's orbit"}},
 {"say": "Our jet would need about twelve hundred years to fly around it. Light would need almost nine hours. But remember the catch. That size rests on a distance and a brightness that are both uncertain, and it breaks the ceiling we just talked about. Many astronomers suspect it's smaller. So the honest answer to which star is the largest? We're still measuring.",
  "vis": {"type": "flight", "name": "St 2-18", "col": CRIM, "value": 1192, "unit": "years", "notes": ["light: ≈ 8 h 40 min per lap", "…if the estimate holds"]}},

 # ---------- THE TWIST: THE GIANT THAT SHRANK ----------
 {"say": "And the most dramatic story played out almost in real time. In twenty twenty four, ESO's Very Large Telescope Interferometer captured the first close-up image of a star outside our galaxy. WOH G sixty four, in the Large Magellanic Cloud, about a hundred and sixty thousand light years away. A red supergiant, around fifteen hundred times wider than the Sun, wrapped in an egg-shaped cocoon of dust.",
  "vis": {"type": "inflate", "r0": 1, "r1": 1540, "maxau": 8.0, "name": "WOH G64", "sub": "first close-up of a star in another galaxy (ESO, 2024)"}},
 {"say": "Then, in twenty twenty five, a team led by Gonzalo Muñoz Sánchez looked back at more than thirty years of observations, and published a surprise in Nature Astronomy. WOH G sixty four has been changing. Its surface got more than a thousand degrees hotter. Its color shifted from red to yellow. And its estimated width dropped to around eight hundred times the Sun. One of the biggest stars we knew may be shrinking in front of our eyes. Some think it's a step toward its final explosion. Not everyone agrees, and that's what makes it so exciting to watch.",
  "vis": {"type": "inflate", "r0": 1540, "r1": 800, "col0": CRIM, "col1": YEL, "maxau": 8.0, "name": "WOH G64", "sub": "red → yellow, ≈ 1,500× → ≈ 800×", "head": "The giant that shrank", "caption": "Nature Astronomy, 2025 — over 30 years of observations"}},

 # ---------- CLOSER TO HOME ----------
 {"say": "And here's the twist closest to home. Our own Sun will become a red giant too. In about five billion years, it's expected to swell up and swallow Mercury and Venus, and possibly Earth. But even then, it will only reach a couple of hundred times its current width. Betelgeuse, today, is already about three times bigger than our Sun will ever get.",
  "vis": {"type": "inflate", "r0": 1, "r1": 210, "col0": GOLDC, "col1": [255, 120, 60], "maxau": 1.9, "name": "Our Sun", "sub": "in about 5 billion years"}},

 # ---------- PAYOFF + NEXT ----------
 {"say": "So, the largest star versus the Sun? Somewhere between eight hundred and two thousand times wider, depending on which giant you trust, and when you look. Big enough to swallow Jupiter. Thin enough to be emptier than air. And restless enough to change size within a human lifetime. But you don't need a giant star to feel the scale of the universe. Right now, the ground under your feet is spinning at up to sixteen hundred and seventy kilometers an hour. So what would happen if Earth suddenly stopped? That's next.",
  "vis": {"type": "title", "title": "Next:\nWhat If Earth Stopped Spinning?", "sub": "COSMIC SCALE", "brand": False, "subcol": CRIM}},
]

SOURCES = [
 "NOIRLab / Gemini North press release noirlab2523 (July 2025): Betelgeuse radius about 700 times the Sun; companion about 1.5 solar masses at about 4 times the Earth–Sun distance, expected to be destroyed within about 10,000 years",
 "ESO press release (Nov 2024): first close-up image of a star outside our galaxy, WOH G64, Large Magellanic Cloud, ~160,000 light-years, egg-shaped dust cocoon (VLTI GRAVITY)",
 "Muñoz-Sánchez et al. (2025), Nature Astronomy, via Sky & Telescope: WOH G64 from ~1,500 to ~800 solar radii, more than 1,000 °C hotter, red to yellow",
 "Wittkowski et al. (2012), A&A: VY Canis Majoris radius ~1,420 solar radii; NASA/Hubble (2021, Humphreys et al.): arcs and knots of ejected gas",
 "Crowther et al. (2010), MNRAS / University of Sheffield R136a1 FAQ: radius ~35 solar radii; Kalari et al. (2022), Gemini: current mass ~200 solar masses",
 "Stephenson 2-18: radius estimate ~2,150 solar radii (Davies et al. 2012 parameters), considered uncertain",
 "UY Scuti: earlier ~1,700 solar radii, revised to ~900 with Gaia distance",
 "Levesque et al. (2005), ApJ: empirical upper limit for red supergiant radii ~1,500 solar radii",
 "NASA / Hubble (Aug 2022, Dupree et al.): Betelgeuse Great Dimming caused by a surface mass ejection; supernova likely within 100,000 years",
 "NASA Science, Sun facts: red giant phase in about 5 billion years",
 "Own calculations (Python): jet laps at 900 km/h, light-travel times, mean densities",
]
