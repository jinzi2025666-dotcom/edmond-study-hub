from __future__ import annotations

import json
import sqlite3
import threading
from contextlib import contextmanager
from datetime import datetime, timezone, timedelta
from pathlib import Path

from .config import CURRICULUM_DIR, DATA_DIR, USER_DB, load_json

SEED_VERSION = "3"
SHANGHAI = timezone(timedelta(hours=8))
_local = threading.local()


def now_iso() -> str:
    return datetime.now(SHANGHAI).replace(microsecond=0).isoformat()


def connect() -> sqlite3.Connection:
    conn = getattr(_local, "conn", None)
    if conn is not None:
        return conn
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(USER_DB, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    _local.conn = conn
    return conn


@contextmanager
def cursor():
    con = connect()
    cur = con.cursor()
    try:
        yield cur
        con.commit()
    except Exception:
        con.rollback()
        raise


def row_to_dict(row) -> dict | None:
    if row is None:
        return None
    return {k: row[k] for k in row.keys()}


def decode_json_fields(item: dict | None, fields: tuple[str, ...]) -> dict | None:
    if not item:
        return None
    out = dict(item)
    for f in fields:
        val = out.get(f)
        if isinstance(val, str) and val != "":
            try:
                out[f] = json.loads(val)
            except json.JSONDecodeError:
                pass
    return out


def init_db() -> None:
    with cursor() as cur:
        cur.executescript(
            """
            CREATE TABLE IF NOT EXISTS knowledge (
              id TEXT PRIMARY KEY,
              subject_id TEXT NOT NULL,
              unit_id TEXT,
              topic_id TEXT,
              title_zh TEXT,
              title_en TEXT,
              summary_zh TEXT,
              summary_en TEXT,
              body_zh TEXT,
              body_en TEXT,
              related_question_ids TEXT,
              published_at TEXT,
              created_at TEXT,
              updated_at TEXT,
              origin TEXT
            );
            CREATE TABLE IF NOT EXISTS questions (
              id TEXT PRIMARY KEY,
              subject_id TEXT NOT NULL,
              unit_id TEXT,
              knowledge_id TEXT,
              type TEXT NOT NULL,
              stem_zh TEXT,
              stem_en TEXT,
              options TEXT,
              answer TEXT,
              accepted TEXT,
              tolerance REAL,
              answer_zh TEXT,
              answer_en TEXT,
              explanation_zh TEXT,
              explanation_en TEXT,
              marks INTEGER DEFAULT 1,
              published_at TEXT,
              created_at TEXT,
              updated_at TEXT,
              origin TEXT
            );
            CREATE TABLE IF NOT EXISTS question_sets (
              id TEXT PRIMARY KEY,
              subject_id TEXT NOT NULL,
              unit_id TEXT,
              kind TEXT NOT NULL,
              title_zh TEXT,
              title_en TEXT,
              question_ids TEXT,
              time_limit_minutes INTEGER,
              published_at TEXT,
              created_at TEXT,
              updated_at TEXT,
              origin TEXT
            );
            CREATE TABLE IF NOT EXISTS knowledge_progress (
              knowledge_id TEXT PRIMARY KEY,
              status TEXT NOT NULL,
              updated_at TEXT
            );
            CREATE TABLE IF NOT EXISTS mistakes (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              question_id TEXT NOT NULL UNIQUE,
              subject_id TEXT,
              given_answer TEXT,
              created_at TEXT,
              updated_at TEXT,
              status TEXT NOT NULL DEFAULT 'open'
            );
            CREATE TABLE IF NOT EXISTS attempts (
              id TEXT PRIMARY KEY,
              set_id TEXT,
              kind TEXT,
              subject_id TEXT,
              started_at TEXT,
              submitted_at TEXT,
              time_limit_minutes INTEGER,
              score INTEGER,
              max_score INTEGER,
              answers TEXT
            );
            CREATE TABLE IF NOT EXISTS activity (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              kind TEXT,
              ref_id TEXT,
              at TEXT
            );
            CREATE TABLE IF NOT EXISTS meta (
              key TEXT PRIMARY KEY,
              value TEXT
            );
            CREATE INDEX IF NOT EXISTS idx_knowledge_subject ON knowledge(subject_id);
            CREATE INDEX IF NOT EXISTS idx_questions_subject ON questions(subject_id);
            CREATE INDEX IF NOT EXISTS idx_sets_subject ON question_sets(subject_id, kind);
            CREATE INDEX IF NOT EXISTS idx_mistakes_status ON mistakes(status, subject_id);
            """
        )
        _ensure_columns(cur)
        cur.execute("CREATE INDEX IF NOT EXISTS idx_knowledge_grade ON knowledge(grade_id)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_questions_grade ON questions(grade_id)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_sets_grade ON question_sets(grade_id)")
    seed_if_needed()


def _table_columns(cur, table: str) -> set[str]:
    return {r[1] for r in cur.execute(f"PRAGMA table_info({table})").fetchall()}


def _ensure_columns(cur) -> None:
    extras = {
        "knowledge": [
            ("grade_id", "TEXT"),
            ("chapter_id", "TEXT"),
            ("section_id", "TEXT"),
            ("objectives_zh", "TEXT"),
            ("objectives_en", "TEXT"),
            ("keypoints_zh", "TEXT"),
            ("keypoints_en", "TEXT"),
            ("difficulties_zh", "TEXT"),
            ("difficulties_en", "TEXT"),
            ("diagram", "TEXT"),
            ("developed", "INTEGER"),
        ],
        "questions": [
            ("grade_id", "TEXT"),
            ("chapter_id", "TEXT"),
            ("section_id", "TEXT"),
        ],
        "question_sets": [
            ("grade_id", "TEXT"),
            ("chapter_id", "TEXT"),
            ("scope", "TEXT"),
        ],
    }
    for table, cols in extras.items():
        existing = _table_columns(cur, table)
        for name, typ in cols:
            if name not in existing:
                cur.execute(f"ALTER TABLE {table} ADD COLUMN {name} {typ}")


def seed_if_needed() -> None:
    content_path = CURRICULUM_DIR / "content.json"
    if not content_path.is_file():
        raise FileNotFoundError(f"Missing {content_path}. Run data/curriculum/build_content.py")
    content = load_json("content.json")
    ts = now_iso()
    with cursor() as cur:
        row = cur.execute("SELECT value FROM meta WHERE key = 'seed_version'").fetchone()
        current = row["value"] if row else None
        if current != SEED_VERSION:
            for sid in (
                "chinese", "mathematics", "english", "computer-science",
                "economics", "physics", "chemistry", "biology",
            ):
                cur.execute("DELETE FROM knowledge WHERE origin = 'seed' AND subject_id = ?", (sid,))
                cur.execute("DELETE FROM questions WHERE origin = 'seed' AND subject_id = ?", (sid,))
                cur.execute("DELETE FROM question_sets WHERE origin = 'seed' AND subject_id = ?", (sid,))
            for obsolete in (
                "kp-physics-speed",
                "kp-physics-reflection",
                "practice-physics-motion-light",
                "paper-physics-a",
            ):
                cur.execute("DELETE FROM knowledge WHERE id = ?", (obsolete,))
                cur.execute("DELETE FROM questions WHERE id = ?", (obsolete,))
                cur.execute("DELETE FROM question_sets WHERE id = ?", (obsolete,))

        def insert_many(table: str, rows: list[dict], columns: list[str], json_fields: set[str]):
            placeholders = ",".join("?" * len(columns))
            cols = ",".join(columns)
            for row in rows:
                values = []
                for col in columns:
                    val = row.get(col)
                    if col in json_fields:
                        val = json.dumps(val if val is not None else ([] if col.endswith("ids") or col in {"options", "accepted"} else val), ensure_ascii=False)
                    if col in {"created_at", "updated_at"} and not val:
                        val = ts
                    if col == "origin" and not val:
                        val = "seed"
                    if col == "published_at" and not val:
                        val = ts
                    values.append(val)
                cur.execute(
                    f"INSERT OR IGNORE INTO {table} ({cols}) VALUES ({placeholders})",
                    values,
                )

        insert_many(
            "knowledge",
            content.get("knowledge") or [],
            KNOWLEDGE_COLS,
            {"related_question_ids"},
        )
        qrows = []
        for q in content.get("questions") or []:
            item = dict(q)
            if not isinstance(item.get("answer"), str):
                item["answer"] = json.dumps(item.get("answer"), ensure_ascii=False) if item.get("answer") is not None else ""
            qrows.append(item)
        insert_many(
            "questions",
            qrows,
            QUESTION_COLS,
            {"options", "accepted"},
        )
        insert_many(
            "question_sets",
            content.get("sets") or [],
            SET_COLS,
            {"question_ids"},
        )
        for table in ("knowledge", "questions", "question_sets"):
            cur.execute(f"UPDATE {table} SET grade_id = '8' WHERE grade_id IS NULL OR grade_id = ''")
        cur.execute(
            "INSERT OR REPLACE INTO meta(key, value) VALUES ('seed_version', ?)",
            (SEED_VERSION,),
        )


def load_subjects() -> list[dict]:
    return load_json("subjects.json")


def load_grades() -> list[dict]:
    path = CURRICULUM_DIR / "grades.json"
    if not path.is_file():
        return []
    return load_json("grades.json")


def load_units() -> list[dict]:
    return load_json("units.json")


def units_by_subject(grade_id: str | None = None) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {}
    for unit in load_units():
        if grade_id and str(unit.get("grade_id") or "8") != str(grade_id):
            continue
        grouped.setdefault(unit["subject_id"], []).append(unit)
    for sid in grouped:
        grouped[sid].sort(key=lambda u: u.get("order") or 0)
    return grouped


def load_coding_exercises() -> list[dict]:
    content = load_json("content.json")
    return content.get("coding_exercises") or []


def get_knowledge(kid: str) -> dict | None:
    cur = connect().execute("SELECT * FROM knowledge WHERE id = ?", (kid,))
    return decode_json_fields(row_to_dict(cur.fetchone()), ("related_question_ids",))


def list_knowledge(subject_id: str | None = None, unit_id: str | None = None, grade_id: str | None = None) -> list[dict]:
    sql = "SELECT * FROM knowledge"
    args: list = []
    clauses = []
    if subject_id:
        clauses.append("subject_id = ?")
        args.append(subject_id)
    if unit_id:
        clauses.append("(unit_id = ? OR chapter_id = ? OR section_id = ?)")
        args.extend([unit_id, unit_id, unit_id])
    if grade_id:
        clauses.append("(grade_id = ? OR grade_id IS NULL OR grade_id = '')")
        args.append(grade_id)
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)
    sql += " ORDER BY published_at DESC, title_en COLLATE NOCASE"
    rows = connect().execute(sql, args).fetchall()
    return [decode_json_fields(row_to_dict(r), ("related_question_ids",)) for r in rows]


