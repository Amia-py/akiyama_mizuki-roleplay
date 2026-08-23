# mizuki-roleplay

> プロジェクトセカイ『25時、ナイトコードで。』のMV担当・**暁山瑞希**（Akiyama Mizuki / Amia）を演じるための Agent Skill。
>
> **言語 / Languages / 语言:** 日本語（現在）· [English](README.en.md) · [简体中文](README.md)

標準の `SKILL.md`（YAML frontmatter + Markdown 本文）に、キャラクター設定、ストーリー資料、構造化データ、そして**フルの台詞コーパス（中国語）**を同梱。自称「僕」、語尾の「♪」、絵名を「古き良きツンデレ」と揶揄する口調まで、すべて資料付き。

## ✨ 特徴

- **キャラクター設定**：性格の二層構造、話し方ルール、呼称表、演じ分けの境界（三言語 `character.*.md`）
- **ストーリー資料**：メインストーリー＋三章構成の概要（瑞希視点、重要イベント18件）
- **フルの台詞コーパス（中国語）**：156ファイル / 65,606行 / 瑞希の台詞5,623件、索引・利用プロトコル付き
- **構造化データ**：`sekai25.json`（イベント / 人物関係 / 台詞サンプル）
- **段階的ロード**：コア規則は SKILL.md、補助資料は `references/` に置き必要時のみ読込
- **クロスプラットフォーム**：Agent Skill のオープン標準に準拠、一つのパッケージで多数のエージェントに対応
- **ツール群**：`build_data.py`（検証）、`integrate_corpus.py`（コーパス統合）、`rename_speaker.py`（話者タグの安全な改名）

## 📦 構成

```
akiyama_mizuki-roleplay/
├── SKILL.md
├── install.sh                # Linux / macOS / WSL / Git Bash 一括インストーラ
├── install.ps1               # Windows PowerShell 用
├── LICENSE                   # AGPL-3.0
└── akiyama_mizuki-roleplay/
    ├── SKILL.md
    └── references/
        ├── character.md      # 設定（character.en.md / character.ja.md あり）
        ├── story-archive.md  # ストーリー資料
        ├── sekai25.json      # 構造化データ
        ├── corpus-index.md   # コーパス索引・利用プロトコル
        ├── corpus/           # 台詞コーパス（中国語・156ファイル）
        ├── corpus_index.json # 機械可読な索引
        ├── build_data.py / integrate_corpus.py / rename_speaker.py
```

## 🚀 インストール

```bash
# Linux / macOS / WSL / Git Bash
bash install.sh

# Windows PowerShell
powershell -ExecutionPolicy Bypass -File install.ps1
```

### Agent × OS マトリクス

| Agent | グローバル | プロジェクト |
|---|---|---|
| **Claude Code** | `~/.claude/skills/` | `<project>/.claude/skills/` |
| **Codex CLI** | `~/.codex/skills/`（一部は `~/.agents/skills/`。両方に置くのが確実） | `<project>/.agents/skills/` |
| **OpenClaw** | `~/.openclaw/skills/` | `<workspace>/skills/` |
| **WorkBuddy / CodeBuddy** | `~/.workbuddy/skills/` | `<project>/.workbuddy/skills/` |
| **Reasonix** | `~/.reasonix/skills/`（`~/.agents/skills/` も読む） | `<project>/.reasonix/skills/` |
| **OpenCode** | `~/.config/opencode/skills/` | `<project>/.opencode/skills/` |
| **Hermes Agent** | 公式ドキュメントに従う（ソース閲覧型：`akiyama_mizuki-roleplay/` を技能パスに指定） | `skills/` |
| **DevEco Code** | 华为公式ドキュメントに従う（AI技能/MCP機構） | — |

> 配置先は必ず `<skills-dir>/akiyama_mizuki-roleplay/SKILL.md`。フォルダを二重にしないこと。

## 💬 使い方

- 「暁山瑞希のロールプレイ」/「瑞希」/「Amia」/「mzk」→ ロールプレイ開始
- 「25時のメインストーリーは？」→ ストーリーQ&A
- 「瑞希は絵名を何と呼ぶ？」→ 人間関係の考据
- 「第150期の原台詞」→ コーパス検索（`corpus-index.md` の手順に従う）

## ⚖️ 著作権について

1. **キャラクター・ストーリーの権利**：暁山瑞希およびプロジェクトセカイは **SEGA / Colorful Palette** に帰属します。
2. **コーパス**：`corpus/` は中国語訳の台詞テキスト（pjsk.moe コミュニティ翻訳由来）。同梱はユーザーの判断によるもので、学習研究目的に限ります。**商用利用禁止**。権利者から求められた場合は削除してください。
3. **ライセンス**：本リポジトリのコード・資料は **AGPL-3.0** で公開。

## 📄 ライセンス

[GNU Affero General Public License v3.0](LICENSE)

---

深夜1時、ナイトコードの着信音が定刻に鳴る——今回は、相手は瑞希だ。♪
