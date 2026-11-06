# EP04 — What Happens If You Fall Into a Black Hole?
# Structure: "choose your black hole" — two parallel dives (small 10-Sun hole vs Sagittarius A*), then the outside view
# (two clocks paradox), crossing, time left inside, the biggest horizon (M87*), payoff -> EP05 (largest star vs the Sun).
# Palette: ember orange / pale cyan. New scene types: blackhole, spaghetti, twoclocks, horizonsize, inside
# Own calculations (Python, G=6.674e-11, c=2.998e8, Msun=1.989e30): horizon diameters 59 km (10 Msun), 25.4 million km (4.3e6),
# 38.4 billion km (6.5e9); tidal stretch on 2 m body = 2GML/r^3: 1 g at ~8,150 km and 100 g at ~1,760 km (10 Msun),
# ~21 million g at its horizon, ~1/9,000 g at Sgr A* horizon; max proper time horizon->singularity = pi*GM/c^3:
# 0.15 ms (10 Msun), 66 s (4.3e6), 27.9 h (6.5e9). Pluto orbit diameter ~11.8 billion km.
TITLE = "What Happens If You Fall Into a Black Hole?"
EMB = [255, 138, 61]
PAL = [159, 232, 255]

SCENES = [
 # ---------- HOOK ----------
 {"say": "Fall into a small black hole, and you die before you even reach it. Fall into a giant one, and you cross the point of no return without feeling a thing. Today we jump into both, and follow you all the way to the end. Including the strangest part of all: what your friends back home would see.",
  "vis": {"type": "blackhole", "r": 120, "head": "Small hole: you die first.  Giant hole: you feel nothing.", "faller": True}},
 {"say": "Here's the experiment. Two black holes. The first is small, about ten times the mass of the Sun, the kind left behind when a giant star collapses. The second is the monster at the center of our own galaxy, Sagittarius A star, about four million times the mass of the Sun, twenty six thousand light years away. By the end, you'll know exactly how much time you'd have left inside each one. For one of them, it's far less than a blink.",
  "vis": {"type": "compare", "left": ["Small", "10 Suns of mass", "≈ 60 km wide", "a city-sized hole"], "right": ["Giant", "Sagittarius A*", "4 million Suns", "≈ 25 million km wide"], "cols": [EMB, PAL], "strike": False}},
 {"say": "What Happens If You Fall Into a Black Hole?",
  "vis": {"type": "title", "title": "What Happens If You\nFall Into a Black Hole?", "sub": "COSMIC SCALE", "brand": True, "subcol": EMB}},

 # ---------- THEY DON'T SUCK ----------
 {"say": "First, forget the vacuum cleaner. Black holes don't suck. If you could crush the Sun into a black hole with the same mass, it would be only about six kilometers wide, and Earth would keep orbiting exactly as it does today. NASA says it plainly: the orbits of the planets would not change. It would just get very dark and very cold. From far away, a black hole pulls like any other object of the same mass. The danger only starts when you get close.",
  "vis": {"type": "horizonsize", "kind": "sun", "caption": "Same mass, same pull. The orbit doesn't change."}},
 {"say": "So what counts as close? Every black hole has an edge called the event horizon. It isn't a surface. There's nothing there to touch. It's simply the distance where escaping would mean moving faster than light. Cross it, and nothing, not even light, ever comes back out. A little farther out is the photon sphere, where gravity bends light into a circle. Light there can orbit the hole. In principle, you could look straight ahead and see the back of your own head.",
  "vis": {"type": "blackhole", "r": 140, "labels": [[["photon sphere", "light can orbit here"], 1.5, 1], [["event horizon", "the point of no return"], 1.42, -1]]}},

 # ---------- DIVE 1: THE SMALL HOLE ----------
 {"say": "Let's start with the small one. Ten Suns of mass, squeezed into a ball about sixty kilometers wide. You could drive across it in well under an hour. You fall feet first. And here's the problem. Gravity pulls harder on your feet than on your head, because your feet are closer. On Earth, that difference is too tiny to notice. Here, by our calculation, about eight thousand kilometers from the center, the stretch on your body already equals your full weight. As if a second copy of you were hanging from your ankles.",
  "vis": {"type": "spaghetti", "msun": 10, "r_from": 60000, "r_to": 8150, "title": "Dive 1: the small hole", "sub": "10 Suns of mass · feet first"}},
 {"say": "And it gets worse fast. Halve the distance, and the stretch grows eight times. At about seventeen hundred kilometers out, it's a hundred times your weight. Already deadly. Physicists really do call what happens next spaghettification. You're pulled long and thin, and squeezed from the sides, until you're a stream of atoms pouring toward the hole.",
  "vis": {"type": "spaghetti", "msun": 10, "r_from": 8150, "r_to": 1760, "title": "Dive 1: the small hole", "sub": "the stretch grows with 1 / distance³", "verdict": "100 g of stretch: you don't make it"}},
 {"say": "By the time what's left of you reaches the event horizon, the stretch is around twenty million times Earth's gravity. So in a small black hole, nobody crosses the horizon in one piece. You never even get to see the edge up close.",
  "vis": {"type": "bignumber", "from": 0, "to": 21000000, "suffix": " g", "col": EMB, "caption": "stretch at the horizon of a 10-Sun black hole"}},

 # ---------- DIVE 2: THE GIANT ----------
 {"say": "Now the giant. Sagittarius A star. Four million times the mass of the Sun. You'd think more mass means more pain. It's the opposite. A bigger black hole has a horizon so far from its center that the difference between your head and your feet almost disappears. Right at the edge, the stretch on your body is less than a thousandth of your weight. You wouldn't feel a thing.",
  "vis": {"type": "spaghetti", "msun": 4300000, "r_from": 300000000, "r_to": 12700000, "big": True, "title": "Dive 2: the giant", "sub": "Sagittarius A* · 4 million Suns", "verdict": "at the horizon: you feel nothing"}},
 {"say": "This isn't just theory on paper. In twenty twenty four, NASA's Goddard Space Flight Center ran a supercomputer simulation of exactly this plunge, into a black hole of four point three million Suns, the same as ours. The virtual camera falls for about three hours, loops around almost twice, and crosses the horizon intact. The bigger the black hole, the gentler its edge.",
  "vis": {"type": "blackhole", "r": 150, "faller": True, "zoom": 0.25, "caption": "NASA Goddard simulation (2024): the camera crosses the horizon intact"}},

 # ---------- RE-ENGAGE 1: THE TWO CLOCKS ----------  # REENGAJE (~3:00)
 {"say": "But here's the strangest part. Your friend stays far away, watching you fall. From your point of view, your watch ticks normally the whole way down. You cross the horizon at a perfectly ordinary second. From your friend's point of view, you slow down. Each tick of your watch takes longer and longer to reach them. Your light stretches into red, then into infrared, then fades. They never see you cross. You seem to freeze at the edge, dimming until you're simply gone.",
  "vis": {"type": "twoclocks", "k": 6.0, "caption": "Same fall. Two completely different stories."}},
 {"say": "So who's right? Both of you. There is no single clock for the universe. Gravity bends time, and near a horizon it bends it to the extreme. NASA's simulation shows this even without falling in. An astronaut who dives close to the horizon and climbs back out, a trip of about six hours, comes home thirty six minutes younger than the partner who waited far away.",
  "vis": {"type": "bignumber", "from": 0, "to": 36, "suffix": " min", "col": PAL, "caption": "younger after a 6-hour trip near the horizon (NASA simulation)"}},

 # ---------- CROSSING ----------
 {"say": "Now you cross. And nothing happens. No wall, no flash, no sign. That's what makes it terrifying. Because inside the horizon, space and time swap roles. The center, the singularity, is no longer a place in front of you. It's a moment in your future. Steering away from it would be like steering away from next Tuesday. Every direction you can possibly move now points inward.",
  "vis": {"type": "inside", "head": "Inside the horizon", "lines": ["The center is not a place ahead…", "…it's a moment in your future", "Every path points inward", "No way to steer out"]}},
 {"say": "So how long do you get? Here's the answer I promised. It depends entirely on which black hole you pick. In the small one, the trip from the horizon to the center lasts, at most, about a sixth of a millisecond. A nerve signal from your toes would need around a hundred times longer just to reach your brain. You would never even feel it.",
  "vis": {"type": "inside", "head": "Small hole · 10 Suns", "timer": 0.15, "timer_fmt": "{:.2f} ms", "timer_sub": "faster than a nerve signal"}},
 {"say": "In Sagittarius A star, our calculation gives you at most about sixty six seconds of your own time. And firing your rockets only makes it shorter. In NASA's simulation, the camera lasts twelve point eight seconds after crossing before the stretching finally tears it apart. About a minute, to see something no one outside can ever see.",
  "vis": {"type": "inside", "head": "Sagittarius A* · 4 million Suns", "timer": 66, "count": True, "timer_fmt": "{:.0f} s", "timer_sub": "NASA sim: torn apart 12.8 s after crossing"}},

 # ---------- RE-ENGAGE 2: THE BIGGEST HORIZON ----------  # REENGAJE (~6:00)
 {"say": "Want more time? You need a bigger monster. And they get much bigger. This is how wide the horizon of Sagittarius A star is, drawn to scale. Around twenty five million kilometers. Bigger than the Sun eighteen times over, yet it would still fit inside the orbit of Mercury.",
  "vis": {"type": "horizonsize", "kind": "sgr", "caption": "Sagittarius A*: horizon drawn to scale over the inner solar system"}},
 {"say": "Now M eighty seven star, the first black hole ever photographed, by the Event Horizon Telescope in twenty nineteen. Fifty five million light years away, six and a half billion times the mass of the Sun. Its horizon is about thirty eight billion kilometers across. Drop it where our Sun is, and it would swallow the orbit of Pluto, three times over.",
  "vis": {"type": "horizonsize", "kind": "m87", "caption": "M87*: horizon drawn to scale over the whole solar system"}},
 {"say": "Fall into that one, and the clock inside runs for up to about twenty eight hours. More than a full day. Enough time to eat, to sleep, maybe to write a letter that no one will ever read.",
  "vis": {"type": "inside", "head": "M87* · 6.5 billion Suns", "timer": 28, "timer_fmt": "{:.0f} hours", "timer_sub": "more than a full day inside"}},

 {"say": "And none of this is just equations on a blackboard. In twenty fifteen, the LIGO detectors felt space itself shiver as two black holes, about thirty six and twenty nine times the mass of the Sun, merged one point three billion light years away. Then the Event Horizon Telescope, a network of radio dishes that works like a telescope as wide as the Earth, photographed the glowing rings around M eighty seven star and Sagittarius A star. A dark shadow, wrapped in bent light. Just like the drawing on your screen.",
  "vis": {"type": "blackhole", "r": 130, "zoom": 0.15, "head": "Not just theory: heard in 2015, photographed in 2019 and 2022", "caption": "drawing, not a photo — the real images show the same shadow and ring"}},
 {"say": "And if you'd rather wait outside, black holes don't last forever either. In nineteen seventy four, Stephen Hawking showed they should slowly leak away energy, now called Hawking radiation. But slowly is an understatement. A black hole with the mass of our Sun would take around ten to the sixty seventh years to evaporate. That's a one followed by sixty seven zeros. The universe is about fourteen billion years old. It hasn't even started.",
  "vis": {"type": "title", "title": "≈ 10⁶⁷ years", "sub": "to evaporate a black hole with the Sun's mass (Hawking, 1974)", "brand": False, "subcol": PAL}},

 # ---------- REALITY CHECK ----------
 {"say": "Is there one anywhere near us? The closest black hole we know, Gaia B H one, is about fifteen hundred and sixty light years away. In twenty twenty four, the European Space Agency's Gaia mission found Gaia B H three, thirty three times the mass of the Sun, about nineteen hundred light years from here. Both are quiet, both are far, and neither can pull on us. To fall into a black hole, you would have to go to it.",
  "vis": {"type": "bullets", "title": "The nearest ones we know", "items": ["Gaia BH1 · ≈ 1,560 light-years", "Gaia BH3 · 33 Suns · ≈ 1,926 ly", "Sagittarius A* · ≈ 26,000 ly", "None can pull on us"], "col": EMB, "highlight": 3}},

 # ---------- PAYOFF + NEXT ----------
 {"say": "So, what happens if you fall into a black hole? Pick a small one, and you're spaghetti before you arrive. Pick a giant, and you cross in peace, with a minute, or a day, left on your watch, while your friends watch you freeze forever at the edge. But black holes aren't the only giants out there. Some stars are so big that, placed where our Sun is, they'd swallow every planet out past Jupiter. So just how big can a star get? Next, we put the largest star ever measured right next to our Sun.",
  "vis": {"type": "title", "title": "Next:\nThe Largest Star vs the Sun", "sub": "COSMIC SCALE", "brand": False, "subcol": EMB}},
]

