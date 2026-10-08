// Douyin 图文 upload + self-check (+ publish if PUBLISH=1). Run via run_mjs.sh: env POST_DIR, SPACE, PUBLISH.
const fs = await import("node:fs/promises");
if (!process.env.SPACE) throw new Error("set SPACE=<TaskSpace id>");
const task = await taskSpace(Number(process.env.SPACE));
const page = task.page("p1");
const dir = process.env.POST_DIR.replace(/\/?$/, "/");
await page.goto("https://creator.douyin.com/creator-micro/content/upload?default-tab=3");
await page.waitForSelector("input[type=file]", { state: "attached", timeout: 20000 });
await page.waitForTimeout(1500);
await page.evaluate(() => { const b = [...document.querySelectorAll("span,button")].find((x) => x.innerText.trim() === "放弃"); if (b) b.click(); });
await page.waitForTimeout(1000);
const imgs = (await fs.readdir(dir)).filter((f) => f.endsWith(".jpg")).sort();
await page.setInputFiles("input[type=file]", imgs.map((f) => dir + f));
await page.waitForSelector('input[placeholder="添加作品标题"]', { state: "visible", timeout: 30000 });
await page.waitForTimeout(2500);
const txt = await fs.readFile(dir + "抖音.txt", "utf8");
const title = txt.match(/标题：(.+)/)[1].trim();
const lines = txt.split("\n").slice(1).map((l) => l.replace(/^正文：/, "")).filter(Boolean);
const tags = lines.filter((l) => l.startsWith("#")).join(" ").split(/\s+/).filter(Boolean);
const body = lines.filter((l) => !l.startsWith("#"));
await page.fill('input[placeholder="添加作品标题"]', title);
await page.evaluate(() => { const e = [...document.querySelectorAll("[contenteditable=true]")].find((x) => x.getBoundingClientRect().height > 0); e.focus(); });
for (const l of body) { await page.keyboard.insertText(l); await page.waitForTimeout(250); await page.keyboard.press("Enter"); await page.waitForTimeout(200); }
for (const t of tags) { await page.keyboard.insertText(t); await page.waitForTimeout(1200); await page.keyboard.press("Space"); await page.waitForTimeout(500); }
// 自主声明：转载 / 取材站外
await page.click("text=请选择自主声明");
await page.waitForTimeout(1200);
await page.click('text="内容为转载信息"');
await page.waitForTimeout(600);
await page.click('text="取材站外"');
await page.waitForTimeout(600);
await page.click('loc=role:button[name="确定"]');
await page.waitForTimeout(1500);
const st = await page.evaluate(() => {
  const ed = [...document.querySelectorAll("[contenteditable=true]")].find((x) => x.getBoundingClientRect().height > 0);
  return { title: document.querySelector('input[placeholder="添加作品标题"]').value, desc: ed.innerText, decl: (document.body.innerText.match(/自主声明\n(.+)/) || [])[1], imgs: (document.body.innerText.match(/已添加(\d+)张图片/) || [])[1] };
});
console.log(JSON.stringify(st));
const bad = !st.desc.includes("来源：") || /\*/.test(st.desc) || st.decl !== "内容为转载信息" || st.imgs !== String(imgs.length);
if (bad) { console.log("CHECK FAILED, not publishing"); }
else if (process.env.PUBLISH === "1") {
  await page.click('loc=role:button[name="发布"]');
  await page.waitForURL(/content\/manage/, { timeout: 30000 }).catch(() => {});
  await page.waitForTimeout(2000);
  console.log("PUBLISHED_URL", await page.url());
}
