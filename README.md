# Edmond Study Hub / Edmond 学习站

A bilingual (中文 / English) personal study site for a Year 8 student at a Singapore international school. Content is organised **grade first, then by subject**, following **Cambridge Lower Secondary (Checkpoint)** and an **IGCSE Economics** foundation where Lower Secondary is not the right fit.

Year 8 of all eight subjects is written: Chinese, Mathematics (0862), English (0861), Computing (0860), Economics (0455 foundation), and Physics, Chemistry and Biology split from Science (0893). Years 7 and 9 are outlines only.

The display name and subtitle live in one file: [`site.config.json`](site.config.json). Change `name_zh`, `name_en`, `subtitle_zh` and `subtitle_en` there; the header reads them on startup.

---

## 在线预览

学生链接（浏览器直接打开，无需安装、无需本地文件）：

[https://jinzi2025666-dotcom.github.io/edmond-study-hub/](https://jinzi2025666-dotcom.github.io/edmond-study-hub/)

页面是 `docs/index.html`，与 `offline/edmond-study-hub.html` 内容相同（单文件、HashRouter，样式、脚本、字体、KaTeX 和课程全部内嵌）。八年级全部八个科目已写完；七年级和九年级仍是大纲。路由写在 `#` 后面（例如 `#/grades/8/subjects/mathematics`），因此挂在 `/edmond-study-hub/` 下也可以用。

GitHub Pages **尚未启用**。请在仓库 Settings → Pages 把来源设为分支 `main`、文件夹 `/docs`。设置生效后，上面的链接才会打开。`docs/.nojekyll` 已放好，避免 Jekyll 把文件里的 KaTeX 宏当成模板语法。

---

## How to start / 如何启动

From the repository root (Node.js and Python 3 required):

```bash
./start.sh
```

`start.sh` will:

1. create a Python virtual environment if needed and install `requirements.txt`;
2. rebuild the built-in content index if `data/curriculum/content.json` is missing;
3. install frontend packages if needed and **build** the React app;
4. start a single FastAPI process (uvicorn) that serves both the API and the built site on **port 8787**.

Then open [http://127.0.0.1:8787](http://127.0.0.1:8787).

To use another port: `PORT=9000 ./start.sh`.

在仓库根目录（需要 Node.js 与 Python 3）：

```bash
./start.sh
```

脚本会安装依赖、构建前端，并用 **uvicorn** 在 **8787** 端口同时提供网页和接口。用浏览器打开 [http://127.0.0.1:8787](http://127.0.0.1:8787) 即可。换端口：`PORT=9000 ./start.sh`。

There is no login. This repository holds the source. The student link is the GitHub Pages URL in 在线预览; it stays offline until Pages is set to branch `main` and folder `/docs`. On this computer, use `./start.sh`, or open the offline HTML below.

本仓库是源码，不含登录。给学生的链接是「在线预览」里的 GitHub Pages 地址；在 Pages 来源设为分支 `main`、文件夹 `/docs` 之前，那个地址还打不开。本机请运行 `./start.sh`，或打开下文的离线 HTML。

---

## Where content lives / 内容放在哪里

| What | Path |
| --- | --- |
| Site name | `site.config.json` |
| Subject list and accents | `data/curriculum/subjects.json` |
| Official unit / topic trees (all eight subjects) | `data/curriculum/units.json` |
| Built-in knowledge, questions, papers, coding tasks (source modules) | `data/curriculum/_content_*.py` |
| Compiled built-in content | `data/curriculum/content.json` (regenerate with `python data/curriculum/build_content.py`) |
| Your weekly additions, edits, progress, mistake book, quiz history | `data/user.db` (SQLite, created on first start) |

Built-in sample content is copied into the database on first start (`INSERT OR IGNORE`, so later seed updates do not overwrite your edits). After that, **everything you change in 内容更新 / Update content is saved on the server** and survives restarts.

内置样例会在第一次启动时写入数据库，不会覆盖你已经改过的条目。之后在「内容更新」里的增删改都会写入 `data/user.db`，重启后还在。

`data/user.db` is gitignored. Deleting it and running `./start.sh` again restores the original sample content (your progress and extras will be gone).

---

## Adding a weekly update / 如何添加每周更新

1. Open **内容更新 / Update content** in the header or footer (`/admin`).
2. Add or edit a knowledge point, a question, or a practice set / paper. Fill in both Chinese and English when you can; if only one language is filled, the site shows that one instead of a blank.
3. Set the **publish date**. Anything dated in the last seven days appears on the home page under **本周更新 / This week’s updates**.
4. You can also build a test paper by ticking existing questions, giving it a title, and optionally a time limit. Please title papers as practice papers for this site (for example “Practice Paper A · Algebra”), not as official Cambridge past papers.

在页眉或页脚打开「内容更新」(`/admin`)：可添加或修改知识点、题目、练习组或测试卷。尽量中英都写；只写了一种语言时，页面会显示已有的那一种，而不是空白。设置发布日期后，近七天的内容会出现在首页「本周更新」。用已有题目组卷时，请用「本站练习卷」这类标题，不要写成剑桥官方试卷。

---

## Pages / 页面地图

- `/` — home: choose a year, then a subject; continue learning, this week’s updates, overall progress
- `/grades/:gradeId/subjects/:subjectId` — units, knowledge, practice sets, papers (Year 8 is written; Years 7 and 9 are outlines)
- `/subjects/:id` — redirects to that subject in the selected grade
- `/knowledge/:id` — a knowledge point (Markdown + KaTeX), related questions, Learning / Mastered
- `/practice/:id` — practice set with instant feedback
- `/papers/:id` — test paper, optional timer, score and review
- `/mistakes` — mistake book (filter, retry, mark mastered)
- `/progress` — per-subject progress and attempt history
- `/search` — full-text search (titles, bodies, question stems, both languages)
- `/admin` — weekly content editor
- `/attempts/:id` — review a saved attempt

The header links are Home, Progress, Mistakes, and Update content. There is no standalone code-lab item. `/code` and `/lab` redirect to the home page.

页眉只有首页、进度、错题本和内容更新，没有单独的代码实验室。`/code` 与 `/lab` 会回到首页。

---

## Curriculum sources and assumptions / 课程来源与说明

Sample notes and questions are **original teaching material** written in the style of Checkpoint / early IGCSE. They are not copied from Cambridge past papers or from endorsed textbooks.

样例笔记与题目为原创教学内容，风格贴近 Checkpoint / 早期 IGCSE，并非摘录剑桥真题或官方教材正文。

### Mathematics — Cambridge Lower Secondary Mathematics (0862) Stage 8

Unit titles follow the official Stage 8 Scheme of Work (`tcm143-595644`): 8.1 Number and calculation; 8.2 Algebraic representation and manipulation; 8.3 2D and 3D shape; 8.4 Fractions, decimals, percentages, ratio and proportion; 8.5 Probability; 8.6 Angles and construction; 8.7 Sequences, functions and graphs; 8.8 Transformations; 8.9 Statistics.

Outline and framework: [Cambridge Lower Secondary Mathematics](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-lower-secondary/curriculum/mathematics/).

### English — Cambridge Lower Secondary English (0861) Stage 8

The six units follow the official Stage 8 Scheme of Work (`tcm143-592828`): 8.1 Mystery and suspense; 8.2 Earth’s wild places; 8.3 Language and power; 8.4 Technology; 8.5 Survival; 8.6 Comedy. Knowledge points focus on skills inside those official themes (suspense techniques; register, tone and purpose), consistent with the framework strands of Reading, Writing, and Speaking and Listening.

### Science split into Physics, Chemistry, Biology — Cambridge Lower Secondary Science (0893) Stage 8

The official subject is combined Science. This site splits it as requested, using the official Stage 8 content strands and learning objectives in the Curriculum Framework (2020, version 2.0), for example the document circulated as `0893 Lower Secondary Science Curriculum Framework 2020`.

- **Biology:** Structure and function (8Bs), Life processes (8Bp), Ecosystems (8Be).
- **Chemistry:** Materials and their structure (8Cm), Properties of materials (8Cp), Changes to materials (8Cc).
- **Physics:** Forces and energy (8Pf), Light and sound (8Ps), Electricity and magnetism (8Pe).

**Earth and Space** is a separate official strand. To keep the eight requested subjects, those Stage 8 topics are placed as clearly labelled units:

- under **Physics**: Earth’s magnetic field, galaxies, asteroids;
- under **Chemistry**: renewable and non-renewable resources, climate and weather, long-term climate cycles.

### Computer Science — Cambridge Lower Secondary Computing (0860) Stage 8

A Stage 8 Computing curriculum exists (0860). Unit titles on this site follow the widely used Stage 8 course sequence aligned to that framework (Building networks; It’s all in the planning; Let’s talk technology; Testing conditions; Data input; Iterating through a solution). They prepare the ground for later IGCSE Computer Science (0478) but are labelled as Lower Secondary Computing, not as 0478 papers.

### Economics — Cambridge IGCSE Economics (0455), Year 8 foundation

Economics is not a Cambridge Lower Secondary subject. The unit tree is the official IGCSE 0455 structure (syllabus for 2026 / 2027–2029): 1 The basic economic problem; 2 The allocation of resources; 3 Microeconomic decision-makers; 4 Government and the macroeconomy; 5 Economic development; 6 International trade and globalisation. Sample teaching content focuses on Units 1–2 at an introductory Year 8 depth, and the subject is labelled **IGCSE foundation**.

### Chinese — practical Year 8 first / second language structure

Cambridge IGCSE offers First Language Chinese, Chinese as a Second Language, and Mandarin Chinese (Foreign Language). Singapore international Year 8 Chinese is often closer to first or second language than to Foreign Language (0547). This site therefore does **not** claim a specific IGCSE paper code. Units are a practical Year 8 structure: 现代文阅读, 写作, 语文知识与语法, 口语与交际, 文学与文化, and 古诗文.

---

## Code practice / 代码练习

There is no top-level code lab. Python practice tasks are stored with Computing lessons (`coding_exercise_ids` on those knowledge points, and `coding_exercises` in `data/curriculum/content.json`). The older standalone runner, `frontend/src/pages/CodeLab.jsx`, loads [Pyodide](https://pyodide.org/) from jsDelivr, but it is not mounted on a route.

没有单独的顶层代码实验室。Python 练习写在计算机课里（知识点上的 `coding_exercise_ids`，以及 `data/curriculum/content.json` 里的 `coding_exercises`）。源码中仍有旧的独立运行器 `frontend/src/pages/CodeLab.jsx`（从 jsDelivr 加载 Pyodide），当前没有挂到任何页面路由上。

---

## Offline single-file edition / 离线单文件版

For computers whose browser cannot reach a local server, there is a **single HTML file** that runs entirely from `file://` with no server and no network:

`offline/edmond-study-hub.html` — open that file directly in a browser (`file://`). Routes use a hash, for example `#/grades/8/subjects/mathematics`.

Rebuild it after changing content or code (same React codebase, separate Vite config):

```bash
cd frontend
npm run build:offline
```

What is different offline:

- **Data:** built-in content is inlined in the file. Progress, mistake book, attempts and anything added/edited in 内容更新 are saved in this browser’s `localStorage` (key `esh-offline-data-v1`), not in `data/user.db`. The two editions do **not** share data.
- **Backup:** 内容更新 / Update content has *Export my data*, *Import a backup file* and *Reset my data*. Export weekly; import to move to another computer or browser.
- **Routes** use `#/…` (for example `#/grades/8/subjects/mathematics`, or the short form `#/subjects/math`, which follows the selected grade).
- **Fonts:** Latin fonts and KaTeX are embedded; Chinese uses the system font.
- **Code practice:** the standalone Python runner is not on a route. Computing lessons still carry the written tasks in the curriculum data.

浏览器无法访问本地服务器时，直接打开 `offline/edmond-study-hub.html` 即可（`file://`，地址形如 `#/grades/8/subjects/mathematics`），无需服务器和网络。离线版的进度、错题、测验记录和你新增的内容保存在该浏览器的本地存储里，与服务器版不互通；请在「内容更新」里定期导出备份，换电脑时导入。修改内容或代码后在 `frontend/` 里运行 `npm run build:offline` 重新生成。

---

## Design and languages / 设计与语言

The interface is fully bilingual. The 中文 / English control in the header is stored in `localStorage` (`esh-lang`). Light and dark themes are stored as `esh-theme`. Dates follow the active locale (zh-CN or en-GB).

Every built-in knowledge point and question has Chinese and English fields (`title_zh` / `title_en`, and so on).

公式使用已打包的 KaTeX，支持 `$...$` 与 `$$...$$`。标题字体为 Fraunces（已打包），中文标题回退到 Noto Serif SC。

---

## Development notes / 开发说明

- Backend: Python FastAPI, `backend/main.py`
- Frontend: Vite + React + React Router, `frontend/`
- Python packages: `requirements.txt`
- JavaScript packages: `frontend/package.json`

For a local frontend dev server (API already running on 8787):

```bash
source .venv/bin/activate
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8787
# in another terminal
cd frontend && npm run dev
```
