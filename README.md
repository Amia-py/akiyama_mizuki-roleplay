# mizuki-roleplay

> 扮演《世界计划 缤纷舞台！ feat. 初音未来》中 25点，Nightcord见。的 MV 师——**晓山瑞希**（暁山瑞希 / Akiyama Mizuki / Amia）的角色扮演 Agent Skill。
>
> **Languages / 语言 / 言語：** [English](README.en.md) · [日本語](README.ja.md) · 简体中文（当前）

一份标准的 `SKILL.md`（YAML frontmatter + Markdown 正文），附带人设档案、剧情档案馆、结构化资料库与**完整台词语料库（中文）**。角色扮演时自称「僕」、句尾带「♪」、调侃绘名是"教科书般的傲娇"——全部有档可查。

## ✨ 特性

- **角色档案**：人设、性格双层结构、说话规则、称呼表、扮演边界（中/英/日三语 `character.*.md`）
- **剧情档案馆**：主线 + 三篇章梗概（瑞希视角，18 个关键节点）
- **完整剧情语料（中文）**：156 文件 / 65,606 行 / 瑞希台词 5,623 句，含索引与使用协议
- **结构化数据**：`sekai25.json`（剧情事件 / 人物关系 / 台词风格示例）
- **渐进式加载**：核心规则在 SKILL.md，辅助资料在 `references/`，按需读取不爆上下文
- **跨平台**：遵循 Agent Skill 开放标准，一套文件适配多端
- **维护工具**：`build_data.py`（校验）、`integrate_corpus.py`（语料整合）、`rename_speaker.py`（说话人标签安全改名）

## 📦 目录结构

```
mizuki-roleplay/
├── SKILL.md                      # 技能主文件
├── install.sh                    # Linux/macOS/WSL/GitBash 一键安装
├── install.ps1                   # Windows PowerShell 一键安装
├── LICENSE                       # AGPL-3.0
└── mizuki-roleplay/
    ├── SKILL.md
    └── references/
        ├── character.md          # 人设档案（+ character.en.md / character.ja.md）
        ├── story-archive.md      # 剧情档案馆
        ├── sekai25.json          # 结构化数据
        ├── corpus-index.md       # 语料索引与使用协议
        ├── corpus/               # 完整台词语料（中文，156 文件）
        ├── corpus_index.json     # 语料机器索引
        ├── build_data.py / integrate_corpus.py / rename_speaker.py
```

## 🚀 安装

### 一键安装

```bash
# Linux / macOS / WSL / Git Bash
bash install.sh

# Windows PowerShell
powershell -ExecutionPolicy Bypass -File install.ps1
```

### 按 Agent × OS 安装矩阵

| Agent | 全局目录 | 项目级目录 |
|---|---|---|
| **Claude Code** | `~/.claude/skills/` | `<项目>/.claude/skills/` |
| **Codex CLI** | `~/.codex/skills/`（部分版本 `~/.agents/skills/`，两处都放最稳） | `<项目>/.agents/skills/` |
| **OpenClaw** | `~/.openclaw/skills/` | `<工作区>/skills/` |
| **WorkBuddy / CodeBuddy** | `~/.workbuddy/skills/` | `<项目>/.workbuddy/skills/` |
| **Reasonix** | `~/.reasonix/skills/`（兼读 `~/.agents/skills/`） | `<项目>/.reasonix/skills/` |
| **OpenCode** | `~/.config/opencode/skills/` | `<项目>/.opencode/skills/` |
| **Hermes Agent** | 按官方文档（源码浏览型，把 `mizuki-roleplay/` 目录加入技能路径） | `skills/` |
| **DevEco Code** | 以官方文档为准（AI 技能/MCP 机制） | — |

> 注意：目标路径必须是 `<skills目录>/mizuki-roleplay/SKILL.md`，**不要多套一层目录**。

## 💬 使用

- "扮演晓山瑞希" / "瑞希" / "Amia" / "mzk" → 触发角色扮演
- "25时的主线剧情讲了什么？" → 剧情问答
- "瑞希管绘名叫什么？" → 人物关系考据
- "第150期的原味台词" → 语料检索（按 `corpus-index.md` 协议）

## ⚖️ 版权声明（重要）

1. **角色与剧情版权**：晓山瑞希及《世界计划 缤纷舞台！》版权归 **SEGA / Colorful Palette** 所有。
2. **语料**：`corpus/` 为剧情中文台词语料（源自 pjsk.moe 国服汉化），随仓库分发为用户自主决定，仅供学习研究，**请勿商用**；版权方要求时应予下架。
3. **许可**：本仓库代码与档案整理以 **AGPL-3.0** 开源。

## 📄 许可

[GNU Affero General Public License v3.0](LICENSE)

---

深夜 1 点，Nightcord 的提示音准时响起——这一次，对面是瑞希。♪
