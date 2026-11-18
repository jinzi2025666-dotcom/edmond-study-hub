from __future__ import annotations

import json
import re
from fractions import Fraction

_ARROW = re.compile(r"(→|⇒|➜|➞|->|=>)")
_SPACE_AROUND_OP = re.compile(r"\s*([+\-/=×*])\s*")
_MULTI_SPACE = re.compile(r"\s+")
_PUNCT_EDGE = re.compile(r"^[\s\"'“”‘’.;:：。、，]+|[\s\"'“”‘’.;:：。、，]+$")


def normalize_text(value: str) -> str:
    s = str(value or "").strip()
    s = s.replace("＋", "+").replace("－", "-").replace("＝", "=")
    s = s.replace("，", ",").replace("。", ".")
    s = _ARROW.sub("->", s)
    s = _MULTI_SPACE.sub(" ", s)
    s = s.lower()
    s = _PUNCT_EDGE.sub("", s)
    s = _SPACE_AROUND_OP.sub(r"\1", s)
    return s


def _try_number(value: str) -> float | None:
    s = str(value or "").strip()
    if not s:
        return None
    s = s.replace("，", "").replace(",", "")
    s = s.replace("−", "-")
    s = re.sub(r"\s+", "", s)
    if s.endswith("%"):
        return None
    try:
        if s.count("/") == 1:
            a, b = s.split("/")
            if a and b and b not in {"0", "-0"}:
                return float(Fraction(a) / Fraction(b))
        return float(Fraction(s)) if re.fullmatch(r"[+-]?\d+(\.\d+)?", s) else float(s)
    except (ValueError, ZeroDivisionError):
        try:
            return float(s)
        except ValueError:
            return None


def numbers_equal(given: float, expected: float, tolerance: float | None) -> bool:
    tol = 1e-6 if tolerance is None else float(tolerance)
    if abs(given - expected) <= tol:
        return True
    scale = max(1.0, abs(expected))
    return abs(given - expected) <= max(tol, 1e-4 * scale)


def accepted_values(question: dict) -> list[str]:
    values: list[str] = []
    for key in ("answer", "answer_zh", "answer_en"):
        val = question.get(key)
        if val is not None and str(val).strip() != "":
            values.append(str(val))
    extra = question.get("accepted") or []
    if isinstance(extra, str):
        extra = [extra]
    values.extend(str(x) for x in extra if x is not None and str(x).strip() != "")
    # unique, keep order
    seen = set()
    out = []
    for v in values:
        if v not in seen:
            seen.add(v)
            out.append(v)
    return out


def keyword_list(question: dict) -> list[str]:
    raw = question.get("keywords") or []
    if isinstance(raw, str):
        raw = raw.strip()
        if not raw:
            return []
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            return [raw]
        if parsed is None:
            return []
        raw = parsed
    if not isinstance(raw, (list, tuple)):
        return []
    return [str(k) for k in raw if k is not None and str(k).strip()]


def keywords_match(question: dict, given) -> bool | None:
    """Extended answers: full marks when enough key phrases appear.

    Returns None when the question has no keyword list, so short answers
    keep exact matching.
    """
    keys = keyword_list(question)
    if not keys:
        return None
    text = normalize_text(given)
    if not text:
        return False
    hits = sum(1 for key in keys if normalize_text(key) and normalize_text(key) in text)
    need = question.get("keyword_min")
    if need is None or need == "":
        need = max(1, (len(keys) + 1) // 2)
    try:
        need_n = int(need)
    except (TypeError, ValueError):
        need_n = max(1, (len(keys) + 1) // 2)
    return hits >= max(1, need_n)


def check_answer(question: dict, given) -> bool:
    typ = (question.get("type") or "short").lower()
    raw = "" if given is None else str(given)
    if typ == "mcq":
        return raw.strip().lower() == str(question.get("answer") or "").strip().lower()

    kw = keywords_match(question, raw)
    if kw is not None:
        return kw

    if typ == "numeric":
        got = _try_number(raw)
        if got is None:
            # fall back to text match, e.g. "1/3"
            ng = normalize_text(raw)
            return any(normalize_text(v) == ng for v in accepted_values(question))
        tol = question.get("tolerance")
        for v in accepted_values(question):
            exp = _try_number(v)
            if exp is not None and numbers_equal(got, exp, tol):
                return True
            if normalize_text(raw) == normalize_text(v):
                return True
        return False

    # short / structured
    ng = normalize_text(raw)
    if not ng:
        return False
    return any(normalize_text(v) == ng for v in accepted_values(question))
