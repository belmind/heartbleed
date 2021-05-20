const puppeteer = require("puppeteer");
const faker = require("faker");

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    ignoreHTTPSErrors: true,
  });
  for (let i = 0; i < 1000; i++) {
    let name = faker.internet.email();
    let password = faker.internet.password();
    const page = await browser.newPage();
    await page.goto(
      `https://www.localhost:8443/index.html?username=${name}&password=${password}`
    );
    console.log("---------------------------");
    console.log(
      name + " with password " + password + " successfully logged in!"
    );
    await page.close();
  }
  await browser.close();
})();
