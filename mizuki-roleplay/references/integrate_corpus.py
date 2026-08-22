# -*- coding: utf-8 -*-
"""把 Mizuki_Stories 语料整合进 mizuki-roleplay Skill：
1. 拷贝语料到 references/corpus/
2. 生成 corpus_index.json（机器可查索引）
3. 生成 corpus-index.md（模型可读目录 + 使用协议）
"""
import os, re, json, shutil, sys

SRC = r"C:\Users\1\WorkBuddy\2026-08-18-21-08-00\Mizuki_Stories"
SKILL = r"C:\Users\1\.workbuddy\skills\mizuki-roleplay"
DST = os.path.join(SKILL, "references", "corpus")

INDEX_ONLY = "index-only" in sys.argv

# ---------- 1. 拷贝（index-only 模式跳过，用于语料已改名后重建索引） ----------
if not INDEX_ONLY:
    if os.path.exists(DST):
        shutil.rmtree(DST)
    shutil.copytree(SRC, DST, ignore=shutil.ignore_patterns("_download_failures.json"))
    print("copied ->", DST)

SPEAKER_RE = re.compile(r"^【([^】]+)】")

def scan_file(path):
    """统计单文件：总行数、瑞希行数、出场角色"""
    total = mizuki = 0
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
                if name == "瑞希":
                    mizuki += 1
            else:
                total += 1  # 旁白/心理
    return total, mizuki, speakers

def build_index():
    entries = []
    # 主线
    main_dir = os.path.join(DST, "主线剧情", "25时")
    for fn in sorted(os.listdir(main_dir)):
        p = os.path.join(main_dir, fn)
        t, mz, sp = scan_file(p)
        m = re.match(r"第(\d+)话[_：](.*)\.md", fn)
        entries.append({
            "type": "main", "id": f"main-{int(m.group(1)):02d}",
            "episode": int(m.group(1)), "title": m.group(2),
            "path": f"corpus/主线剧情/25时/{fn}",
            "lines": t, "mizuki_lines": mz,
            "cast": sorted(sp.keys(), key=lambda k: -sp[k]),
        })
    # 活动剧情
    ev_dir = os.path.join(DST, "活动剧情")
    for fn in sorted(os.listdir(ev_dir)):
        p = os.path.join(ev_dir, fn)
        t, mz, sp = scan_file(p)
        m = re.match(r"(\d+)_(.+)\.md", fn)
        entries.append({
            "type": "event", "id": f"ev-{int(m.group(1)):03d}",
            "episode": int(m.group(1)), "title": m.group(2),
            "path": f"corpus/活动剧情/{fn}",
            "lines": t, "mizuki_lines": mz,
            "cast": sorted(sp.keys(), key=lambda k: -sp[k]),
        })
    # 自我介绍
    si_dir = os.path.join(DST, "自我介绍")
    for fn in sorted(os.listdir(si_dir)):
        p = os.path.join(si_dir, fn)
        t, mz, sp = scan_file(p)
        entries.append({
            "type": "intro", "id": "intro-" + str(len([e for e in entries if e["type"]=="intro"]) + 1),
            "title": fn[:-3], "path": f"corpus/自我介绍/{fn}",
            "lines": t, "mizuki_lines": mz, "cast": sorted(sp.keys()),
        })
    # 区域对话
    ar_dir = os.path.join(DST, "区域对话")
    for fn in sorted(os.listdir(ar_dir)):
        p = os.path.join(ar_dir, fn)
        t, mz, sp = scan_file(p)
        entries.append({
            "type": "area", "id": fn[:-3], "title": fn[:-3],
            "path": f"corpus/区域对话/{fn}",
            "lines": t, "mizuki_lines": mz, "cast": sorted(sp.keys()),
        })
    return entries

entries = build_index()

# 保存 JSON 索引
with open(os.path.join(SKILL, "references", "corpus_index.json"), "w", encoding="utf-8", newline="\n") as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

