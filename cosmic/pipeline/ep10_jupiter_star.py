# EP10 — What If Jupiter Became a Star?
# Structure NEW: "recipe" — hook (a red second sun over Earth's night) -> the recipe, 6 steps: 1) what Jupiter is (not a failed star) ->
# 2) add mass (it doesn't grow; 13 MJ brown dwarf; ~80 MJ red dwarf; smallest known star is Saturn-size) -> 3) where's the mass? (rest of the
# solar system = 0.4 MJ) -> 4) the new sky (≈ full Moon, red point, < 0.001 °C warming) -> 5) the Sun wobbles (barycentre almost at Mercury's
# orbit; binary star) -> 6) planets (stable to ~2 AU) -> RE-ENGAGE: the moons get swallowed -> TWIST: it would outlive the Sun -> EP11.
# Palette Jupiter ochre / ember red / lime. New scenes: massdial, sizeup, massbudget, twosuns, barywobble, moonfall.
# Own calculations (Python): 80 MJ = 0.076 Msun; barycentre 5.2 AU × 0.076/1.076 = 0.37 AU (Mercury 0.39 AU); today 1.07 R_sun from centre;
# period 11.86/sqrt(1.076) = 11.4 yr. Luminosity 1e-4 L_sun at 4.2 AU -> flux 5.7e-6 of sunlight -> magnitude ≈ -13.6 (full Moon -12.7);
# ΔT ≈ 255 K/4 × 5.7e-6 ≈ 0.0004 K. Moons, slow growth (L conserved, a ∝ 1/M): Io 5,300 km, Europa 8,400, Ganymede 13,400, Callisto 23,500 km
# vs star radius ≈ 60,000 km; instant growth -> periapsis a(1/80)/(2-1/80): Callisto 11,800 km (inside too).
# Holman & Wiegert (1999) critical S-type orbit for mu = 0.071, e = 0.049: 0.41 × 5.2 AU ≈ 2.1 AU. Other planets: 129 Earth masses = 0.41 MJ.
TITLE = "What If Jupiter Became a Star?"
OCH = [232, 176, 106]
EMB = [255, 92, 56]
LIME = [190, 240, 110]

