/** Shared coaching, placement and spiral-review rules for Grade 9.
 * Hints never include the model answer. The worked solution stays behind the second hint.
 */

const STOP = new Set(
  "the a an of to and or in on for is are was were be this that with from by as it its if so not no yes 的 了 是 在 和 与 或 一个 这个 我们 你 我".split(/\s+/)
);

export function sectionOrder(units) {
  const out = [];
  (units || []).forEach((chapter, ci) => {
    (chapter.units || []).forEach((unit) => {
      (unit.sections || []).forEach((section) => {
        out.push({
          chapter_id: chapter.id,
          chapter_title_zh: chapter.title_zh,
          chapter_title_en: chapter.title_en,
          chapter_index: ci,
          section_id: section.id,
          title_zh: section.title_zh,
          title_en: section.title_en,
          knowledge_id: section.knowledge_id || `kp-${section.id}`,
        });
      });
    });
  });
  return out;
}

export function pickDiagnosticQuestions(questions, units, limit = 8) {
  const order = sectionOrder(units);
  const bySection = new Map();
  (questions || []).forEach((q) => {
    const sid = q.section_id;
    if (!sid || q.grade_id && q.grade_id !== "9") return;
    if (q.difficulty === "unit") return;
    const list = bySection.get(sid) || [];
    list.push(q);
    bySection.set(sid, list);
  });
  const prefer = (list) => {
    const rank = { basic: 0, exam: 1, challenge: 2 };
    return [...list].sort((a, b) => (rank[a.difficulty] ?? 1) - (rank[b.difficulty] ?? 1))[0];
  };
  const chosen = [];
  const used = new Set();
  const take = (meta) => {
    const list = bySection.get(meta.section_id);
    if (!list || used.has(meta.section_id)) return;
    const q = prefer(list);
    if (!q) return;
    used.add(meta.section_id);
    chosen.push({ ...q, ...meta, question_id: q.id });
  };
  const firstOfChapter = new Map();
  order.forEach((meta) => {
    if (!firstOfChapter.has(meta.chapter_id)) firstOfChapter.set(meta.chapter_id, meta);
  });
  firstOfChapter.forEach((meta) => take(meta));
  order.forEach((meta) => {
    if (chosen.length >= limit) return;
    take(meta);
  });
  return chosen.slice(0, limit);
}

function explanationBody(q) {
  const raw = `${q.explanation_zh || ""}\n${q.explanation_en || ""}`;
  return raw.replace(/\*\*评分要点[\s\S]*?\*\*解析\*\*/g, " ").replace(/\*\*Mark scheme[\s\S]*?\*\*Explanation\*\*/g, " ");
}

