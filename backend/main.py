from __future__ import annotations

import re
import uuid
from datetime import datetime, timedelta
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from . import database as db
from .config import FRONTEND_DIST, load_site_config
from .grading import check_answer

app = FastAPI(title="Edmond Study Hub", docs_url=None, redoc_url=None)
_ISO_TAIL = re.compile(r"Z$")


@app.on_event("startup")
def _startup():
    db.init_db()


def parse_dt(value: str | None) -> datetime | None:
    if not value:
        return None
    text = _ISO_TAIL.sub("+00:00", value)
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=db.SHANGHAI)
    return dt


def within_days(value: str | None, days: int) -> bool:
    dt = parse_dt(value)
    if not dt:
        return False
    now = datetime.now(db.SHANGHAI)
    return dt >= now - timedelta(days=days)


def subject_or_404(subject_id: str) -> dict:
    for s in db.load_subjects():
        if s["id"] == subject_id:
            return s
    raise HTTPException(404, "Subject not found")


def attach_progress(knowledge: list[dict]) -> list[dict]:
    pmap = db.progress_map()
    out = []
    for item in knowledge:
        row = dict(item)
        row["status"] = pmap.get(item["id"], "not_started")
        out.append(row)
    return out


def counts_for_subject(subject_id: str, grade_id: str | None = None) -> dict:
    kps = attach_progress(db.list_knowledge(subject_id, grade_id=grade_id))
    mastered = sum(1 for k in kps if k["status"] == "mastered")
    learning = sum(1 for k in kps if k["status"] == "learning")
    return {
        "knowledge": len(kps),
        "mastered": mastered,
        "learning": learning,
        "questions": len(db.list_questions(subject_id)),
        "practice": len(db.list_sets(subject_id, "practice", grade_id=grade_id)),
        "papers": len(db.list_sets(subject_id, "paper", grade_id=grade_id)),
        "progress": (mastered / len(kps)) if kps else 0,
    }


@app.get("/api/health")
def health():
    return {"ok": True}


@app.get("/api/config")
def api_config():
    cfg = load_site_config()
    return {
        "name_en": cfg["name_en"],
        "name_zh": cfg["name_zh"],
        "subtitle_en": cfg["subtitle_en"],
        "subtitle_zh": cfg["subtitle_zh"],
        "subjects": db.load_subjects(),
        "grades": db.load_grades(),
    }


@app.get("/api/grades")
def api_grades():
    return db.load_grades()


@app.get("/api/subjects")
def api_subjects(grade: str | None = None):
    units = db.units_by_subject(grade)
    out = []
    for s in db.load_subjects():
        item = dict(s)
        item["units"] = units.get(s["id"], [])
        item["counts"] = counts_for_subject(s["id"], grade)
        dev = (s.get("development") or {})
        item["development_status"] = dev.get(str(grade or "8"), "upcoming")
        out.append(item)
    return out


@app.get("/api/subjects/{subject_id}")
def api_subject(subject_id: str, grade: str | None = None):
    subject = subject_or_404(subject_id)
    units = db.units_by_subject(grade).get(subject_id, [])
    knowledge = attach_progress(db.list_knowledge(subject_id, grade_id=grade))
    by_unit: dict[str, list] = {}
    for k in knowledge:
        by_unit.setdefault(k.get("unit_id") or "", []).append(k)
    unit_rows = []
    for unit in units:
        ups = by_unit.get(unit["id"], [])
        mastered = sum(1 for k in ups if k["status"] == "mastered")
        unit_rows.append({
            **unit,
            "knowledge_count": len(ups),
            "mastered": mastered,
            "progress": (mastered / len(ups)) if ups else 0,
        })
    return {
        "subject": subject,
        "units": unit_rows,
        "knowledge": knowledge,
        "practice": db.list_sets(subject_id, "practice", grade_id=grade),
        "papers": db.list_sets(subject_id, "paper", grade_id=grade),
        "counts": counts_for_subject(subject_id, grade),
        "grade_id": grade or "8",
        "development_status": (subject.get("development") or {}).get(str(grade or "8"), "upcoming"),
    }


@app.get("/api/knowledge")
def api_knowledge(subject: str | None = None, unit: str | None = None, grade: str | None = None):
    return attach_progress(db.list_knowledge(subject, unit, grade_id=grade))