def get_question(qid: str) -> dict | None:
    cur = connect().execute("SELECT * FROM questions WHERE id = ?", (qid,))
    return decode_json_fields(row_to_dict(cur.fetchone()), ("options", "accepted"))


def list_questions(subject_id: str | None = None, unit_id: str | None = None) -> list[dict]:
    sql = "SELECT * FROM questions"
    args: list = []
    clauses = []
    if subject_id:
        clauses.append("subject_id = ?")
        args.append(subject_id)
    if unit_id:
        clauses.append("unit_id = ?")
        args.append(unit_id)
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)
    sql += " ORDER BY published_at DESC"
    rows = connect().execute(sql, args).fetchall()
    return [decode_json_fields(row_to_dict(r), ("options", "accepted")) for r in rows]


def get_set(sid: str) -> dict | None:
    cur = connect().execute("SELECT * FROM question_sets WHERE id = ?", (sid,))
    return decode_json_fields(row_to_dict(cur.fetchone()), ("question_ids",))


def list_sets(subject_id: str | None = None, kind: str | None = None, grade_id: str | None = None) -> list[dict]:
    sql = "SELECT * FROM question_sets"
    args: list = []
    clauses = []
    if subject_id:
        clauses.append("subject_id = ?")
        args.append(subject_id)
    if kind:
        clauses.append("kind = ?")
        args.append(kind)
    if grade_id:
        clauses.append("(grade_id = ? OR grade_id IS NULL OR grade_id = '')")
        args.append(grade_id)
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)
    sql += " ORDER BY published_at DESC"
    rows = connect().execute(sql, args).fetchall()
    return [decode_json_fields(row_to_dict(r), ("question_ids",)) for r in rows]


