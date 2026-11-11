// Client-side replacement for the FastAPI backend (offline single-file build).
// Built-in content comes from the inlined curriculum JSON; everything the
// student changes lives in localStorage under STORE_KEY.
import siteConfig from "../../../site.config.json";
import subjects from "../../../data/curriculum/subjects.json";
import units from "../../../data/curriculum/units.json";
import grades from "../../../data/curriculum/grades.json";
import content from "../../../data/curriculum/content.json";
import { checkAnswer } from "./grading";

export const STORE_KEY = "esh-offline-data-v1";

const empty = () => ({
  version: 1,
  knowledge: {},
  questions: {},
  sets: {},
  deleted: { knowledge: [], questions: [], sets: [] },
  progress: {},
  mistakes: {},
  attempts: [],
  activity: [],
});

let memoryFallback = null;

export function loadUser() {
  try {
    const raw = localStorage.getItem(STORE_KEY);
    if (!raw) return empty();
    return { ...empty(), ...JSON.parse(raw) };
  } catch {
    return memoryFallback || empty();
  }
}

function saveUser(data) {
  memoryFallback = data;
  try {
    localStorage.setItem(STORE_KEY, JSON.stringify(data));
  } catch (e) {
    console.warn("Could not save to localStorage", e);
  }
}

function mutate(fn) {
  const data = loadUser();
  const out = fn(data);
  saveUser(data);
  return out;
}

export function nowIso() {
  const d = new Date();
  const local = new Date(d.getTime() + 8 * 3600 * 1000).toISOString().slice(0, 19);
  return `${local}+08:00`;
}

const baseById = (rows) => Object.fromEntries((rows || []).map((r) => [r.id, r]));
const BASE = {
  knowledge: baseById(content.knowledge),
  questions: baseById(content.questions),
  sets: baseById(content.sets),
};

function merged(kind) {
  const user = loadUser();
  const del = new Set(user.deleted[kind] || []);
  const all = { ...BASE[kind], ...(user[kind] || {}) };
  return Object.values(all).filter((r) => !del.has(r.id));
}

const byPublishedDesc = (a, b) => String(b.published_at || "").localeCompare(String(a.published_at || ""));

function listKnowledge(subject, unit, grade) {
  return merged("knowledge")
    .filter((k) => (!subject || k.subject_id === subject) && (!unit || k.unit_id === unit || k.chapter_id === unit || k.section_id === unit) && (!grade || !k.grade_id || k.grade_id === grade))
    .sort(byPublishedDesc);
}
function listQuestions(subject, unit) {
  return merged("questions")
    .filter((q) => (!subject || q.subject_id === subject) && (!unit || q.unit_id === unit))
    .sort(byPublishedDesc);
}
function listSets(subject, kind, grade) {
  return merged("sets")
    .filter((s) => (!subject || s.subject_id === subject) && (!kind || s.kind === kind) && (!grade || !s.grade_id || s.grade_id === grade))
    .sort(byPublishedDesc);
}
const getOne = (kind, id) => merged(kind).find((r) => r.id === id) || null;

function publicQuestion(q, reveal) {
  const item = { ...q };
  if (!reveal) {
    ["answer", "accepted", "answer_zh", "answer_en", "explanation_zh", "explanation_en", "tolerance"].forEach((k) => delete item[k]);
  }
  return item;
}

function attachProgress(rows) {
  const p = loadUser().progress;
  return rows.map((r) => ({ ...r, status: p[r.id]?.status || "not_started" }));
}

function countsFor(subjectId, grade) {
  const kps = attachProgress(listKnowledge(subjectId, undefined, grade));
  const mastered = kps.filter((k) => k.status === "mastered").length;
  return {
    knowledge: kps.length,
    mastered,
    learning: kps.filter((k) => k.status === "learning").length,
    questions: listQuestions(subjectId).length,
    practice: listSets(subjectId, "practice", grade).length,
    papers: listSets(subjectId, "paper", grade).length,
    progress: kps.length ? mastered / kps.length : 0,
  };
}

