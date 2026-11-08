# Ranking #5 — Top 5 Biggest Black Holes Ever Found (Cosmic Scale)
# Visual NEW: "horizons" — event horizons drawn to ONE fixed scale (1,974 AU = 430 px) against our Solar System (Neptune's orbit, a tiny
# gold dot) and Voyager 1's distance (~1 light-day, dashed). Revealed horizons stay as dashed rings. Hook = "?" horizon swallowing the
# Solar System; outro = all five rings. Theme deep violet / white.
# Own calculations: Schwarzschild radius = 2.953 km x M/Msun; 1 AU = 1.496e8 km; light-day = 173.1 AU.
# NGC 4889 21e9 -> 415 AU (10x Pluto); Cosmic Horseshoe 36e9 -> 711 AU; Holm 15A 40e9 -> 790 AU (Voyager 1 ~170 AU = 22%);
# TON 618 66e9 -> 1,303 AU; Phoenix A 100e9 -> 1,974 AU = 11.4 light-days, 66x the diameter of Neptune's orbit (60 AU).
TITLE = "Top 5 Biggest Black Holes Ever Found"
THEME = {"accent": (185, 140, 255), "accent2": (240, 240, 255), "star_col": (255, 170, 90), "tint": (34, 10, 70),
         "bar": "THE 5 BIGGEST BLACK HOLES EVER FOUND", "hook": "horizons", "outro": "horizons",
         "outro_note": "#1 is 66 times wider than our whole solar system"}

HOOK = {"say": "The number one black hole on this list is sixty six times wider than our entire solar system. These are the five biggest black holes ever found.",
        "top": "Biggest black holes ever found", "sub": "#1 is 66× wider than our solar system"}

ITEMS = [
 {"rank": 5, "name": "NGC 4889", "short": "NGC 4889", "tag": "in the Coma Cluster", "num": 21, "suffix": " BILLION", "unit": "times the mass of the Sun",
  "source": "McConnell et al., Nature (2011)", "vis": {"type": "horizons", "au": 415, "note": "horizon: 10× farther out than Pluto"},
  "say": "Number five. NGC forty eight eighty nine, in the Coma Cluster. About twenty one billion times the mass of the Sun. Its edge, the event horizon, would reach ten times farther out than Pluto."},
 {"rank": 4, "name": "Cosmic Horseshoe", "short": "Horseshoe", "tag": "found in 2025", "num": 36, "suffix": " BILLION", "unit": "times the mass of the Sun",
  "source": "Melo-Carneiro et al., MNRAS (2025)", "vis": {"type": "horizons", "au": 711, "note": "its gravity bends light into a horseshoe"},
  "say": "Number four. The Cosmic Horseshoe black hole. Thirty six billion Suns. Found in twenty twenty five, because its gravity bends the light of a galaxy behind it into a glowing horseshoe."},
 {"rank": 3, "name": "Holm 15A", "short": "Holm 15A", "tag": "measured from its stars", "num": 40, "suffix": " BILLION", "unit": "times the mass of the Sun",
  "source": "Max Planck Institute / Mehrgan et al. (2019)", "vis": {"type": "horizons", "au": 790, "note": "Voyager 1 hasn't flown a quarter of that"},
  "say": "Number three. Holm fifteen A. About forty billion Suns, weighed directly from the motion of the stars around it. Voyager 1, after almost fifty years in flight, hasn't covered even a quarter of its horizon's radius."},
 {"rank": 2, "name": "TON 618", "short": "TON 618", "tag": "a blazing quasar", "num": 66, "suffix": " BILLION", "unit": "times the mass of the Sun (estimate)",
  "source": "Shemmer et al. (2004)", "vis": {"type": "horizons", "au": 1303, "note": "horizon: 1,300× the Earth–Sun distance"},
  "say": "Number two. TON six eighteen, a blazing quasar more than ten billion light years away. Estimated at sixty six billion Suns. Its horizon alone is about thirteen hundred times the distance from Earth to the Sun."},
 {"rank": 1, "name": "Phoenix A", "short": "Phoenix A", "tag": "heart of the Phoenix Cluster", "num": 100, "suffix": " BILLION", "unit": "times the mass of the Sun (upper estimate)",
  "source": "Brockamp et al. (2016)", "vis": {"type": "horizons", "au": 1974, "note": "light needs 11 days to cross its radius"},
  "say": "And number one. Phoenix A, at the heart of the Phoenix galaxy cluster. Estimates go as high as a hundred billion Suns. Its horizon would be sixty six times wider than our solar system. Light would need more than eleven days just to cross its radius."},
]

OUTRO = {"say": "And that's only an estimate. Subscribe to Cosmic Scale for more."}

SOURCES = ["McConnell et al. (2011), Nature: NGC 4889 black hole about 21 billion solar masses (Coma Cluster)",
           "Melo-Carneiro et al. (2025), MNRAS 541: Cosmic Horseshoe black hole about 36 billion solar masses, measured with gravitational lensing and stellar motions",
           "Max Planck Institute for Extraterrestrial Physics / Mehrgan et al. (2019), ApJ: Holm 15A about 40 billion solar masses, direct stellar-dynamical measurement",
           "Shemmer et al. (2004), ApJ: TON 618 quasar, black hole estimated at about 66 billion solar masses",
           "Brockamp et al. (2016): Phoenix A, up to about 100 billion solar masses (model estimate, not a direct measurement)",
           "NASA JPL: Voyager 1 about 170 times the Earth–Sun distance, reaching one light-day in November 2026",
           "Own calculations: event horizon radius = 2.95 km per solar mass; light-day = 173 AU; Neptune's orbit about 60 AU across"]
