"""Attach revision-guide text and extra graded questions before a subject is built."""
from __future__ import annotations

from .expansion import EXTRAS, GUIDES


def deepen(spec: dict) -> dict:
    for chapter in spec["chapters"]:
        for unit in chapter["units"]:
            for lesson in unit["lessons"]:
                guide = GUIDES.get(lesson["id"])
                if guide:
                    lesson["guide_zh"], lesson["guide_en"] = guide
                extra = EXTRAS.get(lesson["id"]) or []
                lesson["questions"] = list(lesson["questions"]) + list(extra)
    paper = spec.get("paper")
    if paper:
        if "comprehensive" not in paper["id"]:
            paper["id"] = paper["id"] + "-comprehensive"
        paper["title_zh"] = paper["title_zh"].replace("练习卷", "综合测试卷")
        if not paper["title_zh"].startswith("综合"):
            paper["title_zh"] = "综合测试卷 · " + paper["title_zh"]
        paper["title_en"] = paper["title_en"].replace("Practice paper", "Comprehensive paper")
        if not paper["title_en"].lower().startswith("comprehensive"):
            paper["title_en"] = "Comprehensive paper · " + paper["title_en"]
        for _section, q in paper["items"]:
            q.setdefault("difficulty", "challenge")
    return spec
