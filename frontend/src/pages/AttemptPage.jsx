import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api";
import { useLang } from "../context/LanguageContext";
import { AttemptReview } from "./PracticePage";
import { tField } from "../utils";

export default function AttemptPage() {
  const { id } = useParams();
  const { t, lang } = useLang();
  const [item, setItem] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    api
      .attempt(id)
      .then(setItem)
      .catch((e) => setError(e.message));
  }, [id]);

  if (error) return <p>{t("error")}: {error}</p>;
  if (!item) return <p>{t("loading")}</p>;
  const back = item.kind === "paper" ? `/papers/${item.set_id}` : `/practice/${item.set_id}`;
  return (
    <div>
      <nav className="crumb">
        <Link to="/progress">{t("progress")}</Link>
      </nav>
      <AttemptReview attempt={item} title={tField(item, "set_title", lang) || item.set_id} back={back} />
    </div>
  );
}
