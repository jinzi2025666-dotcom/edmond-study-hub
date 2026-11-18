import { createContext, useContext, useState } from "react";

const KEY = "esh-grade";
const GradeContext = createContext(null);

function readGrade() {
  try {
    return localStorage.getItem(KEY) || "9";
  } catch {
    return "9";
  }
}

export function GradeProvider({ children }) {
  const [gradeId, setGradeIdState] = useState(readGrade);

  const setGradeId = (id) => {
    const next = String(id || "9");
    setGradeIdState(next);
    try {
      localStorage.setItem(KEY, next);
    } catch {
      /* ignore */
    }
  };

  return <GradeContext.Provider value={{ gradeId, setGradeId }}>{children}</GradeContext.Provider>;
}

export function useGrade() {
  return useContext(GradeContext) || { gradeId: "9", setGradeId: () => {} };
}
