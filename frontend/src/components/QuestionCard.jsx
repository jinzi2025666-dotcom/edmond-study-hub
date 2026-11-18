import { useEffect, useState } from "react";
import { useLang } from "../context/LanguageContext";
import { api } from "../api";
import { tField } from "../utils";
import MarkdownBody from "./MarkdownBody";

export default function QuestionCard({
  question,
  index,
  total,
  mode = "practice",
  locked = false,
  initialAnswer = "",
  result,
  onCheck,
  checking,
}) {
  const { lang, t } = useLang();
  const [answer, setAnswer] = useState(initialAnswer ?? "");
  const [step, setStep] = useState(0);
  const [revealed, setRevealed] = useState(null);

  useEffect(() => {
    setAnswer(initialAnswer ?? "");
    setStep(0);
    setRevealed(null);
  }, [question?.id, initialAnswer, result?.correct]);

  if (!question) return null;
  const shown = revealed ? { ...result, ...revealed } : result;
  const showSolution = Boolean(shown?.correct) || step >= 2;
  const typ = question.type || "short";
  const disabled = locked || Boolean(result);
  const typeHint = typ === "mcq" ? t("typeMcq") : typ === "numeric" ? t("typeNumeric") : typ === "structured" ? t("typeStructured") : t("typeShort");

  return (
    <article className="question">
      <div className="q-meta">
        {index != null ? `${index + 1}${total ? ` / ${total}` : ""} · ` : ""}
        {typeHint}
        {question.marks ? ` · ${t("marksCount", { n: question.marks })}` : ""}
        {question.difficulty ? ` · ${t(`diff_${question.difficulty}`)}` : ""}
      </div>
      <MarkdownBody>{tField(question, "stem", lang)}</MarkdownBody>

      {typ === "mcq" && (
        <div className="options" role="radiogroup" aria-label={t("option")}>
          {(question.options || []).map((opt) => {
            const selected = answer === opt.id;
            let cls = "option";
            if (shown && selected && shown.correct) cls += " is-correct";
            if (shown && selected && !shown.correct) cls += " is-wrong";
            if (showSolution && shown?.answer === opt.id) cls += " is-correct";
            return (
              <label key={opt.id} className={cls}>
                <input
                  type="radio"
                  name={`q-${question.id}`}
                  value={opt.id}
                  checked={selected}
                  disabled={disabled}
                  onChange={() => setAnswer(opt.id)}
                />
                <span>
                  <strong style={{ marginRight: "0.4rem" }}>{(opt.id || "").toUpperCase()}.</strong>
                  {lang === "zh" ? opt.zh || opt.en : opt.en || opt.zh}
                </span>
              </label>
            );
          })}
        </div>
      )}

      {typ !== "mcq" && typ !== "structured" && (
        <input
          className="answer-input"
          value={answer}
          disabled={disabled}
          inputMode={typ === "numeric" ? "decimal" : "text"}
          onChange={(e) => setAnswer(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && onCheck && !disabled) {
              e.preventDefault();
              onCheck(answer);
            }
          }}
        />
      )}

      {typ === "structured" && (
        <textarea className="answer-input" value={answer} disabled={disabled} onChange={(e) => setAnswer(e.target.value)} />
      )}

      {mode !== "paper" && !result && onCheck && (
        <div className="btn-row" style={{ marginTop: "0.8rem" }}>
          <button type="button" className="btn btn-primary" disabled={disabled || checking} onClick={() => onCheck(answer)}>
            {t("check")}
          </button>
        </div>
      )}

      {mode === "paper" && !locked && (
        <div style={{ display: "none" }} data-answer={answer} />
      )}

      {shown && (
        <div className={`feedback ${shown.correct ? "ok" : "bad"}`}>
          <strong>{shown.correct ? t("correct") : t("incorrect")}</strong>
          {!shown.correct && !showSolution && (
            <div className="hint-flow">
              <p>{tField(shown, "diagnosis", lang)}</p>
              <p><strong>{t("hintLabel", { n: 1 })}</strong> {tField(shown, "hint1", lang)}</p>
              {step >= 1 && <p><strong>{t("hintLabel", { n: 2 })}</strong> {tField(shown, "hint2", lang)}</p>}
              <div className="btn-row">
                {step < 1 && (
                  <button type="button" className="btn" onClick={() => setStep(1)}>{t("hintStuck")}</button>
                )}
                {step >= 1 && (
                  <button
                    type="button"
                    className="btn"
                    onClick={async () => {
                      const has = shown.explanation_zh || shown.explanation_en || shown.answer;
                      if (!has) {
                        try {
                          setRevealed(await api.reveal(question.id));
                        } catch {
                          /* keep the hints if the solution cannot be loaded */
                        }
                      }
                      setStep(2);
                    }}
                  >
                    {t("hintShow")}
                  </button>
                )}
              </div>
            </div>
          )}
          {showSolution && !shown.correct && shown.answer != null && shown.answer !== "" && (
            <div>
              {t("modelAnswer")}: {String(shown.answer)}
            </div>
          )}
          {showSolution && (tField(shown, "explanation", lang) || "") && (
            <div>
              <div className="kicker" style={{ marginTop: "0.6rem" }}>
                {t("explanation")}
              </div>
              <MarkdownBody>{tField(shown, "explanation", lang)}</MarkdownBody>
            </div>
          )}
        </div>
      )}

      {mode === "paper" && typeof onCheck === "function" && (
        <AnswerBridge questionId={question.id} answer={answer} onCheck={onCheck} />
      )}
    </article>
  );
}

function AnswerBridge({ questionId, answer, onCheck }) {
  useEffect(() => {
    onCheck(questionId, answer);
  }, [questionId, answer, onCheck]);
  return null;
}
