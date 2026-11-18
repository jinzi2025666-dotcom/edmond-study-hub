import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api";
import { useLang } from "../context/LanguageContext";
import { useGrade } from "../context/GradeContext";
import QuestionCard from "../components/QuestionCard";
import { subjectPath } from "../utils";

export default function ReviewPage() {
  const { subjectId, gradeId = "9" } = useParams();
  const { setGradeId } = useGrade();
  const { t } = useLang();
  const [pack, setPack] = useState(null);
  const [results, setResults] = useState({});
  const [done, setDone] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    if (gradeId) setGradeId(gradeId);
  }, [gradeId, setGradeId]);

  useEffect(() => {
    api.spiral(subjectId, gradeId).then(setPack).catch((e) => setError(e.message));
  }, [subjectId, gradeId]);

  if (error) return <p>{t("error")}: {error}</p>;
  if (!pack) return <p>{t("loading")}</p>;
  const back = subjectPath(gradeId, subjectId);
  const questions = pack.questions || [];

  return (
    <div>
      <nav className="crumb">
        <Link to="/">{t("breadcrumbHome")}</Link>
        {" / "}
        <Link to={back}>{t("placementBack")}</Link>
        {" / "}
        {t("spiralTitle")}
      </nav>
      <p className="kicker">{t("spiralTitle")}</p>
      <h1>{pack.due ? t("reviewToday") : t("spiralTitle")}</h1>
      <p className="muted">
        {pack.reason === "waiting"
          ? t("spiralWaiting", { n: pack.days || 1 })
          : pack.reason === "steady"
            ? t("spiralSteady")
            : t("spiralLead")}
      </p>
      {questions.map((q, i) => (
        <QuestionCard
          key={q.id}
          question={q}
          index={i}
          total={questions.length}
          result={results[q.id]}
          onCheck={async (ans) => {
            const res = await api.check(q.id, ans);
            setResults((cur) => ({ ...cur, [q.id]: res }));
          }}
        />
      ))}
      {questions.length === 0 && <p>{t("spiralSteady")}</p>}
      <div className="btn-row">
        {pack.due && !done && (
          <button
            type="button"
            className="btn btn-primary"
            onClick={async () => {
              await api.completeSpiral(subjectId, gradeId);
              setDone(true);
            }}
          >
            {t("spiralDone")}
          </button>
        )}
        {done && <p>{t("spiralSaved")}</p>}
        <Link className="btn" to={back}>{t("placementBack")}</Link>
      </div>
    </div>
  );
}
