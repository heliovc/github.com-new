// Renders the practice shop in real Chromium (served on localhost:8000), saves screenshots and the REAL bounding boxes of the
// elements each CSS selector matches (boxes.json, page fractions) - used by the "scrape" scene in EP17.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const b = await chromium.launch(); const out = {};
  const p = await b.newPage({ viewport: { width: 1000, height: 700 }, deviceScaleFactor: 1.5 });
  await p.goto('http://localhost:8000/catalog/page-1.html'); await p.waitForSelector('.review');
  await p.screenshot({ path: path.join(__dirname, 'shot_page1.png'), fullPage: true });
  const dims = await p.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.scrollHeight]);
  out.size = dims;
  for (const sel of ['article.book', '.title', '.price', '.rating', '#reviews', '.pager a', 'h2']) {
    out[sel] = await p.$$eval(sel, (els, d) => els.map(e => { const r = e.getBoundingClientRect(); return [r.x / d[0], (r.y + scrollY) / d[1], r.width / d[0], r.height / d[1]]; }), dims);
  }
  const q = await b.newContext({ viewport: { width: 1000, height: 700 }, deviceScaleFactor: 1.5, javaScriptEnabled: false });
  const p2 = await q.newPage(); await p2.goto('http://localhost:8000/catalog/page-1.html');
  await p2.screenshot({ path: path.join(__dirname, 'shot_page1_nojs.png'), fullPage: true });
  fs.writeFileSync(path.join(__dirname, 'boxes.json'), JSON.stringify(out));
  console.log('ok', dims, Object.keys(out).map(k => k + ':' + out[k].length).join(' '));
  await b.close();
})();
