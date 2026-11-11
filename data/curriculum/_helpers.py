"""Shared builders for bilingual seed content."""

def opts(*pairs):
    out = []
    for i, (zh, en) in enumerate(pairs):
        out.append({"id": "abcd"[i], "zh": zh, "en": en})
    return out


def Q(qid, subject, unit, typ, stem_zh, stem_en, answer, exp_zh, exp_en,
      options=None, knowledge_id=None, marks=1, published_at=None,
      accepted=None, tolerance=None, answer_zh=None, answer_en=None):
    item = {
        "id": qid,
        "subject_id": subject,
        "unit_id": unit,
        "knowledge_id": knowledge_id,
        "type": typ,
        "stem_zh": stem_zh,
        "stem_en": stem_en,
        "answer": answer,
        "explanation_zh": exp_zh,
        "explanation_en": exp_en,
        "marks": marks,
        "published_at": published_at or "2026-10-20T09:00:00+08:00",
    }
    if options:
        item["options"] = options
    if accepted:
        item["accepted"] = accepted
    if tolerance is not None:
        item["tolerance"] = tolerance
    if answer_zh:
        item["answer_zh"] = answer_zh
    if answer_en:
        item["answer_en"] = answer_en
    return item


def KP(kid, subject, unit, topic, title_zh, title_en, body_zh, body_en,
       related, published_at, summary_zh=None, summary_en=None):
    return {
        "id": kid,
        "subject_id": subject,
        "unit_id": unit,
        "topic_id": topic,
        "title_zh": title_zh,
        "title_en": title_en,
        "summary_zh": summary_zh or "",
        "summary_en": summary_en or "",
        "body_zh": body_zh.strip(),
        "body_en": body_en.strip(),
        "related_question_ids": related,
        "published_at": published_at,
    }


def SET(sid, subject, unit, kind, title_zh, title_en, qids,
        time_limit=None, published_at=None):
    return {
        "id": sid,
        "subject_id": subject,
        "unit_id": unit,
        "kind": kind,  # practice | paper
        "title_zh": title_zh,
        "title_en": title_en,
        "question_ids": qids,
        "time_limit_minutes": time_limit,
        "published_at": published_at or "2026-10-20T09:00:00+08:00",
    }
