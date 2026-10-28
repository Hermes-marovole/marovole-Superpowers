---
name: interview-quote-image-posts
description: "Use when user says 大佬说, or for interview 字幕长图 posts."
version: 2.0.0
author: 智子
license: MIT
metadata:
  hermes:
    tags: [字幕长图, xiaohongshu, douyin, wechat, 图文, interview, yt-dlp]
    related_skills: [native-subtitle-quote-image, cn-social-image-post-publishing, creator-channel-analytics, ego-browser, content-grounding]
---

# 外文访谈 → 中文字幕长图帖（选题 → 出图 → 审核 → 发布 → 看数据）

## 「大佬说」= 本格式的代号（用户定）
用户说「做一条大佬说 <链接>」时不再解释：按本 skill 跑到「审核 PASS + 发布包齐全」为止，发布/存草稿等用户一句话。格式 = 小红书爆款黄仁勋帖同款：名人亲身经历/反差观点，3–6 张 3:4 字幕长图（用户定：看内容，故事够就放宽到 6 张，不凑数），标题「名人/身份：反差原话？」≤20 字，正文①②③对应三图，#大佬说 话题。
- 链接是 YouTube 上的中文搬运切片（标题/简介是中文）时，先 `web_extract` 该链接：页面自带英文转写，取其中一句英文原话 `web_search`，媒体报道/博客通常直接点名节目和主持人；再 `yt-dlp --flat-playlist` 搜「主持人+嘉宾」得到原片 ID，只拉 `--skip-download --write-auto-subs --sub-langs en` 的 vtt，grep 关键句得到时间点，不必下载视频或跑 whisper。核实后先把原片链接、频道、时间点和可切素材量报给用户，再开工。
- 链接是 X/抖音上的短切片（常带烧录字幕）时：切片只当线索，不用其画面。whisper 转写切片 → yt-dlp 搜候选长访谈、拉字幕 grep 关键原句定位原片和时间点 → `--download-sections "*A-B" --force-keyframes-at-cuts` 只下那一段（script.json 的 t 要减去 A）。切片前后的连续段落通常够切满 3 张。
- render-script 每张最多 7 个时间点，超了会直接拒渲。
- 切片原话只有约 2 分钟（不够 3 张）时：先做 2 张核心观点图，再从同一期访谈相邻段落补 1–2 张同气质的反差内容（如「外界以为 X，其实相反」），标题改成能同时覆盖全部图的说法；不要把 2 分钟硬拆成 4 张薄图。只放讲者自己说的话：主持人的问句/定性（如「你爱演讲」）不能当他的原话，图上用「外界以为…？」这类转述并确认他随后明确否认。
- **黄仁勋不再用**（用户 10-23 定：他已发 5 篇，第 5 篇讲观点只有 362 观看），选题从其他大佬里挑，优先逆袭/屈辱经历而非观点访谈。
- 小红书网页端作者评论菜单只有「删除评论」，没有「置顶」：置顶评论只能在 App 里长按设置。网页能做的是先发好作者评论（`.inner-when-not-active` 点开 → insertText →「发送」），再请用户在 App 里置顶。
- 「大佬说」只选高科技行业和高财富大佬（黄仁勋/马斯克/扣克伯格/孙正义/纳德拉/贝索斯/巴菲特这类），符合账号关注点；娱乐/体育名人不入这条线。候选池：`~/HermesWork/字幕长图/选题池-科技财富大佬.md`、`-第2批.md`、`-第3批.md`（马斯克 Babylon Bee/USC、乔布斯癌症/被开除）；开新一批前先读最新一批的未用已核项。同一演讲有多个版本时先用 `--print "%(height)sp %(subtitles.en.0.ext|none)s"` 比画质，官方频道也可能只有 240p（斯坦福乔布斯演讲应该用 Steve Jobs Archive 的 1080p 版）。
- 用户给的链接里讲者国内认脸度不够（如 Alexandr Wang、哈萨比斯），不要靠身份标题硬做，先说明并建议换人；用户已驳回过这种做法。候选池见 `~/HermesWork/字幕长图/选题池-名人-第N批.md`。
- **认脸门槛 = 中国大众「非常熟知」，不是「财经圈有名」**：自己推荐选题时只从第一梯队挑（马斯克、乔布斯、巴菲特、盖茨、扎克伯格、贝索斯、马云这类，黄仁勋已暂停）；埃里森、达利欧这类「需要写身份才认得」的人被用户驳回过，靠「甲骨文创始人」这种身份前缀撑不起来。故事再强也先过这一关，过不了就别排第一推荐。
- **用户点名一个大佬（「做马斯克的」）时，一次给出该人 3–5 个可切故事**，分「已核（附视频 ID+时间区间）/待核（缺字幕等）」，标出今天推荐哪条、哪条因隔周规则要等。找法：先 `web_search "<人名> interview <故事关键词>"` 让媒体报道列出他亲口讲过的窘迫故事（打零工、睡办公室、被霸凌、被拒），再 `yt-dlp --flat-playlist "ytsearch6:<节目/场合>"` 找官方长访谈，`--skip-download --write-auto-subs --sub-langs "en.*"` 拉字幕 → vtt2txt → python 正则只对正文做 `\b` 词边界匹配（直接 grep 数字如 17 会命中时间戳），命中后按时间区间拼整段原文读。只出现在传记/他人转述里的故事（如马斯克锅炉房、PayPal 蜜月被罢免）不算已核，需找到本人视频原话。
- 用户点名国内中文访谈（如孙宇晨×邵艾伦播客）时：先给切角+版权/人设风险让用户拍板，别直接开工；用户已驳回过（国内博主原创节目搬运投诉风险高、外国人优先）。
- 从 analysis-pool2 的 txt 切 transcript 时用正则 `\[\s*([\d.]+)-\s*([\d.]+)\]\s?(.*)` 取正文，不要用 `awk -F'[][]'`：字幕里的 [snorts]/[laughter] 会把句子截断，审核模型会据此误判「原文没有这句」，白烧一轮。
- 同一人物连发（尤其同一期访谈、同一背景）时，封面要和之前几篇拉开区别（用户要求）：换表情（笑脸/手势帧，用 hero_t 指定）+ 改主画面大小（`--hero-fraction 0.66` 脸更大）。出图后把新封面和历史封面拼一张对比图自查。
- 未成年抽烟/喝酒等情节（如黄仁勋 9 岁抽烟一周）即使是原话也不上图，平台对未成年不良行为内容审核严。
- 极限词与违禁风险（平台审核）：标题和图上字幕严禁出现绝对化极限词「最」（如「最年轻」「全美最穷」「世界最…」），国内社交平台极易被判虚假夸大或限流，一律改用「极穷」「极年轻」「极其贫困」「数一数二」等不带「最」的表述。
- 源视频右下角有台标/网址水印（如 BABYLONBEE.COM）时，字幕条默认取画面 0.88 高度会把水印切进每条字幕：render-script 加 `--frame-bottom 0.82 --band-center 0.72`（主画面和字幕条都避开水印），出图后打开原图确认。
- 核对自动字幕里的否定句、关键数字时用本机 `whisper-cli -m ~/models/whisper/ggml-large-v3-turbo.bin -l en -f x.wav -otxt -of out -np`（先 `ffmpeg -ar 16000 -ac 1` 转 wav）。同一句多次转写结果不同（如 "didn't get any response" / "I'd get a response"）时，按上下文和其他访谈的报道判断，把分歧写进 packet 和来源记录，图上措辞取保守说法。
- 渲染脚本（`native_subtitle_stitch.py`）已支持 script.json 顶层 `hero_t`：主画面强制取 hero_t 帧而非 lines[0].t 帧，用于多机位访谈开场是远景、讲者特写在后段的场景。hero_t 时间必须是该视频文件内（分段下载时为所在分段内）的相对秒。

