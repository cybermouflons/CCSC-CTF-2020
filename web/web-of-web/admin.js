const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
  const page = await browser.newPage();

    await page.setCookie({
    'value': 'ccsc{6f759aae73d7be951b5482b1e0146b0c}',
    'domain': 'localhost:5001',
    'expires': Date.now() / 1000 + 10,
    'name': 'flag'
  });
  await page.goto('http://localhost:5001/reviews');
  await browser.close();
})();