SCENES = [
 # ---------- HOOK ----------
 {"say": "Tonight, a second sun rises over Earth. It's tiny, blood red, and bright enough to cast shadows at midnight. That's Jupiter, if Jupiter became a star. To make it happen, we'd need eighty times its mass. And the strangest part? After all that, it would barely get any bigger.",
  "vis": {"type": "twosuns", "head": "A second sun"}},
 {"say": "So today, we build that star like a recipe. Six steps. We turn up the mass, watch what changes, and find out what happens to Earth, to the Sun, and to Jupiter's moons. Some of it works out fine. Some of it really doesn't.",
  "vis": {"type": "massdial", "m0": 1, "m1": 80, "speed": 0.8, "head": "The recipe: add mass"}},
 {"say": "What If Jupiter Became a Star?",
  "vis": {"type": "title", "title": "What If Jupiter\nBecame a Star?", "sub": "COSMIC SCALE", "brand": True, "subcol": EMB}},

 # ---------- STEP 1 ----------
 {"say": "Step one. Know your ingredient. Jupiter is three hundred eighteen times the mass of Earth, more than twice all the other planets put together. It's made mostly of hydrogen and helium, the same stuff as the Sun. That's why it's often called a failed star.",
  "vis": {"type": "massbudget", "mode": "planets", "head": "Step 1: mass, measured in Earths", "caption": "Jupiter outweighs all the other planets combined, about 2.5 times over"}},
 {"say": "But that nickname is wrong. A star isn't defined by what it's made of. It's defined by what happens in its core. Gravity has to squeeze the center so hard that hydrogen nuclei fuse into helium, and that takes millions of degrees. Jupiter's core is estimated at about twenty four thousand degrees Celsius. Hot. But nowhere close. Jupiter never came near to being a star.",
  "vis": {"type": "compare", "left": ["JUPITER'S CORE", "≈ 24,000 °C", "no fusion", "a planet"], "right": ["A STAR'S CORE", "millions of °C", "hydrogen fuses", "it shines"], "cols": [OCH, EMB], "strike": False}},

 {"say": "Jupiter does glow a little on its own. It gives off about one point seven times more heat than it receives from the Sun. That's leftover heat from its formation, leaking out as the planet very slowly contracts. But a warm glow in infrared isn't fusion. A cooling ember isn't a fire.",
  "vis": {"type": "bignumber", "from": 1.0, "to": 1.7, "decimals": 1, "suffix": "×", "col": OCH, "caption": "heat Jupiter gives off vs heat it gets from the Sun (Pearl & Conrath, 1991)"}},

 # ---------- STEP 2 ----------
 {"say": "Step two. Add mass. A lot of it. Pile on Jupiter after Jupiter. And here's the first surprise: Jupiter doesn't swell up. Its own gravity crushes the new material tighter and tighter. Add a few Jupiters, and it barely grows. Add more, and it actually starts to shrink.",
  "vis": {"type": "massdial", "m0": 1, "m1": 12, "speed": 0.75, "head": "Step 2: add mass"}},
 {"say": "Somewhere around thirteen Jupiter masses, the core gets hot enough to fuse deuterium, a rare, heavy form of hydrogen. It glows for a while, then the deuterium runs out. Now it's a brown dwarf. Too big to be a planet. Too small to be a star.",
  "vis": {"type": "massdial", "m0": 12, "m1": 40, "speed": 0.6, "head": "13 Jupiters: a brown dwarf", "caption": "deuterium fusion starts near 13 Jupiter masses"}},
 {"say": "Brown dwarfs aren't just theory. The closest ones we know are a pair called Luhman sixteen, found in twenty thirteen with NASA's WISE space telescope, only about six and a half light years away. They're so dim that they hid in plain sight, right next door to the Sun, until an infrared telescope finally caught their faint glow.",
  "vis": {"type": "bignumber", "from": 0, "to": 6.5, "decimals": 1, "suffix": " ly", "col": [220, 120, 170], "caption": "Luhman 16 A and B: the closest known brown dwarfs (NASA WISE, 2013)"}},
 {"say": "Keep going. At around seventy five to eighty Jupiter masses, the core finally gets hot enough for ordinary hydrogen to fuse, and to keep fusing for good. That's the line. Cross it, and Jupiter becomes a red dwarf, the smallest kind of star there is.",
  "vis": {"type": "massdial", "m0": 40, "m1": 80, "speed": 0.7, "head": "About 80 Jupiters: a star", "caption": "sustained hydrogen fusion: roughly 75 to 80 Jupiter masses"}},
 {"say": "And its size? Smaller than when we started. In twenty seventeen, astronomers at the University of Cambridge measured one of the smallest stars known, EBLM J0555-57Ab. It packs about eighty five Jupiter masses into a ball about the size of Saturn. It circles a Sun like star once every eight days, and it was found when it passed in front of it, dimming its light. A real star that would fit inside Jupiter.",
  "vis": {"type": "sizeup", "caption": "EBLM J0555-57Ab: about 85 Jupiter masses, about Saturn's size (Cambridge, 2017)"}},

 # ---------- STEP 3 ----------
 {"say": "Step three. Find the ingredients. Where do we get seventy nine more Jupiters? Not here. Add up Saturn, Uranus, Neptune, every rocky planet, every moon and asteroid, and it comes to less than half a Jupiter. The rest would have to be brought in from outside the solar system. It's impossible, but let's say we did it.",
  "vis": {"type": "massbudget", "mode": "grid", "import": True, "head": "Step 3: about 80 Jupiters needed"}},

 # ---------- STEP 4 ----------
 {"say": "Step four. Look up. A star this small gives off only a few ten thousandths of the Sun's power, and most of that is invisible infrared. Even at its closest, it's more than six hundred million kilometers from us. By our rough calculation, it would shine about as bright as the full Moon, maybe a little brighter. But all of that light would come from a single red point, far too small to show a disc.",
  "vis": {"type": "twosuns", "head": "Step 4: the new sky", "caption": "our estimate: around magnitude −13.6, close to the full Moon (−12.7)"}},
 {"say": "For part of every year, it would hang in our night sky, washing the land in a dim red light. For other months, it would rise and set with the Sun, almost lost in daylight. And the heat? Practically none. By our estimate, it would warm Earth by less than a thousandth of a degree. No second summer. Just a strange new light.",
  "vis": {"type": "twosuns", "day": True, "meter": False, "head": "In daylight: almost invisible", "caption": "extra warming of Earth: less than 0.001 °C (our estimate)"}},

 # ---------- STEP 5 ----------
 {"say": "Step five. Watch the Sun. Gravity notices far more than our eyes do. Right now, the Sun and Jupiter circle a shared balance point that sits just outside the Sun's surface. Make Jupiter eighty times heavier, and that point moves out to about zero point three seven astronomical units, almost as far as Mercury's orbit. The Sun itself would swing around a loop nearly as big as Mercury's orbit, every eleven and a half years.",
  "vis": {"type": "barywobble", "caption": "barycentre: from just outside the Sun to ≈ 0.37 AU (our calculation)"}},
 {"say": "Seen from another star, we'd no longer look like a single Sun with planets. We'd be a binary star system. And that's not unusual at all. Surveys of nearby Sun like stars find that about forty four percent of them have at least one companion star. We'd just be joining the club.",
  "vis": {"type": "bignumber", "from": 0, "to": 44, "suffix": "%", "col": LIME, "caption": "of nearby Sun-like stars have a companion star (Raghavan et al. 2010)"}},

 {"say": "That wobble is exactly how astronomers find planets around other stars. They watch for stars that rock back and forth. Today, Jupiter tugs the Sun at about twelve meters per second. With eighty times the mass, by our calculation, the Sun would swing at close to one kilometer per second. Alien astronomers could spot it from light years away.",
  "vis": {"type": "bignumber", "from": 12, "to": 960, "suffix": " m/s", "col": LIME, "caption": "speed of the Sun's wobble: today vs with an 80-Jupiter companion (our calculation)"}},

 # ---------- STEP 6 ----------
 {"say": "Step six. Check the planets. A second star five point two astronomical units out reshapes everything. Using a standard stability rule for planets in binary star systems, our rough calculation says orbits can stay stable out to about two astronomical units from the Sun. Mercury, Venus, Earth and Mars could keep going. The asteroid belt gets stirred into chaos. And Saturn, Uranus and Neptune, orbiting just beyond a star, would be in real danger of being flung out of the solar system.",
  "vis": {"type": "barywobble", "mode": "zones", "caption": "stable zone ≈ 2.1 AU (Holman & Wiegert 1999 rule, our calculation)"}},

 # ---------- RE-ENGAGE: THE MOONS ----------
 {"say": "But the biggest losers are the closest ones. Io, Europa, Ganymede and Callisto have circled Jupiter for billions of years. Now the thing they orbit becomes eighty times heavier. What happens to them is the darkest part of this recipe.",
  "vis": {"type": "moonfall", "m0": 1, "m1": 3, "head": "Jupiter's four big moons"}},
 {"say": "If the mass arrived slowly, each moon's orbit would shrink in step, about eighty times smaller. By our calculation, Io would end up around five thousand kilometers from the center. Even Callisto, the farthest, would end up at about twenty four thousand. But the new star is about sixty thousand kilometers in radius. All four moons would end up inside it.",
  "vis": {"type": "moonfall", "m0": 3, "m1": 80, "head": "Mass grows, orbits shrink", "caption": "slow growth: orbit size × mass stays constant (our calculation)"}},
 {"say": "And if the mass arrived all at once, it's no better. Each moon would suddenly be moving far too slowly for its orbit, and it would fall into a long, narrow path that dives straight into the star. Either way, Jupiter's moons get swallowed. Europa's hidden ocean, one of the best places to search for life, would be gone.",
  "vis": {"type": "compare", "left": ["SLOW", "orbits shrink 80×", "Callisto: 23,500 km", "inside the star"], "right": ["ALL AT ONCE", "moons fall inward", "Callisto dips to 11,800 km", "inside the star"], "cols": [LIME, EMB], "strike": False}},

 {"say": "Science fiction got here first. In Arthur C. Clarke's novel twenty ten, Odyssey Two, Jupiter is ignited into a small new sun, and icy Europa thaws into a warm world where life can grow. It's a beautiful idea. But real physics runs the other way. Make Jupiter heavy enough to shine, and Europa isn't warmed. It's devoured.",
  "vis": {"type": "title", "title": "Fiction: Europa thaws.\nPhysics: Europa is swallowed.", "sub": "ARTHUR C. CLARKE, 2010: ODYSSEY TWO (1982)", "brand": False, "subcol": OCH}},

 # ---------- TWIST ----------
 {"say": "Now the twist. The Sun is about halfway through its roughly ten billion year life. A red dwarf this small sips its fuel so slowly that it could shine for trillions of years. Long after the Sun has swollen up and faded into a cooling white dwarf, the star that used to be Jupiter would still be glowing. The smallest star in the system would be the last one shining.",
  "vis": {"type": "compare", "left": ["THE SUN", "≈ 10 billion years", "then a white dwarf", "fading for good"], "right": ["JUPITER-STAR", "trillions of years", "barely changes", "the last one shining"], "cols": [[255, 194, 75], EMB], "strike": False}},

 # ---------- RECAP + NEXT ----------
 {"say": "So here's the full recipe. About eighty Jupiters of mass, brought in from outside. A red point in our sky about as bright as the full Moon. A wobbling Sun, a stable Earth, and outer planets in danger. And four famous moons, swallowed. Science fiction has ignited Jupiter before. Real physics says it stays a planet. And for Europa, that's very good news.",
  "vis": {"type": "bullets", "title": "The recipe", "items": ["about 80 Jupiter masses", "a red point as bright as the full Moon", "the Sun wobbles, Earth stays", "Saturn and beyond in danger", "four moons swallowed"], "col": EMB, "highlight": 4}},
 {"say": "Next time, we give Earth something only the giants have. What if Earth had rings like Saturn? What would they look like from your street, and what would they do to our nights? That's next.",
  "vis": {"type": "title", "title": "Next:\nWhat If Earth Had\nRings Like Saturn?", "sub": "COSMIC SCALE", "brand": False, "subcol": LIME}},
]

