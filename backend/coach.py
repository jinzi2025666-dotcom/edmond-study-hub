"""Coaching text for a wrong answer. Mirrors frontend/src/learning/coach.js enough for the API."""
from __future__ import annotations

import re

_SCHEME_ZH = re.compile(r"\*\*评分要点[\s\S]*?\*\*解析\*\*")
_SCHEME_EN = re.compile(r"\*\*Mark scheme[\s\S]*?\*\*Explanation\*\*")
_STOP = {
    "the", "a", "an", "of", "to", "and", "or", "in", "on", "for", "is", "are",
    "was", "were", "be", "this", "that", "with", "from", "by", "as", "it", "if",
    "的", "了", "是", "在", "和", "与", "或",
}


def _body(q: dict) -> str:
    raw = f"{q.get('explanation_zh') or ''}\n{q.get('explanation_en') or ''}"
    raw = _SCHEME_ZH.sub(" ", raw)
    raw = _SCHEME_EN.sub(" ", raw)
    return raw


def reasoning_keys(q: dict) -> list[str]:
    keys: list[str] = []
    if (q.get("type") or "") == "mcq":
        for opt in q.get("options") or []:
            if opt.get("id") == q.get("answer"):
                keys.extend([opt.get("zh") or "", opt.get("en") or ""])
    else:
        ans = str(q.get("answer") or "")
        if len(ans) > 1:
            keys.append(ans)
    for field in ("answer_zh", "answer_en"):
        if q.get(field):
            keys.append(str(q.get(field)))
    for word in re.split(r"[\s,.;:，。；：、!！?？()（）\[\]【】\"“”'’]+", _body(q)):
        w = word.strip()
        if len(w) >= 2 and w.lower() not in _STOP:
            keys.append(w)
    out = []
    seen = set()
    for key in keys:
        text = str(key).strip()
        if len(text) < 2 or text in seen:
            continue
        seen.add(text)
        out.append(text)
        if len(out) >= 24:
            break
    return out


def reasoning_ok(q: dict, reasoning) -> bool:
    text = str(reasoning or "").strip().lower()
    if len(text) < 8:
        return False
    return any(key.lower() in text for key in reasoning_keys(q))


def diagnose(q: dict, given) -> dict:
    typ = (q.get("type") or "short").lower()
    raw = "" if given is None else str(given).strip()
    if typ == "mcq":
        picked = next((o for o in (q.get("options") or []) if o.get("id") == raw), None)
        if not picked:
            return {
                "diagnosis_zh": "还没有一个能对上选项的答案。先把题目里的关键词圈出来。",
                "diagnosis_en": "There isn’t a clear option yet. Circle the key words in the question first.",
            }
        label = picked.get("en") or picked.get("zh") or raw
        return {
            "diagnosis_zh": f"你选了「{picked.get('zh') or label}」。这往往是把邻近概念当成了题目真正在问的那一件事。先分清题目问的是定义、方向还是计算。",
            "diagnosis_en": f"You chose “{label}”. That is often a neighbouring idea, not the thing the question actually asks. Separate definition, direction and calculation.",
        }
    if typ == "numeric":
        return {
            "diagnosis_zh": "数字还没对上。先写出公式，再代入，最后看单位。只写一个看起来眼熟的数，还不能说明方法是对的。",
            "diagnosis_en": "The number does not match yet. Write the formula, substitute, then check the unit. A familiar-looking number is not the same as a method.",
        }
    if typ == "structured":
        return {
            "diagnosis_zh": "长回答里要点还不够。评分看的是几个关键想法是否出现，不是篇幅。先列出两个必须写到的点，再展开。",
            "diagnosis_en": "The longer answer is still missing key points. Marks follow those points, not the length. Name two ideas that must appear, then develop them.",
        }
    return {
        "diagnosis_zh": "关键词还没对上。先用这节课的术语回答，不要换成一个相近但不相同的说法。",
        "diagnosis_en": "The key point is not there yet. Answer with the term from this lesson, not a nearby phrase.",
    }


def _method(q: dict, lang: str) -> str:
    typ = (q.get("type") or "short").lower()
    if lang == "zh":
        if typ == "mcq":
            return "再想一步：把每个选项翻译成这节课里的一个判断，再看哪一个判断和题目给出的条件方向一致。先不要选那个只是用了相同的词、但问的是另一件事的选项。"
        if typ == "numeric":
            return "再想一步：写出这一节的公式，代入题目里的每一个已知量，并检查单位是否一致。最后一步先不要报出数字。"
        if typ == "structured":
            return "再想一步：先列出两个必须出现的要点，每个要点用题干里的一个事实支撑。先不要写成完整范文。"
        return "再想一步：用这节课的术语回答，并指出题目里哪一个条件把你带到这个术语。先不要只重复题干。"
    if typ == "mcq":
        return "One step further: turn each option into a claim from this lesson, then see which claim matches the condition in the question."
    if typ == "numeric":
        return "One step further: write this lesson’s formula, substitute every given value, and check the units agree. Do not write the final number yet."
    if typ == "structured":
        return "One step further: name two points that must appear, and support each with one fact from the question."
    return "One step further: answer with the term from this lesson, and point to the condition that leads you there."


def hints_for(q: dict) -> dict:
    topic = q.get("title_zh") or q.get("section_id") or q.get("subject_id") or ""
    topic_en = q.get("title_en") or q.get("section_id") or q.get("subject_id") or ""
    return {
        "hint1_zh": f"先不要看解答。这题属于「{topic}」。把题目里的条件圈出来，问自己：它在考定义、公式，还是一个方向？",
        "hint1_en": f"Leave the solution closed. This item sits in “{topic_en}”. Circle the given information and ask whether it is a definition, a formula, or a direction.",
        "hint2_zh": _method(q, "zh"),
        "hint2_en": _method(q, "en"),
    }


def coach_payload(q: dict, given) -> dict:
    out = {}
    out.update(diagnose(q, given))
    out.update(hints_for(q))
    return out
