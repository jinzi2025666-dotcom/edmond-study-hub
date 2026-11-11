export function tField(obj, base, lang) {
  if (!obj) return "";
  const primary = obj[`${base}_${lang}`];
  const fallback = obj[`${base}_${lang === "zh" ? "en" : "zh"}`];
  if (primary != null && String(primary).trim() !== "") return primary;
  if (fallback != null && String(fallback).trim() !== "") return fallback;
  return primary || fallback || "";
}

export function formatDate(value, lang) {
  if (!value) return "";
  const dt = new Date(value);
  if (Number.isNaN(dt.getTime())) return value;
  return dt.toLocaleDateString(lang === "zh" ? "zh-CN" : "en-GB", {
    year: "numeric",
    month: "short",
    day: "numeric",
  });
}

export function formatDateTime(value, lang) {
  if (!value) return "";
  const dt = new Date(value);
  if (Number.isNaN(dt.getTime())) return value;
  return dt.toLocaleString(lang === "zh" ? "zh-CN" : "en-GB", {
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

export function percent(n, lang) {
  const value = Math.round((Number(n) || 0) * 100);
  return lang === "zh" ? `${value}%` : `${value}%`;
}

export function subjectById(subjects, id) {
  return (subjects || []).find((s) => s.id === id) || null;
}

export function newId(prefix) {
  return prefix + Math.random().toString(36).slice(2, 10);
}


export function subjectPath(gradeId, subjectId) {
  return `/grades/${gradeId || "8"}/subjects/${subjectId}`;
}

export function flattenSections(chapters) {
  const out = [];
  for (const ch of chapters || []) {
    for (const unit of ch.units || []) {
      for (const section of unit.sections || []) {
        out.push({
          ...section,
          chapter: ch,
          unit,
          knowledge_id: section.knowledge_id || `kp-${section.id}`,
        });
      }
    }
  }
  return out;
}
