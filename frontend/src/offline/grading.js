// JS port of backend/grading.py — keep the two in sync.
export function normalizeText(value) {
  let s = String(value ?? "").trim();
  s = s.replace(/＋/g, "+").replace(/－/g, "-").replace(/＝/g, "=").replace(/，/g, ",").replace(/。/g, ".");
  s = s.replace(/(→|⇒|➜|➞|->|=>)/g, "->");
  s = s.replace(/\s+/g, " ").toLowerCase();
  s = s.replace(/^[\s"'“”‘’.;:：。、，]+|[\s"'“”‘’.;:：。、，]+$/g, "");
  s = s.replace(/\s*([+\-/=×*])\s*/g, "$1");
  return s;
}

export function tryNumber(value) {
  let s = String(value ?? "").trim();
  if (!s) return null;
  s = s.replace(/[，,]/g, "").replace(/−/g, "-").replace(/\s+/g, "");
  if (s.endsWith("%")) return null;
  if ((s.match(/\//g) || []).length === 1) {
    const [a, b] = s.split("/");
    const na = Number(a), nb = Number(b);
    if (a && b && Number.isFinite(na) && Number.isFinite(nb) && nb !== 0) return na / nb;
    return null;
  }
  if (!/^[+-]?(\d+\.?\d*|\.\d+)(e[+-]?\d+)?$/i.test(s)) return null;
  const n = Number(s);
  return Number.isFinite(n) ? n : null;
}

function numbersEqual(given, expected, tolerance) {
  const tol = tolerance == null ? 1e-6 : Number(tolerance);
  if (Math.abs(given - expected) <= tol) return true;
  const scale = Math.max(1, Math.abs(expected));
  return Math.abs(given - expected) <= Math.max(tol, 1e-4 * scale);
}

export function acceptedValues(q) {
  const vals = [];
  for (const key of ["answer", "answer_zh", "answer_en"]) {
    const v = q[key];
    if (v != null && String(v).trim() !== "") vals.push(String(v));
  }
  let extra = q.accepted || [];
  if (typeof extra === "string") extra = [extra];
  extra.forEach((x) => x != null && String(x).trim() !== "" && vals.push(String(x)));
  return [...new Set(vals)];
}

export function checkAnswer(q, given) {
  const typ = (q.type || "short").toLowerCase();
  const raw = given == null ? "" : String(given);
  if (typ === "mcq") return raw.trim().toLowerCase() === String(q.answer || "").trim().toLowerCase();
  if (typ === "numeric") {
    const got = tryNumber(raw);
    if (got == null) {
      const ng = normalizeText(raw);
      return acceptedValues(q).some((v) => normalizeText(v) === ng);
    }
    return acceptedValues(q).some((v) => {
      const exp = tryNumber(v);
      return (exp != null && numbersEqual(got, exp, q.tolerance)) || normalizeText(raw) === normalizeText(v);
    });
  }
  const ng = normalizeText(raw);
  if (!ng) return false;
  return acceptedValues(q).some((v) => normalizeText(v) === ng);
}