function unitsBySubject(grade) {
  const g = {};
  units.forEach((u) => {
    if (grade && u.grade_id && String(u.grade_id) !== String(grade)) return;
    (g[u.subject_id] ||= []).push(u);
  });
  Object.values(g).forEach((arr) => arr.sort((a, b) => (a.order || 0) - (b.order || 0)));
  return g;
}

function notFound(what) {
  const err = new Error(`${what} not found`);
  err.status = 404;
  throw err;
}

function recordActivity(kind, ref) {
  mutate((d) => {
    d.activity.unshift({ kind, ref_id: ref, at: nowIso() });
    d.activity = d.activity.slice(0, 50);
  });
}

function recordMistake(q, given) {
  mutate((d) => {
    const prev = d.mistakes[q.id];
    d.mistakes[q.id] = {
      question_id: q.id,
      subject_id: q.subject_id,
      given_answer: given == null ? "" : String(given),
      created_at: prev?.created_at || nowIso(),
      updated_at: nowIso(),
      status: "open",
    };
  });
}

function withinDays(value, days) {
  const t = Date.parse(value || "");
  return Number.isFinite(t) && t >= Date.now() - days * 86400000;
}

function gradeAnswers(ids, answers) {
  let score = 0;
  let max = 0;
  const details = [];
  for (const qid of ids) {
    const q = getOne("questions", qid);
    if (!q) continue;
    const marks = Number(q.marks) || 1;
    max += marks;
    const given = answers?.[qid];
    const correct = checkAnswer(q, given);
    if (correct) score += marks;
    if (!correct && given != null && given !== "") recordMistake(q, given);
    details.push({ question_id: qid, question: publicQuestion(q, true), given, correct, marks, awarded: correct ? marks : 0 });
  }
  return { details, score, max };
}

function newId(prefix) {
  return prefix + Math.random().toString(36).slice(2, 12);
}

function upsert(kind, payload, prefix) {
  const item = { ...payload };
  if (!item.id) item.id = newId(prefix);
  if (!item.subject_id) throw new Error("subject_id is required");
  const ts = nowIso();
  mutate((d) => {
    const prev = d[kind][item.id] || BASE[kind][item.id];
    d[kind][item.id] = {
      ...item,
      created_at: prev?.created_at || ts,
      updated_at: ts,
      origin: prev?.origin === "seed" || BASE[kind][item.id] ? "seed-edited" : "user",
      published_at: item.published_at || ts,
    };
    d.deleted[kind] = (d.deleted[kind] || []).filter((x) => x !== item.id);
  });
  return getOne(kind, item.id);
}

function remove(kind, id) {
  if (!getOne(kind, id)) notFound(kind);
  mutate((d) => {
    delete d[kind][id];
    if (BASE[kind][id] && !d.deleted[kind].includes(id)) d.deleted[kind].push(id);
  });
  return { ok: true };
}

function attemptsList(subject, limit = 50) {
  const sets = Object.fromEntries(merged("sets").map((s) => [s.id, s]));
  return loadUser()
    .attempts.filter((a) => !subject || a.subject_id === subject)
    .sort((a, b) => String(b.submitted_at).localeCompare(String(a.submitted_at)))
    .slice(0, limit)
    .map((a) => ({ ...a, set_title_zh: sets[a.set_id]?.title_zh, set_title_en: sets[a.set_id]?.title_en }));
}

function mistakesList(subject, status = "open") {
  return Object.values(loadUser().mistakes)
    .filter((m) => (!subject || m.subject_id === subject) && (!status || status === "all" || m.status === status))
    .sort((a, b) => String(b.updated_at).localeCompare(String(a.updated_at)))
    .map((m) => {
      const q = getOne("questions", m.question_id);
      return { ...m, question: q ? publicQuestion(q, false) : null };
    });
}

