#!/usr/bin/env python3
"""Compile subject modules into content.json (knowledge, questions, sets, coding)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _content_chinese import knowledge_cn, questions_cn, sets_cn
from _content_english import knowledge_en, questions_en, sets_en
from _content_mathematics import knowledge_ma, questions_ma, sets_ma
from _content_chemistry import knowledge_ch, questions_ch, sets_ch
from _content_biology import knowledge_bi, questions_bi, sets_bi
from _content_physics import knowledge as knowledge_ph, questions as questions_ph, sets as sets_ph
from _content_computing import knowledge_cs, questions_cs, sets_cs, coding_exercises
from _content_economics import knowledge_ec, questions_ec, sets_ec

knowledge = (
    knowledge_cn + knowledge_en + knowledge_ma + knowledge_ph
    + knowledge_ch + knowledge_bi + knowledge_cs + knowledge_ec
)
questions = (
    questions_cn + questions_en + questions_ma + questions_ph
    + questions_ch + questions_bi + questions_cs + questions_ec
)
sets = (
    sets_cn + sets_en + sets_ma + sets_ph
    + sets_ch + sets_bi + sets_cs + sets_ec
)

for row in knowledge + questions + sets:
    row.setdefault("grade_id", "8")

# uniqueness checks
for label, rows, key in (
    ("knowledge", knowledge, "id"),
    ("questions", questions, "id"),
    ("sets", sets, "id"),
):
    ids = [r[key] for r in rows]
    if len(ids) != len(set(ids)):
        dup = {i for i in ids if ids.count(i) > 1}
        raise SystemExit(f"Duplicate {label} ids: {dup}")

qids = {q["id"] for q in questions}
for kp in knowledge:
    missing = [i for i in kp["related_question_ids"] if i not in qids]
    if missing:
        raise SystemExit(f"{kp['id']} related ids missing: {missing}")
for s in sets:
    missing = [i for i in s["question_ids"] if i not in qids]
    if missing:
        raise SystemExit(f"{s['id']} question ids missing: {missing}")

payload = {
    "knowledge": knowledge,
    "questions": questions,
    "sets": sets,
    "coding_exercises": coding_exercises,
}
out = HERE / "content.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

from collections import Counter
print(f"Wrote {out}")
print(f"  knowledge: {len(knowledge)}")
print(f"  questions: {len(questions)}")
print(f"  sets: {len(sets)} (practice {sum(1 for s in sets if s['kind']=='practice')}, papers {sum(1 for s in sets if s['kind']=='paper')})")
print(f"  coding: {len(coding_exercises)}")
print("  knowledge by subject:", dict(Counter(k['subject_id'] for k in knowledge)))
print("  questions by subject:", dict(Counter(q['subject_id'] for q in questions)))
print("  physics lessons:", sum(1 for k in knowledge if k['subject_id']=='physics'))
print("  physics questions:", sum(1 for q in questions if q['subject_id']=='physics'))
print("  physics sets:", [s['id'] for s in sets if s['subject_id']=='physics'])
from collections import defaultdict
print("  ready-style subjects:")
for sid in ("chinese","mathematics","english","computer-science","economics","physics","chemistry","biology"):
    ks = sum(1 for k in knowledge if k['subject_id']==sid)
    qs = sum(1 for q in questions if q['subject_id']==sid)
    ss = [s['id'] for s in sets if s['subject_id']==sid]
    print(f"    {sid}: lessons={ks} questions={qs} sets={len(ss)}")
