# Builds the fictional practice bookshop used in EP17 (3 catalog pages x 8 books, robots.txt, a JS-loaded reviews box).
# Usage: python3 make_site.py <out dir>      (then: python3 -m http.server 8000 inside that dir)
import os, sys, json, random
out = sys.argv[1]; random.seed(17)
A = "Quiet Hidden Last Silver Paper Winter Northern Little Broken Golden Distant Small Open Lost Second Gentle".split()
N = "River Garden Lighthouse Map Orchard Harbor Kitchen Library Window Forest Letter Bridge Island Station Valley Notebook".split()
AU = ["Ana Moreno", "Theo Grant", "Mira Patel", "Jonas Berg", "Lucy Hale", "Omar Reyes", "Iris Cole", "Ben Okafor", "Nora Lind", "Sam Ito"]
books, used = [], set()
while len(books) < 24:
    t = f"The {random.choice(A)} {random.choice(N)}"
    if t in used: continue
    used.add(t)
    books.append(dict(title=t, author=random.choice(AU), price=round(random.choice([7, 9, 11, 12, 14, 16, 18, 22]) + random.choice([0.5, 0.99, 0.0, 0.49]), 2),
                      stars=random.choice([3, 4, 4, 5, 5, 2]), stock=random.random() > 0.25, hue=random.randint(0, 359)))
CSS = """*{box-sizing:border-box}body{margin:0;font-family:Georgia,serif;background:#f6f1e7;color:#2b2622}
header{background:#2f4a3a;color:#f6f1e7;padding:18px 28px;display:flex;justify-content:space-between;align-items:center}
header h1{margin:0;font-size:26px}header nav{font-family:Arial,sans-serif;font-size:14px;opacity:.85}
main{padding:20px 28px}h2{font-size:20px;margin:0 0 14px}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.book{background:#fff;border-radius:10px;padding:12px;box-shadow:0 1px 3px rgba(0,0,0,.12)}.cover{height:86px;border-radius:6px;margin-bottom:8px}
.title{font-size:16px;margin:0 0 4px}.title a{color:#2b2622;text-decoration:none}.author{margin:0;color:#7a6f66;font-size:13px;font-family:Arial,sans-serif}
.price{margin:6px 0 2px;font-weight:bold;font-size:17px;color:#2f4a3a;font-family:Arial,sans-serif}.stock{margin:0;font-size:12px;font-family:Arial,sans-serif;color:#3c8a4f}
.stock.out{color:#b5452f}.rating{color:#d89b1d;font-size:14px}.pager{margin-top:16px;font-family:Arial,sans-serif;font-size:14px}.pager a{margin-right:12px;color:#2f4a3a}
#reviews{margin-top:16px;background:#fff;border-radius:10px;padding:10px 14px;font-family:Arial,sans-serif;font-size:13px}.review{margin:4px 0}"""
os.makedirs(os.path.join(out, "catalog"), exist_ok=True); os.makedirs(os.path.join(out, "book"), exist_ok=True); os.makedirs(os.path.join(out, "admin"), exist_ok=True)
open(os.path.join(out, "style.css"), "w").write(CSS)
open(os.path.join(out, "robots.txt"), "w").write("User-agent: *\nDisallow: /admin/\nCrawl-delay: 1\n")
open(os.path.join(out, "admin", "index.html"), "w").write("<!doctype html><title>Admin</title><p>Staff only.</p>\n")
slug = lambda t: t.lower().replace(" ", "-")
for p in range(3):
    cards = []
    for b in books[p * 8:(p + 1) * 8]:
        st = "★" * b["stars"] + "☆" * (5 - b["stars"])
        cards.append(f"""    <article class="book">
      <div class="cover" style="background:hsl({b['hue']},45%,55%)"></div>
      <h3 class="title"><a href="/book/{slug(b['title'])}.html">{b['title']}</a></h3>
      <p class="author">by {b['author']}</p>
      <p class="price">${b['price']:.2f}</p>
      <p class="stock{'' if b['stock'] else ' out'}">{'In stock' if b['stock'] else 'Out of stock'}</p>
      <span class="rating" data-stars="{b['stars']}">{st}</span>
    </article>""")
        open(os.path.join(out, "book", slug(b["title"]) + ".html"), "w").write(f"<!doctype html><title>{b['title']}</title><h1>{b['title']}</h1>\n")
    nav = " ".join(f'<a href="page-{i}.html">{i}</a>' for i in range(1, 4)) + (f' <a class="next" href="page-{p + 2}.html">Next</a>' if p < 2 else "")
    rev = '\n  <div id="reviews">Loading reviews...</div>\n  <script>fetch("reviews.json").then(r => r.json()).then(d => { document.getElementById("reviews").innerHTML = d.map(x => `<p class="review">★ ${x.stars} - ${x.text}</p>`).join(""); });</script>' if p == 0 else ""
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Pine Street Books - Catalog page {p + 1}</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
<header><h1>Pine Street Books</h1><nav>Practice shop - for scraping lessons</nav></header>
<main>
  <h2>All books - page {p + 1} of 3</h2>
  <div class="grid">
{chr(10).join(cards)}
  </div>
  <div class="pager">{nav}</div>{rev}
</main>
</body>
</html>
"""
    open(os.path.join(out, "catalog", f"page-{p + 1}.html"), "w").write(html)
json.dump([{"stars": 5, "text": "Fast delivery, lovely shop."}, {"stars": 4, "text": "Great prices on paperbacks."}, {"stars": 5, "text": "Found a book I'd looked for for years."}],
          open(os.path.join(out, "catalog", "reviews.json"), "w"), indent=1)
print("site ok", len(books), "books")