function search(q) {
  const needle = String(q || "").trim().toLowerCase();
  if (!needle) return [];
  const out = [];
  const hit = (type, item, blobParts, href, subjectId, tz, te) => {
    if (blobParts.join(" ").toLowerCase().includes(needle)) {
      out.push({ type, id: item.id, subject_id: subjectId, title_zh: tz, title_en: te, href });
    }
  };
  units.forEach((u) =>
    hit("unit", u, [u.title_zh, u.title_en, u.code, u.note_zh, u.note_en, ...(u.topics || []).flatMap((t) => [t.title_zh, t.title_en])].map((x) => x || ""),
      `/subjects/${u.subject_id}#${u.id}`, u.subject_id, u.title_zh, u.title_en)
  );
  listKnowledge().forEach((k) =>
    hit("knowledge", k, ["title_zh", "title_en", "summary_zh", "summary_en", "body_zh", "body_en"].map((f) => k[f] || ""),
      `/knowledge/${k.id}`, k.subject_id, k.title_zh, k.title_en)
  );
  listQuestions().forEach((qu) =>
    hit("question", qu, [qu.stem_zh || "", qu.stem_en || "", ...(qu.options || []).flatMap((o) => [o.zh || "", o.en || ""])],
      `/practice/question/${qu.id}`, qu.subject_id, qu.stem_zh, qu.stem_en)
  );
  return out.slice(0, 40);
}

// --- exported API with the same shape as src/api.js (all async) ---
const wrap = (fn) => (...args) => {
  try {
    return Promise.resolve(fn(...args));
  } catch (e) {
    return Promise.reject(e);
  }
};

