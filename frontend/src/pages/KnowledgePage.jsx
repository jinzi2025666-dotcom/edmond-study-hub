import { useEffect, useMemo, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api";
import { useLang } from "../context/LanguageContext";
import { useSite } from "../context/SiteContext";
import { useGrade } from "../context/GradeContext";
import MarkdownBody from "../components/MarkdownBody";
import QuestionCard from "../components/QuestionCard";
import { flattenSections, subjectPath, tField } from "../utils";

export default function KnowledgePage() {
  const { id } = useParams();
  const { lang, t } = useLang();
  const { subjects } = useSite();
  const { gradeId } = useGrade();
  const [item, setItem] = useState(null);
  const [course, setCourse] = useState(null);
  const [error, setError] = useState("");
  const [results, setResults] = useState({});

  useEffect(() => {
    setItem(null);
    setResults({});
    api
      .knowledge(id)
      .then(async (data) => {
        if (data.status === "not_started") {
          try {
            await api.setKnowledgeStatus(id, "learning");
            data = { ...data, status: "learning" };
          } catch {
            /* ignore */
          }
        }
        setItem(data);
        try {
          const sub = await api.subject(data.subject_id, data.grade_id || gradeId || "8");
          setCourse(sub);
        } catch {
          setCourse(null);
        }
      })
      .catch((e) => setError(e.message));
  }, [id, gradeId]);

  const setStatus = async (status) => {
    await api.setKnowledgeStatus(id, status);
    setItem((cur) => ({ ...cur, status }));
  };

  const nav = useMemo(() => {
    if (!course || !item) return { prev: null, next: null, chapter: null, unit: null, sections: [] };
    const chapters = course.units || [];
    const flat = flattenSections(chapters);
    const idx = flat.findIndex((s) => s.id === item.section_id || s.knowledge_id === item.id || `kp-${s.id}` === item.id);
    const current = idx >= 0 ? flat[idx] : null;
    const chapter = current?.chapter || chapters.find((c) => c.id === item.chapter_id || c.id === item.unit_id);
    const knowledge = course.knowledge || [];
    const linkFor = (sec) => {
      if (!sec) return null;
      const k = knowledge.find((row) => row.id === sec.knowledge_id || row.section_id === sec.id || row.id === `kp-${sec.id}`);
      return k ? { ...sec, href: `/knowledge/${k.id}` } : null;
    };
    return {
      prev: idx > 0 ? linkFor(flat[idx - 1]) : null,
      next: idx >= 0 && idx < flat.length - 1 ? linkFor(flat[idx + 1]) : null,
      chapter,
      unit: current?.unit,
      sections: (chapter?.units || []).flatMap((u) => (u.sections || []).map((s) => ({ ...s, unit: u, href: linkFor(s)?.href }))),
    };
  }, [course, item]);

  if (error) return <p>{t("error")}: {error}</p>;
  if (!item) return <p>{t("loading")}</p>;

  const subject = subjects.find((s) => s.id === item.subject_id) || { id: item.subject_id, accent: "var(--copper)" };
  const gradeKey = item.grade_id || gradeId || "8";
  const gradeName = lang === "zh" ? { 7: "七年级", 8: "八年级", 9: "九年级" }[gradeKey] : { 7: "Year 7", 8: "Year 8", 9: "Year 9" }[gradeKey];
  const structured = item.keypoints_zh || item.keypoints_en || item.difficulties_zh || item.objectives_zh;
  const chapterSets = (course?.practice || []).concat(course?.papers || []).filter((s) => s.chapter_id === item.chapter_id || s.unit_id === item.chapter_id);
  const coursePapers = (course?.papers || []).filter((s) => s.scope === "course" || s.id.includes("comprehensive"));

  const check = async (qid, answer) => {
    const res = await api.check(qid, answer);
    setResults((cur) => ({ ...cur, [qid]: res }));
  };

  return (
    <div className={`lesson-shell ${lang}`} style={{ "--accent": subject.accent }}>
      <article className="knowledge-page lesson-page">
        <nav className="crumb">
          <Link to="/">{t("breadcrumbHome")}</Link>
          {" / "}
          <Link to="/">{gradeName}</Link>
          {" / "}
          <Link to={subjectPath(gradeKey, item.subject_id)}>{tField(subject, "name", lang) || item.subject_id}</Link>
          {nav.chapter && (
            <>
              {" / "}
              <Link to={`${subjectPath(gradeKey, item.subject_id)}#${nav.chapter.id}`}>{tField(nav.chapter, "title", lang)}</Link>
            </>
          )}
          {nav.unit && (
            <>
              {" / "}
              {tField(nav.unit, "title", lang)}
            </>
          )}
        </nav>
        <p className="kicker">{t("sectionLabel")}</p>
        <h1>{tField(item, "title", lang)}</h1>
        {tField(item, "objectives", lang) ? (
          <div className="will-learn">
            <p className="kicker">{t("youWillLearn")}</p>
            <p>{tField(item, "objectives", lang)}</p>
          </div>
        ) : (
          tField(item, "summary", lang) && <p className="lede muted">{tField(item, "summary", lang)}</p>
        )}

        <div className="status-bar">
          <span className={`status-pill ${item.status}`}>{t(item.status === "not_started" ? "notStarted" : item.status)}</span>
          <button type="button" className="btn" onClick={() => setStatus("learning")}>
            {t("markLearning")}
          </button>
          <button type="button" className="btn btn-primary" onClick={() => setStatus("mastered")}>
            {t("markMastered")}
          </button>
        </div>

        {structured ? (
          <>
            {(item.keypoints_zh || item.keypoints_en) && (
              <section className="lesson-block block-keypoints">
                <p className="kicker">{t("keyPoints")}</p>
                <h2>{t("keyPoints")}</h2>
                <MarkdownBody>{tField(item, "keypoints", lang)}</MarkdownBody>
              </section>
            )}
            <section className="lesson-block block-explain">
              <p className="kicker">{t("lessonExplanation")}</p>
              <h2>{t("lessonExplanation")}</h2>
              {item.diagram ? (
                <figure className="lesson-figure" dangerouslySetInnerHTML={{ __html: item.diagram }} />
              ) : null}
              <MarkdownBody>{tField(item, "body", lang)}</MarkdownBody>
            </section>
            {(item.difficulties_zh || item.difficulties_en) && (
              <section className="lesson-block block-difficulties">
                <p className="kicker">{t("difficulties")}</p>
                <h2>{t("difficulties")}</h2>
                <MarkdownBody>{tField(item, "difficulties", lang)}</MarkdownBody>
              </section>
            )}
          </>
        ) : (
          <MarkdownBody>{tField(item, "body", lang)}</MarkdownBody>
        )}

        {item.related_questions?.length > 0 && (
          <section className="lesson-block block-practice" id="lesson-practice">
            <p className="kicker">{t("lessonPractice")}</p>
            <h2>{t("lessonPractice")}</h2>
            {item.related_questions.map((q, i) => (
              <QuestionCard
                key={q.id}
                question={q}
                index={i}
                total={item.related_questions.length}
                result={results[q.id]}
                onCheck={(ans) => check(q.id, ans)}
              />
            ))}
          </section>
        )}

        {(chapterSets.length > 0 || coursePapers.length > 0) && (
          <section className="related-sets">
            <p className="kicker">{t("relatedSets")}</p>
            <div className="related-links">
              {chapterSets.map((s) => (
                <Link key={s.id} className="btn" to={s.kind === "paper" ? `/papers/${s.id}` : `/practice/${s.id}`}>
                  {s.kind === "paper" ? t("chapterPaper") : t("chapterPractice")}
                  {" · "}
                  {tField(s, "title", lang)}
                </Link>
              ))}
              {coursePapers.map((s) => (
                <Link key={s.id} className="btn" to={`/papers/${s.id}`}>
                  {t("coursePaper")}
                </Link>
              ))}
            </div>
          </section>
        )}

        <nav className="lesson-pager">
          {nav.prev ? (
            <Link to={nav.prev.href}>
              <span className="muted">{t("prevLesson")}</span>
              <strong>{tField(nav.prev, "title", lang)}</strong>
            </Link>
          ) : (
            <span />
          )}
          {nav.next ? (
            <Link to={nav.next.href} className="next">
              <span className="muted">{t("nextLesson")}</span>
              <strong>{tField(nav.next, "title", lang)}</strong>
            </Link>
          ) : (
            <span />
          )}
        </nav>
      </article>

      {nav.chapter && nav.sections.length > 0 && (
        <aside className="lesson-toc">
          <details open>
            <summary>
              {t("courseOutline")}
              {" · "}
              {tField(nav.chapter, "title", lang)}
            </summary>
            <ol>
              {nav.sections.map((sec) => (
                <li key={sec.id} className={sec.id === item.section_id || sec.knowledge_id === item.id ? "is-current" : ""}>
                  {sec.href ? <Link to={sec.href}>{tField(sec, "title", lang)}</Link> : <span>{tField(sec, "title", lang)}</span>}
                </li>
              ))}
            </ol>
            <p>
              <Link to={subjectPath(gradeKey, item.subject_id)}>{tField(subject, "name", lang)}</Link>
            </p>
          </details>
        </aside>
      )}
    </div>
  );
}
