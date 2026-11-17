# EP15 — Voyager 1 Is Now 1 Light-Day Away
# Structure NEW: "one message, hour by hour" — we send a single radio command to Voyager 1 and ride along with it. Each chapter is a
# moment on a 24-hour dial (1.3 s, 8 min, 43 min, 79 min, 5.6 h, 13 h, 16.8 h, 24 h) and tells the part of Voyager's story that happened
# at that distance. Twist at the end: 49 years bought one light-day; the nearest star is about 1,550 light-days away.
# Palette golden-record gold / Deep Space Network green / plasma violet on deep navy. New scenes: signalrun (Earth -> Voyager track on a
# square-root scale with a travelling radio pulse + light-time clock), signaldial (24-hour dial chapter card), heliobubble (termination
# shock + heliopause TO SCALE with both Voyagers' tracks and a year counter + particle-trend chart), powerdown (watt meter + 10 instrument
# lamps), whisper (22 W out, ~4×10^-19 W in, written out with every zero), pixeldot (our own re-drawing of the Pale Blue Dot + pixel zoom).
# Own calculations (Python): 1 light-day = 299,792.458 km/s × 86,400 s = 25,902,068,371 km = 173.1 AU; light time per AU = 499.0 s ->
# Jupiter 5.2 AU = 43 min, Saturn 9.5 AU = 79 min, Neptune 30.1 AU = 4.2 h, 6 billion km = 5.6 h, 94 AU = 13.0 h, 121 AU = 16.8 h.
# Speed check: (173.1 - 121) AU / (2026.88 - 2012.65) yr = 3.66 AU/yr = 17.4 km/s ≈ 62,000 km/h (NASA: about 17 km/s).
# Received power (free-space link budget, X-band 8.4 GHz, 22 W, 3.7 m dish ≈ 48 dBi, 70 m dish ≈ 74 dBi, 25.9e9 km) ≈ 4e-19 W.
# 4.24 ly × 365.25 = 1,549 light-days; 4.24 ly at 17 km/s ≈ 75,000 years; 1 light-day more every 173.1 / 3.6 ≈ 48 years.
TITLE = "Voyager 1 Is Now 1 Light-Day Away"
GOLD = [240, 190, 80]
DSN = [90, 230, 150]
PLASMA = [170, 120, 255]