**爆款选题规律（本账号后台实测）**：名人「底层屈辱/被否定/极端狼狈」的亲身经历（刷厕所、被骂没出息驱出家门、9 岁寄宿学校、被拒 30 次）是高播放主线（12w+/5.8w/3.6w 级）；纯商业资金链危机叙事（如公司濒临破产）受众缺乏代入感，播放掉到千级。选题时优先前者的反差故事。

- 公司版交付（2026-10-09 起）：用户说「给公司用的」「发给同事发布」时，交付形态 = 发布包文件夹（图 ×N + 小红书/抖音/公众号贴图 三份 txt + 发布说明.md）；我不登录任何平台，发布由同事执行。公司卖补剂：图上字幕和文案不得出现「别依赖补剂」等贬低补剂的表述——即使原话如此也要删句重排（施瓦辛格补剂段即按此只留正面句）。

用户要把英文访谈或演讲（名人、科学家、健康专家）做成「真人画面 + 中文字幕条」的 3:4 长图，发小红书、抖音图文和公众号贴图时用。
渲染交给 `native-subtitle-quote-image` 的脚本字幕模式（`render-script`）。本 skill 管渲染前后的所有环节和本机约定。

## Goal
从一条公开访谈（故事有后续时可再加一条后续事件的官方视频）里切出同一主题的 2–6 张字幕长图，组成一篇帖子。中文要逐句对得回英文原文。审核通过后发布，之后回后台看数据，决定下一批做什么。

