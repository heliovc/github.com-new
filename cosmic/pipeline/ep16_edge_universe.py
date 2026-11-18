# EP16 — Why Can't We See the Edge of the Universe?
# Structure NEW: "five walls" — we fly a telescope's line of sight outward and hit five walls, each one a different reason the edge stays
# hidden (time, stretch, dimming + slow motion, the funhouse mirror, the fog), then the last question: is there an edge at all?
# Different from EP03 (size ladder + horizons): here the stars are the weird optics of looking back in time.
# Palette infrared crimson / fog amber / deep teal on near-black maroon. New scenes: zdial (chapter card: a redshift dial on a log scale
# with live lookback / distance-then / distance-now readouts computed from a flat ΛCDM model), lightcone (the "teardrop": distance of the
# source when its light left vs cosmic time; a dot rides the curve), angsize (one galaxy, same real size, placed farther and farther:
# telescope eyepiece + apparent size curve with the turnaround at z≈1.6; dim=True adds the (1+z)^4 dimming meter), slowmo (two supernova
# light curves, nearby vs z=1, the far one stretched ×2 with two clocks), fogwall (hot plasma: photons bounce between free electrons,
# temperature falls to 3,000 K, atoms form and the light flies free).
# Own calculations (Python, flat ΛCDM, Planck 2018 H0 = 67.66, Ωm = 0.311): age 13.79 Gyr; particle horizon 46.2 Gly; event horizon 16.6 Gly;
# MoM-z14 (z = 14.44): lookback 13.50 Gyr, 2.19 Gly away when the light left, 33.9 Gly now; the largest "distance when emitted" of any
# light we receive is 5.85 Gly at z = 1.59 (lookback 9.7 Gyr); a 100,000 ly galaxy looks 16" at z=0.1, 3.5" at z=1.6, 9.4" at z=14.4;
# surface-brightness dimming (1+z)^4: 16 at z=1, 56,800 at z=14.44; Lyman-alpha 121.6 nm × 15.44 = 1.88 µm; CMB z ≈ 1,090, 3,000 K / 1,091 ≈ 2.7 K;
# CMB matter 42 million ly away then, 45.3 Gly now.
TITLE = "Why Can't We See the Edge of the Universe?"
RED = [255, 84, 84]
AMB = [255, 178, 70]
TEAL = [70, 210, 200]

