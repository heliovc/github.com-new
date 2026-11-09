# EP07 — Neutron Star: A Teaspoon Weighs More Than All of Humanity
# Structure NEW: "a flight to a dead star" — teaspoon paradox hook (opens loop: it would EXPLODE on Earth) -> 1967 mystery signal (LGM-1)
# -> how to make one (collapse in half a second) -> how small (Sun in a city; Earth squeezed = 300 m ball) -> RE-ENGAGE 1 (~3:00): why the
# teaspoon explodes -> approach: magnetic field + 2004 magnetar flare -> surface: gravity, 1 m drop at 1,600 km/s, mountains < 1 mm,
# you'd see the back side -> spin 716/s, equator ~1/5 of light speed -> RE-ENGAGE 2 (~6:00, biggest scale): collisions forge gold (GW170817)
# -> payoff -> EP08 (What If the Moon Crashed Into Earth?).
# Palette electric blue / coral (+ gold only in the merger). New scenes: teaspoon, pulsechart, crush, lensing, pulsar, merger.
# Own calculations (Python): mean density of a 1.4 Msun, 12 km radius star = 3.8e17 kg/m^3 -> 5 mL teaspoon = 1.9e12 kg (≈ 2 billion
# tonnes); 8.2 billion people x 62 kg ≈ 0.5 billion tonnes; surface gravity 1.3e12 m/s^2 = 1.3e11 g; drop from 1 m -> 1,600 km/s
# (Newtonian); escape speed 0.59 c; Earth at that density = radius 155 m (310 m across, Eiffel Tower 330 m);
# 716 Hz at r = 12 km -> 54,000 km/s = 18% of light speed (24% if r = 16 km).
TITLE = "A Teaspoon of This Star Outweighs All of Humanity"
BLUE = [91, 140, 255]
CORAL = [255, 111, 145]
PALE = [200, 220, 255]

