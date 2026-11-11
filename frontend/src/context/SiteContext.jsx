import { createContext, useContext, useEffect, useState } from "react";
import { api } from "../api";

const SiteContext = createContext(null);

export function SiteProvider({ children }) {
  const [config, setConfig] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    api
      .config()
      .then(setConfig)
      .catch((err) => setError(err.message));
  }, []);

  return (
    <SiteContext.Provider value={{ config, subjects: config?.subjects || [], grades: config?.grades || [], error }}>
      {children}
    </SiteContext.Provider>
  );
}

export function useSite() {
  return useContext(SiteContext);
}
