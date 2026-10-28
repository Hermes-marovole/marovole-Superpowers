# 文案格式与各平台发布

## 文案（发布包目录内 txt）
小红书.txt 一律写标记格式：首行 `标题：xxx`，下一行 `正文：`，之后逐行正文。skill 目录里的 xhs_fill.mjs 只认这种格式（自然格式会在 `match(...)[1]` 处报 Cannot read properties of null）；`字幕长图/scripts/xhs_fill.mjs` 新版虽认自然格式，却会把标题行也当正文插进编辑器，所以别用自然格式。话题单独一行，另加 `媒体：<频道>` 行（只供脚本用，不进正文）。公众号贴图.txt 则是「标题 + 空行 + 正文」，用 `head -1` / `tail -n +3` 拆给 md2wechat。
- 发布用的图 jpg 必须位于帖子目录**根目录**、按文件名排序即图序（00_首图、01_、02_…）；output-v1/ 里渲出来的成品要先移到根目录再发布，`sheet.jpg` 会被脚本自动排除。只把图留在 output-v1/ 里跑发布脚本，会上传不了任何图。
| 平台 | 标题 | 正文 | 话题 |
|---|---|---|---|
| 小红书 | ≤20 字 | 一句引入 + ①②③… 依次对应各图（N 张写「N 张图依次对应，滑动看原话～」） + 出处行；另加 `媒体：<频道>` 行（只供脚本用，不进正文） | 5–8 个（脚本逐个点选，少于 5 个补通用话题） |
| 抖音图文 | ≤20 字 | 2–3 句 + 出处行 | 3–5 个 |
| 公众号贴图 | 同小红书 | 小红书正文去掉话题 | 无 |

## 小红书（xhs_fill.mjs）
- 登录态在 ego-lite 的 Profile 6，新建 space 必须带 profile：`taskSpace("<名>", { profileId: "Profile 6" })`，建完先 goto `creator.xiaohongshu.com/new/home` 看是否停留（跳到短信登录页就是 profile 选错了）。默认 profile 的 space 没有登录，脚本会在 `input[type=file]` 处超时；建错的空 space 直接 `finish({keep:[]})` 后用 Profile 6 重建，别在里面折腾登录。
- 上传页 `creator.xiaohongshu.com/publish/publish?source=official&from=tab_switch&target=image`，上传后关掉「我知道了」弹窗。
- 正文编辑器是 `div.tiptap.ProseMirror`。用 evaluate 调 `.focus()` 聚焦，直接点击会被浮层拦住。正文必须逐行 insertText 再按 Enter，一次插多行顺序会乱。每篇都重新打开上传页，在旧内容上重填会混进旧稿。
- 话题：输入 `#xx` 后等下拉出现，点 `div.item` 里首行文字完全一致的那一项，正文里出现 `#xx[话题]#` 才算选中。不要直接按 Enter，会选中推广话题。
- 声明：先把「添加内容类型声明」scrollIntoView，然后 hover「内容来源声明」→ 点「来源转载」→ 填媒体名称 → 确认。成功后 URL 包含 `publish/success`。
- 定时发布（属于发布动作，需要用户授权）：在「更多设置」里点 `.custom-switch-card`「定时发布」的 `.d-switch-simulator` 打开开关 → 点右侧时间框打开日历 → 设定时间 → 底部按钮变成「定时发布」，点击后跳到 `publish/success`。note-manager 里显示「审核中 / 定时发布 / 时间」才算排期成功。时间列是**虚拟滚动**：只渲染可见段、选中即时写入输入框、无确认按钮；`mouse.move` 到列中心 → `mouse.wheel` 滚到目标值进视口 → 重新 evaluate 拿该列 x 范围内的叶子节点坐标再点。禁用整页静态坐标——会把日历日期数字误点成时/分（日期 12 ≠ 小时 12）。弹层点空白处关闭。
- 网页草稿只存在 Ego Lite 本地，手机上看不到。发布失败会自动留一份草稿，收尾时去草稿箱删掉：草稿箱 → 图文笔记 tab → 该行「删除」 → 确认弹窗文案「草稿删除后不可找回」，点弹窗里的「删除」（取 y 更靠下的叶子节点）；每删一条重新按标题定位，行序会变。删重复草稿前先核对保存时间，别把要用的那条删了。
- 后台数据：note-manager 每条依次是 标题、时间、5 个没有标签的数字（观看/评论/点赞/收藏/分享）。新号的「笔记数据」和「账号概览」可能显示「暂未开通数据权限」，这时只能看列表数字和粉丝数据。

## 抖音（dy_publish.mjs）
- 上传页 `creator.douyin.com/creator-micro/content/upload?default-tab=3`。弹出「你还有上次未发布的图文」时点「放弃」。网页端只能暂存 1 条图文。
- 声明：选「内容为转载信息」→ 再选「取材站外」→ 确定。
- 自检项：描述里有「来源：」、没有 `*`、声明正确、「已添加N张图片」等于 jpg 数。不通过就不发。发布成功后跳到 content/manage。

## 公众号贴图
- `md2wechat create_image_post -t 标题 -c 正文 --images a.jpg,b.jpg,c.jpg --open-comment`，把 media_id 记进 receipts（`发布包-<批次>/wechat-receipts.tsv`，格式 post/media_id/created）。
- 命令输出里只有各图的 image media_id，**没有能直接 grep 到的草稿 media_id**；别为了拿 id 重跑一次（会多建一条草稿）。改从草稿列表按标题反查：token 从 `~/.config/md2wechat/config.yaml` 的 `wechat.appid/secret` 换 `cgi-bin/token` 拿，再 `draft/batchget`。**batchget 必须 POST**（GET 返回 `errcode 43002 require POST method`），body `{"offset":0,"count":6,"no_content":1}`，响应按 utf-8 解码，取 `item[].media_id` + `item[].content.news_item[0].title` 按标题匹配。
- 正文里要写清「5 张图依次对应」这类引导；贴图不支持话题，正文按小红书正文去掉话题行。改文案时先 draft/delete 旧草稿再新建。

## 删帖
在 note-manager 或 content/manage 按标题定位。确认框里的标题和目标一致才点确定。每删一条 reload 一次，不要复用旧坐标。删帖会丢掉已有数据，刚删就重发可能被判重复。
