# Shortcut Lab - EP04: Write better AI prompts, 5 techniques that actually work
# Techniques taken from the official prompting guides (OpenAI "Best practices for prompt engineering", Anthropic "Prompt engineering
# overview", Google "Prompting strategies" for Gemini): be specific / give context, specify the format, show examples (few-shot),
# split complex tasks (prompt chaining) + step-by-step reasoning, say what to do instead of what not to do, use delimiters.
# AUTHENTICITY: there is no code in this episode. Every AI reply on screen is an ILLUSTRATION (labeled on screen and in the voice);
# real replies vary every time. No brand logos or app UIs are drawn - a generic chat window only.
TITLE = "Write Better AI Prompts: 5 Techniques That Actually Work"
SPEED = 0.82
ACCENT = (190, 150, 255)  # violet (EP01 lime, EP02 sky, EP03 coral)
SKY, VIO, YEL, LIME, CORAL, PINK = (108, 196, 255), (190, 150, 255), (255, 211, 105), (182, 243, 92), (255, 122, 89), (255, 160, 200)
BADGE = "Illustration: real replies vary"

CTX = [("I sell handmade soy candles on Etsy.", "Who you are", SKY),
       ("Write a product description for my lavender candle.", "The task", VIO),
       ("It burns for 40 hours and comes in a reusable glass jar.", "The details", YEL),
       ("Most buyers get it as a gift.", "Who it's for", LIME)]
FMT = [("Under 80 words.", "Length", PINK), ("Warm, calm tone.", "Tone", SKY),
       ("Format: a title line, two short sentences, then three bullet points.", "Structure", YEL)]

