"""Helpers for the Grade 8 Physics course builder."""
from _helpers import Q as _Q, KP, SET, opts

PUB = "2026-10-20T09:00:00+08:00"
RECENT = {
    "physics-8Pf-s01": "2026-11-10T09:00:00+08:00",
    "physics-8Pf-s02": "2026-11-11T09:00:00+08:00",
    "physics-8Ps-s01": "2026-11-08T09:00:00+08:00",
    "physics-8Pe-s02": "2026-11-07T09:00:00+08:00",
    "physics-8ES-s01": "2026-11-06T09:00:00+08:00",
}

CHAPTER = {
    "8Pf": "physics-8Pf",
    "8Ps": "physics-8Ps",
    "8Pe": "physics-8Pe",
    "8ES": "physics-8ES",
}
UNIT_OF = {
    "physics-8Pf-s01": "physics-8Pf-u1", "physics-8Pf-s02": "physics-8Pf-u1",
    "physics-8Pf-s03": "physics-8Pf-u2", "physics-8Pf-s04": "physics-8Pf-u2",
    "physics-8Pf-s05": "physics-8Pf-u3", "physics-8Pf-s06": "physics-8Pf-u3", "physics-8Pf-s07": "physics-8Pf-u3",
    "physics-8Ps-s01": "physics-8Ps-u1", "physics-8Ps-s02": "physics-8Ps-u1",
    "physics-8Ps-s03": "physics-8Ps-u2", "physics-8Ps-s04": "physics-8Ps-u2",
    "physics-8Pe-s01": "physics-8Pe-u1", "physics-8Pe-s02": "physics-8Pe-u2", "physics-8Pe-s03": "physics-8Pe-u2",
    "physics-8ES-s01": "physics-8ES-u1", "physics-8ES-s02": "physics-8ES-u2", "physics-8ES-s03": "physics-8ES-u2",
}


def sid_chapter(section_id: str) -> str:
    # physics-8Pf-s01 -> physics-8Pf
    return "-".join(section_id.split("-")[:2])


def PQ(qid, section_id, typ, stem_zh, stem_en, answer, exp_zh, exp_en, **kw):
    kw.setdefault("published_at", RECENT.get(section_id, PUB))
    item = _Q(
        qid, "physics", sid_chapter(section_id), typ,
        stem_zh, stem_en, answer, exp_zh, exp_en,
        knowledge_id="kp-" + section_id, **kw,
    )
    item["grade_id"] = "8"
    item["chapter_id"] = sid_chapter(section_id)
    item["unit_id"] = UNIT_OF[section_id]
    item["section_id"] = section_id
    return item


def lesson(section_id, title_zh, title_en, obj_zh, obj_en, kp_zh, kp_en, body_zh, body_en, diff_zh, diff_en, qids, diagram=None, summary_zh="", summary_en=""):
    published = RECENT.get(section_id, PUB)
    item = KP(
        "kp-" + section_id, "physics", sid_chapter(section_id), section_id,
        title_zh, title_en, body_zh, body_en, qids, published,
        summary_zh=summary_zh or obj_zh, summary_en=summary_en or obj_en,
    )
    item.update({
        "grade_id": "8",
        "chapter_id": sid_chapter(section_id),
        "unit_id": UNIT_OF[section_id],
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
    return item


def pset(sid, chapter, kind, title_zh, title_en, qids, minutes=None, published=None):
    item = SET(sid, "physics", chapter, kind, title_zh, title_en, qids, time_limit=minutes, published_at=published or PUB)
    item["grade_id"] = "8"
    item["chapter_id"] = chapter if chapter else None
    item["scope"] = "course" if "comprehensive" in sid or chapter is None else "chapter"
    return item


def svg(inner, w=520, h=220):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" class="lesson-diagram" role="img" aria-hidden="false">'
        f'<rect width="{w}" height="{h}" fill="none"/>'
        f"{inner}</svg>"
    )

INK = 'stroke="currentColor" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"'
FILL = 'fill="currentColor"'
COPPER = 'stroke="#b85c38" fill="none" stroke-width="1.8" stroke-linecap="round"'
