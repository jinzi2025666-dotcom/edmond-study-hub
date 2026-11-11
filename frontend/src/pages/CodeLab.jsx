import { useEffect, useRef, useState } from "react";
import { api } from "../api";
import { useLang } from "../context/LanguageContext";
import MarkdownBody from "../components/MarkdownBody";
import { tField } from "../utils";

export default function CodeLab() {
  const { lang, t } = useLang();
  const [exercises, setExercises] = useState([]);
  const [current, setCurrent] = useState(null);
  const [code, setCode] = useState("");
  const [output, setOutput] = useState("");
  const [status, setStatus] = useState("loading"); // loading | ready | error
  const [running, setRunning] = useState(false);
  const [results, setResults] = useState([]);
  const [showSolution, setShowSolution] = useState(false);
  const pyodideRef = useRef(null);

  useEffect(() => {
    api.coding().then((rows) => {
      setExercises(rows || []);
      if (rows && rows[0]) {
        setCurrent(rows[0]);
        setCode(rows[0].starter || "");
      }
    });
  }, []);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        // A blocked network can hang instead of erroring, so give up after 20 s.
        const timeout = (ms) => new Promise((_, reject) => setTimeout(() => reject(new Error("timeout")), ms));
        const load = async () => {
          if (!window.loadPyodide) {
            await new Promise((resolve, reject) => {
              const s = document.createElement("script");
              s.src = "https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js";
              s.onload = resolve;
              s.onerror = reject;
              document.head.appendChild(s);
            });
          }
          return window.loadPyodide({ indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.2/full/" });
        };
        const py = await Promise.race([load(), timeout(20000)]);
        if (!cancelled) {
          pyodideRef.current = py;
          setStatus("ready");
        }
      } catch {
        if (!cancelled) setStatus("error");
      }
    })();
    return () => {
      cancelled = true;
    };
  }, []);

  const runWithStdin = async (source, stdin) => {
    const py = pyodideRef.current;
    const launcher = `
import sys, io, traceback
_stdin = ${JSON.stringify(stdin || "")}
_src = ${JSON.stringify(source)}
sys.stdin = io.StringIO(_stdin)
sys.stdout = io.StringIO()
sys.stderr = io.StringIO()
_err = ""
try:
    exec(compile(_src, "<student>", "exec"), {"__name__": "__main__"})
except Exception:
    _err = traceback.format_exc()
_out = sys.stdout.getvalue()
_err2 = sys.stderr.getvalue()
`;
    await py.runPythonAsync(launcher);
    const out = py.globals.get("_out") || "";
    const err = (py.globals.get("_err") || "") + (py.globals.get("_err2") || "");
    return { out, err };
  };

  const run = async () => {
    if (!pyodideRef.current) return;
    setRunning(true);
    setResults([]);
    try {
      const tests = current?.tests || [{ stdin: "", stdout: null }];
      const collected = [];
      let lastOut = "";
      for (const test of tests) {
        const { out, err } = await runWithStdin(code, test.stdin || "");
        lastOut = err ? err : out;
        const expected = test.stdout;
        const pass =
          expected == null
            ? !err
            : normalizeOut(out) === normalizeOut(expected) && !err;
        collected.push({ ...test, out, err, pass });
      }
      setOutput(lastOut || "(no output)");
      setResults(collected);
    } catch (e) {
      setOutput(String(e));
    } finally {
      setRunning(false);
    }
  };

  return (
    <div>
      <p className="kicker">{t("codeLab")}</p>
      <h1>{t("codeLab")}</h1>
      <p>{t("codeLabIntro")}</p>
      {status === "loading" && <p className="muted">{t("loadingPython")}</p>}
      {status === "error" && (
        <div className="empty" role="status">
          {import.meta.env.VITE_OFFLINE ? t("pythonOffline") : t("pythonError")}
        </div>
      )}

      <div className="code-layout">
        <div>
          <p className="kicker">{t("starterExercises")}</p>
          <div className="ex-list">
            {exercises.map((ex) => (
              <button
                key={ex.id}
                type="button"
                className={current?.id === ex.id ? "active" : ""}
                onClick={() => {
                  setCurrent(ex);
                  setCode(ex.starter || "");
                  setOutput("");
                  setResults([]);
                  setShowSolution(false);
                }}
              >
                {tField(ex, "title", lang)}
              </button>
            ))}
          </div>
          {current && <MarkdownBody>{tField(current, "brief", lang)}</MarkdownBody>}
          <div className="btn-row" style={{ margin: "0.6rem 0" }}>
            <button type="button" className="btn" onClick={() => setCode(current?.starter || "")}>
              {t("useStarter")}
            </button>
            <button type="button" className="btn btn-primary" disabled={status !== "ready" || running} onClick={run}>
              {running ? t("running") : t("run")}
            </button>
          </div>
          <textarea className="code-editor" value={code} onChange={(e) => setCode(e.target.value)} spellCheck={false} aria-label="Python" />
          {current?.solution && (
            <div style={{ marginTop: "0.8rem" }}>
              <button type="button" className="btn" aria-expanded={showSolution} onClick={() => setShowSolution((v) => !v)}>
                {showSolution ? t("hideSolution") : t("showSolution")}
              </button>
              {showSolution && (
                <>
                  <p className="kicker" style={{ marginTop: "0.8rem" }}>{t("referenceSolution")}</p>
                  <pre className="output-box">{current.solution}</pre>
                </>
              )}
            </div>
          )}
        </div>
        <div>
          <p className="kicker">{t("output")}</p>
          <pre className="output-box">{output}</pre>
          {results.length > 0 && (
            <div>
              <p className="kicker" style={{ marginTop: "1rem" }}>
                {t("tests")}
              </p>
              {results.map((r, i) => (
                <div key={i} className="test-row">
                  <span>
                    {t("stdin")}: {JSON.stringify(r.stdin || "")}
                  </span>
                  <strong className={r.pass ? "feedback ok" : "feedback bad"}>{r.pass ? t("passed") : t("failed")}</strong>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

function normalizeOut(s) {
  return String(s || "").replace(/\r\n/g, "\n").replace(/[ \t]+$/gm, "").trim() + "\n";
}
