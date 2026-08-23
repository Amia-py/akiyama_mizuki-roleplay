# -*- coding: utf-8 -*-
"""说话人标签重命名工具（三语，只动行首标签，绝不碰对话正文）

用法：
  python rename_speaker.py --old "瑞希的姐姐" --new "优希" --lang zh
  python rename_speaker.py --old "Mizuki's Mother" --new "Yuki's Mother" --lang en
  python rename_speaker.py --check --lang zh      # 只审计不改动

规则（用户约定，硬性）：
- 只替换**行首**的 【旧名】 说话人标签，正文/称呼一律不动
- 台词正文里出现的称谓是角色间正常用语，保留
- --check 模式逐行比对源语料，报告是否有标签以外内容被改动
- --lang 指定语言目录 zh/jp/en（各语言说话人名不同：zh/jp 用中文名，en 用英文名）
"""
import os, re, sys, argparse

SRCS = {
    "zh": r"C:\Users\1\WorkBuddy\2026-08-18-21-08-00\Mizuki_Stories",
    "jp": r"C:\Users\1\WorkBuddy\2026-08-12-16-53-09\Mizuki_Stories_JP",
    "en": r"C:\Users\1\WorkBuddy\2026-08-12-16-53-09\Mizuki_Stories_EN",
}
DST_BASE = r"C:\Users\1\.workbuddy\skills\mizuki-roleplay\references\corpus"

SPEAKER = re.compile(r"^(【)([^】]*)(】)(.*)$", re.S)


def read_map(root):
    d = {}
    for dp, _, fs in os.walk(root):
        for fn in fs:
            if fn.endswith(".md"):
                p = os.path.join(dp, fn)
                d[os.path.relpath(p, root)] = open(p, encoding="utf-8").read().split("\n")
    return d


def check_integrity(lang="zh"):
    """审计：语料与源文件相比，除行首标签外不应有任何改动。返回违规行列表。"""
    src_root = SRCS.get(lang)
    if not src_root or not os.path.isdir(src_root):
        print(f"[WARN] {lang} 源目录不存在，跳过完整性审计（仅比较标签外改动不可用）。", file=sys.stderr)
        return []
    src, dst = read_map(src_root), read_map(os.path.join(DST_BASE, lang))
    bad = []
    for rel in dst:
        if rel not in src:
            continue
        for i, (s, d) in enumerate(zip(src[rel], dst[rel])):
            if s == d:
                continue
            m1, m2 = SPEAKER.match(s), SPEAKER.match(d)
            ok = (
                m1 and m2
                and m1.group(2) != m2.group(2)
                and m1.group(1) == m2.group(1) == "【"
                and m1.group(3) == m2.group(3) == "】"
                and m1.group(4) == m2.group(4)
            )
            if not ok:
                bad.append((rel, i + 1, s, d))
    return bad


def rename(old, new, lang="zh"):
    n_files = n_lines = 0
    root = os.path.join(DST_BASE, lang)
    for dp, _, fs in os.walk(root):
        for fn in fs:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dp, fn)
            lines = open(p, encoding="utf-8").read().split("\n")
            changed = False
            for i, line in enumerate(lines):
                m = SPEAKER.match(line)
                if m and m.group(2) == old:
                    lines[i] = m.group(1) + new + m.group(3) + m.group(4)
                    changed, n_lines = True, n_lines + 1
            if changed:
                open(p, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
                n_files += 1
    return n_files, n_lines


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--old", help="旧说话人名（不含括号）")
    ap.add_argument("--new", help="新说话人名（不含括号）")
    ap.add_argument("--lang", default="zh", choices=["zh", "jp", "en"], help="目标语言目录（默认 zh）")
    ap.add_argument("--check", action="store_true", help="只审计标签外改动，不写文件")
    args = ap.parse_args()

    bad = check_integrity(args.lang)
    if bad:
        print(f"[FAIL] 发现 {len(bad)} 处标签外改动（先修这些，禁止直接覆盖）：")
        for rel, ln, s, d in bad[:10]:
            print(f"  {rel}:{ln}\n    源: {s[:70]}\n    现: {d[:70]}")
        sys.exit(1)

    if args.check:
        print(f"[OK] {args.lang} 语料与源一致：所有改动均限于行首说话人标签，对话正文未被动过。")
        sys.exit(0)

    if not (args.old and args.new):
        ap.error("--rename 需同时提供 --old 与 --new")

    nf, nl = rename(args.old, args.new, args.lang)
    bad = check_integrity(args.lang)
    if bad:
        print(f"[FAIL] 重命名后出现 {len(bad)} 处标签外改动，已中止（语料保持原样）。")
        sys.exit(1)
    print(f"[OK] [{args.lang}] 已重命名 {nl} 行（{nf} 个文件）：【{args.old}】→【{args.new}】")
    print("[OK] 复检通过：正文零改动。")
