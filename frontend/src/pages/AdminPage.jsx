import { useEffect, useRef, useState } from "react";
import { api } from "../api";
import { useLang } from "../context/LanguageContext";
import { useSite } from "../context/SiteContext";
import { formatDate, newId, tField } from "../utils";

const emptyKp = () => ({
  id: "",
  subject_id: "",
  unit_id: "",
  topic_id: "",
  title_zh: "",
  title_en: "",
  summary_zh: "",
  summary_en: "",
  body_zh: "",
  body_en: "",
  related_question_ids: [],
  published_at: todayLocal(),
  grade_id: "8",
  chapter_id: "",
  section_id: "",
  objectives_zh: "",
  objectives_en: "",
  keypoints_zh: "",
  keypoints_en: "",
  difficulties_zh: "",
  difficulties_en: "",
  diagram: "",
});

const emptyQ = () => ({
  id: "",
  subject_id: "",
  unit_id: "",
  knowledge_id: "",
  type: "mcq",
  stem_zh: "",
  stem_en: "",
  optionsText: "A 选项 | Option A\nB 选项 | Option B\nC 选项 | Option C\nD 选项 | Option D",
  answer: "a",
  acceptedText: "",
  explanation_zh: "",
  explanation_en: "",
  marks: 1,
  published_at: todayLocal(),
});

const emptySet = () => ({
  id: "",
  subject_id: "",
  unit_id: "",
  kind: "practice",
  title_zh: "",
  title_en: "",
  question_ids: [],
  time_limit_minutes: "",
  published_at: todayLocal(),
});

