import { Link } from "react-router-dom";
import { useLang } from "../context/LanguageContext";

export default function NotFound() {
  const { t } = useLang();
  return (
    <div className="masthead">
      <p className="kicker">404</p>
      <h1>{t("notFoundTitle")}</h1>
      <p>{t("notFoundBody")}</p>
      <Link className="btn btn-primary" to="/">
        {t("backHome")}
      </Link>
    </div>
  );
}
