# EP06 — What If Earth Stopped Spinning?
# Structure NEW: "three ways to stop a planet" — (1) in one second (violent) -> re-engage 1: the pole paradox
# -> (2) over a few decades (gentle): oceans run to the poles, equatorial megacontinent, a day lasts a year, no hurricanes, Venus warning
# -> re-engage 2 / biggest scale: (3) the real stop — Earth IS slowing (18-h days 1.4 Gyr ago, 23.5 h for the dinosaurs' last era),
# Moon receding, leap seconds -> it never finishes before the Sun dies -> payoff -> EP07 (neutron star teaspoon).
# Palette teal / amber. New scenes: spinglobe (globe + speed by latitude, top view rings), pendulum, fling, bulge, yearday, dayclock.
# Own calculations (Python): equator speed 2*pi*6378.137 km / 23.934 h = 1,674 km/h (465 m/s = Mach 1.36); New York (40.7°) 1,269;
# London (51.5°) 1,042; spin energy 0.5*I*w^2 = 2.14e29 J (I = 8.04e37 kg m^2) = 9.3 min of the Sun's output (3.828e26 W);
# centrifugal effect at the equator = 0.35% of g; 1,670 / 408 = 4.1x the record gust.
TITLE = "What If Earth Stopped Spinning?"
TEAL = [46, 230, 197]
AMBER = [255, 170, 60]
SEA = [60, 140, 255]

