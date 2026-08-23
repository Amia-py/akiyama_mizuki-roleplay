# -*- coding: utf-8 -*-
"""校验 / 重建 sekai25.json 的辅助脚本。

用途：
1. 校验 sekai25.json 结构完整性（python build_data.py check）
2. 从导出的分表 JSON 合并重建（一般不需要，直接编辑 sekai25.json 即可）

说明：资料库已改为纯 JSON + Markdown 存储，不再需要 SQLite。
直接编辑 sekai25.json 即可扩充数据；本脚本仅做结构校验。
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, "sekai25.json")

REQUIRED_TABLES = {
    "story_events": ["chapter", "episode", "title_jp", "title_cn", "mizuki_focus", "summary", "mizuki_note"],
    "characters": ["name", "role", "mizuki_calls", "relation_note"],
    "speech_samples": ["scene", "mood", "content"],
}


def check():
    with open(DB, encoding="utf-8") as f:
        data = json.load(f)
    ok = True
    for table, fields in REQUIRED_TABLES.items():
        rows = data.get(table)
        if not isinstance(rows, list):
            print(f"[FAIL] 缺少表: {table}")
            ok = False
            continue
        for i, row in enumerate(rows):
            missing = [k for k in fields if k not in row]
            if missing:
                print(f"[FAIL] {table}[{i}] 缺字段: {missing}")
                ok = False
        print(f"[OK] {table}: {len(rows)} 条记录")
    print("校验通过" if ok else "校验失败")
    return ok


if __name__ == "__main__":
    sys.exit(0 if check() else 1)
