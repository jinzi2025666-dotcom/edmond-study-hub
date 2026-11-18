import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api";
import { useLang } from "../context/LanguageContext";
import { useGrade } from "../context/GradeContext";
import QuestionCard from "../components/QuestionCard";
import { subjectPath, tField } from "../utils";

export default function PlacementPage() {
  const { subjectId, gradeId = "9" } = useParams();
  const { setGradeId } = useGrade();
  const { lang, t } = useLang();
  const [pack, setPack] = useState(null);
  const [answers, setAnswers] = useState({});
  const [reasons, setReasons] = useState({});
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    if (gradeId) setGradeId(gradeId);
  }, [gradeId, setGradeId]);

  const load = () => {
    setError("");
    api.placement(subjectId, gradeId).then((data) => {
      setPack(data);
      setResult(data.result || null);
    }).catch((e) => setError(e.message));
  };

  useEffect(() => {
    load();
  }, [subjectId, gradeId]);

  const submit = async () => {
    const payload = {};
    (pack?.quiz || []).forEach((q) => {
      payload[q.id] = { answer: answers[q.id] || "", reasoning: reasons[q.id] || "" };
    });
    setBusy(true);
    try {
      setResult(await api.submitPlacement(subjectId, gradeId, payload));
    } catch (e) {
      setError(e.message);
    } finally {
      setBusy(false);
    }
  };

  const retake = async () => {
    await api.resetPlacement(subjectId, gradeId);
    setAnswers({});
    setReasons({});
    setResult(null);
    load();
  };

  if (error) return <p>{t("error")}: {error}</p>;
  if (!pack) return <p>{t("loading")}</p>;
  const back = subjectPath(gradeId, subjectId);

  if (result) {
    const start = result.start;
    return (
      <div className="placement-result">
        <nav className="crumb">
          <Link to="/">{t("breadcrumbHome")}</Link>
          {" / "}
          <Link to={back}>{t("placementBack")}</Link>
          {" / "}
          {t("placementTitle")}
        </nav>
        <p className="kicker">{t("placementTitle")}</p>
        <h1>{result.ready ? t("placementReady") : t("placementRecommend")}</h1>
        {start ? (
          <p className="recommend-start">
            <Link className="btn btn-primary" to={`/knowledge/${start.knowledge_id}`}>
              {tField(start, "title", lang)}
            </Link>
          </p>
        ) : (
          <p>{t("placementReadyBody")}</p>
        )}
        <h2>{t("placementPath")}</h2>
        <ol className="personal-path">
          {(result.path || []).map((row) => (
            <li key={row.section_id} className={`status-${row.status}`}>
              <Link to={`/knowledge/${row.knowledge_id}`}>{tField(row, "title", lang)}</Link>
              <span>{t(`status_${row.status}`)}</span>
            </li>
          ))}
        </ol>
        {(result.path || []).length === 0 && <p className="muted">{t("placementReadyBody")}</p>}
        <h2>{t("placementMap")}</h2>
        <ul className="mastery-map">
          {(result.sections || []).map((row) => (
            <li key={row.section_id} className={`status-${row.status}`}>
              <span>{tField(row, "title", lang)}</span>
              <em>{t(`status_${row.status}`)}</em>
            </li>
          ))}
        </ul>
        <p>{t("placementSyllabus")}</p>
        <div className="btn-row">
          <Link className="btn btn-primary" to={back}>{t("placementBack")}</Link>
          <button type="button" className="btn" onClick={retake}>{t("placementRetake")}</button>
        </div>
      </div>
    );
  }

  const quiz = pack.quiz || [];
  return (
    <div>
      <nav className="crumb">
        <Link to="/">{t("breadcrumbHome")}</Link>
        {" / "}
        <Link to={back}>{t("placementBack")}</Link>
        {" / "}
        {t("placementTitle")}
      </nav>
      <p className="kicker">{t("placementTitle")}</p>
      <h1>{t("placementTitle")}</h1>
      <p className="muted">{t("placementLead")}</p>
      {quiz.map((q, i) => (
        <div key={q.id} className="placement-item">
          <p className="kicker">{tField(q, "section_title", lang) || tField(q, "chapter_title", lang)}</p>
          <QuestionCard
            question={q}
            index={i}
            total={quiz.length}
            mode="paper"
            initialAnswer={answers[q.id] || ""}
            onCheck={(qid, ans) => setAnswers((cur) => ({ ...cur, [qid]: ans }))}
          />
          <label className="reason-box">
            <span>{t("placementWhy")}</span>
            <textarea
              value={reasons[q.id] || ""}
              onChange={(e) => setReasons((cur) => ({ ...cur, [q.id]: e.target.value }))}
            />
          </label>
        </div>
      ))}
      <div className="btn-row">
        <button type="button" className="btn btn-primary" disabled={busy || quiz.length === 0} onClick={submit}>
          {t("placementSubmit")}
        </button>
        <Link className="btn" to={back}>{t("placementSkip")}</Link>
      </div>
    </div>
  );
}
