"""Placement diagnostics and spiral review for Grade 9. No login."""
from __future__ import annotations

from datetime import datetime, timezone

from . import database as db
from .coach import reasoning_ok
from .grading import check_answer

FORTNIGHT_MS = 14 * 24 * 3600 * 1000


def _sections(subject_id: str, grade_id: str) -> list[dict]:
    out = []
    for chapter in db.units_by_subject(grade_id).get(subject_id, []):
        for unit in chapter.get("units") or []:
            for section in unit.get("sections") or []:
                out.append({
                    "chapter_id": chapter["id"],
                    "chapter_title_zh": chapter.get("title_zh"),
                    "chapter_title_en": chapter.get("title_en"),
                    "section_id": section["id"],
                    "title_zh": section.get("title_zh"),
                    "title_en": section.get("title_en"),
                    "knowledge_id": section.get("knowledge_id") or f"kp-{section['id']}",
                })
    return out


def _prefer(rows: list[dict]) -> dict | None:
    rank = {"basic": 0, "exam": 1, "challenge": 2}
    ranked = [r for r in rows if r.get("difficulty") != "unit"]
    if not ranked:
        return None
    ranked.sort(key=lambda r: rank.get(r.get("difficulty") or "exam", 1))
    return ranked[0]


def diagnostic_questions(subject_id: str, grade_id: str, limit: int = 8) -> list[dict]:
    sections = _sections(subject_id, grade_id)
    questions = db.list_questions(subject_id, grade_id=grade_id)
    by_section: dict[str, list] = {}
    for q in questions:
        if str(q.get("grade_id") or "") not in ("", str(grade_id)):
            continue
        by_section.setdefault(q.get("section_id") or "", []).append(q)
    chosen = []
    used = set()

    def take(meta):
        if meta["section_id"] in used:
            return
        picked = _prefer(by_section.get(meta["section_id"]) or [])
        if not picked:
            return
        used.add(meta["section_id"])
        public = db.public_question(picked, reveal=False)
        public.update({
            "chapter_id": meta["chapter_id"],
            "chapter_title_zh": meta["chapter_title_zh"],
            "chapter_title_en": meta["chapter_title_en"],
            "section_id": meta["section_id"],
            "section_title_zh": meta["title_zh"],
            "section_title_en": meta["title_en"],
            "knowledge_id": meta["knowledge_id"],
        })
        chosen.append(public)

    seen_chapter = set()
    for meta in sections:
        if meta["chapter_id"] in seen_chapter:
            continue
        seen_chapter.add(meta["chapter_id"])
        take(meta)
    for meta in sections:
        if len(chosen) >= limit:
            break
        take(meta)
    return chosen[:limit]


def _status(correct: bool, understood: bool) -> str:
    if not correct:
        return "gap"
    if not understood:
        return "shaky"
    return "solid"


def grade_placement(subject_id: str, grade_id: str, answers: dict) -> dict:
    sections = _sections(subject_id, grade_id)
    items = []
    by_section: dict[str, str] = {}
    for qid, payload in (answers or {}).items():
        q = db.get_question(qid)
        if not q or q.get("subject_id") != subject_id:
            continue
        given = payload.get("answer") if isinstance(payload, dict) else payload
        reasoning = payload.get("reasoning") if isinstance(payload, dict) else ""
        correct = check_answer(q, given)
        understood = reasoning_ok(q, reasoning) if correct else False
        if not correct and given not in (None, ""):
            db.record_mistake(q, given)
        status = _status(correct, understood)
        prev = by_section.get(q.get("section_id") or "")
        if prev is None or {"gap": 0, "shaky": 1, "solid": 2}[status] < {"gap": 0, "shaky": 1, "solid": 2}[prev]:
            by_section[q.get("section_id") or ""] = status
        items.append({
            "question_id": qid,
            "section_id": q.get("section_id"),
            "chapter_id": q.get("chapter_id"),
            "correct": correct,
            "reasoning_ok": understood,
            "status": status,
        })
    full = [{**meta, "status": by_section.get(meta["section_id"], "unseen")} for meta in sections]
    asked = [row for row in full if row["status"] != "unseen"]
    gaps = [row for row in full if row["status"] == "gap"]
    shaky = [row for row in full if row["status"] == "shaky"]
    unseen = [row for row in full if row["status"] == "unseen"]
    start = (gaps or shaky or unseen or [None])[0]
    path = (gaps + shaky + unseen[:2])[:6]
    result = {
        "subject_id": subject_id,
        "grade_id": str(grade_id),
        "at": db.now_iso(),
        "items": items,
        "sections": asked,
        "start": start,
        "path": path,
        "ready": not gaps and not shaky and not unseen,
    }
    db.set_learning(f"placement:{grade_id}:{subject_id}", result)
    return result


