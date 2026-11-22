# Scale Short #15 — 343 Million Suns Fit Inside Betelgeuse (Cosmic Scale)
# Format: "X inside Y". Betelgeuse radius ~700 times the Sun (NOIRLab/Gemini North release noirlab2523, July 2025; same value as EP05).
# Own calc: volume 700³ = 343,000,000 Suns; Sun = 1,303,500 Earths by volume (NASA fact sheets: 1,412,000 / 1.08321 × 10^12 km³)
# -> ~447 trillion Earths. In the Sun's place its surface sits at 700 × 695,700 km = 3.26 AU (asteroid belt ~2.2–3.2 AU, NASA).
# Hook ≤ 2 s ("That dot is our Sun."), number on frame 0, ends with a question that loops into the hook. Visual NEW: "redgiant". Ties to EP17.
TITLE = "That Dot Is Our Sun. 343 Million of Them Fit Inside Betelgeuse"
THEME = {"accent": (255, 120, 70), "accent2": (255, 215, 140), "tint": (44, 10, 6)}
BIG = {"num": "343 MILLION SUNS", "top": "FIT INSIDE ONE STAR"}

BEATS = [
 {"say": "That dot is our Sun.", "vis": {"type": "redgiant", "mode": "hook"}},
 {"say": "The wall next to it is Betelgeuse, the red shoulder of Orion. About seven hundred times wider than the Sun.",
  "vis": {"type": "redgiant", "mode": "zoom", "head": {"num": "700× WIDER", "top": "BETELGEUSE vs THE SUN"}}},
 {"say": "Seven hundred wide, seven hundred deep, seven hundred tall. That's three hundred forty three million Suns inside.",
  "vis": {"type": "redgiant", "mode": "cube"}},
 {"say": "And every Sun holds one point three million Earths. So Betelgeuse could swallow about four hundred fifty trillion Earths.",
  "vis": {"type": "redgiant", "mode": "earths", "head": {"num": "447 TRILLION", "top": "EARTHS, BY VOLUME"}}},
 {"say": "Put it where our Sun is, and Mercury, Venus, Earth and Mars are all inside it.",
  "vis": {"type": "redgiant", "mode": "orbits", "head": {"num": "3.3 AU", "top": "BETELGEUSE IN THE SUN'S PLACE"}}},
 {"say": "You can see it tonight, no telescope needed. So, which star should we put next to the Sun?",
  "vis": {"type": "redgiant", "mode": "orion", "head": {"num": "343 MILLION SUNS", "top": "LOOK UP TONIGHT"}}},
]

SOURCES = ["NSF NOIRLab / Gemini North release noirlab2523 (July 2025): Betelgeuse has a radius about 700 times the Sun's",
           "NASA Sun Fact Sheet (NSSDC): mean radius 695,700 km, volume 1,412,000 × 10^12 km³; NASA Earth Fact Sheet: volume 1.08321 × 10^12 km³",
           "Own calculations: 700 × 700 × 700 = 343 million Suns by volume; × 1.3 million Earths per Sun ≈ 447 trillion Earths; 700 Sun radii ≈ 3.26 times the Earth–Sun distance",
           "NASA: the main asteroid belt lies roughly 2.2 to 3.2 times the Earth–Sun distance from the Sun"]
