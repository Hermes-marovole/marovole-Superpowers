# Prompt Index 构建与使用说明

## 目录结构

```
docs/.prompt-index/       ← 构建后的索引文件（JSON），供 skill 意图路由查询
  ├── prompt-index.json   ← 主索引（126个prompt的分类 + 设计模式）

scripts/
  ├── build-prompt-index.py  ← 从 awesome-gpt-image-2 fork 构建索引

~/.hermes/skills/creative/
  ├── gpt-image-2-prompts/   ← 可执行模板库（9个模板 + 意图路由）
  ├── gpt-image-2-workflow/  ← 出图工作流（生图脚本、分辨率等）
```

## 工作流

1. `awesome-gpt-image-2` fork 放在 `/Users/marovole/Workspace/awesome-gpt-image-2/`
2. 运行 `python3 scripts/build-prompt-index.py`，从 fork 的 README 解析出分类体系和 Prompt 模式
3. 输出 `docs/.prompt-index/prompt-index.json`，被 skill 的意图路由层读取
4. 用户生图需求 → skill 意图路由（模板匹配或索引查询）→ 输出优化后的 Prompt

## 定期更新

当 fork 有上游更新时（GitHub Actions 自动更新 README）：
```bash
cd /Users/marovole/Workspace/awesome-gpt-image-2
git fetch upstream
git merge upstream/main
cd /Users/marovole/Workspace/Neuma-Superpower
python3 scripts/build-prompt-index.py
# 检查是否有新分类/模式需要吸收
git add docs/.prompt-index/ scripts/build-prompt-index.py
git commit -m "chore: sync prompt index from upstream"
```