stats = {}
for e in entries:
    stats[e["type"]] = stats.get(e["type"], [0, 0])
    stats[e["type"]][0] += 1
    stats[e["type"]][1] += e["mizuki_lines"]
print("index:", {k: tuple(v) for k, v in stats.items()})

# 生成 markdown 目录
def row(e):
    ep = e.get("episode", "")
    return f'| {e["id"]} | {("第"+str(ep)+"话") if e["type"]=="main" else ("第"+str(ep)+"期" if e["type"]=="event" else "—")} | {e["title"]} | {e["lines"]} | {e["mizuki_lines"]} | `{e["path"]}` |'

md = []
md.append("# 剧情语料库目录（corpus index）\n")
md.append("> 来源：pjsk.moe 国服汉化文本，用户自行抓取，仅供本地角色扮演参考。")
md.append("> 格式：`【角色名】台词`；括号内为内心独白；无标记行为旁白。\n")
md.append("## 使用协议（模型必读）\n")
md.append("1. **先查索引，再读文件**：根据用户话题在本目录定位活动/话数，再 Read 对应文件。单文件 500-1600 句，禁止一次读入全部。")
md.append("2. **瑞希台词检索**：需要台词风格参考时，对目标文件按 `【瑞希】` 前缀定位（Grep 或顺序浏览）。")
md.append("3. **引用纪律**：扮演时以语料为风格锚点生成新台词；直接引用单次不超过 2 句，并注明出处话数/期数。不整段复述原文。")
md.append("4. **时期判定**：第145/150期之前瑞希守密，之后已坦白。回答剧情问题先核对所在篇章。\n")
md.append("5. **说话人标记变体**：本目录\"瑞希台词\"列只统计 `【瑞希】`。检索时另需注意：\n")
md.append("   - `【小学生瑞希】`（79 句）：幼年期瑞希，语气更生硬孤僻\n")
md.append("   - `【瑞希的声音】`/`【瑞希的消息】`/`【瑞希の声】`：也是瑞希本人\n")
md.append("   - `【优希】`（278 句）= 晓山优希，瑞希的姐姐；`【优希的母亲】`（16 句）= 瑞希的母亲；`【优希的声音】`/`【优希母亲的声音】` 同理。**都不是瑞希**\n")
md.append("   - `【A&B&瑞希】` 形式：多人合说行，含瑞希但非独白\n")
md.append("   - 台词正文里的\"瑞希的姐姐\"字眼是角色间正常称谓（如优希自我介绍），保留原样\n")
md.append("## 主线剧情（25时，21话）\n")
md.append("| ID | 话数 | 标题 | 总行数 | 瑞希台词 | 文件 |")
md.append("|---|---|---|---|---|---|")
md += [row(e) for e in entries if e["type"] == "main"]
md.append("\n## 活动剧情（瑞希出场，56个）\n")
md.append("| ID | 期数 | 标题 | 总行数 | 瑞希台词 | 文件 |")
md.append("|---|---|---|---|---|---|")
md += [row(e) for e in entries if e["type"] == "event"]
md.append("\n## 自我介绍\n")
md.append("| ID | 期数 | 标题 | 总行数 | 瑞希台词 | 文件 |")
md.append("|---|---|---|---|---|---|")
md += [row(e) for e in entries if e["type"] == "intro"]
md.append("\n## 区域对话（日常碎片，%d 条，文件名即 scriptId）\n" % len([e for e in entries if e["type"]=="area"]))
md.append("区域对话为地图小对话，单条 5-30 句，适合快速取样瑞希日常语气。全部文件见 `corpus/区域对话/`。\n")

with open(os.path.join(SKILL, "references", "corpus-index.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(md))
print("written corpus-index.md")

# 汇总
total_lines = sum(e["lines"] for e in entries)
total_mizuki = sum(e["mizuki_lines"] for e in entries)
print(f"TOTAL files={len(entries)} lines={total_lines} mizuki_lines={total_mizuki}")
