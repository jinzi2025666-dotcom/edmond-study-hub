const jsonHeaders = { "Content-Type": "application/json" };

async function request(path, options = {}) {
  const res = await fetch(path, options);
  const text = await res.text();
  let data = null;
  if (text) {
    try {
      data = JSON.parse(text);
    } catch {
      data = { detail: text };
    }
  }
  if (!res.ok) {
    const msg = (data && (data.detail || data.message)) || res.statusText;
    throw new Error(typeof msg === "string" ? msg : JSON.stringify(msg));
  }
  return data;
}

export const api = {
  config: () => request("/api/config"),
  grades: () => request("/api/grades"),
  subjects: (grade) => request(grade ? `/api/subjects?grade=${encodeURIComponent(grade)}` : "/api/subjects"),
  subject: (id, grade) => request(grade ? `/api/subjects/${id}?grade=${encodeURIComponent(grade)}` : `/api/subjects/${id}`),
  knowledge: (id) => request(`/api/knowledge/${id}`),
  setKnowledgeStatus: (id, status) =>
    request(`/api/knowledge/${id}/status`, {
      method: "POST",
      headers: jsonHeaders,
      body: JSON.stringify({ status }),
    }),
  set: (id) => request(`/api/sets/${id}`),
  check: (questionId, answer) =>
    request("/api/check", {
      method: "POST",
      headers: jsonHeaders,
      body: JSON.stringify({ question_id: questionId, answer }),
    }),
  submitSet: (id, answers, startedAt) =>
    request(`/api/sets/${id}/submit`, {
      method: "POST",
      headers: jsonHeaders,
      body: JSON.stringify({ answers, started_at: startedAt }),
    }),
  attempts: (subject) =>
    request(subject ? `/api/attempts?subject=${encodeURIComponent(subject)}` : "/api/attempts"),
  attempt: (id) => request(`/api/attempts/${id}`),
  mistakes: (params = {}) => {
    const q = new URLSearchParams();
    if (params.subject) q.set("subject", params.subject);
    if (params.status) q.set("status", params.status);
    const suffix = q.toString() ? `?${q}` : "";
    return request(`/api/mistakes${suffix}`);
  },
  masterMistake: (questionId) =>
    request(`/api/mistakes/${questionId}/master`, { method: "POST" }),
  progress: () => request("/api/progress"),
  continue: () => request("/api/continue"),
  updates: () => request("/api/updates?days=7"),
  search: (q) => request(`/api/search?q=${encodeURIComponent(q)}`),
  question: (id) => request(`/api/questions/${id}`),
  coding: () => request("/api/coding/exercises"),
  saveKnowledge: (payload) =>
    request("/api/admin/knowledge", {
      method: "POST",
      headers: jsonHeaders,
      body: JSON.stringify(payload),
    }),
  deleteKnowledge: (id) => request(`/api/admin/knowledge/${id}`, { method: "DELETE" }),
  saveQuestion: (payload) =>
    request("/api/admin/questions", {
      method: "POST",
      headers: jsonHeaders,
      body: JSON.stringify(payload),
    }),
  deleteQuestion: (id) => request(`/api/admin/questions/${id}`, { method: "DELETE" }),
  questions: (subject) =>
    request(subject ? `/api/questions?reveal=true&subject=${encodeURIComponent(subject)}` : "/api/questions?reveal=true"),
  knowledgeList: (subject) =>
    request(subject ? `/api/knowledge?subject=${encodeURIComponent(subject)}` : "/api/knowledge"),
  sets: (subject, kind) => {
    const q = new URLSearchParams();
    if (subject) q.set("subject", subject);
    if (kind) q.set("kind", kind);
    const suffix = q.toString() ? `?${q}` : "";
    return request(`/api/sets${suffix}`);
  },
  saveSet: (payload) =>
    request("/api/admin/sets", {
      method: "POST",
      headers: jsonHeaders,
      body: JSON.stringify(payload),
    }),
  deleteSet: (id) => request(`/api/admin/sets/${id}`, { method: "DELETE" }),
};