SCENES = [
 # ---------- HOOK ----------
 {"say": "If you send a message to Voyager one right now, it will arrive tomorrow. Same time. Twenty four hours later. And if Voyager answers, you'll wait another full day to hear it.",
  "vis": {"type": "signaldial", "h": 24, "stamp": "24:00:00", "kicker": "ONE MESSAGE", "title": "Earth to\nVoyager 1", "sub": "one full day, one way", "fact": "the reply: one more day"}},
 {"say": "On November eighteenth, twenty twenty six, Voyager one became the first object humans ever built to reach one light-day from Earth. That's the distance light covers in a whole day, almost twenty six billion kilometers. A light-year, the unit we use for stars, is three hundred sixty five of these.",
  "vis": {"type": "signalrun", "h0": 0.0, "h1": 24.0, "head": "One light-day: 25.9 billion km", "caption": "NASA: milestone on 18 November 2026, about 10:16 UTC"}},
 {"say": "So today we'll do something simple. We'll send one message, and ride along with it, hour by hour. And at every stop, we'll see what Voyager found when it got there.",
  "vis": {"type": "title", "title": "Voyager 1 Is Now\n1 Light-Day Away", "sub": "COSMIC SCALE", "brand": True, "subcol": DSN}},

 # ---------- 0 s ----------
 {"say": "Zero seconds. The message leaves a seventy meter antenna of NASA's Deep Space Network. That dish is as wide as a soccer field is long, almost. It has to be. Because what comes back from Voyager is unbelievably faint.",
  "vis": {"type": "signaldial", "h": 0.0, "stamp": "0:00:00", "kicker": "STOP 1", "title": "Leaving\nEarth", "sub": "a 70 m dish, Deep Space Network", "fact": "Canberra, Goldstone or Madrid"}},

 # ---------- 1.3 s ----------
 {"say": "One point three seconds. Our message passes the Moon. The Apollo astronauts needed about three days to make that same trip.",
  "vis": {"type": "signalrun", "h0": 0.0, "h1": 1.282 / 3600, "log": True, "head": "1.3 seconds: the Moon", "caption": "384,400 km in 1.28 s"}},

 # ---------- 8 min ----------
 {"say": "Eight minutes and twenty seconds. We're now as far from Earth as the Sun is. Every sunrise you've ever seen was already eight minutes old.",
  "vis": {"type": "signalrun", "h0": 1.282 / 3600, "h1": 499 / 3600, "log": True, "focus": "Sun", "head": "8 min 19 s: as far as the Sun", "caption": "1 astronomical unit = 149.6 million km"}},

 # ---------- 43 min: Jupiter ----------
 {"say": "Forty three minutes. Jupiter's distance. Voyager one got here in March nineteen seventy nine, eighteen months after launch.",
  "vis": {"type": "signaldial", "h": 0.72, "stamp": "0:43", "unit": "hours : minutes", "kicker": "STOP 2", "title": "Jupiter", "sub": "Voyager 1 arrives: March 1979", "fact": "launched 5 September 1977"}},
 {"say": "Here's a strange detail. Voyager one is called one, but it launched second, sixteen days after its twin, Voyager two. It was simply put on a faster, shorter path. It overtook its sibling on the way, and reached Jupiter first.",
  "vis": {"type": "compare", "left": ["VOYAGER 2", "launched 20 Aug 1977", "slower path", "Jupiter: July 1979"], "right": ["VOYAGER 1", "launched 5 Sep 1977", "faster path", "Jupiter: March 1979"], "cols": [PLASMA, GOLD], "strike": False}},
 {"say": "And it saw something no one expected. On Jupiter's moon Io, a plume rising hundreds of kilometers into space. An erupting volcano. The first active volcanoes ever found beyond Earth.",
  "vis": {"type": "compare", "left": ["BEFORE 1979", "active volcanoes known:", "only on Earth", ""], "right": ["AFTER VOYAGER 1", "Io: plumes hundreds", "of km high", "first beyond Earth"], "cols": [PLASMA, GOLD], "strike": False}},

 # ---------- 79 min: Saturn ----------
 {"say": "One hour and nineteen minutes. Saturn. November nineteen eighty. Here, the team made a choice that decided Voyager one's whole future. They sent it close past Titan, Saturn's giant moon, wrapped in a thick orange haze.",
  "vis": {"type": "signaldial", "h": 1.32, "stamp": "1:19", "unit": "hours : minutes", "kicker": "STOP 3", "title": "Saturn", "sub": "November 1980: a close pass by Titan", "fact": "the price: no more planets"}},
 {"say": "The flyby was worth it. But Titan's gravity bent Voyager one's path up, out of the flat plane where the planets orbit. From that moment, it would never visit another planet. It was on its way out.",
  "vis": {"type": "signalrun", "h0": 1.0, "h1": 1.32, "focus": "Saturn", "head": "After Saturn: out of the planets' plane", "caption": "Voyager 2 went on to Uranus and Neptune; Voyager 1 headed out"}},

 # ---------- 4.2 h: Neptune ----------
 {"say": "Four hours and ten minutes. Neptune's orbit, the last planet. Voyager one never came here. Its twin did. In nineteen eighty nine, Voyager two flew past Neptune, and it is still the only spacecraft that has ever visited Uranus or Neptune. Every close-up picture of those two worlds, from any textbook, comes from that one visit.",
  "vis": {"type": "signalrun", "h0": 1.32, "h1": 4.17, "focus": "Neptune", "head": "4 hours 10 minutes: Neptune's orbit", "caption": "Voyager 2: Uranus 1986, Neptune 1989"}},

 # ---------- 5.6 h: Pale Blue Dot ----------
 {"say": "Five hours and thirty four minutes. Six billion kilometers. On Valentine's Day, nineteen ninety, Voyager one turned its camera around, and took a family portrait of the planets.",
  "vis": {"type": "signaldial", "h": 5.56, "stamp": "5:34", "unit": "hours : minutes", "kicker": "STOP 4", "title": "Looking\nBack", "sub": "14 February 1990, 6 billion km", "fact": "Carl Sagan asked for one last look"}},
 {"say": "In one frame, Earth showed up inside a ray of scattered sunlight. It's the picture Carl Sagan called the Pale Blue Dot. Earth fills about twelve percent of one single pixel.",
  "vis": {"type": "pixeldot", "mode": "zoom", "head": "Everyone you know: 0.12 of a pixel"}},
 {"say": "Minutes after that portrait, the cameras were switched off for good, to save power and memory. Voyager one has not taken a picture in more than thirty six years.",
  "vis": {"type": "pixeldot", "mode": "frame", "head": "The last pictures Voyager 1 ever took"}},

 # ---------- 9.6 h: the record ----------
 {"say": "Nine and a half hours. In February nineteen ninety eight, at about this distance, Voyager one passed an older probe, Pioneer ten, and became the most distant object humans have ever made. Nothing has caught up with it since. Nothing we've launched is even on course to.",
  "vis": {"type": "signalrun", "h0": 5.56, "h1": 9.62, "focus": "Pale Blue Dot", "head": "9.6 hours: the most distant human-made object", "caption": "17 February 1998: Voyager 1 overtakes Pioneer 10"}},

 # ---------- 13 h: termination shock ----------
 {"say": "Thirteen hours. Ninety four times farther than the Sun. In December twenty oh four, Voyager one crossed the termination shock. The solar wind, which blows out from the Sun at around four hundred kilometers per second, suddenly slows down here, and piles up, like a river hitting a lake.",
  "vis": {"type": "heliobubble", "mode": "shock", "head": "13 hours: the solar wind hits the brakes"}},

 # ---------- 16.8 h: heliopause ----------
 {"say": "Sixteen hours and fifty minutes. The heliopause, the edge of the Sun's bubble. Voyager one crossed it on August twenty fifth, twenty twelve, at about one hundred twenty one times the Earth to Sun distance. Particles from the Sun almost vanished. Particles from deep space jumped up. For the first time, a human-made object was in interstellar space.",
  "vis": {"type": "heliobubble", "mode": "pause", "chart": True, "head": "16.8 hours: interstellar space"}},
 {"say": "Voyager two followed in twenty eighteen, on a different side of the bubble, a little closer in. That told scientists the bubble isn't a perfect sphere. Two probes, two crossings, and they are still the only direct measurements anyone has ever taken out there.",
  "vis": {"type": "heliobubble", "mode": "out", "head": "Two Voyagers, outside the bubble"}},

 # ---------- 24 h: arrival ----------
 {"say": "Twenty four hours. Our message finally arrives. Voyager one is moving away from the Sun at about seventeen kilometers per second. More than sixty thousand kilometers per hour. Every year, it adds about three and a half times the Earth to Sun distance. At that pace, it will take about forty eight more years to reach two light-days.",
  "vis": {"type": "signaldial", "h": 24, "stamp": "24:00:00", "kicker": "STOP 5", "title": "Voyager 1", "sub": "17 km/s, about 61,000 km/h", "fact": "+3.6 Earth–Sun distances every year"}},
 {"say": "Now listen to the answer. Voyager's radio transmits with about twenty two watts, roughly a fridge light bulb. Spread over twenty six billion kilometers, our own estimate is that the dish on Earth catches less than a billionth of a billionth of a watt.",
  "vis": {"type": "whisper", "head": "The reply is a whisper", "caption": "our link-budget estimate: 22 W, 3.7 m dish, 70 m dish, 25.9 billion km, X-band"}},
 {"say": "And it arrives slowly. One hundred sixty bits per second. A single photo from your phone would take days to download. The computers that run the whole spacecraft have about sixty nine kilobytes of memory. A phone with a hundred twenty eight gigabytes holds almost two million times more.",
  "vis": {"type": "compare", "left": ["VOYAGER 1", "69.6 KB of memory", "160 bits per second", "1970s computers"], "right": ["YOUR PHONE", "128 GB of storage", "≈ 1.8 million × more", "megabits per second"], "cols": [GOLD, DSN], "strike": False}},
 {"say": "Even fixing it takes days. In late twenty twenty three, one memory chip failed, and Voyager one started sending nonsense. Engineers moved its code around, piece by piece, from twenty four light-hours away. Every test took two full days to come back. By April twenty twenty four, it was talking sense again.",
  "vis": {"type": "signaldial", "h": 24, "stamp": "48:00:00", "unit": "for one question and one answer", "kicker": "ROUND TRIP", "title": "Monday\nto Wednesday", "sub": "send a command Monday morning", "fact": "hear back Wednesday morning (NASA)"}},

 # ---------- power ----------
 {"say": "But there's a clock no one can fix. Voyager runs on heat from decaying plutonium. At launch, it had about four hundred seventy watts. It loses roughly four watts every year. Today it has less than half.",
  "vis": {"type": "powerdown", "w_end": 225, "head": "Ten instruments, one shrinking battery"}},
 {"say": "So the team switches things off, one by one, to keep the rest alive. In April twenty twenty six, another instrument went dark. Voyager one launched with ten science instruments. Today, two are still on, listening to the magnetic field and the waves in the thin gas between the stars. In twenty twenty one, scientists reported that this gas has a faint, steady hum, picked up by the plasma wave instrument.",
  "vis": {"type": "powerdown", "w_end": 225, "head": "Still on: 2 of 10", "caption": "NASA/JPL, April 2026"}},

 # ---------- the future ----------
 {"say": "So what's next? When the power finally runs out, Voyager one won't stop. It will keep coasting, silent, for longer than human history. In about three hundred years, it should reach the inner edge of the Oort cloud, a vast shell of icy bodies. Crossing it could take thirty thousand years.",
  "vis": {"type": "bignumber", "from": 0, "to": 30000, "suffix": " years", "col": PLASMA, "caption": "to cross the Oort cloud (NASA estimate)"}},
 {"say": "In about forty thousand years, it will pass within one point six light-years of a small star called Gliese four forty five. That's the closest it gets to anything. Not a visit. Just a distant pass.",
  "vis": {"type": "bignumber", "from": 0, "to": 40000, "suffix": " years", "col": GOLD, "caption": "to pass about 1.6 light-years from Gliese 445"}},
 {"say": "And it carries a message too. A gold-plated record, with greetings in fifty five languages, sounds of Earth, and ninety minutes of music. A letter with no address.",
  "vis": {"type": "bullets", "title": "The Golden Record", "items": ["greetings in 55 languages", "sounds of Earth", "90 minutes of music", "images of our world", "instructions to play it"], "col": GOLD}},

 # ---------- TWIST ----------
 {"say": "Now, the scale. Forty nine years of flight bought us one light-day. The nearest star, Proxima Centauri, is four point two four light-years away. That's about fifteen hundred light-days.",
  "vis": {"type": "bignumber", "from": 1, "to": 1549, "suffix": " light-days", "col": DSN, "caption": "to the nearest star (Voyager has done 1)"}},
 {"say": "At Voyager's speed, the trip to Proxima would take about seventy five thousand years. Voyager one is the fastest thing leaving our solar system, and it has covered less than one tenth of one percent of the way to the nearest star.",
  "vis": {"type": "bars", "title": "Light-days from Earth", "items": [["Voyager 1", 1, "#F0BE50"], ["Proxima", 1549, "#5AE696"]], "suffix": ""}},

 # ---------- RECAP + NEXT ----------
 {"say": "So that's one message. Moon in a second. Sun in eight minutes. Jupiter in forty three. The edge of the Sun's bubble in under seventeen hours. And a tiny, half-asleep spacecraft at the end of a full day. NASA even asked people to flash the letters V G R in Morse code at the night sky, as a hello it will never see.",
  "vis": {"type": "signalrun", "h0": 0.0, "h1": 24.0, "head": "One message, one day"}},
 {"say": "Next time, we go much farther than any spacecraft ever will. Why can't we see the edge of the universe? It's not because our telescopes are too weak. Subscribe to Cosmic Scale so you don't miss it. And tell me in the comments, what would you put in a message to Voyager?",
  "vis": {"type": "title", "title": "Next: why can't we see\nthe edge of the universe?", "sub": "COSMIC SCALE", "subcol": GOLD}},
]