SCENES = [
 # ---------- HOOK ----------
 {"say": "One teaspoon of this star would weigh about two billion tonnes. That's more than every human being on Earth, all eight billion of us, put together. And here's the strange part. If you could actually bring that teaspoon home, it wouldn't sit quietly on a scale. It would explode.",
  "vis": {"type": "teaspoon", "head": "1 teaspoon ≈ 2,000,000,000 tonnes", "phase": 0}},
 {"say": "So today we're flying to a neutron star. First, the signal that made astronomers whisper about aliens. Then how a star gets crushed into a ball the size of a city. Then we'll get close. Close enough to see why that teaspoon explodes, why mountains there are smaller than a grain of sand, and why some of the gold on your finger may have come from two of these stars colliding.",
  "vis": {"type": "bullets", "title": "Flight plan", "items": ["1. A signal from nowhere", "2. Crushing a star", "3. Why the teaspoon explodes", "4. Landing (don't)", "5. Where gold comes from"], "col": BLUE}},
 {"say": "A Teaspoon of a Neutron Star.",
  "vis": {"type": "title", "title": "A Teaspoon of a\nNeutron Star", "sub": "COSMIC SCALE", "brand": True, "subcol": CORAL}},

 # ---------- THE SIGNAL ----------
 {"say": "Cambridge, England, nineteen sixty seven. A graduate student named Jocelyn Bell is checking the output of a new radio telescope, a field of wires and poles the size of fifty seven tennis courts. It prints its data on paper, about two hundred meters of chart every week. And in one corner of the sky, she notices a bit of what she calls scruff.",
  "vis": {"type": "pulsechart", "head": "Cambridge, 1967", "period": 1.33, "phase": 0}},
 {"say": "The scruff turns out to be pulses. Perfectly regular. One every one point three three seconds, like a cosmic metronome. Nothing natural was known to tick that precisely, so the team half jokingly labeled it L G M one. Little green men. But then she found a second one, in a completely different part of the sky. Two alien civilizations, signaling on the same kind of schedule? Unlikely. The real answer was stranger. These were spinning, dead stars. Pulsars. Today we know a few thousand of them, and NASA estimates our galaxy hides tens to hundreds of millions of neutron stars.",
  "vis": {"type": "pulsechart", "head": "LGM-1: \"Little Green Men\"", "period": 1.33, "phase": 1}},

 # ---------- HOW TO MAKE ONE ----------
 {"say": "So how do you make one? Start with a star at least eight times heavier than the Sun. At the end of its life, its core is a ball of iron about the size of Earth, holding roughly one and a half times the mass of the Sun. Iron can't be burned for energy. So when the fuel around it runs out, nothing holds the core up.",
  "vis": {"type": "crush", "phase": 0, "head": "An Earth-sized ball of iron"}},
 {"say": "It collapses. The core falls inward at about a quarter of the speed of light. In half a second or less, a ball the size of a planet becomes a ball about thirty kilometers across. Electrons are forced into protons, turning them into neutrons. The outer layers of the star bounce off this new, ultra hard core and blast out into space as a supernova. What's left behind is a neutron star.",
  "vis": {"type": "crush", "phase": 1, "head": "Half a second later"}},
 {"say": "Here's how small that is. A typical neutron star holds more mass than the Sun, packed into a sphere about twenty kilometers wide. The size of a city. Our own Sun is about one point four million kilometers across. And if you squeezed the whole Earth to the same density, by our calculation it would become a ball about three hundred meters across. Shorter than the Eiffel Tower.",
  "vis": {"type": "compare", "left": ["THE SUN", "1.4 million km wide", "a normal star", ""], "right": ["NEUTRON STAR", "≈ 20 km wide", "more mass than the Sun", "Earth at this density: ≈ 300 m"], "cols": [CORAL, BLUE], "strike": False}},

 # ---------- RE-ENGAGE 1: WHY THE TEASPOON EXPLODES ----------  # REENGAJE (~3:00)
 {"say": "Now, back to that teaspoon. By our calculation, an average neutron star is about four hundred million tonnes per cubic centimeter. A sugar cube of it, NASA says, would weigh around a billion tons. So why would it explode on Earth? Because that density isn't natural for matter. It's forced. The star's own gravity is the only thing holding those neutrons together. Scoop out a teaspoon and that grip is gone. The pressure inside takes over all at once, and the matter expands violently. As one astronomer put it, a spoonful of neutron star appearing on Earth would cause a giant explosion, and probably vaporize a good chunk of the planet. The teaspoon is only heavy while it's home.",
  "vis": {"type": "teaspoon", "head": "Only heavy while it's home", "phase": 1}},

 # ---------- APPROACH: MAGNETISM ----------
 {"say": "So let's leave the teaspoon and go there instead. Long before you arrive, you'd feel it. Not the gravity, the magnetism. When the star collapsed, its magnetic field was squeezed along with it. NASA says neutron stars have magnetic fields billions to trillions of times stronger than Earth's. And a special kind, called a magnetar, is about a thousand times stronger still.",
  "vis": {"type": "ladder", "title": "Magnetic field, times Earth's", "max": 15, "items": [["Earth", 0, 0, "#7FD6FF"], ["Neutron star", 9, 12, "#5B8CFF"], ["Magnetar", 15, 15, "#FF6F91"]], "notes": ["1×", "billions to trillions ×", "≈ 1,000× more"], "caption": "log scale: each step = 1,000×"}},
 {"say": "How strong is that? On December twenty seventh, two thousand four, a magnetar called S G R eighteen oh six minus twenty had a starquake. In about a fifth of a second, it released as much energy as our Sun puts out in two hundred and fifty thousand years. It was roughly fifty thousand light years away, on the far side of the galaxy. And it still squeezed Earth's own magnetic field.",
  "vis": {"type": "bignumber", "from": 0, "to": 250000, "decimals": 0, "suffix": " years", "col": CORAL, "caption": "of Sun's output, released in 0.2 seconds (SGR 1806-20, 2004)"}},

 # ---------- THE SURFACE ----------
 {"say": "Now get close to the surface. The gravity here is, by our calculation, about a hundred billion times what you feel on Earth. Drop a pen from one meter up, and it would hit the ground at around sixteen hundred kilometers per second. To escape, you'd need to fly at more than half the speed of light. Gravity this strong flattens everything. Researchers at the University of Southampton calculated that the tallest mountains on a neutron star are less than a millimeter high.",
  "vis": {"type": "bullets", "title": "On the surface", "items": ["gravity ≈ 100 billion × Earth's", "1 m drop → 1,600 km/s", "escape: > half the speed of light", "tallest mountain: < 1 mm"], "col": CORAL, "highlight": 3}},
 {"say": "And the view would break your brain. Gravity this strong bends light. Light leaving the far side of the star curves around it and reaches your eyes. So from one spot, you would see more than half of the surface at once, including part of the back. NASA's NICER telescope, on the International Space Station, uses exactly this effect. In twenty nineteen, it mapped hot spots on a pulsar called J zero zero three zero, eleven hundred light years away, and measured its size. About twenty six kilometers wide, with about one point four times the mass of the Sun.",
  "vis": {"type": "lensing", "head": "You'd see its back side"}},

 {"say": "And underneath that surface? Nobody has ever seen it, but physicists have a picture. On top, a thin crust of atomic nuclei locked into a crystal. Deeper down, the nuclei are squeezed so tightly that they merge into long strands and flat sheets. Physicists actually call it nuclear pasta, with shapes nicknamed spaghetti and lasagna. Computer simulations published in twenty eighteen suggest it could be the strongest material in the universe, around ten billion times stronger than steel. Below that, a sea of neutrons. And at the very center? Nobody knows yet. The matter there is crushed beyond anything we can make in a lab.",
  "vis": {"type": "layers", "head": "Inside a neutron star", "items": [["crust", 1.0, "#9DB8FF", "nuclei locked in a crystal"], ["nuclear pasta", 0.9, "#FF6F91", "≈ 10 billion × stronger than steel"], ["neutron sea", 0.78, "#5B8CFF", "mostly neutrons"], ["core: ?", 0.4, "#1B2450", "nobody knows yet"]]}},

 # ---------- SPIN ----------
 {"say": "And it's spinning. A collapsing star spins faster as it shrinks, like a figure skater pulling in her arms. The first pulsar turned once every one point three three seconds. The fastest one known, discovered in two thousand five in the star cluster Terzan five, turns seven hundred and sixteen times every second. Its beams sweep past us like a lighthouse gone mad.",
  "vis": {"type": "pulsar", "hz": 716, "head": "716 turns every second", "sub": "PSR J1748-2446ad · Terzan 5 · 28,000 light-years"}},
 {"say": "NASA compares it to forty three thousand turns per minute, twice as fast as a kitchen blender. Except this blender has more mass than the Sun. By our calculation, a point on its equator moves at around fifty thousand kilometers per second. That's roughly a fifth of the speed of light. Spin it much faster, and the star would start to tear itself apart.",
  "vis": {"type": "bignumber", "from": 0, "to": 54000, "decimals": 0, "suffix": " km/s", "col": BLUE, "caption": "speed at its equator ≈ 1/5 of the speed of light (our calculation)"}},

 # ---------- RE-ENGAGE 2: COLLISIONS + GOLD ----------  # REENGAJE (~6:00)
 {"say": "Now the biggest scale of all. Sometimes two neutron stars orbit each other. They slowly spiral together, and when they finally hit, the universe rings like a bell. On August seventeenth, twenty seventeen, gravitational wave detectors on Earth felt that ringing. Two neutron stars had collided in a galaxy called N G C forty nine ninety three, about a hundred and thirty million light years away. The ripple had been traveling since the age of the dinosaurs.",
  "vis": {"type": "merger", "phase": 0, "head": "August 17, 2017"}},
 {"say": "Within hours, telescopes around the world turned to look, and they saw the fireball. It was full of freshly made heavy elements. Harvard astronomer Edo Berger estimated that this one collision produced about ten times the mass of Earth in gold and platinum alone. Collisions like this are now thought to forge much of the universe's gold. Billions of years ago, some of that gold drifted into the cloud of gas that became our solar system. So if you're wearing gold, some of it may have been made by two dead stars smashing together.",
  "vis": {"type": "merger", "phase": 1, "head": "≈ 10 Earth masses of gold and platinum"}},

 # ---------- PAYOFF + NEXT ----------
 {"say": "So that's a neutron star. A city sized ball, heavier than the Sun, spinning hundreds of times a second, where a teaspoon outweighs all of humanity, and only stays that way because it never leaves home. Now picture something much closer, and much heavier than any teaspoon. Our Moon weighs about seventy three billion billion tonnes. In the last episode we saw it drifting away. But what if it came back, and crashed into Earth? That's next.",
  "vis": {"type": "title", "title": "Next:\nWhat If the Moon\nCrashed Into Earth?", "sub": "COSMIC SCALE", "brand": False, "subcol": CORAL}},
]

