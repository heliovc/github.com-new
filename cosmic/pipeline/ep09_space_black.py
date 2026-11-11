# EP09 — Why Is Space Black If There Are Billions of Stars? (Olbers' paradox)
# Structure NEW: "case file" — hook (the sky SHOULD blaze like the Sun's surface) -> 4 suspects on a board -> the forest argument, history,
# how bright -> suspect 1 (too faint: shells) cleared -> suspect 2 (dust: it would heat up and glow) cleared -> suspect 3 (the universe
# has an age: light-travel bubble; star lifetimes) GUILTY -> RE-ENGAGE: accomplice, suspect 4 (expansion stretches light) GUILTY ->
# TWIST: the sky is NOT black, the wall of light exists (CMB, 3,000 K -> 2.725 K, stretched ~1,100×, ~1% of old TV static) -> EP10.
# Palette starlight white / infrared crimson / microwave teal / indigo. New scenes: sightlines, blaze, suspects, shells, lightbubble, stretchwave.
# Own calculations (Python): Sun's disc = 6.79e-5 sr -> 2π / that ≈ 92,500 Suns tile the half-sky above you (185,000 the whole sky).
# Mean free path of a line of sight 1/(nσ), σ = π R_sun², n = N / volume of observable universe (radius 46.5 bn ly):
# N = 1e22..1e24 stars -> 2.5e22..2.5e24 ly, i.e. ~1e12..1e14 × 13.8 bn light-years ("trillions of times farther"; Harrison's "Darkness at Night").
# CMB stretch 3,000 K / 2.725 K ≈ 1,100.
TITLE = "Why Is Space Black If There Are Billions of Stars?"
STAR = [246, 244, 255]
IR = [255, 70, 110]
MW = [60, 230, 190]

SUS = [["1", "Far stars are too faint", "distance"], ["2", "Dust hides them", "clouds"], ["3", "The universe has a birthday", "time"], ["4", "Space is stretching", "expansion"]]

