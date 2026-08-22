# -*- coding: utf-8 -*-
"""三语语料索引构建器（v3）
用法：
  python integrate_corpus.py index-only          # 从 corpus/{zh,jp,en} 重建索引（常用）
  python integrate_corpus.py --sync-lang zh      # 从源目录同步指定语言后重建
  python integrate_corpus.py --sync-lang all     # 同步全部三种语言
"""
import os, re, json, shutil, sys

SKILL = r"C:\Users\1\.workbuddy\skills\mizuki-roleplay"
DST = os.path.join(SKILL, "references", "corpus")
SOURCES = {
    "zh": r"C:\Users\1\WorkBuddy\2026-08-18-21-08-00\Mizuki_Stories",
    "jp": r"C:\Users\1\WorkBuddy\2026-08-12-16-53-09\Mizuki_Stories_JP",
    "en": r"C:\Users\1\WorkBuddy\2026-08-12-16-53-09\Mizuki_Stories_EN",
}
MIZUKI_NAME = {"zh": "瑞希", "jp": "瑞希", "en": "Mizuki"}
SUB_DIRS = ("主线剧情", "活动剧情", "自我介绍", "区域对话")
SPEAKER_RE = re.compile(r"^【([^】]+)】")


def scan_file(path, mizuki):
    total = mizuki_count = 0
    speakers = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#") or s.startswith(">"):
                continue
            m = SPEAKER_RE.match(s)
            if m:
                total += 1
                name = m.group(1)
                speakers[name] = speakers.get(name, 0) + 1
                if name == mizuki:
                    mizuki_count += 1
            else:
                total += 1
    return total, mizuki_count, speakers


def collect_lang(lang):
    root = os.path.join(DST, lang)
    mizuki = MIZUKI_NAME[lang]
    entries = []
    main_dir = os.path.join(root, "主线剧情", "25时")
    if os.path.isdir(main_dir):
        for fn in sorted(os.listdir(main_dir)):
            p = os.path.join(main_dir, fn)
            t, mz, sp = scan_file(p, mizuki)
            m = re.match(r"第(\d+)话[_：](.+)\.md", fn)
            entries.append({
                "lang": lang, "type": "main", "id": f"main-{int(m.group(1)):02d}",
                "episode": int(m.group(1)), "title": m.group(2),
                "path": f"corpus/{lang}/主线剧情/25时/{fn}",
                "lines": t, "mizuki_lines": mz,
                "cast": sorted(sp.keys(), key=lambda k: -sp[k]),
            })
    ev_dir = os.path.join(root, "活动剧情")
    if os.path.isdir(ev_dir):
        for fn in sorted(os.listdir(ev_dir)):
            p = os.path.join(ev_dir, fn)
            t, mz, sp = scan_file(p, mizuki)
            m = re.match(r"(\d+)_(.+)\.md", fn)
            if not m:
                continue
            entries.append({
                "lang": lang, "type": "event", "id": f"ev-{int(m.group(1)):03d}",
                "episode": int(m.group(1)), "title": m.group(2),
                "path": f"corpus/{lang}/活动剧情/{fn}",
                "lines": t, "mizuki_lines": mz,
                "cast": sorted(sp.keys(), key=lambda k: -sp[k]),
            })
    si_dir = os.path.join(root, "自我介绍")
    if os.path.isdir(si_dir):
        for i, fn in enumerate(sorted(os.listdir(si_dir))):
            if not fn.endswith(".md"):
                continue
            p = os.path.join(si_dir, fn)
            t, mz, sp = scan_file(p, mizuki)
            entries.append({
                "lang": lang, "type": "intro", "id": f"intro-{i+1}",
                "title": fn[:-3], "path": f"corpus/{lang}/自我介绍/{fn}",
                "lines": t, "mizuki_lines": mz, "cast": sorted(sp.keys()),
            })
    ar_dir = os.path.join(root, "区域对话")
    if os.path.isdir(ar_dir):
        for fn in sorted(os.listdir(ar_dir)):
            if not fn.endswith(".md"):
                continue
            p = os.path.join(ar_dir, fn)
            t, mz, sp = scan_file(p, mizuki)
            sid = fn[:-3]
            entries.append({
                "lang": lang, "type": "area", "id": sid, "title": sid,
                "path": f"corpus/{lang}/区域对话/{fn}",
                "lines": t, "mizuki_lines": mz, "cast": sorted(sp.keys()),
            })
    return entries


def sync_lang(lang):
    src = SOURCES[lang]
    dst = os.path.join(DST, lang)
    if not os.path.isdir(src):
        print(f"[skip] 源目录不存在: {src}")
        return
    if os.path.exists(dst):
        os.rename(dst, dst + ".old")
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("README.md", "_download_failures.json"))
    print(f"[sync] {lang}: {sum(len(fs) for _,_,fs in os.walk(dst))} files")


