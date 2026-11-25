# EP19 — What If Earth Had a Second Moon?
# Structure NEW: "five parking spots" — we try to park a twin of our Moon (same size, same mass) at five distances from Earth, closest to
# farthest. Every chapter opens on a parking map (slotmap: square-root distance strip Earth -> 1.5 million km with the Roche limit,
# geostationary orbit, the Moon, the stability edge and Earth's Hill sphere) and ends with a verdict stamp. The twin at the Moon's own
# Trojan point is the chapter that may have really happened (Jutzi & Asphaug 2011). Twist: Earth catches tiny second moons right now.
# Keeps EP18's promise (what if Earth had a second Moon?). Different from EP08 (one Moon falling) and EP11 (rings): here the question is
# WHERE a moon can live, and each spot changes the sky, the tides and the day.
# Palette: moonlight lilac / tide aqua / companion amber on deep indigo.
# New scenes: slotmap, twinsky, tidechart, trojan, splat, sunsteal, tangle.
# Own calculations (Python; GM_Earth 3.986e14, Moon radius 1,737.4 km, mean distance 384,400 km, angular size 0.518°):
#   15,000 km < fluid Roche limit 2.44 × 6,371 × (5,514/3,344)^(1/3) = 18,400 km.
#   30,000 km: orbit 14.3 h (faster than Earth spins: rises in the west, every ~35 h), 6.6° wide = 12.8× the Moon, tidal pull (384,400/30,000)³ = 2,100×.
#   100,000 km: orbit 3.6 days, 2.0° wide = 3.8× the Moon (3.75 Suns), full-moon light (3.844)² = 15×, tidal pull 3.844³ = 57×;
#     rough estimate with today's tidal friction: Earth's spin-down torque ∝ M²/a⁶ -> 3.844⁶ ≈ 3,200× -> ~7 s per century instead of ~2.3 ms.
#   Twin at L4 (60° ahead): tidal bulge pattern goes as cos 2θ -> |1 + e^(i·120°)| = 1 -> the combined tide has the SAME height as one Moon,
#     with the peak 30° east of the Moon's direction = about 2 hours LATER; Routh's criterion 27(m1m2+m2m3+m3m1) < (m1+m2+m3)²: 0.668 < 1.050 -> stable;
#     when one is full the other is 120° from the Sun, 75% lit.
#   1,000,000 km: orbit 114 days; Earth's Hill radius 1.50 million km; prograde orbits stay only inside ≈ 0.49 R_H ≈ 730,000 km (Domingos et al. 2006).
# EP19 promises EP20: shrink the universe until the Sun is a grain of sand, and walk to the edge.
TITLE = "What If Earth Had a Second Moon?"
LIL = [200, 190, 255]
AQUA = [90, 220, 210]
AMB = [255, 180, 90]
RED19 = [255, 105, 95]

