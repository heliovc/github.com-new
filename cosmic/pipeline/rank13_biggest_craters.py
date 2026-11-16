# Ranking #13 — Top 5 Biggest Impact Craters on Earth (Cosmic Scale)
# Ranked by diameter as listed in the Earth Impact Database (University of New Brunswick); #5 and #4 share 100 km (said out loud).
# Visual NEW: "crater" (top-down crater TO SCALE at 4.6 px/km on rocky ground: a streak hits, the crater opens with a flash, rim + peak ring;
# older = more eroded rim; a marathon bar, 42 km, as the ruler). Hook: big number "160 KM" + eroded crater with "?"; spoken hook
# "A hole one hundred sixty kilometers wide." (≤ 2 s). Outro: the five rims nested to scale + "Which crater should we put next?".
# Theme NEW: impact orange / desert sand on a rust tint. Own calc: 160 km / 42.195 km ≈ 3.8 marathons.
TITLE = "Top 5 Biggest Impact Craters on Earth"
THEME = {"accent": (255, 140, 60), "accent2": (240, 215, 160), "star_col": (255, 210, 170), "tint": (60, 26, 12),
         "bar": "TOP 5 BIGGEST IMPACT CRATERS ON EARTH", "hook": "crater", "outro": "crater", "outro_note": "#1 is almost 4 marathons wide"}

HOOK = {"say": "A hole one hundred sixty kilometers wide. These are the five biggest impact craters on Earth.",
        "big": "160 KM", "top": "the biggest crater on Earth", "sub": "#2 ended the dinosaurs"}

ITEMS = [
 {"rank": 5, "name": "Manicouagan", "short": "Manicouagan", "tag": "Quebec, Canada · 214 million years", "num": "100 km", "unit": "wide",
  "source": "Earth Impact Database", "vis": {"type": "crater", "km": 100, "erosion": 0.5, "ring": (120, 200, 255), "note": "today a ring-shaped lake, visible from space"},
  "say": "Number five. Manicouagan, in Canada. About a hundred kilometers wide. Today it's a ring-shaped lake you can see from space."},
 {"rank": 4, "name": "Popigai", "short": "Popigai", "tag": "Siberia, Russia · 36 million years", "num": "100 km", "unit": "wide",
  "source": "Earth Impact Database", "vis": {"type": "crater", "km": 100, "erosion": 0.25, "ring": (190, 160, 255), "note": "the impact turned graphite into diamonds"},
  "say": "Number four. Popigai, in Siberia. Also about a hundred kilometers, but much younger. The blast was so strong it turned graphite in the rock into diamonds."},
 {"rank": 3, "name": "Sudbury", "short": "Sudbury", "tag": "Ontario, Canada · 1.85 billion years", "num": "130 km", "unit": "wide",
  "source": "Earth Impact Database", "vis": {"type": "crater", "km": 130, "erosion": 0.8, "ring": (120, 230, 170), "note": "now one of the world's great nickel mines"},
  "say": "Number three. Sudbury, in Canada. A hundred thirty kilometers. Almost two billion years old, and today one of the biggest nickel mining regions on Earth."},
 {"rank": 2, "name": "Chicxulub", "short": "Chicxulub", "tag": "Yucatán, Mexico · 66 million years", "num": "150 km", "unit": "wide",
  "source": "Earth Impact Database; NASA", "vis": {"type": "crater", "km": 150, "erosion": 0.1, "ring": (255, 110, 110), "note": "a 10 km rock, the end of the dinosaurs"},
  "say": "Number two. Chicxulub, in Mexico. A hundred fifty kilometers. A rock about ten kilometers wide made it, and wiped out the dinosaurs."},
 {"rank": 1, "name": "Vredefort", "short": "Vredefort", "tag": "South Africa · about 2 billion years", "num": "160 km", "unit": "wide",
  "source": "Earth Impact Database; UNESCO", "vis": {"type": "crater", "km": 160, "erosion": 0.9, "ring": (255, 200, 80), "note": "the oldest and biggest crater we know"},
  "say": "And number one. Vredefort, in South Africa. About a hundred sixty kilometers, and two billion years old. It's the biggest and oldest impact structure we know."},
]

OUTRO = {"say": "Almost four marathons, end to end. Which crater should we put next? Subscribe to Cosmic Scale."}

SOURCES = ["Earth Impact Database (Planetary and Space Science Centre, University of New Brunswick): Vredefort about 160 km, about 2.02 billion years; Chicxulub about 150 km, about 66 million years; Sudbury about 130 km, about 1.85 billion years; Popigai about 100 km, about 35.7 million years; Manicouagan about 100 km, about 214 million years (some sources give other sizes, measured as the eroded or the original crater)",
           "UNESCO World Heritage: Vredefort Dome, the oldest and largest impact structure found on Earth",
           "NASA: the Chicxulub impactor was about 10 km wide and struck about 66 million years ago",
           "Popigai: impact diamonds formed from graphite by the shock of the impact (Russian Academy of Sciences)",
           "Own calculation: 160 km / 42.195 km (marathon) ≈ 3.8"]