def public_question(q: dict, reveal: bool = False) -> dict:
    item = dict(q)
    if not reveal:
        for key in ("answer", "accepted", "answer_zh", "answer_en", "explanation_zh", "explanation_en"):
            item.pop(key, None)
        item.pop("tolerance", None)
    return item


def progress_map() -> dict[str, str]:
    rows = connect().execute("SELECT knowledge_id, status FROM knowledge_progress").fetchall()
    return {r["knowledge_id"]: r["status"] for r in rows}


def set_knowledge_status(kid: str, status: str) -> None:
    if status not in {"learning", "mastered", "not_started"}:
        raise ValueError("invalid status")
    with cursor() as cur:
        if status == "not_started":
            cur.execute("DELETE FROM knowledge_progress WHERE knowledge_id = ?", (kid,))
            return
        cur.execute(
            """
            INSERT INTO knowledge_progress(knowledge_id, status, updated_at)
            VALUES (?, ?, ?)
            ON CONFLICT(knowledge_id) DO UPDATE SET status=excluded.status, updated_at=excluded.updated_at
            """,
            (kid, status, now_iso()),
        )


def record_activity(kind: str, ref_id: str) -> None:
    with cursor() as cur:
        cur.execute(
            "INSERT INTO activity(kind, ref_id, at) VALUES (?, ?, ?)",
            (kind, ref_id, now_iso()),
        )


