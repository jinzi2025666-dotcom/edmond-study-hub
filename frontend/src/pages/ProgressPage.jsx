import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api";
import { useLang } from "../context/LanguageContext";
import { useGrade } from "../context/GradeContext";
import { formatDateTime, percent, subjectPath, tField } from "../utils";
import SubjectIcon from "../components/SubjectIcon";

export default function ProgressPage() {
  const { lang, t } = useLang();
  const { gradeId } = useGrade();
  const [data, setData] = useState(null);

  useEffect(() => {
    api.progress().then(setData);
  }, []);

  if (!data) return <p>{t("loading")}</p>;
  const overall = data.overall;

  return (
    <div>
      <p className="kicker">{t("progress")}</p>
      <h1>{t("overall")}</h1>
      <p className="muted"><Link to={subjectPath(gradeId, "physics")}>{t("physicsShortcut")}</Link></p>
      <p>{t("masteredOf", { m: overall.mastered, t: overall.knowledge })}</p>
      <div className="progress-track" style={{ margin: "0.6rem 0 1.4rem" }}>
        <div className="progress-fill" style={{ "--p": percent(overall.progress, lang) }} />
      </div>
      <div className="subject-grid">
        {data.subjects.map((s) => (
          <Link key={s.id} to={subjectPath(gradeId, s.id)} className="subject-card" style={{ "--accent": s.accent }}>
            <SubjectIcon id={s.id} size={26} />
            <h3>{tField(s, "name", lang)}</h3>
            <div className="progress-track">
              <div className="progress-fill" style={{ "--p": percent(s.counts?.progress || 0, lang), "--accent": s.accent }} />
            </div>
            <span className="muted" style={{ fontSize: "0.85rem" }}>
              {t("masteredOf", { m: s.counts?.mastered || 0, t: s.counts?.knowledge || 0 })}
            </span>
          </Link>
        ))}
      </div>

      <h2 style={{ marginTop: "2rem" }}>{t("recentAttempts")}</h2>
      {(!data.attempts || data.attempts.length === 0) && <div className="empty">{t("noAttempts")}</div>}
      <ul className="result-list">
        {(data.attempts || []).map((a) => (
          <li key={a.id}>
            <Link to={`/attempts/${a.id}`}>
              <div className="muted">{formatDateTime(a.submitted_at, lang)}</div>
              <h3>{tField(a, "set_title", lang) || a.set_id}</h3>
              <p className="muted">{t("historyScore", { s: a.score, m: a.max_score })}</p>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