## Success
- 一篇帖子是 2–6 张同主题的图，张数看内容：一段完整故事或多段强经历就开到 4–6 张，素材单薄就 2–3 张，不凑数。不要一张图发一篇。每张图讲一个观点，用 5–7 句连贯原话。
- 每句中文都能对到 `analysis/transcript.txt` 同一时间段的英文。文案里的每个事实都能在原文里找到。
- 每张图的第一帧是讲者正脸特写；封面第 1 张尤其必须一眼认出是谁（用户 2026-10-14 驳回过看不到小扎正脸的封面）。没有黑条、没有切脸、字幕完整，并且都打开原图看过。
- Gemini 审核结果为 `OVERALL: PASS`。发布后以后台读到的状态为准，不以脚本的自报为准。
- 发布包齐全：`发布包-<批次>/<NN-讲者-主题>/{01_..jpg,02_..jpg,03_..jpg,小红书.txt,抖音.txt,公众号贴图.txt}`，加上 `review-*.md`。

## Constraints
- 事实红线：中文只翻译或压缩，不加原话里没有的东西。标题不能比图里的内容说得更宽，例如原话没提鸡蛋，标题就不能写鸡蛋。名人故事的标题可以用反差加问号，但答案必须在图里。
- 图上字幕是后期译制的，不是原生字幕。`来源记录.md` 和文案出处行都要写「中文字幕为译制」。
- 每篇正文末尾写出处：`来源：<频道/媒体> <讲者+场合>（YouTube 官方频道），中文字幕为译制。` 健康类再加 `内容为受访者观点，不构成医疗建议。`
- `小红书.txt` 必须有 `媒体：<原频道名>` 这一行。脚本用它填「来源转载」声明，缺这一行会直接报错，不会用默认值。
- 发布、定时发布和删帖都是敏感操作。用户说「审过就发」或「排上」，并且审核是 PASS，才能执行；否则只存草稿。公众号只推草稿，由用户在公众号助手 App 里点发表。定时发布时一次问清平台组合和时刻，之后批量排，不再逐篇追问。
- 新号每平台每天最多 1–3 篇，按 1 篇排。同一时段不要连发，几篇会互相抢流量。
- 系统 python 是 3.9，渲染一律用 `~/.hermes/venvs/nsqi/bin/python`。跑 yt-dlp 前先 `unset PYTHONPATH PYTHONHOME`。
- yt-dlp 一律写全路径 `/opt/homebrew/bin/yt-dlp`：后台/部分 shell 的 PATH 会先命中 `~/Library/Python/3.9/bin/yt-dlp`（2025 旧版），换 player_client 也只会报 unavailable/403。YouTube 报「Sign in to confirm you're not a bot」时，用 ego-browser 打开 youtube.com，`page.cdp("Network.getCookies",{urls:[youtube/google 域]})` 导出 Netscape 格式到 `~/.hermes/cache/scratch/yt/cookies.txt`（0600），再 `--cookies` 传入；本机没有 Chrome cookie 库，`--cookies-from-browser chrome` 不可用。
- 补「后续/当面致谢」类画面时，优先选无烧录字幕的通讯社版本（如 Reuters）；日媒现场版常带日文硬字幕，会和字幕条打架。

