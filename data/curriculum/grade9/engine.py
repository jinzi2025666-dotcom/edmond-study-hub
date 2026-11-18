"""Build one Grade 9 subject: lessons, practice, topic tests, unit tests, comprehensive paper.

Lesson ids stay stable so later notes can replace a body without breaking links.
See data/README.md.
"""
from __future__ import annotations

from _apply import add_question
from _course_util import Course
from _helpers import opts

LESSON_PUBLISHED = "2026-11-16T09:00:00+08:00"
PRACTICE_PUBLISHED = "2026-11-16T10:00:00+08:00"
TOPIC_PUBLISHED = "2026-11-17T09:00:00+08:00"
UNIT_PUBLISHED = "2026-11-17T12:00:00+08:00"


def _scheme(q: dict) -> dict:
    q = dict(q)
    exp_zh = q.get("exp_zh") or ""
    exp_en = q.get("exp_en") or ""
    if "评分要点" in exp_zh or "Mark scheme" in exp_en:
        return q
    marks = int(q.get("marks") or 1)
    ans_zh = q.get("answer_zh") or q.get("answer") or ""
    ans_en = q.get("answer_en") or q.get("answer") or ""
    if q.get("type") == "mcq":
        letter = str(q.get("answer") or "").upper()
        ans_zh = f"选项 {letter}"
        ans_en = f"option {letter}"
    unit = "分" if marks != 1 else "分"
    q["exp_zh"] = (
        f"**评分要点（{marks} {unit}）**\n\n"
        f"- 给出与参考答案一致的要点：{ans_zh}。\n"
        f"- 若题目要求解释，解释必须扣住该要点，不能只重复题干。\n\n"
        f"**解析**\n\n{exp_zh}"
    )
    label = "mark" if marks == 1 else "marks"
    q["exp_en"] = (
        f"**Mark scheme ({marks} {label})**\n\n"
        f"- Award the mark for the point in the model answer: {ans_en}.\n"
        f"- If the question asks for a reason, the reason must support that point.\n\n"
        f"**Explanation**\n\n{exp_en}"
    )
    return q


def _options(q: dict) -> dict:
    q = _scheme(q)
    options = q.get("options")
    if options and isinstance(options[0], (list, tuple)):
        q["options"] = opts(*options)
    return q


def _guide(lesson: dict) -> tuple[str, str]:
    zh = (lesson.get("guide_zh") or "").strip()
    en = (lesson.get("guide_en") or "").strip()
    if zh and en:
        return zh, en
    steps_zh = []
    steps_en = []
    for i, (a, b) in enumerate(lesson.get("points") or [], 1):
        steps_zh.append(f"{i}. {a}")
        steps_en.append(f"{i}. {b}")
    traps = lesson.get("traps") or []
    trap_zh = "\n".join(f"- {a}" for a, _b in traps) or "- 先把题目里的指令词圈出来，再作答。"
    trap_en = "\n".join(f"- {b}" for _a, b in traps) or "- Circle the command word before you answer."
    zh = "\n\n".join([
        "## 关键定义\n\n" + "\n".join(f"- {a}" for a, _b in lesson.get("points") or []),
        "## 逐步讲解\n\n" + (lesson.get("explain_zh") or "").strip(),
        "## 公式、关系与进一步的例子\n\n" + "\n".join(steps_zh),
        "## 图示与版面\n\n先看标题和单位，再看箭头或数值的方向。把图里的每一个符号说成一句完整的话，再把它用回题目。",
        "## 考试提示与指令词\n\n- **写出 / state**：给定义或结果，不必展开。\n- **计算 / calculate**：写出公式、代入和单位。\n- **解释 / explain**：因为…所以…，至少一条因果。\n- **讨论 / discuss**：两边都写，最后给判断。\n\n常见失分：\n" + trap_zh,
        "## 本课小结\n\n" + (lesson.get("obj_zh") or ""),
    ])
    en = "\n\n".join([
        "## Key definitions\n\n" + "\n".join(f"- {b}" for _a, b in lesson.get("points") or []),
        "## Step by step\n\n" + (lesson.get("explain_en") or "").strip(),
        "## Formulas, relationships and a further pass\n\n" + "\n".join(steps_en),
        "## Diagrams and layout\n\nRead the title and the units first, then the direction of an arrow or a value. Turn each symbol into a full sentence before you use it in an answer.",
        "## Exam tips and command words\n\n- **State**: give the definition or result, without a long development.\n- **Calculate**: write the formula, the substitution and the unit.\n- **Explain**: because… therefore…, at least one causal link.\n- **Discuss**: both sides, then a judgement.\n\nCommon losses:\n" + trap_en,
        "## Short summary\n\n" + (lesson.get("obj_en") or ""),
    ])
    return zh, en


def _body(lesson: dict) -> tuple[str, str]:
    guide_zh, guide_en = _guide(lesson)
    zh = (lesson.get("explain_zh") or "").strip() + "\n\n" + guide_zh
    en = (lesson.get("explain_en") or "").strip() + "\n\n" + guide_en
    zh += "\n\n## 例题\n\n" + (lesson.get("example_zh") or "").strip()
    en += "\n\n## Worked example\n\n" + (lesson.get("example_en") or "").strip()
    return zh, en


def _set_scope(item: dict, scope: str) -> dict:
    item["scope"] = scope
    return item