SCENES = [
 # ---------- HOOK ----------
 {"say": "This is what the night sky should look like. Not black. A wall of light, as bright as the surface of the Sun, in every direction, all night long. Our galaxy alone holds hundreds of billions of stars, and there are hundreds of billions of galaxies. So why is it dark?",
  "vis": {"type": "blaze", "speed": 0.55, "head": "The sky we should have"}},
 {"say": "That question bothered astronomers for four hundred years, and the answer turned out to be one of the strongest clues we have about how everything began. Today we treat it as a case file. Four suspects. One by one, we clear them, until we find who turned out the lights.",
  "vis": {"type": "suspects", "items": SUS, "title": "THE SUSPECTS"}},
 {"say": "Why Is Space Black If There Are Billions of Stars?",
  "vis": {"type": "title", "title": "Why Is Space Black\nIf There Are Billions of Stars?", "sub": "COSMIC SCALE", "brand": True, "subcol": MW}},

 # ---------- THE CASE ----------
 {"say": "First, why this is a real puzzle. Imagine standing in the middle of a huge forest. Close by, you can see gaps between the trees. But if the forest goes on far enough, every line of sight eventually ends on a trunk. Look any direction, and you see wood. Now swap the trees for stars. In an endless universe full of stars, every line of sight should end on the surface of a star.",
  "vis": {"type": "sightlines", "r0": 90, "r1": 1300, "head": "Lines of sight"}},
 {"say": "The puzzle carries the name of Heinrich Olbers, a German astronomer who wrote about it in eighteen twenty three. But Johannes Kepler was already using it in sixteen ten, to argue that the stars could not go on forever. Others took it on after him. A poet, and a famous physicist. We'll meet them both before the case is closed.",
  "vis": {"type": "bullets", "title": "A 400-year-old cold case", "items": ["1610: Johannes Kepler", "1823: Heinrich Olbers", "1848: a poet", "1901: Lord Kelvin", "1965: a surprise in the sky"], "col": STAR}},
 {"say": "How bright would that sky be? The Sun covers a tiny patch of sky, smaller than your fingertip at arm's length. By our calculation, it would take about ninety two thousand Suns, packed edge to edge, to tile the half of the sky above your head. Day and night, the sky would glow like the surface of a star, at more than five thousand degrees. Nothing on Earth could survive it.",
  "vis": {"type": "blaze", "speed": 0.7, "count": 92500, "head": "If every direction ended on a star"}},

 {"say": "One quick thing first, so we're asking the right question. Astronauts on the Moon saw a black sky even at noon, with the Sun blazing overhead. Our sky is blue in the daytime only because air scatters sunlight in every direction. Take the air away and the daytime sky goes black. But that doesn't solve anything. Air doesn't explain why the darkness between the stars is dark. Out there, there's no air at all, and the paradox is still waiting.",
  "vis": {"type": "sky", "moon": False, "start": 0.1, "speed": 0.45, "caption": "no air to scatter sunlight = a black sky, even at noon"}},

 # ---------- SUSPECT 1 ----------
 {"say": "Suspect number one. Faraway stars are simply too faint to matter. It sounds convincing. Move twice as far from a star, and it looks four times dimmer. Move ten times farther, and it's a hundred times dimmer.",
  "vis": {"type": "suspects", "items": SUS, "focus": 0, "title": "SUSPECT 1"}},
 {"say": "But picture the stars arranged in shells around you, like layers of an onion. A shell twice as far away has four times the area, so it holds four times as many stars. Each one is four times dimmer, but there are four times as many. Every shell sends you the same amount of light. Stack up endless shells, and the light keeps adding up, until nearer stars block the ones behind. Distance alone can't make the sky dark.",
  "vis": {"type": "shells", "n": 5, "caption": "more stars × dimmer stars = the same light from every shell"}},

 # ---------- SUSPECT 2 ----------
 {"say": "Suspect one, cleared. Suspect number two. Dust. Space really is full of gas and dust, and it really does block starlight. It's why the center of our own galaxy is hidden from our eyes. Olbers himself believed this was the answer.",
  "vis": {"type": "suspects", "items": SUS, "focus": 1, "cleared": [0], "new": [0], "title": "SUSPECT 2"}},
 {"say": "But it fails. Dust that soaks up light also soaks up energy. In an ageless universe drowning in starlight, the dust would keep warming until it was as hot as the stars themselves, and then it would glow just as brightly. A curtain can hide a fire for a while. Not forever. Suspect two, cleared.",
  "vis": {"type": "suspects", "items": SUS, "focus": 1, "cleared": [0, 1], "new": [1], "title": "SUSPECT 2"}},

 # ---------- SUSPECT 3 ----------
 {"say": "Suspect number three. The universe has a birthday. Light is fast, but it isn't instant. The light from the Andromeda Galaxy left it about two and a half million years ago. The farther you look, the further back in time you see.",
  "vis": {"type": "lightbubble", "y0": 0.0, "y1": 4.0, "head": "Time since the beginning"}},
 {"say": "And the universe is about thirteen point eight billion years old. So there's a limit. Past a certain distance, light simply hasn't had time to get here yet. We live inside a bubble of visible universe. Beyond its edge there may be countless stars, but their light is still on the way.",
  "vis": {"type": "lightbubble", "y0": 4.0, "y1": 13.8, "head": "Time since the beginning"}},
 {"say": "One detail makes the bubble even stranger. Because space kept stretching while that light was traveling, the most distant objects we can see are now about forty six billion light years away. That's the radius of the observable universe. Huge. And still, by the standards of this paradox, far too small.",
  "vis": {"type": "bignumber", "from": 13.8, "to": 46.5, "decimals": 1, "suffix": " billion ly", "col": MW, "caption": "radius of the observable universe today"}},
 {"say": "Now go back to the forest. How deep would it have to be for every line of sight to hit a star? By our rough calculation, deeper than a hundred billion trillion light years. That's trillions of times farther than light has traveled since the beginning. The forest is real. We can only see a small clearing in the middle of it.",
  "vis": {"type": "sightlines", "r0": 90, "r1": 1300, "limit": 300, "head": "What we can see", "caption": "a line of sight would need ≈ 10²³ light-years to hit a star (our rough calculation)"}},
 {"say": "And stars don't shine forever. A star like the Sun lasts about ten billion years. To fill the sky with light, stars would have to keep shining for unimaginably longer. Lord Kelvin worked this out in nineteen oh one. But the first to guess it was not a scientist. It was the poet Edgar Allan Poe, in eighteen forty eight. The dark sky is a clock. Suspect three, guilty.",
  "vis": {"type": "suspects", "items": SUS, "focus": 2, "cleared": [0, 1], "guilty": [2], "new": [2], "title": "SUSPECT 3"}},

 {"say": "Poe's words, from his essay Eureka, still hold up. He wrote that the only way to understand the empty gaps our telescopes find in countless directions would be to suppose the invisible background is so far away that no ray from it has yet been able to reach us at all. A poet, working from pure reasoning, more than eighty years before astronomers learned the universe had a beginning. He didn't have the numbers. But he had the idea.",
  "vis": {"type": "title", "title": "\"...no ray from it has yet\nbeen able to reach us at all.\"", "sub": "EDGAR ALLAN POE, EUREKA (1848)", "brand": False, "subcol": STAR}},

 # ---------- RE-ENGAGE: THE ACCOMPLICE ----------  # REENGAJE
 {"say": "But this case has an accomplice. Suspect number four. Space itself is stretching. Since Edwin Hubble's work in the nineteen twenties, we've known that distant galaxies are moving away from us, and the farther away they are, the faster they recede.",
  "vis": {"type": "suspects", "items": SUS, "focus": 3, "cleared": [0, 1], "guilty": [2], "title": "SUSPECT 4"}},
 {"say": "As light crosses expanding space, its waves get stretched. Blue shifts toward red. Red shifts into infrared. The most distant galaxies have been stretched right out of the colors our eyes can see. That's why the James Webb Space Telescope was built to see in infrared. That old light isn't gone. It's been dragged out of view.",
  "vis": {"type": "stretchwave", "s0": 1.1, "s1": 2.7, "head": "Expanding space stretches the light", "caption": "redshift: the farther the galaxy, the more its light is stretched"}},

 {"say": "Stretched light also loses energy. The James Webb Space Telescope has caught a galaxy whose light left it only about three hundred million years after the Big Bang. That light set out as ultraviolet. Its waves are now about fifteen times longer, and it arrives as infrared. To our eyes, that galaxy is perfectly black.",
  "vis": {"type": "stretchwave", "s0": 0.3, "s1": 2.5, "head": "Ultraviolet when it left, infrared when it arrives", "caption": "JWST galaxy JADES-GS-z14-0: light stretched ≈ 15×"}},

 # ---------- TWIST ----------
 {"say": "And now the twist. The sky is not actually black. About three hundred and eighty thousand years after the Big Bang, the entire universe was a glowing fog, at around three thousand degrees. In every direction, a wall of light. Exactly the sky that Olbers was looking for. And that wall is still out there, surrounding us right now.",
  "vis": {"type": "blaze", "speed": 0.6, "head": "380,000 years after the Big Bang"}},
 {"say": "But since then, space has stretched about eleven hundred times. That glow has cooled to just two point seven degrees above absolute zero, and its light has been stretched all the way into microwaves. It's called the cosmic microwave background, and it was found by accident in nineteen sixty five. If you ever saw static on an old analog TV, about one percent of that noise was this glow. The afterglow of the beginning.",
  "vis": {"type": "stretchwave", "s0": 1.4, "s1": 3.7, "temp": [3000, 2.725], "sub": "temperature of the glow", "caption": "cosmic microwave background: 2.725 K today, stretched ≈ 1,100× (our calculation)"}},
 {"say": "Suspect four, guilty. So in a strange way, Olbers was right. Every line of sight does end on a glowing wall. We just can't see it, because our eyes catch only a tiny slice of light, and the universe has stretched that glow far outside it.",
  "vis": {"type": "suspects", "items": SUS, "cleared": [0, 1], "guilty": [2, 3], "new": [3], "title": "CASE CLOSED"}},

 {"say": "And the darkness is growing. Expansion is speeding up, so distant galaxies are slowly being carried beyond the edge of what we can ever see. Physicists Lawrence Krauss and Robert Scherrer worked out that in more than a hundred billion years, astronomers in our galaxy might see no other galaxies at all, and the microwave glow would be stretched too thin to detect. Their night sky would be black, with no clues left that there was ever a beginning. We are lucky. We still get to read the evidence.",
  "vis": {"type": "compare", "left": ["TODAY", "billions of galaxies visible", "the glow of the Big Bang", "clues to the beginning"], "right": ["FAR FUTURE", "only our own galaxy", "the glow stretched away", "100+ billion years from now"], "cols": [MW, IR], "strike": False}},

 # ---------- VERDICT + NEXT ----------
 {"say": "So why is space black? Because the universe has an age, and light from most of it hasn't reached us. Because stars burn out. And because the oldest light has been stretched into colors we can't see. A dark night sky is one of the simplest pieces of evidence that the universe had a beginning. You can check it tonight, just by looking up.",
  "vis": {"type": "bullets", "title": "The verdict", "items": ["the universe has an age", "light from most of it hasn't arrived", "stars burn out", "the oldest light is stretched out of sight"], "col": MW, "highlight": 0}},
 {"say": "Next time, we build a star. What if Jupiter became one? How bright would our nights get, and would Earth survive the change? That's next.",
  "vis": {"type": "title", "title": "Next:\nWhat If Jupiter\nBecame a Star?", "sub": "COSMIC SCALE", "brand": False, "subcol": IR}},
]

