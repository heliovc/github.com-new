# EP13 — How Long Would It Take to Travel to Every Planet?
# Structure NEW: "departure board" — hook (a car that left when the Great Pyramid was being built would still be driving to Neptune) ->
# the rules (3 vehicles: a car at 100 km/h nonstop, a jet at 900 km/h, Parker Solar Probe's record 692,000 km/h; distances = closest
# approach) -> one "gate" per destination, the board flips row by row: Moon (warm-up), Venus, Mars, Mercury (paradox: hardest to reach),
# Jupiter, Saturn, Uranus + Neptune -> the full board + light -> twist: you can't fly straight (transfer orbits, slingshots, the Grand Tour)
# -> recap -> EP14. Palette road amber / board teal / ticket coral on a plum tint.
# New scenes: departures (split-flap board), roadtrip (highway into space: odometer, calendar, generations), transfer (top-down orbits,
# curved path + day counter, ghost straight line), slingshot (flyby that adds or removes speed, speedometer).
# Own calculations (Python): distances = NASA Planetary Fact Sheet minimum distance from Earth (10^6 km): Venus 38.2, Mars 54.6,
# Mercury 77.3, Jupiter 588.5, Saturn 1,195.5, Uranus 2,581.9, Neptune 4,305.9; Moon 384,400 km (mean). Car 100 km/h: Moon 160 days,
# Venus 43.6 y, Mars 62.3 y, Mercury 88.2 y, Jupiter 671 y, Saturn 1,364 y, Uranus 2,945 y, Neptune 4,912 y; Sun 171 y. Jet 900 km/h:
# Moon 18 d, Mars 6.9 y, Neptune 546 y. Parker 692,000 km/h: Mars 3.3 d, Jupiter 35 d, Neptune 259 d. Light: Neptune 4.0 h.
# Real trips (launch -> arrival): Venus Express 153 d; Perseverance 203 d; MESSENGER 6.6 y; Juno 4.9 y; Cassini 6.7 y; Voyager 2 8.4 y
# (Uranus) and 12.0 y (Neptune); BepiColombo 8.1 y (Mercury orbit insertion planned for November 2026).
TITLE = "How Long to Reach Every Planet?"
ROAD = [255, 170, 60]
BOARD = [60, 225, 200]
TICKET = [255, 120, 110]

