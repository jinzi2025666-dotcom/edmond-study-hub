import { useCallback, useEffect, useRef, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api";
import { useLang } from "../context/LanguageContext";
import { useSite } from "../context/SiteContext";
import QuestionCard from "../components/QuestionCard";
import { AttemptReview } from "./PracticePage";
import { tField } from "../utils";

export default function PaperPage() {
  const { id } = useParams();
  const { lang, t } = useLang();
  const { subjects } = useSite();
  const [item, setItem] = useState(null);
  const [answers, setAnswers] = useState({});
  const [attempt, setAttempt] = useState(null);
  const [error, setError] = useState("");
  const [useTimer, setUseTimer] = useState(false);
  const [remaining, setRemaining] = useState(null);
  const [timeUp, setTimeUp] = useState(false);
  const [startedAt] = useState(() => new Date().toISOString());
  const answersRef = useRef(answers);
  answersRef.current = answers;

  useEffect(() => {
    setAttempt(null);
    setAnswers({});
    setUseTimer(false);
    setRemaining(null);
    setTimeUp(false);
    api
      .set(id)
      .then(setItem)
      .catch((e) => setError(e.message));
  }, [id]);

  const storeAnswer = useCallback((qid, value) => {
    setAnswers((cur) => ({ ...cur, [qid]: value }));
  }, []);

  const submit = useCallback(async () => {
    const att = await api.submitSet(id, answersRef.current, startedAt);
    setAttempt(att);
  }, [id, startedAt]);

  useEffect(() => {
    if (!useTimer || remaining == null || attempt) return undefined;
    if (remaining <= 0) {
      setTimeUp(true);
      submit();
      return undefined;
    }
    const h = setTimeout(() => setRemaining((n) => n - 1), 1000);
    return () => clearTimeout(h);
  }, [useTimer, remaining, attempt, submit]);

  if (error) return <p>{t("error")}: {error}</p>;
  if (!item) return <p>{t("loading")}</p>;
  const subject = subjects.find((s) => s.id === item.subject_id) || {};

  if (attempt) {
    return <AttemptReview attempt={attempt} title={tField(item, "title", lang)} back={`/papers/${id}`} />;
  }

  const mm = remaining != null ? Math.floor(remaining / 60) : 0;
  const ss = remaining != null ? remaining % 60 : 0;

  return (
    <div>
      <nav className="crumb">
        <Link to="/">{t("breadcrumbHome")}</Link>
        {" / "}
        <Link to={`/subjects/${item.subject_id}`}>{tField(subject, "name", lang)}</Link>
        {" / "}
        {tField(item, "title", lang)}
      </nav>
      <p className="kicker">{t("papers")}</p>
      <h1>{tField(item, "title", lang)}</h1>
      <p className="muted">{t("unofficial")}</p>
      <p className="muted">
        {t("questionsCount", { n: (item.questions || []).length })}
        {item.time_limit_minutes ? ` · ${t("timeLimit", { n: item.time_limit_minutes })}` : ""}
      </p>

      {item.time_limit_minutes && !useTimer && (
        <div className="btn-row" style={{ margin: "0.8rem 0 1rem" }}>
          <span className="muted">{t("optionalTimer")}</span>
          <button
            type="button"
            className="btn"
            onClick={() => {
              setUseTimer(true);
              setRemaining(item.time_limit_minutes * 60);
            }}
          >
            {t("startTimer")}
          </button>
        </div>
      )}
      {useTimer && remaining != null && (
        <p className={`timer ${remaining < 60 ? "warn" : ""}`}>
          {t("remaining")}: {mm}:{String(ss).padStart(2, "0")}
        </p>
      )}
      {timeUp && <p className="feedback bad">{t("timeUp")}</p>}

      {(item.questions || []).map((q, i) => (
        <QuestionCard
          key={q.id}
          question={q}
          index={i}
          total={item.questions.length}
          mode="paper"
          onCheck={storeAnswer}
        />
      ))}
      <div className="btn-row">
        <button type="button" className="btn btn-primary" onClick={submit}>
          {t("submitPaper")}
        </button>
      </div>
    </div>
  );
}