SCENES = [
dict(chapter="The result", say="Same AI, same question. This prompt gets a bland, generic answer. This one gets exactly what you need, on the first try. The difference isn't a secret trick. It's five simple techniques, and they work in any chatbot.",
     vis=dict(type="prompt", title="SAME AI. DIFFERENT PROMPT.", before="Write a description for my candle.", strike=4.5, hdr2="AFTER", segs=CTX + FMT[2:], size=32,
              note="Five techniques. Any chatbot.")),
dict(say="In the next eight minutes, you'll learn five prompt techniques that come straight from the official guides by OpenAI, Anthropic and Google. They work with ChatGPT, Claude, Gemini, Copilot, any of them. No experience needed. And around the middle, I'll show you the mistake almost everyone makes, that quietly makes the answers worse.",
     vis=dict(type="title", kicker="AI for beginners", text="Write Better AI Prompts", sub="5 techniques from the official guides · works in any chatbot")),
dict(chapter="The 5 techniques", say="Here they are. One, give it context. Two, say exactly what you want back. Three, show an example. Four, break big tasks into steps. And five, let the AI ask you questions. We'll use one real-life task the whole way through, a product description for a small online shop, so you can see the answer get better at every step.",
     vis=dict(type="steps", title="The 5 techniques", items=["Give it context", "Say exactly what you want back", "Show an example", "Break big tasks into steps", "Let the AI ask you questions"])),
# 1 CONTEXT
dict(chapter="#1 Give it context", say="Technique one, context. The AI knows nothing about you, your business, or your goal. So here's a simple test. Imagine you're handing this task to a smart new coworker, on their very first day. What would they need to know? Who you are. What exactly the task is. The important details. And who the result is for.",
     vis=dict(type="steps", title="The new-coworker test", items=["Who are you?", "What exactly is the task?", "What details matter?", "Who is the result for?"])),
dict(say="So instead of, write a description for my candle, you write this. I sell handmade soy candles on Etsy. Write a product description for my lavender candle. It burns for forty hours and comes in a reusable glass jar. Most buyers get it as a gift. Four short sentences, and each one answers one of those questions.",
     vis=dict(type="prompt", title="#1  GIVE IT CONTEXT", before="Write a description for my candle.", segs=CTX, delay=1.8, span=0.65)),
dict(say="And here's the kind of answer you get now. It mentions the forty hours, the reusable jar, and it talks to gift buyers. Quick note. The replies in this video are illustrations. Real answers change every time you ask, but this is the kind of difference you'll see.",
     vis=dict(type="chat", title="Example chat", badge=BADGE, gap=0.22, msgs=[("you", "I sell handmade soy candles on Etsy. Write a product description for my lavender candle. It burns for 40 hours, in a reusable glass jar. Most buyers get it as a gift."),
              ("ai", "Give the gift of a slow evening. This hand-poured lavender soy candle fills the room with a soft, calming scent for up to 40 hours. When it's done, the glass jar lives on as a planter or a pen holder. A thoughtful present for anyone who needs a break.")])),
dict(say="Pro move. You can also give the AI a role. Start with something like, you are an experienced copywriter for small online shops. Google's guide for Gemini calls this a persona. It sets the vocabulary and the level of detail, so the answer sounds like it came from someone who does this every day. Just keep it realistic, and still add the context.",
     vis=dict(type="prompt", title="PRO MOVE: GIVE IT A ROLE", hdr2="START WITH", span=0.45, size=40, segs=[("You are an experienced copywriter", "The role", PINK), ("for small online shops.", "The field", SKY)],
              note="Role + context beats role alone")),
# 2 FORMAT
dict(chapter="#2 Say exactly what you want back", say="Technique two. Say exactly what you want back. If you don't, the AI guesses the length, the tone, and the layout. So tell it. Under eighty words. Warm, calm tone. And the structure. A title line, two short sentences, then three bullet points.",
     vis=dict(type="prompt", title="#2  SAY EXACTLY WHAT YOU WANT BACK", hdr2="ADD TO THE PROMPT", segs=FMT, span=0.7)),
dict(say="Now the answer has exactly the shape you asked for. You can paste it straight into your shop, without rewriting anything. And because you asked for bullets, it's easy to scan on a phone, where a lot of people shop.",
     vis=dict(type="chat", title="Example chat", badge=BADGE, gap=0.15, size=29, msgs=[("you", "... Under 80 words. Warm, calm tone. Format: a title line, two short sentences, then three bullet points."),
              ("ai", "Lavender Calm Soy Candle\nUnwind with the soft scent of lavender, hand-poured in small batches. A simple gift that says: take a break.\n•  Up to 40 hours of clean, even burn\n•  Reusable glass jar\n•  Natural soy wax")])),
dict(say="Pro move. When you're comparing things, ask for a table, and name the columns. For example, compare these three laptops in a table, with columns for price, battery life and weight. One look, and you can decide.",
     vis=dict(type="tip", tag="PRO MOVE", text='Comparing things? Ask for a table and name the columns: "...in a table with columns: price, battery life, weight."', color=SKY)),
# REENGAGE ~3:00
dict(chapter="The mistake almost everyone makes", say="Now, the mistake almost everyone makes. When the answer isn't right, we pile on rules about what not to do. Don't be boring. Don't use jargon. Don't make it long. The problem is, a don't only tells the AI what to avoid. It doesn't tell it what to do instead.",
     vis=dict(type="prompt", title="THE MISTAKE ALMOST EVERYONE MAKES", hdr2="WHAT WE TYPE", grow=True, span=0.5, segs=[("Don't be boring.", "", CORAL), ("Don't use jargon.", "", CORAL), ("Don't make it long.", "", CORAL)], breaks=True,
              note="A \"don't\" says what to avoid, not what to do", notecol=CORAL)),
dict(say="OpenAI's own guide gives this exact advice. Say what to do, instead of what not to do. So, don't use jargon, becomes, use words a twelve year old would understand. Don't make it long, becomes, three sentences maximum. And don't be boring, becomes, start with a surprising fact. Every rule now points somewhere. By the way, this works on people too.",
     vis=dict(type="compare", title="Say what to DO instead", left=("Don't...", ["Don't use jargon", "Don't make it long", "Don't be boring"]),
              right=("Do this instead", ["Use words a 12-year-old knows", "Three sentences maximum", "Start with a surprising fact"]))),
# 3 EXAMPLES
dict(chapter="#3 Show an example", say="Technique three, show an example. Describing a style in words is hard. Showing it is easy. If you already have something you like, paste it in, and ask the AI to match it. This is called few-shot prompting, and it's one of the most reliable techniques in all three official guides.",
     vis=dict(type="prompt", title="#3  SHOW AN EXAMPLE", hdr2="PROMPT", span=0.7, breaks=True, size=33, segs=[("Here is a description I wrote that I love:", "Intro", SKY),
              ('"Cedar & Smoke. Like a campfire, without the smoke in your hair. 45 hours of slow, even burn."', "The example", YEL),
              ("Write the lavender candle in the same style and length.", "The task", VIO)])),
dict(say="And the answer copies the rhythm. A short name. A playful line. Then the burn time. One good example often beats a whole paragraph of instructions.",
     vis=dict(type="chat", title="Example chat", badge=BADGE, gap=0.25, msgs=[("you", "... Write the lavender candle in the same style and length."),
              ("ai", "Lavender Calm. Like a quiet Sunday morning, in a jar. 40 hours of soft, slow glow.")])),
dict(say="Quick tip. When you paste text into a prompt, put it between quotes, or between simple tags, like example in angle brackets. That way the AI knows exactly where your instructions end, and where the material begins. This matters most when you paste long emails or documents. Both OpenAI and Anthropic recommend this.",
     vis=dict(type="tip", tag="TIP: USE DELIMITERS", text='Wrap pasted text in quotes or tags: <example> ... </example>. The AI can tell your instructions from your material.', color=YEL)),
# 4 STEPS
dict(chapter="#4 Break big tasks into steps", say="Technique four. Break big tasks into steps. If you ask for everything in one giant prompt, you usually get an average result for every part. Instead, ask for one step, check it, then ask for the next. For our shop, step one, list ten name ideas. Step two, you pick your favorite. Step three, write the description. Step four, write three titles for the listing.",
     vis=dict(type="flow", title="One big task, four small prompts", check=True, steps=["List 10 name ideas", "You pick your favorite", "Write the description", "Write 3 listing titles"])),
dict(say="It looks like this. Give me ten name ideas for a lavender soy candle, just the names, numbered. Then you pick one, and in your next message, you say, write the description for number three. The chat remembers the conversation, so you don't need to repeat everything. And if one step goes wrong, you fix just that step, instead of starting over.",
     vis=dict(type="chat", title="Example chat", badge=BADGE, gap=0.2, size=29, msgs=[("you", "Give me 10 name ideas for a lavender soy candle. Just the names, numbered."),
              ("ai", "1. Lavender Calm   2. Quiet Fields   3. Sunday Slow\n4. Purple Hour   5. Soft Landing   6. Field Notes\n7. Dusk & Lavender   8. Still Water   9. Hush   10. Linen Sky"),
              ("you", "I love number 3. Write the description for Sunday Slow, same format as before.")])),
dict(say="And for anything with logic or math, add one line. Work through it step by step, then give the final answer. The official guides call this giving the model time to think, and it helps it make fewer mistakes.",
     vis=dict(type="tip", tag="MATH OR LOGIC?", text='Add: "Work through it step by step, then give the final answer."', color=LIME)),
# 5 QUESTIONS (REENGAGE ~6:00)
dict(chapter="#5 Let the AI ask you questions", say="Technique five, my favorite, and the one almost nobody uses. Instead of guessing what to include, let the AI interview you. Just end your prompt with one line. Before you start, ask me up to three questions about anything you need to know.",
     vis=dict(type="prompt", title="#5  LET THE AI ASK YOU QUESTIONS", hdr2="END YOUR PROMPT WITH", span=0.5, size=40, segs=[("Before you start,", "", VIO), ("ask me up to 3 questions", "The magic line", YEL), ("about anything you need to know.", "", VIO)])),
dict(say="Now the AI asks for what's missing. What's the price? Is the wax vegan? Where will this text appear? You answer in a few words, and the result fits your situation, instead of a generic guess. It also shows you what you forgot to mention, which is useful on its own.",
     vis=dict(type="chat", title="Example chat", badge=BADGE, gap=0.3, msgs=[("ai", "Happy to help! Three quick questions:\n1. What's the price?\n2. Is the wax vegan or cruelty-free?\n3. Where will this text appear: Etsy, Instagram, or both?"),
              ("you", "1. $24   2. Yes, 100% vegan   3. Etsy only")])),
dict(say="And remember, the first answer is a draft, not the final. Don't just say, make it better. Give specific feedback, like you would to a person. Keep the first sentence. Make the bullets shorter. Swap the word cozy for something fresher.",
     vis=dict(type="compare", title="Feedback that actually works", left=("Vague", ["Make it better", "Try again", "I don't like it"]),
              right=("Specific", ["Keep the first sentence", "Make the bullets shorter", "Swap 'cozy' for a fresher word"]))),
# BONUS TEMPLATE
dict(chapter="Bonus: a prompt template you can reuse", say="Bonus. Put all five together, and you get a template you can save in a note, and reuse for anything. Context. The task. The format. An example. And the magic line at the end. Fill in the blanks, and you're done. I keep mine in a notes app, and paste it whenever I start a new chat.",
     vis=dict(type="prompt", title="BONUS: SAVE THIS TEMPLATE", hdr2="TEMPLATE", span=0.6, breaks=True, size=32, segs=[("I am a [who you are].", "1  Context", SKY), ("Write a [what] for [who it's for].", "Task", VIO),
              ("Format: [length], [tone], [structure].", "2  Format", YEL), ('Match this example: "[paste it]"', "3  Example", LIME), ("Before you start, ask me up to 3 questions.", "5  Questions", PINK)])),
dict(chapter="The template on a new task", say="Let's try the template on something completely different. Say you want to learn Excel. I'm a total beginner with thirty minutes a day. Create a two week study plan to learn Excel. Format, a table with three columns, day, topic, and one practice task. And the magic line. Before you start, ask me up to three questions. Same five parts, brand new task.",
     vis=dict(type="prompt", title="THE TEMPLATE ON A NEW TASK", hdr2="PROMPT", span=0.65, breaks=True, size=32, segs=[("I'm a total beginner with 30 minutes a day.", "Context", SKY),
              ("Create a 2-week study plan to learn Excel.", "Task", VIO), ("Format: a table with 3 columns: day, topic, one practice task.", "Format", YEL),
              ("Before you start, ask me up to 3 questions.", "Questions", PINK)])),
dict(say="The AI asks what version of Excel you have, and what you want to use it for. You answer, and you get a plan that fits your week, in a table you can follow. Same AI as before. The prompt did the work.",
     vis=dict(type="chat", title="Example chat", badge=BADGE, gap=0.22, size=29, msgs=[("ai", "Great goal! Two questions first:\n1. Which Excel do you have: Microsoft 365, 2021, or the free web version?\n2. What will you use it for: work reports, budgeting, or school?"),
              ("you", "Microsoft 365. Monthly sales reports at work."),
              ("ai", "Day 1  |  Cells, rows and columns  |  Build a 10-row sales table\nDay 2  |  SUM and AVERAGE  |  Total each month\nDay 3  |  Sorting and filtering  |  Find the top 5 sales")])),
# COMMON MISTAKES
dict(chapter="Common mistakes", say="Four quick mistakes to avoid. First, trusting every fact. AI can sound completely sure and still be wrong, so always check numbers, dates, names and quotes. Second, pasting private information. Never paste passwords, bank details, or confidential work. Third, asking ten things in one prompt. One step per message. And fourth, giving up after the first try. The magic is in the follow-up. And when the answer really matters, ask where the information comes from, then check that source yourself.",
     vis=dict(type="compare", title="4 mistakes, 4 fixes", left=("Mistake", ["Trusting every fact", "Pasting private info", "Ten tasks in one prompt", "Giving up after one try"]),
              right=("Fix", ["Check numbers, dates, quotes", "No passwords or secrets", "One step per message", "Give specific feedback"]))),
# PRO TIP
dict(chapter="Pro tip: Shift + Enter", say="Pro tip. In most chat apps, pressing Enter sends your message right away. Press Shift and Enter together instead, and you get a new line. That's how you write a clean prompt, with context, format and example on separate lines, without sending it halfway through.",
     vis=dict(type="keys", title="PRO TIP: a new line without sending", keys=["Shift", "Enter"], sub="Write your prompt on separate lines, then press Enter to send")),
# RECAP
dict(chapter="Recap", say="Quick recap. Give it context, with the new coworker test. Say exactly what you want back. Show an example. Break big tasks into steps. And let the AI ask you questions. Plus, say what to do, not what to avoid. Five techniques, and better answers on the first try.",
     vis=dict(type="steps", title="Recap", items=["Context: the new-coworker test", "Format: length, tone, structure", "Example: show, don't describe", "Steps: one prompt per step", "Questions: \"ask me up to 3\""])),
dict(say="Next on Shortcut Lab, Git in ten minutes. How to save every version of your work, and go back in time when something breaks. Subscribe, so you don't miss it.",
     vis=dict(type="outro", next="Git in 10 Minutes: Save Every Version of Your Work")),
]
