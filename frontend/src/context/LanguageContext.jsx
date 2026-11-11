import { createContext, useContext, useEffect, useMemo, useState } from "react";
import { tr } from "../i18n";

const LanguageContext = createContext(null);

export function LanguageProvider({ children }) {
  const [lang, setLang] = useState(() => localStorage.getItem("esh-lang") || "zh");

  useEffect(() => {
    localStorage.setItem("esh-lang", lang);
    document.documentElement.lang = lang === "zh" ? "zh-CN" : "en";
    document.documentElement.classList.toggle("zh", lang === "zh");
  }, [lang]);

  const value = useMemo(
    () => ({
      lang,
      setLang,
      toggle: () => setLang((cur) => (cur === "zh" ? "en" : "zh")),
      t: (key, vars) => tr(lang, key, vars),
    }),
    [lang]
  );
  return <LanguageContext.Provider value={value}>{children}</LanguageContext.Provider>;
}

export function useLang() {
  return useContext(LanguageContext);
}