def build_subject(spec: dict):
    course = Course(spec["subject_id"], {}, {}, tag=spec["tag"], grade_id="9")
    chapters_out = []
    topic_qids: dict[str, list[str]] = {}
    lesson_meta: dict[str, dict] = {}

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
                    q.setdefault("difficulty", "exam")
                    qids.append(add_question(course, sid, q))
                topic_qids[sid] = [
                    qid for qid, raw in zip(qids, lesson["questions"])
                    if (raw.get("difficulty") or "exam") in ("basic", "exam")
                ] or list(qids)
                body_zh, body_en = _body(lesson)
                points = lesson.get("points") or []
                kp_zh = "\n".join(f"- {a}" for a, _b in points)
                kp_en = "\n".join(f"- {b}" for _a, b in points)
                traps = lesson.get("traps") or []
                diff_zh = "\n".join(f"- **{a}**" for a, _b in traps)
                diff_en = "\n".join(f"- **{b}**" for _a, b in traps)
                course.lesson(
                    sid,
                    lesson["title_zh"], lesson["title_en"],
                    lesson["obj_zh"], lesson["obj_en"],
                    kp_zh, kp_en, body_zh, body_en, diff_zh, diff_en,
                    qids, diagram=lesson.get("diagram") or "",
                )
                lesson_meta[sid] = lesson
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
                t_ids = topic_qids[sid]
                topic = course.chapter_paper(
                    ch["id"],
                    f"{lesson['title_zh']} · 专题测验",
                    f"{lesson['title_en']} · topic test",
                    t_ids,
                    minutes=max(15, min(35, len(t_ids) * 2)),
                    published=TOPIC_PUBLISHED,
                )
                # chapter_paper uses id paper-{chapter}; make it unique per topic
                topic["id"] = f"paper-topic-{sid}"
                _set_scope(topic, "topic")
            units_out.append({
                "id": unit["id"],
                "code": unit.get("code") or str(ui),
                "order": unit.get("order") or ui,
                "title_zh": unit["title_zh"],
                "title_en": unit["title_en"],
                "sections": sections_out,
            })
        lesson_qids = [
            q["id"] for q in course.questions
            if q.get("chapter_id") == ch["id"] and q.get("difficulty") != "unit"
        ]
        if lesson_qids:
            course.chapter_practice(
                ch["id"],
                f"{ch['title_zh']} · 练习",
                f"{ch['title_en']} · practice",
                lesson_qids,
                minutes=ch.get("practice_minutes") or 25,
                published=ch.get("practice_published") or PRACTICE_PUBLISHED,
            )
        challenge = []
        seen_ids = set()
        for wanted in ("unit", "challenge", "exam"):
            for q in course.questions:
                if q.get("chapter_id") != ch["id"] or q.get("difficulty") != wanted:
                    continue
                if q["id"] in seen_ids:
                    continue
                if wanted == "exam" and len(challenge) >= 8:
                    break
                challenge.append(q["id"])
                seen_ids.add(q["id"])
            if wanted == "challenge" and len(challenge) >= 8:
                break
        challenge = challenge[:12]
        if challenge:
            unit_paper = course.chapter_paper(
                ch["id"],
                f"{ch['title_zh']} · 单元测验",
                f"{ch['title_en']} · unit test",
                challenge,
                minutes=max(25, min(50, len(challenge) * 3)),
                published=UNIT_PUBLISHED,
            )
            unit_paper["id"] = f"paper-unit-{ch['id']}"
            _set_scope(unit_paper, "unit")
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

    # chapter_paper assigns the same id paper-{chapter} to the last call.
    # Rewrite ids that collided: any set whose id is paper-{chapter} and scope still chapter
    # was overwritten in the list because we mutated the dict after append.
    # chapter_paper appends a new dict each time, then we change its id. Good.
    # BUT the first topic paper and the unit paper both call chapter_paper which uses
    # id f"paper-{chapter}" BEFORE we overwrite. If two dicts are appended then both
    # get their ids changed, no collision remains. Verify chapter_paper doesn't
    # reuse the same dict. It creates a new item each call. Good.

    paper = spec.get("paper")
    if paper:
        paper_ids = []
        for i, (section_id, raw) in enumerate(paper["items"], 1):
            q = _options(raw)
            q.setdefault("difficulty", "challenge")
            q.setdefault("id", f"q-{spec['tag']}-p-{i:02d}")
            qid = add_question(course, section_id, q)
            paper_ids.append(qid)
            for kp in course.knowledge:
                if kp.get("section_id") == section_id and qid not in kp["related_question_ids"]:
                    kp["related_question_ids"].append(qid)
        pid = paper["id"]
        if "comprehensive" not in pid:
            pid = pid + "-comprehensive"
        title_zh = paper["title_zh"].replace("练习卷", "综合测试卷")
        title_en = paper["title_en"].replace("Practice paper", "Comprehensive paper")
        course.comprehensive(
            pid, title_zh, title_en, paper_ids,
            minutes=paper["minutes"], published=paper.get("published"),
        )
    # Drop duplicate paper ids if chapter_paper left an intermediate id.
    seen = set()
    unique = []
    for item in course.sets:
        if item["id"] in seen:
            continue
        seen.add(item["id"])
        unique.append(item)
    course.sets = unique
    return course.knowledge, course.questions, course.sets, chapters_out
