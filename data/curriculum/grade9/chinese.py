"""Grade 9 Chinese — IGCSE First Language Chinese (0523), Year 1.

Unit 1 follows the term sequence: youth and education, reading formats
(table, short answer, multiple choice), PEEL, and a short email.
Original teaching text only; not the workbook passage.
"""
from __future__ import annotations

TAG = "g9cn"


def L(sid, code, title_zh, title_en, obj_zh, obj_en, points, ez, ee, xz, xe, traps, questions):
    return dict(
        id=sid, code=code, title_zh=title_zh, title_en=title_en,
        obj_zh=obj_zh, obj_en=obj_en, points=points,
        explain_zh=ez, explain_en=ee, example_zh=xz, example_en=xe,
        traps=traps, questions=questions,
    )


def mcq(zh, en, answer, ez, ee, options, marks=1):
    return dict(type="mcq", stem_zh=zh, stem_en=en, answer=answer, exp_zh=ez, exp_en=ee, options=options, marks=marks)


def short(zh, en, answer, ez, ee, accepted, marks=1):
    return dict(type="short", stem_zh=zh, stem_en=en, answer=answer, exp_zh=ez, exp_en=ee, accepted=accepted, marks=marks)


def write(qid, zh, en, answer, ez, ee, keywords, keyword_min, marks):
    return dict(
        type="structured", id=qid, stem_zh=zh, stem_en=en, answer=answer,
        exp_zh=ez, exp_en=ee, keywords=keywords, keyword_min=keyword_min, marks=marks,
    )


