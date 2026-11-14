# EP12 — The Speed of Light Is Slow (and here's proof)
# Structure NEW: "7 messages, 1 stopwatch" — hook (sunlight's energy is thousands of years old) -> light is fast (7.5 laps of Earth per
# second) -> 7 messages, each with its lag on a log meter: 1 inside a chip (10 cm per tick), 2 New York -> London (fiber), 3 a call to the
# Moon, 4 driving on Mars (Perseverance landing), 5 sunlight (8 min 19 s + the random walk inside the Sun), 6 Voyager 1 (almost 1 light-day)
# + Proxima / Milky Way / Andromeda as old photographs, 7 beyond the cosmic event horizon (never) -> recap -> EP13.
# Palette photon gold / signal green / fiber magenta / navy. New scenes: lagmeter, chiptick, fiberrace, marsdelay, randomwalk, horizonrun.
# Own calculations (Python): c = 299,792.458 km/s = 1,079,252,849 km/h; Earth's equator 40,075 km -> 7.48 laps per second;
# 3 GHz tick = 0.333 ns -> 9.99 cm; New York–London ≈ 5,570 km great circle -> 18.6 ms in vacuum, 27.3 ms in fiber (n ≈ 1.47);
# Moon 384,400 km -> 1.28 s (2.56 s round trip); 1 AU 149,597,871 km -> 499 s = 8 min 19 s; Sun radius 696,000 km -> 2.3 s in a straight
# line; Proxima 4.24 ly -> 8.5-year round trip; reachable share of the observable universe ≈ 299,792 / 192 ≈ 1,561; (16/46)^3 ≈ 4% -> more than 9 in 10
# galaxies we can see are out of reach (rough, assumes galaxies spread evenly).
TITLE = "The Speed of Light Is Slow"
PHOT = [255, 232, 150]
SIG = [110, 255, 170]
FIB = [255, 95, 200]

