# Ranking #17 — Top 5 Heaviest Objects in the Solar System (Cosmic Scale)
# Masses from the NASA planetary fact sheets, in Earth masses: Uranus 14.54, Neptune 17.15, Saturn 95.16, Jupiter 317.8, Sun 332,946.
# Earth (1.0) is #6 — the hook. Visual NEW: "weigh" (balance beam: object vs a stack of Earths, counter, log ruler 1 -> 1,000,000 Earths).
# Own calc: Jupiter / (all other planets) = 317.8 / (0.055+0.815+1+0.107+95.16+14.54+17.15) = 2.47; Sun share = 99.86%.
TITLE = "Top 5 Heaviest Objects in the Solar System"
THEME = {"accent": (120, 225, 255), "accent2": (255, 205, 120), "star_col": (220, 230, 255), "tint": (12, 22, 40),
         "bar": "TOP 5 HEAVIEST OBJECTS", "hook": "weigh", "outro": "weigh",
         "outro_note": "Earth is number six"}

HOOK = {"say": "Earth doesn't even make the top five. The heaviest things in the solar system.",
        "big": "333,000×", "top": "Earth's mass: the heaviest one", "sub": "weighed in Earths"}

ITEMS = [
 {"rank": 5, "name": "Uranus", "tag": "wider than Neptune, but lighter", "num": "14.5", "unit": "Earth masses",
  "source": "NASA Uranus Fact Sheet", "vis": {"type": "weigh", "kind": "ice", "col": (150, 220, 230), "r": 70, "earths": 14.54, "note": "tipped on its side, 98°"},
  "say": "Number five. Uranus. Fourteen and a half Earths. And it spins tipped almost completely on its side, like a rolling ball."},
 {"rank": 4, "name": "Neptune", "tag": "smaller than Uranus, but heavier", "num": "17.1", "unit": "Earth masses",
  "source": "NASA Neptune Fact Sheet", "vis": {"type": "weigh", "kind": "ice", "col": (80, 120, 240), "r": 68, "earths": 17.15, "note": "denser: more rock and ice inside"},
  "say": "Number four. Neptune. Smaller than Uranus, but heavier, because it's packed with more rock and ice. Seventeen Earths."},
 {"rank": 3, "name": "Saturn", "tag": "light enough to float in water", "num": "95", "unit": "Earth masses",
  "source": "NASA Saturn Fact Sheet", "vis": {"type": "weigh", "kind": "ringed", "col": (225, 200, 150), "r": 78, "earths": 95.16, "note": "average density 0.69 g/cm³ — less than water"},
  "say": "Number three. Saturn. Ninety five Earths, yet on average it's less dense than water. In a big enough bathtub, it would float."},
 {"rank": 2, "name": "Jupiter", "tag": "2.5× all other planets combined", "num": "318", "unit": "Earth masses",
  "source": "NASA Jupiter Fact Sheet", "vis": {"type": "weigh", "kind": "gas", "col": (215, 170, 125), "r": 95, "earths": 317.8, "note": "every other planet, together: 128 Earths"},
  "say": "Number two. Jupiter. Three hundred eighteen Earths. Two and a half times every other planet combined. Without the Sun, Jupiter would be the king."},
 {"rank": 1, "name": "The Sun", "tag": "99.86% of everything", "num": "333,000", "unit": "Earth masses",
  "source": "NASA Sun Fact Sheet", "vis": {"type": "weigh", "kind": "sun", "col": (255, 200, 90), "r": 100, "earths": 332946, "note": "everything else = 0.14%"},
  "say": "And number one. The Sun. Three hundred thirty three thousand Earths. Ninety nine point eight six percent of everything here."},
]

OUTRO = {"say": "What should we weigh next? Subscribe to Cosmic Scale."}

SOURCES = ["NASA planetary fact sheets (NSSDC): masses Uranus 86.8, Neptune 102.4, Saturn 568.3, Jupiter 1,898 × 10^24 kg; Earth 5.97 × 10^24 kg; Sun 1,988,400 × 10^24 kg (332,946 Earths)",
           "NASA: the Sun holds about 99.86% of the solar system's mass; Saturn's mean density 0.687 g/cm³ (less than water); Uranus's axis is tilted about 98°",
           "NASA: Neptune is smaller in diameter than Uranus (49,528 vs 51,118 km) but more massive",
           "Own calculations: Jupiter ÷ all other planets combined = 317.8 ÷ 128.8 Earth masses ≈ 2.5"]
