# EP18 — What If You Fell Into Jupiter?
# Structure NEW: "the elevator" — one fall, floor by floor. Every chapter opens on a depth gauge (depth below the 1-bar level, pressure,
# temperature) and then shows what that floor is like. Keeps EP17's promise (what if you fell into Jupiter). Ends with the things that
# really did fall in (Galileo orbiter 2003, comet Shoemaker-Levy 9 in 1994).
# Palette: Jupiter ochre / ammonia cream / deep metallic violet; depth darkens the background floor by floor.
# New scenes: plunge, depthgauge, cloudstack, nosurface, jupcut, scars.
# Own calculations (Python, GM_Jupiter = 1.26687e17 m³/s², 1-bar equatorial radius 71,492 km):
#   fall from rest at Europa's orbit (670,900 km): 56.3 km/s at the cloud tops after 14.8 h; from far away: escape speed 59.5 km/s (214,000 km/h);
#   gravity 24.79 m/s² = 2.53 g (70 kg feels like 177 kg); centre ~69,900 km down = 5.5 Earth diameters;
#   at Galileo's average descent pace (≈ 150 km in 58 min) the trip to the centre would take ≈ 19 days.
# EP18 promised EP19: what if Earth had a second Moon?
TITLE = "What If You Fell Into Jupiter?"
OCH = [230, 170, 100]
CREAM = [245, 225, 185]
VIO18 = [170, 120, 255]
HOT18 = [255, 120, 70]

