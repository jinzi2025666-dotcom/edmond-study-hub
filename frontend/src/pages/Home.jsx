import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api";
import { useLang } from "../context/LanguageContext";
import { useSite } from "../context/SiteContext";
import { useGrade } from "../context/GradeContext";
import SubjectIcon from "../components/SubjectIcon";
import { formatDate, percent, subjectPath, tField } from "../utils";

export default function Home() {
  const { lang, t } = useLang();
  const { config, subjects, grades } = useSite();
  const { gradeId, setGradeId } = useGrade();
  const [rows, setRows] = useState([]);
  const [updates, setUpdates] = useState([]);
  const [cont, setCont] = useState(null);
  const [progress, setProgress] = useState(null);

  const gradeList = grades.length ? grades : [
    { id: "7", name_zh: "七年级", name_en: "Year 7", status: "upcoming" },
    { id: "8", name_zh: "八年级", name_en: "Year 8", status: "active" },
    { id: "9", name_zh: "九年级", name_en: "Year 9", status: "upcoming" },
  ];
  const currentGrade = gradeList.find((g) => g.id === gradeId) || gradeList.find((g) => g.id === "8");
  const gradeReady = (currentGrade?.status || "upcoming") === "active";

  useEffect(() => {
    api.subjects(gradeId).then(setRows).catch(() => setRows([]));
    api.updates().then(setUpdates).catch(() => setUpdates([]));
    api.continue().then(setCont).catch(() => setCont(null));
    api.progress().then(setProgress).catch(() => setProgress(null));
  }, [gradeId]);

  const overall = progress?.overall || { knowledge: 0, mastered: 0, progress: 0 };
  const name = tField(config || {}, "name", lang);
  const subjectName = (id) => tField(subjects.find((s) => s.id === id) || {}, "name", lang);
  const cards = rows.length ? rows : subjects;

  return (
    <>
      <header className="masthead">
        <p className="kicker">{tField(config || {}, "subtitle", lang)}</p>
        <h1>{name}</h1>
        <p className="lede">
          {lang === "zh"
            ? "先选年级，再按科目进入课程。八年级物理已按章、单元、小节写完，可直接开课。"
            : "Choose a year first, then open a subject. Year 8 Physics is written chapter by chapter, ready to study."}
        </p>
      </header>

      <section className="grade-switch" aria-label={t("selectGrade")}>
        <p className="kicker">{t("selectGrade")}</p>
        <div className="grade-pills" role="tablist">
          {gradeList.map((g) => (
            <button
              key={g.id}
              type="button"
              role="tab"
              aria-selected={g.id === gradeId}
              className={g.id === gradeId ? "is-active" : ""}
              onClick={() => setGradeId(g.id)}
            >
              <strong>{tField(g, "name", lang)}</strong>
              <span>{tField(g, "stage", lang)}</span>
            </button>
          ))}
        </div>
      </section>

      {gradeReady && (
        <div className="home-grid">
          <section className="panel">
            <p className="kicker">{t("continue")}</p>
            {cont && cont.id ? (
              <>
                <h2>
                  <Link to={`/knowledge/${cont.id}`}>{tField(cont, "title", lang)}</Link>
                </h2>
                <p className="muted">
                  {t("continueHint")} {subjectName(cont.subject_id)}
                  {cont.status && cont.status !== "not_started" ? ` · ${t(cont.status)}` : ""}
                </p>
                <Link className="btn btn-primary" to={`/knowledge/${cont.id}`} style={{ display: "inline-block", marginTop: "0.4rem" }}>
                  {t("continueLesson")}
                </Link>
              </>
            ) : (
              <>
                <p>{t("continueEmpty")}</p>
                <Link className="btn btn-primary" to={subjectPath(gradeId, "physics")} style={{ display: "inline-block", marginTop: "0.4rem" }}>
                  {t("physicsShortcut")}
                </Link>
              </>
            )}
          </section>

          <section className="panel">
            <p className="kicker">{t("overall")}</p>
            <h2>{t("masteredOf", { m: overall.mastered, t: overall.knowledge })}</h2>
            <div className="progress-track" style={{ margin: "0.6rem 0 0.2rem" }}>
              <div className="progress-fill" style={{ "--p": percent(overall.progress, lang), "--accent": "var(--copper)" }} />
            </div>
            <div className="snapshot">
              <div>
                <span className="muted">{t("snapshotMistakes")}</span>
                <strong>{progress?.open_mistakes ?? "—"}</strong>
              </div>
              <div>
                <span className="muted">{t("snapshotAttempts")}</span>
                <strong>{progress?.attempts?.length ?? "—"}</strong>
              </div>
              <div>
                <span className="muted">{t("overall")}</span>
                <strong>{percent(overall.progress, lang)}</strong>
              </div>
            </div>
          </section>
        </div>
      )}

      <section>
        <p className="kicker">{tField(currentGrade || {}, "name", lang)} · {t("subjects")}</p>
        {!gradeReady ? (
          <div className="empty coming-soon">
            <h2>{t("comingSoon")}</h2>
            <p>{t("comingSoonBody")}</p>
          </div>
        ) : (
          <div className="subject-grid">
            {cards.map((s) => {
              const counts = s.counts || {};
              const p = percent(counts.progress || 0, lang);
              const status = s.development_status || (s.development || {})[gradeId] || "outline";
              const ready = status === "ready";
              return (
                <Link key={s.id} to={subjectPath(gradeId, s.id)} className={`subject-card ${ready ? "is-ready" : "is-outline"}`} style={{ "--accent": s.accent }}>
                  <SubjectIcon id={s.id} size={30} />
                  <h3>{tField(s, "name", lang)}</h3>
                  <p>{tField(s, "blurb", lang)}</p>
                  <div className="progress-track">
                    <div className="progress-fill" style={{ "--p": p, "--accent": s.accent }} />
                  </div>
                  <span className="muted" style={{ fontSize: "0.82rem" }}>
                    {ready
                      ? t("masteredOf", { m: counts.mastered || 0, t: counts.knowledge || 0 })
                      : t("outlineReady")}
                  </span>
                </Link>
              );
            })}
          </div>
        )}
      </section>
      {gradeReady && (
        <section style={{ marginBottom: "2.2rem" }}>
          <p className="kicker">{t("thisWeek")}</p>
          {updates.slice(0, 6).length === 0 ? (
            <div className="empty">
              {t("thisWeekEmpty")}{" "}
              <Link to="/admin">{t("updateContent")}</Link>
            </div>
          ) : (
            <ol className="update-list">
              {updates.slice(0, 6).map((item) => (
                <li key={`${item.type}-${item.id}`}>
                  <div className="update-meta">
                    <span>{formatDate(item.published_at, lang)}</span>
                    <span>{subjectName(item.subject_id)}</span>
                    <span>
                      {item.type === "knowledge" ? t("weekItemKnowledge") : item.type === "paper" ? t("weekItemPaper") : t("weekItemPractice")}
                    </span>
                  </div>
                  <Link
                    to={
                      item.type === "knowledge"
                        ? `/knowledge/${item.id}`
                        : item.type === "paper"
                          ? `/papers/${item.id}`
                          : `/practice/${item.id}`
                    }
                  >
                    {tField(item, "title", lang)}
                  </Link>
                </li>
              ))}
            </ol>
          )}
        </section>
      )}

    </>
  );
}