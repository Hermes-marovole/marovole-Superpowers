# Superpowers / Hermes Skills Health Map

Generated: 2026-05-02
Repo: /Users/marovole/Workspace/HermesWork/marovole-Superpowers
Local skills: /Users/marovole/.hermes/skills

## Git status
```
## main...origin/main
d8b3d6b
```

## Summary
- Repository tracked skill files: 2
- Local active skill files: 175
- Local total skill files including .archive: 202
- Duplicate active skill names: 0 detected
- Repository/local same-name path mismatches: 2
- README skill links missing in repository checkout: 70

## Repository skills currently tracked
- dokobot: skills/dokobot/SKILL.md (frontmatter category: none, 137 lines)
- link2doc: skills/research/link2doc/SKILL.md (frontmatter category: research, 1527 lines)

## Local active skills by category
- (root): 2
- apple: 4
- autonomous-ai-agents: 9
- content-publishing: 1
- creative: 28
- data-science: 1
- devops: 9
- document-processing: 4
- email: 3
- external-tools: 3
- gaming: 2
- github: 6
- inference: 2
- leisure: 1
- mcp: 2
- media: 6
- mlops: 5
- mlops/cloud: 2
- mlops/evaluation: 5
- mlops/inference: 6
- mlops/models: 6
- mlops/research: 1
- mlops/training: 11
- mlops/vector-databases: 1
- note-taking: 2
- productivity: 4
- red-teaming: 1
- research: 15
- smart-home: 1
- social-media: 3
- software-development: 19
- task-management: 4
- web-automation: 2
- workspace-integration: 4

## Categories above 15 active skills
- creative: 28
- software-development: 19

## Repository vs local path mismatches
- dokobot: repo skills/dokobot/SKILL.md ; local external-tools/dokobot/SKILL.md
- link2doc: repo skills/research/link2doc/SKILL.md ; local productivity/link2doc/SKILL.md

## Active name/dir naming debt
- creative/creative-ideation/SKILL.md: name=ideation, dir=creative-ideation
- mlops/cloud/lambda-labs/SKILL.md: name=lambda-labs-gpu-cloud, dir=lambda-labs
- mlops/cloud/modal/SKILL.md: name=modal-serverless-gpu, dir=modal
- mlops/evaluation/lm-evaluation-harness/SKILL.md: name=evaluating-llms-harness, dir=lm-evaluation-harness
- mlops/evaluation/saelens/SKILL.md: name=sparse-autoencoder-training, dir=saelens
- mlops/inference/gguf/SKILL.md: name=gguf-quantization, dir=gguf
- mlops/inference/vllm/SKILL.md: name=serving-llms-vllm, dir=vllm
- mlops/models/audiocraft/SKILL.md: name=audiocraft-audio-generation, dir=audiocraft
- mlops/models/segment-anything/SKILL.md: name=segment-anything-model, dir=segment-anything
- mlops/models/stable-diffusion/SKILL.md: name=stable-diffusion-image-generation, dir=stable-diffusion
- mlops/training/accelerate/SKILL.md: name=huggingface-accelerate, dir=accelerate
- mlops/training/flash-attention/SKILL.md: name=optimizing-attention-flash, dir=flash-attention
- mlops/training/peft/SKILL.md: name=peft-fine-tuning, dir=peft
- mlops/training/simpo/SKILL.md: name=simpo-training, dir=simpo
- mlops/training/slime/SKILL.md: name=slime-rl-training, dir=slime
- mlops/training/torchtitan/SKILL.md: name=distributed-llm-pretraining-torchtitan, dir=torchtitan
- mlops/training/trl-fine-tuning/SKILL.md: name=fine-tuning-with-trl, dir=trl-fine-tuning
- mlops/vector-databases/qdrant/SKILL.md: name=qdrant-vector-search, dir=qdrant

## Health conclusions
- The local Hermes skills store is the real 175-active-skill system; the Superpowers repository currently tracks only 2 SKILL.md files under skills/.
- README.md describes a full 120+ skill tree, but most referenced skill directories are not present in this repository checkout, so README is aspirational/stale relative to Git contents.
- No duplicate active skill names were detected in ~/.hermes/skills.
- The largest local categories are creative (28) and software-development (19); both exceed the >15 overcrowding threshold and are candidates for a later Phase 3 refactor.
- link2doc and dokobot exist in both repo and local, but repo paths/categories are stale versus local post-refactor placement.

## Recommended next actions
1. Decide repository policy: mirror all active ~/.hermes/skills into Superpowers, or keep Superpowers mostly as docs plus selected promoted skills.
2. If mirroring, copy/sync active skill directories from ~/.hermes/skills to repo/skills preserving category paths, then update README links to skills/<category>/<skill>.
3. If not mirroring, rewrite README to say the complete live skill registry is ~/.hermes/skills and only promoted examples live in repo/skills.
4. Fix immediate stale repo skills: move skills/dokobot -> skills/external-tools/dokobot and skills/research/link2doc -> skills/productivity/link2doc, or replace them with symlink-free synced copies from local.
5. Consider Phase 3: split creative and software-development categories.
