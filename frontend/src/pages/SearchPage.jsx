import { useEffect, useState } from "react";
import { Link, useSearchParams } from "react-router-dom";
import { api } from "../api";
import { useLang } from "../context/LanguageContext";
import { useSite } from "../context/SiteContext";
import { tField } from "../utils";

export default function SearchPage() {
  const { lang, t } = useLang();
  const { subjects } = useSite();
  const [params, setParams] = useSearchParams();
  const q0 = params.get("q") || "";
  const [q, setQ] = useState(q0);
  const [rows, setRows] = useState([]);
  const [searched, setSearched] = useState(false);

  useEffect(() => {
    setQ(q0);
    if (!q0.trim()) {
      setRows([]);
      setSearched(false);
      return;
    }
    api.search(q0).then((data) => {
      setRows(data || []);
      setSearched(true);
    });
  }, [q0]);

  const submit = (e) => {
    e.preventDefault();
    setParams(q.trim() ? { q: q.trim() } : {});
  };

  return (
    <div className="search-page">
      <p className="kicker">{t("search")}</p>
      <h1>{t("searchResults")}</h1>
      <form className="search-form" onSubmit={submit}>
        <input value={q} onChange={(e) => setQ(e.target.value)} placeholder={t("searchPlaceholder")} />
        <button className="btn btn-primary" type="submit">
          {t("search")}
        </button>
      </form>
      {searched && rows.length === 0 && <div className="empty">{t("noResults")}</div>}
      <ul className="result-list">
        {rows.map((r) => (
          <li key={`${r.type}-${r.id}`}>
            <Link to={r.href || "#"}>
              <div className="muted">
                {r.type} · {tField(subjects.find((s) => s.id === r.subject_id) || {}, "name", lang)}
              </div>
              <h3>{tField(r, "title", lang)}</h3>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
