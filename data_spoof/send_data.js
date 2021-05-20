const puppeteer = require("puppeteer");
const faker = require("faker");

(async () => {
  const browser = await puppeteer.launch({
    // launch chromium browser
    headless: true,
    ignoreHTTPSErrors: true, // Needed because vulnerable OpenSSL version
  });
  for (let i = 0; i < 1000; i++) {
    // 1000 fake users
    let email = faker.internet.email(); // generate email
    let password = faker.internet.password(); // generate password
    const page = await browser.newPage(); // open a new page
    await page.goto(
      // go to vulnerable site
      `https://www.localhost:8443/index.html?username=${email}&password=${password}`
    );
    console.log("---------------------------");
    console.log(
      "INFO:" +
        email +
        " with password " +
        password +
        " successfully logged in!"
    );
    await page.close(); // close page
  }
  await browser.close(); // close browser
})();