SCENES = [
 # ---------- HOOK ----------
 {"say": "Picture two Moons tonight. Ours, and a twin. Here's the strange part. Two Moons would not give you bigger tides. Park the twin in the right spot, and the tides stay exactly the same.",
  "vis": {"type": "twinsky", "km2": 384400, "lead": 60, "head": "TWO MOONS", "sub": "same tides as one?"}},
 {"say": "But park it in the wrong spot, and it rips itself apart, or drowns our coasts, or simply flies away. Today we try five parking spots, and find out which ones keep a second Moon.",
  "vis": {"type": "title", "title": "What If Earth Had\na Second Moon?", "sub": "COSMIC SCALE", "brand": True, "subcol": LIL}},
 {"say": "The rules. Our new Moon is an exact twin of the one we have. Three thousand four hundred and seventy four kilometers wide, with the same mass. The only thing we choose is where it goes.",
  "vis": {"type": "compare", "left": ["THE MOON", "3,474 km wide", "384,400 km away", "1 orbit: 27.3 days"], "right": ["THE TWIN", "3,474 km wide", "same mass", "distance: our choice"], "cols": [LIL, AMB], "strike": False}},
 {"say": "Here's the parking lot. Earth at the left, our Moon in the middle, and the edge of Earth's gravity a million and a half kilometers out. The scale is squeezed so everything fits. Five spots. Let's start close.",
  "vis": {"type": "slotmap", "km": 0, "n": 0, "title": "THE PARKING LOT", "sub": "square-root scale · Earth -> 1.5 million km"}},

 # ---------- SPOT 1: 15,000 km ----------
 {"say": "Spot one. Fifteen thousand kilometers from Earth's center. That's only about nine thousand kilometers above the ground. Closer than the satellites that bring you TV. For comparison, the International Space Station flies about four hundred kilometers up.",
  "vis": {"type": "slotmap", "km": 15000, "n": 1, "title": "SPOT 1 · 15,000 km", "sub": "about 8,600 km above the ground"}},
 {"say": "It doesn't survive the trip. Earth's gravity pulls harder on the near side of the Moon than on the far side. Inside about eighteen thousand kilometers, that difference wins. It's called the Roche limit, and the twin is torn into pieces.",
  "vis": {"type": "splat", "mode": "shred"}},
 {"say": "The pieces spread around the planet, and Earth ends up with rings like Saturn. Beautiful, but it's not a Moon anymore. Verdict: torn apart.",
  "vis": {"type": "slotmap", "km": 15000, "n": 1, "title": "SPOT 1 · 15,000 km", "stamp": "TORN APART", "scol": RED19}},

 # ---------- SPOT 2: 30,000 km ----------
 {"say": "Spot two. Thirty thousand kilometers. Just outside the danger line. And the sky goes wild. The twin would look almost thirteen times wider than our Moon. Hold three fingers out at arm's length. It's about that big.",
  "vis": {"type": "twinsky", "km2": 30000, "lead": 25, "head": "SPOT 2 · 30,000 km", "sub": "12.8× wider than the Moon"}},
 {"say": "And it moves the wrong way. It circles Earth in just over fourteen hours, faster than the planet turns. So it rises in the west and sets in the east, roughly every day and a half. Mars has a moon that does exactly this. Phobos.",
  "vis": {"type": "slotmap", "km": 30000, "n": 2, "title": "SPOT 2 · 30,000 km", "sub": "1 orbit = 14.3 hours · rises in the west", "drift": "in"}},
 {"say": "The tides are the real problem. Tidal pull grows fast as a moon gets closer. Cut the distance by thirteen, and the pull jumps more than two thousand times.",
  "vis": {"type": "tidechart", "ratio": 2104, "lead": 0, "period2": 17.7, "head": "Tidal pull: 2,100× the Moon's", "mode": "bar"}},
 {"say": "And it can't stay. Below about forty two thousand kilometers, a moon orbits faster than its planet spins, and the tides it raises drag it down. Phobos is falling toward Mars about one point eight meters every century. Our twin would spiral in the same way, until it reached spot one, and shattered. Verdict: doomed.",
  "vis": {"type": "slotmap", "km": 30000, "n": 2, "title": "SPOT 2 · 30,000 km", "stamp": "SPIRALS IN", "scol": RED19, "drift": "in"}},

 # ---------- SPOT 3: 100,000 km ----------
 {"say": "Spot three. One hundred thousand kilometers. About a quarter of the way to our Moon, and safely above that forty two thousand kilometer line. Here, it drifts outward instead, just like our Moon does today.",
  "vis": {"type": "slotmap", "km": 100000, "n": 3, "title": "SPOT 3 · 100,000 km", "sub": "outside geostationary orbit · drifts outward", "drift": "out"}},
 {"say": "Now the sky is gorgeous. Two Moons, one of them almost four times wider than the other. At full phase, the big one would light the night about fifteen times brighter than our full Moon. You could read a book outside. And since it moves the same way Earth turns, it would crawl across the sky, taking about sixteen hours from rising to setting.",
  "vis": {"type": "twinsky", "km2": 100000, "lead": 40, "head": "SPOT 3 · 100,000 km", "sub": "3.8× wider · 15× the light"}},
 {"say": "It's nearly four times wider than the Sun, too. Whenever it passed in front of the Sun, it would cover it completely, with room to spare. Solar eclipses would last much longer than the few minutes we get today.",
  "vis": {"type": "compare", "left": ["THE SUN", "0.53° wide", "", ""], "right": ["THE TWIN", "1.99° wide from 100,000 km", "3.75 Suns across", "total eclipses, easily"], "cols": [AMB, LIL], "strike": False}},
 {"say": "And the tides. The twin pulls on the oceans fifty seven times harder than our Moon. And because it orbits in three and a half days, its tides fall out of step with the Moon's. Look at the harbor. Some days the two pulls add up. Some days they fight.",
  "vis": {"type": "tidechart", "ratio": 57, "lead": 0, "period2": 16.5, "head": "One harbor, three days", "mode": "curve"}},
 {"say": "There's a hidden cost. Tides act like a brake on Earth's spin. Today the Moon stretches our day by about two milliseconds every century. Our rough estimate, using today's tidal friction: the twin at spot three would brake Earth about three thousand times harder. Several seconds every century.",
  "vis": {"type": "bignumber", "from": 1, "to": 3200, "prefix": "≈ ", "suffix": "×", "col": AQUA, "caption": "how much harder the twin brakes Earth's spin (our rough estimate)"}},
 {"say": "Over millions of years, our days would grow long, fast. But the twin itself is safe. It slowly drifts away and stays with us. Verdict: it stays, and it changes everything.",
  "vis": {"type": "slotmap", "km": 100000, "n": 3, "title": "SPOT 3 · 100,000 km", "stamp": "IT STAYS", "scol": AQUA, "drift": "out"}},

 # ---------- SPOT 4: THE TWIN IN THE MOON'S ORBIT ----------
 {"say": "Spot four is the clever one. Same distance as our Moon, same orbit, but sixty degrees ahead of it. Earth, the Moon, and the twin form a perfect triangle. This is a special balance point, called L four.",
  "vis": {"type": "trojan", "mode": "triangle"}},
 {"say": "Is it stable? There's a test from eighteen seventy five, Routh's rule. It compares the masses. Earth is eighty one times heavier than the Moon, and that's enough. Our calculation says even a full sized twin would hold its place. It would only rock gently back and forth around the point. Jupiter already does this with more than ten thousand asteroids, the Trojans, sixty degrees ahead of it and behind it.",
  "vis": {"type": "trojan", "mode": "wobble"}},
 {"say": "And here is the hook we promised. With a twin sixty degrees ahead, the two tides overlap in a way that cancels the extra. Our calculation: the high tide is exactly as tall as it is today. Just about two hours later. Two Moons, same tides.",
  "vis": {"type": "tidechart", "ratio": 1, "lead": 60, "period2": 12.42, "head": "Twin 60° ahead: same height, 2 h later", "mode": "curve"}},
 {"say": "The sky would be odd, too. The two would never be full on the same night. When ours is full, the twin is only three quarters lit, a few days ahead in its phases.",
  "vis": {"type": "twinsky", "km2": 384400, "lead": 60, "phase": True, "head": "SPOT 4 · THE MOON'S ORBIT", "sub": "never both full"}},
 {"say": "Now the twist. This may have really happened. In twenty eleven, two scientists, Martin Jutzi and Erik Asphaug, suggested that the early Earth had a second, smaller moon, about twelve hundred kilometers wide, parked at exactly this kind of point.",
  "vis": {"type": "trojan", "mode": "companion"}},
 {"say": "As the Moon drifted away from Earth, the balance broke, and the companion slowly caught up. It hit the Moon at only two to three kilometers per second. Slow enough not to blast a crater. It splattered across one side, like a pancake.",
  "vis": {"type": "splat", "mode": "splat"}},
 {"say": "And that might explain a real mystery. The far side of the Moon, the side we never see, is covered in thick highlands, very different from the side facing us, with a much thicker crust. Maybe that's the scar of our lost second Moon. Verdict: stable, for a while.",
  "vis": {"type": "splat", "mode": "farside"}},

 # ---------- SPOT 5: 1,000,000 km ----------
 {"say": "Spot five. A million kilometers out, far beyond our Moon. Here the twin would take a hundred and fourteen days to go around once, and it would look smaller than our Moon, less than half as wide. Its tides would be about seventeen times weaker than the Moon's. Barely a ripple.",
  "vis": {"type": "slotmap", "km": 1000000, "n": 5, "title": "SPOT 5 · 1,000,000 km", "sub": "1 orbit = 114 days · 0.4× the Moon's width"}},
 {"say": "But out here, Earth isn't the only one pulling. The Sun pulls too. Earth's gravity rules out to about one and a half million kilometers, but orbits that go the same way as the Moon only stay safe inside about half of that.",
  "vis": {"type": "sunsteal", "phase": 0}},
 {"say": "So the Sun tugs, and the twin's path gets wilder, until it slips out of Earth's grip and goes around the Sun on its own. In our simple simulation, that takes about five months. Verdict: stolen by the Sun.",
  "vis": {"type": "sunsteal", "phase": 1}},

 # ---------- TWIST: WE ALREADY CATCH SECOND MOONS ----------
 {"say": "So only a few spots work. But here's the last surprise. Earth catches second Moons all the time. They're just tiny. In two thousand six, a rock about three meters wide was caught and looped around Earth for about a year before it escaped. Astronomers estimate that at almost any moment, at least one rock about a meter wide is looping around Earth, too small and dark for us to notice.",
  "vis": {"type": "tangle", "phase": 0}},
 {"say": "Another one, barely a meter wide, was spotted in twenty twenty, after years of looping around us. And in late twenty twenty four, a ten meter rock tagged along for two months. Its colors match Moon rock. It may be a piece of our own Moon, blasted off long ago.",
  "vis": {"type": "tangle", "phase": 1}},
 {"say": "And there's one more. Kamo'oalewa doesn't orbit Earth, but it circles the Sun right alongside us, year after year. A quasi moon. This year, China's Tianwen two probe reached it, to bring a piece of it home.",
  "vis": {"type": "tangle", "phase": 2}},

 # ---------- RECAP ----------
 {"say": "So, our five parking spots. Fifteen thousand kilometers, torn apart. Thirty thousand, it spirals in. A hundred thousand, it stays and floods the coasts. In the Moon's own orbit, same tides, and maybe history. A million kilometers, stolen by the Sun.",
  "vis": {"type": "bullets", "title": "Five parking spots", "items": ["15,000 km · torn apart", "30,000 km · spirals in", "100,000 km · stays, 57× tides", "L4, 60° ahead · same tides", "1,000,000 km · stolen by the Sun"], "col": LIL, "highlight": 3}},

 # ---------- NEXT ----------
 {"say": "Next time, we shrink the whole universe until the Sun is a grain of sand, and then we walk to the edge. Subscribe to Cosmic Scale so you don't miss it. And tell me in the comments, where would you park a second Moon?",
  "vis": {"type": "title", "title": "Next: shrink the universe\nto a grain of sand", "sub": "COSMIC SCALE", "subcol": AMB}},
]

