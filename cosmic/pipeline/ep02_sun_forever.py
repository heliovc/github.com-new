# EP02 — What If the Sun Disappeared Forever?
# Structure: "mission clock" (T+0 → millions of years), cold palette. New scene types: clock, escape, sky, thermo, energy, ocean, galaxy, planetsdark
TITLE = "What If the Sun Disappeared Forever?"
ICE = [170, 225, 255]

SCENES = [
 # ---------- HOOK ----------
 {"say": "Last time, the Sun vanished for one single second, and Earth barely noticed. Today, there is no coming back. The Sun disappears, and it never returns. No light. No heat. No gravity holding us in place. How long would we last? Days? Years? The answer splits into two very different stories. One on the surface, and one deep underground.",
  "vis": {"type": "sun", "forever": True, "vanish_at": 0.42, "label": "FOREVER", "caption": "No light. No heat. No gravity."}},
 {"say": "Let's start the clock.",
  "vis": {"type": "title", "title": "What If the Sun\nDisappeared Forever?", "sub": "COSMIC SCALE", "brand": True}},

 # ---------- T+0 ----------
 {"say": "Time zero. And for the first eight minutes and twenty seconds, absolutely nothing changes. The sunlight reaching your eyes left the Sun eight minutes ago, and changes in gravity travel at the very same speed. So the light already in flight is the last sunlight Earth will ever receive.",
  "vis": {"type": "clock", "idx": 0, "stamp": "T + 0", "sub": "Nothing changes. Yet."}},

 # ---------- T+8 min ----------
 {"say": "Then the final photons arrive. And the lights go out.",
  "vis": {"type": "clock", "idx": 1, "stamp": "T + 8 MIN", "sub": "The last sunlight lands"}},
 {"say": "On the day side, the blue sky drains to black almost instantly. A blue sky is just sunlight scattered by the air. With no sunlight, there is nothing to scatter. The stars come out at noon. Now look at the Moon. It has no light of its own, it only reflects the Sun. About a second later, the Moon goes dark too. A black circle you can only find because it hides the stars behind it.",
  "vis": {"type": "sky", "moon": True, "start": 0.08, "speed": 0.3, "moon_off": 0.62, "caption": "Stars at noon. A black Moon."}},

 # ---------- gravity ----------
 {"say": "At the same moment, gravity lets go. Earth was racing along at almost thirty kilometers per second, its path constantly bent around the Sun. With nothing left to bend it, Earth does the simplest thing possible. It goes straight. In a straight line, at thirty kilometers per second, forever.",
  "vis": {"type": "escape", "au": 1.2, "time": "first weeks", "caption": "No pull, no curve: a straight line"}},
 {"say": "After one year of coasting, Earth would be about nine hundred and fifty million kilometers from the spot where the Sun used to be. That is farther out than Jupiter's orbit. And the Moon? It comes with us. The Moon is held by Earth's gravity, not the Sun's, so the two keep traveling together, a tiny dark pair.",
  "vis": {"type": "escape", "au": 6.28, "jupiter": True, "time": "after 1 year", "caption": "The Moon stays with Earth"}},
 {"say": "Every other planet does the same thing. Mercury, Venus, Mars, Jupiter. Each one flies off along its own straight line, in its own direction. The solar system doesn't collapse inward. It comes apart, like a spinning carnival ride whose ropes are all cut at once.",
  "vis": {"type": "planetsdark", "caption": "The solar system doesn't collapse. It comes apart."}},
 {"say": "Then the planets begin to vanish from our sky. Venus, the brightest point of light at night, only shines with reflected sunlight. It fades away. Then Mars, then Jupiter, then Saturn, as their last reflected light finishes the trip back to us. Within about three hours, every planet is gone, and only the distant stars remain.",
  "vis": {"type": "stars", "caption": "One by one, the planets fade from our sky"}},
 {"say": "Strangely, days don't end. Earth keeps spinning once every twenty four hours, because nothing is there to stop it. But a day no longer means anything. No sunrise, no sunset. Just the same stars wheeling overhead, again and again, in a sky that is always night.",
  "vis": {"type": "sky", "night_only": True, "moon": True, "moon_off": -1, "caption": "Earth still spins. Every hour is night."}},
 {"say": "Here is an effect almost nobody thinks about. The tides change. The Moon raises most of our ocean tides, but the Sun helps a lot. According to NOAA, the Sun's tide-raising force is about forty six percent of the Moon's. Without it, tides get weaker, and the extra high spring tides around full moon and new moon simply stop.",
  "vis": {"type": "bignumber", "from": 0, "to": 46, "suffix": "%", "col": ICE, "caption": "Sun's tidal force compared with the Moon's (NOAA)"}},

 # ---------- T+1 day ----------
 {"say": "Now the cold begins. Our air holds surprisingly little heat. Caltech planetary scientist David Stevenson notes that the atmosphere's warmth only matters for a few days. After that, the ground and the oceans carry the load, and they leak heat into space every second, with nothing coming back in.",
  "vis": {"type": "clock", "idx": 2, "stamp": "T + 1 DAY", "sub": "The cold begins"}},

 # ---------- T+1 week ----------
 {"say": "One week in.",
  "vis": {"type": "clock", "idx": 3, "stamp": "T + 1 WEEK", "sub": "Freezer planet"}},
 {"say": "Today, the average temperature at Earth's surface is about fifteen degrees Celsius. Within roughly a week of darkness, it falls below minus eighteen. That is zero degrees Fahrenheit. Colder than your home freezer, everywhere on the planet, including the tropics. The surface of the sea begins to freeze over.",
  "vis": {"type": "thermo", "from": 15, "to": -18, "marks": [[15, "Today: about 15 °C"], [-18, "1 week: below −18 °C"]], "caption": "Colder than a freezer, even at the equator"}},
 {"say": "Life feels it immediately. Photosynthesis, the process that feeds almost every food chain on the planet, stops the moment the light is gone. Most plants would die within a few weeks. Strangely, the giants last longest. Large trees store so much sugar that they could hang on for decades, frozen and dormant.",
  "vis": {"type": "bullets", "title": "Life on the surface", "items": ["Photosynthesis stops instantly", "Most plants die within weeks", "Big trees: frozen for decades"], "highlight": 2, "col": ICE}},

 # ---------- T+1 year ----------
 {"say": "One year.",
  "vis": {"type": "clock", "idx": 4, "stamp": "T + 1 YEAR", "sub": "A world without seasons"}},
 {"say": "After a year, Stevenson estimates the surface would be below two hundred kelvin. That's about minus seventy three degrees Celsius, or minus one hundred Fahrenheit. The cold of a deep Antarctic winter night, but everywhere, all year round, with no summer ever coming back.",
  "vis": {"type": "thermo", "from": -18, "to": -73, "marks": [[15, "Today: about 15 °C"], [-18, "1 week: below −18 °C"], [-73, "1 year: below −73 °C"]], "caption": "Below 200 kelvin after one year"}},

 # ---------- the ocean twist ----------
 {"say": "But here is the twist. The oceans don't freeze solid. Not for a very, very long time. Ice floats, and ice is a good insulator. As the frozen lid gets thicker, it works like a blanket over the water underneath. And down on the sea floor, hydrothermal vents keep pumping out hot, mineral rich water, heated by Earth itself. The microbes living there feed on chemical energy, not on sunlight. Some of them could keep going for a very long time.",
  "vis": {"type": "ocean", "ice0": 12, "ice1": 140, "air": "−70 °C", "ice_lab": "thickening every year", "caption": "Ice on top works like a blanket"}},

 # ---------- Earth's own heat ----------
 {"say": "So where does that deep heat come from? Earth has a furnace of its own. Heat left over from its formation, plus radioactive elements slowly decaying in the rock. It leaks out through the crust at about forty seven terawatts. Sounds enormous, until you compare it with sunlight. The sunlight hitting Earth delivers about one hundred and seventy three thousand terawatts. Earth's own heat is roughly one part in three thousand seven hundred. Without the Sun, that tiny red square is everything we have.",
  "vis": {"type": "energy", "ratio": 3690, "a_val": "≈ 173,000 TW", "b_val": "≈ 47 TW (shown 6× zoomed)", "caption": "Earth's inner heat ≈ 1/3,700 of sunlight"}},

 # ---------- millions of years ----------
 {"say": "Now jump ahead millions of years.",
  "vis": {"type": "clock", "idx": 6, "stamp": "MILLIONS OF YEARS", "sub": "The final temperature"}},
 {"say": "The surface finally settles where that faint trickle of inner heat balances what escapes to space. Stevenson puts it around thirty kelvin. That's about minus two hundred and forty degrees Celsius. Long before that, the air itself gives up. Nitrogen freezes at minus two hundred and ten degrees, oxygen a little colder. The atmosphere falls to the ground as snow, burying the planet under a frozen layer of what used to be its sky.",
  "vis": {"type": "thermo", "from": -73, "to": -243, "marks": [[15, "Today: about 15 °C"], [-73, "1 year: below −73 °C"], [-210, "Nitrogen freezes: air snows down"], [-243, "Final: about 30 kelvin"]], "label": "average surface", "caption": "The sky itself freezes and falls"}},

 # ---------- humans ----------
 {"say": "And people? On the surface, survival would be measured in years at most. But we are a stubborn species. Iceland already heats almost nine out of ten homes with geothermal energy. Nuclear reactors don't need sunlight. Stevenson suggests that a small number of people could survive for a very long time by moving miles underground, where the rock stays warm. Life would look less like a city, and more like a submarine. Food would come from greenhouses lit by lamps, powered by the planet's own heat. Every calorie would have to be earned the hard way.",
  "vis": {"type": "bullets", "title": "How humans could hold on", "items": ["Geothermal heat, like Iceland", "Nuclear power, no sunlight needed", "Habitats miles underground"], "highlight": -1, "col": [255, 140, 60]}},

 {"say": "And far away, the Sun would still be shining for a while. Its last light keeps racing outward. Neptune sees a normal Sun for four more hours. Voyager one, a full day. Anyone watching from Proxima Centauri would see our Sun for more than four years. From the Andromeda galaxy, for two and a half million years. A star that no longer exists, still glowing in someone else's sky.",
  "vis": {"type": "scale", "title": "Who still sees our Sun shining?", "sub": "its last light keeps traveling outward", "points": [["Earth", "8 min"], ["Neptune", "4 hours"], ["Voyager 1", "1 day"], ["Proxima Centauri", "4.2 years"], ["Andromeda", "2.5 million years"]]}},
 # ---------- galaxy ----------
 {"say": "Meanwhile, Earth keeps moving through the galaxy. It still carries the Sun's old speed around the Milky Way, so it would still complete a lap roughly every two hundred and thirty million years. Just alone. And it wouldn't even be unusual. NASA researchers estimate our galaxy may hold about twenty times more rogue planets than stars. Worlds drifting in the dark with no sun at all. Earth would simply become one more of them.",
  "vis": {"type": "galaxy", "rogues": True, "label": "Earth — now a rogue planet", "caption": "Possibly 20× more rogue planets than stars (NASA)"}},
 {"say": "Could we ever reach another star? Earth's speed is fixed at about thirty kilometers per second. At that pace, crossing even the four point two light years to Proxima Centauri would take more than forty two thousand years. And space is so empty that Earth would almost certainly never pass close to any star at all.",
  "vis": {"type": "bignumber", "from": 0, "to": 42700, "suffix": " years", "col": ICE, "caption": "to cover 4.2 light-years at 30 km/s"}},

 # ---------- ending ----------
 {"say": "So, let's put it all together. Not instant darkness, but eight more minutes of an ordinary day. Earth doesn't fall into anything, it just goes straight. And life doesn't end in a single moment. It retreats. From the surface, to the ocean floor, to the warm rock deep below.",
  "vis": {"type": "compare", "left": ["Myth", "Instant darkness", "Earth falls into the void", "Everything dies at once"], "right": ["Reality", "8 min 20 s of normal", "Straight line at 30 km/s", "Deep life holds on"]}},
 {"say": "We think of the Sun as a lamp. It's really an anchor, holding a whole family of worlds together. Take it away, and everything we know drifts apart into the dark.",
  "vis": {"type": "title", "title": "Not a lamp.\nAn anchor.", "sub": "Remove it and everything drifts apart", "subcol": ICE}},
 {"say": "Next time, we zoom all the way out. How big is the universe, really? The answer is bigger, and stranger, than the number you've probably heard. Subscribe to Cosmic Scale so you don't miss it. See you out there.",
  "vis": {"type": "title", "title": "Next:", "sub": "How Big Is the Universe, Really?", "brand": True}},
]