export function reasoningKeys(q) {
  const keys = [];
  if (q.type === "mcq") {
    const opt = (q.options || []).find((o) => o.id === q.answer);
    if (opt) keys.push(opt.zh, opt.en);
  } else if (q.answer && String(q.answer).length > 1) {
    keys.push(String(q.answer));
  }
  if (q.answer_zh) keys.push(q.answer_zh);
  if (q.answer_en) keys.push(q.answer_en);
  explanationBody(q)
    .split(/[\s,.;:，。；：、!！?？()（）\[\]【】"/“”'’]+/)
    .forEach((word) => {
      const w = word.trim();
      if (w.length >= 2 && !STOP.has(w.toLowerCase())) keys.push(w);
    });
  return [...new Set(keys.map((k) => String(k).trim()).filter((k) => k.length >= 2))].slice(0, 24);
}

export function reasoningOk(q, reasoning) {
  const text = String(reasoning || "").trim().toLowerCase();
  if (text.length < 8) return false;
  return reasoningKeys(q).some((key) => text.includes(String(key).toLowerCase()));
}

export function statusOf(correct, understood) {
  if (!correct) return "gap";
  if (!understood) return "shaky";
  return "solid";
}

export function buildPlacementResult(items, units) {
  const order = sectionOrder(units);
  const bySection = new Map();
  items.forEach((item) => {
    const prev = bySection.get(item.section_id);
    const status = item.status || statusOf(item.correct, item.reasoning_ok);
    if (!prev || rank(status) < rank(prev)) bySection.set(item.section_id, status);
  });
  const annotated = order.map((meta) => ({
    ...meta,
    status: bySection.get(meta.section_id) || "unseen",
  }));
  const gaps = annotated.filter((row) => row.status === "gap");
  const shaky = annotated.filter((row) => row.status === "shaky");
  const unseen = annotated.filter((row) => row.status === "unseen");
  const start = gaps[0] || shaky[0] || unseen[0] || null;
  const path = [...gaps, ...shaky, ...unseen.slice(0, 2)].slice(0, 6);
  return {
    sections: annotated.filter((row) => row.status !== "unseen"),
    start,
    path,
    ready: !gaps.length && !shaky.length && !unseen.length,
  };
}

function rank(status) {
  return { gap: 0, shaky: 1, solid: 2, unseen: 3 }[status] ?? 3;
}

export function diagnose(q, given) {
  const typ = (q.type || "short").toLowerCase();
  const raw = String(given ?? "").trim();
  if (typ === "mcq") {
    const picked = (q.options || []).find((o) => o.id === raw);
    const label = picked ? `${String(picked.id).toUpperCase()}. ${picked.zh || picked.en || ""}` : raw.toUpperCase();
    return {
      diagnosis_zh: picked
        ? `你选了「${label}」。这往往是把邻近概念当成了题目真正在问的那一件事，不一定是完全没读懂。先分清题目问的是定义、方向还是计算。`
        : "还没有一个能对上选项的答案。先把题目里的关键词圈出来。",
      diagnosis_en: picked
        ? `You chose “${picked.en || picked.zh || label}”. That is often a neighbouring idea, not the thing the question actually asks. Separate definition, direction and calculation before you choose again.`
        : "There isn’t a clear option yet. Circle the key words in the question first.",
    };
  }
  if (typ === "numeric") {
    const got = Number(String(raw).replace(/,/g, ""));
    const exp = Number(String(q.answer).replace(/,/g, ""));
    let diagnosis_zh = "数字还没对上。先写出公式，再代入，最后看单位。只写一个看起来眼熟的数，还不能说明方法是对的。";
    let diagnosis_en = "The number does not match yet. Write the formula, substitute, then check the unit. A familiar-looking number is not the same as a method.";
    if (Number.isFinite(got) && Number.isFinite(exp) && exp !== 0) {
      const ratio = got / exp;
      if (Math.abs(ratio - 10) < 0.2 || Math.abs(ratio - 0.1) < 0.02 || Math.abs(ratio - 100) < 2 || Math.abs(ratio - 0.01) < 0.002) {
        diagnosis_zh = "结果的大小差了大约 10 倍或 100 倍。这通常是单位换算（例如 cm 和 m，或 g 和 kg），不是整条公式都错了。";
        diagnosis_en = "The size is off by about 10 or 100. That is usually a unit change, such as cm and m, or g and kg, rather than a wholly wrong formula.";
      } else if (Math.abs(got - exp) / Math.abs(exp) < 0.15) {
        diagnosis_zh = "你已经很接近。差在四舍五入、漏了一项，或最后一步的符号。";
        diagnosis_en = "You are close. The gap is rounding, a missing term, or the sign on the last step.";
      }
    }
    return { diagnosis_zh, diagnosis_en };
  }
  if (typ === "structured") {
    return {
      diagnosis_zh: "长回答里要点还不够。评分看的是几个关键想法是否出现，不是篇幅。先列出两个必须写到的点，再展开。",
      diagnosis_en: "The longer answer is still missing key points. Marks follow those points, not the length. Name two ideas that must appear, then develop them.",
    };
  }
  return {
    diagnosis_zh: "关键词还没对上。先用这节课的术语回答，不要换成一个相近但不相同的说法。",
    diagnosis_en: "The key point is not there yet. Answer with the term from this lesson, not a nearby phrase that is not the same thing.",
  };
}

export function hintsFor(q) {
  const topic = q.title_zh || q.section_id || q.subject_id || "";
  const topicEn = q.title_en || q.section_id || q.subject_id || "";
  return {
    hint1_zh: `先不要看解答。这题属于「${topic}」。把题目里的条件圈出来，问自己：它在考定义、公式，还是一个方向（谁大、向哪边、先做什么）？`,
    hint1_en: `Leave the solution closed. This item sits in “${topicEn}”. Circle the given information and ask whether it is a definition, a formula, or a direction (which is larger, which way, what comes first).`,
    hint2_zh: secondHint(q, "zh"),
    hint2_en: secondHint(q, "en"),
  };
}

function methodHint(q, lang) {
  const typ = (q.type || "short").toLowerCase();
  if (lang === "zh") {
    if (typ === "mcq") return "再想一步：把每个选项翻译成这节课里的一个判断，再看哪一个判断和题目给出的条件方向一致。先不要选那个只是用了相同的词、但问的是另一件事的选项。";
    if (typ === "numeric") return "再想一步：写出这一节的公式，代入题目里的每一个已知量，并检查单位是否一致。最后一步先不要报出数字。";
    if (typ === "structured") return "再想一步：先列出两个必须出现的要点，每个要点用题干里的一个事实支撑。先不要写成完整范文。";
    return "再想一步：用这节课的术语回答，并指出题目里哪一个条件把你带到这个术语。先不要只重复题干。";
  }
  if (typ === "mcq") return "One step further: turn each option into a claim from this lesson, then see which claim matches the condition in the question. Leave aside the option that reuses a word but answers a different question.";
  if (typ === "numeric") return "One step further: write this lesson’s formula, substitute every given value, and check the units agree. Do not write the final number yet.";
  if (typ === "structured") return "One step further: name two points that must appear, and support each with one fact from the question. Do not write the full model answer yet.";
  return "One step further: answer with the term from this lesson, and point to the condition that leads you there. Do not only repeat the question.";
}

function secondHint(q, lang) {
  // The second hint stays on the method. Quoting the explanation here was giving away the working.
  return methodHint(q, lang);
}

export function coachPayload(q, given) {
  return { ...diagnose(q, given), ...hintsFor(q) };
}

export function spiralDue({ placement, mistakes, checkpointAt, lastReviewAt, now = Date.now() }) {
  const weakFromPlacement = (placement?.sections || []).some((s) => s.status === "gap" || s.status === "shaky");
  const weak = weakFromPlacement || (mistakes || 0) > 0;
  if (!weak) {
    return { due: false, reason: "steady" };
  }
  const fortnight = 14 * 24 * 3600 * 1000;
  if (!lastReviewAt) return { due: true, reason: "first" };
  const reviewed = Date.parse(lastReviewAt);
  if (checkpointAt && Date.parse(checkpointAt) > reviewed) return { due: true, reason: "unit" };
  if (now - reviewed >= fortnight) return { due: true, reason: "fortnight" };
  const days = Math.max(1, Math.ceil((fortnight - (now - reviewed)) / (24 * 3600 * 1000)));
  return { due: false, reason: "waiting", days };
}

export function pickSpiralQuestions(pool, placement, mistakeIds, limit = 6) {
  const byId = new Map((pool || []).map((q) => [q.id, q]));
  const chosen = [];
  const used = new Set();
  const push = (q) => {
    if (!q || used.has(q.id) || chosen.length >= limit) return;
    used.add(q.id);
    chosen.push(q);
  };
  (mistakeIds || []).forEach((id) => push(byId.get(id)));
  const weakSections = new Set(
    (placement?.sections || []).filter((s) => s.status === "gap" || s.status === "shaky").map((s) => s.section_id)
  );
  (pool || []).forEach((q) => {
    if (weakSections.has(q.section_id) && (q.difficulty === "basic" || q.difficulty === "exam" || !q.difficulty)) push(q);
  });
  (pool || []).forEach((q) => {
    if (q.difficulty === "basic" || q.difficulty === "exam") push(q);
  });
  return chosen.slice(0, limit);
}