SCENES = [
 # ---------- HOOK ----------
 {"say": "The sunlight on your skin right now left the Sun eight minutes ago. But the energy inside it may have spent tens of thousands of years, maybe more than a hundred thousand, just fighting its way out of the Sun.",
  "vis": {"type": "randomwalk", "y1": 170000, "head": "How old is the sunlight on your skin?"}},
 {"say": "Light is the fastest thing in the universe. It covers almost three hundred thousand kilometers every second, enough to circle the Earth seven and a half times before you finish saying the word second. Nothing with mass can ever catch it.",
  "vis": {"type": "bignumber", "from": 0, "to": 7.5, "decimals": 1, "suffix": " laps", "col": PHOT, "caption": "around Earth in one second (c = 299,792 km/s)"}},
 {"say": "The fastest machine we've ever built, NASA's Parker Solar Probe, reached about six hundred ninety thousand kilometers per hour as it skimmed past the Sun. Light is still more than fifteen hundred times faster.",
  "vis": {"type": "bignumber", "from": 0, "to": 1561, "suffix": "×", "col": SIG, "caption": "light vs Parker Solar Probe's record 192 km/s (NASA, our calculation)"}},
 {"say": "And yet, light is slow. Painfully slow. I'll prove it with seven messages. We'll start inside your phone, and end at a place no message will ever reach. Seven messages, one stopwatch.",
  "vis": {"type": "lagmeter", "n": 0, "head": "7 messages, 1 stopwatch"}},
 {"say": "The Speed of Light Is Slow.",
  "vis": {"type": "title", "title": "The Speed of Light\nIs Slow", "sub": "COSMIC SCALE", "brand": True, "subcol": PHOT}},

 # ---------- 1 CHIP ----------
 {"say": "Message one. Inside the device you're watching this on.",
  "vis": {"type": "lagmeter", "n": 1}},
 {"say": "A modern processor ticks about three billion times every second. In one of those ticks, light travels just ten centimeters. That's about the width of your hand. Even the light from your screen needs more than a billionth of a second to reach your eyes. And the electrical signals inside a chip are slower than light in empty space.",
  "vis": {"type": "chiptick", "caption": "3 GHz: 1 tick = 0.33 ns, light covers ≈ 10 cm (our calculation)"}},
 {"say": "So chip designers fight over millimeters. A signal simply can't run across a big chip and back in a single tick. That's one reason processors are tiny and packed tight, and why memory sits as close to the processor as engineers can put it. At the scale of a computer, the speed of light is already a wall you can bump into.",
  "vis": {"type": "chiptick", "period": 1.6, "head": "Every millimeter costs time"}},

 # ---------- 2 FIBER ----------
 {"say": "Message two. A stock trade from New York to London.",
  "vis": {"type": "lagmeter", "n": 2}},
 {"say": "The two cities are about fifty five hundred seventy kilometers apart. In a vacuum, light would cross that in about nineteen milliseconds. But the internet runs through glass fiber, and inside glass, light slows down to roughly two thirds of its full speed.",
  "vis": {"type": "fiberrace", "head": "New York → London: 5,570 km"}},
 {"say": "So by our calculation, even a perfectly straight cable needs about twenty seven milliseconds, one way. Real cables take detours, so it's more. That sounds like nothing, until you learn that trading firms have paid for straighter cables and chains of microwave towers, because radio through air travels almost at the full speed of light. Fortunes are won and lost over a few thousandths of a second. And every time you play an online game against someone on another continent, part of the lag you feel is simply light taking its time.",
  "vis": {"type": "fiberrace", "microwave": True, "head": "Glass slows light to about 2/3", "caption": "our calculation: 18.6 ms in vacuum, 27.3 ms in glass"}},

 # ---------- 3 MOON ----------
 {"say": "Message three. A phone call to the Moon.",
  "vis": {"type": "lagmeter", "n": 3}},
 {"say": "The Moon is about three hundred eighty four thousand kilometers away. Light needs about one point three seconds to get there, so every answer arrives at least two and a half seconds after you ask the question. You can hear those pauses in the Apollo recordings, between mission control and the astronauts. It's awkward, but you can still have a conversation. Scientists use this delay on purpose. Apollo astronauts left mirrors on the Moon, and observatories still fire lasers at them and time the echo. Today, that round trip measures the distance to the Moon to within a few millimeters.",
  "vis": {"type": "marsdelay", "mode": "moon", "head": "A call to the Moon, in real time"}},

 # ---------- 4 MARS ----------
 {"say": "Message four. Driving a rover on Mars.",
  "vis": {"type": "lagmeter", "n": 4}},
 {"say": "Earth and Mars circle the Sun at different speeds, so the distance between them keeps changing. Depending on where the two planets are, a radio signal takes somewhere between about three and twenty two minutes, one way. Nobody can drive a rover with a joystick and a twenty minute lag. By the time you saw the rock, you'd already have hit it. That's why rovers get their instructions as a plan for the whole day, and then mostly drive themselves. And when the Sun passes between Earth and Mars, it blocks the signal entirely for about two weeks, and the rovers are left completely on their own.",
  "vis": {"type": "marsdelay", "mode": "range", "head": "Earth to Mars: the lag keeps changing"}},
 {"say": "In February twenty twenty one, NASA's Perseverance rover had about seven minutes to get from the top of the Martian atmosphere to the ground. Its signal took about eleven minutes to reach Earth.",
  "vis": {"type": "marsdelay", "mode": "landing", "head": "Seven minutes on Mars, eleven minutes of lag"}},
 {"say": "So when the engineers heard that the rover was entering the atmosphere, it had already been on the ground for minutes, landed safely or smashed into the rock. Nobody on Earth could help. Every move had to be decided by the rover itself, because light was simply too slow to let humans steer.",
  "vis": {"type": "marsdelay", "mode": "landing", "head": "Too late to help"}},

 # ---------- 5 SUNLIGHT ----------
 {"say": "Message five. Not one we send. One we receive. Sunlight.",
  "vis": {"type": "lagmeter", "n": 5}},
 {"say": "The Sun is about a hundred fifty million kilometers away, so its light takes about eight minutes and nineteen seconds to reach you. Every time you look at the Sun's disc, you're looking eight minutes into the past. If the Sun vanished right now, you'd keep seeing it and feeling its warmth for more than eight minutes. Even its gravity, which also travels at the speed of light, would keep Earth on its old path for those eight minutes.",
  "vis": {"type": "bignumber", "from": 0, "to": 499, "suffix": " s", "col": PHOT, "caption": "8 min 19 s from the Sun to Earth (our calculation, 1 AU)"}},
 {"say": "But that's the easy part of the trip. The energy in sunlight is made in the Sun's core, and getting out is a nightmare. Inside, the Sun is so dense that light is absorbed and given off again and again, each time in a random direction. In a straight line, the trip from the core to the surface would take about two seconds.",
  "vis": {"type": "randomwalk", "y1": 10000, "head": "Inside the Sun: a random walk"}},
 {"say": "Instead, according to NASA, that energy can take around a hundred seventy thousand years to work its way out. The exact number depends on the model, and some estimates are closer to ten thousand years. Either way, the warmth on your face began its journey long before anyone built a city. Eight minutes through space. Thousands of years through the Sun.",
  "vis": {"type": "randomwalk", "y1": 170000, "head": "Thousands of years to get out", "caption": "NASA; Mitalas & Sills (1992): about 170,000 years (model-dependent)"}},

 # ---------- 6 VOYAGER + OLD PHOTOGRAPHS ----------
 {"say": "Message six. A call to the most distant spacecraft ever.",
  "vis": {"type": "lagmeter", "n": 6}},
 {"say": "Voyager one left Earth in nineteen seventy seven and it's still talking to us. Right now it's so far away that a command takes almost a full day to arrive. In a few days, on November eighteenth, it crosses one light-day from Earth for the first time. Ask it a question on Monday, and the answer comes back on Wednesday. When engineers fix a problem on Voyager, they wait two days to find out whether the fix worked.",
  "vis": {"type": "voyager", "line": "≈ 26 billion km  •  signal time: almost 24 hours", "caption": "1 light-day from Earth on 18 November 2026 (NASA)"}},
 {"say": "And Voyager is basically still next door. The nearest star, Proxima Centauri, is four point two four light-years away. Say hello today, and the earliest possible reply would arrive about eight and a half years from now. The light from Proxima reaching Earth tonight left the star in twenty twenty two. A round trip across our galaxy, the Milky Way, would take about two hundred thousand years.",
  "vis": {"type": "bignumber", "from": 0, "to": 8.5, "decimals": 1, "suffix": " years", "col": SIG, "caption": "earliest reply from Proxima Centauri, 4.24 light-years away"}},
 {"say": "That slowness has a strange side effect. Every time you look up, you're looking at the past. The Andromeda galaxy, on a dark night, is light that left it about two and a half million years ago, before our species existed. You're not seeing Andromeda. You're seeing a very old photograph of it.",
  "vis": {"type": "compare", "left": ["WHAT YOU SEE", "the Sun, 8 min ago", "Proxima, 4.2 yr ago", "Andromeda, 2.5 Myr ago"], "right": ["WHAT IT IS NOW", "you can't know yet", "the news is on its way", "already different"], "cols": [PHOT, FIB], "strike": False}},

 # ---------- 7 NEVER ----------
 {"say": "Message seven. The one that can never arrive.",
  "vis": {"type": "lagmeter", "n": 7}},
 {"say": "The universe is expanding. The space between distant galaxies keeps stretching, and the expansion is speeding up. Picture light from a far away galaxy as a runner on a treadmill that keeps getting longer and faster.",
  "vis": {"type": "horizonrun", "label": False, "head": "Light on a stretching treadmill"}},
 {"say": "For galaxies closer than about sixteen billion light-years, the light they send today will reach us eventually. Beyond that line, called the cosmic event horizon, it never will. Not in a billion years. Not ever. And as time goes on, more and more galaxies slip across that line.",
  "vis": {"type": "horizonrun", "label": True, "head": "The cosmic event horizon"}},
 {"say": "We can still see plenty of galaxies beyond that line, because we're catching old light they sent long ago, when they were closer. But by our rough calculation, more than nine out of ten galaxies in the observable universe are already out of reach forever. Even a message sent today at the speed of light would never get there.",
  "vis": {"type": "bignumber", "from": 0, "to": 96, "prefix": "≈ ", "suffix": "%", "col": FIB, "caption": "of the galaxies we can see: out of reach forever (our rough calculation)"}},

 # ---------- RECAP + NEXT ----------
 {"say": "So yes, light is the fastest thing there is. It's also too slow for your processor, too slow for traders, too slow to drive on Mars, and too slow to ever reach most of the universe. The cosmic speed limit isn't just fast. It's a wall. Every number in this video, with its source, is in the description.",
  "vis": {"type": "bullets", "title": "Light is slow", "items": ["10 cm per processor tick", "27+ ms New York → London", "3 to 22 min to Mars", "≈ 1 day to Voyager 1", "never, past ≈ 16 billion ly"], "col": PHOT, "highlight": 4}},
 {"say": "And if light is slow, imagine us. Next time: how long would it take to travel to every planet in the solar system, by car, by plane, and by the fastest spacecraft ever built? That's next.",
  "vis": {"type": "title", "title": "Next:\nHow Long to Reach\nEvery Planet?", "sub": "COSMIC SCALE", "brand": False, "subcol": SIG}},
]