SCENES = [
 # ---------- HOOK ----------
 {"say": "Here's something that sounds like a mistake. Point a telescope at a galaxy, then at an identical one much farther away. The far one should look smaller. And it does, up to a point. Then, if you keep going, the farther galaxy starts to look bigger.",
  "vis": {"type": "angsize", "z0": 0.1, "z1": 14.44, "head": "Farther away, and it looks BIGGER?"}},
 {"say": "That's not an optical trick. It's a clue about why nobody, with any telescope, will ever see the edge of the universe. There are five walls in the way. Let's hit them, one by one.",
  "vis": {"type": "title", "title": "Why Can't We See the\nEdge of the Universe?", "sub": "COSMIC SCALE", "brand": True, "subcol": RED}},

 # ---------- WALL 1: TIME ----------
 {"say": "Wall number one is time. Light is fast, but not infinitely fast. So when you look far, you also look back. The Sun you see is eight minutes old. The Andromeda galaxy, two and a half million years old.",
  "vis": {"type": "zdial", "z": 0.0, "n": 1, "title": "Time", "sub": "looking far = looking back", "kicker": "WALL 1 OF 5"}},
 {"say": "Now go much deeper. At a redshift of one, a number astronomers use for distance in time, you're seeing light that left almost eight billion years ago. Before the Earth existed. Before the Sun existed.",
  "vis": {"type": "zdial", "z": 1.0, "n": 1, "title": "Older Than\nthe Sun", "sub": "light that left 7.9 billion years ago", "kicker": "REDSHIFT 1"}},
 {"say": "And the universe itself is only thirteen point eight billion years old. So there's a hard limit. You can't receive light that's older than the universe. Whatever is out there beyond that, its light simply hasn't arrived yet. Not dim. Not hidden. Just still on its way. Every year that passes, a little more of it gets here, and our view grows a tiny bit deeper.",
  "vis": {"type": "bignumber", "from": 0, "to": 13.8, "decimals": 1, "suffix": " billion years", "col": RED, "caption": "the oldest any light can be (Planck satellite: 13.79 billion years)"}},

 # ---------- WALL 2: STRETCH ----------
 {"say": "Wall number two is the stretch. While that ancient light travels, space expands underneath it. And the light expands with it. Its waves get longer, and redder.",
  "vis": {"type": "zdial", "z": 3.0, "n": 2, "title": "The Stretch", "sub": "space grows, light gets redder", "kicker": "WALL 2 OF 5"}},
 {"say": "The farthest galaxy ever confirmed is called MoM z fourteen. Its light left when the universe was about two hundred eighty million years old. Ultraviolet light from its young, hot stars arrives here more than fifteen times longer. Pushed right past red, deep into the infrared. Invisible to your eyes, and to Hubble's best camera.",
  "vis": {"type": "stretchwave", "s0": 0.35, "s1": 2.25, "head": "Ultraviolet in, infrared out", "caption": "MoM-z14, redshift 14.44: 121.6 nm becomes 1.88 µm (our calculation)"}},
 {"say": "And that stretch is also a measuring tape. A redshift of fourteen point four four means every wave arrives fifteen point four four times longer than it left. Which means the universe itself has grown fifteen point four four times in every direction since that light set off.",
  "vis": {"type": "bignumber", "from": 1, "to": 15.44, "decimals": 2, "suffix": "×", "col": RED, "caption": "how much the universe has grown since MoM-z14's light left (1 + z)"}},
 {"say": "That's exactly why the James Webb telescope was built for infrared, with a sunshield the size of a tennis court, keeping it colder than minus two hundred twenty degrees. A warm telescope would glow in the same light it's trying to catch.",
  "vis": {"type": "compare", "left": ["HUBBLE", "mostly visible + UV", "near-infrared to 1.7 µm", "2.4 m mirror"], "right": ["WEBB", "infrared, 0.6 to 28 µm", "colder than −223 °C", "6.5 m mirror"], "cols": [TEAL, RED], "strike": False}},

 # ---------- WALL 3: DIMMING + SLOW MOTION ----------
 {"say": "Wall number three is a double penalty. Far away things are dim, of course. But in an expanding universe, they get dimmer much faster than distance alone would explain.",
  "vis": {"type": "zdial", "z": 6.0, "n": 3, "title": "The Fade", "sub": "dimmer, and slower", "kicker": "WALL 3 OF 5"}},
 {"say": "Each photon loses energy as it's stretched. And the photons also arrive spread out, fewer per second. Put those effects together, and the surface brightness of a galaxy falls with one plus the redshift, to the fourth power. At redshift one, that's sixteen times dimmer. For MoM z fourteen, about fifty seven thousand times dimmer, on top of the normal fading with distance.",
  "vis": {"type": "angsize", "z0": 1.0, "z1": 14.44, "dim": True, "head": "The fade: (1 + z) to the 4th power"}},
 {"say": "And here's the strangest part. The distant universe is playing in slow motion. An exploding star called a type one A supernova brightens and fades over a few weeks. In twenty twenty four, the Dark Energy Survey compared fifteen hundred of them. The ones at redshift one took twice as long. Exactly the stretch the expanding universe predicts.",
  "vis": {"type": "slowmo", "z": 1.0, "head": "Same explosion, twice as slow"}},
 {"say": "So the far universe is redder, dimmer, and slower. Every step outward, it gets harder to see anything at all.",
  "vis": {"type": "bullets", "title": "The farther you look", "items": ["redder: light stretched", "dimmer: (1 + z)⁴", "slower: time stretched", "older: up to 13.8 billion years"], "col": AMB}},

 # ---------- WALL 4: THE FUNHOUSE MIRROR ----------
 {"say": "Wall number four is the funhouse mirror. Remember the galaxy that looked bigger when it was farther? Here's why.",
  "vis": {"type": "zdial", "z": 1.6, "n": 4, "title": "The Funhouse\nMirror", "sub": "why far things look big", "kicker": "WALL 4 OF 5"}},
 {"say": "The light from MoM z fourteen has traveled thirteen and a half billion years. But when it left, that galaxy wasn't thirteen and a half billion light years away. Using the standard model of the universe, we calculated it was only about two point two billion. The universe was smaller then, and everything was closer together.",
  "vis": {"type": "lightcone", "z": 14.44, "head": "Distance when the light left"}},
 {"say": "So we see it at the size it had, at that closer distance. Its image is like an old photo, taken up close, that took billions of years to be mailed to us. That's why it looks larger than galaxies in between. The astronomer Fred Hoyle pointed this out back in nineteen fifty nine. It falls straight out of the math of an expanding universe.",
  "vis": {"type": "angsize", "z0": 1.6, "z1": 14.44, "head": "An old photo, taken up close"}},
 {"say": "Now trace every light ray we receive, back to where it started. They make this teardrop shape. And the widest point of the teardrop is a surprise. No light that reaches us today left from farther than about five point eight billion light years away. The deepest pictures ever taken show things that were, at the time, relatively near.",
  "vis": {"type": "lightcone", "z": 1.59, "max": True, "head": "The widest point: 5.8 billion light-years"}},

 # ---------- WALL 5: THE FOG ----------
 {"say": "Wall number five is the real wall. Go back far enough, and the universe stops being transparent.",
  "vis": {"type": "zdial", "z": 1090, "n": 5, "title": "The Fog", "sub": "the universe was opaque", "kicker": "WALL 5 OF 5"}},
 {"say": "For its first three hundred eighty thousand years, the universe was a hot glowing plasma. Electrons weren't attached to atoms. They floated free, and light couldn't travel in a straight line. A photon would hit an electron, bounce, hit another, bounce again. Like headlights in thick fog.",
  "vis": {"type": "fogwall", "mode": "fog", "head": "Before 380,000 years: fog"}},
 {"say": "Then it cooled to about three thousand degrees, roughly as hot as the filament of an old light bulb. Electrons finally settled into atoms. The fog cleared, and the light that was there at that moment has been flying free ever since.",
  "vis": {"type": "fogwall", "mode": "clear", "head": "At 3,000 kelvin, the fog clears"}},
 {"say": "That light is still arriving, from every direction. Stretched about eleven hundred times, it's now microwaves, at less than three degrees above absolute zero. The cosmic microwave background. It's the farthest thing we can see with light. The glowing gas that sent it was only about forty two million light years away back then. Today, by our calculation, that same matter is about forty five billion light years away.",
  "vis": {"type": "stretchwave", "s0": 1.2, "s1": 3.6, "temp": [3000, 2.73], "sub": "temperature of the glow", "caption": "Big Bang afterglow: 3,000 K then, 2.725 K now"}},
 {"say": "After the fog cleared, the universe went dark. No stars yet, just cooling hydrogen gas. Astronomers call it the cosmic dark ages. Webb is now catching the very end of it, galaxies only a few hundred million years after the Big Bang. Radio telescopes are trying to hear the hydrogen itself, a faint signal born at twenty one centimeters, stretched by now to meters.",
  "vis": {"type": "zdial", "z": 20.0, "n": 5, "title": "The Dark\nAges", "sub": "after the fog, before the stars", "kicker": "BETWEEN THE WALLS"}},
 {"say": "Behind that glow is a wall no telescope will ever see through. Not because it's far, but because it's opaque. To look past it, we'd need something other than light. Ghostly particles called neutrinos, released about one second after the Big Bang. Or ripples in space itself, gravitational waves. Both should be out there. Neither has been caught from that era yet.",
  "vis": {"type": "compare", "left": ["LIGHT", "stops at 380,000 years", "the fog wall", "seen: yes"], "right": ["OTHER MESSENGERS", "neutrinos: first second", "gravitational waves", "seen: not yet"], "cols": [AMB, TEAL], "strike": False}},

 # ---------- THE LAST QUESTION ----------
 {"say": "So every direction we look, the view ends at that glowing shell, about forty six billion light years away. Which means we're at the center of our view. But so is everyone. An alien astronomer in MoM z fourteen would see their own bubble, centered on them, reaching places we will never see.",
  "vis": {"type": "lightbubble", "caption": "Every observer has their own observable universe"}},
 {"say": "And it shrinks in a sense, too. Because the expansion is speeding up, light that a galaxy sends today will only ever reach us if that galaxy is less than about sixteen and a half billion light years away right now. Farther than that, and its present is cut off from us forever.",
  "vis": {"type": "lightcone", "z": 1.59, "event": True, "head": "The point of no return: 16.6 billion light-years"}},
 {"say": "And what's beyond the horizon? Probably more of the same. The ancient glow looks almost identical in every direction, the same temperature to about one part in a hundred thousand. Nothing in it hints that our patch is special, or that the galaxies stop just past where we can see.",
  "vis": {"type": "bignumber", "from": 1, "to": 100000, "prefix": "1 part in ", "col": TEAL, "caption": "how evenly the afterglow's temperature is spread across the sky (NASA/ESA)"}},
 {"say": "So is there an edge out there at all? The Planck satellite measured the geometry of space from that ancient glow. It came out flat, to within about a fifth of a percent. A flat universe can go on forever. Or be curved so gently, on a scale so huge, that we can't tell. Either way, there is no sign of a wall, or a border, or a place where space stops.",
  "vis": {"type": "compare", "left": ["CURVED", "finite, no border", "like a sphere's surface", "not ruled out"], "right": ["FLAT", "Planck: flat to ~0.2%", "could be infinite", "best fit so far"], "cols": [AMB, RED], "strike": False}},
 {"say": "That's the twist. We can't see the edge of the universe, because there's probably no edge to see. What we have instead is a horizon in time. Five walls, and beyond them, more universe.",
  "vis": {"type": "bullets", "title": "Five walls", "items": ["1. time: 13.8 billion years", "2. the stretch: into infrared", "3. the fade: dimmer and slower", "4. the funhouse mirror", "5. the fog: 380,000 years"], "col": RED}},

 # ---------- NEXT ----------
 {"say": "Next time, we come back to something closer, but way bigger than it looks. We'll put the biggest star ever measured in place of our Sun, and see what happens to the planets. Subscribe to Cosmic Scale so you don't miss it. And tell me in the comments, if you could see past the fog, what would you hope to find?",
  "vis": {"type": "title", "title": "Next: the biggest star\nin place of our Sun", "sub": "COSMIC SCALE", "subcol": AMB}},
]

