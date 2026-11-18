"""Grade 9 English — IGCSE First Language English 0500 and World Literature 0408.

Q3 directed writing, Q4 interview / journal / letter / speech, and the play
Anowa. Teaching notes paraphrase the play. They do not reproduce it.
"""
from __future__ import annotations

PASSAGE = (
    "The valve\n\n"
    "Last March, a 16-year-old named Farah walked a hospital corridor she already knew by heart. "
    "A donated human valve, smaller than a coin, had been stitched into her heart two years earlier. "
    "It was not a machine and not a copy of her. It was tissue from a stranger, matched, cooled and carried overnight.\n\n"
    "Dr Sen, who leads the unit, told our reporter that the waiting list is the real story. "
    "“We can plan an operation,” she said. “We cannot plan a donation.” "
    "Farah’s mother kept the old appointment card in her coat. She did not want a speech about miracles. "
    "She wanted the next family to know what the wait feels like at 2 a.m.\n\n"
    "The article is not a set of instructions. It asks readers to join the register, and it refuses the easy ending: "
    "Farah is well enough to swim, but the list behind her has not grown shorter."
)


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
    return dict(type="structured", id=qid, stem_zh=zh, stem_en=en, answer=answer, exp_zh=ez, exp_en=ee, keywords=keywords, keyword_min=keyword_min, marks=marks)


