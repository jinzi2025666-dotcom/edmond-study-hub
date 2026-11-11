import { useEffect, useMemo, useState } from "react";
import { Link, Navigate, useParams } from "react-router-dom";
import { api } from "../api";
import { useLang } from "../context/LanguageContext";
import { useGrade } from "../context/GradeContext";
import SubjectIcon from "../components/SubjectIcon";
import { flattenSections, percent, subjectPath, tField } from "../utils";

const ALIASES = { math: "mathematics", maths: "mathematics", cs: "computer-science", computing: "computer-science", econ: "economics", phys: "physics", chem: "chemistry", bio: "biology", cn: "chinese", en: "english" };

export default function SubjectPage() {
  const { subjectId: raw, gradeId } = useParams();
  const { setGradeId } = useGrade();
  useEffect(() => {
    if (gradeId) setGradeId(gradeId);
  }, [gradeId, setGradeId]);
  if (ALIASES[raw]) return <Navigate to={subjectPath(gradeId || "8", ALIASES[raw])} replace />;
  return <SubjectView subjectId={raw} gradeId={gradeId || "8"} />;
}

function findKnowledge(knowledge, section) {
  const kid = section.knowledge_id || `kp-${section.id}`;
  return (knowledge || []).find((k) => k.id === kid || k.section_id === section.id || k.topic_id === section.id);
}

