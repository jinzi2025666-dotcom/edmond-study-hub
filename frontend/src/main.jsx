import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, HashRouter } from "react-router-dom";
import App from "./App";
import { LanguageProvider } from "./context/LanguageContext";
import { ThemeProvider } from "./context/ThemeContext";
import { SiteProvider } from "./context/SiteContext";
import { GradeProvider } from "./context/GradeContext";

import "@fontsource/fraunces/latin-400.css";
import "@fontsource/fraunces/latin-600.css";
import "@fontsource/fraunces/latin-700.css";
import "@fontsource/source-sans-3/latin-400.css";
import "@fontsource/source-sans-3/latin-500.css";
import "@fontsource/source-sans-3/latin-600.css";
import "@fontsource/source-sans-3/latin-700.css";
import "katex/dist/katex.min.css";
import "./index.css";

// file:// cannot serve deep paths, so the offline build uses #/ routes.
const Router = import.meta.env.VITE_OFFLINE ? HashRouter : BrowserRouter;

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <ThemeProvider>
      <LanguageProvider>
        <SiteProvider>
          <GradeProvider>
            <Router>
              <App />
            </Router>
          </GradeProvider>
        </SiteProvider>
      </LanguageProvider>
    </ThemeProvider>
  </React.StrictMode>
);
