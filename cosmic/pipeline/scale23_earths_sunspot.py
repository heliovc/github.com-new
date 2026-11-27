# Scale Short #23 — 10 Earths Fit Across One Spot on the Sun (Cosmic Scale)
# Format: "X inside Y". NASA (Solar Dynamics Observatory / NASA SVS "The Big Sunspot of 2014"): active region AR 12192, October 2014,
# about 80,000 miles (about 129,000 km) across, roughly the size of Jupiter, wide enough for about 10 Earths side by side; the largest
# sunspot group since 1990; it produced 6 X-class flares. NASA: sunspots look dark because they are cooler than the surface around them.
# NASA fact sheets: Earth 12,742 km, Jupiter 142,984 km, Sun 1,391,400 km.
# Own calc: 129,000 / 12,742 = 10.1 Earths; 129,000 / 142,984 = 0.90 Jupiter; 129,000 / 1,391,400 = 9% of the Sun's width.
# Visual NEW: "sunspot" (code-drawn granulation + umbra/penumbra, Earths to scale). Loop: the tail returns to the hook frame.
TITLE = "10 Earths Fit Across One Spot on the Sun"
THEME = {"accent": (255, 190, 80), "accent2": (140, 200, 255), "tint": (40, 16, 4)}
BIG = {"num": "10 EARTHS", "top": "ACROSS ONE SUNSPOT"}

BEATS = [
 {"say": "Ten Earths fit across one spot on the Sun.", "vis": {"type": "sunspot", "mode": "hook"}},
 {"say": "October twenty fourteen. NASA's Solar Dynamics Observatory watched this sunspot grow to about a hundred and thirty thousand kilometers across.",
  "vis": {"type": "sunspot", "mode": "grow", "head": {"num": "129,000 KM", "top": "ONE SUNSPOT, OCTOBER 2014"}}},
 {"say": "Line up Earths across it, to scale. Ten of them.",
  "vis": {"type": "sunspot", "mode": "row", "head": {"num": "10 EARTHS", "top": "SIDE BY SIDE"}}},
 {"say": "That's almost as wide as Jupiter, the biggest planet.",
  "vis": {"type": "sunspot", "mode": "jupiter", "head": {"num": "90% OF JUPITER", "top": "SAME SCALE"}}},
 {"say": "And on the whole Sun, it's still a freckle. It only looks black because the surface around it is even hotter and brighter.",
  "vis": {"type": "sunspot", "mode": "sun", "head": {"num": "9% OF THE SUN", "top": "STILL JUST A FRECKLE"}}},
 {"say": "It fired six of the strongest kind of flare. What should we put on the Sun next? Ten Earths, one spot.",
  "vis": {"type": "sunspot", "mode": "tail"}},
]

SOURCES = ["NASA Scientific Visualization Studio / Solar Dynamics Observatory, 'The Big Sunspot of 2014': active region AR 12192, October 2014, about 80,000 miles (129,000 km) across, about the size of Jupiter, wide enough for 10 Earths; the largest since 1990",
           "NASA (Oct 2014): AR 12192 produced six X-class flares, the strongest class of solar flare",
           "NASA: sunspots appear dark because they are cooler than the surrounding surface of the Sun",
           "NASA fact sheets: Earth diameter 12,742 km; Jupiter 142,984 km; Sun 1,391,400 km",
           "Own calculations: 129,000 / 12,742 = 10.1 Earths; 129,000 / 142,984 = 0.90 of Jupiter's width; 129,000 / 1,391,400 = 9% of the Sun's width"]
