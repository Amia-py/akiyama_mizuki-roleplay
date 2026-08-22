# mizuki-roleplay

> An Agent Skill for roleplaying **Akiyama Mizuki** (暁山瑞希 / Amia), the MV artist of *25-ji, Nightcord de.* from *Project SEKAI: Colorful Stage! feat. Hatsune Miku*.
>
> **Languages / 语言 / 言語:** English (current) · [日本語](README.ja.md) · [简体中文](README.md)

A standard `SKILL.md` (YAML frontmatter + Markdown body) bundled with a character profile, a story archive, structured data, and a **complete dialogue corpus (Chinese)**. She speaks in first person 「僕」, ends sentences with 「♪」, and teases Enanan as a "textbook tsundere" — every detail is documented.

## ✨ Features

- **Character profile**: personality, speech rules, address-name table, roleplay boundaries (tri-lingual `character.*.md`)
- **Story archive**: main story + 3 arcs summarized from Mizuki's perspective (18 key beats)
- **Full story corpus (Chinese)**: 156 files / 65,606 lines / 5,623 Mizuki lines, with index and usage protocol
- **Structured data**: `sekai25.json` (story events / characters / speech samples)
- **Progressive disclosure**: core rules in SKILL.md, support docs in `references/`, loaded on demand
- **Cross-platform**: follows the open Agent Skill standard; one package, many agents
- **Tooling**: `build_data.py` (validation), `integrate_corpus.py` (corpus integration), `rename_speaker.py` (safe speaker-label renaming)

## 📦 Layout

```
mizuki-roleplay/
├── SKILL.md
├── install.sh                # Linux / macOS / WSL / Git Bash one-shot installer
├── install.ps1               # Windows PowerShell installer
├── LICENSE                   # AGPL-3.0
└── mizuki-roleplay/
    ├── SKILL.md
    └── references/
        ├── character.md      # profile (+ character.en.md / character.ja.md)
        ├── story-archive.md  # story archive
        ├── sekai25.json      # structured data
        ├── corpus-index.md   # corpus index & usage protocol
        ├── corpus/           # full dialogue corpus (Chinese, 156 files)
        ├── corpus_index.json # machine-readable corpus index
        ├── build_data.py / integrate_corpus.py / rename_speaker.py
```

## 🚀 Install

### One-shot

```bash
# Linux / macOS / WSL / Git Bash
bash install.sh

# Windows PowerShell
powershell -ExecutionPolicy Bypass -File install.ps1
```

### Agent × OS matrix

| Agent | Global dir | Project dir |
|---|---|---|
| **Claude Code** | `~/.claude/skills/` | `<project>/.claude/skills/` |
| **Codex CLI** | `~/.codex/skills/` (some builds: `~/.agents/skills/`; install to both) | `<project>/.agents/skills/` |
| **OpenClaw** | `~/.openclaw/skills/` | `<workspace>/skills/` |
| **WorkBuddy / CodeBuddy** | `~/.workbuddy/skills/` | `<project>/.workbuddy/skills/` |
| **Reasonix** | `~/.reasonix/skills/` (also reads `~/.agents/skills/`) | `<project>/.reasonix/skills/` |
| **OpenCode** | `~/.config/opencode/skills/` | `<project>/.opencode/skills/` |
| **Hermes Agent** | follow its docs (source-browsing type: point at the `mizuki-roleplay/` dir) | `skills/` |
| **DevEco Code** | follow Huawei official docs (AI skill/MCP mechanism) | — |

> The target must be `<skills-dir>/mizuki-roleplay/SKILL.md` — do **not** nest an extra directory.

## 💬 Usage

- "Play as Akiyama Mizuki" / "Mizuki" / "Amia" / "mzk" → roleplay
- "What happens in the 25-ji main story?" → story Q&A
- "What does Mizuki call Ena?" → lore lookup
- "Original lines from event 150" → corpus retrieval (see `corpus-index.md`)

## ⚖️ Copyright notice

1. **Character & story rights**: Akiyama Mizuki and *Project SEKAI* belong to **SEGA / Colorful Palette**.
2. **Corpus**: `corpus/` contains Chinese translated story dialogue (sourced from the pjsk.moe community translation). Distributing it with this repo is the user's decision; it is for study only — **no commercial use**; remove on rights-holder request.
3. **License**: code and written material in this repo are **AGPL-3.0**.

## 📄 License

[GNU Affero General Public License v3.0](LICENSE)

---

It's 1 AM, and the Nightcord chime rings on time — this time, Mizuki is on the other end. ♪