def last_viewed_knowledge() -> dict | None:
    row = connect().execute(
        "SELECT ref_id FROM activity WHERE kind = 'view_knowledge' ORDER BY at DESC LIMIT 1"
    ).fetchone()
    if not row:
        return None
    return get_knowledge(row["ref_id"])


def record_mistake(question: dict, given) -> None:
    with cursor() as cur:
        cur.execute(
            """
            INSERT INTO mistakes(question_id, subject_id, given_answer, created_at, updated_at, status)
            VALUES (?, ?, ?, ?, ?, 'open')
            ON CONFLICT(question_id) DO UPDATE SET
              given_answer=excluded.given_answer,
              updated_at=excluded.updated_at,
              status='open'
            """,
            (question["id"], question.get("subject_id"), "" if given is None else str(given), now_iso(), now_iso()),
        )


def list_mistakes(subject_id: str | None = None, status: str | None = "open") -> list[dict]:
    sql = "SELECT * FROM mistakes"
    args: list = []
    clauses = []
    if subject_id:
        clauses.append("subject_id = ?")
        args.append(subject_id)
    if status and status != "all":
        clauses.append("status = ?")
        args.append(status)
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)
    sql += " ORDER BY updated_at DESC"
    rows = [row_to_dict(r) for r in connect().execute(sql, args).fetchall()]
    out = []
    for m in rows:
        q = get_question(m["question_id"])
        m["question"] = public_question(q, reveal=False) if q else None
        out.append(m)
    return out


