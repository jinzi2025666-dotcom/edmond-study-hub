"""Apply lesson / question / set dictionaries onto a Course."""
from __future__ import annotations

from _helpers import opts as make_opts


def add_question(course, section_id, q, default_prefix=None):
    q = dict(q)
    typ = q.pop("type")
    qid = q.pop("id")
    if typ == "mcq" and q.get("options") and isinstance(q["options"][0], (list, tuple)):
        q["options"] = make_opts(*[(a, b) for a, b in q["options"]])
    course.Q(qid, section_id, typ, **q)
    return qid


def add_lesson(course, lesson):
    section = lesson["id"]
    qids = []
    prefix = getattr(course, "tag", None) or default_prefix_for(course)
    for i, q in enumerate(lesson["questions"], 1):
        q = dict(q)
        q.setdefault("id", f"q-{prefix}-{section}-{i:02d}")
        qids.append(add_question(course, section, q))
    course.lesson(
        section,
        lesson["title_zh"], lesson["title_en"],
        lesson["obj_zh"], lesson["obj_en"],
        lesson["kp_zh"], lesson["kp_en"],
        lesson["body_zh"], lesson["body_en"],
        lesson["diff_zh"], lesson["diff_en"],
        qids,
        diagram=lesson.get("diagram") or "",
        coding_exercise_ids=lesson.get("coding_exercise_ids"),
    )
    return qids


def default_prefix_for(course):
    return course.subject_id[:2]


def add_sets(course, chapter_sets, comprehensive=None):
    for row in chapter_sets:
        kind = row["kind"]
        if kind == "practice":
            course.chapter_practice(row["chapter"], row["title_zh"], row["title_en"], row["qids"],
                                    minutes=row.get("minutes", 15), published=row.get("published"))
        else:
            course.chapter_paper(row["chapter"], row["title_zh"], row["title_en"], row["qids"],
                                 minutes=row.get("minutes", 25), published=row.get("published"))
    if comprehensive:
        course.comprehensive(
            comprehensive["id"],
            comprehensive["title_zh"], comprehensive["title_en"],
            comprehensive["qids"],
            minutes=comprehensive.get("minutes", 35),
            published=comprehensive.get("published"),
        )


def add_extra_questions(course, items):
    """items: list of (section_id, question_dict) used by chapter papers."""
    qids = []
    for section_id, q in items:
        q = dict(q)
        qids.append(add_question(course, section_id, q))
    return qids
