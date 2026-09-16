#!/usr/bin/env python3
"""
虚拟女主播库 · 命令行调取接口

只依赖 Python 标准库，不需要安装任何东西。
读 index/ai-index.json，卡从 cards/ 下按索引里的路径取。

例：
    python3 query.py --factor F04 --fields id,one_liner --format md
    python3 query.py --language 韩语
    python3 query.py --card 宝钟玛琳 --full
    python3 query.py --grep "ASMR"
    python3 query.py --random 6 --fields id,factors
"""
import argparse
import json
import os
import random
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(ROOT, "index", "ai-index.json")


def load():
    if not os.path.exists(INDEX):
        sys.exit("找不到 index/ai-index.json；请在仓库根目录运行。")
    return json.load(open(INDEX, encoding="utf-8"))


def read_card(rel):
    return open(os.path.join(ROOT, rel), encoding="utf-8").read()


def sections(text):
    out, cur, buf = {}, None, []
    for line in text.splitlines():
        m = re.match(r"^##\s+(.*)$", line)
        if m:
            if cur:
                out[cur] = "\n".join(buf)
            cur, buf = m.group(1).strip(), []
        elif cur is not None:
            buf.append(line)
    if cur:
        out[cur] = "\n".join(buf)
    return out


def main():
    ap = argparse.ArgumentParser(description="虚拟女主播库 · 命令行调取接口")
    ap.add_argument("--platform", help="平台目录，如 hololive / B站-个人势 / 英语圈-独立势")
    ap.add_argument("--affiliation", help="阵营，如 hololive / 独立 / VirtuaReal")
    ap.add_argument("--language", help="语言：日语 / 英语 / 中文 / 韩语 / 印尼语")
    ap.add_argument("--status", help="活动中 / 毕业 / 停活 / 休止")
    ap.add_argument("--factor", help="要素编号，如 F04；可逗号分隔，取并集")
    ap.add_argument("--has-prompt", action="store_true", help="只取写了提示词的")
    ap.add_argument("--grep", help="在卡片正文里全文匹配（返回命中的 id 与命中行）")
    ap.add_argument("--card", help="取某一位的完整卡")
    ap.add_argument("--full", action="store_true", help="配合 --card：输出完整正文")
    ap.add_argument("--random", type=int, help="随机抽 N 位（做参考采样）")
    ap.add_argument("--sort", choices=["subs", "fans", "name"], default="subs")
    ap.add_argument("--limit", type=int, default=0, help="0 = 不限")
    ap.add_argument("--fields", default="", help="逗号分隔要返回的字段，如 id,platform,one_liner")
    ap.add_argument("--format", choices=["json", "md", "ids"], default="json")
    a = ap.parse_args()
    d = load()

    if a.card:
        hit = next((c for c in d["characters"] if c["id"] == a.card), None)
        if not hit:
            sys.exit(f"没有这个人：{a.card}")
        text = read_card(hit["card"])
        if a.full:
            print(text)
        else:
            sec = sections(text)
            print(json.dumps({
                "meta": hit,
                "identity": sec.get("一、身份", "")[:1500],
                "look_analysis": sec.get("七、人物形象分析", "") or "（尚未写）",
                "prompt": sec.get("八、人设生成提示词", "") or "（尚未写）",
            }, ensure_ascii=False, indent=1))
        return

    items = d["characters"]

    if a.grep:
        pat = re.compile(a.grep, re.I)
        out = []
        for c in items:
            hits = [ln.strip()[:120] for ln in read_card(c["card"]).splitlines()
                    if pat.search(ln)]
            if hits:
                out.append({"id": c["id"], "platform": c["platform_dir"],
                            "hits": hits[:4], "card": c["card"]})
        if a.format == "ids":
            print("\n".join(x["id"] for x in out))
        elif a.format == "md":
            for x in out:
                print(f"- **{x['id']}**（{x['platform']}）— " + " ／ ".join(x["hits"][:2]))
        else:
            print(json.dumps(out, ensure_ascii=False, indent=1))
        return

    if a.platform:
        want = set(a.platform.split(","))
        items = [c for c in items if c["platform_dir"] in want]
    if a.language:
        want = set(a.language.split(","))
        items = [c for c in items if c.get("language") in want]
    if a.affiliation:
        want = set(a.affiliation.split(","))
        items = [c for c in items if c.get("affiliation") in want]
    if a.status:
        want = set(a.status.split(","))
        items = [c for c in items if c["status"] in want]
    if a.factor:
        want = {x.strip().upper() for x in a.factor.split(",")}
        items = [c for c in items if want & {f["id"] for f in c["factors"]}]
    if a.has_prompt:
        items = [c for c in items if c["has_prompt"]]

    if a.random:
        items = random.sample(items, min(a.random, len(items)))
    else:
        if a.sort == "subs":
            items.sort(key=lambda c: -(c["metrics"]["youtube_subscribers"] or 0))
        elif a.sort == "fans":
            items.sort(key=lambda c: -(c["metrics"]["bilibili_fans"] or 0))
        else:
            items.sort(key=lambda c: c["id"])
    if a.limit:
        items = items[:a.limit]

    fields = ([f.strip() for f in a.fields.split(",") if f.strip()]
              if a.format == "json" else None)
    if fields and "id" not in fields:
        fields = ["id"] + fields
    if fields:
        items = [{k: c.get(k) for k in fields} for c in items]

    if a.format == "ids":
        print("\n".join(c["id"] if isinstance(c, dict) and "id" in c else str(c)
                        for c in items))
    elif a.format == "md":
        for c in items:
            if isinstance(c, dict) and "id" in c:
                plat = c.get("platform_dir") or c.get("platform") or ""
                print(f"- **{c['id']}**（{plat}）— {c.get('one_liner','')}")
            else:
                print(f"- {c}")
    else:
        print(json.dumps({"count": len(items), "characters": items},
                         ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