SOURCES = [
 "NASA Planetary Fact Sheets: Jupiter mass 1.898 × 10^27 kg (317.8 Earth masses, about 1/1,048 of the Sun), radius 71,492 km, distance 5.2 AU, orbit 11.86 years; masses of the other planets",
 "NASA Science, Jupiter: made mostly of hydrogen and helium; core temperature estimated at about 24,000 °C (43,000 °F)",
 "Sky at Night Magazine / Space.com: Jupiter is not a failed star; it would need roughly 75 to 80 times more mass to fuse hydrogen and become a red dwarf",
 "NASA / EarthSky, brown dwarfs: deuterium fusion begins near 13 Jupiter masses; brown dwarfs are about the size of Jupiter",
 "NASA / JPL WISE (2013), Luhman: Luhman 16 AB, the closest known brown dwarfs, about 6.5 light-years away",
 "University of Cambridge (2017), von Boetticher et al., Astronomy & Astrophysics: EBLM J0555-57Ab, about 85 Jupiter masses, radius about 0.84 Jupiter's, comparable to Saturn",
 "Raghavan et al. (2010), Astrophysical Journal Supplement: about 44% of nearby Sun-like stars have at least one stellar companion",
 "Holman & Wiegert (1999), Astronomical Journal: stability limit for planets orbiting one star of a binary",
 "Laughlin, Bodenheimer & Adams (1997), Astrophysical Journal, \"The End of the Main Sequence\": the smallest red dwarfs live for trillions of years; NASA: the Sun's lifetime is about 10 billion years",
 "Pearl & Conrath (1991), Journal of Geophysical Research (Voyager data): Jupiter emits about 1.67 times the energy it absorbs from the Sun",
 "Arthur C. Clarke, \"2010: Odyssey Two\" (1982): Jupiter ignited into the small sun Lucifer",
 "NASA Europa Clipper: Europa likely hides a global salt-water ocean beneath its ice",
 "Own calculations (Python): 80 Jupiter masses = 0.076 solar masses; Sun–Jupiter barycentre today about 1.07 solar radii from the Sun's centre, with 80× the mass about 0.37 AU (Mercury orbits at 0.39 AU), period about 11.4 years; assuming a luminosity of about 0.0001 Suns, at 4.2 AU it would reach about magnitude −13.6 (full Moon −12.7) and warm Earth by about 0.0004 °C; Galilean moon orbits shrinking as 1/mass (Io about 5,300 km, Callisto about 23,500 km from the centre) vs a star radius of about 60,000 km; with instant growth Callisto's closest approach about 11,800 km; Holman & Wiegert stability limit about 2.1 AU; reflex speed of the Sun today about 12.5 m/s, with an 80-Jupiter companion about 960 m/s; all other planets together about 0.4 Jupiter masses",
]
