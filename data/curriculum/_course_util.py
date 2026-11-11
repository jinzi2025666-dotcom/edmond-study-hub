"""Shared builders for full Year 8 courses (mirrors Physics helpers)."""
from __future__ import annotations

import json
from pathlib import Path

from _helpers import Q as _Q, KP, SET, opts

PUB = "2026-10-20T09:00:00+08:00"
RECENT_DEFAULT = "2026-11-12T09:00:00+08:00"


def svg(inner, w=520, h=220):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" class="lesson-diagram" role="img" aria-hidden="false">'
        f'<rect width="{w}" height="{h}" fill="none"/>'
        f"{inner}</svg>"
    )


INK = 'stroke="currentColor" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"'
FILL = 'fill="currentColor"'
ACCENT = 'stroke="#b85c38" fill="none" stroke-width="1.8" stroke-linecap="round"'


class Course:
    """Accumulate lessons, questions and sets for one subject."""

    def __init__(self, subject_id: str, unit_of: dict[str, str], chapter_of: dict[str, str] | None = None,
                 recent: dict[str, str] | None = None, tag: str = ""):
        self.subject_id = subject_id
        self.unit_of = unit_of
        self.chapter_of = chapter_of or {}
        self.recent = recent or {}
        self.tag = tag or subject_id[:2]
        self.knowledge: list[dict] = []
        self.questions: list[dict] = []
        self.sets: list[dict] = []
        self._lesson_qids: dict[str, list[str]] = {}

    def chapter_id(self, section_id: str) -> str:
        if section_id in self.chapter_of:
            return self.chapter_of[section_id]
        if section_id in self.unit_of:
            # unit id like chemistry-8Cm-u1 -> chemistry-8Cm
            uid = self.unit_of[section_id]
            parts = uid.split("-")
            # drop trailing uN if present
            if parts and parts[-1].startswith("u") and parts[-1][1:].isdigit():
                return "-".join(parts[:-1])
            return uid
        # fallback: strip last -sXX or -N
        parts = section_id.split("-")
        return "-".join(parts[:-1]) if len(parts) > 1 else section_id

    def Q(self, qid, section_id, typ, stem_zh, stem_en, answer, exp_zh, exp_en, **kw):
        pub = kw.pop("published_at", self.recent.get(section_id, PUB))
        chapter = self.chapter_id(section_id)
        item = _Q(
            qid, self.subject_id, chapter, typ,
            stem_zh, stem_en, answer, exp_zh, exp_en,
            knowledge_id="kp-" + section_id, published_at=pub, **kw,
        )
        item["grade_id"] = "8"
        item["chapter_id"] = chapter
        item["unit_id"] = self.unit_of[section_id]
        item["section_id"] = section_id
        self.questions.append(item)
        return item

    def mcq(self, qid, section_id, stem_zh, stem_en, answer, exp_zh, exp_en, options, **kw):
        return self.Q(qid, section_id, "mcq", stem_zh, stem_en, answer, exp_zh, exp_en, options=options, **kw)

    def numeric(self, qid, section_id, stem_zh, stem_en, answer, exp_zh, exp_en, **kw):
        kw.setdefault("tolerance", 0)
        return self.Q(qid, section_id, "numeric", stem_zh, stem_en, answer, exp_zh, exp_en, **kw)

    def short(self, qid, section_id, stem_zh, stem_en, answer, exp_zh, exp_en, **kw):
        return self.Q(qid, section_id, "short", stem_zh, stem_en, answer, exp_zh, exp_en, **kw)

    def lesson(self, section_id, title_zh, title_en, obj_zh, obj_en, kp_zh, kp_en,
               body_zh, body_en, diff_zh, diff_en, qids, diagram=None,
               summary_zh="", summary_en="", coding_exercise_ids=None):
        published = self.recent.get(section_id, PUB)
        chapter = self.chapter_id(section_id)
        item = KP(
            "kp-" + section_id, self.subject_id, chapter, section_id,
            title_zh, title_en, body_zh, body_en, qids, published,
            summary_zh=summary_zh or obj_zh, summary_en=summary_en or obj_en,
        )
        item.update({
            "grade_id": "8",
            "chapter_id": chapter,
            "unit_id": self.unit_of[section_id],
            "section_id": section_id,
            "objectives_zh": obj_zh.strip(),
            "objectives_en": obj_en.strip(),
            "keypoints_zh": kp_zh.strip(),
            "keypoints_en": kp_en.strip(),
            "difficulties_zh": diff_zh.strip(),
            "difficulties_en": diff_en.strip(),
            "diagram": diagram or "",
            "developed": True,
        })
        if coding_exercise_ids:
            item["coding_exercise_ids"] = list(coding_exercise_ids)
        self.knowledge.append(item)
        self._lesson_qids[section_id] = list(qids)
        return item

    def pset(self, sid, chapter, kind, title_zh, title_en, qids, minutes=None, published=None):
        item = SET(sid, self.subject_id, chapter, kind, title_zh, title_en, qids,
                   time_limit=minutes, published_at=published or PUB)
        item["grade_id"] = "8"
        item["chapter_id"] = chapter if chapter else None
        item["scope"] = "course" if (chapter is None or "comprehensive" in sid) else "chapter"
        self.sets.append(item)
        return item

    def chapter_practice(self, chapter, title_zh, title_en, qids, minutes=15, published=None):
        return self.pset(f"practice-{chapter}", chapter, "practice", title_zh, title_en, qids,
                         minutes=minutes, published=published)

    def chapter_paper(self, chapter, title_zh, title_en, qids, minutes=25, published=None):
        return self.pset(f"paper-{chapter}", chapter, "paper", title_zh, title_en, qids,
                         minutes=minutes, published=published)

    def comprehensive(self, sid, title_zh, title_en, qids, minutes=35, published=None):
        return self.pset(sid, None, "paper", title_zh, title_en, qids,
                         minutes=minutes, published=published or RECENT_DEFAULT)


def maps_from_units(subject_id: str, grade_id: str = "8"):
    """Build section -> unit and section -> chapter maps from units.json."""
    path = Path(__file__).resolve().parent / "units.json"
    tree = json.loads(path.read_text(encoding="utf-8"))
    unit_of = {}
    chapter_of = {}
    for chapter in tree:
        if chapter.get("subject_id") != subject_id:
            continue
        if str(chapter.get("grade_id") or "8") != str(grade_id):
            continue
        for unit in chapter.get("units") or []:
            for section in unit.get("sections") or []:
                unit_of[section["id"]] = unit["id"]
                chapter_of[section["id"]] = chapter["id"]
    return unit_of, chapter_of