SOURCES = [
 "NASA Science, \"Neutron Stars Are Weird!\": made by stars of roughly 7 to 19 solar masses; up to two solar masses in a city-size sphere; a sugar cube of neutron star material would weigh about 1 billion tons; magnetic fields billions to trillions of times Earth's, magnetars about a thousand times stronger; fastest known pulsar spins 43,000 times a minute, twice as fast as a household blender",
 "Smithsonian Magazine, \"Fifty Years Ago, a Grad Student's Discovery Changed the Course of Astrophysics\": Jocelyn Bell, 1967, pulses 1.33 seconds apart, \"scruff\", LGM-1, array the size of 57 tennis courts, about 700 feet of chart paper per week",
 "Astronomy magazine, \"What makes stars explode?\" (2019): Earth-sized iron core of about 1.5 solar masses collapses at about a quarter of light speed, in half a second or less, to a proto-neutron star about 30 km across",
 "Astronomy magazine, Ask Astro (August 2018), Valerie Mikles: a spoonful of neutron star on Earth would expand and cause a giant explosion, probably vaporizing a good chunk of the planet",
 "EarthSky, \"What is a magnetar?\" and Science News (2005): SGR 1806-20 giant flare, 27 December 2004, about 0.2 seconds, as much energy as the Sun emits in 250,000 years, about 50,000 light-years away; it compressed Earth's magnetic field",
 "University of Southampton / Royal Astronomical Society, Gittins et al. (NAM 2021): neutron star mountains are a fraction of a millimeter tall",
 "Astronomy magazine (Dec 2019), NASA NICER: PSR J0030+0451, 1.3–1.4 solar masses, about 26 km wide, 1,100 light-years away; gravity bends light so the far side is visible",
 "McGill University / NRAO, Hessels et al. (Science, 2006): PSR J1748-2446ad spins 716 times per second, Terzan 5, about 28,000 light-years, Green Bank Telescope",
 "Space.com (Oct 2017), LIGO/Virgo GW170817: neutron star merger on 17 August 2017 in NGC 4993, about 130 million light-years away; Edo Berger (Harvard): about 10 Earth masses of gold and platinum",
 "NASA Moon fact sheet: mass 7.35 × 10^22 kg",
 "Walpole et al. (2012), BMC Public Health: average adult body mass about 62 kg (used for the estimate of the mass of all humans)",
 "Phys.org (Sept 2018), Caplan, Schneider and Horowitz, Physical Review Letters: nuclear pasta may be about 10 billion times stronger than steel",
 "NASA (May 2026), Roman Space Telescope: tens to hundreds of millions of neutron stars in the Milky Way, only a few thousand known",
 "Own calculations (Python): mean density of a 1.4-solar-mass, 12 km-radius neutron star (3.8 × 10^17 kg/m³), teaspoon of 5 mL ≈ 1.9 billion tonnes, total human mass under 0.6 billion tonnes, surface gravity ≈ 1.3 × 10^11 g, 1 m drop ≈ 1,600 km/s, escape speed ≈ 0.59 c, Earth at that density ≈ 310 m across, equator speed at 716 turns per second ≈ 54,000 km/s",
]
