# Ranking #12 — Top 5 Fastest Winds Ever Measured (Cosmic Scale)
# Ranked by top wind speed (km/h). Visual NEW: "wind" (banded world with cloud streaks racing at a visible, log-scaled speed + log wind
# meter 100–50,000 km/h with a Cat 5 hurricane, an airliner and the speed of sound as reference marks).
# Hook: big number in frame 0 ("33,000 KM/H") + a streaming "?" world; spoken hook "Thirty three thousand kilometers an hour." (≤ 2 s).
# Outro: all five on the meter + "Which world should we put next?". Theme NEW: storm cyan / hot pink on a slate-blue tint.
# Own calc: 33,000 / 1,235 ≈ 27 times the speed of sound at sea level; 33,000 / 408 ≈ 81 times Earth's record gust.
TITLE = "Top 5 Fastest Winds Ever Measured"
THEME = {"accent": (90, 230, 255), "accent2": (255, 110, 200), "star_col": (200, 230, 255), "tint": (14, 28, 60),
         "bar": "TOP 5 FASTEST WINDS EVER MEASURED", "hook": "wind", "outro": "wind", "outro_note": "#1 is 27 times the speed of sound"}

HOOK = {"say": "Thirty three thousand kilometers an hour. These are the five fastest winds ever measured.",
        "big": "33,000 KM/H", "top": "the fastest wind ever measured", "sub": "#1 isn't in our solar system"}

ITEMS = [
 {"rank": 5, "name": "Earth", "short": "Earth", "tag": "Barrow Island, Australia, 1996", "num": "408 km/h", "unit": "strongest gust ever recorded",
  "source": "World Meteorological Organization", "vis": {"type": "wind", "kmh": 408, "col": (70, 130, 230), "earth": True, "r": 230, "note": "a gust during Cyclone Olivia"},
  "say": "Number five. Earth. During a cyclone in nineteen ninety six, a weather station in Australia recorded a gust of four hundred and eight kilometers per hour."},
 {"rank": 4, "name": "Saturn", "short": "Saturn", "tag": "winds at the equator", "num": "1,800 km/h", "unit": "top wind speed",
  "source": "NASA", "vis": {"type": "wind", "kmh": 1800, "col": (225, 200, 140), "r": 260, "note": "faster than the speed of sound on Earth"},
  "say": "Number four. Saturn. Its equatorial winds reach about eighteen hundred kilometers per hour. Faster than sound on Earth."},
 {"rank": 3, "name": "Neptune", "short": "Neptune", "tag": "the windiest planet in the solar system", "num": "2,000 km/h", "unit": "top wind speed",
  "source": "NASA", "vis": {"type": "wind", "kmh": 2000, "col": (80, 120, 240), "r": 240, "note": "the coldest, darkest giant, and the windiest"},
  "say": "Number three. Neptune. Thirty times farther from the Sun than Earth, and still its winds blow at more than two thousand kilometers per hour."},
 {"rank": 2, "name": "HD 189733b", "short": "HD 189733b", "tag": "a hot Jupiter, 64 light-years away", "num": "8,700 km/h", "unit": "winds measured from Earth",
  "source": "Louden & Wheatley 2015, Univ. of Warwick", "vis": {"type": "wind", "kmh": 8700, "col": (60, 110, 220), "r": 240, "note": "the first wind map of a planet beyond the Sun"},
  "say": "Number two. A giant planet orbiting another star, sixty four light-years away. Astronomers measured winds of about eight thousand seven hundred kilometers per hour."},
 {"rank": 1, "name": "WASP-127b", "short": "WASP-127b", "tag": "a puffy giant, 500 light-years away", "num": "33,000 km/h", "unit": "supersonic jet stream",
  "source": "ESO, Nortmann et al. 2025", "vis": {"type": "wind", "kmh": 33000, "col": (130, 100, 210), "r": 270, "note": "about 9 km every second"},
  "say": "And number one. WASP one twenty seven b. A jet stream circling the whole planet at thirty three thousand kilometers per hour, about nine kilometers every second."},
]

OUTRO = {"say": "That's twenty seven times the speed of sound. Which world should we put next? Subscribe to Cosmic Scale."}

SOURCES = ["World Meteorological Organization: 408 km/h gust at Barrow Island, Australia, on 10 April 1996 (Tropical Cyclone Olivia), the highest wind gust recorded on Earth that was not in a tornado",
           "NASA: winds in Saturn's upper atmosphere reach about 500 m/s (about 1,800 km/h) near the equator",
           "NASA: Neptune's winds reach more than 2,000 km/h (1,200 mph), the fastest in the solar system",
           "Louden & Wheatley (2015), Astrophysical Journal Letters (University of Warwick): winds of about 8,700 km/h (5,400 mph) on exoplanet HD 189733b, about 64 light-years away",
           "ESO (January 2025), Nortmann et al., Astronomy & Astrophysics: a supersonic jet stream of up to 33,000 km/h (about 9 km/s) on exoplanet WASP-127b, about 500 light-years away",
           "Own calculations: speed of sound in air at sea level about 1,235 km/h; 33,000 / 1,235 ≈ 27; 33,000 / 3,600 ≈ 9.2 km/s"]