SOURCES = ["NASA: the International Space Station orbits about 400 km above Earth",
           "NASA Moon Fact Sheet (NSSDC): equatorial radius 1,738.1 km (mean 1,737.4 km), mean distance 384,400 km, sidereal period 27.32 days, mass 0.0123 of Earth's (Earth is 81.3 times heavier)",
           "NASA Earth Fact Sheet: mean radius 6,371 km, density 5,514 kg per cubic metre; Moon density 3,344 kg per cubic metre; geostationary orbit radius 42,164 km",
           "Roche limit (fluid body): d = 2.44 × R × (planet density / moon density)^(1/3)",
           "NASA: Phobos orbits faster than Mars rotates, rises in the west and moves about 1.8 m closer to Mars every 100 years; it is expected to break up or crash within roughly 30 to 50 million years",
           "Lunar Laser Ranging (NASA/JPL): the Moon moves away from Earth about 3.8 cm per year; tidal friction lengthens the day by about 2.3 milliseconds per century (Stephenson et al. 2016 measured about 1.8 ms per century over 27 centuries)",
           "Routh (1875): the triangular Lagrange points are stable when 27(m1·m2 + m2·m3 + m3·m1) is less than (m1 + m2 + m3)²",
           "Jutzi & Asphaug (2011), Nature 476, 69–72, 'Forming the lunar farside highlands by accretion of a companion moon': a companion about 1,200 km wide at a Trojan point colliding at 2–3 km/s",
           "Domingos, Winter & Yokoyama (2006), MNRAS: prograde satellite orbits remain stable out to about 0.49 Hill radii",
           "Granvik, Vaubaillon & Jedicke (2012), Icarus: at any time at least one minimoon about 1 m across is likely orbiting Earth; NASA/JPL: more than 10,000 Jupiter Trojan asteroids are known, leading and trailing Jupiter by 60°",
           "Minimoons: 2006 RH120 (about 3 m, captured from mid-2006 to mid-2007); 2020 CD3 (about 1.2 m, Fedorets et al. 2020, captured for several years before 2020); 2024 PT5 (about 10 m, bound from September 29 to November 25, 2024; spectrum matches lunar rock, Kareta et al. 2025, ApJ Letters)",
           "Kamo'oalewa (2016 HO3): an Earth quasi-satellite; China's Tianwen-2 (launched May 2025) reached it in mid-2026 to collect a sample",
           "Own calculations (Python): 15,000 km is inside the 18,400 km Roche limit; at 30,000 km the orbit takes 14.3 h, the twin spans 6.6° (12.8 times the Moon's 0.518°) and its tidal pull is (384,400 / 30,000)³ = 2,100 times the Moon's; at 100,000 km: orbit 3.6 days, 1.99° wide (3.8 Moons, 3.75 Suns of 0.53°), full-phase light (3.844)² = 15 times, synodic period 33 h so about 16.5 h above the horizon, tidal pull 3.844³ = 57 times; spin-down torque scales as mass² / distance⁶, so 3.844⁶ ≈ 3,200 times today's (rough estimate assuming today's tidal friction); twin 60° ahead: the tidal bulge pattern repeats every 180°, so two equal pulls 120° apart in that pattern add to the same height as one (|1 + e^(i·120°)| = 1), with the peak 30° east of the Moon's direction, about 2 hours later; Routh test 0.668 is less than 1.050 for Earth, Moon and an equal twin; when one is full, the twin 60° ahead is 75% lit; at 1,000,000 km the orbit takes 114 days, the twin spans 0.20° and its tidal pull is (0.3844)³ = 1/17 of the Moon's; Earth's Hill radius = 149.6 million km × (Earth/Sun mass ÷ 3)^(1/3) = 1.50 million km, 0.49 of it ≈ 730,000 km; simple Hill-problem simulation (Earth + Sun, no Moon): a circular prograde orbit started at 1,000,000 km leaves 3 million km after about 149 days, one started at 400,000 km stays"]