SCENES = [
 # ---------- HOOK ----------
 {"say": "If Earth stopped spinning right now, you wouldn't stop with it. You'd keep going, east, at up to sixteen hundred and seventy kilometers an hour. So would the air around you. So would the oceans, the cars, the buildings, anything not welded to solid rock. And here's the strange part. The safest place on the whole planet would be a spot where almost nobody lives.",
  "vis": {"type": "fling", "speed": 1670, "stop_at": 0.12, "head": "Earth stops. You don't.", "label": "you, still moving east"}},
 {"say": "So let's stop the Earth three different ways. In one second. Over a few decades. And the way it's actually happening, right now, while you watch this. By the end, you'll know where the oceans would go, why a single day would last an entire year, and why your own days are already getting longer.",
  "vis": {"type": "bullets", "title": "Three ways to stop a planet", "items": ["1. In one second", "2. Over a few decades", "3. The way it's really happening"], "col": TEAL}},
 {"say": "What If Earth Stopped Spinning?",
  "vis": {"type": "title", "title": "What If Earth\nStopped Spinning?", "sub": "COSMIC SCALE", "brand": True, "subcol": TEAL}},

 # ---------- HOW FAST ARE WE MOVING ----------
 {"say": "First, how fast are we moving? Earth turns once every twenty three hours and fifty six minutes. At the equator, the ground covers about forty thousand kilometers in that time. That's roughly sixteen hundred and seventy kilometers an hour. Move away from the equator and the circle you ride on gets smaller, so you go slower. New York, about twelve hundred and seventy. London, about a thousand. At the North Pole, you just turn in place. And you feel none of it, for the same reason you don't feel a smooth flight. Speed itself is invisible. Only changes in speed hurt.",
  "vis": {"type": "spinglobe", "head": "How fast is the ground moving?", "marks": [[0, "Equator  1,670 km/h"], [40.7, "New York  ≈ 1,270"], [51.5, "London  ≈ 1,040"], [90, "North Pole  0"]]}},

 {"say": "So how do we even know we're spinning, if we can't feel it? In eighteen fifty one, Léon Foucault hung a heavy iron ball from a sixty seven meter wire, under the dome of the Panthéon in Paris, and let it swing. Hour after hour, the line of the swing slowly turned, about eleven degrees every hour. The pendulum wasn't turning. The floor of Paris was turning underneath it. At the North Pole, the swing would turn a full circle every day. At the equator, it wouldn't turn at all.",
  "vis": {"type": "pendulum", "head": "Foucault's pendulum, Paris 1851", "notes": [["Paris", "≈ 11° per hour"], ["North Pole", "360° per day"], ["Equator", "0°"]]}},

 # ---------- STOP 1: ONE SECOND ----------
 {"say": "Stop number one. The planet halts in a single second. The rock stops. Everything resting on it doesn't. At the equator, you would be launched east at about four hundred and sixty five meters per second. That's faster than the speed of sound. Cars, trees, people, loose soil, roof tiles, all sliding and tumbling in the same direction, at the same moment, everywhere on Earth.",
  "vis": {"type": "fling", "speed": 1670, "stop_at": 0.05, "head": "Stop #1: in one second", "label": "465 m/s — faster than sound", "debris": True}},
 {"say": "Then the air arrives. The atmosphere doesn't stop either, so near the equator it becomes a wind of up to sixteen hundred and seventy kilometers an hour. For comparison, the strongest gust ever measured on Earth was four hundred and eight kilometers an hour, recorded on Barrow Island, Australia, during Cyclone Olivia in nineteen ninety six. The stop wind would be about four times faster, scouring the ground down to bedrock.",
  "vis": {"type": "bars", "title": "Wind speed (km/h)", "items": [["Category 5 hurricane", 252, "#9FB4D8"], ["Record gust (1996)", 408, "#FFAA3C"], ["The stop wind", 1670, "#2EE6C5"]], "suffix": ""}},
 {"say": "The oceans keep moving too, piling up against every coast that faces east, as walls of water bigger than anything in recorded history. And all that motion has to go somewhere. By our calculation, the energy stored in Earth's spin is about two times ten to the twenty nine joules. That's as much energy as the entire Sun puts out in about nine minutes. Stop the planet in one second, and much of that turns into heat, through friction, crushing, and turbulence.",
  "vis": {"type": "bignumber", "from": 0, "to": 9.3, "decimals": 1, "suffix": " min", "col": AMBER, "caption": "Energy of Earth's spin ≈ the whole Sun's output for 9 minutes (our calculation)"}},

 # ---------- RE-ENGAGE 1: THE POLE PARADOX ----------  # REENGAJE (~3:00)
 {"say": "Now the paradox. Look at Earth from above the North Pole. The farther from the center, the faster the ground is moving. But right at the poles, it's barely moving at all. Stand exactly on the pole, and when the planet stops, you'd simply stop turning in place. No launch. The worst second in the history of the planet, and the safest spots are two patches of ice where almost nobody lives. The few dozen people wintering at the South Pole research station would survive the first second. The global storm would reach them later.",
  "vis": {"type": "spinglobe", "top": True, "head": "Seen from above the pole", "marks": [[0, "1,670 km/h"], [45, "≈ 1,180"], [70, "≈ 570"], [90, "0  ← safe"]]}},

 # ---------- STOP 2: OVER DECADES ----------
 {"say": "Stop number two is gentle. The spin fades over a few decades, so slowly that nothing gets thrown. You'd survive it. You just might not recognize the planet afterward. Because Earth isn't a perfect ball. Its spin makes it bulge around the middle. The equator sits about twenty one kilometers farther from the center than the poles do. And the oceans bulge with it. The spin holds up a hump of water around the equator, roughly eight kilometers high.",
  "vis": {"type": "bulge", "phase": 0, "head": "Spin makes Earth bulge", "notes": ["equator ≈ 21 km farther from the center", "ocean hump ≈ 8 km high"]}},
 {"say": "Take the spin away, and that hump collapses. The water runs downhill, toward the poles. In a well known simulation by Witold Fraczek at the mapping company Esri, the oceans end up split into two great polar seas, one in the north and one in the south. And around the middle of the planet, a single giant continent rises out of the water, wrapping all the way around the Earth. Along its spine, Chimborazo, in Ecuador, would tower more than thirteen kilometers above the new sea level. And you? Standing on the equator, you'd weigh about a third of a percent more, because the spin that used to fling you outward, ever so slightly, would be gone.",
  "vis": {"type": "bulge", "phase": 1, "head": "No spin: the oceans run to the poles", "notes": ["two polar oceans", "one ring-shaped continent", "Chimborazo ≈ 13.6 km above the sea"]}},
 {"say": "Then there's the Sun. Today, a day lasts twenty four hours because we spin. Stop the spin, and the only thing that changes which side of Earth faces the Sun is our trip around it. One day would last one whole year. About six months of daylight, followed by six months of night.",
  "vis": {"type": "yearday", "head": "One day = one year"}},
 {"say": "The day side would bake under a Sun that never sets, while the night side freezes through months of darkness. And the weather would be rebuilt from scratch. Today, Earth's spin is what twists storms into spirals. It's why hurricanes almost never form within about five degrees of the equator, where that twisting effect fades away. On a still Earth, there would be no hurricanes at all. Instead, air would flow in giant loops, from the hot day side to the frozen night side.",
  "vis": {"type": "compare", "left": ["DAY SIDE", "Sun never sets", "≈ 6 months of light", "baking heat"], "right": ["NIGHT SIDE", "no sunrise for months", "deep freeze", "no hurricanes anywhere"], "cols": [AMBER, SEA], "strike": False}},
 {"say": "And there's one more risk that scientists aren't sure about. Earth's magnetic field comes from molten iron churning in the outer core, and the planet's spin helps organize that churning. Venus is almost the same size as Earth, but it turns so slowly that one rotation takes two hundred and forty three Earth days. That's longer than its entire year. And Venus has no global magnetic field of its own. Slow spin may not be the whole reason. But without a magnetic shield, the solar wind would have a much easier time stripping away our air.",
  "vis": {"type": "bars", "title": "How long does it take?", "items": [["Earth: one turn", 1, "#2EE6C5"], ["Venus: one orbit", 225, "#FFAA3C"], ["Venus: one turn", 243, "#FF7A5C"]], "suffix": " days"}},

 # ---------- RE-ENGAGE 2: THE REAL STOP ----------  # REENGAJE (~6:00)
 {"say": "Which brings us to stop number three. The real one. Earth is slowing down right now. The Moon's gravity raises tides, and the tides drag on the spinning planet like a brake. Days used to be shorter. A seventy million year old fossil clam, studied in twenty twenty, laid down daily growth rings showing that a year back then had about three hundred and seventy two days. Each day lasted about twenty three and a half hours. And ancient rock layers suggest that one point four billion years ago, a day lasted just over eighteen hours.",
  "vis": {"type": "dayclock", "head": "Earth's day is getting longer", "items": [["1.4 billion years ago", 18.0], ["70 million years ago", 23.5], ["Today", 24.0]]}},
 {"say": "The same tidal brake is pushing the Moon away from us, by about three point eight centimeters every year. That's roughly as fast as your fingernails grow. It's all very slow. Today, our days are getting longer by only a couple of thousandths of a second per century.",
  "vis": {"type": "bignumber", "from": 0, "to": 3.8, "decimals": 1, "suffix": " cm", "col": TEAL, "caption": "the Moon drifts away about 3.8 cm every year"}},
 {"say": "And it isn't perfectly smooth. Since nineteen seventy two, timekeepers have added twenty seven leap seconds to keep our clocks in step with the planet. Lately, Earth has actually been spinning slightly faster. A twenty twenty four study in Nature found that melting polar ice is slowing the spin back down, just enough to delay what could become the first negative leap second ever, now expected around twenty twenty nine.",
  "vis": {"type": "bullets", "title": "Earth's clock wobbles", "items": ["27 leap seconds added since 1972", "lately: spinning slightly faster", "melting ice: slowing it back down", "first negative leap second? ≈ 2029"], "col": AMBER, "highlight": 3}},
 {"say": "So will Earth ever actually stop? The Moon already lost this battle. Earth's tides braked its spin long ago, which is why the Moon always shows us the same face. But for Earth, it won't happen in any future that matters. For the Moon to brake us until one face of Earth always points at it, would take tens of billions of years. Long before that, in about five billion years, the Sun swells into a red giant. Earth will still be turning when the Sun runs out of time.",
  "vis": {"type": "spinglobe", "slow": True, "head": "Will it ever stop?", "marks": [[0, "still turning in 5 billion years"]]}},

 # ---------- PAYOFF + NEXT ----------
 {"say": "So, what if Earth stopped spinning? In one second, it's the worst day in the planet's history, unless you happen to be standing on a pole. Over a few decades, the oceans run to the poles and a single day lasts a year. And in reality, it's happening at the speed of a growing fingernail. Our planet turns once a day. But out there are dead stars that spin more than seven hundred times every second. They're so dense that a single teaspoon of one would weigh as much as a mountain. How is that even possible? That's next.",
  "vis": {"type": "title", "title": "Next:\nA Teaspoon That Weighs a Mountain", "sub": "COSMIC SCALE", "brand": False, "subcol": TEAL}},
]