export const api = {
  config: wrap(() => ({ ...siteConfig, subjects, grades })),
  grades: wrap(() => grades),
  subjects: wrap((grade) => {
    const g = unitsBySubject(grade);
    return subjects.map((s) => ({
      ...s,
      units: g[s.id] || [],
      counts: countsFor(s.id, grade),
      development_status: (s.development || {})[String(grade || "8")] || "upcoming",
    }));
  }),
  subject: wrap((id, grade) => {
    const subject = subjects.find((s) => s.id === id) || notFound("Subject");
    const knowledge = attachProgress(listKnowledge(id, undefined, grade));
    const unitRows = (unitsBySubject(grade)[id] || []).map((u) => {
      const ups = knowledge.filter((k) => k.unit_id === u.id || k.chapter_id === u.id);
      const mastered = ups.filter((k) => k.status === "mastered").length;
      return { ...u, knowledge_count: ups.length, mastered, progress: ups.length ? mastered / ups.length : 0 };
    });
    return {
      subject,
      units: unitRows,
      knowledge,
      practice: listSets(id, "practice", grade),
      papers: listSets(id, "paper", grade),
      counts: countsFor(id, grade),
      grade_id: grade || "8",
      development_status: (subject.development || {})[String(grade || "8")] || "upcoming",
    };
  }),
  knowledge: wrap((id) => {
    const item = getOne("knowledge", id) || notFound("Knowledge point");
    recordActivity("view_knowledge", id);
    return {
      ...item,
      status: loadUser().progress[id]?.status || "not_started",
      related_questions: (item.related_question_ids || [])
        .map((qid) => getOne("questions", qid))
        .filter(Boolean)
        .map((q) => publicQuestion(q, false)),
    };
  }),
  setKnowledgeStatus: wrap((id, status) => {
    if (!getOne("knowledge", id)) notFound("Knowledge point");
    mutate((d) => {
      if (status === "not_started") delete d.progress[id];
      else d.progress[id] = { status, updated_at: nowIso() };
    });
    return { ok: true, status };
  }),
  set: wrap((id, reveal = false) => {
    const item = getOne("sets", id) || notFound("Set");
    const questions = (item.question_ids || []).map((qid) => getOne("questions", qid)).filter(Boolean).map((q) => publicQuestion(q, reveal));
    return { ...item, questions, marks: questions.reduce((n, q) => n + (Number(q.marks) || 1), 0) };
  }),
  check: wrap((qid, answer) => {
    const q = getOne("questions", qid) || notFound("Question");
    const correct = checkAnswer(q, answer);
    if (!correct) recordMistake(q, answer);
    const marks = Number(q.marks) || 1;
    return {
      correct,
      marks,
      awarded: correct ? marks : 0,
      explanation_zh: q.explanation_zh,
      explanation_en: q.explanation_en,
      answer: q.answer,
      accepted: q.accepted || [],
    };
  }),
  submitSet: wrap((id, answers, startedAt) => {
    const item = getOne("sets", id) || notFound("Set");
    const { details, score, max } = gradeAnswers(item.question_ids || [], answers || {});
    const attempt = {
      id: newId("att-"),
      set_id: id,
      kind: item.kind,
      subject_id: item.subject_id,
      started_at: startedAt,
      submitted_at: nowIso(),
      time_limit_minutes: item.time_limit_minutes,
      score,
      max_score: max,
      answers: details,
    };
    mutate((d) => d.attempts.push(attempt));
    return attempt;
  }),
  attempts: wrap((subject) => attemptsList(subject)),
  attempt: wrap((id) => attemptsList(null, 100000).find((a) => a.id === id) || notFound("Attempt")),
  mistakes: wrap((params = {}) => mistakesList(params.subject, params.status || "open")),
  masterMistake: wrap((qid) => {
    const user = loadUser();
    if (!user.mistakes[qid]) notFound("Mistake");
    mutate((d) => {
      d.mistakes[qid].status = "mastered";
      d.mistakes[qid].updated_at = nowIso();
    });
    return { ok: true };
  }),
  progress: wrap(() => {
    let tk = 0;
    let tm = 0;
    const rows = subjects.map((s) => {
      const counts = countsFor(s.id);
      tk += counts.knowledge;
      tm += counts.mastered;
      return { ...s, counts };
    });
    return {
      subjects: rows,
      overall: { knowledge: tk, mastered: tm, progress: tk ? tm / tk : 0 },
      attempts: attemptsList(null, 20),
      open_mistakes: mistakesList(null, "open").length,
    };
  }),
  continue: wrap(() => {
    const user = loadUser();
    const last = user.activity.find((a) => a.kind === "view_knowledge" && getOne("knowledge", a.ref_id));
    if (last) {
      const k = getOne("knowledge", last.ref_id);
      const status = user.progress[k.id]?.status || "not_started";
      if (status !== "mastered") return { ...k, status };
    }
    return attachProgress(listKnowledge()).find((k) => k.status !== "mastered") || null;
  }),
  updates: wrap(() => {
    const items = [];
    listKnowledge().forEach((k) => withinDays(k.published_at, 7) && items.push({ type: "knowledge", id: k.id, subject_id: k.subject_id, title_zh: k.title_zh, title_en: k.title_en, published_at: k.published_at }));
    listSets().forEach((s) => withinDays(s.published_at, 7) && items.push({ type: s.kind || "set", id: s.id, subject_id: s.subject_id, title_zh: s.title_zh, title_en: s.title_en, published_at: s.published_at }));
    return items.sort(byPublishedDesc);
  }),
  search: wrap(search),
  question: wrap((id) => publicQuestion(getOne("questions", id) || notFound("Question"), false)),
  coding: wrap(() => content.coding_exercises || []),
  questions: wrap((subject) => listQuestions(subject).map((q) => publicQuestion(q, true))),
  knowledgeList: wrap((subject) => attachProgress(listKnowledge(subject))),
  sets: wrap((subject, kind) => listSets(subject, kind)),
  saveKnowledge: wrap((p) => upsert("knowledge", { related_question_ids: [], ...p }, "kp-")),
  deleteKnowledge: wrap((id) => remove("knowledge", id)),
  saveQuestion: wrap((p) => upsert("questions", { type: "mcq", marks: 1, ...p }, "q-")),
  deleteQuestion: wrap((id) => remove("questions", id)),
  saveSet: wrap((p) => upsert("sets", { kind: "practice", question_ids: [], ...p }, "set-")),
  deleteSet: wrap((id) => remove("sets", id)),

  // offline-only: backup / restore / reset
  exportData: wrap(() => ({
    app: "edmond-study-hub",
    exported_at: nowIso(),
    data: loadUser(),
  })),
  importData: wrap((json) => {
    const data = json && json.data ? json.data : json;
    if (!data || typeof data !== "object" || !("progress" in data || "knowledge" in data || "mistakes" in data)) {
      throw new Error("Not an Edmond Study Hub backup file");
    }
    saveUser({ ...empty(), ...data });
    return { ok: true };
  }),
  resetData: wrap(() => {
    try {
      localStorage.removeItem(STORE_KEY);
    } catch {
      /* ignore */
    }
    memoryFallback = null;
    return { ok: true };
  }),
};