## Procedure
1. **选题池**：用 `yt-dlp --flat-playlist` 搜索候选，按 `references/sourcing-and-rendering.md` 的标准排序，写进 `选题池-<线>-第N批.md`（链接、频道、时长、播放量、可切的故事、标题草稿，可切的故事都标「待字幕核实」）。名人线另看 `references/celebrity-track.md`；健康个人号（名人怎么吃/练/抗衰）看 `references/health-track.md`。
2. **下载**：整片用 `scripts/dl.sh <NN-讲者-主题> <YouTube ID>`，会轮换 player_client 并重试。长播客只要一段时：把 yt-dlp 命令（含 `-o 'source/seg.%(ext)s'` 这类带括号参数）写进 .sh 文件再 `bash` 执行——直接塞进 terminal 一行会因括号报 bash eval 语法错；下完 `ln -sf seg.mp4 source/video.mp4`，render_all.sh 只认 video.mp4。字幕转写 `scripts/vtt2txt.py <in.vtt> <out.txt>` 必须给两个参数（不写 stdout）。新批次目录编号先 `ls -d` 全局（含 发布包-*/ 里的子目录）取最大号+1，避免与已发布包撞号；做完把工作目录整个 mv 进 `发布包-<批次>/` 再把成品 jpg 拷到目录根。macOS 的 `sed -i` 要写 `sed -i ''`。写 `来源记录.md`（URL、标题、频道、时长、字幕类型、下载日期、模式=脚本字幕、版权归属）。
3. **选句**：在 transcript 里定位故事段落。字幕定位不到的故事就换一段，不硬写。
   - 故事有「结局/回响」（多年后致谢、重逢、回应），或用户说「后来他还说过 X」而本访谈里没有：不要直接回「他没说过」。先 web_search 中英文各查一次后续新闻，打开原文核实引语和日期，再用 yt-dlp 搜现场的官方视频（路透/官方频道/现场全程）。核实后可以做成末张「结局图」，这种结尾的情绪冲击比纯字幕强。帖子用到两个来源时，出处行两个都写，`来源记录.md` 也分两段记录。
   - 用户补充的事实同样要过核验：本访谈里只有近似说法（例如主持人说了，讲者只回一句附和）时，图上只能放讲者实际说出的那句，不能把近似说法升级成他的原话。每张图选 5–7 句连续论证，过渡句可以跳过。第一句写明主语，不要用「他们/它」开头。
4. **写 script.json**：`lines[].t` 取字幕区间的中点，必须严格递增。每行约 ≤17 字，长句拆到同一区间内的两个时间点。用 `sample -t ... --around 0.8` 检查第一帧，必须是讲者正脸特写。注意：多机位现场访谈（播客现场舞台）前十几秒常见导播在双人全景/远景机位，讲者只有几十像素——第一帧绝不能取在 `lines[0].t` 附近的默认位置，先在同一段视频里扫找讲者单人近景特写帧（人脸占画面要够大），再把这个时间写进 script.json 顶层 `hero_t` 字段（渲染脚本已支持：`{"hero_t": 20.0, "lines": [...]}`，主画面取 hero_t 帧，字幕条仍按 lines[].t 取帧）。单人舞台演讲（毕业演讲这类）通常全程中景、没有近景特写：主画面标准放宽为「正脸清楚、睁眼、人脸够大」的清晰中景帧，先用 `sample --start A --end B --interval 4` 扫候选再挑帧，不要因为找不到特写就整个换视频。
5. **渲染和质检**：改动或重命名 script.json 前，必须先删除旧的 `*.script.json` 及 `output-v1/*.jpg`（`render_all.sh` 遍历目录下所有 script.json，残留旧文件会导致发布包产出重复废图）。跑 `scripts/render_all.sh <目录>`，渲染全部 script.json 并生成 sheet.jpg。逐张打开原图检查。出现黑条说明那个时间点是 B-roll，用 `sample --start A --end B --interval 0.5` 找到讲者帧，把 t 挪过去后加 `--overwrite` 重渲。分段下载的素材（source/a.mp4..d.mp4）没有统一 video.mp4 时，render-script 直接对单段 mp4 渲染（script.json 的 t 是该段内相对时间，见来源记录.md）；主特写在别的分段时也先在该段里找等价近景帧。**每张图来自不同分段时不要用 `render_all.sh`**：它只渲染 source/video.mp4 且会遍历目录下所有 script.json。改在帖子目录写一个 `render.sh`，逐行把「script.json → 所属分段 mp4」按表渲到 output-v1/，末尾用 PIL 拼 sheet（图源分段多时一张图可能需要再补下载一个更宽的分段，如网景简历+公司被收购两句分属两处）。播客「越肩机位」（讲者正脸偏左、主持人后脑在右）是常态，人脸占主图约 1/4 宽、清晰睁眼即可接受，不必为此换片；真正要避开的是双人全景帧（扫描图里讲者只有几十像素）。质检可用人脸检测硬校验：`cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml').detectMultiScale(灰度图)`，成品主图区应检出 ≥200px 的正脸框，否则换帧重渲。
6. **写文案**：格式见 `references/platform-publishing.md`。正文用「① ② ③ 依次对应三张图」，标题 ≤20 字。
7. **审核闸门**：packet = 每张图前后各留余量的英文原文 + 图上中文字幕 + 各平台文案。原文必须覆盖中文字幕提及的全部上下文（若字幕包含前几句交代的地名/背景，packet 必须将上文段落一并囊括，否则审校模型会判「引入未经提及的外部背景」而报 FIX）。改文案或字幕后必须同步更新 packet 里的内容再重审（只改 txt/script 不改 packet 会白烧一轮）；不要为了让审核过而对 packet 删改英文原文。跑 `hermes -z "$(cat review-prompt.md review-packet.md)" --provider antigravity-oauth -m gemini-3.8-flash > review-gemini-N.md`。结果是 FIX 时，先回原文核对再改（如监管语境 check up on 应译为「查房/巡查」而非温情的「照看」；审稿模型误报也要辨析）。改完重审，直到 PASS。prompt 模板在 `templates/review-prompt.md`，复制到帖子目录后把里面「1 条（3 张图）」改成实际张数（`sed -i ''`）；把三个平台 txt 也追加进 packet 一起审。写 script.json 时就避开审校模型必抓的两类翻译问题：
   - 动作动词按原意译，不向「更惨的画面」渲染（例：return Coke bottles for the 5-cent deposits 是「退空瓶换押金买吃的」，译成「捡瓶子」就是把退押金机制脑补成拾荒）。
   - 每张图因果链要完整：关键转折句（如「直到对方保证 X 她才松口」）在本张放不下时，移到下一张首句，不要整句丢掉——跨图跳接会让审校报「因果断层」。
