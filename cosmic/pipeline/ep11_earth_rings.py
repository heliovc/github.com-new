# EP11 — What If Earth Had Rings Like Saturn?
# Structure NEW: "postcards by latitude" — hook (a glowing arch over New York at night) -> build the rings (Saturn's, scaled to Earth;
# why they must sit inside the Roche limit; 10 m thick) -> 5 postcards travelling north: Quito 0° (edge-on line), Mexico City 19°
# (huge band), New York 41° (inner ring gone), London 52° (low arc), Reykjavik 64° (nothing) -> the fine print: the night arch with
# Earth's shadow, the winter ring shadow (season chart), satellites -> rings don't last (ring rain) -> TWIST: Earth may have had a ring
# 466 million years ago -> Mars will get one -> EP12.
# Palette ring cream / dusk rose / sea teal. New scenes: ringsky, orbitzones, ringedge, shadowmap, craterbelt.
# Own calculations (Python): Saturn ring radii in Saturn radii (R = 60,268 km): C 1.239–1.527, B 1.527–1.951, Cassini Division
# 1.951–2.027, A 2.027–2.269 -> scaled to Earth (6,371 km): 7,892–14,459 km from the centre = 1,521–8,088 km above the surface.
# A ring edge at r Earth radii is above the horizon only where cos(lat) > 1/r: inner C edge up to 36.2°, inner B up to 49.1°,
# outer B up to 59.2°, outer A up to 63.9°. Ring shadow at noon on the winter solstice (Sun 23.44° below the equator plane):
# x = cos(lat) + sin(lat)/tan(23.44°) -> C ring 7–13°, B ring 14–27°, A ring 31–41° of the winter hemisphere.
# Roche limit 2.44 R (5,514/rho)^(1/3): ice (900) ≈ 28,400 km, rock (3,000) ≈ 19,000 km. Ring width/thickness 273,000 km / 10 m
# = 27 million -> a sheet of paper (0.1 mm) would be 2.7 km wide.
TITLE = "What If Earth Had Rings Like Saturn?"
CREAM = [240, 226, 196]
ROSE = [240, 140, 160]
TEAL = [70, 200, 185]