function todayLocal() {
  const d = new Date();
  const z = (n) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${z(d.getMonth() + 1)}-${z(d.getDate())}T09:00`;
}

export default function AdminPage() {
  const { lang, t } = useLang();
  const { subjects } = useSite();
  const [tab, setTab] = useState("knowledge");
  const [units, setUnits] = useState({});
  const [knowledge, setKnowledge] = useState([]);
  const [questions, setQuestions] = useState([]);
  const [sets, setSets] = useState([]);
  const [filterSubject, setFilterSubject] = useState("");
  const [flash, setFlash] = useState("");

  const reload = async () => {
    const rows = await api.subjects();
    const u = {};
    rows.forEach((s) => {
      u[s.id] = s.units || [];
    });
    setUnits(u);
    setKnowledge(await api.knowledgeList(filterSubject || undefined));
    setQuestions(await api.questions(filterSubject || undefined));
    setSets(await api.sets(filterSubject || undefined));
  };

  useEffect(() => {
    reload().catch((e) => setFlash(e.message));
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [filterSubject]);

  return (
    <div>
      <p className="kicker">{t("admin")}</p>
      <h1>{t("updateContent")}</h1>
      <p>{t("adminIntro")}</p>
      <div className="filter-row">
        <label>
          {t("filterSubject")}{" "}
          <select value={filterSubject} onChange={(e) => setFilterSubject(e.target.value)}>
            <option value="">{t("allSubjects")}</option>
            {subjects.map((s) => (
              <option key={s.id} value={s.id}>
                {tField(s, "name", lang)}
              </option>
            ))}
          </select>
        </label>
      </div>
      {flash && <p className="flash" role="status">{flash}</p>}
      {typeof api.exportData === "function" && <BackupPanel t={t} onDone={async (msg) => { setFlash(msg); await reload(); }} />}
      <div className="tabs" role="tablist">
        {["knowledge", "questions", "papers"].map((id) => (
          <button key={id} type="button" role="tab" aria-selected={tab === id} onClick={() => setTab(id)}>
            {id === "knowledge" ? t("tabKnowledge") : id === "questions" ? t("tabQuestions") : t("tabPapers")}
          </button>
        ))}
      </div>
      {tab === "knowledge" && (
        <KnowledgeAdmin
          items={knowledge}
          subjects={subjects}
          units={units}
          lang={lang}
          t={t}
          onSaved={async (msg) => {
            setFlash(msg);
            await reload();
          }}
        />
      )}
      {tab === "questions" && (
        <QuestionAdmin
          items={questions}
          knowledge={knowledge}
          subjects={subjects}
          units={units}
          lang={lang}
          t={t}
          onSaved={async (msg) => {
            setFlash(msg);
            await reload();
          }}
        />
      )}
      {tab === "papers" && (
        <SetAdmin
          items={sets}
          questions={questions}
          subjects={subjects}
          units={units}
          lang={lang}
          t={t}
          onSaved={async (msg) => {
            setFlash(msg);
            await reload();
          }}
        />
      )}
    </div>
  );
}

function KnowledgeAdmin({ items, subjects, units, lang, t, onSaved }) {
  const [form, setForm] = useState(emptyKp());
  const set = (k, v) => setForm((cur) => ({ ...cur, [k]: v }));
  const unitList = units[form.subject_id] || [];
  const topics = (unitList.find((u) => u.id === form.unit_id)?.topics || []);

  const save = async (e) => {
    e.preventDefault();
    if (!form.subject_id || !(form.title_zh || form.title_en)) {
      onSaved(t("required"));
      return;
    }
    const payload = {
      ...form,
      id: form.id || newId("kp-"),
      related_question_ids: String(form.related_question_ids || "")
        .split(",")
        .map((x) => x.trim())
        .filter(Boolean),
      published_at: toIso(form.published_at),
    };
    await api.saveKnowledge(payload);
    setForm(emptyKp());
    onSaved(t("saved"));
  };

  return (
    <div className="admin-layout">
      <SideList
        items={items}
        lang={lang}
        t={t}
        active={form.id}
        onNew={() => setForm(emptyKp())}
        onPick={(it) =>
          setForm({
            ...emptyKp(),
            ...it,
            related_question_ids: (it.related_question_ids || []).join(", "),
            published_at: toLocalInput(it.published_at),
          })
        }
        onDelete={async (id) => {
          if (!confirm(t("confirmDelete"))) return;
          await api.deleteKnowledge(id);
          setForm(emptyKp());
          onSaved(t("saved"));
        }}
      />
      <form onSubmit={save}>
        <SubjectUnitFields form={form} set={set} subjects={subjects} unitList={unitList} topics={topics} lang={lang} t={t} />
        <div className="grid-2">
          <Field label={t("titleZh")} value={form.title_zh} onChange={(v) => set("title_zh", v)} />
          <Field label={t("titleEn")} value={form.title_en} onChange={(v) => set("title_en", v)} />
          <Field label={t("summaryZh")} value={form.summary_zh} onChange={(v) => set("summary_zh", v)} />
          <Field label={t("summaryEn")} value={form.summary_en} onChange={(v) => set("summary_en", v)} />
        </div>
        <div className="grid-2">
          <Field label={t("gradeLabel")} value={form.grade_id || "8"} onChange={(v) => set("grade_id", v)} />
          <Field label="chapter_id" value={form.chapter_id || ""} onChange={(v) => set("chapter_id", v)} />
          <Field label="section_id" value={form.section_id || ""} onChange={(v) => set("section_id", v)} />
        </div>
        <Field area label={t("youWillLearn") + " (zh)"} value={form.objectives_zh || ""} onChange={(v) => set("objectives_zh", v)} />
        <Field area label={t("youWillLearn") + " (en)"} value={form.objectives_en || ""} onChange={(v) => set("objectives_en", v)} />
        <Field area label={t("keyPoints") + " (zh)"} value={form.keypoints_zh || ""} onChange={(v) => set("keypoints_zh", v)} />
        <Field area label={t("keyPoints") + " (en)"} value={form.keypoints_en || ""} onChange={(v) => set("keypoints_en", v)} />
        <Field area label={t("bodyZh")} value={form.body_zh} onChange={(v) => set("body_zh", v)} />
        <Field area label={t("difficulties") + " (zh)"} value={form.difficulties_zh || ""} onChange={(v) => set("difficulties_zh", v)} />
        <Field area label={t("difficulties") + " (en)"} value={form.difficulties_en || ""} onChange={(v) => set("difficulties_en", v)} />
        <Field area label="diagram (SVG)" value={form.diagram || ""} onChange={(v) => set("diagram", v)} />
        <Field area label={t("bodyEn")} value={form.body_en} onChange={(v) => set("body_en", v)} />
        <Field label={t("relatedIds")} value={form.related_question_ids} onChange={(v) => set("related_question_ids", v)} />
        <Field label={t("publishedAt")} type="datetime-local" value={form.published_at} onChange={(v) => set("published_at", v)} />
        <div className="btn-row">
          <button className="btn btn-primary" type="submit">
            {t("save")}
          </button>
          <button className="btn" type="button" onClick={() => setForm(emptyKp())}>
            {t("cancel")}
          </button>
        </div>
      </form>
    </div>
  );
}

function QuestionAdmin({ items, knowledge, subjects, units, lang, t, onSaved }) {
  const [form, setForm] = useState(emptyQ());
  const set = (k, v) => setForm((cur) => ({ ...cur, [k]: v }));
  const unitList = units[form.subject_id] || [];

  const save = async (e) => {
    e.preventDefault();
    if (!form.subject_id || !(form.stem_zh || form.stem_en)) {
      onSaved(t("required"));
      return;
    }
    const options = parseOptions(form.optionsText);
    const accepted = String(form.acceptedText || "")
      .split("\n")
      .map((x) => x.trim())
      .filter(Boolean);
    const payload = {
      ...form,
      id: form.id || newId("q-"),
      options: form.type === "mcq" ? options : [],
      accepted,
      marks: Number(form.marks) || 1,
      published_at: toIso(form.published_at),
    };
    delete payload.optionsText;
    delete payload.acceptedText;
    await api.saveQuestion(payload);
    setForm(emptyQ());
    onSaved(t("saved"));
  };

  return (
    <div className="admin-layout">
      <SideList
        items={items}
        lang={lang}
        t={t}
        titleKey="stem"
        active={form.id}
        onNew={() => setForm(emptyQ())}
        onPick={(it) =>
          setForm({
            ...emptyQ(),
            ...it,
            optionsText: formatOptions(it.options),
            acceptedText: (it.accepted || []).join("\n"),
            published_at: toLocalInput(it.published_at),
          })
        }
        onDelete={async (id) => {
          if (!confirm(t("confirmDelete"))) return;
          await api.deleteQuestion(id);
          setForm(emptyQ());
          onSaved(t("saved"));
        }}
      />
      <form onSubmit={save}>
        <SubjectUnitFields form={form} set={set} subjects={subjects} unitList={unitList} topics={[]} lang={lang} t={t} hideTopic />
        <div className="field">
          <label>{t("knowledge")}</label>
          <select value={form.knowledge_id || ""} onChange={(e) => set("knowledge_id", e.target.value)}>
            <option value="">{t("none")}</option>
            {knowledge
              .filter((k) => !form.subject_id || k.subject_id === form.subject_id)
              .map((k) => (
                <option key={k.id} value={k.id}>
                  {tField(k, "title", lang)}
                </option>
              ))}
          </select>
        </div>
        <div className="grid-2">
          <div className="field">
            <label>{t("type")}</label>
            <select value={form.type} onChange={(e) => set("type", e.target.value)}>
              <option value="mcq">{t("typeMcq")}</option>
              <option value="short">{t("typeShort")}</option>
              <option value="numeric">{t("typeNumeric")}</option>
              <option value="structured">{t("typeStructured")}</option>
            </select>
          </div>
          <Field label={t("marks")} type="number" value={form.marks} onChange={(v) => set("marks", v)} />
        </div>
        <Field area label={t("stemZh")} value={form.stem_zh} onChange={(v) => set("stem_zh", v)} />
        <Field area label={t("stemEn")} value={form.stem_en} onChange={(v) => set("stem_en", v)} />
        {form.type === "mcq" && <Field area label={t("options")} value={form.optionsText} onChange={(v) => set("optionsText", v)} />}
        <Field label={t("answer")} value={form.answer} onChange={(v) => set("answer", v)} />
        <Field area label={t("accepted")} value={form.acceptedText} onChange={(v) => set("acceptedText", v)} />
        <Field area label={t("explanationZh")} value={form.explanation_zh} onChange={(v) => set("explanation_zh", v)} />
        <Field area label={t("explanationEn")} value={form.explanation_en} onChange={(v) => set("explanation_en", v)} />
        <Field label={t("publishedAt")} type="datetime-local" value={form.published_at} onChange={(v) => set("published_at", v)} />
        <div className="btn-row">
          <button className="btn btn-primary" type="submit">
            {t("save")}
          </button>
          <button className="btn" type="button" onClick={() => setForm(emptyQ())}>
            {t("cancel")}
          </button>
        </div>
      </form>
    </div>
  );
}

function SetAdmin({ items, questions, subjects, units, lang, t, onSaved }) {
  const [form, setForm] = useState(emptySet());
  const set = (k, v) => setForm((cur) => ({ ...cur, [k]: v }));
  const unitList = units[form.subject_id] || [];
  const pool = questions.filter((q) => !form.subject_id || q.subject_id === form.subject_id);

  const save = async (e) => {
    e.preventDefault();
    if (!form.subject_id || !(form.title_zh || form.title_en)) {
      onSaved(t("required"));
      return;
    }
    const payload = {
      ...form,
      id: form.id || newId(form.kind === "paper" ? "paper-" : "practice-"),
      time_limit_minutes: form.time_limit_minutes === "" || form.time_limit_minutes == null ? null : Number(form.time_limit_minutes),
      published_at: toIso(form.published_at),
    };
    await api.saveSet(payload);
    setForm(emptySet());
    onSaved(t("saved"));
  };

  const toggleQ = (qid) => {
    const ids = form.question_ids || [];
    set("question_ids", ids.includes(qid) ? ids.filter((x) => x !== qid) : [...ids, qid]);
  };

  return (
    <div className="admin-layout">
      <SideList
        items={items}
        lang={lang}
        t={t}
        active={form.id}
        onNew={() => setForm(emptySet())}
        onPick={(it) =>
          setForm({
            ...emptySet(),
            ...it,
            time_limit_minutes: it.time_limit_minutes ?? "",
            published_at: toLocalInput(it.published_at),
          })
        }
        onDelete={async (id) => {
          if (!confirm(t("confirmDelete"))) return;
          await api.deleteSet(id);
          setForm(emptySet());
          onSaved(t("saved"));
        }}
      />
      <form onSubmit={save}>
        <SubjectUnitFields form={form} set={set} subjects={subjects} unitList={unitList} topics={[]} lang={lang} t={t} hideTopic />
        <div className="grid-2">
          <div className="field">
            <label>{t("kind")}</label>
            <select value={form.kind} onChange={(e) => set("kind", e.target.value)}>
              <option value="practice">{t("kindPractice")}</option>
              <option value="paper">{t("kindPaper")}</option>
            </select>
          </div>
          <Field label={t("timeMinutes")} type="number" value={form.time_limit_minutes} onChange={(v) => set("time_limit_minutes", v)} />
        </div>
        <div className="grid-2">
          <Field label={t("titleZh")} value={form.title_zh} onChange={(v) => set("title_zh", v)} />
          <Field label={t("titleEn")} value={form.title_en} onChange={(v) => set("title_en", v)} />
        </div>
        <Field label={t("publishedAt")} type="datetime-local" value={form.published_at} onChange={(v) => set("published_at", v)} />
        <div className="field">
          <label>{t("questionIds")}</label>
          <div style={{ maxHeight: "20rem", overflow: "auto", border: "1px solid var(--rule)", padding: "0.4rem 0.6rem" }}>
            {pool.map((q) => (
              <label key={q.id} style={{ display: "block", margin: "0.25rem 0" }}>
                <input type="checkbox" checked={(form.question_ids || []).includes(q.id)} onChange={() => toggleQ(q.id)} />{" "}
                {tField(q, "stem", lang).slice(0, 90) || q.id}
              </label>
            ))}
          </div>
        </div>
        <div className="btn-row">
          <button className="btn btn-primary" type="submit">
            {t("save")}
          </button>
          <button className="btn" type="button" onClick={() => setForm(emptySet())}>
            {t("cancel")}
          </button>
        </div>
      </form>
    </div>
  );
}

function SideList({ items, lang, t, active, onNew, onPick, onDelete, titleKey = "title" }) {
  return (
    <div>
      <button type="button" className="btn" onClick={onNew} style={{ marginBottom: "0.5rem" }}>
        {t("addNew")}
      </button>
      <ul className="side-list">
        {items.map((it) => (
          <li key={it.id}>
            <button type="button" className={it.id === active ? "active" : ""} onClick={() => onPick(it)}>
              {tField(it, titleKey, lang) || it.id}
              <div className="muted">{formatDate(it.published_at, lang)}</div>
            </button>
            <button type="button" className="btn-danger btn" style={{ margin: "0 0.4rem 0.4rem", fontSize: "0.8rem" }} onClick={() => onDelete(it.id)}>
              {t("remove")}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

function SubjectUnitFields({ form, set, subjects, unitList, topics, lang, t, hideTopic }) {
  return (
    <>
      <div className="field">
        <label>{t("subject")}</label>
        <select value={form.subject_id} onChange={(e) => set("subject_id", e.target.value)}>
          <option value="">{t("selectSubject")}</option>
          {subjects.map((s) => (
            <option key={s.id} value={s.id}>
              {tField(s, "name", lang)}
            </option>
          ))}
        </select>
      </div>
      <div className="field">
        <label>{t("unit")}</label>
        <select value={form.unit_id || ""} onChange={(e) => set("unit_id", e.target.value)}>
          <option value="">{t("none")}</option>
          {unitList.map((u) => (
            <option key={u.id} value={u.id}>
              {u.code} {tField(u, "title", lang)}
            </option>
          ))}
        </select>
      </div>
      {!hideTopic && (
        <div className="field">
          <label>{t("topic")}</label>
          <select value={form.topic_id || ""} onChange={(e) => set("topic_id", e.target.value)}>
            <option value="">{t("none")}</option>
            {topics.map((tp) => (
              <option key={tp.id} value={tp.id}>
                {tField(tp, "title", lang)}
              </option>
            ))}
          </select>
        </div>
      )}
    </>
  );
}

function Field({ label, value, onChange, area, type = "text" }) {
  return (
    <div className="field">
      <label>{label}</label>
      {area ? (
        <textarea rows={8} value={value || ""} onChange={(e) => onChange(e.target.value)} />
      ) : (
        <input type={type} value={value ?? ""} onChange={(e) => onChange(e.target.value)} />
      )}
    </div>
  );
}

function parseOptions(text) {
  const lines = String(text || "")
    .split("\n")
    .map((l) => l.trim())
    .filter(Boolean);
  return lines.map((line, i) => {
    const ids = "abcdefghijklmnopqrstuvwxyz";
    let id = ids[i] || String(i);
    let rest = line;
    const m = line.match(/^([a-zA-Z0-9])[.)、:]\s*(.*)$/);
    if (m) {
      id = m[1].toLowerCase();
      rest = m[2];
    }
    const [zh, en] = rest.split("|").map((s) => s.trim());
    return { id, zh: zh || rest, en: en || zh || rest };
  });
}

function formatOptions(options) {
  if (!options || !options.length) return "";
  return options.map((o) => `${(o.id || "").toUpperCase()}. ${o.zh || ""} | ${o.en || ""}`).join("\n");
}

function toIso(value) {
  if (!value) return new Date().toISOString();
  if (/T/.test(value) && !value.includes("+") && !value.endsWith("Z")) return `${value}:00+08:00`;
  return value;
}

function toLocalInput(value) {
  if (!value) return todayLocal();
  const d = new Date(value);
  if (Number.isNaN(d.getTime())) return todayLocal();
  const z = (n) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${z(d.getMonth() + 1)}-${z(d.getDate())}T${z(d.getHours())}:${z(d.getMinutes())}`;
}

