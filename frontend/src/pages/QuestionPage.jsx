import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api";
import { useLang } from "../context/LanguageContext";
import { useSite } from "../context/SiteContext";
import QuestionCard from "../components/QuestionCard";
import { tField } from "../utils";

export default function QuestionPage() {
  const { id } = useParams();
  const { lang, t } = useLang();
  const { subjects } = useSite();
  const [q, setQ] = useState(null);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    setResult(null);
    api
      .question(id)
      .then(setQ)
      .catch((e) => setError(e.message));
  }, [id]);

  if (error) return <p>{t("error")}: {error}</p>;
  if (!q) return <p>{t("loading")}</p>;
  const subject = subjects.find((s) => s.id === q.subject_id) || {};

  return (
    <div>
      <nav className="crumb">
        <Link to="/">{t("breadcrumbHome")}</Link>
        {" / "}
        <Link to={`/subjects/${q.subject_id}`}>{tField(subject, "name", lang)}</Link>
      </nav>
      <p className="kicker">{t("questions")}</p>
      <h1>{t("retryQuestion")}</h1>
      <QuestionCard
        question={q}
        index={0}
        total={1}
        result={result}
        onCheck={async (ans) => setResult(await api.check(q.id, ans))}
      />
    </div>
  );
}
