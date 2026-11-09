# EP08 — What If the Moon Crashed Into Earth?
# Structure NEW: "countdown with two endings + twist" — hook (4 days 20 h, Moon 20× wider, breaks up 22 min before impact) -> what's falling
# -> FAST ENDING as a day-by-day countdown (fall to scale, sky view, tides 1/d³, the last hours, Roche limit, impact energy, Earth melts)
# -> RE-ENGAGE (~5:30): SLOW ENDING (spiral in -> rings; Phobos is doing it now) -> TWIST: it already happened (Theia) -> why it can't happen
# (3.8 cm/yr away) -> EP09.
# Palette moon silver / ultramarine / magma. New scenes: skyline, fallpath, tides, roche, theia.
# Own calculations (Python, numeric radial free fall from rest at 384,400 km, G(M_E+M_M)): impact after 4.82 days (≈ 4 d 20 h);
# 10,300 km fallen after day 1; 283,700 km away on day 3 (0.70° wide = 1.35×); 105,600 km at day 4.5 (2.35 km/s, 3.6× wider, tides ×48);
# Roche limit (fluid, 2.44 R_E (ρE/ρM)^1/3) ≈ 18,400 km, crossed at 4.80 d, 22 min before contact; there the Moon is 10.8° wide (≈ 21×),
# tides ×9,000; contact speed ≈ 9.9 km/s; impact energy (reduced mass) ≈ 3.5e30 J = 8.4 million × Chicxulub (4.2e23 J) = 1.7e13 × Tsar Bomba
# (50 Mt = 2.1e17 J) ≈ 960 × energy to heat + boil all oceans (1.4e21 kg: 3.7e27 J) ≈ 2.6 h of total solar output; Earth's gravitational
# binding energy (uniform sphere) 2.2e32 J ≈ 63× the impact. Mass ratio Earth/Moon = 81. Orbital speed ≈ 1.02 km/s.
TITLE = "What If the Moon Crashed Into Earth? You'd Have 4 Days"
SILVER = [222, 226, 236]
SEA = [46, 112, 255]
MAGMA = [255, 96, 44]