SCENES = [
 # ---------- HOOK ----------
 {"say": "Step outside in New York tonight, and a glowing arch splits the sky in two. It rises from the east, arcs over the southern horizon, and comes down in the west, glowing with reflected sunlight. And in the middle of it, there's a dark patch, as if someone took a bite out of it.",
  "vis": {"type": "ringsky", "lat": 40.7, "mode": "night", "shadow": True, "elev": 28, "city": "New York"}},
 {"say": "That's what Earth would look like with rings like Saturn's. But move a few thousand kilometers and the view changes completely. In one city it's a thin line. In another it fills half the sky. And in some places, the rings would steal the winter sunshine.",
  "vis": {"type": "ringsky", "lat": 19.4, "mode": "day", "elev": 35, "city": "Mexico City"}},
 {"say": "What If Earth Had Rings Like Saturn?",
  "vis": {"type": "title", "title": "What If Earth Had\nRings Like Saturn?", "sub": "COSMIC SCALE", "brand": True, "subcol": ROSE}},

 # ---------- BUILD THE RINGS ----------
 {"say": "First, let's build them. We'll take Saturn's main rings and shrink them to fit Earth, keeping the same proportions. The inner edge would sit about fifteen hundred kilometers above the ground. The outer edge, about eight thousand. Edge to edge, they'd be wider than the whole planet.",
  "vis": {"type": "orbitzones", "fit0": 16000, "fit1": 16000, "show": ["rings"], "head": "Saturn's rings, shrunk to fit Earth", "caption": "our calculation: 7,900 to 14,500 km from Earth's centre"}},
 {"say": "Why so close? Because rings can only survive near a planet. Inside a boundary called the Roche limit, the planet's tides pull harder on the near side of a clump than on the far side, so loose material can never pull itself together into a moon. For icy rubble around Earth, that limit is roughly twenty eight thousand kilometers from the center. For rock, about nineteen thousand. Our Moon sits more than twenty times farther out.",
  "vis": {"type": "orbitzones", "fit0": 16000, "fit1": 32000, "show": ["rings", "roche", "moon"], "head": "Rings live inside the Roche limit", "caption": "Roche limit: our calculation for ice and for rock"}},
 {"say": "And here's the part that's hard to believe. Saturn's main rings stretch across roughly two hundred seventy thousand kilometers, but in most places they're only about ten meters thick. That's about the height of a three storey building.",
  "vis": {"type": "ringedge", "head": "Zoom in on the edge of a ring", "caption": "273,000 km across, about 10 m thick (NASA)"}},
 {"say": "If you shrank the rings down to the thickness of a sheet of paper, by our calculation they'd still be almost three kilometers wide. They're made almost entirely of water ice, in pieces from tiny grains up to boulders several meters across, all circling in their own orbits. Each piece is basically a tiny moon. Billions of them, bumping gently into each other, flattening the whole system into a sheet.",
  "vis": {"type": "bignumber", "from": 0, "to": 2.7, "decimals": 1, "suffix": " km", "col": CREAM, "caption": "a ring as thin as paper would be this wide (our calculation)"}},

 # ---------- POSTCARDS ----------
 {"say": "Now let's travel. Postcard number one, from Quito, right on the equator. You're standing exactly in the plane of the rings, so you see them edge on. Just a thin, bright line running from east to west, straight over your head. By day, you might not even notice it.",
  "vis": {"type": "ringsky", "lat": 0, "mode": "day", "elev": 58, "city": "Quito"}},
 {"say": "But the rings would still be up there, casting a narrow shadow, and a single stripe would cut across the equator. Every launch from near the equator, where rockets get the biggest boost from Earth's spin, would have to be planned around the rings.",
  "vis": {"type": "ringsky", "lat": 0, "mode": "dusk", "elev": 58, "city": "Quito"}},
 {"say": "Postcard two, from Mexico City, about nineteen degrees north. Here the rings become a vast ribbon, sweeping from the eastern horizon to the western one, high across the southern sky. All three main rings are visible, the faint inner ring, the bright middle one, and the outer ring, with a dark gap between them. The gap alone would look wider than the full Moon. At sunset, the whole arch would turn orange and pink, long after the ground had gone dark, because sunlight still reaches the ice high above you.",
  "vis": {"type": "ringsky", "lat": 19.4, "mode": "night", "elev": 35, "city": "Mexico City"}},
 {"say": "Postcard three, from New York. The arch is lower now, and something is missing. The faint inner ring has slipped below the horizon, hidden behind the curve of the Earth. By our calculation, nobody north of about thirty six degrees could ever see it.",
  "vis": {"type": "ringsky", "lat": 40.7, "mode": "day", "elev": 28, "city": "New York"}},
 {"say": "Postcard four, from London. Now only the outer rings peek over the southern horizon, a low pale arc, like a permanent rainbow that never moves. And the farther north you go, the more of it sinks out of sight.",
  "vis": {"type": "ringsky", "lat": 51.5, "mode": "dusk", "elev": 18, "city": "London"}},
 {"say": "And postcard five, from Reykjavik, at sixty four degrees north. Nothing. By our calculation, the outer edge of the rings would sit just below the horizon. People in Iceland, northern Scandinavia and Alaska would live on a ringed planet and never see the rings at all, unless they traveled south. Imagine flying from Reykjavik to Madrid, and watching a giant arch slowly climb out of the horizon as you go. For many people, a first look at the rings would be a vacation photo.",
  "vis": {"type": "ringsky", "lat": 64.1, "mode": "night", "elev": 15, "city": "Reykjavik"}},
 {"say": "The southern hemisphere gets the same show in reverse. From Sydney or Buenos Aires, the arch would hang over the northern horizon instead. Wherever you live, the rings always sit over the equator.",
  "vis": {"type": "compare", "left": ["NORTH", "rings to the south", "visible to ≈ 64° N", "lowest near the pole"], "right": ["SOUTH", "rings to the north", "visible to ≈ 64° S", "same arch, mirrored"], "cols": [ROSE, TEAL], "strike": False}},

 # ---------- THE FINE PRINT ----------
 {"say": "Now the fine print. First, the nights. Ice is a great mirror, so the rings would reflect sunlight down onto the night side of Earth. Nights would never get truly dark. But around midnight, Earth's own shadow falls across the rings, and that's the dark bite you saw in New York.",
  "vis": {"type": "ringsky", "lat": 25.8, "mode": "night", "shadow": True, "elev": 32, "city": "Miami"}},
 {"say": "Second, the winters. Earth is tilted, so for half the year the Sun sits below the plane of the rings for the northern hemisphere, and above it for the southern one. In winter, the rings would stand between you and the Sun.",
  "vis": {"type": "shadowmap", "cities": ["Quito", "Mexico City", "Miami", "Cairo", "New York", "London", "São Paulo", "Sydney"], "head": "A year of ring shadows", "caption": "noon shadow of Saturn-like rings, our calculation"}},
 {"say": "By our calculation, at noon on the winter solstice, the shadow of the thick middle ring would cover a band from about fourteen to twenty seven degrees of latitude. Mexico City, Hong Kong, Havana and Miami would spend part of every winter in a long twilight, with the Sun dimmed or blocked at midday. Darker winters would almost certainly mean colder winters. And because the shadow drifts with the seasons, sliding toward the equator as spring arrives, every city in that band would get its own strange calendar of shadow days.",
  "vis": {"type": "shadowmap", "cities": ["Mexico City", "Hong Kong", "Miami", "Cairo", "New York", "São Paulo", "Sydney"], "head": "The thick B ring's shadow", "caption": "at noon on the winter solstice: about 14° to 27° (our calculation)"}},
 {"say": "Third, satellites. The International Space Station flies about four hundred twenty kilometers up, below our rings. GPS satellites fly about twenty thousand kilometers up, above them. But anything that has to cross the rings would risk smashing into ice at several kilometers per second. The space between fifteen hundred and eight thousand kilometers would be a no fly zone.",
  "vis": {"type": "orbitzones", "fit0": 30000, "fit1": 44000, "show": ["rings", "iss", "gps", "geo"], "head": "Satellites would have to work around the rings", "caption": "ISS ≈ 420 km, GPS ≈ 20,200 km, geostationary 35,786 km"}},

 # ---------- RINGS DON'T LAST ----------
 {"say": "And fourth, the rings wouldn't last forever. Saturn is losing its rings right now. Icy particles get electrically charged and pulled along its magnetic field into the planet. NASA scientists estimate this ring rain drains enough water to fill an Olympic swimming pool every half hour.",
  "vis": {"type": "bignumber", "from": 0, "to": 30, "suffix": " min", "col": TEAL, "caption": "one Olympic pool of ring material lost every half hour (NASA, O'Donoghue et al. 2018)"}},
 {"say": "At that pace, the whole ring system could be gone in about three hundred million years, and maybe much sooner. Some measurements even suggest the rings themselves are young, only a few hundred million years old. That means we're lucky to be alive while Saturn has them.",
  "vis": {"type": "compare", "left": ["RING RAIN ALONE", "≈ 300 million years", "until the rings", "are gone"], "right": ["WITH CASSINI DATA", "maybe under 100", "million years", "left"], "cols": [TEAL, ROSE], "strike": False}},

 # ---------- TWIST ----------
 {"say": "Now the twist. Earth may already have had a ring. In twenty twenty four, geologists at Monash University in Australia mapped twenty one impact craters from about four hundred sixty six million years ago, a time when there was a sudden spike in meteorite impacts.",
  "vis": {"type": "craterbelt", "head": "Did Earth already have a ring?"}},
 {"say": "When they rebuilt where the continents sat back then, every one of those craters landed within thirty degrees of the equator, even though most of the land that could have kept a crater lay outside that band. Their explanation? A large asteroid passed inside Earth's Roche limit, broke apart, and formed a ring that slowly rained down along the equator.",
  "vis": {"type": "craterbelt", "head": "21 craters, all near the equator", "caption": "Tomkins, Martin & Cawood, Earth and Planetary Science Letters (2024)"}},
 {"say": "They even suggested the ring's shadow may have helped cool the planet, just before one of the coldest periods in Earth's history. Not every scientist is convinced, and the dating of some craters is still debated. But it means the view from your street might have looked like this once, long before anyone was around to see it.",
  "vis": {"type": "ringsky", "lat": 30, "mode": "dusk", "elev": 30, "city": "466 million years ago"}},
 {"say": "And Earth won't be the last. Mars's moon Phobos is spiraling inward. In roughly twenty to forty million years, according to a twenty fifteen study, it will cross Mars's Roche limit and be torn into a ring. Mars is about to become a ringed planet. On the scale of the universe, that's the blink of an eye.",
  "vis": {"type": "bignumber", "from": 40, "to": 40, "prefix": "20–", "suffix": " million yr", "col": ROSE, "caption": "until Phobos breaks into a ring around Mars (Black & Mittal, Nature Geoscience 2015)"}},

 # ---------- RECAP + NEXT ----------
 {"say": "So, rings like Saturn's would hang fifteen hundred to eight thousand kilometers above us, only about ten meters thick. They'd be a thin line from the equator, a huge arch from the tropics, and invisible from the far north. They'd brighten our nights, darken our winters, and get in the way of our satellites. And they might not be science fiction at all. They might be Earth's past.",
  "vis": {"type": "bullets", "title": "A ringed Earth", "items": ["1,500 to 8,100 km above us", "about 10 m thick", "invisible north of ≈ 64°", "brighter nights, darker winters", "maybe our past"], "col": ROSE, "highlight": 4}},
 {"say": "Next time, the fastest thing in the universe turns out to be painfully slow. Light takes eight minutes to reach us from the Sun, and the numbers only get worse from there. The speed of light is slow, and here's the proof. That's next.",
  "vis": {"type": "title", "title": "Next:\nThe Speed of Light\nIs Slow", "sub": "COSMIC SCALE", "brand": False, "subcol": TEAL}},
]

