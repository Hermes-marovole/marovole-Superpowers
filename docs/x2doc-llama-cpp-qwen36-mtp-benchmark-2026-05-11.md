# llama.cpp + Qwen3.6-35B-A3B-MTP 消费级显卡 MTP 评测 — X2Doc 整理

> 来源：https://x.com/itsmeajaykv/status/2053562304902672530?s=46
> 作者：@ItsmeAjayKV
> 整理时间：2026-05-11
> 来自翡冷翠

---

## TL;DR

- 在 **12GB RTX 3060** 上实测 **Qwen3.6-35B-A3B-MTP** (Q6_K_XL) 的 MTP 加速表现
- 无 MTP 约 **21 t/s**，开启 MTP 后达到 **30–35 t/s**，提升约 **50–67%**
- 关键发现：ngl/ncmoe 的 VRAM 权衡 和 --spec-draft-n-max 存在甜蜜点（2–4），盲目加深 speculation 反而降速
- 作者正在跟进 **context size 增长对 MTP 行为的影响** —— verifier cost 与 throughput 的交互比预期更复杂

---

## 原帖核心内容

AJ 系统测试了 llama.cpp 上 Qwen3.6-35B-A3B-MTP 的 MTP (Multi-Token Prediction) 参数组合：

**测试变量：**
- `ngl` (GPU 层数)
- `ncmoe` (MoE expert 数量)
- `--spec-draft-n-max` (speculative decoding 最大深度)

**规律总结：**
1. **ngl** — 增加 GPU 层数提升 tg，直到 VRAM 压力成为瓶颈
2. **ncmoe** — 降低值让更多 expert 常驻 GPU，tg 提升，但 VRAM 占用快速攀升
3. **--spec-draft-n-max** — 更深的 speculation ≠ 更快。存在明显边际递减，甚至反噬

**最优配置（平衡型）：**
- `ngl 6 -ncmoe 28 --spec-draft-n-max 3`

**最高 tg 配置：**
- `ngl 6 -ncmoe 24 --spec-draft-n-max 2`

**作者结论：** `--spec-draft-n-max 2~4` 是该 12GB 消费卡的最强操作区间。

**后续方向：** 测试 MTP 在长上下文增长时的行为变化。context size、verifier cost 和 throughput 的三方交互比预期更值得关注。

---

## 关键信息与资源

| Type | Name | Link | Why it matters |
|---|---|---|---|
| Model | Qwen3.6-35B-A3B-MTP GGUF (havenoammo) | https://huggingface.co/havenoammo/Qwen3.6-35B-A3B-MTP-GGUF | MTP 量化模型下载，社区早期上传 |
| PR | llama.cpp MTP implementation | https://github.com/ggml-org/llama.cpp/pull/XXX | 官方 MTP PR 进度（ggml-org/llama.cpp） |
| Model | Qwopus3.6-35B-A3B-v1-APEX-GGUF (mudler) | https://huggingface.co/mudler/Qwopus3.6-35B-A3B-v1-APEX-GGUF | 同日发布的 APEX Quant 版本，可对比质量 |
| Related | DGX Spark Qwen3.6 300% 加速 (@SpaceTimeViking) | https://x.com/SpaceTimeViking/status/2053427507601269153 | 同一模型在 DGX Spark 上的另一组高性能调参 |
| Related | MTPLX for Mac MLX (@AlexJonesax) | https://x.com/AlexJonesax/status/2053468341122007422 | Mac 上的 MTPLX 推断服务器，无需 draft model |

---

## 我的吸收判断

- **可复用能力：** 消费级 VRAM (8–16GB) 的 MTP 参数调优方法论 —— ngl/ncmoe/n-max 的三方权衡框架可直接复用到 M2 Max 本地推理
- **值得沉淀到 skill / workflow 吗：** 是。可扩展为「本地 LLM 推理参数调优速查」skill，覆盖 llama.cpp + MLX 双栈
- **对 AI × Product × Biohacking / Super Individual 的价值：** 高。Neumina Agent 的后端推理栈如果引入 MTP，可显著降低 35B+ 模型的响应延迟，直接影响用户体验。M2 Max 64GB 的条件比 12GB RTX 3060 宽松得多，参数空间更大
- **风险或待验证点：**
  - 回复中 @SheppaDean 指出 synthetic benchmark 可能掩盖实际输出质量下降，需关注 MTP 对代码/医学推理任务的真实影响
  - 作者提到 Qwen3.6 早期需要 Q4 + 4-bit KV cache 才能跑通，现在 MTP + Q6 + 8-bit KV cache 即可流畅 —— 但质量对比需 A/B 测试
  - llama.cpp MTP PR 尚未 merge，稳定性待观察

---

## 可执行下一步

- [ ] 在 M2 Max 64GB 上复现同一组参数测试（llama.cpp + MLX 双栈），建立 Apple Silicon 版本的 sweet spot 表
- [ ] 对比 MTP 开启/关闭在 Neumina Agent 实际任务（医学问答、症状推理）上的质量差异，不只是 t/s
- [ ] 追踪 llama.cpp MTP PR merge 进度，评估生产环境接入时机
- [ ] 测试 context 128k+ 长场景下 MTP 的 KV cache 驻留策略，验证作者提到的 "more interesting than expected" 交互

---

*来自翡冷翠*
