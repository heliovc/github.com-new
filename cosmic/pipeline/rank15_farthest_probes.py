# Ranking #15 — Top 5 Farthest Human-Made Objects (Cosmic Scale)
# Ranked by distance from the Sun in November 2026. Distances are rounded estimates: last published positions (Heavens-Above / JPL-based
# tables, 2024–2026) advanced at each probe's speed (Voyager 1 ≈ 3.6 AU/yr, Voyager 2 ≈ 3.25, Pioneer 10 ≈ 2.5, Pioneer 11 ≈ 2.4, New
# Horizons ≈ 2.9). Voyager 1: NASA, 1 light-day ≈ 173 AU on 18 Nov 2026. Voyager 2 passed Pioneer 10 (from the Sun) in July 2023 at ≈ 133.9 AU.
# Visual NEW: "probes" (code-drawn probe + light-time + STILL TALKING / SILENT badge + square-root track Sun -> 180 AU).
# Hook: big "24 HOURS" + light pulse running along the track toward a "?"; spoken "Light takes a full day to reach number one."
# Own calc: AU -> billion km × 0.1496; light time h = AU × 499 s / 3600 (66 -> 9.1 h, 120 -> 16.6 h, 142 -> 19.7 h, 145 -> 20.1 h, 173 -> 24.0 h).
TITLE = "Top 5 Farthest Human-Made Objects"
THEME = {"accent": (255, 200, 90), "accent2": (110, 235, 170), "star_col": (255, 220, 160), "tint": (10, 40, 34),
         "bar": "TOP 5 FARTHEST THINGS WE EVER BUILT", "hook": "probes", "outro": "probes",
         "outro_note": "the youngest of them launched 20 years ago"}

HOOK = {"say": "Light takes a full day to reach number one. These are the five farthest things humans ever built.",
        "big": "24 HOURS", "top": "for light to reach #1", "sub": "and it's still moving away"}

ITEMS = [
 {"rank": 5, "name": "New Horizons", "short": "New Horizons", "tag": "launched 2006 · still working", "num": "≈ 9.9 billion", "unit": "km from the Sun (≈ 66 AU)",
  "source": "NASA / JHU APL; our estimate, Nov 2026", "vis": {"type": "probes", "kind": "horizons", "au": 66, "col": (240, 200, 110), "alive": True, "note": "flew past Pluto in 2015"},
  "say": "Number five. New Horizons. About ten billion kilometers. Nine years after launch, it gave us the first close look at Pluto."},
 {"rank": 4, "name": "Pioneer 11", "short": "Pioneer 11", "tag": "launched 1973 · first to Saturn", "num": "≈ 18 billion", "unit": "km from the Sun (≈ 120 AU)",
  "source": "NASA; our estimate, Nov 2026", "vis": {"type": "probes", "kind": "pioneer", "au": 120, "col": (200, 170, 255), "alive": False, "silent": "SILENT SINCE 1995", "note": "first spacecraft to visit Saturn, 1979"},
  "say": "Number four. Pioneer eleven. About eighteen billion. The first visitor to Saturn. We last heard from it in nineteen ninety five."},
 {"rank": 3, "name": "Pioneer 10", "short": "Pioneer 10", "tag": "launched 1972 · first to Jupiter", "num": "≈ 21.3 billion", "unit": "km from the Sun (≈ 142 AU)",
  "source": "NASA; our estimate, Nov 2026", "vis": {"type": "probes", "kind": "pioneer", "au": 142, "col": (150, 200, 255), "alive": False, "silent": "SILENT SINCE 2003", "note": "carries a plaque with a map to Earth"},
  "say": "Number three. Pioneer ten. Twenty one billion. It carries a metal plaque with a map back to Earth. Its last whisper reached us in two thousand three."},
 {"rank": 2, "name": "Voyager 2", "short": "Voyager 2", "tag": "launched 1977 · still working", "num": "≈ 21.7 billion", "unit": "km from the Sun (≈ 145 AU)",
  "source": "NASA/JPL; our estimate, Nov 2026", "vis": {"type": "probes", "kind": "voyager", "au": 145, "col": (255, 150, 120), "alive": True, "note": "passed Pioneer 10 in 2023"},
  "say": "Number two. Voyager two. Almost twenty two billion. It only overtook Pioneer ten in twenty twenty three."},
 {"rank": 1, "name": "Voyager 1", "short": "Voyager 1", "tag": "launched 1977 · still working", "num": "25.9 billion", "unit": "km from Earth: one light-day",
  "source": "NASA/JPL, 18 Nov 2026", "vis": {"type": "probes", "kind": "voyager", "au": 173, "col": (255, 205, 90), "alive": True, "note": "a radio command takes a full day to arrive"},
  "say": "And number one. Voyager one. Twenty six billion kilometers. This week it became the first thing we built to sit one full light-day away."},
]

OUTRO = {"say": "Where should we send one next? Subscribe to Cosmic Scale."}

SOURCES = ["NASA/JPL: Voyager 1 reaches one light-day (about 25.9 billion km) from Earth on 18 November 2026; Voyager 1 and 2 launched in 1977 and still return data",
           "NASA: Pioneer 10 launched 1972, first spacecraft to fly past Jupiter, carries the Pioneer plaque, last signal January 2003; Pioneer 11 launched 1973, first spacecraft to fly past Saturn (1979), last contact 1995",
           "NASA / Johns Hopkins APL: New Horizons launched January 2006, flew past Pluto in July 2015 and Arrokoth in 2019",
           "Voyager 2 passed Pioneer 10 in distance from the Sun in July 2023 at about 133.9 AU (JPL-based tables)",
           "Own estimates for November 2026: last published distances from the Sun (Heavens-Above / JPL-based tables) advanced at each probe's speed — Voyager 2 ≈ 145 AU, Pioneer 10 ≈ 142 AU, Pioneer 11 ≈ 120 AU, New Horizons ≈ 66 AU; 1 AU = 149.6 million km; light time = AU × 499 s"]
