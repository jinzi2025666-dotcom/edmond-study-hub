# Curriculum data

Grade 8 lessons, questions and papers in `data/curriculum/` are the existing Lower Secondary course.

Grade 9, added under `data/curriculum/grade9/`, is an **initial draft for the owner to review**. It is not a finished set of classroom notes. It follows the term’s IGCSE Year 1 order (Sec 3 / S3): topics already taught, plus the topic in progress. It is not Cambridge Lower Secondary Stage 9.

Please check, subject by subject, before anything is treated as the version students should rely on:

- names of topics against the slides and worksheet titles actually used in class
- which sub-topics are in the next test and which are only “coming next”
- numbers in worked examples
- whether a model paragraph is in the voice you want
- anything that should be replaced by your own notes or exercises

The draft does not name teachers, students or the school. Literature notes paraphrase the set text. They do not reproduce it. When a real essay needs a quotation, students should use a short line from their own copy.

## How to add or replace material

Two routes. Use the first when you are replacing a whole lesson. Use the second when you are adding one note, question or paper on top.

### 1. Edit the subject file and rebuild

Each subject is one file:

| Subject | File |
| --- | --- |
| 语文 / Chinese 0523 | `data/curriculum/grade9/chinese.py` |
| 数学 / Mathematics 0580 and 0606 | `data/curriculum/grade9/mathematics.py` |
| 英语 / English 0500 and World Literature 0408 | `data/curriculum/grade9/english.py` |
| 计算机 / Computer Science | `data/curriculum/grade9/computer_science.py` |
| 经济 / Economics 0455 | `data/curriculum/grade9/economics.py` |
| 物理 / Physics | `data/curriculum/grade9/physics.py` |
| 化学 / Chemistry | `data/curriculum/grade9/chemistry.py` |
| 生物 / Biology 0610 | `data/curriculum/grade9/biology.py` |

A lesson is one `L(...)` block. To replace a draft with your own notes, keep the same lesson `id` (for example `g9ec-7`) and rewrite the Chinese and English text and the questions. Keeping the id keeps links, progress and the mistake book attached to that lesson.

Then, from the repository root:

```bash
python3 data/curriculum/build_content.py
```

That refreshes `content.json` and the Grade 9 chapters in `units.json`. Grade 8 rows are left in place. Restart the site afterwards. The first start after a content rebuild uses a new seed version and reloads built-in rows; notes you added in **内容更新** (origin `user`) are kept.

`units.json` is the outline students see. `content.json` is the compiled lessons and questions. Do not edit `content.json` by hand.

### 2. Add a single item in 内容更新

Open **内容更新 / Update content**. Set **grade** to `9`. Choose the chapter in the unit list (chapters are labelled `G9`). For a note that should appear on an existing section, set `section_id` to the section id in `units.json`, such as `g9ph-5`. New questions and papers need `grade_id` `9` as well, or they will not show inside Grade 9.

Give the item a publish date. Items from the last seven days appear under **本周更新** for the grade that is selected on the home page.

## Question marking

Short, numeric and multiple-choice answers are marked exactly (numbers accept equivalent fractions). Longer writing — an email, a PEEL paragraph, an empathic response, an 8-mark essay, a pseudocode algorithm — is marked by whether enough key phrases are present. The explanation still holds a model answer. Treat that score as a first check, then read the writing yourself.
