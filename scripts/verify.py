#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AISecSight 接口自检：逐个请求核心接口，检查 HTTP 状态与关键字段。

用法：
    python scripts/verify.py            # 检查全部
    python scripts/verify.py --etag     # 额外验证 ETag / 304 协商缓存

仅依赖 Python 3.8+ 标准库，无需安装任何第三方包。
"""

import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE = "https://aisecsight.com"
UA = "aisecsight-skill-verify/1.0 (+https://github.com/SecurityGuardian-pro/aisecsight-skill)"

# (名称, 路径, 需要存在的键, 说明)
CHECKS = [
    ("接口索引", "/api/v1", ["endpoints"], "接口清单"),
    ("法规检索", "/api/v1/laws?q=" + urllib.parse.quote("深度伪造"), ["laws"], "关键词检索"),
    ("法域筛选", "/api/v1/laws?region=eu", ["laws", "total"], "欧盟法规"),
    ("法规详情", "/api/v1/laws/euact", ["law"], "单部法规"),
    ("罚则条款", "/api/v1/laws/euact", ["law"], "penalty.tiers"),
    ("合规问答", "/api/v1/qa?q=" + urllib.parse.quote("标识"), ["items"], "带出处的问答"),
    ("处罚量化", "/api/v1/penalties", ["fx"], "最高处罚与汇率"),
    ("十大法规", "/api/v1/top10", ["items"], "Top 10"),
    ("安全事件", "/api/v1/incidents", ["items"], "2023 年以来"),
    ("治理动态", "/api/v1/news?type=governance&limit=3", ["items"], "最近治理动态"),
    ("每周要点", "/api/v1/weekly/latest", [], "上一周要点"),
]


def fetch(path, timeout=30, extra_headers=None):
    req = urllib.request.Request(BASE + path, headers={"User-Agent": UA, "Accept": "application/json"})
    for k, v in (extra_headers or {}).items():
        req.add_header(k, v)
    start = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            elapsed = (time.time() - start) * 1000
            return resp.status, raw, case_insensitive(dict(resp.headers)), elapsed
    except urllib.error.HTTPError as e:
        return e.code, e.read(), case_insensitive(dict(e.headers)), (time.time() - start) * 1000
    except Exception as e:  # 网络层错误
        return None, str(e).encode(), {}, (time.time() - start) * 1000


def case_insensitive(headers):
    """响应头大小写不固定（服务端发的是 Etag），统一成小写键方便取。"""
    return {str(k).lower(): v for k, v in headers.items()}


def check_one(item):
    name, path, keys, note = item
    status, raw, headers, ms = fetch(path)
    ok = status == 200
    detail = ""
    data = None
    if ok:
        try:
            data = json.loads(raw.decode("utf-8"))
        except Exception:
            ok, detail = False, "返回不是合法 JSON"
        else:
            missing = [k for k in keys if k not in data]
            if missing:
                ok, detail = False, "缺少字段 " + ", ".join(missing)
            else:
                total = data.get("total")
                if isinstance(total, int):
                    detail = "total=%d" % total
                elif isinstance(data.get("laws"), list):
                    detail = "%d 条" % len(data["laws"])
                elif isinstance(data.get("items"), list):
                    detail = "%d 条" % len(data["items"])
                elif isinstance(data.get("endpoints"), list):
                    detail = "%d 个接口" % len(data["endpoints"])
                else:
                    detail = "OK"
    else:
        detail = ("HTTP %s" % status) if status else "网络错误: " + raw.decode("utf-8", "replace")[:80]

    # 罚则接口额外的深层字段检查
    if ok and name == "罚则条款":
        law = data.get("law") or {}
        tiers = ((law.get("penalty") or {}).get("tiers")) or []
        if not tiers:
            ok, detail = False, "penalty.tiers 为空"
        else:
            detail = "%d 档罚则，reviewed=%s" % (len(tiers), law.get("reviewed", "?"))

    return dict(name=name, path=path, ok=ok, status=status, ms=ms, detail=detail, note=note,
                etag=headers.get("etag"))


def check_etag():
    """带 If-None-Match 重放请求，验证 304 协商缓存。"""
    status, _, headers, _ = fetch("/api/v1/laws?region=cn")
    etag = headers.get("etag")
    if status != 200 or not etag:
        return False, "首个请求未返回 ETag（status=%s）" % status
    status2, _, _, _ = fetch("/api/v1/laws?region=cn", extra_headers={"If-None-Match": etag})
    if status2 == 304:
        return True, "ETag=%s，重放返回 304" % etag
    return False, "ETag=%s，但重放返回 %s（预期 304）" % (etag, status2)


def main():
    ap = argparse.ArgumentParser(description="AISecSight 接口自检")
    ap.add_argument("--etag", action="store_true", help="额外验证 ETag / 304")
    args = ap.parse_args()

    print("AISecSight 接口自检 · %s" % BASE)
    print("-" * 84)

    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(check_one, CHECKS))

    failed = 0
    for r in results:
        mark = "PASS" if r["ok"] else "FAIL"
        if not r["ok"]:
            failed += 1
        print("%-4s %-10s %-8s %6.0fms  %s" % (mark, r["name"], r["status"] or "-", r["ms"], r["detail"]))

    if args.etag:
        print("-" * 84)
        ok, msg = check_etag()
        print("%-4s %-10s %s" % ("PASS" if ok else "FAIL", "协商缓存", msg))
        failed += 0 if ok else 1

    print("-" * 84)
    total_ms = sum(r["ms"] for r in results)
    if failed == 0:
        print("全部通过（%d 项，合计 %.1fs）。装好了，新开会话即可使用。" % (len(results), total_ms / 1000))
        return 0
    print("%d 项未通过（共 %d 项）。常见原因：网络不通、IP 被限流（HTTP 429，按 Retry-After 等待）。"
          % (failed, len(results) + (1 if args.etag else 0)))
    return 1


if __name__ == "__main__":
    sys.exit(main())