8. **发布**：`scripts/run_mjs.sh <帖子目录> 1 <PUBLISH 0|1> <xhs_fill.mjs|dy_publish.mjs> <SPACE id> [SAVE]`。第一篇先用 `UPLOAD=1 PUBLISH=0` 跑一遍，截图确认图数、顺序和正文（页面会显示「N/18」和手机预览），再 `UPLOAD=0 PUBLISH=1` 正式发（已在同一页，不重传）。小红书登录态与 space 的建法见 `references/platform-publishing.md` 小红书一节。发完去 note-manager 按标题核对「审核中」并 `finish`。要定时发布，就在平台的定时发布里设时间；没有定时发布时，用 cron 在设定时刻跑上面的命令。公众号贴图用 `md2wechat create_image_post`，不发小红书当天也可直接建草稿（贴图草稿不受「审核中」影响）；media_id 记进 `发布包-<批次>/wechat-receipts.tsv`。任务中途 finish 过的 space 会失效，重开一个拿新 id 再跑；resume 同名 space 会新开一个 id，不要沿用旧编号。
8b. **X（@marovole）**：用户定每天 1 篇日更（X 无长尾，日更优先），用 X 原生定时（时区 UTC+8，21:30）。文案压成短版≤280 加权字符（汉字算 2）：标题+一段钩子+「来源：…，中文字幕为译制」+#大佬说 #人名。脚本 `~/HermesWork/字幕长图/发布包-X大佬说/schedule_one.mjs`（ego-browser）；Post/Schedule 按钮被透明层挡住，要用 evaluate 里的 el.click()；fileInput 要限定在 [role=dialog] 里。核对页：x.com/compose/post/unsent/scheduled。
9. **核对**：小红书看 note-manager（`.note-card` 含标题/时间/数据行，卡片封面 img url 就是已发布的首图），抖音看 content/manage，公众号用 draft/batchget，按标题确认帖子在、图数对。删掉失败时留下的本地草稿，然后 `task.finish({keep: []})`。**小红书已发布的图文笔记不支持换图**：发现首图不达标要整篇删除重发（用户一句话拍板后执行），公众号则直接删旧草稿重推新图。
10. **看数据**：发布后 24h 和 48h 各读一次后台，方法见 `creator-channel-analytics`（小红书登录态所在 space 与取数片段见该 skill 的平台配方参考）。用户说「XX那条又爆了」但没给数字时：先按最新发布包目录猜是哪条，再直接去后台读实数，比率用代码算后再下「与哪条同档/最高」的结论。读完给用户 24h 复查点；用户要提醒时建 Mac 提醒事项，时间=发布时刻+24h 取整（见 apple-macos 的 reminders 参考）。和同期笔记比中位数倍数，算赞、藏、评、分享各占观看的比例。结果更新到 `references/celebrity-track.md` 的观察表，下一批选题按它调整。

## Stop
- 素材找不到干净的讲者特写、字幕核实不了、平台要扫码登录，或者审核出现 BLOCK：停下来，把情况交给用户。
- 发布前任一自检不过（声明、出处行、图数、话题）：脚本会打印 `CHECK FAILED` 并且不发。不要绕过检查。

## Verify
交付时说明：各平台的实际状态（后台核对的结果）、审核跑了几轮、改了什么、需要用户手动做的事，以及下一次看数据的时间。