SOURCES = [
 "NASA Science, 10 Questions You Might Have About Black Holes (spaghettification; same-mass black hole would not change planetary orbits; Sgr A* about 4 million Suns, 26,000 light-years; M87 6.5 billion Suns)",
 "NASA Goddard Space Flight Center (May 2024), black hole plunge visualization by Jeremy Schnittman: 4.3 million solar masses, horizon about 25 million km, ~3-hour fall, torn apart 12.8 s after crossing, 6-hour trip leaves astronaut 36 minutes younger",
 "Event Horizon Telescope press release, April 10, 2019 (M87*: 55 million light-years, 6.5 billion solar masses)",
 "LIGO Caltech, GW150914 (Sept 14, 2015): black holes of about 36 and 29 solar masses merging 1.3 billion light-years away",
 "Event Horizon Telescope, May 12, 2022 (Sagittarius A* image, about 4 million solar masses, about 27,000 light-years)",
 "ESA Gaia, April 2024: Gaia BH3, 33 solar masses, about 1,926 light-years",
 "El-Badry et al. (2023), MNRAS / NOIRLab: Gaia BH1, about 1,560 light-years",
 "Hawking (1974), Nature: black hole explosions?; evaporation time ≈ 2×10^67 years for one solar mass (own calculation, 5120πG²M³/ħc⁴)",
 "Own calculations (Schwarzschild metric): horizon sizes, tidal stretch 2GML/r³ on a 2 m body, maximum proper time horizon→singularity πGM/c³",
]