SPEC = {
    "subject_id": "english",
    "tag": "g9en",
    "chapters": [
        {
            "id": "g9-english-1",
            "code": "0500",
            "order": 1,
            "title_zh": "英语第一语言 · Paper 1",
            "title_en": "First Language English · Paper 1",
            "note_zh": "Q3 是根据阅读材料的定向写作；Q4 是扩展写作，课上练过访谈、日记、书信和演讲。",
            "note_en": "Q3 is directed writing from a reading text. Q4 is the extended response: interview, journal, letter and speech have all been practised.",
            "practice_minutes": 25,
            "units": [{
                "id": "g9-english-1-u1",
                "code": "1",
                "order": 1,
                "title_zh": "阅读与定向写作",
                "title_en": "Reading and directed writing",
                "lessons": [
                    L(
                        "g9en-1-1", "1.1",
                        "Q3：根据材料定向写作",
                        "Q3: directed writing from a text",
                        "能从一篇非虚构材料里选出可用的事实，并按题目要求的读者、目的和体裁改写，而不是复述全文。",
                        "Select usable facts from a non-fiction text and reshape them for the audience, purpose and form the question names, rather than retelling the whole piece.",
                        [
                            ("先标三件事：写给谁、要对方做什么或感到什么、用哪种体裁。", "Mark three things first: who you are writing to, what they should do or feel, and which form you are using."),
                            ("只搬运对这个任务有用的事实。原文的优美句子不一定要保留。", "Carry over only the facts that serve this task. A handsome sentence in the source need not be kept."),
                            ("把事实写成新体裁自己的声音。演讲要用口头的“你”，报告则不用。", "Turn the facts into the voice of the new form. A speech can say “you”; a report should not."),
                            ("结尾要完成目的：报名、劝说或说明，而不是再总结一遍原文。", "The ending completes the purpose — to sign up, persuade or explain — rather than summarising the source again."),
                        ],
                        "课上的非虚构阅读包括科学新闻这一类，例如克隆研究和器官移植。下面用一篇原创短文练习同一套方法，不代替课堂那几篇。\n\n定向写作的分数在于“用了材料”并且“变成了题目要的文本”。若题目要你以医院发言人的身份写一段对家长的说明，Farah 的故事只能作为一个例子，Dr Sen 关于等待名单的话才是论点。不要把原文按段落重写一遍。\n\n" + PASSAGE,
                        "Class reading has included science journalism, such as cloning research and transplants. The original article below is for the same skill. It does not replace those class texts.\n\nMarks depend on using the source and becoming the text the question asks for. If you write as a hospital spokesperson addressing parents, Farah’s story is one example and Dr Sen’s point about the waiting list is the argument. Do not rewrite the article paragraph by paragraph.\n\n" + PASSAGE,
                        "题目：你是医院的学生通讯员。给同年级写一段 120 词左右的说明，劝他们了解器官捐献登记。只能用上文里的事实。\n\n**可用的三点：** 瓣膜来自陌生人而不是机器；医生能安排手术，却不能安排捐献；Farah 已经能游泳，但名单没有变短。语气用“我们”，结尾给出一个具体行动：向家人问起登记。",
                        "Task: you are the hospital’s student reporter. Write about 120 words to your year group, urging them to learn about the donation register. Use only facts from the article above.\n\n**Three facts that earn their place:** the valve came from a stranger, not a machine; a doctor can plan an operation but not a donation; Farah can swim, and the list behind her is not shorter. Use “we”, and end with one action: ask at home about the register.",
                        [
                            ("把原文几乎整篇搬过来，读者和目的都没变。", "Moving the article across almost unchanged, so the audience and purpose never change."),
                            ("加入原文没有的医疗承诺，例如“登记了就一定能救到你的家人”。", "Adding a medical promise the text never makes, such as “joining the register will certainly save your family”."),
                            ("只有劝说的口号，没有任何来自材料的事实。", "Slogans of persuasion and no fact from the source."),
                        ],
                        [
                            mcq("Q3 首先要确定的是？", "The first decision in Q3 is:", "a", "读者、目的和体裁。", "Audience, purpose and form.", [("读者、目的和体裁", "audience, purpose and form"), ("原文有多少个段落", "how many paragraphs the source has"), ("作者的生日", "the writer’s birthday"), ("把每个句子都改短", "making every sentence shorter")]),
                            short("在这篇原创短文里，Dr Sen 认为真正的问题是什么？", "In this original article, what does Dr Sen say the real story is?", "the waiting list", "她说能安排手术，不能安排捐献。", "She can plan an operation, not a donation.", ["the waiting list", "等待名单", "we cannot plan a donation"], 2),
                            mcq("Farah 能游泳这一事实，在劝说文里更适合用来？", "In a persuasive piece, the fact that Farah can swim is best used to:", "b", "说明捐献会改变一个人的生活，同时不能假装名单已经消失。", "Show that a donation changes a life, without pretending the list has gone.", [("证明名单已经清空", "prove that the list is now empty"), ("说明一个人的生活可以改变，同时名单仍在", "show that one life can change while the list remains"), ("代替所有医学事实", "replace every medical fact"), ("说明瓣膜是一台机器", "show that the valve is a machine")]),
                        ],
                    ),
                    L(
                        "g9en-1-2", "1.2",
                        "Q4：访谈、日记、书信、演讲",
                        "Q4: interview, journal, letter and speech",
                        "能根据题目选择并维持一种扩展文体：访谈的问答、日记的私密现在、书信的对象、演讲的口头号召。",
                        "Choose and sustain one extended form: the turns of an interview, the private present of a journal, the addressee of a letter, or the spoken appeal of a speech.",
                        [
                            ("访谈：有采访者和受访者，问题要让回答露出想法，而不是只问是或否。", "Interview: an interviewer and a guest. Questions should let the answers show thinking, not only yes or no."),
                            ("日记：写给自己，可以用未完成的想法，但仍要有场景和感受的变化。", "Journal: written to yourself. Unfinished thoughts are allowed, but a scene and a change of feeling are still needed."),
                            ("书信：称呼和收信人决定能说什么。给校长和给朋友不是同一封信。", "Letter: the greeting and the recipient decide what may be said. A head teacher and a friend do not get the same letter."),
                            ("演讲：有口头标志（你们、停顿、设问），结尾要有一个听众能做的行动。", "Speech: spoken signs (you, a pause, a question to the room) and an ending the audience can act on."),
                        ],
                        "Q4 的评分看的是体裁是否从头到尾站得住，以及想法是否发展，不是看你是否用了某一种“高级词”。四种体裁课上都练过。选定之后不要中途换成另一种：一封信的中间突然出现“记者问”就破了体裁。\n\n不论哪一种，都先写一个会变化的想法。例如从“我想拒绝”到“我知道拒绝要付出什么”。没有变化的篇子会在中段重复同一句。",
                        "Q4 rewards a form that holds from the first line to the last, and an idea that develops. It does not reward a list of ambitious words. All four forms have been practised. Once you choose, do not switch: a letter that suddenly says “the reporter asked” has broken the form.\n\nIn every form, plan one idea that changes. For example, from “I want to refuse” to “I know what the refusal will cost”. A piece that never changes repeats itself in the middle.",
                        "同一件事——你决定把每天四十分钟留给读书而不是再做一套题——分别用日记的一句和演讲的一句来写。\n\n**日记：** I closed the paper. The clock said forty minutes, and I was angry with myself for wanting them.\n\n**演讲：** You know that clock. Give it forty minutes that are not another paper.",
                        "The same decision — forty minutes for reading rather than another paper — in one journal sentence and one speech sentence.\n\n**Journal:** I closed the paper. The clock said forty minutes, and I was angry with myself for wanting them.\n\n**Speech:** You know that clock. Give it forty minutes that are not another paper.",
                        [
                            ("访谈里只有一个声音，没有问题。", "An interview with one voice and no questions."),
                            ("日记写成给校长的正式申请。", "A journal written as a formal application to the head teacher."),
                            ("演讲没有听众，通篇是 “I think that” 的作文腔。", "A speech with no audience, written as an essay of “I think that”."),
                        ],
                        [
                            mcq("一封写给朋友的信，不合适的开头是？", "An unsuitable opening for a letter to a friend is:", "c", "“尊敬的校长先生”。", "“Dear Headteacher”.", [("用对方的名字", "using the friend’s name"), ("提起一件只有你们知道的事", "mentioning something only the two of you know"), ("尊敬的校长先生", "Dear Headteacher"), ("直接说你为什么写", "saying at once why you are writing")]),
                            short("演讲结尾通常要给听众什么？", "What should the ending of a speech usually give the audience?", "something they can do", "一个可以做的行动。", "An action they can take.", ["something they can do", "an action", "一个行动", "a call to act"], 1),
                            mcq("日记和访谈最明显的差别是？", "The clearest difference between a journal and an interview is:", "a", "日记是对自己说的，访谈至少有两个声音。", "A journal speaks to the self; an interview has at least two voices.", [("日记对自己说，访谈有来有往", "a journal speaks to the self; an interview has two voices"), ("日记必须押韵", "a journal must rhyme"), ("访谈不能出现感受", "an interview cannot include feelings"), ("两者都要写成实验报告", "both must be lab reports")]),
                        ],
                    ),
                ],
            }],
        },
        {
            "id": "g9-english-2",
            "code": "0408",
            "order": 2,
            "title_zh": "世界文学 · Anowa",
            "title_en": "World Literature · Anowa",
            "note_zh": "剧本 Anowa（Ama Ata Aidoo）。下面是课堂用的情节与手法说明，不是剧本正文。评论和移情写作请用你自己书上的短引文。",
            "note_en": "The play Anowa, by Ama Ata Aidoo. These are class notes on plot and method, not the text of the play. In a critical or empathic answer, use short quotations from your own copy.",
            "practice_minutes": 25,
            "units": [{
                "id": "g9-english-2-u1",
                "code": "2",
                "order": 1,
                "title_zh": "戏剧与评论",
                "title_en": "Drama and criticism",
                "lessons": [
                    L(
                        "g9en-2-1", "2.1",
                        "背景、序幕与戏剧形式",
                        "Context, the prologue and dramatic form",
                        "能说明剧本发生的时间与地点，并解释序幕里两个评说者怎样让观众先听到社会的判断。",
                        "Place the play in time and location, and explain how the two commentators in the prologue let the audience hear the community’s judgement first.",
                        [
                            ("作者是加纳剧作家 Ama Ata Aidoo。故事发生在十九世纪后期黄金海岸的村镇 Yebi。", "The writer is the Ghanaian playwright Ama Ata Aidoo. The story is set in Yebi, on the nineteenth-century Gold Coast."),
                            ("序幕不是正文的第一场闲谈。一对老人以不同态度预告 Anowa 的选择，观众因此同时听到民间说法。", "The prologue is not small talk before Scene 1. An old pair preview Anowa’s choice from different attitudes, so the audience hears the community’s talk at once."),
                            ("戏剧靠出场、对话和谁在场来推进，不能依赖小说式的内心长篇交代。", "A play moves by entrances, dialogue and who is present. It cannot rely on a novel’s long passage inside a mind."),
                            ("评说者让“个人的选择”从一开始就放在“别人怎么说”旁边。", "The commentators set “one person’s choice” beside “what other people say” from the start."),
                        ],
                        "读剧本先问：这一刻谁在舞台上，谁听得见。序幕里的老人并不代替 Anowa 做决定，他们让观众在认识她之前，先认识村庄已经准备好的两种说法：一个年轻人自己选丈夫，是勇敢，还是给家里带来麻烦。后面的情节会检验这两种说法，而不是简单宣布哪一位老人正确。\n\n写评论时，把序幕称作一种结构选择：作家让社会的声音先于女主人公的声音。不要只写“序幕介绍了背景”。",
                        "Ask, at each moment, who is on stage and who can hear. The old pair in the prologue do not decide for Anowa. Before we know her, they let us hear two versions the village is ready to tell: that a young woman who chooses her own husband is brave, or that she is trouble for the house. Later scenes test those versions. They do not simply award the prize to one elder.\n\nIn criticism, call the prologue a structural choice. The writer lets the community speak before the protagonist does. Do not stop at “the prologue introduces the setting”.",
                        "为什么序幕比一段舞台说明更能表现“个人与社会”？\n\n**解：** 舞台说明可以由读者默读。序幕里的分歧是说出来的，而且两个人互相听得见。社会的判断因此成为戏的一部分，而不只是给读者的注释。",
                        "Why does the prologue show “the individual and society” more strongly than a stage direction would?\n\n**Solution:** A stage direction can be read in silence. The disagreement in the prologue is spoken, and the two speakers can hear each other. The community’s judgement becomes part of the play, not only a note to the reader.",
                        [
                            ("把序幕当成与后面无关的民间故事。", "Treating the prologue as a folk tale that never touches the rest."),
                            ("只介绍作者国籍，不谈这个信息如何帮助阅读十九世纪的贸易与婚姻。", "Giving the writer’s nationality and never saying how it helps a reading of nineteenth-century trade and marriage."),
                            ("用小说的方式写“Anowa 心里想”，却不指出剧本实际上把想法放在了哪一句对话里。", "Writing “Anowa thought” as a novel would, without pointing to the line of dialogue that actually carries it."),
                        ],
                        [
                            mcq("序幕里两个评说者的主要作用是？", "The two commentators in the prologue mainly:", "b", "让观众先听到社会对 Anowa 的不同说法。", "Let the audience hear the community’s competing accounts first.", [("代替 Anowa 做出婚姻决定", "make the marriage choice for Anowa"), ("让社会的不同说法先被听见", "let the community’s competing accounts be heard first"), ("解释后来的全部科学情节", "explain a later science plot"), ("取消戏剧对白的必要", "make dialogue unnecessary")]),
                            short("剧本主要发生在什么地方？", "Where is the play principally set?", "Yebi", "黄金海岸的村镇 Yebi。", "Yebi, on the Gold Coast.", ["Yebi", "the Gold Coast village of Yebi", "耶比"], 1),
                            mcq("讨论戏剧形式时，较有用的做法是？", "A more useful way to discuss dramatic form is to:", "a", "指出谁在场、谁听得见。", "Say who is present and who can hear.", [("指出这一刻谁在舞台上、谁听得见", "say who is on stage and who can hear"), ("把剧本改写成日记再分析", "rewrite the play as a journal and then analyse that"), ("只统计页数", "only count the pages"), ("避免提到序幕", "avoid mentioning the prologue")]),
                        ],
                    ),
                    L(
                        "g9en-2-2", "2.2",
                        "Anowa、三个阶段与她和 Kofi 的关系",
                        "Anowa, the three phases, and Kofi",
                        "能按阶段说明 Anowa 与 Kofi Ako 的关系如何从自己的选择变成财富与孤立。",
                        "Track, phase by phase, how Anowa’s relationship with Kofi Ako moves from a choice of her own to wealth and isolation.",
                        [
                            ("Anowa 拒绝家里安排的对象，选择当时并不富有的 Kofi，并离开 Yebi。", "Anowa refuses the partners her family would choose, marries Kofi when he is not wealthy, and leaves Yebi."),
                            ("第二阶段：贸易带来财富。Kofi 想买下被奴役的人，Anowa 拒绝。两人在孩子的问题上也裂开。", "In the second phase, trade brings wealth. Kofi wants to acquire enslaved people; Anowa refuses. They also split over children."),
                            ("第三阶段：房子富了，婚姻空了。社区的闲话把私人的失败说成公开的耻辱。", "In the third phase the house is rich and the marriage is empty. Gossip turns a private failure into a public shame."),
                            ("关系的变化要用“他要什么、她拒绝什么”来写，不要只用“他们越来越不快乐”。", "Write the change as what he wants and what she refuses, not only as “they grew sadder”."),
                        ],
                        "三个阶段是评论时的骨架。第一阶段的关键是 Anowa 的选择：她不是被抢走的，她是自己走的，而父母 Badua 和 Osam 的忧虑让这个选择从一开始就有代价。第二阶段的关键是财富的来路。Kofi 把成功理解成可以拥有更多的人；Anowa 把同一件事看成不能接受的交易。第三阶段不要写成突然的吵架。它是第二阶段没有解决的问题：没有孩子、有闲话、有钱，而两个人已经不能用同一套词谈论生活。\n\n结局是悲剧性的，两人都死去。写的时候点明代价即可，不必展开血腥细节。",
                        "The three phases are a skeleton for criticism. In the first, the key point is that Anowa chooses. She is not carried off. She leaves, and the worry of her parents, Badua and Osam, puts a cost on that choice at once. In the second, the key point is where the wealth comes from. Kofi reads success as the right to own more people. Anowa reads the same plan as a trade she will not accept. Do not write the third phase as a sudden argument. It is what the second phase never solved: no child, plenty of gossip, money, and two people who no longer have one vocabulary for a life.\n\nThe ending is tragic: both die. Name the cost. You do not need graphic detail.",
                        "用两句话写出第二阶段里关系发生了什么变化。\n\n**解：** Kofi 要用被奴役的劳动力扩大贸易，Anowa 拒绝。财富因此不再是两个人共同的成就，而变成他们无法共享的道德选择。",
                        "In two sentences, say what changes in the relationship in the second phase.\n\n**Solution:** Kofi wants enslaved labour to expand the trade, and Anowa refuses. Wealth stops being a success they share and becomes a moral choice they cannot share.",
                        [
                            ("把 Anowa 写成完全被动，忽略是她自己选择了 Kofi。", "Writing Anowa as entirely passive and forgetting that she chooses Kofi."),
                            ("跳过奴隶贸易这一冲突，只谈“他们缺少沟通”。", "Skipping the conflict about the slave trade and only saying “they failed to communicate”."),
                            ("三个阶段写成三次重复的同一场吵架。", "Writing the three phases as the same argument three times."),
                        ],
                        [
                            short("Anowa 离开村庄时，选择的丈夫是谁？", "Whom does Anowa choose as her husband when she leaves the village?", "Kofi Ako", "Kofi Ako。", "Kofi Ako.", ["Kofi Ako", "Kofi", "科菲"], 1),
                            mcq("第二阶段里，两人最尖锐的分歧是？", "The sharpest split in the second phase is over:", "c", "是否用被奴役的人来扩大财富。", "Whether enslaved people will be used to grow the wealth.", [("晚饭吃什么", "what to eat for dinner"), ("要不要回到序幕重念一遍", "whether to reread the prologue"), ("Kofi 想拥有被奴役的人，Anowa 拒绝", "Kofi wants to own enslaved people, and Anowa refuses"), ("谁来画思维导图", "who will draw the mind map")]),
                            short("写关系变化时，应抓住哪一类句子，而不是只写“他们不快乐”？", "When you write the change, what should you capture instead of only “they were unhappy”?", "what he wants and what she refuses", "欲望与拒绝。", "Desire and refusal.", ["what he wants and what she refuses", "他要什么、她拒绝什么", "his want and her refusal"], 2),
                        ],
                    ),
                    L(
                        "g9en-2-3", "2.3",
                        "语言、悲剧与主题",
                        "Language, tragedy and themes",
                        "能把语言上的一个选择连到主题：物质、财富，以及个人与社会的评判。",
                        "Connect one language choice to a theme: materialism, wealth, and the individual judged by society.",
                        [
                            ("悲剧在这里不只是性格缺陷。殖民贸易和村庄规矩一起把两个人推到没有退路的位置。", "The tragedy is not only a private flaw. Colonial trade and the village’s rules together leave the two of them with no way back."),
                            ("物质主题：财富增加时，婚姻和自由并没有一起增加。", "Materialism: as wealth grows, the marriage and Anowa’s freedom do not grow with it."),
                            ("个人与社会：闲话、父母的警告和序幕的评说，使私人选择一直处在被观看之中。", "Individual and society: gossip, the parents’ warnings and the prologue keep a private choice under watch."),
                            ("分析语言时写“这个说法让谁听见、产生什么判断”，而不只写“用了比喻”。", "When you analyse language, say who hears the phrase and what judgement it produces, not only “there is a metaphor”."),
                        ],
                        "一个好的主题句必须能被某一次冲突证明。例如：“剧本说明财富可以成为另一种主人。”证据方向是 Kofi 越富有，Anowa 越被排除在那个家的道德之外。解释时把观众也算进去：我们先在序幕里学会用村庄的词看她，后来又不得不修改那些词。\n\n不要把悲剧收成“她脾气不好”或“他太贪心”其中一句。性格有份，制度也有份。两者都写，才站得住。",
                        "A good theme sentence has to be provable from one conflict. For example: “The play shows that wealth can become another kind of master.” The evidence runs this way: the richer Kofi becomes, the further Anowa is shut out of the moral life of that house. In the explanation, include the audience. The prologue teaches us the village’s words for her, and later scenes force us to revise them.\n\nDo not reduce the tragedy to “she was difficult” or “he was greedy” alone. Character has a part. The system has a part. An answer that holds includes both.",
                        "用一句话写出物质主题，并点明它落在谁的选择上。\n\n**解：** Kofi 用扩大贸易和购买被奴役的人来理解成功，财富因此取代了当初两个人一起离开村庄的理由。",
                        "Write the materialism theme in one sentence, and name whose choice carries it.\n\n**Solution:** Kofi reads success as a larger trade and the purchase of enslaved people, so wealth replaces the reason the two of them left the village together.",
                        [
                            ("主题句很大，但没有任何阶段或冲突可以证明它。", "A huge theme sentence with no phase or conflict that could prove it."),
                            ("只责怪其中一个人物，完全不提贸易和社区的压力。", "Blaming only one character and never mentioning trade or the pressure of the community."),
                            ("说“语言很有力”，却不说那一句话对谁产生了什么判断。", "Saying “the language is powerful” and never saying what judgement a line produces, or for whom."),
                        ],
                        [
                            mcq("本剧的悲剧更准确的说法是？", "The more accurate account of the tragedy is:", "d", "个人的选择与贸易制度、社区评判叠在一起。", "A personal choice is stacked with the trade system and the community’s judgement.", [("只是一次误会", "only a misunderstanding"), ("只是 Anowa 的性格问题", "only a flaw in Anowa"), ("只是天气不好", "only bad weather"), ("个人选择与贸易制度、社区评判叠在一起", "a personal choice stacked with the trade system and the community’s judgement")]),
                            short("物质主题可以用哪一个变化来证明？", "Which change can prove the theme of materialism?", "wealth grows while the marriage empties", "财富增加，婚姻却空了。", "Wealth grows and the marriage empties.", ["wealth grows while the marriage empties", "财富增加而关系破裂", "Kofi grows rich and Anowa is shut out"], 2),
                            mcq("分析一句台词时，最好继续问的是？", "After you notice a line, the better next question is:", "a", "谁听见了它，并因此做出什么判断？", "Who hears it, and what judgement follows?", [("谁听见了，并因此做出什么判断", "who hears it, and what judgement follows"), ("这一页有多少个逗号", "how many commas are on the page"), ("能不能换成一篇日记", "whether it could be a journal instead"), ("作者的出版商是谁", "who the publisher was")]),
                        ],
                    ),
                    L(
                        "g9en-2-4", "2.4",
                        "移情写作",
                        "Empathic writing",
                        "能以剧中人物的声音，在指定的一刻写 250 到 350 词，只使用那一刻已经知道的事。",
                        "Write 250–350 words in a character’s voice at a named moment, using only what that person knows then.",
                        [
                            ("开头就处在那一刻，不要从童年重述整部剧。", "Begin inside the moment. Do not retell the play from childhood."),
                            ("只用那个时间点之前发生过的事。后面的结局还不知道。", "Use only what has already happened by that moment. The ending is not yet known."),
                            ("声音要像那个人：Anowa 会争辩道德，不会写成一份历史报告。", "The voice has to sound like that person. Anowa will argue a moral case; she will not write a history report."),
                            ("篇幅约 250–350 词。用一个具体物件或一句话把情绪固定住。", "Aim for about 250–350 words. Hold the feeling to one object or one sentence that has just been said."),
                        ],
                        "移情不是缩写情节。阅卷人要看见你坐在那一刻里。若题目是 Anowa 拒绝把被奴役的人买进家里的那个晚上，她可以想起离开 Yebi 的理由，但不能知道最后的死亡。她对 Kofi 的称呼、她对“房子变大了”的看法，都应该像她会说的话。\n\n可以有不满，也要有她仍然认得的那个人。只有愤怒、没有关系的文章会变成演讲，而不像这个妻子在这个夜里的想法。作业和课程作业要用自己的话；这里的练习同样不要整段抄剧本。",
                        "Empathic writing is not a plot summary. The reader has to find you inside the moment. If the moment is the night Anowa refuses to have enslaved people bought into the house, she may remember why she left Yebi. She cannot know the deaths at the end. The name she uses for Kofi, and what she thinks when the house grows larger, should sound like her.\n\nAnger can be there, and so can the person she still recognises. A piece that is only rage, with no relationship, becomes a speech rather than that wife on that night. Coursework has to be your own words. This practice, too, should not copy out the play.",
                        "一刻：Kofi 第一次把“买人”说成做生意。用 Anowa 的声音写开头两句。\n\n**示例：** He called it trade, as if a person could be lifted onto the same list as cloth. I looked at his hands, the hands I chose in Yebi, and I could not make them match the sentence.",
                        "Moment: the first time Kofi calls buying people “business”. Write the opening two sentences in Anowa’s voice.\n\n**Sample:** He called it trade, as if a person could be lifted onto the same list as cloth. I looked at his hands, the hands I chose in Yebi, and I could not make them match the sentence.",
                        [
                            ("从序幕写到结局，指定的那一刻反而一笔带过。", "Writing from the prologue to the ending, so the named moment is only a glance."),
                            ("使用人物当时不可能知道的后文。", "Using later events the character cannot yet know."),
                            ("声音变成评论员，满篇 “This shows that the theme is”。", "The voice becomes a critic, full of “this shows that the theme is”."),
                        ],
                        [
                            mcq("移情写作最应避免的是？", "Empathic writing should above all avoid:", "b", "写成从头到尾的情节简介。", "A plot summary from start to finish.", [("待在指定的那一刻", "staying inside the named moment"), ("把整部剧从头概述一遍", "summarising the whole play from the start"), ("使用人物会说的词", "using words the character would say"), ("写出矛盾的心情", "writing a mixed feeling")]),
                            short("如果一刻是在结局之前，文章能不能写两人的死亡？", "If the moment is before the ending, may the piece describe their deaths?", "no", "那一刻还不知道结局。", "The character does not yet know the ending.", ["no", "不能", "not yet"], 1),
                            short("字数通常要求在哪个范围？", "What word range is usually required?", "250-350", "大约 250 到 350 词。", "About 250 to 350 words.", ["250-350", "250 to 350", "250–350"], 1),
                        ],
                    ),
                    L(
                        "g9en-2-5", "2.5",
                        "评论段：PEEL 与短引文",
                        "A critical paragraph: PEEL and a short quotation",
                        "能写一个 PEEL 评论段：一个观点、一处很短的引文或准确转述、对含义和效果的解释、回到题目。",
                        "Write one critical PEEL paragraph: a point, one very short quotation or a precise paraphrase, an explanation of meaning and effect, and a return to the question.",
                        [
                            ("观点句里要有剧名或人物，以及一个可辩的判断。", "The point names the play or the character and makes a judgement that could be argued."),
                            ("引文要短。课堂评论常用一两处不超过一行的原文，并说明它如何作用于听众。", "Keep quotations short. A class paragraph often uses one or two lines of no more than a line each, and says how they work on an audience."),
                            ("解释要写含义、效果、观众和作者意图中的至少两项。", "The explanation should cover at least two of: meaning, effect, the audience, and the writer’s intention."),
                            ("若手边没有书，就明确写成转述，不要编造看起来像原文的长句。", "If the book is not in front of you, paraphrase and say so. Do not invent a long sentence that pretends to be the play."),
                        ],
                        "PEEL 用在文学评论里时，第二个 E 要比语文课的说明更具体：这个说法让观众站到谁一边，或者让观众不安。例如观点是“财富把 Kofi 和 Anowa 分开”。转述证据：他把购买被奴役的人说成生意。解释：观众听出，当初那个愿意跟她离开村庄的人，开始用市场的词谈论人。作者让这句话由 Kofi 自己说出来，而不是由序幕里的老人宣布，所以分裂发生在婚姻内部。\n\n没有书就不要伪造大段台词。用 “Kofi frames the purchase as trade” 这种转述，并在能引用时只引很短的一句。",
                        "In literature, the second E has to be more precise than a general explanation. Say whom the audience is pushed toward, or why the audience is made uneasy. Point: wealth separates Kofi from Anowa. Paraphrased evidence: he frames the purchase of enslaved people as business. Explanation: the audience hears the man who left the village with her begin to talk about people in the language of a market. The writer gives the sentence to Kofi rather than to the elders in the prologue, so the split happens inside the marriage.\n\nWithout the book, do not fake a long speech. Write “Kofi frames the purchase as trade”, and when you can quote, quote only a very short line.",
                        "判断下面哪一句更像评论段的观点句。\n\nA. Anowa is a play.\nB. In Anowa, Aidoo makes Kofi’s wealth a moral test that the marriage cannot pass.\n\n**解：** B。它有判断，并且可以被后面的证据检验。A 只是事实。",
                        "Which sentence is closer to a point in a critical paragraph?\n\nA. Anowa is a play.\nB. In Anowa, Aidoo makes Kofi’s wealth a moral test that the marriage cannot pass.\n\n**Solution:** B. It makes a judgement that evidence can test. A is only a fact.",
                        [
                            ("观点句没有判断，只宣布剧名。", "A point with no judgement, only the title."),
                            ("引文很长，解释却只有 “this is effective”。", "A long quotation and an explanation that only says “this is effective”."),
                            ("编造一大段假装来自剧本的对白。", "Inventing a long speech and pretending it is in the play."),
                        ],
                        [
                            mcq("更合格的观点句是？", "The stronger point sentence is:", "b", "带有可以论证的判断。", "It contains a judgement that can be argued.", [("Anowa is a play by Aidoo.", "Anowa is a play by Aidoo."), ("Aidoo makes Kofi’s wealth a test the marriage fails.", "Aidoo makes Kofi’s wealth a test the marriage fails."), ("The play has a prologue.", "The play has a prologue."), ("Yebi is a place.", "Yebi is a place.")]),
                            short("解释一句台词时，至少还应写哪两类分析中的一类？含义之外。", "Besides meaning, name one other kind of comment an explanation should include.", "effect on the audience", "效果、观众或作者意图。", "Effect, the audience, or the writer’s intention.", ["effect on the audience", "the writer's intention", "效果", "audience"], 2),
                            mcq("手边没有剧本时，正确的做法是？", "If you do not have the play in front of you, you should:", "c", "转述，并避免编造长段原文。", "Paraphrase, and do not invent a long passage of the play.", [("编一段看起来像原文的台词", "invent a speech that looks like the original"), ("放弃观点", "abandon the point"), ("明确转述，只在确实记得时使用很短的引文", "paraphrase, and use a very short quotation only when you really remember it"), ("改写科学说明文", "switch to a science report")]),
                        ],
                    ),
                ],
            }],
        },
    ],
    "paper": {
        "id": "paper-g9-english",
        "title_zh": "练习卷 · Q4 书信、PEEL 与移情写作",
        "title_en": "Practice paper · Q4 letter, PEEL and empathic writing",
        "minutes": 50,
        "published": "2026-11-18T12:00:00+08:00",
        "items": [
            ("g9en-1-2", mcq(
                "Q4 要求你写一封给朋友的信。哪一项最能维持体裁？",
                "Q4 asks for a letter to a friend. Which choice best sustains the form?",
                "a",
                "用朋友的名字，并写出只有你们之间说得通的理由。",
                "Use the friend’s name and a reason that belongs to that friendship.",
                [("Dear Mira — you were there when I refused, so you know why I am writing.", "Dear Mira — you were there when I refused, so you know why I am writing."), ("Dear Sir or Madam, I wish to apply for the post of theme.", "Dear Sir or Madam, I wish to apply for the post of theme."), ("Reporter: Why did you do it?  Me: Because.", "Reporter: Why did you do it? Me: Because."), ("22 March. Weather fine. This journal is a speech.", "22 March. Weather fine. This journal is a speech.")],
                1,
            )),
            ("g9en-1-2", short(
                "演讲和日记都要写“我决定把四十分钟留给读书”。日记更应具备哪一种声音？",
                "Both a speech and a journal describe keeping forty minutes for reading. What kind of voice should the journal have?",
                "a private voice to yourself",
                "日记是写给自己的。",
                "A journal is written to yourself.",
                ["a private voice to yourself", "private", "写给自己", "to myself"],
                2,
            )),
            ("g9en-2-5", write(
                "q-g9en-peel",
                "评论段（PEEL）。题目：In Anowa, how does Aidoo show that wealth can divide two people who chose each other? 写一段英语。要有判断、一处转述或很短的引文、对效果的解释。不要编造大段原文。系统按要点给分，语言质量请对照后面的参考段自评。",
                "Critical paragraph (PEEL). Question: In Anowa, how does Aidoo show that wealth can divide two people who chose each other? Write one English paragraph with a judgement, a paraphrase or a very short quotation, and a comment on effect. Do not invent a long passage of the play. Key points are marked automatically; compare the quality of the writing with the sample afterwards.",
                "See the sample paragraph in the explanation.",
                "参考段：In Anowa, Aidoo makes Kofi’s wealth a test that the marriage cannot pass. The man Anowa chose when he was poor later frames the purchase of enslaved people as a way to grow the trade. The audience hears the vocabulary of a market inside a house that began as a choice against the village. Because the line belongs to Kofi rather than to the elders in the prologue, the division is not only public gossip. It is the couple’s own language breaking in two.",
                "Sample: In Anowa, Aidoo makes Kofi’s wealth a test that the marriage cannot pass. The man Anowa chose when he was poor later frames the purchase of enslaved people as a way to grow the trade. The audience hears the vocabulary of a market inside a house that began as a choice against the village. Because the line belongs to Kofi rather than to the elders in the prologue, the division is not only public gossip. It is the couple’s own language breaking in two.",
                ["Anowa", "Kofi", "wealth", "slave", "audience", "trade"],
                3,
                8,
            )),
            ("g9en-2-4", write(
                "q-g9en-empathic",
                "移情写作（约 250–350 词）。以 Anowa 的声音，写她第一次听见 Kofi 把购买被奴役的人称作生意的那个夜里。不要写结局，不要概述全剧，不要大段抄录剧本。系统只检测关键想法是否出现；词句是否像她，请对照参考开头自评。",
                "Empathic writing, about 250–350 words. In Anowa’s voice, write the night she first hears Kofi call the purchase of enslaved people “business”. Do not write the ending, do not summarise the whole play, and do not copy long passages. The marker only checks that key ideas are present. Judge for yourself whether the voice sounds like hers, using the sample opening.",
                "See the sample opening in the explanation.",
                "参考开头（不是唯一写法）：He called it trade, as if a person could be lifted onto the same list as cloth. I looked at his hands — the hands I chose in Yebi, when there was no big house — and I could not make them match the sentence. We left so that I would not be given away. I will not help him do the giving.",
                "Sample opening, not the only possible one: He called it trade, as if a person could be lifted onto the same list as cloth. I looked at his hands — the hands I chose in Yebi, when there was no big house — and I could not make them match the sentence. We left so that I would not be given away. I will not help him do the giving.",
                ["Kofi", "Yebi", "trade", "slave", "chose", "house"],
                3,
                10,
            )),
        ],
    },
}
