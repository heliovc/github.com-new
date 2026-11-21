# Scale Short #14 — Andromeda Is 6 Times Wider Than the Full Moon (Cosmic Scale)
# Format: "small vs giant" in the sky — NASA Hubble Messier 31 page / ESA: in angular size Andromeda is about six times the diameter of
# the full Moon (~3° vs ~0.5°); visible to the unaided eye only as its bright core. Distance about 2.5 million light-years (NASA).
# Our species (Homo sapiens) is about 300,000 years old (Smithsonian). Visual NEW: "andromeda". Ties to EP03 (How Big Is the Universe).
# Loop: ends on a question; the hook line restarts the idea.
TITLE = "There's a Galaxy in Your Sky 6 Times Wider Than the Moon. You've Never Seen It"
THEME = {"accent": (170, 190, 255), "accent2": (255, 235, 170), "tint": (12, 10, 40)}
BIG = {"num": "6× THE MOON", "top": "A GALAXY IN YOUR SKY"}

BEATS = [
 {"say": "This galaxy is six times wider than the full Moon.", "vis": {"type": "andromeda", "mode": "hook"}},
 {"say": "It's Andromeda, our nearest big neighbor. End to end, it covers about three degrees of sky. The Moon covers half a degree.",
  "vis": {"type": "andromeda", "mode": "row", "head": {"num": "3° vs 0.5°", "top": "ANDROMEDA vs FULL MOON"}}},
 {"say": "So why have you never noticed it? Its light is spread so thin that, even from a dark field, your eyes only catch the core. A faint smudge.",
  "vis": {"type": "andromeda", "mode": "eye", "head": {"num": "INVISIBLE", "top": "TO THE NAKED EYE, MOSTLY"}}},
 {"say": "And that faint light is old. It left Andromeda two and a half million years ago, before our species even existed.",
  "vis": {"type": "andromeda", "mode": "light", "head": {"num": "2.5 MILLION", "top": "LIGHT-YEARS AWAY"}}},
 {"say": "Leave a camera open for a few minutes, and the whole thing appears, right where it's always been. Which hidden giant should we find next?",
  "vis": {"type": "andromeda", "mode": "photo", "head": {"num": "6× THE MOON", "top": "ALWAYS THERE"}}},
]

SOURCES = ["NASA Hubble Messier Catalog, Messier 31: Andromeda is about six times the apparent diameter of the full Moon and can be seen with the unaided eye from dark skies; about 2.5 million light-years away",
           "ESA (Flyeye image of Andromeda, 2025): in angular size it is about six times the diameter of the full Moon",
           "The full Moon spans about 0.5° of sky; Andromeda's visible disc about 3° (long exposures)",
           "Smithsonian Human Origins Program: Homo sapiens appeared about 300,000 years ago"]
