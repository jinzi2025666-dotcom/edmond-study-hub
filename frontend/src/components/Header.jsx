import { NavLink, useNavigate } from "react-router-dom";
import { useLang } from "../context/LanguageContext";
import { useTheme } from "../context/ThemeContext";
import { useSite } from "../context/SiteContext";
import { tField } from "../utils";
import { useState } from "react";

export default function Header() {
  const { lang, toggle, t } = useLang();
  const { theme, toggle: toggleTheme } = useTheme();
  const { config } = useSite();
  const navigate = useNavigate();
  const [q, setQ] = useState("");

  const onSearch = (e) => {
    e.preventDefault();
    const query = q.trim();
    if (query) navigate(`/search?q=${encodeURIComponent(query)}`);
  };

  return (
    <header className="site-header">
      <a className="skip-link" href="#main">
        {t("skip")}
      </a>
      <div className="header-inner">
        <NavLink to="/" className="brand">
          <span className="brand-name">{tField(config || {}, "name", lang) || "Edmond Study Hub"}</span>
          <span className="brand-sub">{tField(config || {}, "subtitle", lang)}</span>
        </NavLink>
        <div className="header-tools">
          <form className="search-form" onSubmit={onSearch} role="search">
            <label className="visually-hidden" htmlFor="site-search" style={{ position: "absolute", width: 1, height: 1, overflow: "hidden", clip: "rect(0 0 0 0)" }}>
              {t("search")}
            </label>
            <input
              id="site-search"
              value={q}
              onChange={(e) => setQ(e.target.value)}
              placeholder={t("searchPlaceholder")}
            />
            <button className="btn" type="submit">
              {t("search")}
            </button>
          </form>
          <button type="button" className="text-btn" onClick={toggle} aria-label={t("langLabel")}>
            {t("langToggle")}
          </button>
          <button type="button" className="text-btn" onClick={toggleTheme} aria-label={t("themeToggle")}>
            {theme === "light" ? t("themeDark") : t("themeLight")}
          </button>
        </div>
        <nav className="header-nav" aria-label="Main">
          <NavLink to="/" end>
            {t("home")}
          </NavLink>
          <NavLink to="/progress">{t("progress")}</NavLink>
          <NavLink to="/mistakes">{t("mistakes")}</NavLink>
          <NavLink to="/admin">{t("admin")}</NavLink>
        </nav>
      </div>
    </header>
  );
}