@app.get("/api/knowledge/{kid}")
def api_knowledge_one(kid: str):
    item = db.get_knowledge(kid)
    if not item:
        raise HTTPException(404, "Knowledge point not found")
    db.record_activity("view_knowledge", kid)
    pmap = db.progress_map()
    item["status"] = pmap.get(kid, "not_started")
    related = []
    for qid in item.get("related_question_ids") or []:
        q = db.get_question(qid)
        if q:
            related.append(db.public_question(q, reveal=False))
    item["related_questions"] = related
    return item


@app.post("/api/knowledge/{kid}/status")
def api_knowledge_status(kid: str, payload: dict):
    if not db.get_knowledge(kid):
        raise HTTPException(404, "Knowledge point not found")
    status = (payload or {}).get("status") or "learning"
    try:
        db.set_knowledge_status(kid, status)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    if status == "learning":
        db.record_activity("view_knowledge", kid)
    return {"ok": True, "status": status}


@app.get("/api/sets")
def api_sets(subject: str | None = None, kind: str | None = None):
    return db.list_sets(subject, kind)


@app.get("/api/sets/{sid}")
def api_set(sid: str, reveal: bool = False):
    item = db.get_set(sid)
    if not item:
        raise HTTPException(404, "Set not found")
    questions = []
    for qid in item.get("question_ids") or []:
        q = db.get_question(qid)
        if q:
            questions.append(db.public_question(q, reveal=reveal))
    item["questions"] = questions
    item["marks"] = sum(int(q.get("marks") or 1) for q in questions)
    return item


@app.post("/api/check")
def api_check(payload: dict):
    qid = (payload or {}).get("question_id")
    given = (payload or {}).get("answer")
    q = db.get_question(qid) if qid else None
    if not q:
        raise HTTPException(404, "Question not found")
    correct = check_answer(q, given)
    if not correct:
        db.record_mistake(q, given)
    return {
        "correct": correct,
        "marks": int(q.get("marks") or 1),
        "awarded": int(q.get("marks") or 1) if correct else 0,
        "explanation_zh": q.get("explanation_zh"),
        "explanation_en": q.get("explanation_en"),
        "answer": q.get("answer"),
        "accepted": q.get("accepted") or [],
    }


def _grade_answers(question_ids: list[str], answers: dict) -> tuple[list[dict], int, int]:
    details = []
    score = 0
    maximum = 0
    for qid in question_ids:
        q = db.get_question(qid)
        if not q:
            continue
        marks = int(q.get("marks") or 1)
        maximum += marks
        given = answers.get(qid)
        if given is None and isinstance(answers, dict):
            # allow either raw map or already wrapped
            given = answers.get(str(qid))
        correct = check_answer(q, given)
        awarded = marks if correct else 0
        score += awarded
        if not correct and given not in (None, ""):
            db.record_mistake(q, given)
        details.append({
            "question_id": qid,
            "question": db.public_question(q, reveal=True),
            "given": given,
            "correct": correct,
            "marks": marks,
            "awarded": awarded,
        })
    return details, score, maximum


@app.post("/api/sets/{sid}/submit")
def api_submit(sid: str, payload: dict):
    item = db.get_set(sid)
    if not item:
        raise HTTPException(404, "Set not found")
    answers = (payload or {}).get("answers") or {}
    details, score, maximum = _grade_answers(item.get("question_ids") or [], answers)
    attempt = {
        "id": "att-" + uuid.uuid4().hex[:12],
        "set_id": sid,
        "kind": item.get("kind"),
        "subject_id": item.get("subject_id"),
        "started_at": (payload or {}).get("started_at"),
        "submitted_at": db.now_iso(),
        "time_limit_minutes": item.get("time_limit_minutes"),
        "score": score,
        "max_score": maximum,
        "answers": details,
    }
    db.save_attempt(attempt)
    return attempt


@app.get("/api/attempts")
def api_attempts(subject: str | None = None, limit: int = 50):
    rows = db.list_attempts(subject, limit)
    sets = {s["id"]: s for s in db.list_sets()}
    out = []
    for row in rows:
        item = dict(row)
        s = sets.get(row.get("set_id") or "")
        if s:
            item["set_title_zh"] = s.get("title_zh")
            item["set_title_en"] = s.get("title_en")
        out.append(item)
    return out


