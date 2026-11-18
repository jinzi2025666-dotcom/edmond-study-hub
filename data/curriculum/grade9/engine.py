"""Build one Grade 9 subject from a chapter/lesson specification.

Lesson ids stay stable so later teacher notes can replace the body without
breaking links, progress or the mistake book. See data/README.md.
"""
from __future__ import annotations

from _apply import add_question
from _compact import body as pack_body, bullets, diffs
from _course_util import Course
from _helpers import opts

LESSON_PUBLISHED = "2026-11-16T09:00:00+08:00"
PRACTICE_PUBLISHED = "2026-11-16T10:00:00+08:00"


def _options(q: dict) -> dict:
    q = dict(q)
    options = q.get("options")
    if options and isinstance(options[0], (list, tuple)):
        q["options"] = opts(*options)
    return q


def build_subject(spec: dict):
    course = Course(spec["subject_id"], {}, {}, tag=spec["tag"], grade_id="9")
    chapters_out = []
    for ci, ch in enumerate(spec["chapters"], 1):
        units_out = []
        topics = []
        for ui, unit in enumerate(ch["units"], 1):
            sections_out = []
            for lesson in unit["lessons"]:
                sid = lesson["id"]
                course.unit_of[sid] = unit["id"]
                course.chapter_of[sid] = ch["id"]
                course.recent[sid] = lesson.get("published") or LESSON_PUBLISHED
                qids = []
                for i, raw in enumerate(lesson["questions"], 1):
                    q = _options(raw)
                    q.setdefault("id", f"q-{spec['tag']}-{sid}-{i:02d}")
                    qids.append(add_question(course, sid, q))
                kp_zh, kp_en = bullets(lesson["points"])
                body_zh, body_en = pack_body(
                    lesson["explain_zh"], lesson["explain_en"],
                    lesson["example_zh"], lesson["example_en"],
                )
                diff_zh, diff_en = diffs(lesson["traps"])
                course.lesson(
                    sid,
                    lesson["title_zh"], lesson["title_en"],
                    lesson["obj_zh"], lesson["obj_en"],
                    kp_zh, kp_en, body_zh, body_en, diff_zh, diff_en,
                    qids, diagram=lesson.get("diagram") or "",
                )
                sections_out.append({
                    "id": sid,
                    "code": lesson.get("code") or sid,
                    "title_zh": lesson["title_zh"],
                    "title_en": lesson["title_en"],
                    "knowledge_id": "kp-" + sid,
                })
                topics.append({
                    "id": sid,
                    "title_zh": lesson["title_zh"],
                    "title_en": lesson["title_en"],
                })
            units_out.append({
                "id": unit["id"],
                "code": unit.get("code") or str(ui),
                "order": unit.get("order") or ui,
                "title_zh": unit["title_zh"],
                "title_en": unit["title_en"],
                "sections": sections_out,
            })
        lesson_qids = [q["id"] for q in course.questions if q.get("chapter_id") == ch["id"]]
        if lesson_qids:
            course.chapter_practice(
                ch["id"],
                f"{ch['title_zh']} · 练习",
                f"{ch['title_en']} · practice",
                lesson_qids,
                minutes=ch.get("practice_minutes") or 20,
                published=ch.get("practice_published") or PRACTICE_PUBLISHED,
            )
        chapters_out.append({
            "id": ch["id"],
            "subject_id": spec["subject_id"],
            "grade_id": "9",
            "kind": "chapter",
            "code": ch.get("code") or str(ci),
            "order": ch.get("order") or ci,
            "title_zh": ch["title_zh"],
            "title_en": ch["title_en"],
            "developed": True,
            "note_zh": ch.get("note_zh") or "",
            "note_en": ch.get("note_en") or "",
            "units": units_out,
            "topics": topics,
        })

    paper = spec.get("paper")
    if paper:
        paper_ids = []
        for i, (section_id, raw) in enumerate(paper["items"], 1):
            q = _options(raw)
            q.setdefault("id", f"q-{spec['tag']}-p-{i:02d}")
            qid = add_question(course, section_id, q)
            paper_ids.append(qid)
            for kp in course.knowledge:
                if kp.get("section_id") == section_id and qid not in kp["related_question_ids"]:
                    kp["related_question_ids"].append(qid)
        course.comprehensive(
            paper["id"], paper["title_zh"], paper["title_en"], paper_ids,
            minutes=paper["minutes"], published=paper.get("published"),
        )
    return course.knowledge, course.questions, course.sets, chapters_out