SOURCES = [
 "BIPM / SI definition: the speed of light in vacuum is exactly 299,792,458 m/s",
 "NASA Science, Sun: a photon's energy takes about 170,000 years to travel from the core to the surface; Mitalas & Sills (1992), Astrophysical Journal; other estimates are as low as about 10,000 years (model-dependent)",
 "ESA (Mars Express) and NASA (Perseverance): radio signals between Earth and Mars take about 3 to 22 minutes one way, depending on the planets' positions",
 "NASA: during Mars solar conjunction (about every two years) the Sun blocks communications with Mars missions for about two weeks",
 "NASA / JPL, Perseverance landing (18 February 2021): about seven minutes from the top of the atmosphere to touchdown; about 11 minutes for the signal to reach Earth",
 "NASA: average Earth–Moon distance 384,400 km",
 "Lunar laser ranging (APOLLO station, Apache Point Observatory; Murphy 2013, Reports on Progress in Physics): Apollo retroreflectors, Earth–Moon distance measured to about a millimeter",
 "NASA: Parker Solar Probe reached about 692,000 km/h (192 km/s) on 24 December 2024, the fastest human-made object",
 "NASA / JPL: Voyager 1 (launched 1977) reaches one light-day from Earth on 18 November 2026",
 "NASA: Proxima Centauri is 4.24 light-years away; the Milky Way is about 100,000 light-years across; the Andromeda galaxy is about 2.5 million light-years away",
 "Davis & Lineweaver (2004), Publications of the Astronomical Society of Australia, 'Expanding Confusion': cosmic event horizon about 16 billion light-years; observable universe radius about 46 billion light-years",
 "Own calculations (Python): c = 1,079,252,849 km/h; 40,075 km equator, 7.48 laps per second; 3 GHz tick = 0.33 ns, about 10 cm of light travel; New York–London about 5,570 km great circle, 18.6 ms in vacuum and 27.3 ms in glass fiber (refractive index about 1.47); 1 AU = 149,597,871 km, 499 s = 8 min 19 s; Sun radius 696,000 km, 2.3 s in a straight line; screen to eyes about 0.5 m = 1.7 ns; 2 × 4.24 = 8.5-year round trip to Proxima; 299,792 / 192 ≈ 1,561; (16/46)^3 ≈ 4%, so more than 9 in 10 galaxies we can see are out of reach (assumes galaxies spread evenly)",
]