SOURCES = ["Planck Collaboration (2018): age of the universe 13.787 ± 0.020 billion years; H0 = 67.66 km/s/Mpc, matter density 0.311; spatial curvature consistent with flat (Ωk = 0.0007 ± 0.0019 with BAO)",
           "Naidu et al. (2025), Open Journal of Astrophysics (2026): MoM-z14 confirmed with JWST at redshift 14.44, about 280 million years after the Big Bang",
           "NASA/STScI: James Webb Space Telescope observes 0.6 to 28.5 µm, 6.5 m mirror, tennis-court-sized sunshield, instruments below about 50 K; Hubble 2.4 m mirror observes ultraviolet, visible and near-infrared (to about 1.7 µm)",
           "R. M. White et al. (2024), MNRAS 533, 3365, Dark Energy Survey: 1,504 Type Ia supernovae (redshift 0.1 to 1.2) show light-curve widths stretched by (1 + z), as expected from cosmic time dilation",
           "F. Hoyle (1959): in an expanding universe the apparent angular size of objects reaches a minimum and then grows with distance", "Tolman surface-brightness test: in an expanding universe surface brightness falls as (1 + z)^4",
           "NASA (WMAP/Planck): the cosmic microwave background was released about 380,000 years after the Big Bang at about 3,000 K; today 2.725 K",
           "NASA: the cosmic neutrino background (decoupled about 1 second after the Big Bang) and primordial gravitational waves have not yet been detected directly",
           "Own calculations (flat ΛCDM with the Planck 2018 values above): radius of the observable universe 46.2 billion light-years; cosmic event horizon 16.6 billion light-years; redshift 1 = 7.9 billion years of lookback; MoM-z14 was 2.19 billion light-years away when its light left and is 33.9 billion light-years away today; maximum distance-at-emission 5.85 billion light-years at redshift 1.59; the apparent size of a 100,000 light-year galaxy is smallest near redshift 1.6 (3.5 arcseconds) and grows to 9.4 arcseconds at redshift 14.44; (1+z)^4 = 16 at z = 1 and about 56,800 at z = 14.44; Lyman-alpha 121.6 nm × 15.44 ≈ 1.88 µm; CMB emitted about 42 million light-years away, now about 45.3 billion light-years"]
