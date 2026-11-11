import { useEffect, useState } from "react";
import { useLang } from "../context/LanguageContext";
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

  useEffect(() => {
    setAnswer(initialAnswer ?? "");
  }, [question?.id, initialAnswer]);

  if (!question) return null;
  const typ = question.type || "short";
  const disabled = locked || Boolean(result);
  const typeHint = typ === "mcq" ? t("typeMcq") : typ === "numeric" ? t("typeNumeric") : typ === "structured" ? t("typeStructured") : t("typeShort");

  return (
    <article className="question">
      <div className="q-meta">
        {index != null ? `${index + 1}${total ? ` / ${total}` : ""} · ` : ""}
        {typeHint}
        {question.marks ? ` · ${t("marksCount", { n: question.marks })}` : ""}
      </div>
      <MarkdownBody>{tField(question, "stem", lang)}</MarkdownBody>

      {typ === "mcq" && (
        <div className="options" role="radiogroup" aria-label={t("option")}>
          {(question.options || []).map((opt) => {
            const selected = answer === opt.id;
            let cls = "option";
            if (result && selected && result.correct) cls += " is-correct";
            if (result && selected && !result.correct) cls += " is-wrong";
            if (result && result.answer === opt.id) cls += " is-correct";
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

      {result && (
        <div className={`feedback ${result.correct ? "ok" : "bad"}`}>
          <strong>{result.correct ? t("correct") : t("incorrect")}</strong>
          {!result.correct && result.answer != null && result.answer !== "" && (
            <div>
              {t("modelAnswer")}: {String(result.answer)}
            </div>
          )}
          {(tField(result, "explanation", lang) || "") && (
            <div>
              <div className="kicker" style={{ marginTop: "0.6rem" }}>
                {t("explanation")}
              </div>
              <MarkdownBody>{tField(result, "explanation", lang)}</MarkdownBody>
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