SOURCES = [
 "NASA Science, Saturn's rings: main rings extend up to about 282,000 km from the planet but are about 10 m thick in most places; made mostly of water ice, from tiny grains to large chunks",
 "NASA Saturnian Rings Fact Sheet: ring radii (C ring 74,658–92,000 km, B ring 92,000–117,580 km, Cassini Division 117,580–122,170 km, A ring 122,170–136,775 km); Saturn's equatorial radius 60,268 km",
 "NASA / O'Donoghue et al. (2018), Icarus: 'ring rain' drains about an Olympic pool of material every half hour; rings could be gone in about 300 million years, possibly under 100 million with Cassini data",
 "Iess et al. (2019), Science (Cassini Grand Finale): low ring mass, consistent with relatively young rings",
 "Tomkins, Martin & Cawood (2024), Earth and Planetary Science Letters, 'Evidence suggesting that Earth had a ring in the Ordovician': 21 impact craters from about 466 million years ago, all within 30° of the equator; proposed ring and possible link to the Hirnantian icehouse",
 "Eos (AGU), 2024: other researchers call for more precise crater dating before accepting the ring hypothesis",
 "Black & Mittal (2015), Nature Geoscience, 'The demise of Phobos and development of a Martian ring system': Phobos breaks into a ring in about 20 to 40 million years",
 "NASA: International Space Station orbits about 400–420 km up; GPS satellites about 20,200 km; geostationary orbit 35,786 km",
 "Own calculations (Python): Saturn's rings scaled to Earth = 7,900–14,500 km from the centre (1,500–8,100 km up); ring edges visible from the ground only where cos(latitude) is greater than 1/r (inner ring up to about 36°, outer edge up to about 64°); noon ring shadow on the winter solstice for 23.44° axial tilt (B ring about 14°–27°, whole ring system about 7°–41°); Roche limit 2.44 R (density ratio)^(1/3) about 28,400 km for ice and 19,000 km for rock; 273,000 km / 10 m = 27 million, so paper-thin rings would be about 2.7 km wide",
]