function SubjectView({ subjectId, gradeId }) {
  const { lang, t } = useLang();
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    setData(null);
    setError("");
    api
      .subject(subjectId, gradeId)
      .then(setData)
      .catch((e) => setError(e.message));
  }, [subjectId, gradeId]);

  const chapters = data?.units || [];
  const knowledge = data?.knowledge || [];
  const sections = useMemo(() => flattenSections(chapters), [chapters]);
  const continueItem = useMemo(() => {
    for (const sec of sections) {
      const k = findKnowledge(knowledge, sec);
      if (k && k.status !== "mastered") return k;
    }
    return findKnowledge(knowledge, sections[0] || {}) || knowledge[0] || null;
  }, [sections, knowledge]);

  if (error) return <p>{t("error")}: {error}</p>;
  if (!data) return <p>{t("loading")}</p>;

  const s = data.subject;
  const accent = s.accent;
  const status = data.development_status || (s.development || {})[gradeId] || "upcoming";
  const gradeName = lang === "zh" ? { 7: "七年级", 8: "八年级", 9: "九年级" }[gradeId] : { 7: "Year 7", 8: "Year 8", 9: "Year 9" }[gradeId];

  if (status === "upcoming" || chapters.length === 0) {
    return (
      <div style={{ "--accent": accent }}>
        <nav className="crumb">
          <Link to="/">{t("breadcrumbHome")}</Link>
          {" / "}
          {gradeName}
          {" / "}
          {tField(s, "name", lang)}
        </nav>
        <div className="empty coming-soon">
          <h1>{tField(s, "name", lang)}</h1>
          <p>{t("comingSoonBody")}</p>
        </div>
      </div>
    );
  }

  const ready = status === "ready";
  const practiceByChapter = (id) => (data.practice || []).filter((p) => p.chapter_id === id || p.unit_id === id);
  const papersByChapter = (id) => (data.papers || []).filter((p) => p.chapter_id === id || p.unit_id === id);
  const coursePapers = (data.papers || []).filter((p) => p.scope === "course" || p.id.includes("comprehensive"));

  return (
    <div className="course-page" style={{ "--accent": accent }}>
      <nav className="crumb">
        <Link to="/">{t("breadcrumbHome")}</Link>
        {" / "}
        <Link to="/">{gradeName}</Link>
        {" / "}
        {tField(s, "name", lang)}
      </nav>
      <div className="subject-hero">
        <div className="icon-wrap">
          <SubjectIcon id={s.id} size={48} />
        </div>
        <div>
          <p className="kicker">{tField(s, "framework", lang)}</p>
          <h1>
            {gradeName}
            <span className="title-slash"> / </span>
            {tField(s, "name", lang)}
          </h1>
          <p className="muted">{tField(s, "blurb", lang)}</p>
          <p className={`dev-flag ${ready ? "ready" : "outline"}`}>{ready ? t("courseReady") : t("outlineReady")}</p>
        </div>
      </div>

      {continueItem && ready && (
        <p className="course-continue">
          <Link className="btn btn-primary" to={`/knowledge/${continueItem.id}`}>
            {t("continueLesson")}
            {" · "}
            {tField(continueItem, "title", lang)}
          </Link>
        </p>
      )}

      <div className="course-outline">
        {chapters.map((ch, index) => {
          const chSections = flattenSections([ch]);
          const chKnowledge = chSections.map((sec) => findKnowledge(knowledge, sec)).filter(Boolean);
          const mastered = chKnowledge.filter((k) => k.status === "mastered").length;
          const prog = chKnowledge.length ? mastered / chKnowledge.length : 0;
          return (
            <section key={ch.id} id={ch.id} className="chapter-block">
              <header className="chapter-head">
                <div>
                  <div className="unit-code">
                    {t("chapterLabel")} {index + 1}
                    {ch.code ? ` · ${ch.code}` : ""}
                  </div>
                  <h2>{tField(ch, "title", lang)}</h2>
                </div>
                <div className="chapter-tools">
                  {chKnowledge.length > 0 && <span className="muted">{percent(prog, lang)}</span>}
                  {practiceByChapter(ch.id).map((p) => (
                    <Link key={p.id} className="btn" to={`/practice/${p.id}`}>
                      {t("chapterPractice")}
                    </Link>
                  ))}
                  {papersByChapter(ch.id).map((p) => (
                    <Link key={p.id} className="btn" to={`/papers/${p.id}`}>
                      {t("chapterPaper")}
                    </Link>
                  ))}
                </div>
              </header>
              <div className="progress-track" style={{ marginBottom: "0.85rem" }}>
                <div className="progress-fill" style={{ "--p": percent(prog, lang), "--accent": accent }} />
              </div>
              {(ch.note_zh || ch.note_en) && <p className="chapter-note">{tField(ch, "note", lang)}</p>}
              {(ch.units || []).map((unit) => (
                <div key={unit.id} className="unit-group">
                  <h3>
                    {t("unitLabel")}
                    {" · "}
                    {tField(unit, "title", lang)}
                  </h3>
                  <ol className="section-list">
                    {(unit.sections || []).map((sec) => {
                      const k = findKnowledge(knowledge, sec);
                      const label = tField(sec, "title", lang);
                      const tick = k?.status === "mastered" ? "is-mastered" : k?.status === "learning" ? "is-learning" : "is-todo";
                      return (
                        <li key={sec.id} className={tick}>
                          <span className="tick" aria-hidden="true" />
                          {k ? (
                            <Link to={`/knowledge/${k.id}`}>
                              {sec.code ? <span className="sec-code">{sec.code}</span> : null}
                              {label}
                            </Link>
                          ) : (
                            <span>
                              {sec.code ? <span className="sec-code">{sec.code}</span> : null}
                              {label}
                              {!ready && <em className="outline-tag">{t("outlineReady")}</em>}
                            </span>
                          )}
                        </li>
                      );
                    })}
                  </ol>
                </div>
              ))}
            </section>
          );
        })}
      </div>

      {coursePapers.length > 0 && (
        <section className="course-paper-band">
          <p className="kicker">{t("coursePaper")}</p>
          <div className="set-grid">
            {coursePapers.map((p) => (
              <Link key={p.id} className="set-card" to={`/papers/${p.id}`}>
                <h3>{tField(p, "title", lang)}</h3>
                <p className="muted">
                  {t("questionsCount", { n: (p.question_ids || []).length })}
                  {p.time_limit_minutes ? ` · ${t("timeLimit", { n: p.time_limit_minutes })}` : ""}
                </p>
                <p className="muted">{t("unofficial")}</p>
                <span className="btn" style={{ alignSelf: "flex-start" }}>{t("startPaper")}</span>
              </Link>
            ))}
          </div>
        </section>
      )}
    </div>
  );
}