SPEC = {
    "subject_id": "chinese",
    "tag": TAG,
    "chapters": [
        {
            "id": "g9-chinese-1",
            "code": "0523 · 1",
            "order": 1,
            "title_zh": "第一单元 · 青少年与教育",
            "title_en": "Unit 1 · Young people and education",
            "note_zh": "本单元按已学顺序：应试与素质、访谈类阅读、PEEL、填表／简答／选择，以及电邮。",
            "note_en": "In the order already taught: exam pressure and broader education, interview reading, PEEL, table / short-answer / multiple-choice reading, then email.",
            "practice_minutes": 25,
            "units": [
                {
                    "id": "g9-chinese-1-u1",
                    "code": "1",
                    "order": 1,
                    "title_zh": "阅读与思维",
                    "title_en": "Reading and thinking",
                    "lessons": [
                        L(
                            "g9cn-1-1", "1.1",
                            "应试教育与素质教育",
                            "Exam-focused schooling and a broader education",
                            "分清两种教育取向，并能用原文依据说明人物的态度，而不是只贴标签。",
                            "Separate the two approaches to education, and support a person’s attitude from the text instead of only attaching a label.",
                            [
                                ("应试取向强调分数、排名和升学；素质取向同时看思考、身体、同伴与判断。", "An exam-focused approach stresses marks, rank and the next school; a broader education also looks at thinking, health, peers and judgement."),
                                ("两种取向可以并存：承认考试有用，不等于承认“只剩考试”。", "The two can sit together: accepting that exams are useful is not the same as accepting that exams are all that is left."),
                                ("阅读时先找说话人、观点和理由，再判断作者有没有偏向。", "When you read, find the speaker, the view and the reason before you decide whether the writer takes a side."),
                                ("评价题要先概括，再引用或转述，最后说明这句话起什么作用。", "An evaluation answer summarises, then quotes or paraphrases, then says what the line does."),
                            ],
                            "这一单元的讨论不是“考试全错、活动全对”。更常见的材料会让家里的人各说一层：有人担心分数，有人担心孩子只剩练习册。读的时候把两层都记下来。\n\n可以先画三个圈：谁在说话、他要什么、他用什么例子。例子往往比口号有用。例如“连运动和社团都停了”是具体代价；“素质教育很重要”只是判断。简答题要的是代价，不是口号。",
                            "The discussion in this unit is not “exams are wrong and activities are right”. A typical text lets people in one family each add a layer: one person worries about marks, another worries that the child has nothing left but workbooks. Keep both layers.\n\nDraw three circles first: who is speaking, what they want, and which example they use. The example is usually more useful than the slogan. “Sport and clubs both stopped” is a concrete cost; “a broader education matters” is only a judgement. A short-answer question wants the cost.",
                            "父亲说：“分数当然要紧。可我更在意他能不能把一个问题想清楚。”问：父亲是否反对考试？\n\n**解：** 不反对。他承认分数要紧，重点放在“想清楚并讲出来”。答题时应写出这两个部分，不能只写“父亲支持素质教育”。",
                            "A father says: “Marks do matter. What I care about more is whether he can think a problem through.” Does he oppose exams?\n\n**Solution:** No. He accepts that marks matter, and he puts the weight on thinking a problem through and explaining it. The answer needs both parts, not only “the father supports a broader education”.",
                            [
                                ("把人物说成“完全反对考试”，忽略原文里的让步。", "Writing that a character “completely opposes exams” and missing the concession in the text."),
                                ("只复述“素质教育”四个字，没有说它在文中指什么。", "Only repeating the four characters for “broader education”, without saying what it means in this text."),
                            ],
                            [
                                mcq("“分数当然要紧，可我更在意他把问题想清楚。”这句话的态度是？", "“Marks do matter, but I care more that he can think a problem through.” The attitude is:", "b", "承认考试，同时把思考放在前面。", "Exams are accepted, and thinking is placed in front.", [("完全取消考试", "exams should be abolished"), ("承认分数有用，但更看重想清楚", "marks are useful, but thinking a problem through matters more"), ("只看排名", "only rank matters"), ("分数毫无意义", "marks mean nothing")]),
                                short("用一句话写出“只剩考试”可能付出的一种具体代价。", "In one sentence, give one concrete cost of a life that is “nothing but exams”.", "运动或社团被停掉", "代价要具体。", "The cost should be concrete.", ["运动或社团被停掉", "没有精神", "sport or clubs stop", "the student is worn out"], 2),
                                mcq("评价人物观点时，较稳妥的顺序是？", "A steadier order for evaluating a view is:", "a", "先概括，再依据，再说作用。", "Summarise, then the evidence, then the effect.", [("先概括，再给依据，最后说作用", "summarise, then give evidence, then say the effect"), ("先下结论“全对”或“全错”", "begin with “entirely right” or “entirely wrong”"), ("只抄最后一句", "copy only the last sentence"), ("不提说话人是谁", "never say who is speaking")]),
                            ],
                        ),
                        L(
                            "g9cn-1-2", "1.2",
                            "访谈阅读与思维导图",
                            "Interview reading and a mind map",
                            "把访谈整理成谁、观点、理由、例子四栏，并能从中找出父母与孩子的相同点和不同点。",
                            "Turn an interview into four columns — who, view, reason, example — and find where a parent and a child agree and differ.",
                            [
                                ("访谈常有多个人。先标说话人，再记观点，避免把母亲的话算到父亲头上。", "An interview often has several speakers. Mark the speaker before the view, so a mother’s line is not given to the father."),
                                ("思维导图的中心是议题，分支是人物；每条分支下只留理由和例子。", "The centre of the map is the issue, and the branches are the people; under each branch keep only the reason and the example."),
                                ("比较题要先写相同，再写不同，两边都要有依据。", "A comparison states the similarity first, then the difference, with evidence on both sides."),
                                ("整理笔记是为了答题，不是为了把全文缩写成另一篇文章。", "Notes are for answering, not for rewriting the whole passage as another essay."),
                            ],
                            "读访谈时可以在姓名旁用不同记号。父亲谈“想清楚”，孩子谈“不是不学习”，母亲谈“每天四十分钟”。三个人都没有否定学习，差别在于把时间留给什么。\n\n导图不必漂亮。一张能用的图通常是：中心写“怎样才算教育好”，三条线分别指向父亲、孩子、母亲，每条线下两个词。答题时按图提取，就不容易漏掉其中一个人。",
                            "Mark each name with a different sign. The father talks about thinking a problem through, the child says this is not a refusal to study, and the mother talks about forty minutes a day. None of them rejects study. The difference is what the time is kept for.\n\nThe map does not need to be handsome. A usable one has the issue in the centre and one line each for father, child and mother, with two words under each line. Answering from the map makes it harder to leave a person out.",
                            "比较父亲和孩子：相同点是什么？不同点是什么？\n\n**解：** 相同：都认为学习或分数有位置。不同：父亲强调把问题想清楚并讲出来；孩子强调考试之外还要有身体、同伴和自己的判断。两边都要写到。",
                            "Compare the father and the child. What is similar, and what is different?\n\n**Solution:** Similar: both give study or marks a place. Different: the father stresses thinking a problem through and explaining it; the child stresses that health, peers and a person’s own judgement sit outside the exam. Both sides are required.",
                            [
                                ("导图只写口号，没有例子，简答题就没有材料可用。", "A map of slogans and no examples leaves the short-answer questions with nothing to use."),
                                ("比较时只写一方，或把两个人的话合成一个人。", "A comparison that writes only one side, or merges two speakers into one."),
                            ],
                            [
                                short("访谈笔记至少应先标出什么，以免张冠李戴？", "What should interview notes mark first, so that one person’s words are not given to another?", "说话人", "先标说话人。", "Mark the speaker first.", ["说话人", "谁在说话", "the speaker", "who is speaking"]),
                                mcq("思维导图的中心更适合写？", "The centre of the mind map is better used for:", "c", "议题，而不是某一个例子。", "The issue, not one example.", [("某一个标点", "one punctuation mark"), ("最长的句子原文", "the longest sentence, copied out"), ("这一则材料的议题", "the issue of the text"), ("作者的笔名", "the writer’s pen name")]),
                                short("比较两个人时，答案通常要包含哪两部分？", "A comparison of two people usually needs which two parts?", "相同点和不同点", "两边都要有。", "Both parts are needed.", ["相同点和不同点", "同和异", "a similarity and a difference", "what is shared and what differs"], 2),
                            ],
                        ),
                        L(
                            "g9cn-1-3", "1.3",
                            "PEEL 段落",
                            "A PEEL paragraph",
                            "用观点、依据、解释、回扣写成一个完整段落，依据来自材料而不是空泛表态。",
                            "Write one paragraph as point, evidence, explanation and link, with evidence taken from the text rather than a general slogan.",
                            [
                                ("P：用一句话回答题目，句中要有明确判断。", "P: answer the question in one sentence that contains a clear judgement."),
                                ("E：给一个来自材料的短依据，可以转述。", "E: give one short piece of evidence from the text; a paraphrase is allowed."),
                                ("E：解释这个依据怎样支撑观点，不要再复述一遍。", "E: explain how that evidence supports the point; do not simply repeat it."),
                                ("L：用半句回到题目里的关键词。", "L: use half a sentence to return to the key words of the question."),
                            ],
                            "PEEL 不是四条不相干的笔记，而是一段能读下去的话。观点句要能脱离后文独立成立。依据句要短，解释句才是拿分的地方：说明这个例子为什么能证明你的判断。\n\n回扣不要新开一个话题。如果题目问的是“应试与素质能否并存”，结尾就回到“并存”，不要突然写成“我以后要当科学家”。",
                            "PEEL is one paragraph a reader can follow, not four unrelated notes. The point should still make sense if the rest were removed. The evidence stays short. The explanation is where the marks sit: say why this example proves the judgement.\n\nThe link should not open a new topic. If the question is whether exam pressure and a broader education can sit together, the last line returns to “sit together”. It does not suddenly become “I want to be a scientist”.",
                            "题目：材料中的家庭是否完全否定考试？写一个 PEEL 段。\n\n**参考：** 这个家庭没有完全否定考试。父亲说分数当然要紧，孩子也说考试能让人知道哪里不会。可见他们反对的是只剩考试，而不是考试本身。因此，材料支持的是两种取向并存，而不是取消评价。",
                            "Question: does the family in the text reject exams completely? Write one PEEL paragraph.\n\n**Sample:** The family does not reject exams completely. The father says marks do matter, and the child says an exam shows what is not yet understood. What they resist is a life with nothing but exams, not the exam itself. The text therefore supports holding the two approaches together, not removing assessment.",
                            [
                                ("有观点和口号，但没有任何材料依据。", "A point and a slogan, with no evidence from the text."),
                                ("解释句只是把依据又抄了一遍。", "An explanation that only copies the evidence again."),
                                ("回扣写成新的故事，离开了题目。", "A link that starts a new story and leaves the question."),
                            ],
                            [
                                mcq("PEEL 里第二个 E 主要做什么？", "What does the second E in PEEL mainly do?", "d", "解释依据如何支撑观点。", "It explains how the evidence supports the point.", [("再写一个新故事", "starts a new story"), ("列出所有生词", "lists every new word"), ("取消观点", "cancels the point"), ("解释依据怎样支撑观点", "explains how the evidence supports the point")]),
                                short("观点句应当能怎样独立存在？", "In what way should the point sentence stand on its own?", "脱离后文仍能回答题目", "它本身就是判断。", "It is the judgement.", ["脱离后文仍能回答题目", "单独读也能回答问题", "it still answers the question without the rest", "it is a clear judgement"]),
                                mcq("回扣句最应回到哪里？", "A link sentence should return to:", "a", "题目中的关键词。", "The key words of the question.", [("题目中的关键词", "the key words of the question"), ("一个全新的职业理想", "a brand-new career plan"), ("无关的成语接龙", "an unrelated idiom chain"), ("试卷的页码", "the page number")]),
                            ],
                        ),
                        L(
                            "g9cn-1-4", "1.4",
                            "填表、简答与选择",
                            "Tables, short answers and multiple choice",
                            "按三种阅读题的得分方式作答：填表抄准词，简答写完整句，选择回原文排除。",
                            "Answer the three reading formats the way they award marks: exact words in a table, a full sentence for a short answer, and a return to the text for multiple choice.",
                            [
                                ("填表题看格子。格子问“谁”，就不要写成长句；问“时间”，就写时间。", "A table is read cell by cell. If the cell asks “who”, do not write a long sentence; if it asks “when”, write the time."),
                                ("简答题通常要一句完整话，并包含题目里的关键词。", "A short answer is usually one full sentence and includes the key words of the question."),
                                ("选择题先排除与原文相反的项，再核对绝对词，如“完全”“一定”“只”。", "For multiple choice, first remove what contradicts the text, then check absolute words such as “completely”, “always” and “only”."),
                                ("答案用自己的话时，不能改变原文的程度和对象。", "A paraphrase must not change the degree or the person the text is talking about."),
                            ],
                            "三种题看的是同一篇材料，但得分点不同。填表最怕多写，把解释填进只能放四个字的格子。简答最怕少写，只丢一个词，没有回答“为什么”。选择最怕被“看起来很正确”的口号吸引，而那句口号原文并没有说。\n\n做选择时，把每个选项代回原文：能找到依据的留下，找不到或说反了的划掉。若两个选项都对，再看哪一个更贴题目的问法。",
                            "The three tasks use one text, but they award marks differently. A table fails when an explanation is squeezed into a cell that only has room for a few words. A short answer fails when it is only one word and never says why. Multiple choice fails when a slogan sounds right but was never said.\n\nFor each option, go back to the text. Keep what you can point to. Cross out what is absent or reversed. If two options are both true, keep the one that answers the question that was actually asked.",
                            "表格一格的提示是“家庭约定的时间”。材料写“每天留四十分钟”。\n\n**解：** 填“每天四十分钟”。不要把母亲后面的活动清单整段抄进这一格。",
                            "A cell is labelled “time agreed at home”. The text says “forty minutes are kept each day”.\n\n**Solution:** Write “forty minutes a day”. Do not copy the mother’s whole list of activities into that cell.",
                            [
                                ("填表写成小作文，超出格子所问的范围。", "Turning a table cell into a mini-essay beyond what that cell asks."),
                                ("简答题只写一个名词，没有回答“为什么”或“怎样”。", "A short answer that is only a noun, with no why or how."),
                                ("看到“一定”“完全”也不回原文核对。", "Not checking “always” or “completely” against the text."),
                            ],
                            [
                                short("格子问“时间”时，应优先填写什么？", "If a cell asks for the time, what should you write first?", "时间本身", "不要写整段解释。", "Do not write the whole explanation.", ["时间本身", "每天四十分钟这类时间", "the time itself", "a time phrase"]),
                                mcq("简答题最常见的失分是？", "A common way to lose a short-answer mark is to:", "b", "只丢一个词，没有把原因说完。", "Give one word and never the reason.", [("句子太完整", "writing a sentence that is too complete"), ("只给一个词，没有回答为什么", "giving one word and not saying why"), ("使用了题目中的关键词", "using the key words of the question"), ("答案能在原文找到", "an answer that can be found in the text")]),
                                mcq("选项里出现“完全否定考试”，而原文只是反对“只剩考试”。应如何处理？", "An option says “rejects exams completely”, but the text only resists “nothing but exams”. You should:", "c", "排除该项，因为它改变了程度。", "Remove it, because it changes the degree.", [("直接选它，因为提到了考试", "choose it, because it mentions exams"), ("不看其他选项", "ignore the other options"), ("排除它，因为程度被说重了", "remove it, because the degree has been made stronger than the text"), ("把它当作填表答案", "use it as a table answer")]),
                            ],
                        ),
                        L(
                            "g9cn-1-5", "1.5",
                            "词语：慎重、丰足与日常表达",
                            "Words: care, plenty, and everyday expressions",
                            "掌握本阶段听写里的一组词，能解释含义并放进合适的句子。",
                            "Learn the dictation set from this stage: explain each item and place it in a fitting sentence.",
                            [
                                ("探索世界：主动去了解未知，不限于地理上的远行。", "探索世界: to look into what is unknown; it is not limited to a long journey."),
                                ("沟通、点赞、微信：一组与交流有关的词，有的偏口语。", "沟通, 点赞, 微信: a set about communication; some of them are colloquial."),
                                ("慎重考虑：强调决定前想清楚，不是“随便想想”。", "慎重考虑: to think a decision through; it is not a casual thought."),
                                ("丰衣足食、无所事事、人生路不熟：分别写富足、空虚和缺乏经验。", "丰衣足食, 无所事事 and 人生路不熟: plenty, emptiness, and a lack of experience."),
                            ],
                            "听写不只看字形。组词之后要想它能不能用在“教育”这个议题里。例如“慎重考虑”可以接家庭约定；“无所事事”可以写停掉所有安排之后的空虚，但不要用它嘲笑认真休息的人。\n\n“人生路不熟”是比喻，说的是经验不足，不是字面的不认识路。写作时比喻要服务于人物，不要堆在一句里。",
                            "Dictation is not only the shape of the characters. After you know a word, ask whether it can serve the topic of education. 慎重考虑 can introduce a family agreement. 无所事事 can describe the emptiness after every activity has been dropped; it should not be used to sneer at real rest.\n\n人生路不熟 is a metaphor for inexperience, not a literal lost path. In writing, a metaphor has to serve the person. Do not pile several into one sentence.",
                            "选词填空：做家庭计划之前，父母和孩子都要______。\n\n**解：** 慎重考虑。句中是决定之前的认真思考，不是“点赞”或“无所事事”。",
                            "Choose a word: before a family plan is made, parents and the child both need to ______.\n\n**Solution:** 慎重考虑. The sentence is careful thought before a decision, not “to like a post” and not “to idle”.",
                            [
                                ("把“人生路不熟”理解成地图不会看。", "Reading 人生路不熟 as not being able to use a map."),
                                ("词语会写，但放进句子后意思相反。", "The characters are correct, but the sentence reverses the meaning."),
                            ],
                            [
                                mcq("“丰衣足食”主要指？", "丰衣足食 mainly means:", "a", "衣食富足。", "Plenty of clothing and food.", [("衣食富足", "plenty of clothing and food"), ("完全没有衣服", "no clothes at all"), ("在网上点赞", "liking a post online"), ("路不认识", "not knowing the road")]),
                                mcq("“无所事事”用来描写的是？", "无所事事 describes:", "b", "没有事做的空虚状态。", "An empty state with nothing to do.", [("非常忙碌", "being very busy"), ("闲着而没有寄托", "idleness with nothing to hold on to"), ("慎重地做计划", "planning with care"), ("食物很丰盛", "a plentiful meal")]),
                                short("“人生路不熟”在比喻里指什么？", "Used as a metaphor, what does 人生路不熟 refer to?", "经验不足", "不是字面迷路。", "It is not a literal lost path.", ["经验不足", "缺乏阅历", "inexperience", "a lack of experience"]),
                            ],
                        ),
                    ],
                },
                {
                    "id": "g9-chinese-1-u2",
                    "code": "2",
                    "order": 2,
                    "title_zh": "电邮",
                    "title_en": "Email",
                    "lessons": [
                        L(
                            "g9cn-2-1", "2.1",
                            "短电邮：称呼、事由与祝颂",
                            "A short email: greeting, purpose and close",
                            "在限定字数内写一封得体的中文电邮：称呼、一件清楚的事、一个理由、祝颂和署名。",
                            "Write a fitting Chinese email inside a word limit: greeting, one clear purpose, one reason, a close and a name.",
                            [
                                ("称呼顶格，对老师用“老师”或“姓＋老师”，不要用对同学的口气。", "The greeting starts at the left. For a teacher use “老师” or the surname plus “老师”, not the tone you would use with a classmate."),
                                ("第一句说明写这封信的原因，不要先写天气。", "The first sentence says why you are writing. Do not begin with the weather."),
                                ("正文只完成题目要求的件数：一项活动加一个理由就够，除非题目要两项。", "The body does only what the task asks. One activity and one reason are enough unless two are required."),
                                ("祝颂单独成行，如“此致”后另起“敬礼”，最后署名。", "The close is on its own lines, for example 此致 and then 敬礼, and then the name."),
                            ],
                            "电邮是实用文，得分点通常是任务完成和语气，而不是华丽的比喻。先用四行打草稿：称呼、目的、理由、结尾。理由要具体，例如“我想参加社区阅读，因为我想把一个问题讲清楚”，比“因为很好”更能得分。\n\n字数不够时删掉重复的客套，不要删掉事由。字数超出时删例子，不要删祝颂和署名。对老师保持尊敬，但不需要堆很多敬词。",
                            "An email is practical writing. Marks usually sit on completing the task and on tone, not on ornate metaphor. Draft four lines: greeting, purpose, reason, close. The reason should be concrete. “I want to join the community reading, because I want to explain a problem clearly” scores more than “because it is good”.\n\nIf you are short of words, cut repeated courtesy, not the purpose. If you are over the limit, cut an example, not the close and the name. Stay respectful to a teacher without stacking honorifics.",
                            "任务：学校举办素质教育体验日。用电邮告诉班主任你想参加的一项活动，并给出一个理由。约 80 字。\n\n**参考结构：** 老师您好。我想报名社区阅读。因为我想练习把一个问题讲清楚，而不只是做题。谢谢老师。此致　敬礼　学生",
                            "Task: the school is holding an experience day. Email your form teacher with one activity you want to join and one reason. About 80 characters.\n\n**A shape that works:** Greeting. I would like to join the community reading. I want to practise explaining a problem, not only completing papers. Thank you. Close and name.",
                            [
                                ("没有称呼或没有署名，格式分会丢掉。", "No greeting or no name, so the format marks go."),
                                ("活动写了两项，理由却一项都没有展开。", "Two activities and no reason developed for either."),
                                ("语气像通知同学，或相反，敬词多到盖住了事由。", "A tone that sounds like a note to a classmate, or so many honorifics that the purpose disappears."),
                            ],
                            [
                                mcq("给老师的电邮，第一句更应写？", "The first sentence of an email to a teacher should:", "a", "写这封信的原因。", "Say why you are writing.", [("说明写这封信要办的事", "state the purpose of the email"), ("先描写天气", "describe the weather first"), ("抄一段课文", "copy a textbook paragraph"), ("只写一个感叹号", "write only an exclamation mark")]),
                                short("电邮结尾至少要有哪两个格式部分？", "Which two format parts does the end of the email need at minimum?", "祝颂和署名", "两者都要有。", "Both are needed.", ["祝颂和署名", "此致敬礼和名字", "a close and a name", "the sign-off and the name"]),
                                mcq("字数超出时，优先删去的是？", "If you are over the word limit, cut first:", "c", "重复的客套，保留事由。", "Repeated courtesy, and keep the purpose.", [("事由本身", "the purpose itself"), ("署名", "the name"), ("重复的客套", "repeated courtesy"), ("题目要求的那个理由", "the reason the task asked for")]),
                            ],
                        ),
                    ],
                },
            ],
        }
    ],
    "paper": {
        "id": "paper-g9-chinese",
        "title_zh": "练习卷 · 阅读（填表、简答、选择）与电邮",
        "title_en": "Practice paper · reading (table, short answers, multiple choice) and email",
        "minutes": 45,
        "published": "2026-11-18T10:00:00+08:00",
        "items": [
            ("g9cn-1-4", short(
                "阅读下面的原创访谈，完成填表。父亲认为分数怎样？只写短语。\n\n初三开学后，林可的课桌上只剩练习册。记者请父亲谈谈怎样才算把孩子教育好。父亲说：“分数当然要紧。可我更在意他能不能把一个问题想清楚，再讲给别人听。”林可说：“我不是反对考试。考试能让我知道哪里不会。我反对的是只剩考试。”母亲说：“我们慎重考虑之后约定，每天留四十分钟，做与试卷无关的事。”",
                "Read the original interview and complete the table. What does the father think about marks? A phrase is enough.\n\nAfter the new term began, Lin Ke’s desk held only workbooks. A reporter asked the father what it means to educate a child well. The father said: “Marks do matter. What I care about more is whether he can think a problem through and then explain it.” Lin Ke said: “I am not against exams. An exam shows me what I do not yet know. What I am against is a life with nothing but exams.” The mother said: “After thinking it through, we agreed to keep forty minutes a day for something that is not a paper.”",
                "要紧，但更看重想清楚",
                "填表要短，并保留“要紧”和“更在意”两层。",
                "Keep the cell short, and keep both “marks matter” and “thinking matters more”.",
                ["要紧，但更看重想清楚", "分数要紧但更看重思考", "marks matter, but thinking matters more", "marks matter but thinking a problem through matters more"],
                2,
            )),
            ("g9cn-1-4", short(
                "同一则访谈。填表：家庭约定每天留出多少时间？",
                "Same interview. Table: how much time does the family keep each day?",
                "四十分钟",
                "格子问的是时间。",
                "The cell asks for the time.",
                ["四十分钟", "每天四十分钟", "forty minutes", "40 minutes"],
                1,
            )),
            ("g9cn-1-4", short(
                "同一则访谈。填表：这些时间用来做什么？用短语。",
                "Same interview. Table: what is that time used for? A phrase is enough.",
                "做与试卷无关的事",
                "不要把三个人的话都写进这一格。",
                "Do not put all three speakers into this cell.",
                ["做与试卷无关的事", "与试卷无关的事", "something that is not a paper", "something other than exam papers"],
                1,
            )),
            ("g9cn-1-2", short(
                "简答：林可为什么说自己不是反对考试？用完整的一句。",
                "Short answer: why does Lin Ke say she is not against exams? One full sentence.",
                "因为考试能让她知道哪里不会",
                "要写出原因，而不只是重复“不反对”。",
                "Give the reason, not only “not against”.",
                ["因为考试能让她知道哪里不会", "考试能显示不会的地方", "because an exam shows what she does not yet know", "an exam shows the gaps"],
                2,
            )),
            ("g9cn-1-1", short(
                "简答：父亲和林可的相同点是什么？一句即可。",
                "Short answer: what do the father and Lin Ke share? One sentence is enough.",
                "都不否定考试或学习",
                "相同点是都给考试留下位置。",
                "The similarity is that both leave a place for exams.",
                ["都不否定考试或学习", "都认为考试有用", "neither rejects exams or study", "both give exams a place"],
                2,
            )),
            ("g9cn-1-3", short(
                "简答：若把母亲的约定写成 PEEL 的依据，可以引用哪一个事实？",
                "Short answer: if the mother’s agreement is the evidence in a PEEL paragraph, which fact can you use?",
                "每天四十分钟做与试卷无关的事",
                "依据要具体。",
                "The evidence should be concrete.",
                ["每天四十分钟做与试卷无关的事", "每天留四十分钟", "forty minutes a day for something that is not a paper", "forty minutes a day"],
                2,
            )),
            ("g9cn-1-4", mcq(
                "同一则访谈。最符合原文的一项是？",
                "Same interview. Which statement best matches the text?",
                "b",
                "三个人都没有主张取消考试。",
                "None of the three argues for abolishing exams.",
                [("父亲认为分数毫无意义", "The father thinks marks mean nothing"), ("林可反对的是只剩考试，而不是考试本身", "Lin Ke resists a life with nothing but exams, not the exam itself"), ("母亲要求取消所有学习", "The mother wants all study cancelled"), ("林可的桌上没有任何练习册", "There is no workbook on Lin Ke’s desk")],
                1,
            )),
            ("g9cn-1-4", mcq(
                "选项“这个家庭完全否定考试”不能选，主要因为？",
                "Why can you not choose “this family rejects exams completely”?",
                "a",
                "原文的程度没有这么重。",
                "The text never goes that far.",
                [("它把程度说得比原文重", "it makes the degree stronger than the text"), ("文中没有出现“家庭”", "the text never mentions a family"), ("填表不能出现数字", "a table cannot contain a number"), ("电邮不需要称呼", "an email needs no greeting")],
                1,
            )),
            ("g9cn-1-4", mcq(
                "“慎重考虑之后”在母亲的话里修饰的是？",
                "In the mother’s words, “after thinking it through” describes:",
                "c",
                "做出约定的过程。",
                "The process of making the agreement.",
                [("林可的练习册", "Lin Ke’s workbooks"), ("记者的职业", "the reporter’s job"), ("做出家庭约定的过程", "the process of making the family agreement"), ("分数的计算方法", "how marks are calculated")],
                1,
            )),
            ("g9cn-1-5", mcq(
                "哪一个词最适合描述“决定前想清楚”？",
                "Which word best fits “think it through before deciding”?",
                "d",
                "慎重考虑。",
                "慎重考虑.",
                [("无所事事", "idling"), ("丰衣足食", "plenty"), ("点赞", "liking a post"), ("慎重考虑", "thinking it through with care")],
                1,
            )),
            ("g9cn-2-1", write(
                "q-g9cn-email",
                "电邮（约 80 字）。学校将举办素质教育体验日。请写给班主任：说明你想参加的**一项**活动，并给出**一个**理由。要有称呼、事由、祝颂和署名。系统按要点给分，交卷后请对照参考答案看语气和格式。",
                "Email, about 80 characters. An experience day is being held. Write to your form teacher: name **one** activity you want to join and give **one** reason. Include a greeting, the purpose, a close and a name. Key points are marked automatically; after you submit, compare tone and format with the sample.",
                "见解析中的参考电邮。",
                "参考：\n\n老师您好。\n\n体验日我想参加社区阅读。因为我想练习把一个问题讲清楚，而不只是完成试卷。\n\n谢谢老师。\n\n此致\n敬礼\n\n学生",
                "Sample:\n\nDear teacher,\n\nFor the experience day I would like to join the community reading, because I want to practise explaining a problem rather than only finishing papers.\n\nThank you.\n\nYours\nA student",
                ["老师", "您好", "阅读", "因为", "谢谢", "敬礼", "teacher", "because", "thank", "reading"],
                4,
                10,
            )),
        ],
    },
}
