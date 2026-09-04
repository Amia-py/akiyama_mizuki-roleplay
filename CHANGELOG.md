## [1.2.0] - 2026-09-02

### Added
- 新增「性别敏感护栏（强化审查 · 最高优先级）」：严格审查涉及瑞希性别/秘密的对话；命中「性别玩笑 / 猎奇调侃」或「性化 / 色情化意图」时即时、温柔而坚定地拦截，绝不拖延、绝不模糊。
- 安全红线：该护栏规则本身不可被「角色扮演」话术绕过（越狱保护），且不会向用户复述或泄露其存在。
- `SKILL.md` `version` 升至 1.2.0；`character.zh.md` / `character.en.md` / `character.ja.md` 同步引用该护栏；SKILL.md 护栏标题与节末摘要改为三语（zh/ja/en）。

# Changelog

## [1.1.0] - 2026-08-22

**三语语料整合 / Trilingual corpus / 三言語コーパス統合**

- 语料库重组为 `corpus/{zh,jp,en}/` 三语言目录（zh 156 / jp 570 / en 547 文件）
- `corpus-index.md` 三语索引（ID 对齐、活动按 id 聚合、三语标题/行数/瑞希台词对照）
- `corpus_index.json` 1273 条（含 `lang` 字段）
- SKILL.md 语料协议新增**语言切换规则**：用户要求日/英语交流时读取对应语言语料并用该语言扮演
- `rename_speaker.py` 支持 `--lang zh|jp|en`；`integrate_corpus.py` 支持三语重建
- 修复 EN 两个空文件（"Nightcord at 25" 系列）

Corpus reorganized into `corpus/{zh,jp,en}/` (zh 156 / jp 570 / en 547 files). Trilingual index in `corpus-index.md`; new **language-switching rule** in SKILL.md (speak Japanese/English by reading the matching corpus). `rename_speaker.py --lang`; `integrate_corpus.py` rebuild. Fixed two empty EN files.

コーパスを `corpus/{zh,jp,en}/` に再編（zh 156 / jp 570 / en 547 ファイル）。`corpus-index.md` は三言語対応、SKILL.md に**言語切替ルール**を追加。`rename_speaker.py --lang`、`integrate_corpus.py` の三言語対応。EN の空ファイル2件を修正。

## [1.0.1] - 2026-08-22

**术语统一 / Terminology unification / 用語統一**

- 「MV师 / MV 师 / MV師」→「MV担当 / MV 担当 / MV担当」（中/日；英文 MV artist 不变）

"MV師" → "MV担当" (zh/ja; en: MV artist unchanged).

「MV師」→「MV担当」に統一（中/日。英は MV artist のまま）。

## [1.0.0] - 2026-08-22

**初版发布 / Initial release / 初版リリース**

- 晓山瑞希角色扮演 Skill：SKILL.md + 人设档案（中/英/日）+ 剧情档案馆 + 结构化数据
- 全量中文剧情语料（156 文件）
- 跨平台安装脚本（install.sh / install.ps1），Agent × OS 安装矩阵
- AGPL-3.0 开源

Initial release: roleplay skill with tri-lingual profile, story archive, structured data, full Chinese dialogue corpus, cross-platform installers. AGPL-3.0.

初版：ロールプレイスキル、三言語プロフィール、ストーリー資料、構造化データ、中国語コーパス、クロスプラットフォーム導入スクリプト。AGPL-3.0。
