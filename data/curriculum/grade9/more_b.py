"""Remaining guides and the extra question bank."""
from .expansion import G, mcq, short, num, write

def _g(*pairs):
    # Callers pass (English, Chinese). G expects (Chinese, English).
    return G(*((b, a) for a, b in pairs))

GUIDES = {
"g9en-1-1": _g(
    ("Directed writing keeps the facts of a source and changes the audience, purpose and form. A fact that does not serve the new task is left behind. A promise the source never made must not be added.",
     "定向写作保留材料里的事实，改的是读者、目的和体裁。对新任务没有用的事实留下。材料没作过的承诺不能加进去。"),
    ("Mark three things before you draft: who reads it, what they should do or feel, and which form you are using. Then select two or three facts. End by completing the purpose, not by summarising the article again.",
     "动笔前先标三件事：谁读、要对方做什么或感到什么、用什么体裁。然后只选两三个事实。结尾完成目的，而不是把原文再概括一遍。"),
    ("From the original hospital article, a student notice can use: the valve came from a stranger; a doctor can plan an operation but not a donation; Farah can swim and the list is not shorter. It cannot say “joining the register will certainly save your family”.",
     "用那篇原创医院短文写通知时，可用的事实是：瓣膜来自陌生人；医生能安排手术但不能安排捐献；Farah 能游泳而名单没有变短。不能写“登记就一定能救你的家人”。"),
    ("In the margin, label A (audience), P (purpose), F (form). Underline only the sentences you will actually carry over. If a sentence has no label, it is probably a retelling.",
     "页边标 A（读者）、P（目的）、F（体裁）。只给真正会用到的句子画线。没有标记的句子多半是在复述。"),
    ("Command words: “using the information” means the facts must be traceable. “Write a speech / report / letter” fixes the voice. A piece that could still be the original article has not done Q3.",
     "指令词 “using the information” 表示事实必须能指回原文。“Write a speech / report / letter” 规定声音。如果交上去的文字仍像原文，Q3 就没有完成。"),
    ("Select, reshape, and stop. Q3 is not a summary and not an invention.",
     "挑选、改写、然后停笔。Q3 不是摘要，也不是编造。"),
),
"g9en-1-2": _g(
    ("An interview has two voices and questions that open thinking. A journal speaks to the self and can hold an unfinished feeling. A letter is shaped by the person named in the greeting. A speech uses “you” and ends with an action.",
     "访谈有两个声音，问题要能引出想法。日记对自己说，可以留下未完成的感受。书信由称呼里的那个人决定能说什么。演讲用“你们”，并以一个行动结束。"),
    ("Choose the form and do not switch. Plan one idea that changes, for example from “I want the forty minutes” to “I know what they cost”. A middle that repeats the same sentence has stopped developing.",
     "选定体裁就不要中途更换。安排一个会变化的想法，例如从“我想要这四十分钟”到“我知道它们的代价”。中段反复同一句，就是没有发展。"),
    ("Journal: “I closed the paper. The clock said forty minutes, and I was angry with myself for wanting them.” Speech: “You know that clock. Give it forty minutes that are not another paper.” Same decision, two forms.",
     "日记：“我合上试卷。时钟说还有四十分钟，我却生自己的气，因为我想要它们。”演讲：“你们都认识那个时钟。把四十分钟给一件不是试卷的事。”同一决定，两种体裁。"),
    ("Interview on the page: name, question, name, answer. Letter: greeting and a close. Speech: short sentences and a question to the room. If the layout could belong to another form, the form has slipped.",
     "访谈在纸上是：名字、问题、名字、回答。书信有称呼和结尾。演讲用短句，并向房间里的人发问。如果版面可以属于另一种体裁，体裁就已经滑走了。"),
    ("The Q4 rubric rewards a form that holds and an idea that develops. It does not reward a list of ambitious words. “Dear Headteacher” cannot open a letter to a friend.",
     "Q4 看的是体裁是否站得住、想法是否发展，不看你堆了多少大词。给朋友的信不能用“尊敬的校长”开头。"),
    ("One form, one changing idea, an ending that belongs to that form.",
     "一种体裁，一个会变化的想法，一个属于这种体裁的结尾。"),
),
"g9en-2-1": _g(
    ("Anowa is a play by Ama Ata Aidoo, set in nineteenth-century Yebi. The prologue lets an old pair speak the village’s competing judgements before Anowa chooses. A play moves by who is on stage and who can hear, not by a novel’s long passage inside a mind.",
     "《Anowa》是 Ama Ata Aidoo 的剧本，背景在十九世纪的 Yebi。序幕让一对老人在 Anowa 选择之前说出村庄里两种互相竞争的判断。戏靠谁在场、谁听得见推进，而不是靠小说式的长篇内心。"),
    ("Ask, at each moment, who is present. The elders do not decide for Anowa. They teach the audience the words the village is ready to use. Later scenes test those words.",
     "每一刻都问谁在场。老人并不替 Anowa 作决定。他们让观众先学会村庄准备好的那些词。后面的场次检验这些词。"),
    ("A stage direction can be read in silence. A disagreement spoken in the prologue is heard by both speakers and by us. That is why the prologue shows “the individual and society” more strongly than a note in the margin.",
     "舞台说明可以默读。序幕里说出来的分歧，两个说话人和观众都听得见。所以序幕比页边的注释更能表现“个人与社会”。"),
    ("In notes, put the prologue in a box labelled “community speaks first”. Draw an arrow to the later phase you are discussing. Do not leave the prologue as a folk tale that never returns.",
     "笔记里把序幕放进一个框，标明“社会先说话”。画箭头指向你正在讨论的后面阶段。不要把序幕当成再也不回来的民间故事。"),
    ("“How does the writer use the prologue?” needs a structural point: the community’s voice comes before the protagonist’s. Naming the country alone does not answer it.",
     "“作者如何使用序幕”要答结构：社会的声音先于主人公。只写国家名字回答不了这个问题。"),
    ("The prologue is a choice about order. Society is allowed to speak first.",
     "序幕是关于顺序的选择。社会被允许先开口。"),
),
"g9en-2-2": _g(
    ("Phase 1: Anowa chooses Kofi Ako when he is not wealthy, and she leaves Yebi. Her parents, Badua and Osam, make the cost of that choice visible. Phase 2: trade brings wealth; Kofi wants enslaved labour; Anowa refuses; the marriage also splits over children. Phase 3: the house is rich, the marriage is empty, and gossip turns a private failure into public shame. Both die. Name the cost without graphic detail.",
     "第一阶段：Anowa 在 Kofi 并不富有时选择了他，并离开 Yebi。父母 Badua 和 Osam 让这个选择的代价可见。第二阶段：贸易带来财富；Kofi 想使用被奴役的劳动力；Anowa 拒绝；婚姻也在孩子的问题上裂开。第三阶段：房子富了，婚姻空了，闲话把私人的失败变成公开的耻辱。两人都死去。点明代价即可，不必写血腥细节。"),
    ("Write each phase as what he wants and what she refuses. Do not write “they grew sadder” three times. The second phase is where wealth stops being a shared success and becomes a moral choice they cannot share.",
     "每个阶段都写成他要什么、她拒绝什么。不要把“他们更不快乐”写三遍。第二阶段里，财富不再是共同的成就，而变成他们无法共享的道德选择。"),
    ("Two sentences for phase 2: Kofi wants enslaved people in order to expand the trade. Anowa refuses, so the reason they left the village is no longer a reason they share.",
     "第二阶段用两句就够：Kofi 想用被奴役的人扩大贸易。Anowa 拒绝，于是当初离开村庄的理由不再是他们共同的理由。"),
    ("A three-box timeline is enough: choice, wealth and refusal, emptiness and gossip. Put one quotation or one precise paraphrase in each box when you have the book. Do not invent a long speech.",
     "三个框的时间线就够：选择、财富与拒绝、空虚与闲话。有书时每格放一句很短的引文或准确转述。不要编造长段台词。"),
    ("“How does the relationship change?” is a how-question. It needs the sequence, not a single adjective. Skipping the slave trade and writing only “they failed to communicate” misses the play’s central split.",
     "“关系如何变化”是 how 的问题，要顺序，不要一个形容词。跳过奴隶贸易、只写“他们缺乏沟通”，就错过了戏的核心分裂。"),
    ("She chooses him. Wealth then asks her to accept what she will not accept. The ending is the cost of that refusal inside that system.",
     "她选择了他。财富随后要求她接受她不能接受的事。结局是这个拒绝在那个制度里的代价。"),
),
"g9en-2-3": _g(
    ("A theme sentence must be provable from one conflict. Materialism: as Kofi’s wealth grows, the marriage and Anowa’s freedom do not. Individual and society: gossip, the parents and the prologue keep a private choice under watch. The tragedy is a personal choice stacked with colonial trade and the village’s judgement, not a single flaw.",
     "主题句必须能被一次冲突证明。物质：Kofi 的财富增加时，婚姻和 Anowa 的自由并没有一起增加。个人与社会：闲话、父母和序幕让私人选择一直被观看。悲剧是个人选择叠上殖民贸易和村庄的评判，不是单一的性格缺陷。"),
    ("Point, then one conflict, then what the audience is pushed to think. Include both character and system. “She was difficult” or “he was greedy” alone will not hold.",
     "先写观点，再写一次冲突，再写观众被推向什么判断。性格和制度都要有。只有“她很难相处”或“他太贪”站不住。"),
    ("“The play shows that wealth can become another kind of master.” Evidence direction: the richer Kofi becomes, the further Anowa is shut out of the moral life of the house. The audience, taught the village’s words in the prologue, has to revise them.",
     "“剧本说明财富可以成为另一种主人。”证据方向：Kofi 越富有，Anowa 就越被排除在这个家的道德生活之外。序幕里学会了村庄用语的观众，不得不修改那些词。"),
    ("In a paragraph, underline the theme sentence and the one conflict. If you cannot find the conflict, the theme sentence is too large.",
     "在段落里给主题句和那一次冲突画线。如果找不到冲突，主题句就太大了。"),
    ("“How does language…?” means who hears the line and what judgement follows. “The language is powerful” is not an analysis. Do not fake a long quotation from memory.",
     "“语言如何……”意思是谁听见这句、随后做出什么判断。“语言很有力”不是分析。不要凭记忆编造长段引文。"),
    ("One conflict proves one theme. Character and the system both belong in the answer.",
     "一次冲突证明一个主题。答案里要同时有性格和制度。"),
),
"g9en-2-4": _g(
    ("Empathic writing is 250–350 words in a character’s voice at one named moment. Use only what that person already knows. Do not retell the play and do not use the ending if the moment is earlier.",
     "移情写作是以人物的声音、在指定的一刻写大约 250 到 350 词。只用那个人当时已经知道的事。不要概述全剧；如果一刻在结局之前，就不要写死亡。"),
    ("Begin inside the moment. Hold the feeling to one object or one sentence just spoken. Anowa can argue a moral case. She should not write a critic’s sentence such as “this shows the theme”.",
     "开头就在那一刻里面。用一个物件或刚说出口的一句话把情绪固定住。Anowa 会争辩道德。她不会写“这说明了主题”这种评论句。"),
    ("Opening for the night Kofi calls buying people “business”: “He called it trade, as if a person could be lifted onto the same list as cloth. I looked at his hands, the hands I chose in Yebi, and I could not make them match the sentence.”",
     "Kofi 把买人称作生意的那个夜里，可以这样开头：“他把这叫做买卖，好像一个人可以和布匹写在同一张单子上。我看着他的手，那双我在 Yebi 选择的手，却无法让它们和这句话对上。”"),
    ("A short plan of five beats is enough: the sentence he has just said; one memory of leaving Yebi; what she will not do; what she still recognises in him; a last line that stays in the night. Cross out any beat that needs the ending.",
     "五个节拍的提纲就够：他刚说的那句；离开 Yebi 的一个记忆；她不愿意做的事；她仍然认得的那个人；停在这个夜里的最后一句。划掉任何需要结局才能成立的节拍。"),
    ("Coursework must be your own words. The marker of a practice on this site only checks that key ideas are present. You still have to judge whether it sounds like her.",
     "课程作业必须是自己的话。本站练习只检测关键想法是否出现。声音像不像她，仍要自己判断。"),
    ("Stay in the moment, in her voice, with no knowledge from later in the play.",
     "留在这一刻，用她的声音，不使用后文才知道的事。"),
),
"g9en-2-5": _g(
    ("A critical point names the play or the writer and makes a judgement that evidence can test. “Anowa is a play” is not a point. Evidence is one short quotation or a precise paraphrase. The explanation covers at least two of meaning, effect, audience and intention.",
     "评论的观点要有剧名或作者，并且是证据能检验的判断。“Anowa 是一部戏”不是观点。依据是一句很短的引文或准确转述。解释至少要写到含义、效果、观众、作者意图中的两项。"),
    ("Write the judgement, then the evidence, then “the audience hears…”, then a return to the question. If the book is not in front of you, say that you are paraphrasing. Do not invent a speech and pretend it is the play.",
     "先写判断，再写依据，再写“观众听见……”，最后回到题目。书不在眼前就说明是转述。不要编一段台词假装它在剧本里。"),
    ("Stronger point: “Aidoo makes Kofi’s wealth a test the marriage fails.” Weaker point: “The play has a prologue.” Only the first can be proved or challenged.",
     "更强的观点：“Aidoo 让 Kofi 的财富成为这场婚姻通不过的考验。”更弱的观点：“剧本有序幕。”只有前者能被证明或反驳。"),
    ("One paragraph, four beats, no bullet points unless asked. Keep any quotation under a line. If you cannot remember a line exactly, paraphrase.",
     "一个段落、四个节拍。除非题目要求，不用项目符号。引文不超过一行。记不准就转述。"),
    ("“Analyse” and “how does the writer” need effect, not a plot summary. A long quotation followed by “this is effective” does not score the explanation.",
     "“Analyse” 和 “how does the writer” 要效果，不要剧情简介。长段引文后面只写 “this is effective”，解释分就没有了。"),
    ("Judgement, short evidence, effect on a reader, return to the question.",
     "判断、短依据、对读者的作用、回到题目。"),
),
}

def _add_guides(more):
    GUIDES.update(more)

# Sciences and economics guides, plus every extra question, follow in the same module.
from .more_c import GUIDES as _G3, EXTRAS as _E3
GUIDES.update(_G3)
EXTRAS = _E3
