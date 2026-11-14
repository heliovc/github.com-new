# Ranking #11 — Top 5 Fastest-Spinning Objects Ever Measured (Cosmic Scale)
# Ranked by rotation period (spins per second). Visual NEW: "spin" (each object spins at a visible rate with a computed "REAL SPEED" /
# "sped up N×" / "slowed down N×" stamp + log meter of spins per second from 1 per day to 1,000 per second, Earth as reference).
# Hook: big number in frame 0 ("716 / SECOND") + a pulsar sweeping its beams; spoken hook "Seven hundred sixteen spins a second." (≤ 2 s).
# Outro: all five on the meter + "Which object should we put next?". Theme NEW: electric violet / lime on a deep-teal tint.
# Own calc: Jupiter 9 h 56 min = 35,760 s -> 2.8e-5 spins/s; 716 Hz pulsar equator ≈ 24% of light speed (Hessels et al.); 2024 BX1 2.588 s.
# Note: a "black hole spinning 1,000 times per second" claim was checked and dropped (no reliable source).
TITLE = "Top 5 Fastest-Spinning Objects Ever Measured"
THEME = {"accent": (190, 140, 255), "accent2": (180, 255, 90), "star_col": (220, 210, 255), "tint": (10, 44, 56),
         "bar": "TOP 5 FASTEST-SPINNING OBJECTS", "hook": "spin", "outro": "spin", "outro_note": "Earth: 1 spin per day"}

HOOK = {"say": "Seven hundred sixteen spins a second. These are the five fastest-spinning objects ever measured.",
        "big": "716 / SECOND", "top": "a whole star, spinning", "sub": "#1 is a star the size of a city"}

ITEMS = [
 {"rank": 5, "name": "Jupiter", "short": "Jupiter", "tag": "the fastest-spinning planet", "num": "9 h 56 min", "unit": "for one full spin",
  "source": "NASA", "vis": {"type": "spin", "kind": "gas", "rps": 1 / 35760, "vis_rps": 0.25, "r": 250, "col": (215, 175, 130), "note": "a day shorter than 10 hours, on a planet 11 Earths wide"},
  "say": "Number five. Jupiter. Eleven times wider than Earth, and its day lasts less than ten hours. The fastest-spinning planet we know."},
 {"rank": 4, "name": "LAMOST J0240+1952", "short": "White dwarf", "tag": "a white dwarf star", "num": "25 s", "unit": "for one full spin",
  "source": "Pelisoli et al. 2021, Sheffield / Warwick", "vis": {"type": "spin", "kind": "dwarf", "rps": 1 / 24.93, "vis_rps": 0.4, "r": 190, "note": "a dead star about the size of Earth"},
  "say": "Number four. A white dwarf, the leftover core of a star, about the size of Earth. It spins once every twenty five seconds."},
 {"rank": 3, "name": "Asteroid 2024 BX1", "short": "2024 BX1", "tag": "burned up over Berlin, January 2024", "num": "2.6 s", "unit": "for one full spin",
  "source": "Devogele et al. 2024", "vis": {"type": "spin", "kind": "rock", "rps": 1 / 2.588, "vis_rps": 1 / 2.588, "r": 170, "note": "about 1 meter wide, about 33,000 spins a day"},
  "say": "Number three. A tiny asteroid that burned up over Berlin in twenty twenty four. It spun once every two point six seconds, the fastest asteroid ever measured."},
 {"rank": 2, "name": "PSR B1937+21", "short": "B1937+21", "tag": "a pulsar, record holder for 24 years", "num": "642 / s", "unit": "spins per second",
  "source": "Backer et al. 1982, Nature", "vis": {"type": "spin", "kind": "pulsar", "rps": 642, "vis_rps": 1.4, "r": 55, "col": (140, 200, 255), "note": "a neutron star, about 20 km across"},
  "say": "Number two. A pulsar, a dead star about twenty kilometers wide, spinning six hundred forty two times every second."},
 {"rank": 1, "name": "PSR J1748-2446ad", "short": "J1748-2446ad", "tag": "the fastest pulsar known", "num": "716 / s", "unit": "spins per second",
  "source": "Hessels et al. 2006, Science", "vis": {"type": "spin", "kind": "pulsar", "rps": 716, "vis_rps": 1.8, "r": 55, "col": (190, 140, 255), "note": "its equator moves at about 24% of light speed"},
  "say": "And number one. Another pulsar, spinning seven hundred sixteen times a second. Its surface moves at about a quarter of the speed of light."},
]

OUTRO = {"say": "Earth needs a whole day for one spin. Which object should we put next? Subscribe to Cosmic Scale."}

SOURCES = ["NASA: Jupiter rotates once about every 9 hours 56 minutes, the shortest day of any planet; about 11 times Earth's width",
           "Pelisoli et al. (2021), Nature Astronomy (Universities of Sheffield and Warwick): white dwarf LAMOST J0240+1952 spins every 24.93 seconds, the fastest confirmed white dwarf",
           "Devogele et al. (2024), arXiv preprint: asteroid 2024 BX1, about 1 m wide, which broke up over Berlin on 21 January 2024, rotated every 2.588 seconds, the fastest asteroid spin measured",
           "Backer et al. (1982), Nature: pulsar PSR B1937+21 spins 642 times per second (record until 2006)",
           "Hessels et al. (2006), Science, 'A Radio Pulsar Spinning at 716 Hz': PSR J1748-2446ad in the globular cluster Terzan 5; its equator moves at roughly 24% of the speed of light",
           "Own calculations: 9 h 56 min = 35,760 s; 86,400 / 2.588 ≈ 33,000 spins a day; animation speeds compared with real spin rates"]