@app.get("/api/attempts/{aid}")
def api_attempt(aid: str):
    item = db.get_attempt(aid)
    if not item:
        raise HTTPException(404, "Attempt not found")
    s = db.get_set(item.get("set_id") or "")
    if s:
        item["set_title_zh"] = s.get("title_zh")
        item["set_title_en"] = s.get("title_en")
        item["kind"] = item.get("kind") or s.get("kind")
    return item


@app.get("/api/mistakes")
def api_mistakes(subject: str | None = None, status: str = "open"):
    return db.list_mistakes(subject, status)


@app.post("/api/mistakes/{question_id}/master")
def api_master_mistake(question_id: str):
    if not db.master_mistake(question_id):
        raise HTTPException(404, "Mistake not found")
    return {"ok": True}


@app.get("/api/progress")
def api_progress():
    subjects = []
    total_k = total_m = 0
    for s in db.load_subjects():
        counts = counts_for_subject(s["id"])
        total_k += counts["knowledge"]
        total_m += counts["mastered"]
        subjects.append({**s, "counts": counts})
    return {
        "subjects": subjects,
        "overall": {
            "knowledge": total_k,
            "mastered": total_m,
            "progress": (total_m / total_k) if total_k else 0,
        },
        "attempts": api_attempts(limit=20),
        "open_mistakes": len(db.list_mistakes(status="open")),
    }


@app.get("/api/continue")
def api_continue():
    last = db.last_viewed_knowledge()
    pmap = db.progress_map()
    if last:
        last = dict(last)
        last["status"] = pmap.get(last["id"], "not_started")
        if last["status"] != "mastered":
            return last
    # first not-mastered knowledge, preferring recently published
    for item in attach_progress(db.list_knowledge()):
        if item["status"] != "mastered":
            return item
    return last


@app.get("/api/updates")
def api_updates(days: int = 7):
    items = []
    for k in db.list_knowledge():
        if within_days(k.get("published_at") or k.get("updated_at"), days):
            items.append({
                "type": "knowledge",
                "id": k["id"],
                "subject_id": k["subject_id"],
                "title_zh": k.get("title_zh"),
                "title_en": k.get("title_en"),
                "published_at": k.get("published_at") or k.get("updated_at"),
            })
    for s in db.list_sets():
        if within_days(s.get("published_at") or s.get("updated_at"), days):
            items.append({
                "type": s.get("kind") or "set",
                "id": s["id"],
                "subject_id": s["subject_id"],
                "title_zh": s.get("title_zh"),
                "title_en": s.get("title_en"),
                "published_at": s.get("published_at") or s.get("updated_at"),
            })
    items.sort(key=lambda x: x.get("published_at") or "", reverse=True)
    return items


@app.get("/api/search")
def api_search(q: str = Query("", min_length=1)):
    needle = q.strip().lower()
    if not needle:
        return []
    results = []

    def hit(kind: str, item: dict, fields: list[str], href: str, subject_id: str):
        blob = " ".join(str(item.get(f) or "") for f in fields).lower()
        if needle not in blob:
            return
        # title preference
        title_zh = item.get("title_zh") or item.get("stem_zh") or ""
        title_en = item.get("title_en") or item.get("stem_en") or ""
        results.append({
            "type": kind,
            "id": item.get("id"),
            "subject_id": subject_id,
            "title_zh": title_zh,
            "title_en": title_en,
            "href": href,
        })

    for unit in db.load_units():
        topic_blob = " ".join(
            f"{(tp.get('title_zh') or '')} {(tp.get('title_en') or '')}"
            for tp in (unit.get("topics") or [])
        )
        searchable = dict(unit)
        searchable["_topics"] = topic_blob
        hit(
            "unit",
            searchable,
            ["title_zh", "title_en", "code", "note_zh", "note_en", "_topics"],
            f"/subjects/{unit['subject_id']}#{unit['id']}",
            unit["subject_id"],
        )

    for k in db.list_knowledge():
        hit(
            "knowledge", k,
            ["title_zh", "title_en", "summary_zh", "summary_en", "body_zh", "body_en"],
            f"/knowledge/{k['id']}", k["subject_id"],
        )
    for qu in db.list_questions():
        opt_text = []
        for opt in qu.get("options") or []:
            if isinstance(opt, dict):
                opt_text.extend([opt.get("zh") or "", opt.get("en") or ""])
        hit(
            "question", qu,
            ["stem_zh", "stem_en", *opt_text],
            f"/practice/question/{qu['id']}", qu["subject_id"],
        )
    return results[:40]