SCENES = [
 # ---------- HOOK ----------
 {"say": "You're falling toward Jupiter. Nothing can stop you now. And here's the strange part. There is no ground waiting for you. You could fall for seventy thousand kilometers, and never land on anything.",
  "vis": {"type": "plunge", "mode": "hook", "head": "70,000 km down. No ground."}},
 {"say": "Jupiter is the biggest planet we have, eleven Earths wide. Today we jump in, and we ride all the way down, floor by floor, to find out what's really inside.",
  "vis": {"type": "title", "title": "What If You\nFell Into Jupiter?", "sub": "COSMIC SCALE", "brand": True, "subcol": OCH}},
 {"say": "And it's heavy. Jupiter holds three hundred and eighteen times the mass of Earth. That's more than twice as much as all the other planets put together. Everything about this fall is going to be extreme.",
  "vis": {"type": "bignumber", "from": 1, "to": 318, "suffix": " Earths", "col": OCH, "caption": "Jupiter's mass, in Earth masses (NASA fact sheet: 317.8)"}},
 {"say": "Here's how this works. Jupiter has no surface, so scientists pick a zero point. It's the height where the air pressure is the same as at sea level on Earth. One bar. Everything we measure today is depth below that line. And on the way, we'll watch three numbers. How deep, how hard the air is pushing, and how hot it gets.",
  "vis": {"type": "depthgauge", "depth": 0, "ptxt": "1 bar", "ttxt": "≈ −107 °C", "floor": "THE ZERO LINE", "note": "where the pressure equals sea level on Earth"}},

 # ---------- FLOOR 1: THE APPROACH ----------
 {"say": "Floor one is still in space. Let's say you step off near Europa, one of Jupiter's moons, six hundred and seventy thousand kilometers out. At first, you barely move. But Jupiter pulls harder and harder. Our calculation: after almost fifteen hours of falling, you're going fifty six kilometers per second.",
  "vis": {"type": "plunge", "mode": "approach", "v0": 0, "v1": 56.3, "hours": 14.8}},
 {"say": "And the view is unreal. From Europa's distance, Jupiter already spans about twelve degrees of sky. Picture twenty three full Moons lined up side by side. As you fall, it grows until there's nothing in front of you but clouds, from one edge of your vision to the other.",
  "vis": {"type": "plunge", "mode": "view"}},
 {"say": "Fall in from even farther away, and you'd hit the top of the air at fifty nine and a half kilometers per second. Over two hundred thousand kilometers per hour. Sixty times faster than a rifle bullet.",
  "vis": {"type": "bignumber", "from": 0, "to": 214000, "suffix": " km/h", "col": HOT18, "caption": "Jupiter's escape speed: 59.5 km/s (NASA fact sheet)"}},

 # ---------- FLOOR 2: ENTRY ----------
 {"say": "Floor two. The entry. We know exactly what this feels like, because we've done it. In December nineteen ninety five, NASA's Galileo probe hit Jupiter's atmosphere at about forty seven kilometers per second.",
  "vis": {"type": "plunge", "mode": "entry", "v0": 47.4, "v1": 47.4, "g": 228}},
 {"say": "Within about a minute, the air slowed it down so violently that the probe felt two hundred and twenty eight times its own weight. The front of its heat shield reached around sixteen thousand degrees, hotter than the surface of the Sun. A person would not survive that first minute.",
  "vis": {"type": "compare", "left": ["GALILEO'S ENTRY", "47 km/s", "228 g of braking", "≈ 16,000 °C on the shield"], "right": ["A HUMAN", "blacks out near 5 g", "can't survive minutes at 50 g", "no suit survives 16,000 °C"], "cols": [HOT18, CREAM], "strike": False}},
 {"say": "So from here on, imagine you're inside an unbreakable capsule. It can't burn and it can't be crushed. It can only fall, and report back. And even after the braking, there's Jupiter's gravity. Two and a half times Earth's. If you weigh seventy kilos at home, you'd feel like a hundred and seventy seven.",
  "vis": {"type": "bignumber", "from": 70, "to": 177, "suffix": " kg", "col": OCH, "caption": "how 70 kg feels in Jupiter's gravity, 2.53 g (our calculation)"}},

 # ---------- FLOOR 3: THE CLOUDS ----------
 {"say": "Floor three. The clouds. The colorful stripes you know from photos are only the top of the weather. Models say there are three cloud decks stacked on top of each other. First, white clouds of ammonia ice, freezing cold.",
  "vis": {"type": "cloudstack", "depth": 10, "hl": 0}},
 {"say": "Below them, a brownish deck of ammonium hydrosulfide, a compound of ammonia and sulfur that smells like rotten eggs. And deeper still, clouds of water, flickering with lightning.",
  "vis": {"type": "cloudstack", "depth": 70, "hl": 2}},
 {"say": "And it's windy. As Galileo sank under its parachute, it measured the winds getting stronger, not weaker, with depth. Over six hundred kilometers per hour, far below the clouds where sunlight never reaches.",
  "vis": {"type": "cloudstack", "depth": 110, "hl": 3, "wind": True}},

 # ---------- FLOOR 4: GALILEO'S LAST STOP ----------
 {"say": "Floor four. About a hundred and fifty kilometers down. This is where our real explorer stopped. After fifty eight minutes of sending data, Galileo went silent. The pressure was about twenty three times Earth's air, and it was around a hundred and fifty degrees.",
  "vis": {"type": "depthgauge", "depth": 150, "ptxt": "≈ 23 bar", "ttxt": "≈ 150 °C", "floor": "GALILEO'S LAST SIGNAL", "note": "58 minutes of data, then silence (December 7, 1995)"}},
 {"say": "That sounds tough, but it's like being two hundred and twenty meters under the sea. Submarines go deeper than that. We've barely scratched Jupiter. Galileo made it through less than a quarter of one percent of the way to the center. At its average pace, the full trip down would take around nineteen days.",
  "vis": {"type": "jupcut", "depth": 150, "hl": "skin", "note": "Galileo's whole dive, to scale"}},

 # ---------- FLOOR 5: WHERE'S THE SURFACE? ----------
 {"say": "Floor five. You'd expect to splash into an ocean somewhere around here. But you never do. Hydrogen, the main ingredient of Jupiter, stops behaving like a normal gas or liquid above about minus two hundred and forty degrees, once it's squeezed hard enough. Here it's hundreds of degrees hotter than that.",
  "vis": {"type": "nosurface", "phase": 0}},
 {"say": "So the air simply gets thicker, and thicker, and thicker. It turns into something like a hot, dark syrup, with no line in between. There's no moment where the sky ends and the sea begins. Your capsule just keeps sinking, slower and slower, through a fluid that never ends.",
  "vis": {"type": "nosurface", "phase": 1}},
 {"say": "Even Jupiter's famous storm goes deep. In twenty twenty one, NASA's Juno spacecraft found that the roots of the Great Red Spot reach up to about five hundred kilometers down. A storm wider than Earth, and taller than the entire layer of air we live in, many times over.",
  "vis": {"type": "depthgauge", "depth": 500, "floor": "THE ROOTS OF THE GREAT RED SPOT", "note": "up to ≈ 500 km deep (Juno, 2021)", "approx": True}},

 # ---------- FLOOR 6: METAL RAIN ----------
 {"say": "Now we go much, much deeper. Floor six, about ten thousand kilometers down. Almost the width of Earth below the clouds. The pressure here is one to two million times Earth's air, and it's around five thousand degrees.",
  "vis": {"type": "depthgauge", "depth": 10000, "ptxt": "1–2 million bar", "ttxt": "≈ 5,000 °C", "floor": "THE METAL OCEAN BEGINS", "note": "≈ 10,000–13,000 km down (models)", "approx": True}},
 {"say": "And something incredible happens to hydrogen. It's squeezed so hard that its electrons break free, and it starts to behave like a liquid metal. It conducts electricity. Churning around, this ocean of metal powers Jupiter's magnetic field, the strongest of any planet.",
  "vis": {"type": "jupcut", "depth": 10000, "hl": "metal", "note": "liquid metallic hydrogen"}},
 {"say": "Right at the top of that metal ocean, scientists think it rains. Not water. Helium. Droplets of helium sink through the hydrogen like rain, and they may carry neon down with them. That would explain why Galileo found so little neon in the air above.",
  "vis": {"type": "nosurface", "phase": 2}},

 # ---------- FLOOR 7: THE FUZZY CORE ----------
 {"say": "Floor seven. For decades, the textbook picture was simple. Deep inside Jupiter, a solid ball of rock and ice, a few times heavier than Earth. Then Juno started measuring Jupiter's gravity, very precisely, orbit after orbit.",
  "vis": {"type": "jupcut", "depth": 30000, "hl": "oldcore", "note": "the old textbook picture"}},
 {"say": "And the answer was a surprise. The heavy stuff isn't packed into a neat ball. It's smeared out, mixed with hydrogen, spread across maybe half of Jupiter's radius. Scientists call it a dilute core. One idea is that a giant collision, long ago, stirred it up.",
  "vis": {"type": "jupcut", "depth": 35000, "hl": "dilute", "note": "the dilute core (Juno gravity data)"}},
 {"say": "How much heavy stuff is in there? Estimates range from about seven to twenty five Earths' worth of rock, ice and metal. It's like dissolving a few whole planets into a giant ball of gas, and stirring.",
  "vis": {"type": "bignumber", "from": 0, "to": 25, "prefix": "7 – ", "suffix": " Earths", "col": VIO18, "caption": "heavy elements in Jupiter's core region (Wahl et al. 2017)"}},

 # ---------- FLOOR 8: THE CENTRE ----------
 {"say": "Floor eight. The center. Seventy thousand kilometers down, five and a half Earths stacked end to end. Models put the temperature around twenty thousand degrees, more than three times hotter than the surface of the Sun. And the pressure? Tens of millions of times what you feel right now.",
  "vis": {"type": "depthgauge", "depth": 69900, "ptxt": "tens of millions of bar", "ttxt": "≈ 20,000 °C", "floor": "THE CENTRE", "note": "temperature and pressure from interior models", "approx": True}},
 {"say": "And even here, there may be no solid floor. You started falling at the top of the air, and you'd end in the middle of a hot, crushed soup. In a sense, you never stopped falling. You just ran out of planet.",
  "vis": {"type": "jupcut", "depth": 69900, "hl": "centre", "note": "no floor at any depth"}},

 # ---------- WHO ALREADY FELL IN ----------
 {"say": "Here's the twist. Things really have fallen into Jupiter, and we watched. In July nineteen ninety four, the comet Shoemaker Levy nine, broken into about twenty one pieces, slammed into Jupiter one piece after another over six days.",
  "vis": {"type": "scars", "phase": 0}},
 {"say": "Each piece hit at about sixty kilometers per second, almost exactly the speed you'd arrive at. The biggest one, fragment G, released energy estimated at around six million megatons of TNT, in a single flash.",
  "vis": {"type": "bignumber", "from": 0, "to": 6000000, "suffix": " Mt", "col": HOT18, "caption": "estimated energy of fragment G, July 18, 1994 (NASA)"}},
 {"say": "The impacts left dark scars in the clouds, some of them bigger than Earth. Backyard telescopes could see them. A comet a few kilometers wide, and it bruised the biggest planet we have.",
  "vis": {"type": "scars", "phase": 1}},
 {"say": "And in twenty oh three, NASA did it on purpose. The Galileo orbiter, low on fuel, was steered into Jupiter at about forty eight kilometers per second, so it could never crash into Europa and contaminate an ocean that might hold life. Somewhere down there, its atoms are still falling.",
  "vis": {"type": "plunge", "mode": "entry", "v0": 48.2, "v1": 48.2, "g": 0, "label": "GALILEO ORBITER · SEPTEMBER 21, 2003"}},

 # ---------- RECAP ----------
 {"say": "So, our fall, floor by floor. Fifty nine kilometers per second at the top. Clouds of ammonia, rotten eggs and water. Galileo's last signal at a hundred and fifty kilometers. An ocean with no surface. Metal rain. A fuzzy core. And no ground anywhere.",
  "vis": {"type": "bullets", "title": "The fall, floor by floor", "items": ["59.5 km/s at the top of the air", "3 cloud decks, 600+ km/h winds", "Galileo's last signal: ≈ 150 km", "metal hydrogen: ≈ 10,000 km", "a dilute core, no floor at all"], "col": OCH}},

 # ---------- NEXT ----------
 {"say": "Next time, we stay closer to home and give Earth a gift. What if we had a second Moon? Tides, nights, and maybe a crash, all change. Subscribe to Cosmic Scale so you don't miss it. And tell me in the comments, which planet should we fall into next?",
  "vis": {"type": "title", "title": "Next: what if Earth\nhad a second Moon?", "sub": "COSMIC SCALE", "subcol": OCH}},
]

