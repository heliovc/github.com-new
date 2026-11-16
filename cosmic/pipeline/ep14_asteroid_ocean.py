# EP14 — What If an Asteroid Hit the Ocean?
# Structure NEW: "drop test" — the same ocean, five rocks, each bigger than the last (18 m -> 140 m -> 250 m -> 1 km -> 10 km); every rock gets
# a chapter card on a log size ladder, then what really happens when it lands in water. Hook = the counterintuitive one: the 10 km rock is
# almost three times taller than the ocean is deep. Twist at the end: for most rocks, the sea is the safest place to be hit.
# Palette abyss teal / impact orange / foam white on deep navy. New scenes: oceancut (cross-section TO SCALE), sizeladder (log ladder with
# landmarks), wavering (local rings vs coastline | global rings over a globe), plume (steam column into the stratosphere | ozone + UV meter).
# Own calculations (Python): average ocean depth 3.682 km (NOAA) -> 10 km rock = 2.7x taller; at ~20 km/s it crosses 3.7 km of water in
# ~0.2 s; deep-water wave speed sqrt(g*h) at 3,682 m = 190 m/s = 684 km/h (airliner ~ 900 km/h); 71% of the surface is ocean.
TITLE = "What If an Asteroid Hit the Ocean?"
TEAL = [40, 205, 195]
IMPACT = [255, 128, 46]
FOAM = [222, 242, 255]