SOURCES = ["NASA/JPL: Voyager 1 reaches one light-day (about 25.9 billion km, 16.1 billion miles) from Earth on 18 November 2026, about 10:16 UTC; a command sent Monday morning gets an answer Wednesday morning (mission manager Suzy Dodd); public event: flash V-G-R in Morse code",
           "NASA/JPL: Voyager 1 launched 5 September 1977; Jupiter flyby March 1979 (active volcanoes discovered on Io); Saturn flyby November 1980 with a close pass by Titan that sent it out of the plane of the planets",
           "NASA/JPL: Pale Blue Dot, 14 February 1990, about 6 billion km; Earth is about 0.12 of a pixel; the cameras were turned off soon after",
           "NASA/JPL: Voyager 1 crossed the termination shock in December 2004 (about 94 AU) and the heliopause on 25 August 2012 (about 121 AU); Voyager 2 crossed it on 5 November 2018",
           "NASA: the solar wind blows at about 400 km/s; Voyager 1 travels at about 17 km/s",
           "NASA/JPL: Voyager's transmitter radiates about 22 W; data rate 160 bits per second; about 69.63 KB of memory across its computers",
           "NASA/JPL: flight data system memory chip failure (November 2023) worked around by relocating code; engineering and science data restored by April and June 2024",
           "NASA/JPL: radioisotope power about 470 W at launch, about 4 W lost per year; instruments switched off to save power, Low-Energy Charged Particles instrument off on 17 April 2026; Voyager 1 has two science instruments still operating",
           "NASA: about 300 years to the inner edge of the Oort Cloud and possibly 30,000 years to fly beyond it; in about 40,000 years Voyager 1 passes within about 1.6 light-years of Gliese 445",
           "NASA/JPL: Voyager 2 launched 20 August 1977, Voyager 1 on 5 September 1977 on a faster trajectory; Voyager 1 overtook Pioneer 10 as the most distant human-made object on 17 February 1998",
           "S. K. Ocker et al., Nature Astronomy (2021): a persistent, faint plasma wave signal in interstellar space detected by Voyager 1's plasma wave instrument",
           "NASA/JPL: the Golden Record carries greetings in 55 languages, sounds of Earth, about 90 minutes of music and images",
           "Proxima Centauri is about 4.24 light-years away (NASA)",
           "Own calculations: 1 light-day = 299,792.458 km/s × 86,400 s ≈ 25.9 billion km ≈ 173.1 AU; light time 499 s per AU (Jupiter 5.2 AU ≈ 43 min, Saturn 9.5 AU ≈ 79 min, 6 billion km ≈ 5.6 h, 94 AU ≈ 13 h, 121 AU ≈ 16.8 h); speed check (173.1 - 121) AU in 14.2 years ≈ 3.66 AU/yr ≈ 17.4 km/s; received power estimate from a free-space link budget (22 W, 8.4 GHz, 3.7 m and 70 m dishes) ≈ 4 × 10^-19 W; 128 GB / 69.63 KB ≈ 1.8 million; 4.24 ly × 365.25 ≈ 1,549 light-days; 4.24 ly at 17 km/s ≈ 75,000 years; 1 / 1,549 ≈ 0.06%; 173.1 AU / 3.6 AU per year ≈ 48 years per extra light-day"]