function BackupPanel({ t, onDone }) {
  const fileRef = useRef(null);
  const doExport = async () => {
    const data = await api.exportData();
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `edmond-study-hub-backup-${new Date().toISOString().slice(0, 10)}.json`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  const doImport = async (e) => {
    const file = e.target.files?.[0];
    e.target.value = "";
    if (!file) return;
    if (!confirm(t("confirmImport"))) return;
    try {
      await api.importData(JSON.parse(await file.text()));
      onDone(t("importDone"));
    } catch (err) {
      onDone(`${t("error")}: ${err.message}`);
    }
  };
  const doReset = async () => {
    if (!confirm(t("confirmReset"))) return;
    await api.resetData();
    onDone(t("resetDone"));
  };
  return (
    <section className="panel" style={{ marginBottom: "1.25rem" }}>
      <p className="kicker">{t("offlineBadge")}</p>
      <h2>{t("backupTitle")}</h2>
      <p className="muted">{t("backupIntro")}</p>
      <div className="btn-row">
        <button type="button" className="btn btn-primary" onClick={doExport}>{t("exportData")}</button>
        <button type="button" className="btn" onClick={() => fileRef.current?.click()}>{t("importData")}</button>
        <input ref={fileRef} type="file" accept="application/json,.json" onChange={doImport} hidden />
        <button type="button" className="btn btn-danger" onClick={doReset}>{t("resetData")}</button>
      </div>
    </section>
  );
}
