# Ranking #19 — Top 5 Densest Planets (Cosmic Scale)
# Mean density from the NASA NSSDC planetary fact sheet (kg/m³): Earth 5,514, Mercury 5,429, Venus 5,243, Mars 3,934, Neptune 1,638;
# Jupiter 1,326, Uranus 1,270, Saturn 687 (less than water, 1,000). 1,000 kg/m³ = 1 kg per litre, so "a litre of Earth" weighs 5.51 kg.
# Paradox hooks: #1 is the planet you're on; the giants are light; Saturn would float. Mercury's huge iron core (~85% of its radius, NASA).
# Visual NEW: "litre" (a litre of each world poured into a jar on a kitchen scale, water bottle as reference + kg/L bar).
TITLE = "Top 5 Densest Planets"
THEME = {"accent": (255, 150, 110), "accent2": (140, 220, 255), "star_col": (255, 220, 200), "tint": (36, 14, 10),
         "bar": "TOP 5 DENSEST PLANETS", "hook": "litre", "outro": "litre",
         "outro_note": "Saturn: 0.69 kg. It would float."}

HOOK = {"say": "One litre of planet number one weighs five and a half kilos. And you're standing on it.",
        "big": "5.51 KG", "top": "one litre of planet #1", "sub": "a litre of water: 1 kg"}

ITEMS = [
 {"rank": 5, "name": "Neptune", "tag": "the densest giant", "num": "1.64", "unit": "kg per litre · NASA: 1,638 kg/m³",
  "source": "NASA Neptune Fact Sheet", "vis": {"type": "litre", "col": (80, 120, 240), "kgl": 1.638, "note": "smaller than Saturn, but packed tighter"},
  "say": "Number five. Neptune. The only giant that makes the list. Smaller than Saturn, but packed much tighter. A litre of it: one point six kilos."},
 {"rank": 4, "name": "Mars", "tag": "rock, with a small core", "num": "3.93", "unit": "kg per litre · NASA: 3,934 kg/m³",
  "source": "NASA Mars Fact Sheet", "vis": {"type": "litre", "col": (205, 100, 60), "kgl": 3.934, "note": "more than double Neptune"},
  "say": "Number four. Mars. Pure rock, almost four kilos a litre. It's rock all the way down, but light rock, with a small core. Then the list jumps."},
 {"rank": 3, "name": "Venus", "tag": "Earth's heavy twin", "num": "5.24", "unit": "kg per litre · NASA: 5,243 kg/m³",
  "source": "NASA Venus Fact Sheet", "vis": {"type": "litre", "col": (230, 190, 120), "kgl": 5.243, "note": "almost Earth's size, almost Earth's density"},
  "say": "Number three. Venus. Nearly our size, and nearly as heavy. Five point two four."},
 {"rank": 2, "name": "Mercury", "tag": "a giant iron ball", "num": "5.43", "unit": "kg per litre · NASA: 5,429 kg/m³",
  "source": "NASA Mercury Fact Sheet", "vis": {"type": "litre", "col": (165, 160, 165), "kgl": 5.429, "note": "its iron core fills ~85% of its radius"},
  "say": "Number two. Mercury. The smallest planet, but its iron core fills most of it. Five point four three."},
 {"rank": 1, "name": "Earth", "tag": "the planet under your feet", "num": "5.51", "unit": "kg per litre · NASA: 5,514 kg/m³",
  "source": "NASA Earth Fact Sheet", "vis": {"type": "litre", "col": (60, 120, 220), "kgl": 5.514, "note": "squeezed by its own weight"},
  "say": "And number one. Earth. Its own weight squeezes it tight. And Saturn? Less than a litre of water. It would float."},
]

OUTRO = {"say": "The giants feel huge, but they're mostly gas. What should we put on the scale next? Subscribe to Cosmic Scale."}

SOURCES = ["NASA planetary fact sheets (NSSDC): mean density Earth 5,514, Mercury 5,429, Venus 5,243, Mars 3,934, Neptune 1,638, Jupiter 1,326, Uranus 1,270, Saturn 687 kg/m³",
           "1,000 kg/m³ = 1 kg per litre (density of water)",
           "NASA Science, Mercury: its metallic core takes up about 85% of the planet's radius"]