SCENES = [
 # ---------- HOOK ----------
 {"say": "If you had started driving to Neptune when the Great Pyramid was being built, you would still be on the road today, with about four hundred years left to drive.",
  "vis": {"type": "roadtrip", "dest": "Neptune", "km": 4305.9e6, "kmh": 100, "years": 4912, "head": "Road trip to Neptune"}},
 {"say": "Today we're buying tickets to every planet in the solar system. Three ways to travel. One departure board. And one destination that is much harder to reach than it looks.",
  "vis": {"type": "departures", "rows": 0, "head": "DEPARTURES"}},
 {"say": "Before we start, make a guess. Driving nonstop to Mars, how long would it take? A month? A year? A lifetime? Keep your guess in mind, because we reach Mars at gate two.",
  "vis": {"type": "roadtrip", "dest": "Mars", "km": 54.6e6, "kmh": 100, "years": 62.3, "hide": True, "head": "Guess: Mars by car?"}},
 {"say": "How Long Would It Take to Travel to Every Planet?",
  "vis": {"type": "title", "title": "How Long to Reach\nEvery Planet?", "sub": "COSMIC SCALE", "brand": True, "subcol": BOARD}},

 # ---------- RULES ----------
 {"say": "First, the rules. Vehicle one is a car, driving at a hundred kilometers per hour, with no stops. No sleep, no gas stations, no traffic. Vehicle two is a passenger jet, at about nine hundred kilometers per hour. Vehicle three is the fastest machine humans have ever built, NASA's Parker Solar Probe, at its record speed of about six hundred ninety two thousand kilometers per hour.",
  "vis": {"type": "compare", "left": ["THE VEHICLES", "car: 100 km/h", "jet: 900 km/h", "Parker: 692,000 km/h"], "right": ["THE ROUTE", "straight line", "no stops", "planet at its closest"], "cols": [ROAD, BOARD], "strike": False}},
 {"say": "And we'll be generous. We'll leave on the day each planet comes closest to Earth, and we'll travel in a perfectly straight line. Real spacecraft can't do that, and we'll see why at the end. For now, the doors are closing.",
  "vis": {"type": "transfer", "target": "Mars", "days": 203, "ghost": True, "straight": True, "head": "The rules: straight line, closest approach"}},

 # ---------- MOON ----------
 {"say": "Gate zero. A warm-up. The Moon.",
  "vis": {"type": "departures", "rows": 1, "hl": 0}},
 {"say": "The Moon is about three hundred eighty four thousand kilometers away. By car, that's a hundred sixty days of nonstop driving, about five months. By jet, eighteen days. If you walked, it would take almost nine years. Our fastest probe would be there in about half an hour. The Apollo astronauts, for comparison, needed about three days.",
  "vis": {"type": "roadtrip", "dest": "Moon", "km": 384400, "kmh": 100, "days": 160, "head": "Gate 0: the Moon by car"}},

 # ---------- VENUS ----------
 {"say": "Gate one. Venus, the planet that comes closest to us.",
  "vis": {"type": "departures", "rows": 2, "hl": 1}},
 {"say": "At its closest, Venus is about thirty eight million kilometers away. That's a hundred times farther than the Moon. By car, forty four years of nonstop driving. Leave at twenty, arrive at sixty four. By jet, almost five years. Parker would need just over two days. The real record is slower. The European probe Venus Express took about five months to get there and slip into orbit.",
  "vis": {"type": "departures", "rows": 2, "hl": 1, "detail": "real trip: Venus Express, 153 days (ESA)"}},

 # ---------- MARS ----------
 {"say": "Gate two. Mars.",
  "vis": {"type": "departures", "rows": 3, "hl": 2}},
 {"say": "Mars at its closest is about fifty five million kilometers away. By car, sixty two years. Most people who start that drive would not live to park. By jet, about seven years. Parker, about three days. But NASA's Perseverance rover took two hundred and three days, almost seven months.",
  "vis": {"type": "roadtrip", "dest": "Mars", "km": 54.6e6, "kmh": 100, "years": 62.3, "head": "Gate 2: Mars by car"}},
 {"say": "Why so slow? Because a spacecraft doesn't drive toward Mars. It's thrown into a long curve around the Sun, timed so that Mars arrives at the same spot at the same moment. Launch a few weeks late, and you wait about two years for the next window.",
  "vis": {"type": "transfer", "target": "Mars", "days": 203, "head": "Perseverance: 203 days on a curve", "caption": "path drawn for illustration; launch 30 Jul 2020, landing 18 Feb 2021 (NASA)"}},
 {"say": "And the curve is long. Perseverance didn't cover fifty five million kilometers. By NASA's count, it traveled about four hundred seventy two million kilometers to reach Mars, more than eight times the straight-line distance. In space, the shortest path in time is almost never the shortest path in distance.",
  "vis": {"type": "bignumber", "from": 0, "to": 472, "suffix": " million km", "col": BOARD, "caption": "distance Perseverance actually traveled to Mars (NASA)"}},

 # ---------- MERCURY ----------
 {"say": "Gate three. Mercury. This is where it gets strange.",
  "vis": {"type": "departures", "rows": 4, "hl": 3}},
 {"say": "Mercury is closer to us than Jupiter by a factor of almost eight. By car, it's eighty eight years. By jet, ten. So you'd expect it to be quick. It isn't. NASA's MESSENGER probe needed six and a half years to get into orbit around Mercury. Longer than it took Juno to reach Jupiter.",
  "vis": {"type": "compare", "left": ["MERCURY", "77 million km", "MESSENGER", "6.6 years"], "right": ["JUPITER", "588 million km", "Juno", "4.9 years"], "cols": [TICKET, ROAD], "strike": False}},
 {"say": "Here's the catch. Earth is racing around the Sun at about thirty kilometers per second, and so is everything we launch. To reach Mercury, you're falling toward the Sun, and you speed up the whole way down. Arrive like that, and you fly straight past. So MESSENGER spent years braking, swinging past Earth once, Venus twice and Mercury three times, using each planet's gravity to shed speed.",
  "vis": {"type": "slingshot", "mode": "brake", "head": "Falling toward the Sun: you must brake"}},
 {"say": "And it's still happening. The European and Japanese mission BepiColombo launched in twenty eighteen. It's due to slip into orbit around Mercury this month, eight years after leaving Earth. Nine flybys, for a planet that, on average, is actually the closest planet to Earth.",
  "vis": {"type": "bignumber", "from": 0, "to": 8.1, "decimals": 1, "suffix": " years", "col": TICKET, "caption": "BepiColombo: launched Oct 2018, Mercury orbit insertion planned Nov 2026 (ESA)"}},
 {"say": "Yes, on average. Venus comes closest, but it also spends long stretches on the far side of the Sun. Mercury never strays far from the Sun, so averaged over time, it stays nearer. In fact, according to a twenty nineteen analysis in Physics Today, Mercury is the closest planet, on average, to every other planet. Even Neptune.",
  "vis": {"type": "transfer", "target": "Mercury", "days": 2420, "avg": True, "head": "On average, Mercury is our closest planet", "caption": "Stockman, Monroe & Cordner, Physics Today (2019)"}},

 # ---------- JUPITER ----------
 {"say": "Gate four. Jupiter. Now the board starts to look ridiculous.",
  "vis": {"type": "departures", "rows": 5, "hl": 4}},
 {"say": "Five hundred eighty eight million kilometers at its closest. By car, six hundred seventy one years. A family would need about twenty generations behind the wheel. By jet, seventy five years, a whole human life. Parker, thirty five days. Juno did it in just under five years, with an extra swing past Earth to pick up speed.",
  "vis": {"type": "roadtrip", "dest": "Jupiter", "km": 588.5e6, "kmh": 100, "years": 671, "gens": True, "head": "Gate 4: Jupiter by car"}},

 # ---------- SATURN ----------
 {"say": "Gate five. Saturn. One point two billion kilometers.",
  "vis": {"type": "departures", "rows": 6, "hl": 5}},
 {"say": "By car, about thirteen hundred and sixty years. If you had left in the year six hundred sixty, you'd be pulling up about now. By jet, a hundred and fifty years. The Cassini spacecraft took almost seven years, bouncing off Venus twice, Earth once, and Jupiter once on the way. Even light needs more than an hour to make that trip.",
  "vis": {"type": "slingshot", "mode": "boost", "planet": "Jupiter", "head": "Cassini: four gravity assists to Saturn"}},

 # ---------- URANUS + NEPTUNE ----------
 {"say": "Gates six and seven. Uranus and Neptune. Only one spacecraft has ever visited either of them.",
  "vis": {"type": "departures", "rows": 8, "hl": 7}},
 {"say": "Uranus is two point six billion kilometers away, nearly three thousand years by car. Neptune, at four point three billion kilometers, is almost five thousand years by car, and about five hundred and fifty years by jet. Even our record-breaking Parker Solar Probe would need about eight and a half months.",
  "vis": {"type": "roadtrip", "dest": "Neptune", "km": 4305.9e6, "kmh": 100, "years": 4912, "gens": True, "head": "Gate 7: Neptune by car"}},
 {"say": "The one spacecraft that made it is Voyager two. It reached Uranus eight and a half years after launch, and Neptune after twelve. It only managed it because the giant planets had lined up in a pattern that happens about once every hundred and seventy five years, letting it bounce from one to the next.",
  "vis": {"type": "slingshot", "mode": "tour", "head": "Voyager 2: the Grand Tour", "caption": "launched 20 Aug 1977; Uranus Jan 1986; Neptune Aug 1989 (NASA)"}},
 {"say": "Out there, even a conversation is slow. When Voyager two flew past Neptune, its radio signals needed about four hours to reach Earth. The engineers were watching pictures of a moment that had already ended hours before. The flyby was programmed in advance, and the spacecraft did it alone.",
  "vis": {"type": "bignumber", "from": 0, "to": 4, "suffix": " hours", "col": TICKET, "caption": "radio signal time from Neptune to Earth during the 1989 flyby (NASA)"}},

 # ---------- FULL BOARD ----------
 {"say": "Here's the whole board. For the car, every planet is a trip measured in lifetimes. For the jet, everything past Mars takes longer than a career. And for light, the fastest thing there is, Neptune is about four hours away.",
  "vis": {"type": "departures", "rows": 8, "hl": -1, "light": True, "head": "The full board"}},
 {"say": "Look at the gap between the rows. The jump from Mars to Jupiter is bigger than everything before it combined. The inner planets huddle close to the Sun, and then the solar system suddenly opens up. Neptune is about eighty times farther than Mars at its closest. If the Sun were a front door, Mars would sit about three hundred thirty meters from it, and Neptune six and a half kilometers away.",
  "vis": {"type": "transfer", "target": "Jupiter", "days": 0, "map": True, "head": "The solar system opens up"}},

 # ---------- TWIST ----------
 {"say": "So why can't we just point a rocket at Neptune and go? Because there is no such thing as standing still in space. You start out already moving around the Sun at thirty kilometers per second, sideways. Going outward means climbing out of the Sun's gravity, and every kilometer per second costs fuel.",
  "vis": {"type": "transfer", "target": "Neptune", "days": 4386, "ghost": True, "head": "No straight lines in space"}},
 {"say": "Parker Solar Probe got its record speed by falling toward the Sun, not by flying away from it. The fastest anything has ever been launched from Earth is New Horizons, on its way to Pluto, at about fifty eight thousand kilometers per hour. Even so, it took nine and a half years to get there.",
  "vis": {"type": "bignumber", "from": 0, "to": 58536, "suffix": " km/h", "col": BOARD, "caption": "New Horizons, fastest launch speed ever (NASA); Pluto flyby after 9.5 years"}},
 {"say": "That's the real lesson of the solar system. The distances are huge, but the hard part is not the distance. It's the speed you have to gain, or lose, and the planets you have to borrow it from.",
  "vis": {"type": "slingshot", "mode": "boost", "planet": "Jupiter", "head": "Distance is easy. Speed is hard."}},

 # ---------- RECAP + NEXT ----------
 {"say": "So, by car, every planet is out of reach. By jet, only the nearest are reachable in a lifetime. By spacecraft, it's months to Mars, years to Jupiter, and more than a decade to Neptune. And Mercury, the closest planet on average, is one of the hardest to stop at. Every number in this video, with its source, is in the description.",
  "vis": {"type": "bullets", "title": "Tickets to every planet", "items": ["Moon: 160 days by car", "Mars: 62 years by car, 203 days real", "Mercury: 6.6 years to stop there", "Jupiter: 671 years by car", "Neptune: 4,912 years by car, 12 real"], "col": ROAD, "highlight": 2}},
 {"say": "Next time: an asteroid is heading for Earth, and it's going to hit the ocean. Would that be better, or much worse? That's next.",
  "vis": {"type": "title", "title": "Next:\nWhat If an Asteroid\nHit the Ocean?", "sub": "COSMIC SCALE", "brand": False, "subcol": TICKET}},
]

