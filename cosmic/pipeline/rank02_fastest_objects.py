# Ranking #2 — Top 5 Fastest Objects Ever Measured (Cosmic Scale)
# Visual: "speed lanes" on a logarithmic scale (1 km/s -> speed of light), cyan/blue theme, streak hook. kms = speed in km/s.
TITLE = "Top 5 Fastest Objects Ever Measured"
THEME = {"accent": (90, 220, 255), "accent2": (190, 240, 255), "star_col": (120, 200, 255), "tint": (10, 50, 90),
         "bar": "THE 5 FASTEST THINGS EVER MEASURED", "hook": "streaks", "outro_note": "light: 299,792 km/s — still #0"}

HOOK = {"say": "Number one could race a beam of light across the entire Milky Way, and lose by about four millimeters. These are the five fastest things ever measured.",
        "top": "Fastest things ever measured", "sub": "#1 almost ties with light"}

ITEMS = [
 {"rank": 5, "name": "Voyager 1", "short": "Voyager 1", "tag": "leaving the solar system since 1977", "num": 61000, "suffix": "", "unit": "km/h  ·  about 17 km/s",
  "source": "NASA", "vis": {"type": "speed", "kms": 16.9},
  "say": "Number five. Voyager one. About sixty one thousand kilometers per hour, fast enough to escape the Sun forever."},
 {"rank": 4, "name": "Parker Solar Probe", "short": "Parker Probe", "tag": "fastest object humans ever built", "num": 692000, "suffix": "", "unit": "km/h  ·  about 192 km/s",
  "source": "NASA (Dec 24, 2024)", "vis": {"type": "speed", "kms": 192},
  "say": "Number four. NASA's Parker Solar Probe. Diving past the Sun in December twenty twenty four, it hit about six hundred and ninety thousand kilometers per hour. New York to Tokyo in under a minute."},
 {"rank": 3, "name": "S5-HVS1", "short": "S5-HVS1", "tag": "a star thrown out of the Milky Way", "num": 1755, "suffix": "", "unit": "km/s",
  "source": "Koposov et al., MNRAS (2019)", "vis": {"type": "speed", "kms": 1755},
  "say": "Number three. A star called S five H V S one. Our galaxy's central black hole flung it away at about one thousand seven hundred and fifty kilometers per second. It's leaving the Milky Way, and never coming back."},
 {"rank": 2, "name": "S4714", "short": "S4714", "tag": "orbiting our galaxy's black hole", "num": 24000, "suffix": "", "unit": "km/s  ·  8% of light speed",
  "source": "Peissker et al., ApJ (2020) / ESO VLT", "vis": {"type": "speed", "kms": 24000},
  "say": "Number two. S forty seven fourteen. A star whipping around that same black hole at about twenty four thousand kilometers per second. That's eight percent of the speed of light."},
 {"rank": 1, "name": "Oh-My-God particle", "short": "OMG particle", "tag": "a single proton · Utah, 1991", "num": "99.99…%", "unit": "of light speed (23 nines in a row)",
  "source": "Fly's Eye (1991) / Scientific American", "vis": {"type": "speed", "kms": 299792},
  "say": "And number one. The Oh My God particle. A single proton that hit our atmosphere in nineteen ninety one, carrying the energy of a pitched baseball. It was so close to light speed that in a race across the whole Milky Way, light would win by about four millimeters."},
]

OUTRO = {"say": "And light itself stays undefeated. Nothing with mass can ever catch it. Subscribe to Cosmic Scale for more."}

SOURCES = ["NASA Science, Voyager 1: What Is a Light-Day (cruising at nearly 38,000 mph / 61,000 km/h)",
           "NASA Science, Parker Solar Probe Reports Successful Closest Approach to Sun (Dec 24, 2024: about 430,000 mph)",
           "Koposov et al. (2019), The Great Escape: discovery of a nearby 1700 km/s star ejected from the Milky Way by Sgr A* (MNRAS)",
           "Peissker et al. (2020), Astrophysical Journal: S4714 at about 24,000 km/s (ESO Very Large Telescope data)",
           "Scientific American, Where did the 'Oh-My-God' particle come from? (Fly's Eye, 1991, ~3.2×10^20 eV)",
           "Own calculation: a 3.2×10^20 eV proton (Lorentz factor ~3.4×10^11) loses to light by ~4 mm over 100,000 light-years"]
