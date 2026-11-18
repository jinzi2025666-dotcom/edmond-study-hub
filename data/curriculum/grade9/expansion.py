"""Revision-guide sections and extra graded questions for every Grade 9 lesson.

Each guide is written so a student can revise the topic from the page:
definitions, a worked sequence, a second example, how to read a diagram,
command words, and a short summary. The original lesson text stays above it.
"""
from __future__ import annotations

HEADS = (
    ("关键定义", "Key definitions"),
    ("逐步讲解", "Step by step"),
    ("公式、关系与第二道例题", "Formulas and a second worked example"),
    ("图示与版面", "Diagrams and layout"),
    ("考试提示与指令词", "Exam tips and command words"),
    ("本课小结", "Short summary"),
)


def G(*pairs):
    zh, en = [], []
    for (hz, he), (pz, pe) in zip(HEADS, pairs):
        zh.append(f"## {hz}\n\n{pz.strip()}")
        en.append(f"## {he}\n\n{pe.strip()}")
    return "\n\n".join(zh), "\n\n".join(en)


def mcq(diff, zh, en, answer, ez, ee, options, marks=1):
    return dict(type="mcq", difficulty=diff, stem_zh=zh, stem_en=en, answer=answer,
                exp_zh=ez, exp_en=ee, options=options, marks=marks)


def short(diff, zh, en, answer, ez, ee, accepted, marks=1):
    return dict(type="short", difficulty=diff, stem_zh=zh, stem_en=en, answer=answer,
                exp_zh=ez, exp_en=ee, accepted=accepted, marks=marks)


def num(diff, zh, en, answer, ez, ee, marks=1, tolerance=0, accepted=None):
    q = dict(type="numeric", difficulty=diff, stem_zh=zh, stem_en=en, answer=str(answer),
             exp_zh=ez, exp_en=ee, marks=marks, tolerance=tolerance)
    if accepted:
        q["accepted"] = accepted
    return q


def write(diff, zh, en, answer, ez, ee, keywords, keyword_min, marks):
    return dict(type="structured", difficulty=diff, stem_zh=zh, stem_en=en, answer=answer,
                exp_zh=ez, exp_en=ee, keywords=keywords, keyword_min=keyword_min, marks=marks)


# ---------------------------------------------------------------------------
# Guides. Six blocks each. Kept specific to the lesson, not a generic frame.
# ---------------------------------------------------------------------------