def main():
    args = sys.argv[1:]
    if "--sync-lang" in args:
        lang = args[args.index("--sync-lang") + 1]
        langs = ("zh", "jp", "en") if lang == "all" else (lang,)
        for l in langs:
            sync_lang(l)
    all_entries = []
    for lang in ("zh", "jp", "en"):
        entries = collect_lang(lang)
        all_entries.extend(entries)
        stats = {}
        for e in entries:
            stats[e["type"]] = stats.get(e["type"], [0, 0])
            stats[e["type"]][0] += 1
            stats[e["type"]][1] += e["mizuki_lines"]
        print(f"[{lang}]", {k: tuple(v) for k, v in stats.items()})

    with open(os.path.join(SKILL, "references", "corpus_index.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(all_entries, f, ensure_ascii=False, indent=2)
    print("corpus_index.json:", len(all_entries), "entries")

    write_md(all_entries)
    print("corpus-index.md written")


def write_md(entries):
    # 按 (type, id, lang) 聚合：活动按 id 合并（jp/en 每话一文件），主线/自我介绍/区域对话 1:1
    by_id = {}
    for e in entries:
        key = (e["type"], e["id"], e["lang"])
        if key not in by_id:
            by_id[key] = dict(e)
            by_id[key]["_count"] = 1
        else:
            by_id[key]["lines"] += e["lines"]
            by_id[key]["mizuki_lines"] += e["mizuki_lines"]
            by_id[key]["_count"] += 1
    L = ("zh", "jp", "en")

    def get(lang, typ, tid):
        d = by_id.get((typ, tid, lang))
        if not d:
            return None
        o = dict(d)
        if o.get("_count", 1) > 1:
            o["title"] = f"{o['title']} ほか{o['_count']}話" if lang == "jp" else (f"{o['title']} +{o['_count']-1}eps" if lang == "en" else o["title"])
        return o

    def title(e):
        return e["title"] if e else "—"

    md = []
    md.append("# 剧情语料库目录（corpus index · 三语）")
    md.append("")
    md.append("> 来源：pjsk.moe 数据层（zh/jp/en 三服）。格式：`【角色名】台词`；括号内为内心独白；无标记行为旁白。")
    md.append("> ⚠️ 版权：角色与剧情归 SEGA / Colorful Palette，语料仅供学习研究，请勿商用；版权方要求时下架。")
    md.append("")
    md.append("## 使用协议（模型必读）")
    md.append("")
    md.append("1. **语言切换**：默认中文。用户要求用日语/英语交流时 → 改读 `corpus/jp/` 或 `corpus/en/` 对应文件校准口吻与称呼，并**用该语言扮演**；切回中文同理。语料路径 = `corpus/{zh|jp|en}/…`。")
    md.append("2. **先查索引，再读文件**：按 (type, id) 定位三个语言的文件路径，再 Read 对应单文件（500-1,600 行，禁止全量加载）。")
    md.append("3. **说话人变体**：`【瑞希】`（zh/jp）/`【Mizuki】`（en）是本人；`【小学生瑞希】`/`【Kid Mizuki】` 为幼年期；`【优希】`=姐姐、`【瑞希的母亲】`/`【Mizuki's Mother】` 等家人**不是**瑞希；`【A&B&瑞希】` 为多人合说。")
    md.append("4. **引用纪律**：生成新台词为主；直接引用单次 ≤2 句并注明出处（语言+期数）。不整段复述。")
    md.append("5. **时期判定**：145/150 期是瑞希心态分水岭（守密→坦白），回答前先核对所在时期。")
    md.append("6. **改名铁律**：说话人标签可改（用 `rename_speaker.py`，支持 --lang），对话正文与称呼一律不动。")
    md.append("")

    def table(header, ids):
        md.append(header)
        md.append("| ID | 中文标题 | 日本語タイトル | English Title | 行数 z/j/e | 瑞希台词 z/j/e |")
        md.append("|---|---|---|---|---|---|")
        for tid in ids:
            zh = get("zh", header_kind, tid)
            jp = get("jp", header_kind, tid)
            en = get("en", header_kind, tid)
            rows = " / ".join(str(x["lines"]) if x else "—" for x in (zh, jp, en))
            mzs = " / ".join(str(x["mizuki_lines"]) if x else "—" for x in (zh, jp, en))
            md.append(f"| {tid} | {title(zh)} | {title(jp)} | {title(en)} | {rows} | {mzs} |")
        md.append("")

    main_ids = sorted({k[1] for k in by_id if k[0] == "main"}, key=lambda x: int(x.split("-")[1]))
    ev_ids = sorted({k[1] for k in by_id if k[0] == "event"}, key=lambda x: int(x.split("-")[1]))
    intro_ids = sorted({k[1] for k in by_id if k[0] == "intro"})
    area_ids = sorted({k[1] for k in by_id if k[0] == "area"})

    header_kind = "main"
    table("## 主线剧情（25时）", main_ids)
    header_kind = "event"
    table("## 活动剧情（瑞希出场）", ev_ids)
    header_kind = "intro"
    table("## 自我介绍", intro_ids)

    md.append("## 区域对话（日常碎片，三语各 77 条）")
    md.append("")
    md.append("| ID | 中文 | 日本語 | English | 行数 z/j/e | 瑞希台词 z/j/e |")
    md.append("|---|---|---|---|---|---|")
    for sid in area_ids:
        zh = get("zh", "area", sid)
        jp = get("jp", "area", sid)
        en = get("en", "area", sid)
        rows = " / ".join(str(x["lines"]) if x else "—" for x in (zh, jp, en))
        mzs = " / ".join(str(x["mizuki_lines"]) if x else "—" for x in (zh, jp, en))
        md.append(f"| {sid} | — | — | — | {rows} | {mzs} |")
    md.append("")
    md.append("> 路径：`corpus/{zh,jp,en}/区域对话/{sid}.md`；完整字段（含 cast）见 `corpus_index.json`。")
    md.append("")
    with open(os.path.join(SKILL, "references", "corpus-index.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(md))


if __name__ == "__main__":
    main()
