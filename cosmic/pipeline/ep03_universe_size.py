# EP03 — How Big Is the Universe, Really?
# Structure: "zoom-out ladder" (light-travel odometer, 9 rungs) -> the 13.8 vs 46 paradox -> three horizons -> galaxy count -> shrink-to-Earth -> beyond the edge.
# Palette: violet / magenta. New scene types: zoom, stretch, horizons, deepfield, shrink
TITLE = "How Big Is the Universe, Really?"
VIO = [186, 140, 255]
MAG = [255, 120, 200]

SCENES = [
 # ---------- HOOK ----------
 {"say": "The universe is thirteen point eight billion years old. So the farthest we can see should be thirteen point eight billion light years, right? Wrong. The edge of what we can see is about forty six billion light years away, in every direction. More than three times farther than light could have traveled. Today we find out how that's possible, and how big everything really is.",
  "vis": {"type": "bignumber", "from": 13.8, "to": 46, "decimals": 1, "suffix": " bn ly", "col": MAG, "caption": "13.8 billion years old. 46 billion light-years to the edge."}},
 {"say": "To feel it, we need a ruler that works out there. Not kilometers. Light. Light moves at almost three hundred thousand kilometers every second. One light year, the distance it covers in a year, is about nine and a half trillion kilometers. Let's climb, one rung at a time.",
  "vis": {"type": "title", "title": "How Big Is the\nUniverse, Really?", "sub": "COSMIC SCALE", "brand": True, "subcol": VIO}},

 # ---------- THE LADDER ----------
 {"say": "Rung one. The Moon. Light covers the distance from Earth to the Moon in about one point three seconds. Every Moon you have ever seen was a little over a second old.",
  "vis": {"type": "zoom", "rung": 0, "kind": "moon", "name": "Earth → Moon", "lt": "1.3 seconds", "dist": "384,400 km"}},
 {"say": "Rung two. The Sun. Eight minutes and twenty seconds. When you feel sunlight on your skin, it left the Sun before you finished your coffee.",
  "vis": {"type": "zoom", "rung": 1, "kind": "sun", "name": "Earth → Sun", "lt": "8 min 20 s", "dist": "150 million km", "prev": "Moon"}},
 {"say": "Rung three. Neptune, the last big planet. About four hours. A message sent to a spacecraft there at breakfast gets its answer back after lunch.",
  "vis": {"type": "zoom", "rung": 2, "kind": "solar", "name": "Sun → Neptune", "lt": "≈ 4 hours", "dist": "4.5 billion km", "prev": "Earth's orbit"}},
 {"say": "Rung four. Voyager one, our most distant spacecraft, launched in nineteen seventy seven. This month, it reaches a distance of one full light day. NASA's signal, moving at the fastest speed there is, will take twenty four hours just to get there.",
  "vis": {"type": "zoom", "rung": 3, "kind": "voyager", "name": "Earth → Voyager 1", "lt": "≈ 1 day", "dist": "≈ 26 billion km", "prev": "Neptune's orbit"}},
 {"say": "Now the first giant jump. The nearest star, Proxima Centauri. Four point two four light years. Voyager would need more than seventy thousand years to get there. Everything humans have ever built is still sitting at the front door.",
  "vis": {"type": "zoom", "rung": 4, "kind": "stars", "name": "Sun → Proxima Centauri", "lt": "4.24 years", "dist": "40 trillion km", "prev": "Voyager 1"}},
 {"say": "Rung six. Our galaxy, the Milky Way. About one hundred thousand light years across, with at least one hundred billion stars. Light takes so long to cross it that the starlight arriving from the far side today set off before humans had invented farming.",
  "vis": {"type": "zoom", "rung": 5, "kind": "galaxy", "name": "Across the Milky Way", "lt": "100,000 years", "dist": "at least 100 billion stars", "prev": "Sun + neighbors"}},
 {"say": "Rung seven. Andromeda, the nearest big galaxy, about two and a half million light years away. On a dark night you can see it with your naked eye. That faint smudge is light that left when our ancestors were first learning to make stone tools.",
  "vis": {"type": "zoom", "rung": 6, "kind": "local", "name": "Milky Way → Andromeda", "lt": "2.5 million years", "dist": "nearest big galaxy", "prev": "Milky Way"}},
 {"say": "Rung eight. In twenty fourteen, astronomers mapped how galaxies flow through space and drew the borders of our home supercluster. They named it Laniakea, Hawaiian for immeasurable heaven. It spans about five hundred and twenty million light years and holds around one hundred thousand galaxies.",
  "vis": {"type": "zoom", "rung": 7, "kind": "super", "name": "Laniakea supercluster", "lt": "520 million years", "dist": "≈ 100,000 galaxies", "prev": "Local Group"}},
 {"say": "And the final rung. The edge of the observable universe. About forty six billion light years in every direction. Ninety three billion light years from one side to the other. Which brings us back to the puzzle. How can anything be that far, in a universe only thirteen point eight billion years old?",
  "vis": {"type": "zoom", "rung": 8, "kind": "universe", "name": "The observable universe", "lt": "46 billion ly", "ltlab": "RADIUS", "dist": "93 billion ly across", "prev": "Laniakea"}},

 # ---------- THE PARADOX ----------
 {"say": "Here is the trick. Space itself is stretching. Picture a photon leaving a distant galaxy. It races toward us at the speed of light, but the space it crosses keeps growing underneath it, like an ant walking on a balloon that someone keeps inflating. By the time the light finally arrives, after thirteen and a half billion years, the galaxy that sent it has been carried much farther away.",
  "vis": {"type": "stretch", "a0": 0.07, "light": 13.5, "now": 33.9, "src": "MoM-z14", "caption": "The light travels. The space it crosses keeps stretching."}},
 {"say": "This is a real example. In twenty twenty five, the James Webb Space Telescope confirmed a galaxy called MoM z fourteen. Its light is about thirteen and a half billion years old. When that light left, the galaxy was only about two billion light years from the matter that would become us. Today, by our calculation using the standard cosmological model, it's about thirty four billion light years away.",
  "vis": {"type": "compare", "left": ["When light left", "≈ 2.2 billion ly away", "280 million years", "after the Big Bang"], "right": ["Today", "≈ 34 billion ly away", "13.5 billion years", "of travel later"], "cols": [VIO, MAG], "strike": False}},
 {"say": "The oldest light of all is the cosmic microwave background, the afterglow of the Big Bang, released about three hundred and eighty thousand years after it began. The gas that glowed was then only around forty million light years away. That same matter is now about forty five billion light years from us. That's the edge. Not a wall. Just the farthest light that has had time to reach us.",
  "vis": {"type": "stretch", "a0": 0.0009, "light": 13.8, "now": 45.3, "src": "Big Bang afterglow", "cmb": True, "caption": "The edge is a horizon in time, not a wall"}},

 # ---------- HORIZONS ----------
 {"say": "And it gets stranger. The universe is expanding, and the expansion is even speeding up. Today the rate is about seventy kilometers per second for every three point two six million light years of distance. Add enough distance, and the stretching outruns light. Beyond roughly fourteen billion light years, galaxies are moving away from us faster than light, right now. That doesn't break relativity. Nothing is racing through space. Space itself is growing.",
  "vis": {"type": "horizons", "show": 1, "caption": "Beyond ~14 billion ly, space recedes faster than light"}},
 {"say": "Here's an embarrassing secret. We don't fully agree on that expansion rate. Measure it from the Big Bang's afterglow, as the Planck satellite did, and you get about sixty seven. Measure it from nearby exploding stars and pulsing stars, as the SH0ES team did with Hubble, and you get about seventy three. Webb has double checked the nearby side, and while teams still debate the details, the gap hasn't gone away. Astronomers call it the Hubble tension, and it might be a clue that something in our picture of the universe is missing.",
  "vis": {"type": "compare", "left": ["Early universe", "≈ 67 km/s/Mpc", "Planck satellite", "Big Bang afterglow"], "right": ["Nearby universe", "≈ 73 km/s/Mpc", "SH0ES team", "Hubble + Webb"], "cols": [[186, 140, 255], [255, 120, 200]], "strike": False}},
 {"say": "So there are really three borders. The observable universe, at about forty six billion light years, holds everything whose light has reached us so far. But there is a much smaller one, the cosmic event horizon, at roughly sixteen and a half billion light years. Light leaving a galaxy beyond it today will never, ever reach us. We can see galaxies out there, as they were in the past. But whatever they are doing now is gone from us forever.",
  "vis": {"type": "horizons", "show": 3, "caption": "Most of what we see, we can never contact"}},

 {"say": "Play that forward. Every year, more distant galaxies slip past that horizon. Physicists Lawrence Krauss and Robert Scherrer worked out that in around a hundred billion years, every galaxy beyond our own local group will have been pushed past that horizon, and later they fade from view completely. By then, the Milky Way and Andromeda will long since have merged into one giant galaxy. Astronomers living there would look out and see a single island of stars in an empty, black universe. They would have no way to discover that the universe is expanding at all. We are lucky to be looking now, while the evidence is still visible.",
  "vis": {"type": "horizons", "show": 3, "fade": True, "caption": "In ~100 billion years, the other galaxies slip past the horizon"}},

 # ---------- HOW MANY ----------
 {"say": "How much is inside that bubble? For years, the headline number was two trillion galaxies. Then in twenty twenty one, NASA's New Horizons spacecraft, far beyond Pluto where the sky is darker, measured how much background light there really is. The verdict: hundreds of billions of galaxies, not two trillion. Still, if you counted one galaxy every second, without sleeping, two hundred billion would take you more than six thousand years.",
  "vis": {"type": "deepfield", "count": "≈ 200,000,000,000+", "caption": "Counting one per second: over 6,000 years"}},

 # ---------- SHRINK IT ----------
 {"say": "Numbers this big stop meaning anything, so let's shrink it. Squeeze the entire observable universe down to the size of Earth.",
  "vis": {"type": "shrink", "rows": 0}},
 {"say": "On that scale, our whole Milky Way would be about fourteen meters across. Roughly a city bus, floating somewhere inside a planet. Andromeda would be a few blocks away, about three hundred and forty meters. Proxima Centauri would sit about half a millimeter from the Sun. And the Sun itself? Smaller than a single atom.",
  "vis": {"type": "shrink", "rows": 4}},

 # ---------- BEYOND THE EDGE ----------
 {"say": "So is that the whole universe? Almost certainly not. The observable universe is only the part we can see, centered on us. Every galaxy has its own bubble. An alien astronomer forty billion light years away sees a completely different edge, and would look at us as the ones at the border.",
  "vis": {"type": "bullets", "title": "The edge is personal", "items": ["Every observer has a bubble", "Each bubble has its own edge", "No center, no wall"], "highlight": 2, "col": VIO}},
 {"say": "What lies past our horizon? The best clue is the shape of space. The Planck satellite measured that space is flat, to within a fraction of a percent. If the universe curves back on itself at all, it must be enormously larger than the part we can see. And if it is perfectly flat, the simplest answer is the most unsettling one. It may go on forever.",
  "vis": {"type": "compare", "left": ["If space curves", "Finite, no edge", "Far bigger than", "our bubble"], "right": ["If perfectly flat", "Possibly infinite", "Galaxies without", "end"], "cols": [VIO, MAG], "strike": False}},

 # ---------- ENDING ----------
 {"say": "So, how big is the universe, really? The part we can see is ninety three billion light years across. The part we could ever reach is far smaller. And the whole thing might have no size at all, because it may never end.",
  "vis": {"type": "scale", "title": "How big is the universe?", "sub": "distance from us (radius) — each answer is a different border", "points": [["Faster than light", "14 bn ly"], ["Ever reachable", "16.5 bn ly"], ["Observable", "46 bn ly"], ["Whole universe", "∞ ?"]], "col": VIO}},
 {"say": "Next time, we stop looking and start falling. What happens if you fall into a black hole? Spoiler: it depends on which black hole you pick. Subscribe to Cosmic Scale so you don't miss it. See you out there.",
  "vis": {"type": "title", "title": "Next:", "sub": "What Happens If You Fall Into a Black Hole?", "brand": True, "subcol": MAG}},
]