SCENES = [
 # ---------- HOOK ----------
 {"say": "If the Moon suddenly stopped in its orbit tonight, it would fall. And you would have about four days and twenty hours. For most of that time, the sky would look almost normal. Then, in the final hours, the Moon would swell to twenty times its usual width. And twenty two minutes before impact, it would start to tear apart.",
  "vis": {"type": "skyline", "deg0": 0.518, "deg1": 10.8, "speed": 0.85, "head": "Final hours", "cracked": 0.7}},
 {"say": "Today we run that countdown, day by day, and then minute by minute. After that, a slower and stranger way the Moon could come down, one that is happening right now around another planet. And finally a twist. This crash has already happened once. It is the reason we have a Moon at all.",
  "vis": {"type": "bullets", "title": "The countdown", "items": ["Day 0: the Moon stops", "Day 3: the sky still looks normal", "Day 4: the oceans move", "Minus 22 minutes: it cracks", "The slow ending, and the twist"], "col": MAGMA}},
 {"say": "What If the Moon Crashed Into Earth?",
  "vis": {"type": "title", "title": "What If the Moon\nCrashed Into Earth?", "sub": "COSMIC SCALE", "brand": True, "subcol": SEA}},

 # ---------- WHAT'S FALLING ----------
 {"say": "First, what exactly is falling. The Moon is about three thousand four hundred and seventy four kilometers wide, a bit more than a quarter of Earth's width. You would need about eighty one Moons to balance one Earth. It sits, on average, three hundred and eighty four thousand kilometers away. And here is the counterintuitive part. The Moon is already falling toward us, right now, all the time. It just moves sideways at about one kilometer per second, so it keeps missing.",
  "vis": {"type": "compare", "left": ["EARTH", "12,742 km wide", "81× the Moon's mass", ""], "right": ["THE MOON", "3,474 km wide", "384,400 km away", "≈ 1 km/s sideways"], "cols": [SEA, SILVER], "strike": False}},
 {"say": "Isaac Newton was the first to see it this way. The force that pulls an apple to the ground is the same force that holds the Moon. The Moon is a falling apple that is moving sideways fast enough to never land. So to make it crash, you don't need to push it. You only need to stop it.",
  "vis": {"type": "bullets", "title": "The Moon is always falling", "items": ["same gravity as a falling apple", "≈ 1 km/s sideways", "so it keeps missing Earth", "stop it, and it lands"], "col": SILVER, "highlight": 3}},

 # ---------- FAST ENDING: COUNTDOWN ----------
 {"say": "So let's take that sideways speed away. Day zero. The Moon stops dead, and Earth's gravity starts pulling it straight in. But this far out, the pull is gentle. After one full day, by our calculation, the Moon has fallen only about ten thousand kilometers. That is less than three percent of the way.",
  "vis": {"type": "fallpath", "d0": 0, "d1": 1.0, "head": "Day 0 to day 1, drawn to scale"}},
 {"say": "Day three. Look up, and you might not even notice. The Moon is still about two hundred and eighty thousand kilometers away. It looks around a third wider than usual. Odd, but not terrifying. The problem is that a falling object never falls at a steady speed. It keeps accelerating.",
  "vis": {"type": "skyline", "deg0": 0.518, "deg1": 0.70, "speed": 0.6, "head": "Day 3"}},
 {"say": "Day four. Now people notice. The Moon is about twice as wide as normal, and because it covers about four times as much sky, moonlit nights are about four times brighter. It is still more than a hundred and eighty thousand kilometers away. Nothing has broken yet. But there are now less than twenty hours left.",
  "vis": {"type": "skyline", "deg0": 0.70, "deg1": 1.07, "speed": 0.6, "head": "Day 4"}},
 {"say": "From here, the countdown speeds up. On day four, the Moon is about a hundred and eighty five thousand kilometers away. Half a day later, at day four and a half, it has crossed most of the gap. It is now a hundred and six thousand kilometers out, moving at more than two kilometers per second.",
  "vis": {"type": "fallpath", "d0": 3.0, "d1": 4.5, "head": "Day 3 to day 4.5"}},

 {"say": "Now the oceans notice. Tides come from the difference in the Moon's pull between the near side and the far side of Earth. That difference grows with the cube of the distance. Bring the Moon to half the distance, and the tidal pull is eight times stronger. At day four and a half, by our calculation, it is about fifty times today's. Coastal cities would see the sea pulled out and pushed back again and again as Earth turns beneath the Moon.",
  "vis": {"type": "tides", "m0": 1, "m1": 48, "head": "Day 4.5: the oceans notice", "caption": "tidal pull grows with 1 / distance³ (our calculation)"}},
 {"say": "And it isn't only water. Rock bends too. Jupiter's moon Io is squeezed this way by Jupiter's tides, and it is the most volcanically active world in the solar system. In the final hours, Earth's crust would be flexed the same way, with earthquakes and eruptions on a planetary scale. When the Moon reaches the danger line we'll see in a moment, the tidal pull is around nine thousand times today's.",
  "vis": {"type": "tides", "m0": 48, "m1": 9000, "head": "The final hours", "caption": "at the Roche limit: about 9,000× today's tidal pull (our calculation)"}},

 {"say": "Here is the view from a coastal town in those final hours. The Moon grows to twice its normal width. Then five times. Then ten. When it is twenty times wider than tonight's Moon, covering a patch of sky about as wide as your fist held at arm's length, it crosses an invisible line.",
  "vis": {"type": "skyline", "deg0": 1.0, "deg1": 10.8, "speed": 0.75, "head": "Final hours", "tide": 70, "cracked": 0.3}},
 {"say": "That line is called the Roche limit. Inside it, Earth's pull on the near side of the Moon is so much stronger than on the far side that it beats the Moon's own gravity. For a body like the Moon, it sits around eighteen thousand kilometers from Earth's center. Cross it, and the Moon begins to be pulled apart. But in this ending, there's no time. The Moon crosses the line only twenty two minutes before impact. It arrives stretched and cracked, but still mostly in one piece.",
  "vis": {"type": "roche", "mode": "fall", "caption": "Roche limit for a Moon-like body ≈ 18,400 km from Earth's center (our calculation)"}},
 {"say": "Now the last minutes, seen by someone standing right under it. Ten minutes before impact, the Moon is about thirty degrees wide, by our calculation. Five minutes out, forty five degrees. In the final minute, a cracked, glowing wall of rock fills half of the sky, falling at nearly ten kilometers per second. Nobody standing there would hear it coming. It would arrive faster than its own sound.",
  "vis": {"type": "skyline", "deg0": 16.7, "deg1": 97, "speed": 0.8, "head": "The last minutes", "tide": 120, "cracked": 1.0}},

 {"say": "Impact. The Moon hits at roughly ten kilometers per second. By our calculation, it releases about three and a half million trillion trillion joules. Numbers like that mean nothing, so let's put them on a ladder. The most powerful bomb ever tested, the Tsar Bomba, released about fifty megatons. The asteroid that ended the dinosaurs released around two million times more than that. Boiling every ocean on Earth would take nearly ten thousand dinosaur asteroids. And the Moon? About eight million dinosaur asteroids. Around a thousand times the energy needed to boil all the oceans. Roughly everything the Sun shines out, in every direction, for two and a half hours.",
  "vis": {"type": "ladder", "title": "Energy, times the biggest bomb ever", "max": 15, "items": [["Tsar Bomba", 0, 0, "#9AA4BC"], ["Dinosaur asteroid", 6.3, 6.3, "#FFC24B"], ["Boil all oceans", 10.2, 10.2, "#2E70FF"], ["Moon impact", 13.2, 13.2, "#FF602C"]], "notes": ["50 megatons", "≈ 2 million ×", "≈ 17 billion ×", "≈ 17 trillion ×"]}},
 {"say": "Would Earth be destroyed? As a planet, no. Pulling Earth completely apart would take more than sixty times the energy of the impact. But the surface would not survive. The crust would melt, the oceans would boil away, and the sky would fill with vaporized rock. Earth would become a glowing ball of magma, something it hasn't been for more than four billion years. And the Moon would simply be gone, mixed into Earth.",
  "vis": {"type": "bullets", "title": "After the impact", "items": ["Earth survives as a planet", "the crust melts", "the oceans boil away", "a sky of vaporized rock", "the Moon is gone"], "col": MAGMA, "highlight": 0}},

 # ---------- RE-ENGAGE: THE SLOW ENDING ----------  # REENGAJE
 {"say": "But that's the fast ending. There's a slower one, and it's much stranger. Imagine the Moon isn't stopped, but slowly dragged inward, spiraling down over a very long time. Now it reaches the Roche limit gently. And it never hits Earth. Not as a Moon.",
  "vis": {"type": "compare", "left": ["FAST ENDING", "the Moon stops", "falls in 4 days 20 hours", "one giant impact"], "right": ["SLOW ENDING", "the Moon spirals in", "torn apart by tides", "a ring around Earth"], "cols": [MAGMA, SILVER], "strike": False}},
 {"say": "Tides pull it apart into a cloud of rubble, and that rubble spreads along its orbit. Earth gets rings, like Saturn. Some of the debris would rain down as meteors, but a ring could stay for a very long time. Science fiction? It's happening right now, at Mars. Its moon Phobos is spiraling inward by about two meters every century. In roughly thirty to fifty million years, Mars is expected to tear it apart, and Mars will have a ring.",
  "vis": {"type": "roche", "mode": "ring", "big": "Earth gets rings", "sub": "the slow ending", "caption": "Mars's moon Phobos: ≈ 2 m closer per century, expected to break into a ring"}},

 # ---------- TWIST ----------
 {"say": "Now the twist. A crash between Earth and the Moon? In a way, it already happened. About four and a half billion years ago, a world roughly the size of Mars, nicknamed Theia, slammed into the young Earth. Molten rock was thrown into orbit, and that debris gathered into a new body. Our Moon. Simulations run by NASA and Durham University even suggest it may have formed in just a few hours. The Moon didn't come to crash into us. It was born from a crash.",
  "vis": {"type": "theia", "head": "About 4.5 billion years ago", "caption": "giant impact hypothesis · NASA Ames / Durham University simulations (2022)"}},
 {"say": "The evidence is in the rocks the Apollo astronauts brought back. Moon rocks have almost exactly the same mix of oxygen isotopes as rocks on Earth, a chemical fingerprint that is different on Mars and on most meteorites. The Moon is made largely of the same stuff as Earth. Exactly what you would expect if it was splashed out of Earth in a giant collision.",
  "vis": {"type": "bullets", "title": "The fingerprint in Apollo rocks", "items": ["Moon rocks ≈ Earth rocks (oxygen isotopes)", "Mars and most meteorites differ", "the Moon came largely from Earth's material", "splashed out by a giant impact"], "col": SEA, "highlight": 3}},

 # ---------- REALITY ----------
 {"say": "So could the Moon ever fall back? No. It's moving the other way. Since the Apollo missions, scientists have been firing lasers at mirrors left on the lunar surface and timing the reflections. The Moon is drifting away by about three point eight centimeters every year, roughly as fast as your fingernails grow. The tides it raises on Earth are slowly nudging it outward. And the same tides act as a brake on Earth's spin, so our days are getting longer by around two milliseconds every century.",
  "vis": {"type": "bignumber", "from": 0, "to": 3.8, "decimals": 1, "suffix": " cm / year", "col": SILVER, "caption": "the Moon is moving AWAY (Apollo laser reflectors)"}},

 # ---------- PAYOFF + NEXT ----------
 {"say": "So the Moon won't crash. It was born in a collision, it would need four days and twenty hours to fall, and instead it's leaving us, one fingernail at a time. Next time, a question that sounds simple and isn't. If there are billions of stars out there, why is space black? That's next.",
  "vis": {"type": "title", "title": "Next:\nWhy Is Space Black If There\nAre Billions of Stars?", "sub": "COSMIC SCALE", "brand": False, "subcol": SEA}},
]