SOURCES = ["NASA Jupiter Fact Sheet (NSSDC): equatorial radius 71,492 km at the 1-bar level, mean radius 69,911 km, gravity 24.79 m/s², escape velocity 59.5 km/s",
           "NASA/JPL, Galileo Probe: entered Jupiter's atmosphere on December 7, 1995 at about 47 km/s (106,000 mph); peak deceleration about 228 g; heat shield about 16,000 °C; 58 minutes of data; signal lost at about 23 bar",
           "Seiff et al. (1998) and Atkinson et al. (1998), Journal of Geophysical Research: Galileo probe temperature about 150 °C near 22 bar; winds increasing with depth to about 170 m/s (over 600 km/h)",
           "Cloud decks (thermochemical models): ammonia ice near 0.7 bar, ammonium hydrosulfide near 2.2 bar, water near 5 bar (e.g. Atreya et al.; Juno microwave results)",
           "Hydrogen critical point: about 33 K (−240 °C) and 13 bar; above it there is no boundary between gas and liquid",
           "NASA/JPL (2021): Juno found the Great Red Spot extends up to about 500 km below the cloud tops (Parisi et al. 2021, Science; Bolton et al. 2021)",
           "Metallic hydrogen and helium rain: about 10,000–13,000 km below the cloud tops, 1–2 million bar, about 5,000 °C (Wilson & Militzer 2010; Physics Today; Berkeley Lab)",
           "Dilute core: Wahl et al. (2017), Geophysical Research Letters; Militzer et al. (2022), Planetary Science Journal: 7–25 Earth masses of heavy elements, spread to about half of Jupiter's radius; Liu et al. (2019), Nature: a giant impact may have stirred it",
           "Centre: about 20,000 K and tens of millions of bar in interior models (e.g. Guillot; 40–70 Mbar)",
           "NASA: comet Shoemaker-Levy 9 hit Jupiter July 16–22, 1994 in about 21 fragments; some impact scars were larger than Earth",
           "NASA/JPL: the Galileo orbiter was sent into Jupiter on September 21, 2003 at about 48 km/s to avoid contaminating Europa",
           "Galileo probe: about 166 K (−107 °C) at the 1-bar level; NASA: Jupiter has 317.8 Earth masses, more than twice all the other planets combined; Shoemaker-Levy 9 fragments hit at about 60 km/s, fragment G about 6 million megatons of TNT (NASA/JPL estimates)",
           "Own calculations (Python): from Europa's orbit Jupiter spans 2 × atan(71,492 / 670,900) = 12.2°, about 23 full Moons (0.52° each); fall from rest at Europa's orbit (670,900 km) reaches 56.3 km/s after 14.8 hours; 59.5 km/s = 214,000 km/h, about 60 times a 1 km/s rifle bullet; 24.79 / 9.81 = 2.53 g, so 70 kg feels like 177 kg; 23 bar ≈ 220 m of seawater; centre ≈ 69,900 km = 5.5 Earth diameters; at about 150 km per 58 minutes the trip to the centre would take about 19 days"]
