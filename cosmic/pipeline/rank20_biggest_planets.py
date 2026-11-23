# Ranking #20 — Top 5 Biggest Planets (Cosmic Scale)
# Equatorial diameters from the NASA NSSDC planetary fact sheet (km): Jupiter 142,984, Saturn 120,536, Uranus 51,118, Neptune 49,528,
# Earth 12,756, Venus 12,104 (Earth wins #5 by 652 km). Own calc, in Earth widths (÷ 12,756): Jupiter 11.21, Saturn 9.45, Uranus 4.01,
# Neptune 3.88. Neptune is narrower than Uranus but 18% heavier (NASA: 102.4 vs 86.8 × 10^24 kg). Saturn's rings span about 273,000 km
# (NASA), wider than Jupiter. Visual NEW: "beads" (Earths strung across each planet's equator, one common scale). Ties to EP18 (Jupiter).
TITLE = "Top 5 Biggest Planets"
THEME = {"accent": (255, 190, 110), "accent2": (130, 220, 255), "star_col": (255, 225, 190), "tint": (30, 18, 10),
         "bar": "TOP 5 BIGGEST PLANETS", "hook": "beads", "outro": "beads",
         "outro_note": "Earth wins #5 by just 652 km"}

HOOK = {"say": "Eleven Earths, side by side. That's how wide planet number one is.",
        "big": "11 EARTHS", "top": "across planet #1", "sub": "same scale, all five"}

ITEMS = [
 {"rank": 5, "name": "Earth", "tag": "beats Venus by a hair", "num": "12,756 km", "unit": "wide at the equator",
  "source": "NASA Earth & Venus Fact Sheets", "vis": {"type": "beads", "kind": "earth", "col": (70, 130, 230), "km": 12756, "earths": 1.0, "note": "Venus: 12,104 km, just 652 km narrower"},
  "say": "Number five. Earth. Venus is almost a twin, but we win, by just six hundred and fifty two kilometers."},
 {"rank": 4, "name": "Neptune", "tag": "smaller, but heavier", "num": "49,528 km", "unit": "3.88 Earths wide",
  "source": "NASA Neptune Fact Sheet", "vis": {"type": "beads", "kind": "ice", "col": (80, 120, 240), "km": 49528, "earths": 3.88, "note": "narrower than Uranus, yet 18% heavier"},
  "say": "Number four. Neptune. Almost four Earths across. And it's narrower than Uranus, yet heavier."},
 {"rank": 3, "name": "Uranus", "tag": "the sideways giant", "num": "51,118 km", "unit": "4.01 Earths wide",
  "source": "NASA Uranus Fact Sheet", "vis": {"type": "beads", "kind": "ice2", "col": (150, 215, 225), "km": 51118, "earths": 4.01, "note": "it spins tipped on its side"},
  "say": "Number three. Uranus. Just over four Earths. Then the list jumps."},
 {"rank": 2, "name": "Saturn", "tag": "rings wider than Jupiter", "num": "120,536 km", "unit": "9.45 Earths wide",
  "source": "NASA Saturn Fact Sheet", "vis": {"type": "beads", "kind": "ringed", "col": (225, 200, 150), "km": 120536, "earths": 9.45, "note": "with its rings: about 273,000 km"},
  "say": "Number two. Saturn. Nine and a half Earths. Count the rings, and it's wider than anything else on this list."},
 {"rank": 1, "name": "Jupiter", "tag": "the king of the planets", "num": "142,984 km", "unit": "11.21 Earths wide",
  "source": "NASA Jupiter Fact Sheet", "vis": {"type": "beads", "kind": "jupiter", "col": (215, 170, 125), "km": 142984, "earths": 11.21, "note": "and you could fall into it for 70,000 km"},
  "say": "And number one. Jupiter. Eleven Earths wide. And there's no ground. You could fall in for seventy thousand kilometers."},
]

OUTRO = {"say": "Eleven Earths, side by side. Which world should we measure next? Subscribe to Cosmic Scale."}

SOURCES = ["NASA planetary fact sheets (NSSDC): equatorial diameter Jupiter 142,984 km, Saturn 120,536 km, Uranus 51,118 km, Neptune 49,528 km, Earth 12,756 km, Venus 12,104 km",
           "NASA: Neptune mass 102.4 × 10^24 kg vs Uranus 86.8 × 10^24 kg; Saturn's main rings span about 273,000 km",
           "Own calculations: diameters divided by Earth's 12,756 km (Jupiter 11.21, Saturn 9.45, Uranus 4.01, Neptune 3.88); Earth minus Venus = 652 km"]