SOURCES = [
 "NASA Science, Milky Way: 100 to 400 billion stars; NASA / Hubble: hundreds of billions of galaxies in the observable universe",
 "Olbers' paradox: Heinrich Wilhelm Olbers (1823); Johannes Kepler (1610); Edgar Allan Poe, \"Eureka\" (1848); Lord Kelvin (1901); Edward Harrison, \"Darkness at Night: A Riddle of the Universe\" (Harvard University Press, 1987)",
 "Dust argument fails: absorbed starlight would heat dust until it re-radiates (thermodynamics; see Harrison 1987)",
 "NASA Science, Andromeda: light takes about 2.5 million years to reach us",
 "ESA / Planck collaboration: age of the universe about 13.8 billion years; observable universe radius about 46.5 billion light-years",
 "NASA Science, the Sun: total lifetime about 10 billion years; surface (photosphere) about 5,500 °C",
 "Edwin Hubble (1929): galaxies recede faster the farther away they are; NASA James Webb Space Telescope observes in infrared to see redshifted distant galaxies",
 "NASA WMAP / COBE: cosmic microwave background, released about 380,000 years after the Big Bang at about 3,000 K, today 2.725 K; discovered by Penzias and Wilson (1965); roughly 1% of the static on an untuned analog TV",
 "NASA Apollo: the lunar sky is black at noon because the Moon has no atmosphere; Earth's daytime sky is blue from Rayleigh scattering of sunlight",
 "NASA / ESA / CSA JWST, JADES-GS-z14-0 (Carniani et al. 2024): redshift about 14.3, light emitted about 290 million years after the Big Bang",
 "Krauss & Scherrer (2007), General Relativity and Gravitation, \"The return of a static universe and the end of cosmology\"",
 "Own calculations (Python): the Sun covers 6.8 × 10^-5 steradians -> about 92,500 Suns to tile the half-sky above you; line-of-sight mean free path 1/(nσ) with 10^22 to 10^24 stars in the observable universe -> roughly 10^22 to 10^24 light-years; CMB stretch 3,000 K / 2.725 K ≈ 1,100; light stretch 1 + z ≈ 15.3 for z = 14.3",
]