SCENES = [
 # ---------- HOOK ----------
 {"say": "The asteroid that killed the dinosaurs was about ten kilometers wide. The ocean, on average, is less than four kilometers deep. So if a rock like that hit the open sea, it would touch the seafloor while its back end was still sticking out of the water.",
  "vis": {"type": "oceancut", "d_m": 10000, "view_km": 16, "mode": "drop", "head": "10 km rock, 3.7 km of ocean", "label": "Chicxulub-size"}},
 {"say": "Seventy one percent of Earth is ocean. So most space rocks that reach us land in water. Today we run a drop test. Same ocean, five rocks, each one bigger than the last. And we'll find out where the water saves us, and where it makes things much, much worse.",
  "vis": {"type": "sizeladder", "n": 0}},
 {"say": "What If an Asteroid Hit the Ocean?",
  "vis": {"type": "title", "title": "What If an Asteroid\nHit the Ocean?", "sub": "COSMIC SCALE", "brand": True, "subcol": TEAL}},

 # ---------- ROCK 1: 18 m ----------
 {"say": "Rock one. Eighteen meters across. About the size of a five story building. This is the kind of rock that hits Earth's atmosphere every few decades.",
  "vis": {"type": "sizeladder", "n": 1}},
 {"say": "We know exactly what this one does, because it already happened. In February twenty thirteen, a rock about this size came in over Chelyabinsk, in Russia. It never reached the ground. Air pressure tore it apart about thirty kilometers up, releasing roughly four hundred forty kilotons of energy, thirty times the Hiroshima bomb.",
  "vis": {"type": "oceancut", "d_m": 18, "view_km": 40, "mode": "burst", "alt": 30, "head": "Rock 1: it never reaches the water", "label": "Chelyabinsk, 2013"}},
 {"say": "Over a city, that blast shattered windows across a whole region and injured about fifteen hundred people, most of them from flying glass. Over the open ocean, the same explosion would leave almost no trace. No crater, no tsunami. Just a flash and a boom that nobody hears. And since most of the planet is water, most rocks like this, statistically, explode where nobody is watching.",
  "vis": {"type": "compare", "left": ["OVER A CITY", "windows blown out", "about 1,500 injured", "Chelyabinsk, 2013"], "right": ["OVER THE OCEAN", "a flash, a boom", "no crater", "no tsunami"], "cols": [IMPACT, TEAL], "strike": False}},

 # ---------- ROCK 2: 140 m ----------
 {"say": "Rock two. A hundred and forty meters. Taller than the Statue of Liberty, and smaller than the Eiffel Tower.",
  "vis": {"type": "sizeladder", "n": 2}},
 {"say": "This size matters, because it's the line NASA drew. Rocks of a hundred forty meters and up are the ones Congress asked NASA to find. There are about twenty five thousand of them near Earth, and we've found only around forty percent. On land, NASA says, one of these could devastate an entire region.",
  "vis": {"type": "bignumber", "from": 0, "to": 40, "suffix": "%", "col": IMPACT, "caption": "share of the ~25,000 near-Earth asteroids over 140 m found so far (NASA)"}},
 {"say": "This one doesn't burn up. It punches straight through the air and into the sea, and for a moment, it opens a hole in the ocean, a crater made of water, several kilometers wide. Then the walls of that hole collapse, and the water rushes back in, collides in the middle, and shoots up in a tower of spray.",
  "vis": {"type": "oceancut", "d_m": 140, "view_km": 12, "mode": "crater", "cav_km": 5, "head": "Rock 2: a crater made of water", "cav_label": "a hole in the sea, for a few seconds", "caption": "cavity size illustrative"}},
 {"say": "And here's the surprise. You'd expect a giant tsunami. But in computer simulations at Los Alamos, the physicist Galen Gisler found that waves from impacts like this are short and steep. They break and fade in the open ocean, much faster than earthquake tsunamis do. The danger is local. If it lands within about a hundred kilometers of a coast, that coast is in serious trouble. Far out at sea, the waves die before they arrive.",
  "vis": {"type": "wavering", "mode": "local", "view_km": 300, "reach_km": 260, "coast_km": 100, "coast": "a coastline", "minutes": 20,
          "heights": [[0.0, "huge, near impact"], [0.45, "dropping fast"], [0.8, "breaking up"]], "head": "Impact waves fade fast", "caption": "illustration of Gisler's result (Los Alamos, AGU 2016); heights not to scale"}},

 # ---------- ROCK 3: 250 m ----------
 {"say": "Rock three. Two hundred fifty meters. Almost as tall as the Eiffel Tower.",
  "vis": {"type": "sizeladder", "n": 3}},
 {"say": "In Gisler's simulations, a rock this size hitting deep water throws up something you can't see in the movies. Steam. Up to two hundred fifty million tonnes of water, flashed into vapor and blasted high into the sky.",
  "vis": {"type": "plume", "mode": "vapor", "count": 250, "unit": "million tonnes of water", "top_km": 42, "head": "Rock 3: the ocean goes up"}},
 {"say": "Why does that matter? Because water vapor that reaches the stratosphere, above the weather, doesn't rain out. It can linger there for a long time, and it's a powerful greenhouse gas. Gisler's own conclusion was that the most significant effect of an ocean impact is not the wave. It's the steam, with possible effects on climate.",
  "vis": {"type": "compare", "left": ["THE FEAR", "a giant wave", "flooded coasts", ""], "right": ["THE REAL RISK", "steam in the stratosphere", "a stronger greenhouse", "possible climate effects"], "cols": [FOAM, TEAL], "strike": True}},

 # ---------- ROCK 4: 1 km ----------
 {"say": "Rock four. One kilometer. Now we're past anything a city could survive.",
  "vis": {"type": "sizeladder", "n": 4}},
 {"say": "When this one hits the sea, the steam carries something else with it. Salt. And sea salt is full of chlorine and bromine, the same kind of chemicals that tore the ozone hole over Antarctica.",
  "vis": {"type": "oceancut", "d_m": 1000, "view_km": 12, "mode": "crater", "cav_km": 18, "x": 980, "head": "Rock 4: salt in the sky", "cav_label": "steam, salt, chlorine, bromine", "caption": "cavity size illustrative"}},
 {"say": "In a twenty ten study, Elisabetta Pierazzo and her colleagues modeled a one kilometer asteroid landing in the ocean. The result was an ozone hole covering much of the planet, with more than seventy percent of the ozone gone at mid to high latitudes for over two years. The ultraviolet index, which the World Health Organization calls extreme at eleven, could reach fifty six. A number nobody has ever measured.",
  "vis": {"type": "plume", "mode": "ozone", "uv0": 10, "uv": 56, "head": "Ozone hole for the whole planet", "caption": "Pierazzo et al., Earth and Planetary Science Letters (2010), model results"}},
 {"say": "And this has happened. About two and a half million years ago, an asteroid somewhere around a kilometer wide fell into the Southern Ocean, off the coast of Chile, where the sea is four to five kilometers deep. It's called the Eltanin impact. Scientists found its debris in seafloor mud. But no clear crater was ever found. The deep water took the hit.",
  "vis": {"type": "oceancut", "d_m": 1000, "view_km": 9, "depth": 4.8, "mode": "drop", "seed": 7, "head": "Eltanin: the deep sea took the hit", "label": "Eltanin, ~2.5 million years ago"}},

 # ---------- ROCK 5: 10 km ----------
 {"say": "Rock five. Ten kilometers. Taller than Mount Everest.",
  "vis": {"type": "sizeladder", "n": 5}},
 {"say": "Sixty six million years ago, a rock this size struck what is now Mexico's Yucatan Peninsula, which was then covered by a shallow sea. At around twenty kilometers per second, it crossed the water in a fraction of a second. For a rock this big, the ocean is a puddle. It hit the seafloor and dug a crater about a hundred fifty kilometers wide. The water above it didn't slow it down. It just added to the chaos, because now a whole sea had been thrown out of its basin.",
  "vis": {"type": "oceancut", "d_m": 10000, "view_km": 16, "mode": "drop", "everest": True, "x": 760, "head": "Rock 5: the ocean is a puddle", "label": "Chicxulub, 66 million years ago"}},
 {"say": "Then the water came back. In twenty twenty two, a team led by Molly Range at the University of Michigan ran the first global simulation of that tsunami. Within about ten minutes, a wall of water around one and a half kilometers tall was rolling outward from the crater. That is almost twice the height of the Burj Khalifa, the tallest building in the world.",
  "vis": {"type": "wavering", "mode": "local", "view_km": 600, "reach_km": 520, "minutes": 10, "heights": [[0.15, "≈ 1.5 km tall"]], "head": "10 minutes after impact", "caption": "Range et al., AGU Advances (2022)"}},
 {"say": "Within two days, the waves had reached most of the world's coastlines. Their energy, the team estimated, was up to thirty thousand times larger than the twenty oh four Indian Ocean tsunami, one of the deadliest disasters in modern history.",
  "vis": {"type": "wavering", "mode": "global", "hours": 48, "tilt": 30, "heights": [[0.3, "up to 30,000×"]], "hlabel": "energy vs the 2004 tsunami", "head": "The whole planet rings", "caption": "Range et al., AGU Advances (2022)"}},
 {"say": "In deep water, a tsunami moves about as fast as a jet airliner. Our own calculation for an ocean three point seven kilometers deep gives close to seven hundred kilometers per hour. Across open ocean, the Chicxulub waves were still more than ten meters high as they approached the coasts of the North Atlantic.",
  "vis": {"type": "bignumber", "from": 0, "to": 684, "suffix": " km/h", "col": TEAL, "caption": "deep-water wave speed: square root of g × depth, at 3.7 km (our calculation)"}},
 {"say": "We may even have its footprints. In twenty twenty one, geologists found giant ripples buried one and a half kilometers under Louisiana. Each about sixteen meters tall, and six hundred meters apart. They think the tsunami's currents carved them into the old seafloor. Ripples on a beach are a few centimeters. These are the size of a five story building.",
  "vis": {"type": "compare", "left": ["BEACH RIPPLES", "a few cm tall", "a few cm apart", ""], "right": ["UNDER LOUISIANA", "≈ 16 m tall", "≈ 600 m apart", "1.5 km underground"], "cols": [FOAM, IMPACT], "strike": False}},

 # ---------- TWIST ----------
 {"say": "So does the ocean protect us? Here's the twist. For almost every rock on our list, yes. In twenty sixteen, NASA and NOAA brought tsunami experts together to settle exactly this question. Their conclusion: across all the rocks that could realistically hit us, the danger from tsunamis is substantially smaller than the danger from the same rocks hitting land.",
  "vis": {"type": "bullets", "title": "The verdict, rock by rock", "items": ["18 m: explodes in the air", "140 m: dangerous only near a coast", "250 m: steam into the stratosphere", "1 km: ozone hole, worldwide", "10 km: the ocean doesn't matter"], "col": TEAL}},
 {"say": "The sea absorbs the blast, the waves break and fade, and most of the planet's water is far from any city. The one exception is the rock that's too big for any ocean. And that's exactly the kind we're best at tracking. Every known asteroid over one kilometer that comes near Earth has been studied, and none of them is on a collision course for at least the next century.",
  "vis": {"type": "oceancut", "d_m": 140, "view_km": 12, "mode": "crater", "cav_km": 5, "x": 760, "head": "Far from shore, the sea takes the hit", "cav_label": "far from any coast", "caption": "illustration"}},
 {"say": "And we can now push back. In twenty twenty two, NASA flew its DART spacecraft into a small asteroid moon called Dimorphos on purpose. It shortened that moon's orbit by thirty two minutes. It was the first time humanity changed the motion of a natural object in space. And NEO Surveyor, a telescope built to hunt the rocks we haven't found yet, is scheduled to launch no earlier than September twenty twenty seven.",
  "vis": {"type": "bignumber", "from": 0, "to": 32, "suffix": " minutes", "col": IMPACT, "caption": "how much DART shortened Dimorphos's orbit (NASA, 2022)"}},

 # ---------- RECAP + NEXT ----------
 {"say": "So, five rocks, one ocean. The small ones never touch the water. The mid-sized ones are dangerous mostly near a coast, and they send steam and salt into the sky. And the giant one treats the deepest ocean like a puddle. Seventy one percent of our planet is water, and it is a better shield than it looks, until it suddenly isn't.",
  "vis": {"type": "sizeladder", "n": 6}},
 {"say": "Next time, a real milestone, happening this week. Voyager 1, launched in nineteen seventy seven, is about to become the first human-made object one full light-day from Earth. A radio message will need twenty four hours to reach it. We'll put that distance to scale. Subscribe to Cosmic Scale so you don't miss it. And tell me in the comments, which rock surprised you the most?",
  "vis": {"type": "title", "title": "Next: Voyager 1,\none light-day away", "sub": "COSMIC SCALE", "subcol": IMPACT}},
]

