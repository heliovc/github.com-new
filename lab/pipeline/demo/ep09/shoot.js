// Renders each step folder in real Chromium and saves the screenshot (used on screen in EP09).
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const jobs = [['s1',720,600],['s3a',720,600],['s4a',720,600],['s4b',720,600],['s4c',390,700,'mobile'],['s2',720,600],['s3',720,600],['s4',720,600],['s4',720,600,'hover'],['s4',390,700,'mobile'],['e1',720,600],['e2',720,600]];
  for (const [d,w,h,mode] of jobs) {
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1.25 });
    await p.goto('file://' + path.resolve(__dirname, 'site', d, 'index.html'));
    if (mode === 'hover') await p.hover('.button');
    const out = `shot_${d}${mode ? '_' + mode : ''}.png`;
    await p.screenshot({ path: path.join(__dirname, out) });
    console.log(out, w + 'x' + h);
    await p.close();
  }
  await b.close();
})();
