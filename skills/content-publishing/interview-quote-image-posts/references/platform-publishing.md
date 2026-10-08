# 文案格式与各平台发布

## 文案（发布包目录内 txt，首行 `标题：`，`正文：` 后逐行，话题单独一行）
| 平台 | 标题 | 正文 | 话题 |
|---|---|---|---|
| 小红书 | ≤20 字 | 一句引入 + ①②③ 依次对应三张图 + 「三张图依次对应，滑动看原话～」 + 出处行；另加 `媒体：<频道>` 行（只供脚本用，不进正文） | 5–8 个 |
| 抖音图文 | ≤20 字 | 2–3 句 + 出处行 | 3–5 个 |
| 公众号贴图 | 同小红书 | 小红书正文去掉话题 | 无 |

## 小红书（xhs_fill.mjs）
- 上传页 `creator.xiaohongshu.com/publish/publish?source=official&from=tab_switch&target=image`，上传后关掉「我知道了」弹窗。
- 正文编辑器是 `div.tiptap.ProseMirror`。用 evaluate 调 `.focus()` 聚焦，直接点击会被浮层拦住。正文必须逐行 insertText 再按 Enter，一次插多行顺序会乱。每篇都重新打开上传页，在旧内容上重填会混进旧稿。
- 话题：输入 `#xx` 后等下拉出现，点 `div.item` 里首行文字完全一致的那一项，正文里出现 `#xx[话题]#` 才算选中。不要直接按 Enter，会选中推广话题。
- 声明：先把「添加内容类型声明」scrollIntoView，然后 hover「内容来源声明」→ 点「来源转载」→ 填媒体名称 → 确认。成功后 URL 包含 `publish/success`。
- 定时发布：在发布页的「定时发布」开关里设时间，属于发布动作，需要用户授权。
- 网页草稿只存在 Ego Lite 本地，手机上看不到。发布失败会自动留一份草稿，收尾时去草稿箱删掉。
- 后台数据：note-manager 每条依次是 标题、时间、5 个没有标签的数字（观看/评论/点赞/收藏/分享）。新号的「笔记数据」和「账号概览」可能显示「暂未开通数据权限」，这时只能看列表数字和粉丝数据。

## 抖音（dy_publish.mjs）
- 上传页 `creator.douyin.com/creator-micro/content/upload?default-tab=3`。弹出「你还有上次未发布的图文」时点「放弃」。网页端只能暂存 1 条图文。
- 声明：选「内容为转载信息」→ 再选「取材站外」→ 确定。
- 自检项：描述里有「来源：」、没有 `*`、声明正确、「已添加N张图片」等于 jpg 数。不通过就不发。发布成功后跳到 content/manage。

## 公众号贴图
- `md2wechat create_image_post -t 标题 -c 正文 --images a.jpg,b.jpg,c.jpg --open-comment`，把 media_id 记进 receipts。
- 核对用 stable_token + draft/batchget，经 127.0.0.1:6152 代理，响应按 utf-8 解码。改文案时先 delete 旧草稿再新建。

## 删帖
在 note-manager 或 content/manage 按标题定位。确认框里的标题和目标一致才点确定。每删一条 reload 一次，不要复用旧坐标。删帖会丢掉已有数据，刚删就重发可能被判重复。