GUIDES = {
"g9cn-1-1": G(
    ("应试取向看分数、排名和升学；素质取向同时看想清楚、身体、同伴和自己的判断。二者可以并存：承认考试有用，不等于承认生活里只剩考试。经济物品式的“有代价”在这里是时间：刷题占掉的运动和社团，就是代价。",
     "An exam-focused approach watches marks, rank and the next school. A broader education also watches clear thinking, health, peers and a person’s own judgement. The two can sit together: accepting that exams are useful is not the same as accepting a life with nothing but exams. The cost is time. Sport and clubs given up for extra papers are that cost."),
    ("读人物态度分三步。第一，标出谁在说话。第二，找出让步，例如“分数当然要紧”。第三，找出转折后的重点，例如“更在意他把问题想清楚”。评价题再加第四步：这个重点在文中用哪个具体例子撑住。没有例子就不要写成“他完全支持素质教育”。",
     "Read an attitude in three steps. First, mark who is speaking. Second, find the concession, for example “marks do matter”. Third, find the weight after the turn, for example “I care more that he can think a problem through”. An evaluation adds a fourth step: which concrete example holds that weight up. Without an example, do not write “he fully supports a broader education”."),
    ("第二道例题。材料只写“他把社团停了，成绩上去了，人却没精神”。问：能否说他反对一切考试？不能。能说的是：他付出的代价是社团和精力，而不是考试本身被否定。答题句式：虽然……但是……，依据是……。",
     "Second example. The text only says the club stopped, the marks rose, and the student was worn out. Can you say he opposes every exam? No. You can say the cost was the club and his energy, not a rejection of exams themselves. A usable sentence is: although…, the evidence is…"),
    ("思维上把它画成左右两栏，而不是一个口号。左栏写“考试仍有的位置”，右栏写“考试之外失去的东西”。栏与栏之间用箭头标“但是”。以后做填表，一格只填一栏里的短语。",
     "Lay it out as two columns, not one slogan. The left column is “the place exams still have”. The right column is “what is lost outside exams”. Put “but” on the arrow between them. Later, a table cell takes a phrase from one column only."),
    ("指令词“说明态度”要态度加依据，不是只贴标签。“概括”只保留谁、要什么、代价是什么。“评价”必须先概括再判断。看到“完全”“只”“一定”，回原文核对程度。",
     "The command “explain the attitude” needs the attitude and the evidence, not a label alone. “Summarise” keeps who, what they want, and the cost. “Evaluate” summarises before it judges. When you see “completely”, “only” or “always”, check the degree against the text."),
    ("这一课的判断是：材料通常不取消考试，它讨论考试是否挤掉了其他成长。答题时两边都要出现。",
     "The judgement of this lesson is that the texts usually do not cancel exams. They ask whether exams have crowded out other kinds of growing up. An answer needs both sides."),
),
"g9cn-1-2": G(
    ("访谈笔记的四栏是：说话人、观点、理由、例子。中心议题只有一个，例如“怎样才算把教育做好”。比较题的相同点是双方都承认的那一层，不同点是理由或例子不一样的那一层。",
     "Interview notes have four columns: speaker, view, reason, example. There is one central issue, for example “what counts as educating a child well”. In a comparison, the similarity is the layer both sides accept, and the difference is the layer where the reason or the example changes."),
    ("第一步，用不同记号标姓名，避免把母亲的话算到父亲头上。第二步，每人只留一个观点句和一条依据。第三步，先写相同，再写不同，两边都要有原文里的事实。导图不必好看，但必须能直接变成简答题的句子。",
     "First, mark each name with a different sign so a mother’s line is not given to the father. Second, keep one view and one piece of evidence per person. Third, write the similarity, then the difference, with a fact from the text on both sides. The map does not need to be handsome. It does need to become a short-answer sentence without more hunting."),
    ("例：父亲要“想清楚再讲出来”，孩子要“考试之外还有身体和同伴”，母亲用“每天四十分钟”把约定写具体。相同点：三个人都没有取消学习。不同点：父亲看表达，孩子看生活的其他部分，母亲看时间表。漏掉任何一个人，比较题就会少一边。",
     "Example: the father wants a problem thought through and explained, the child wants health and peers as well as exams, and the mother makes it concrete with forty minutes a day. Similarity: none of them cancels study. Difference: the father watches explanation, the child watches the rest of life, the mother watches the timetable. Leave one person out and a comparison loses a side."),
    ("导图画成一个中心加三条线。线的末端只写两个词，不写整段。答题时按线提取。若题目只问母亲，就不要把三条线都抄进去。",
     "Draw one centre and three lines. The end of a line holds two words, not a paragraph. Answer by following the line. If the question asks only about the mother, do not copy all three lines."),
    ("“比较”必须有同有异。“整理”不是把全文缩写成另一篇作文。简答要完整句，但句子里的事实必须能在导图上指出来。",
     "“Compare” needs both a similarity and a difference. “Organise” is not a second essay that shortens the whole text. A short answer is a full sentence, but the fact inside it must be pointable on the map."),
    ("访谈阅读的得分点是：人没有张冠李戴，比较两边都在，例子具体。",
     "The marks in interview reading sit on not mixing up the speakers, keeping both sides of a comparison, and using a concrete example."),
),
"g9cn-1-3": G(
    ("PEEL 是一个能读下去的段落，不是四条不相干的笔记。P 是能独立回答题目的判断。第一个 E 是短依据。第二个 E 是依据如何支撑判断。L 回到题目里的关键词，不新开话题。",
     "PEEL is one paragraph a reader can follow, not four unrelated notes. P is a judgement that can answer the question on its own. The first E is short evidence. The second E says how that evidence supports the judgement. L returns to the key words of the question and does not open a new topic."),
    ("先写判断句，检查把它单独读是否已经回答问题。再从材料选一个最短的事实，不要把整段抄下来。解释句禁止只把事实再说一遍，要写“这说明……”。最后用半句扣回题目里的词，例如“并存”或“并没有完全否定”。",
     "Write the judgement first and check that it still answers the question if read alone. Then choose the shortest fact from the text; do not copy the paragraph. The explanation must not repeat the fact. It should say “this shows…”. End with half a sentence that returns to a word in the question, such as “sit together” or “does not reject completely”."),
    ("题目：这个家庭是否完全否定考试？P：没有完全否定。E：父亲说分数要紧，孩子说考试能显示不会的地方。E：他们反对的是只剩考试。L：所以材料支持的是两种取向并存。若回扣写成“我以后想当科学家”，段落就离开了题目。",
     "Question: does this family reject exams completely? P: it does not. E: the father says marks matter, and the child says an exam shows what is not yet known. E: what they resist is a life with nothing but exams. L: the text therefore supports holding the two approaches together. A link that says “I want to be a scientist” has left the question."),
    ("在稿纸上写成四行：P / E / E / L。交卷前检查第二行是否短、第三行是否比第二行多一句解释。不要交四条项目符号，除非题目明确要求笔记。",
     "Draft four lines: P / E / E / L. Before you hand it in, check that line two is short and line three adds an explanation. Do not hand in four bullet points unless the question asked for notes."),
    ("指令词“用材料说明”没有依据就是 0 分里的内容分。“写一段”要成段。“结合文本”不能只写个人经历。",
     "If the command is “use the text to show” and there is no evidence, the content marks go. “Write a paragraph” means a paragraph. “Using the text” cannot be replaced by a personal story alone."),
    ("PEEL 的力量在第二个 E。观点和依据都对，但没有解释，仍然不是一个完整的段落。",
     "The strength of PEEL is the second E. A point and evidence without an explanation are still not a complete paragraph."),
),
"g9cn-1-4": G(
    ("填表按格子的问法作答：问谁就写谁，问时间就写时间。简答通常是一个完整句，并含题目里的关键词。选择题先排除与原文相反或程度更重的项。三种题用的是同一篇材料，得分方式不同。",
     "A table is answered in the shape of the cell: “who” gets a person, “when” gets a time. A short answer is usually one full sentence and includes the key words of the question. Multiple choice first removes what contradicts the text or makes the degree stronger. The three tasks share one text and award marks differently."),
    ("填表：读格头，回到原文摘短语，不写解释。简答：先在心里用原文的词回答，再写成一句，补上“因为”。选择：把每个选项代回原文，找不到依据或说反了就划掉。两个选项都像对时，留那个更贴问法的。",
     "Table: read the cell heading, return to the text, and lift a phrase. Do not add an explanation. Short answer: answer in the text’s words in your head, then write one sentence and add “because”. Multiple choice: take each option back to the text. Cross out what is missing or reversed. If two options both look true, keep the one that answers the question that was actually asked."),
    ("格头是“家庭约定的时间”，原文是“每天四十分钟”。正确填写就是这五个字左右，不是把母亲后面的活动清单整段抄进格子。若简问答“为什么不反对考试”，只写“不反对”没有分，必须写出“因为考试能显示哪里不会”。",
     "The cell says “time agreed at home” and the text says “forty minutes a day”. That phrase is the whole cell. Do not copy the mother’s list of activities into it. If a short question asks why someone is not against exams, “not against” alone scores nothing. The because-clause has to say that an exam shows what is not yet known."),
    ("做题时在原文旁用三种记号：方框给填表，下划线给简答，问号给选择里拿不准的项。交卷前只检查记号对应的格子，避免把简答的长句填进表。",
     "Mark the text in three ways: a box for a table fact, an underline for a short answer, a question mark for an option you are unsure of. Before you hand it in, check only the mark that belongs to that task, so a long short-answer sentence does not land in a table cell."),
    ("“根据文章”意味着答案能指回句子。“选择正确的一项”不要选听起来正确、原文没说的口号。绝对词是排除用的工具。",
     "“According to the text” means the answer can be pointed back to a sentence. For multiple choice, do not choose a slogan that sounds right but was never said. Absolute words are tools for ruling options out."),
    ("填表求短，简答求完整，选择求核对。三种都不要改变原文的程度和对象。",
     "Tables want brevity, short answers want a complete sentence, and multiple choice wants a check against the text. None of the three should change the degree or the person in the source."),
),
"g9cn-1-5": G(
    ("本组词要会写，也要会放进“教育”这个议题。探索世界：主动了解未知。沟通、点赞、微信：交流，其中后两个偏口语。慎重考虑：决定前想清楚。丰衣足食：衣食富足。无所事事：没有寄托的空闲。人生路不熟：比喻经验不足，不是地图不会看。",
     "These words must be written correctly and also placed inside the topic of education. 探索世界 is to look into what is unknown. 沟通, 点赞 and 微信 are about communication; the last two are colloquial. 慎重考虑 is to think a decision through. 丰衣足食 is plenty of clothing and food. 无所事事 is empty idleness. 人生路不熟 is a metaphor for inexperience, not an inability to read a map."),
    ("听写后做三件事：组一个词，造一个能放进本单元的句子，再检查感情色彩。例如“无所事事”可以写停掉所有安排之后的空虚，不要用它嘲笑认真的休息。“慎重考虑”后面接决定，不接随便一想。",
     "After dictation, do three things: build a phrase, write a sentence that could sit in this unit, and check the tone. 无所事事 can describe the emptiness after every activity has been dropped. It should not sneer at real rest. 慎重考虑 is followed by a decision, not by a casual thought."),
    ("填空：做家庭计划之前，父母和孩子都要______。答案是“慎重考虑”。点赞、无所事事、丰衣足食都接不进“决定之前”这个位置。人生路不熟若用在刚升上中三的学生身上，说的是经验不足，要加上下文，不能单独当迷路。",
     "Gap fill: before a family plan is made, parents and the child both need to ______. The answer is 慎重考虑. Liking a post, idleness and plenty do not fit the slot “before a decision”. Used of a student new to this year, 人生路不熟 means inexperience and needs context. It is not literal lostness."),
    ("把八个词分成三组记：交流（沟通、点赞、微信）、判断（探索世界、慎重考虑）、状态（丰衣足食、无所事事、人生路不熟）。组内对比着记，比孤立地背字形更不容易用反。",
     "Learn the eight items in three groups: communication (沟通, 点赞, 微信), judgement (探索世界, 慎重考虑), and state (丰衣足食, 无所事事, 人生路不熟). Contrasts inside a group are safer than memorising the shape of each character alone."),
    ("听写分看字形。运用分看搭配和褒贬。解释比喻时要说本体是什么，不能停在字面。",
     "Dictation marks the characters. Use marks the collocation and the tone. When you explain a metaphor, name what it really refers to. Do not stop at the literal picture."),
    ("这组词是本单元的语言工具。会写不够，还要能放进谈教育和选择的句子里。",
     "These words are the language tools of the unit. Being able to write them is not enough. They also have to sit inside a sentence about education and choice."),
),
"g9cn-2-1": G(
    ("给老师的短电邮有四件必有的东西：顶格称呼、第一句就写事由、一个具体理由、祝颂和署名。语气尊敬，但敬词不能多到盖住事情。字数不够时删重复的客套；字数超出时删例子，不删事由和署名。",
     "A short email to a teacher has four required parts: a greeting at the left margin, a first sentence that states the purpose, one concrete reason, and a close plus a name. The tone is respectful, but honorifics must not bury the task. If you are short of words, cut repeated courtesy. If you are over the limit, cut an example, not the purpose and not the name."),
    ("草稿只写四行：称呼；我想参加哪一项；因为什么；谢谢、此致、署名。理由要能被看懂，例如“我想练习把一个问题讲清楚”，不要只写“因为很好”。活动只写题目要求的件数。题目说一项，就不要写两项却两项都没有理由。",
     "Draft four lines only: greeting; the one activity; the because; thank you, close, name. The reason must be understandable, for example “I want to practise explaining a problem”, not “because it is good”. Write only as many activities as the task allows. If it says one, do not offer two with no reason for either."),
    ("参考形状（约 80 字）：老师您好。体验日我想参加社区阅读，因为我想练习把一个问题讲清楚，而不只是完成试卷。谢谢老师。此致 敬礼 学生。缺称呼或署名会丢格式分；缺“因为”会丢任务分。",
     "A shape of about 80 characters: greeting; I would like to join the community reading, because I want to practise explaining a problem rather than only finishing papers; thank you; close; name. Missing the greeting or the name loses format marks. Missing “because” loses task marks."),
    ("版面：称呼单独一行，正文分段，祝颂单独成行，“敬礼”另起，署名在最后。不要把整封信写成一段没有空行的长句。",
     "Layout: the greeting on its own line, the body in a short paragraph, the close on its own line, the sign-off on the next line, the name last. Do not write the whole email as one line with no breaks."),
    ("实用文的指令是“写一封电邮说明……并给出理由”。评分看任务是否完成、语气是否对老师、格式是否齐全，不看比喻华丽不华丽。",
     "The command is “write an email explaining… and give a reason”. Marks sit on completing the task, a tone fit for a teacher, and a complete format. They do not sit on ornate metaphor."),
    ("电邮先把事情说清，再把理由说具体，最后把格式写全。",
     "In an email, state the task, make the reason concrete, and then complete the format."),
),
}

EXTRAS: dict = {}

def _load():
    from .more_a import GUIDES as g1
    from .more_b import GUIDES as g2, EXTRAS as e2
    GUIDES.update(g1)
    EXTRAS.update(e2)

_load()