def master_mistake(question_id: str) -> bool:
    with cursor() as cur:
        cur.execute(
            "UPDATE mistakes SET status='mastered', updated_at=? WHERE question_id=?",
            (now_iso(), question_id),
        )
        return cur.rowcount > 0


def save_attempt(attempt: dict) -> None:
    with cursor() as cur:
        cur.execute(
            """
            INSERT INTO attempts(id, set_id, kind, subject_id, started_at, submitted_at,
              time_limit_minutes, score, max_score, answers)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                attempt["id"], attempt.get("set_id"), attempt.get("kind"), attempt.get("subject_id"),
                attempt.get("started_at"), attempt.get("submitted_at"), attempt.get("time_limit_minutes"),
                attempt.get("score"), attempt.get("max_score"),
                json.dumps(attempt.get("answers") or {}, ensure_ascii=False),
            ),
        )


def get_attempt(aid: str) -> dict | None:
    row = row_to_dict(connect().execute("SELECT * FROM attempts WHERE id=?", (aid,)).fetchone())
    return decode_json_fields(row, ("answers",))


def list_attempts(subject_id: str | None = None, limit: int = 50) -> list[dict]:
    sql = "SELECT * FROM attempts"
    args: list = []
    if subject_id:
        sql += " WHERE subject_id = ?"
        args.append(subject_id)
    sql += " ORDER BY submitted_at DESC LIMIT ?"
    args.append(limit)
    return [decode_json_fields(row_to_dict(r), ("answers",)) for r in connect().execute(sql, args).fetchall()]


def upsert_row(table: str, item: dict, columns: list[str], json_fields: set[str]) -> None:
    ts = now_iso()
    item = dict(item)
    item.setdefault("created_at", ts)
    item["updated_at"] = ts
    item.setdefault("origin", "user")
    if not item.get("published_at"):
        item["published_at"] = ts
    placeholders = ",".join("?" * len(columns))
    cols = ",".join(columns)
    updates = ",".join(f"{c}=excluded.{c}" for c in columns if c != "id")
    values = []
    for col in columns:
        val = item.get(col)
        if col in json_fields:
            val = json.dumps(val if val is not None else [], ensure_ascii=False)
        values.append(val)
    with cursor() as cur:
        cur.execute(
            f"INSERT INTO {table} ({cols}) VALUES ({placeholders}) ON CONFLICT(id) DO UPDATE SET {updates}",
            values,
        )


def delete_row(table: str, item_id: str) -> bool:
    with cursor() as cur:
        cur.execute(f"DELETE FROM {table} WHERE id=?", (item_id,))
        return cur.rowcount > 0


KNOWLEDGE_COLS = [
    "id", "subject_id", "unit_id", "topic_id", "title_zh", "title_en",
    "summary_zh", "summary_en", "body_zh", "body_en",
    "related_question_ids", "published_at", "created_at", "updated_at", "origin",
    "grade_id", "chapter_id", "section_id",
    "objectives_zh", "objectives_en", "keypoints_zh", "keypoints_en",
    "difficulties_zh", "difficulties_en", "diagram", "developed",
]
QUESTION_COLS = [
    "id", "subject_id", "unit_id", "knowledge_id", "type", "stem_zh", "stem_en",
    "options", "answer", "accepted", "tolerance", "answer_zh", "answer_en",
    "explanation_zh", "explanation_en", "marks", "published_at",
    "created_at", "updated_at", "origin",
    "grade_id", "chapter_id", "section_id",
]
SET_COLS = [
    "id", "subject_id", "unit_id", "kind", "title_zh", "title_en",
    "question_ids", "time_limit_minutes", "published_at",
    "created_at", "updated_at", "origin",
    "grade_id", "chapter_id", "scope",
]
