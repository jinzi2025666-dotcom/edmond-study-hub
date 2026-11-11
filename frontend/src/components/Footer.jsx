import { Link } from "react-router-dom";
import { useLang } from "../context/LanguageContext";

export default function Footer() {
  const { t } = useLang();
  return (
    <footer className="site-footer">
      <div className="footer-inner">
        <span>{t("footerNote")}</span>
        <span>
          <Link to="/progress">{t("progress")}</Link>
          {" · "}
          <Link to="/mistakes">{t("mistakes")}</Link>
          {" · "}
          <Link to="/admin">{t("updateContent")}</Link>
        </span>
      </div>
    </footer>
  );
}
