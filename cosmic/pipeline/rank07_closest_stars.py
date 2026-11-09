# Ranking #7 — Top 5 Closest Stars to the Sun (Cosmic Scale)
# Star systems by distance (brown dwarfs like Luhman 16 excluded: they are not stars). Alpha Centauri A and B counted as one entry.
# Visual NEW: "lightyears" — a vertical light-year ruler (Sun at the bottom, 0–9 ly) with a light pulse travelling down to us,
# each star placed at its true distance, + "the light you see tonight left it in YEAR" (2026.86 − distance).
# Hook: big number in frame 0 ("40 TRILLION KM") + "?" star at 4.24 ly. Outro: full ruler + question "Which star should we put next?"
# Theme NEW: rose / steel blue. Own calc: 1 ly = 9.4607 trillion km; Voyager 1 times scaled from NASA's "over 73,000 years" to Proxima.
TITLE = "Top 5 Closest Stars to the Sun"
THEME = {"accent": (255, 130, 160), "accent2": (190, 215, 255), "star_col": (255, 130, 160), "tint": (20, 26, 52),
         "bar": "THE 5 CLOSEST STARS TO THE SUN", "hook": "lightyears", "outro": "lightyears",
         "outro_note": "Proxima's light left it in 2022"}

HOOK = {"say": "Forty trillion kilometers. That's the shortest trip to another star. These are the five closest stars to the Sun.",
        "big": "40 TRILLION KM", "top": "to the nearest star", "sub": "#1: Voyager would need 73,000 years"}

ITEMS = [
 {"rank": 5, "name": "Lalande 21185", "short": "Lalande 21185", "tag": "a red dwarf in Ursa Major", "num": 8.31, "dec": 2, "suffix": " LY", "unit": "light-years away",
  "source": "NASA / RECONS nearest-stars list", "vis": {"type": "lightyears", "ly": 8.31, "col": (255, 120, 90), "r": 95, "note": "too faint to see without binoculars"},
  "say": "Number five. Lalande twenty one one eight five, a red dwarf eight point three light years away. One of the brightest red dwarfs in our sky, and still too faint to see without binoculars."},
 {"rank": 4, "name": "Wolf 359", "short": "Wolf 359", "tag": "one of the faintest stars known", "num": 7.86, "dec": 2, "suffix": " LY", "unit": "light-years away",
  "source": "NASA / RECONS nearest-stars list", "vis": {"type": "lightyears", "ly": 7.86, "col": (255, 100, 80), "r": 70, "note": "about a tenth of the Sun's mass"},
  "say": "Number four. Wolf three five nine, seven point nine light years away. A tiny red dwarf with only about a tenth of the Sun's mass."},
 {"rank": 3, "name": "Barnard's Star", "short": "Barnard's", "tag": "the fastest-moving star in our sky", "num": 5.96, "dec": 2, "suffix": " LY", "unit": "light-years away",
  "source": "NASA / RECONS nearest-stars list", "vis": {"type": "lightyears", "ly": 5.96, "col": (255, 135, 95), "r": 80, "note": "it drifts across our sky faster than any other star"},
  "say": "Number three. Barnard's Star, about six light years away. No other star drifts across our night sky faster."},
 {"rank": 2, "name": "Alpha Centauri A & B", "short": "Alpha Cen A+B", "tag": "a pair of Sun-like stars", "num": 4.37, "dec": 2, "suffix": " LY", "unit": "light-years away",
  "source": "NASA", "vis": {"type": "lightyears", "ly": 4.37, "col": (255, 225, 150), "pair": (255, 190, 120), "r": 125, "note": "the third-brightest star in the night sky"},
  "say": "Number two. Alpha Centauri A and B. Two Sun like stars orbiting each other, four point three seven light years away. Together, the third brightest star in the night sky."},
 {"rank": 1, "name": "Proxima Centauri", "short": "Proxima", "tag": "a red dwarf with a planet", "num": 4.24, "dec": 2, "suffix": " LY", "unit": "light-years ≈ 40 trillion km",
  "source": "NASA", "vis": {"type": "lightyears", "ly": 4.24, "col": (255, 110, 85), "r": 75, "note": "Voyager 1 would need over 73,000 years"},
  "say": "And number one. Proxima Centauri. Four point two four light years. Even at Voyager one's speed, the trip would take more than seventy three thousand years."},
]

OUTRO = {"say": "The light from Proxima left it in twenty twenty two. Which star should we put next? Subscribe to Cosmic Scale."}

SOURCES = ["NASA Imagine the Universe, \"The Nearest Star\": Proxima Centauri about 4.2 light-years; at Voyager's speed the trip would take over 73,000 years",
           "NASA Science, Alpha Centauri: Alpha Centauri A and B about 4.37 light-years, third-brightest star in the night sky",
           "RECONS (Research Consortium on Nearby Stars) / NASA nearest-stars lists: Barnard's Star 5.96 ly, Wolf 359 7.86 ly, Lalande 21185 8.31 ly",
           "Barnard's Star has the largest proper motion of any star (Barnard, 1916)",
           "Wolf 359: about 0.11 solar masses; Lalande 21185: apparent magnitude about 7.5 (binoculars needed)",
           "Own calculations: 1 light-year = 9.46 trillion km (4.24 ly ≈ 40 trillion km); year the light left = November 2026 minus distance"]