@app.get("/api/questions")
def api_questions(subject: str | None = None, unit: str | None = None, reveal: bool = False):
    return [db.public_question(q, reveal=reveal) for q in db.list_questions(subject, unit)]


@app.get("/api/questions/{qid}")
def api_question(qid: str, reveal: bool = False):
    q = db.get_question(qid)
    if not q:
        raise HTTPException(404, "Question not found")
    return db.public_question(q, reveal=reveal)


@app.get("/api/coding/exercises")
def api_coding():
    return db.load_coding_exercises()


# ----- admin (no auth in v1) -----
def _require_id(payload: dict, prefix: str) -> str:
    item_id = (payload.get("id") or "").strip()
    if not item_id:
        item_id = prefix + uuid.uuid4().hex[:10]
    payload["id"] = item_id
    return item_id


@app.post("/api/admin/knowledge")
def admin_save_knowledge(payload: dict):
    if not payload:
        raise HTTPException(400, "Empty payload")
    _require_id(payload, "kp-")
    if not payload.get("subject_id"):
        raise HTTPException(400, "subject_id is required")
    payload.setdefault("related_question_ids", payload.get("related_question_ids") or [])
    db.upsert_row("knowledge", payload, db.KNOWLEDGE_COLS, {"related_question_ids"})
    return db.get_knowledge(payload["id"])


@app.delete("/api/admin/knowledge/{kid}")
def admin_delete_knowledge(kid: str):
    if not db.delete_row("knowledge", kid):
        raise HTTPException(404, "Knowledge point not found")
    return {"ok": True}


@app.post("/api/admin/questions")
def admin_save_question(payload: dict):
    if not payload:
        raise HTTPException(400, "Empty payload")
    _require_id(payload, "q-")
    if not payload.get("subject_id"):
        raise HTTPException(400, "subject_id is required")
    payload.setdefault("type", "mcq")
    payload.setdefault("marks", 1)
    db.upsert_row("questions", payload, db.QUESTION_COLS, {"options", "accepted"})
    return db.get_question(payload["id"])


@app.delete("/api/admin/questions/{qid}")
def admin_delete_question(qid: str):
    if not db.delete_row("questions", qid):
        raise HTTPException(404, "Question not found")
    return {"ok": True}


@app.post("/api/admin/sets")
def admin_save_set(payload: dict):
    if not payload:
        raise HTTPException(400, "Empty payload")
    _require_id(payload, "set-")
    if not payload.get("subject_id"):
        raise HTTPException(400, "subject_id is required")
    payload.setdefault("kind", "practice")
    payload.setdefault("question_ids", payload.get("question_ids") or [])
    db.upsert_row("question_sets", payload, db.SET_COLS, {"question_ids"})
    return db.get_set(payload["id"])


@app.delete("/api/admin/sets/{sid}")
def admin_delete_set(sid: str):
    if not db.delete_row("question_sets", sid):
        raise HTTPException(404, "Set not found")
    return {"ok": True}


# ----- static SPA -----
if (FRONTEND_DIST / "assets").is_dir():
    app.mount("/assets", StaticFiles(directory=FRONTEND_DIST / "assets"), name="assets")


@app.get("/{full_path:path}")
async def spa(full_path: str):
    if full_path.startswith("api/"):
        return JSONResponse({"detail": "Not found"}, status_code=404)
    dist = FRONTEND_DIST
    if not (dist / "index.html").is_file():
        return JSONResponse(
            {"detail": "Frontend is not built yet. Run start.sh or npm run build in frontend/."},
            status_code=503,
        )
    candidate = dist / full_path
    if full_path and candidate.is_file():
        return FileResponse(candidate)
    return FileResponse(dist / "index.html")
