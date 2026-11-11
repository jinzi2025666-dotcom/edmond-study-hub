import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api";
import { useLang } from "../context/LanguageContext";
import { useSite } from "../context/SiteContext";
import QuestionCard from "../components/QuestionCard";
import { useGrade } from "../context/GradeContext";
import { formatDateTime, subjectPath, tField } from "../utils";

export default function MistakesPage() {
  const { lang, t } = useLang();
  const { gradeId } = useGrade();
  const { subjects } = useSite();
  const [subject, setSubject] = useState("");
  const [status, setStatus] = useState("open");
  const [rows, setRows] = useState([]);
  const [results, setResults] = useState({});
  const [error, setError] = useState("");

  const load = () => {
    api
      .mistakes({ subject: subject || undefined, status })
      .then(setRows)
      .catch((e) => setError(e.message));
  };

  useEffect(() => {
    load();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [subject, status]);

  return (
    <div>
      <p className="kicker">{t("mistakes")}</p>
      <h1>{t("mistakes")}</h1>
      <p className="muted"><Link to={subjectPath(gradeId, "physics")}>{t("physicsShortcut")}</Link></p>
      <div className="filter-row">
        <label>
          {t("filterSubject")}{" "}
          <select value={subject} onChange={(e) => setSubject(e.target.value)}>
            <option value="">{t("allSubjects")}</option>
            {subjects.map((s) => (
              <option key={s.id} value={s.id}>
                {tField(s, "name", lang)}
              </option>
            ))}
          </select>
        </label>
        <button type="button" className="btn" onClick={() => setStatus(status === "open" ? "all" : "open")}>
          {status === "open" ? t("showArchived") : t("hideArchived")}
        </button>
      </div>
      {error && <p>{t("error")}: {error}</p>}
      {rows.length === 0 && <div className="empty">{t("mistakesEmpty")}</div>}
      {rows.map((m) => (
        <section key={m.question_id} style={{ marginBottom: "1.4rem" }}>
          <p className="muted">
            {tField(subjects.find((s) => s.id === m.subject_id) || {}, "name", lang)} · {formatDateTime(m.updated_at, lang)}
            {m.status === "mastered" ? ` · ${t("archived")}` : ""}
            {m.given_answer ? ` · ${t("yourAnswer")}: ${m.given_answer}` : ""}
          </p>
          {m.question && (
            <QuestionCard
              question={m.question}
              result={results[m.question_id]}
              onCheck={async (ans) => {
                const res = await api.check(m.question_id, ans);
                setResults((cur) => ({ ...cur, [m.question_id]: res }));
                if (res.correct) load();
              }}
            />
          )}
          {m.status !== "mastered" && (
            <button
              type="button"
              className="btn"
              onClick={async () => {
                await api.masterMistake(m.question_id);
                load();
              }}
            >
              {t("markMistakeDone")}
            </button>
          )}
        </section>
      ))}
    </div>
  );
}