SOURCES = [
 "NASA Planetary Fact Sheet (NSSDCA): minimum distance from Earth in millions of km: Venus 38.2, Mars 54.6, Mercury 77.3, Jupiter 588.5, Saturn 1,195.5, Uranus 2,581.9, Neptune 4,305.9",
 "NASA: average Earth–Moon distance 384,400 km; Apollo missions reached the Moon in about three days",
 "NASA: Parker Solar Probe reached about 692,000 km/h (192 km/s) on 24 December 2024, the fastest human-made object",
 "ESA: Venus Express launched 9 November 2005 and entered orbit around Venus on 11 April 2006",
 "NASA / JPL: Perseverance launched 30 July 2020 and landed on Mars 18 February 2021; Earth–Mars launch windows about every 26 months",
 "NASA / JHUAPL: MESSENGER launched 3 August 2004 and entered orbit around Mercury on 18 March 2011, after flybys of Earth (1), Venus (2) and Mercury (3)",
 "ESA / JAXA: BepiColombo launched 20 October 2018; nine planetary flybys; Mercury orbit insertion planned for November 2026",
 "Stockman, Monroe & Cordner (2019), Physics Today, 'Venus is not Earth's closest neighbor': on average Mercury is the closest planet to Earth and to every other planet",
 "NASA / JPL: Juno launched 5 August 2011, Earth flyby October 2013, arrived at Jupiter 4 July 2016",
 "NASA / JPL: Cassini launched 15 October 1997, flybys of Venus (2), Earth and Jupiter, arrived at Saturn 1 July 2004",
 "NASA / JPL: Voyager 2 launched 20 August 1977, flew past Uranus on 24 January 1986 and Neptune on 25 August 1989, the only spacecraft to visit them; the alignment that allowed the Grand Tour happens about once every 175 years",
 "NASA: New Horizons left Earth at about 58,536 km/h (16.26 km/s), the fastest launch speed ever; Pluto flyby 14 July 2015",
 "NASA: Earth orbits the Sun at about 30 km/s",
 "NASA / JPL: Perseverance traveled about 472 million km (293 million miles) from Earth to Mars; during Voyager 2's Neptune flyby, signals took about 4 hours to reach Earth",
 "NASA: Sun diameter about 1,392,000 km; Mars orbits about 1.52 AU and Neptune about 30.1 AU from the Sun",
 "Great Pyramid of Giza: built around 2560 BC (about 4,500 years ago)",
 "Own calculations (Python): time = distance / speed with no stops; car 100 km/h, jet 900 km/h, Parker 692,000 km/h, light 299,792 km/s. Car: Moon 160 days, Venus 43.6 years, Mars 62.3, Mercury 88.2, Jupiter 671, Saturn 1,364, Uranus 2,945, Neptune 4,912. Jet: Moon 18 days, Venus 4.8 years, Mars 6.9, Mercury 9.8, Jupiter 74.6, Saturn 152, Uranus 327, Neptune 546. Parker: Venus 2.3 days, Mars 3.3, Mercury 4.6, Jupiter 35, Saturn 72, Uranus 155, Neptune 259. Light to Neptune 4.0 hours. Neptune vs Mars at closest: 4,305.9 / 54.6 = 79. Sun scaled to a 2 m door: 1 AU = 215 m, so Mars at 1.52 AU ≈ 330 m and Neptune at 30.1 AU ≈ 6.5 km from the Sun. Walking to the Moon at 5 km/h: 8.8 years. 30 years per generation (Jupiter by car about 22 generations)",
]