def get_placement(subject_id: str, grade_id: str) -> dict | None:
    return db.get_learning(f"placement:{grade_id}:{subject_id}")


def note_checkpoint(subject_id: str, grade_id: str, scope: str) -> None:
    if scope not in ("unit", "course"):
        return
    db.set_learning(f"checkpoint:{grade_id}:{subject_id}", {"at": db.now_iso(), "scope": scope})


def _ms(value: str | None) -> float:
    if not value:
        return 0
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp() * 1000
    except ValueError:
        return 0


def spiral_status(subject_id: str, grade_id: str) -> dict:
    placement = get_placement(subject_id, grade_id) or {}
    mistakes = db.list_mistakes(subject_id, status="open")
    weak = any(s.get("status") in ("gap", "shaky") for s in placement.get("sections") or []) or len(mistakes) > 0
    review = db.get_learning(f"spiral:{grade_id}:{subject_id}") or {}
    checkpoint = db.get_learning(f"checkpoint:{grade_id}:{subject_id}") or {}
    now = datetime.now(timezone.utc).timestamp() * 1000
    last = _ms(review.get("at"))
    check = _ms(checkpoint.get("at"))
    if not weak:
        state = {"due": False, "reason": "steady", "days": None}
    elif not last:
        state = {"due": True, "reason": "first", "days": 0}
    elif check > last:
        state = {"due": True, "reason": "unit", "days": 0}
    elif now - last >= FORTNIGHT_MS:
        state = {"due": True, "reason": "fortnight", "days": 0}
    else:
        days = max(1, int((FORTNIGHT_MS - (now - last)) / (24 * 3600 * 1000) + 0.999))
        state = {"due": False, "reason": "waiting", "days": days}
    questions = _spiral_questions(subject_id, grade_id, placement, mistakes)
    state.update({
        "subject_id": subject_id,
        "grade_id": str(grade_id),
        "weak_count": len(mistakes) + sum(1 for s in placement.get("sections") or [] if s.get("status") in ("gap", "shaky")),
        "questions": [db.public_question(q, reveal=False) for q in questions],
    })
    return state


def _spiral_questions(subject_id: str, grade_id: str, placement: dict, mistakes: list[dict]) -> list[dict]:
    pool = [q for q in db.list_questions(subject_id, grade_id=grade_id) if str(q.get("grade_id") or grade_id) == str(grade_id)]
    by_id = {q["id"]: q for q in pool}
    chosen = []
    used = set()

    def push(q):
        if not q or q["id"] in used or len(chosen) >= 6:
            return
        used.add(q["id"])
        chosen.append(q)

    for mistake in mistakes:
        push(by_id.get(mistake.get("question_id")))
    weak_sections = {s.get("section_id") for s in placement.get("sections") or [] if s.get("status") in ("gap", "shaky")}
    for q in pool:
        if q.get("section_id") in weak_sections and q.get("difficulty") in ("basic", "exam", None, ""):
            push(q)
    for q in pool:
        if q.get("difficulty") in ("basic", "exam"):
            push(q)
    return chosen[:6]


def complete_spiral(subject_id: str, grade_id: str) -> dict:
    payload = {"at": db.now_iso(), "subject_id": subject_id, "grade_id": str(grade_id)}
    db.set_learning(f"spiral:{grade_id}:{subject_id}", payload)
    return payload