SOURCES = [
 "NASA Moon fact sheet (NSSDCA): mass 7.346 × 10^22 kg, equatorial radius 1,738 km (diameter about 3,474 km), mean distance 384,400 km, mean orbital speed 1.022 km/s; Earth mass 5.972 × 10^24 kg, radius 6,371 km",
 "NASA Science, Moon: the Moon is moving away from Earth by about 3.8 cm (1.5 inches) per year, measured with Apollo laser retroreflectors",
 "NASA Science / Lunar and Planetary Institute: Apollo samples have oxygen isotope ratios nearly identical to Earth's, unlike Mars and most meteorites (evidence for the giant impact)",
 "Tidal braking: Earth's day lengthens by roughly 2 milliseconds per century (lunar laser ranging and historical eclipse records)",
 "Speed of sound in air about 0.34 km/s",
 "NASA Science, Io: the most volcanically active world in the solar system, heated by tidal flexing",
 "Black & Mittal (2015), Nature Geoscience, \"The demise of Phobos and development of a Martian ring system\"; NASA Goddard (2015): Phobos falls about 2 m per century and is expected to break up in about 30 to 50 million years",
 "NASA Ames / Durham University, Kegerreis et al. (2022), The Astrophysical Journal Letters: the Moon may have formed within hours of a giant impact; giant impact hypothesis (Theia, roughly Mars-sized, about 4.5 billion years ago)",
 "Chicxulub impact energy about 100 million megatons of TNT (about 4.2 × 10^23 J); Tsar Bomba (1961) about 50 megatons",
 "Own calculations (Python): numeric free fall from rest at 384,400 km → impact after 4.82 days (about 4 days 20 hours); 10,300 km fallen after one day; 283,700 km on day 3; 105,600 km and 2.35 km/s at day 4.5; fluid Roche limit ≈ 18,400 km, crossed 22 minutes before contact, where the Moon would appear about 10.8° wide (≈ 21× today); tidal pull ∝ 1/d³ (×48 at day 4.5, ×9,000 at the Roche limit); impact speed ≈ 9.9 km/s; seen from directly below: ≈ 29° wide 10 minutes before impact, ≈ 46° at 5 minutes, ≈ 97° in the final minute; energy ≈ 3.5 × 10^30 J ≈ 8 million Chicxulubs ≈ 960× the energy to heat and boil all oceans (1.4 × 10^21 kg) ≈ 2.6 hours of the Sun's total output (3.83 × 10^26 W); Earth's gravitational binding energy ≈ 2.2 × 10^32 J (about 63× the impact)",
]
