# Ranking #18 — Top 5 Strongest Gravity in the Solar System (Cosmic Scale)
# Surface gravity from the NASA fact sheets (m/s²; gas giants at the 1-bar level): Earth 9.80, Saturn 10.44, Neptune 11.15,
# Jupiter 24.79, Sun 274.0 (photosphere). Venus and Uranus (8.87) just miss. Own calc: a 70 kg person reads 70 × g / 9.80 on a scale:
# Saturn 74.6, Neptune 79.6, Jupiter 177, Sun 1,957 kg; a 50 cm jump on Earth -> 50 × 9.80 / g (Jupiter 20 cm, Sun 1.8 cm).
# Paradox hooks: Earth makes the list; Saturn (95 Earths) barely beats Earth; Neptune beats Saturn with 1/5 of its mass.
# Visual NEW: "gravity" (person on a bathroom scale on each world's curved surface + log ruler × Earth's gravity).
TITLE = "Top 5 Strongest Gravity in the Solar System"
THEME = {"accent": (140, 255, 170), "accent2": (255, 200, 120), "star_col": (220, 230, 255), "tint": (10, 30, 24),
         "bar": "TOP 5 STRONGEST GRAVITY", "hook": "gravity", "outro": "gravity",
         "outro_note": "Earth is number five"}

HOOK = {"say": "On number one, you'd weigh two tonnes. The strongest gravity in the solar system.",
        "big": "2 TONNES", "top": "what you'd weigh on #1", "sub": "a 70 kg person, five worlds"}

ITEMS = [
 {"rank": 5, "name": "Earth", "tag": "yes, home makes the list", "num": "9.80", "unit": "m/s² · the baseline: 1×",
  "source": "NASA Earth Fact Sheet", "vis": {"type": "gravity", "kind": "earth", "col": (70, 130, 230), "g": 9.80, "note": "Uranus is 14× heavier, yet pulls less"},
  "say": "Number five. Earth. Uranus is fourteen times heavier, but it's so puffy that its pull at the cloud tops is weaker than ours."},
 {"rank": 4, "name": "Saturn", "tag": "95 Earths of mass, barely more pull", "num": "10.4", "unit": "m/s² · 1.07× Earth",
  "source": "NASA Saturn Fact Sheet", "vis": {"type": "gravity", "kind": "ringed", "col": (225, 200, 150), "g": 10.44, "note": "huge, so its clouds sit far from the centre"},
  "say": "Number four. Saturn. Ninety five times our mass, yet you'd gain only five kilos. Its clouds sit so far from its centre."},
 {"rank": 3, "name": "Neptune", "tag": "beats Saturn with a fifth of the mass", "num": "11.2", "unit": "m/s² · 1.14× Earth",
  "source": "NASA Neptune Fact Sheet", "vis": {"type": "gravity", "kind": "ice", "col": (80, 120, 240), "g": 11.15, "note": "smaller and denser than Saturn"},
  "say": "Number three. Neptune. Only a fifth of Saturn's mass, but smaller and denser, so it pulls harder. Eighty kilos."},
 {"rank": 2, "name": "Jupiter", "tag": "the planet that would crush you", "num": "24.8", "unit": "m/s² · 2.5× Earth",
  "source": "NASA Jupiter Fact Sheet", "vis": {"type": "gravity", "kind": "gas", "col": (215, 170, 125), "g": 24.79, "note": "a 50 cm jump here: 20 cm"},
  "say": "Number two. Jupiter. Two and a half times Earth. You'd weigh one hundred seventy seven kilos, and your best jump would barely clear a shoebox."},
 {"rank": 1, "name": "The Sun", "tag": "28 times Earth's pull", "num": "274", "unit": "m/s² · 28× Earth",
  "source": "NASA Sun Fact Sheet", "vis": {"type": "gravity", "kind": "sun", "col": (255, 190, 80), "g": 274.0, "note": "a 50 cm jump here: under 2 cm"},
  "say": "And number one. The Sun. Twenty eight times Earth's gravity. Nearly two tonnes on the scale. Your heart couldn't lift your own blood."},
]

OUTRO = {"say": "Where should we weigh you next? Subscribe to Cosmic Scale."}

SOURCES = ["NASA planetary fact sheets (NSSDC): surface gravity Earth 9.80, Saturn 10.44, Neptune 11.15, Jupiter 24.79, Venus 8.87, Uranus 8.87 m/s² (gas giants measured at the 1-bar pressure level)",
           "NASA Sun Fact Sheet (NSSDC): surface gravity 274.0 m/s²",
           "NASA fact sheets: masses Uranus 14.5, Neptune 17.1, Saturn 95.2 Earths",
           "Own calculations: scale reading = 70 kg × g ÷ 9.80 (Saturn 74.6, Neptune 79.6, Jupiter 177, Sun 1,957 kg); a 50 cm jump on Earth reaches 50 × 9.80 ÷ g"]
