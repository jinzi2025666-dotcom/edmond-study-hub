import { useCallback, useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api";
import { useLang } from "../context/LanguageContext";
import { useSite } from "../context/SiteContext";
import QuestionCard from "../components/QuestionCard";
import { tField } from "../utils";

export default function PracticePage() {
  const { id } = useParams();
  const { lang, t } = useLang();
  const { subjects } = useSite();
  const [item, setItem] = useState(null);
  const [results, setResults] = useState({});
  const [answers, setAnswers] = useState({});
  const [attempt, setAttempt] = useState(null);
  const [error, setError] = useState("");
  const [startedAt] = useState(() => new Date().toISOString());

  useEffect(() => {
    setAttempt(null);
    setResults({});
    setAnswers({});
    api
      .set(id)
      .then(setItem)
      .catch((e) => setError(e.message));
  }, [id]);

  const check = async (qid, answer) => {
    setAnswers((cur) => ({ ...cur, [qid]: answer }));
    const res = await api.check(qid, answer);
    setResults((cur) => ({ ...cur, [qid]: res }));
  };

  const saveAttempt = async () => {
    const att = await api.submitSet(id, answers, startedAt);
    setAttempt(att);
  };

  if (error) return <p>{t("error")}: {error}</p>;
  if (!item) return <p>{t("loading")}</p>;
  const subject = subjects.find((s) => s.id === item.subject_id) || {};

  if (attempt) {
    return <AttemptReview attempt={attempt} title={tField(item, "title", lang)} back={`/practice/${id}`} />;
  }

  const checked = Object.keys(results).length;

  return (
    <div>
      <nav className="crumb">
        <Link to="/">{t("breadcrumbHome")}</Link>
        {" / "}
        <Link to={`/subjects/${item.subject_id}`}>{tField(subject, "name", lang)}</Link>
        {" / "}
        {tField(item, "title", lang)}
      </nav>
      <p className="kicker">{t("practice")}</p>
      <h1>{tField(item, "title", lang)}</h1>
      <p className="muted">{t("questionsCount", { n: (item.questions || []).length })}</p>
      {(item.questions || []).map((q, i) => (
        <QuestionCard
          key={q.id}
          question={q}
          index={i}
          total={item.questions.length}
          initialAnswer={answers[q.id] || ""}
          result={results[q.id]}
          onCheck={(ans) => check(q.id, ans)}
        />
      ))}
      <div className="btn-row">
        <button type="button" className="btn btn-primary" onClick={saveAttempt} disabled={checked === 0}>
          {t("submitPractice")}
        </button>
      </div>
    </div>
  );
}

export function AttemptReview({ attempt, title, back }) {
  const { lang, t } = useLang();
  return (
    <div>
      <div className="result-banner">
        <p className="kicker">{t("score")}</p>
        <h1>{title}</h1>
        <strong>
          {attempt.score} / {attempt.max_score}
        </strong>
        <div className="btn-row" style={{ marginTop: "0.8rem" }}>
          <Link className="btn" to={back}>
            {t("retry")}
          </Link>
          <Link className="btn" to="/progress">
            {t("progress")}
          </Link>
        </div>
      </div>
      {(attempt.answers || []).map((row, i) => (
        <QuestionCard
          key={row.question_id}
          question={row.question}
          index={i}
          total={(attempt.answers || []).length}
          locked
          initialAnswer={row.given ?? ""}
          result={{
            correct: row.correct,
            answer: row.question?.answer,
            explanation_zh: row.question?.explanation_zh,
            explanation_en: row.question?.explanation_en,
          }}
        />
      ))}
    </div>
  );
}
