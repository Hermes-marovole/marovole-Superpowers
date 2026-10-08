// Fill/publish one Xiaohongshu image note from a 发布包 dir (all *.jpg sorted + 小红书.txt).
// Run via run_mjs.sh: env POST_DIR, SPACE (ego-browser TaskSpace id), UPLOAD=1, PUBLISH=1 or SAVE=1.
// 小红书.txt must contain a `媒体：<原频道/媒体名>` line — it fills the 来源转载 declaration.
const fs = await import("node:fs/promises");
if (!process.env.SPACE) throw new Error("set SPACE=<TaskSpace id>");
const task = await taskSpace(Number(process.env.SPACE));
const page = task.page("p1");
const dir = process.env.POST_DIR.replace(/\/?$/, "/");
if (process.env.UPLOAD === "1") {
  await page.goto("https://creator.xiaohongshu.com/publish/publish?source=official&from=tab_switch&target=image");
  await page.waitForSelector("input[type=file]", { state: "attached", timeout: 20000 });
  const imgs = (await fs.readdir(dir)).filter((f) => f.endsWith(".jpg")).sort();
  await page.setInputFiles("input[type=file]", imgs.map((f) => dir + f));
  await page.waitForSelector('input[placeholder="填写标题会有更多赞哦"]', { state: "visible", timeout: 30000 });
  await page.waitForTimeout(2000);
  await page.evaluate(() => { const b = [...document.querySelectorAll("button")].find((x) => x.innerText.trim() === "我知道了"); if (b) b.click(); });
}
const txt = await fs.readFile(dir + "小红书.txt", "utf8");
const title = txt.match(/标题：(.+)/)[1].trim();
const lines = txt.split("正文：\n")[1].split("\n").filter(Boolean);
const tags = lines.filter((l) => l.startsWith("#")).join(" ").split(/\s+/).filter(Boolean);
const text = lines.filter((l) => !l.startsWith("#") && !l.startsWith("媒体：")).join("\n");
await page.fill('input[placeholder="填写标题会有更多赞哦"]', title);
const editor = "div.tiptap.ProseMirror";
await page.keyboard.press("Escape").catch(() => {});
await page.evaluate((s) => document.querySelector(s).focus(), editor);
await page.keyboard.press("ControlOrMeta+a");
await page.keyboard.press("Backspace");
for (const l of text.split("\n")) { await page.keyboard.insertText(l); await page.waitForTimeout(300); await page.keyboard.press("Enter"); await page.waitForTimeout(200); }
const result = [];
for (const t of tags) {
  await page.keyboard.insertText(t);
  await page.waitForTimeout(1800);
  const hit = await page.evaluate((tag) => {
    const e = [...document.querySelectorAll("div.item")].find((d) => d.innerText.split("\n")[0].trim() === tag && d.getBoundingClientRect().height > 0);
    if (!e) return null; const r = e.getBoundingClientRect(); return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
  }, t);
  if (hit) { await page.mouse.click(hit.x, hit.y, { label: "pick exact topic" }); result.push(t + "✓"); }
  else { await page.keyboard.press("Space"); result.push(t + "(plain)"); }
  await page.waitForTimeout(600);
}
const content = await page.evaluate((s) => document.querySelector(s).innerText, editor);
console.log({ title, tags: result.join(" ") });
console.log(content);
if (process.env.PUBLISH === "1") {
  await page.evaluate(() => { const e = [...document.querySelectorAll("*")].find((x) => x.children.length === 0 && x.innerText === "添加内容类型声明"); e && e.scrollIntoView({ block: "center" }); });
  await page.waitForTimeout(800);
  await page.click("text=添加内容类型声明");
  await page.waitForTimeout(1000);
  await page.hover("text=内容来源声明");
  await page.waitForTimeout(1000);
  await page.click('text="来源转载"');
  await page.waitForTimeout(1500);
  const media = (txt.match(/媒体：(.+)/) || [])[1]?.trim();
  if (!media) throw new Error("小红书.txt 缺少 媒体： 行，拒绝用默认值填转载声明");
  await page.fill('input[placeholder="请输入媒体名称"]', media);
  await page.waitForTimeout(500);
  await page.click("loc=role:button[name='确认']");
  await page.waitForTimeout(1500);
  const decl = await page.evaluate(() => document.body.innerText.includes("来源转载"));
  const okBody = (content.includes("来源：") || content.includes("原作者")) && content.includes("[话题]");
  console.log({ decl, okBody });
  if (!decl || !okBody) { console.log("CHECK FAILED, not publishing"); }
  else {
    await page.click("loc=role:button[name='发布']");
    await page.waitForURL(/publish\/success/, { timeout: 20000 }).catch(() => {});
    console.log("PUBLISHED_URL", await page.url());
  }
}
if (process.env.SAVE === "1" && process.env.PUBLISH !== "1") {
  await page.click("loc=role:button[name='暂存离开']");
  await page.waitForTimeout(3000);
  console.log("saved ->", await page.url());
}