SOURCES = ["NOAA: the ocean covers about 71% of Earth's surface; average ocean depth about 3,682 m (Charette and Smith, Oceanography, 2010)",
           "NASA: the Chicxulub impactor was about 10 km wide and struck about 66 million years ago; crater about 150 km wide (Earth Impact Database)",
           "NASA: the Chelyabinsk meteor (15 February 2013) was about 18 m wide, broke up roughly 30 km up and released about 440 kilotons; about 1,500 people were injured, mostly by broken glass",
           "NASA Planetary Defense: about 25,000 near-Earth asteroids are 140 m or larger; roughly 40% have been found",
           "G. Gisler (Los Alamos National Laboratory), American Geophysical Union Fall Meeting 2016: impact waves dissipate quickly; dangerous near populated shores (about 100 km); a ~250 m impact can vaporize up to 250 megatons of water; 'the most significant effect of an impact into the ocean is the injection of water vapor into the stratosphere, with possible climate effects'",
           "E. Pierazzo et al., Earth and Planetary Science Letters (2010), 'Ozone perturbation from medium-size asteroid impacts in the ocean': 1 km ocean impact, more than 70% ozone loss at mid-high latitudes for over two years, UV index up to 56",
           "World Health Organization: UV index 11 and above is 'extreme'",
           "Eltanin impact: about 2.5 million years ago, Bellingshausen Sea (Southern Ocean), water 4 to 5 km deep, impactor roughly 1 km (estimates 1 to 4 km), no confirmed crater (Gersonde et al., Nature 1997)",
           "M. Range et al., AGU Advances (2022): Chicxulub tsunami about 1.5 km high within about 10 minutes; reached most coastlines within 48 hours; initial energy up to 30,000 times the 2004 Indian Ocean tsunami; open-ocean waves over 10 m approaching North Atlantic coasts",
           "G. Kinsland et al., Earth and Planetary Science Letters (2021): buried megaripples in Louisiana, about 1.5 km deep, average height 16 m and spacing 600 m (interpretation debated)",
           "NASA/NOAA Asteroid Generated Tsunami Workshop 2016 (Morrison and Venkatapathy, NASA TM 2017): the tsunami contribution to overall impact hazard is substantially less than that of land impacts",
           "NASA: DART (26 September 2022) shortened Dimorphos's 11 h 55 min orbit by 32 minutes; NEO Surveyor launch no earlier than September 2027 (JPL)",
           "NASA CNEOS: no known asteroid larger than 1 km has a significant chance of hitting Earth in the next 100 years",
           "Burj Khalifa: 828 m tall; 1.5 km / 828 m ≈ 1.8", "Own calculations: 10 / 3.682 ≈ 2.7; 3.7 km at 20 km/s ≈ 0.2 s; deep-water wave speed = √(9.81 m/s² × 3,682 m) ≈ 190 m/s ≈ 684 km/h; 440 kt ≈ 30 × Hiroshima (15 kt)"]