SOURCES = [
 "Esri ArcUser, Witold Fraczek, \"What Would Happen If Earth Stopped Spinning?\" (2010): equatorial bulge about 21.4 km, ocean bulge about 8 km at the equator, two polar oceans and an equatorial megacontinent, Chimborazo about 13,615 m above the new sea level, a day would last a year",
 "Astronomy magazine (Feb 2026), \"What happens if Earth stops rotating?\": equator moves at about 1,668 km/h; winds above 1,600 km/h in a sudden stop; leap seconds and a possible negative leap second in 2029",
 "World Meteorological Organization: highest recorded surface wind gust 408 km/h, Barrow Island, Australia, Tropical Cyclone Olivia, 10 April 1996",
 "NOAA / National Hurricane Center: tropical cyclones rarely form within about 5 degrees of the equator, where the Coriolis effect is too weak",
 "NASA Science, Venus facts: one rotation takes 243 Earth days, longer than its 225-day year; Venus has no intrinsic global magnetic field",
 "Winter et al. (2020), Paleoceanography and Paleoclimatology (AGU): 70-million-year-old rudist clam, 372 days per year, days about 23.5 hours",
 "Meyers and Malinverno (2018), PNAS (University of Wisconsin–Madison): 1.4 billion years ago a day lasted just over 18 hours; the Moon recedes about 3.82 cm per year",
 "Stephenson et al. (2016), Proceedings of the Royal Society A: length of day increasing by about 1.8 milliseconds per century",
 "Agnew (2024), Nature: melting polar ice is slowing Earth's rotation, delaying a possible negative leap second to about 2029; 27 leap seconds added since 1972 (IERS)",
 "NASA: the Sun will become a red giant in about 5 billion years; neutron stars: a teaspoon would weigh about as much as a mountain; fastest known pulsar spins 716 times per second",
 "Encyclopaedia Britannica, Foucault pendulum: Panthéon, Paris, 1851, 67 m wire; at Paris the swing plane turns about 11 degrees per hour; a full turn per day at the poles, none at the equator",
 "Own calculations (Python): rotation speed by latitude, spin energy (about 2.1e29 J, about 9 minutes of solar output), wind ratio",
]
