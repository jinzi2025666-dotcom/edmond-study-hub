"""Extra graded questions for lessons that are not already banked in more_c."""
from .expansion import mcq, short, num, write

def S(diff, zh, en, answer, ez, ee, accepted, marks=1):
    return short(diff, zh, en, answer, ez, ee, accepted, marks)

def M(diff, zh, en, answer, ez, ee, options, marks=1):
    return mcq(diff, zh, en, answer, ez, ee, options, marks)

def N(diff, zh, en, answer, ez, ee, marks=1, tolerance=0):
    return num(diff, zh, en, answer, ez, ee, marks, tolerance)

EXTRAS = {
"g9en-1-1": [
    M("basic", "Q3 首先要确定的三件事是？", "The first three decisions in Q3 are:", "a", "读者、目的、体裁。", "Audience, purpose, form.", [("读者、目的、体裁", "audience, purpose and form"), ("原文段落数", "the number of paragraphs"), ("作者生日", "the writer’s birthday"), ("把每句都改短", "making every sentence shorter")]),
    S("exam", "为什么不能把原文几乎整篇搬进新体裁？", "Why must you not move the source across almost unchanged?", "读者和目的都没有变", "定向写作要改任务。", "The task has to change.", ["读者和目的都没有变", "audience and purpose never change"], 2),
    S("challenge", "医院短文里，Dr Sen 认为真正的困难是什么？", "In the hospital article, what does Dr Sen say the real difficulty is?", "等待名单，捐献无法被安排", "能安排手术，不能安排捐献。", "An operation can be planned; a donation cannot.", ["等待名单", "the waiting list", "不能安排捐献"], 2),
    S("unit", "FLE 单元：定向写作结尾应当完成什么？", "FLE unit: what should the ending of directed writing complete?", "题目要求的目的，而不是再概括原文", "结尾服务新任务。", "The ending serves the new task.", ["题目的目的", "the purpose of the task", "不是再概括原文"], 2),
    M("unit", "下列哪一项是材料允许的事实？", "Which fact is allowed by the source?", "b", "瓣膜来自陌生人。", "The valve came from a stranger.", [("登记一定能救家人", "joining the register will certainly save your family"), ("瓣膜来自陌生人而不是机器", "the valve came from a stranger, not a machine"), ("名单已经清空", "the list is now empty"), ("Farah 不能游泳", "Farah cannot swim")]),
],
"g9en-1-2": [
    M("basic", "日记和访谈最明显的差别是？", "The clearest difference between a journal and an interview is:", "a", "日记对自己，访谈有来有往。", "A journal speaks to the self; an interview has two voices.", [("日记对自己，访谈有两个声音", "journal to the self, interview has two voices"), ("日记必须押韵", "a journal must rhyme"), ("访谈不能有感受", "an interview cannot include feelings"), ("两者都是实验报告", "both are lab reports")]),
    S("exam", "演讲结尾通常要给听众什么？", "What should a speech ending give the audience?", "一个可以做的行动", "号召要能被执行。", "A call they can act on.", ["一个行动", "an action", "something they can do"], 1),
    S("challenge", "同一件“四十分钟读书”的决定，日记的声音应当是？", "For the same forty-minute decision, the journal voice should be:", "写给自己的私密声音", "不是给校长的申请。", "Not an application to the head.", ["写给自己", "private", "to yourself"], 2),
    S("unit", "Q4 单元：为什么中途从书信改成访谈会丢分？", "Q4 unit: why does switching from a letter to an interview lose marks?", "体裁没有从头到尾站稳", "形式必须保持。", "The form has to hold.", ["体裁没有保持", "the form does not hold", "switched form"], 2),
],
"g9en-2-1": [
    S("basic", "剧本主要发生在哪里？", "Where is the play principally set?", "Yebi", "十九世纪黄金海岸的村镇。", "A town on the nineteenth-century Gold Coast.", ["Yebi", "耶比"], 1),
    M("exam", "序幕的主要作用是？", "The prologue mainly:", "b", "让社会的不同说法先被听见。", "Lets the community’s accounts be heard first.", [("替 Anowa 决定婚姻", "decides the marriage for Anowa"), ("让社会的说法先被听见", "lets the community speak first"), ("取消对白", "cancels dialogue"), ("解释后来的科学情节", "explains a later science plot")]),
    S("challenge", "为什么序幕比一段舞台说明更能表现个人与社会？", "Why does the prologue show the individual and society more strongly than a stage direction?", "分歧是说出来的，双方和观众都听得见", "舞台说明可以默读。", "A stage direction can be read in silence.", ["说出来并且听得见", "it is spoken and heard", "双方都听得见"], 2),
    S("unit", "文学单元：评论序幕时不能只写什么？", "Literature unit: what is not enough when writing about the prologue?", "只写它介绍了背景或只写作者国籍", "要写结构选择。", "You need the structural choice.", ["只介绍背景", "only the setting", "只写国籍"], 2),
],
"g9en-2-2": [
    S("basic", "Anowa 离开村庄时选择的丈夫是谁？", "Whom does Anowa choose when she leaves?", "Kofi Ako", "Kofi Ako。", "Kofi Ako.", ["Kofi Ako", "Kofi", "科菲"], 1),
    M("exam", "第二阶段最尖锐的分歧是？", "The sharpest split in phase 2 is:", "c", "是否用被奴役的人扩大财富。", "Whether enslaved people will grow the wealth.", [("晚饭", "dinner"), ("重读序幕", "rereading the prologue"), ("Kofi 想拥有被奴役的人，Anowa 拒绝", "Kofi wants enslaved people; Anowa refuses"), ("谁画导图", "who draws the map")]),
    S("challenge", "写关系变化时，应抓住哪一类句子？", "When writing the change, what kind of sentence should you use?", "他要什么、她拒绝什么", "不要只写不快乐。", "Not only that they were unhappy.", ["他要什么她拒绝什么", "what he wants and what she refuses"], 2),
    S("unit", "单元：三个阶段如果写成同一场吵架，问题在哪里？", "Unit: what is wrong if the three phases are the same argument three times?", "没有写出关系的变化", "阶段要有发展。", "The phases must develop.", ["没有变化", "no change", "same argument"], 2),
],
"g9en-2-3": [
    M("basic", "本剧悲剧更准确的说法是？", "The more accurate account of the tragedy is:", "d", "个人选择与贸易制度、社区评判叠在一起。", "A personal choice stacked with trade and the community.", [("只是误会", "only a misunderstanding"), ("只是 Anowa 的性格", "only Anowa’s character"), ("只是天气", "only the weather"), ("个人选择叠上制度和社区", "choice stacked with the system and the community")]),
    S("exam", "物质主题可以用哪一个变化证明？", "Which change can prove materialism?", "财富增加而婚姻变空", "财富与关系反向。", "Wealth and the marriage move apart.", ["财富增加婚姻变空", "wealth grows and the marriage empties"], 2),
    S("challenge", "分析一句台词时，除了含义还要问什么？", "Besides meaning, what else should you ask of a line?", "谁听见，并做出什么判断", "效果和观众。", "Effect and audience.", ["谁听见", "who hears it", "what judgement"], 2),
],
"g9en-2-4": [
    M("basic", "移情写作最应避免的是？", "Empathic writing should above all avoid:", "b", "从头到尾的情节简介。", "A plot summary.", [("留在指定的一刻", "staying in the moment"), ("把整部剧概述一遍", "summarising the whole play"), ("用人物会说的词", "using the character’s words"), ("写出矛盾的心情", "a mixed feeling")]),
    S("exam", "如果一刻在结局之前，能不能写两人的死亡？", "If the moment is before the ending, may you describe their deaths?", "不能", "那一刻还不知道。", "The character does not know yet.", ["不能", "no", "not yet"], 1),
    S("unit", "移情单元：声音变成 “this shows the theme” 时，问题是什么？", "Empathic unit: what is wrong when the voice says “this shows the theme”?", "变成了评论员，不再是人物", "要留在她的夜里。", "It has become a critic.", ["变成评论", "becomes a critic", "not her voice"], 2),
],
"g9en-2-5": [
    M("basic", "更合格的观点句是？", "The stronger point is:", "b", "带有可论证的判断。", "A judgement that can be argued.", [("Anowa is a play.", "Anowa is a play."), ("Aidoo makes Kofi’s wealth a test the marriage fails.", "Aidoo makes Kofi’s wealth a test the marriage fails."), ("The play has a prologue.", "The play has a prologue."), ("Yebi is a place.", "Yebi is a place.")]),
    S("exam", "手边没有剧本时应当怎样处理引文？", "If you do not have the play, how should you handle quotation?", "转述，不编造长段原文", "记不准就不要假装引用。", "Paraphrase rather than fake a speech.", ["转述", "paraphrase", "do not invent"], 2),
    S("unit", "PEEL 单元：第二个 E 至少还要写到什么？", "PEEL unit: besides meaning, the second E should also reach:", "效果、观众或作者意图", "至少再加一项。", "At least one more of those.", ["效果", "audience", "effect", "作者意图"], 2),
],
"g9cs-7-1": [
    M("basic", "画流程图通常属于？", "Drawing a flowchart belongs to:", "b", "设计。", "Design.", [("出售之后", "after the program is sold"), ("设计", "design"), ("只换显示器", "changing the monitor"), ("校验录错", "verification of a typo")]),
    S("exam", "把大问题拆成子问题叫什么？", "Splitting a large problem into sub-problems is called:", "decomposition", "分解。", "Decomposition.", ["decomposition", "分解"], 1),
    S("unit", "单元：测试只运行一次成功，为什么不够？", "Unit: why is one successful run not enough testing?", "还要用正常、边界和异常数据", "测试要分类。", "Testing needs kinds of data.", ["边界和异常", "boundary and abnormal", "more than one kind"], 2),
],
"g9cs-7-2": [
    M("basic", "菱形表示？", "A diamond means:", "c", "判断。", "A decision.", [("开始", "start"), ("输入", "input"), ("判断", "a decision"), ("必须执行的赋值", "an assignment that must run")]),
    S("exam", "判断框通常有几个出口？", "How many exits does a decision usually have?", "2", "YES 和 NO。", "YES and NO.", ["2", "two", "两个"], 1),
    S("unit", "单元：循环在流程图上长什么样？", "Unit: what does a loop look like on a flowchart?", "判断的一个箭头回到前面的过程", "箭头送回去。", "An arrow returns to an earlier process.", ["箭头回到前面", "arrow returns", "decision sends you back"], 2),
],
"g9cs-7-3": [
    S("basic", "伪代码的赋值符号是什么？", "Pseudocode’s assignment symbol?", "←", "左箭头。", "A left arrow.", ["←", "<-"], 1),
    S("exam", "Python 要得到 1、2、3、4、5，range 怎样写？", "Which range produces 1, 2, 3, 4 and 5?", "range(1, 6)", "右端不包含。", "The end is excluded.", ["range(1, 6)", "range(1,6)"], 2),
    M("unit", "单元：input() 得到的值在相加前通常要？", "Unit: before adding a value from input(), you usually:", "d", "转换成 int 或 float。", "Convert to int or float.", [("什么都不用做", "do nothing"), ("改成流程图", "turn it into a chart"), ("乘以 0", "multiply by 0"), ("转换成 int 或 float", "convert to int or float")]),
],
"g9cs-7-4": [
    N("basic", "3、5、2 的总和？", "Total of 3, 5 and 2?", "10", "3+5+2。", "3+5+2.", 1, 0),
    N("exam", "其中大于 4 的有几个？", "How many are greater than 4?", "1", "只有 5。", "Only 5.", 1, 0),
    N("challenge", "若把最大值初值错设为 0，而数据是 -2、-5、-1，错误的最大值会是多少？正确最大值是 -1。本题问错误做法得到的“最大值”。", "If max is wrongly started at 0 for -2, -5, -1, what wrong maximum appears?", "0", "0 比所有数据都大，所以不会被更新。", "0 is larger than every value, so it is never replaced.", 2, 0),
    N("unit", "单元：4、7、1、9 的平均数？", "Unit: average of 4, 7, 1, 9?", "5.25", "21/4。", "21/4.", 2, 0.01),
],
"g9cs-7-5": [
    M("basic", "两次输入同一个学号并比较，这是？", "Entering an ID twice and comparing is:", "b", "校验。", "Verification.", [("范围验证", "range validation"), ("校验", "verification"), ("求平均", "an average"), ("分解", "decomposition")]),
    S("exam", "年龄 11 到 18，写出一个应被接受的边界值。", "Age 11 to 18. One boundary value that should be accepted.", "11", "11 或 18。", "11 or 18.", ["11", "18"], 1),
    S("unit", "单元：为什么范围检查抓不住把 16 打成 17？", "Unit: why does a range check miss 17 typed instead of 16?", "17 仍然合理，只是不是事实", "那是校验的工作。", "That is verification’s job.", ["17 仍然合理", "17 is still reasonable", "not the true value"], 2),
],
"g9cs-7-8": [
    N("basic", "WHILE x 从 1 加到 total，直到 x 变成 4 后停止。结束时 total 是 1+2+3。total=?", "The WHILE adds x into total for x = 1, 2, 3. Final total?", "6", "6。", "6.", 1, 0),
    M("exam", "REPEAT 循环体至少执行几次？", "A REPEAT body runs at least how many times?", "a", "一次。", "Once.", [("一次", "once"), ("零次", "never"), ("必须 n 次", "exactly n"), ("两次因为有 UNTIL", "twice because of UNTIL")]),
    S("unit", "单元：追踪表里为什么不能把三次循环写在一行？", "Unit: why not write three loops in one row of a trace?", "看不见每一步变量如何变化", "要展开。", "Unroll it.", ["看不见每一步", "cannot see each step", "must unroll"], 2),
],
"g9cs-7-9": [
    S("basic", "计数器应在哪里变成 0？", "Where is a counter set to 0?", "循环之前", "在循环外。", "Before the loop.", ["循环之前", "before the loop", "outside the loop"], 1),
    S("exam", "用 -1 结束输入时，-1 应当？", "If -1 ends the input, -1 should be:", "不算作数据", "它是哨兵。", "It is a sentinel.", ["不算作数据", "not data", "ignored"], 1),
    S("unit", "单元：题目要求计数，为什么不能交一段冒泡排序？", "Unit: the task is a count. Why is a bubble sort not an answer?", "它没有完成题目要求的算法", "要按任务写。", "Write the algorithm that was asked for.", ["没有完成题目", "does not do the task", "wrong algorithm"], 2),
],
"g9cs-8-1": [
    M("basic", "必须把结果交还调用处的是？", "Which must hand a result back?", "b", "函数。", "A function.", [("过程", "a procedure"), ("函数", "a function"), ("箭头", "an arrow"), ("注释", "a comment")]),
    S("exam", "只在子程序内部有效的变量叫什么？", "A variable that exists only inside the sub-routine is:", "local", "局部变量。", "Local.", ["local", "局部变量", "a local variable"], 1),
    S("unit", "编程单元：为什么能用参数就不要用全局变量传递分数？", "Programming unit: why pass a mark as a parameter rather than a global?", "全局变量任何地方都能改，容易出错", "参数更清楚。", "A global can be changed anywhere.", ["任何地方都能改", "can be changed anywhere", "use a parameter"], 2),
],
"g9cs-8-2": [
    N("basic", "伪代码 A[1]=4，A[2]=9。A[2] 是多少？", "In pseudocode A[1]=4, A[2]=9. What is A[2]?", "9", "第二格。", "The second cell.", 1, 0),
    S("exam", "什么时候必须用数组而不能只保留总和？", "When must you keep an array rather than only a total?", "还要再次使用每一个数", "例如第二遍比较平均值。", "When each value is needed again.", ["还要再次使用", "needed again", "second pass"], 2),
    N("unit", "单元：Python 列表 marks 的第一格下标是多少？", "Unit: the index of the first cell of a Python list?", "0", "从 0 开始。", "Python starts at 0.", 1, 0),
],
"g9ec-1": [
    M("basic", "稀缺的直接原因是？", "Scarcity exists because:", "a", "欲望无限而资源有限。", "Unlimited wants and limited resources.", [("欲望无限而资源有限", "unlimited wants and limited resources"), ("政府禁止生产", "production is banned"), ("所有物品免费", "every good is free"), ("价格永远为零", "price is always zero")]),
    S("exam", "经济物品和自由物品的差别？", "Difference between an economic good and a free good?", "经济物品有机会成本", "自由物品没有。", "A free good has none.", ["经济物品有机会成本", "an economic good has an opportunity cost"], 2),
    S("unit", "第 1–4 章单元：定义稀缺，并举一个不是“已经用完”的例子。", "Chapters 1–4 unit: define scarcity and give an example that is not “nothing left”.", "欲望无限资源有限，例如食堂座位要选择", "定义加例子。", "Definition plus example.", ["欲望无限", "unlimited wants", "座位"], 4),
],
"g9ec-2": [
    S("basic", "机器和厂房属于哪一要素？", "Machines and buildings are which factor?", "capital", "资本。", "Capital.", ["capital", "资本"], 1),
    M("exam", "企业家才能的报酬通常是？", "The reward to enterprise is usually:", "d", "利润。", "Profit.", [("地租", "rent"), ("工资", "wages"), ("利息", "interest"), ("利润", "profit")]),
    S("unit", "单元：为什么家里没用于生产的存款不是资本？", "Unit: why are household savings not used in production not capital?", "资本必须是用于生产的人造物品", "现金本身不是工具。", "Capital is a human-made aid to production.", ["用于生产", "used in production", "not a tool"], 2),
],
"g9ec-3": [
    S("basic", "机会成本的定义？", "Define opportunity cost.", "放弃的次优选择", "不是所有没选的。", "Not every rejected option.", ["放弃的次优选择", "next best alternative forgone", "次优"], 2),
    M("exam", "政府建学校，次优是公路。机会成本是？", "A school is built; the next best was a road. The opportunity cost is:", "b", "没建的公路。", "The road not built.", [("学校的砖", "the bricks"), ("没建的公路", "the road not built"), ("政府的名称", "the government’s name"), ("零，因为学校有用", "zero, because a school is useful")]),
    S("unit", "单元：价格和机会成本为什么不是同一个东西？", "Unit: why is price not the same thing as opportunity cost?", "价格是付出的钱，机会成本是放弃的那一个次优物品", "6 元不是那支笔。", "Six dollars is not the pen.", ["放弃的物品", "the good given up", "not the money"], 3),
],
"g9ec-4": [
    M("basic", "生产可能性曲线以内的点表示？", "A point inside the PPC shows:", "a", "资源未充分使用。", "Resources not fully used.", [("资源未充分使用", "resources not fully used"), ("目前无法达到", "currently impossible"), ("机会成本为零", "zero opportunity cost"), ("技术已经进步", "technology has already improved")]),
    S("exam", "沿曲线移动说明什么？", "What does a movement along the curve show?", "机会成本或取舍", "一种增加，另一种减少。", "More of one means less of the other.", ["机会成本", "opportunity cost", "取舍", "a trade-off"], 2),
    M("unit", "单元：发现新资源最可能使曲线？", "Unit: new resources would most likely make the curve:", "c", "向外平移。", "Shift outwards.", [("沿原曲线滑动", "slide along it"), ("变成一个点", "become one point"), ("向外平移", "shift outwards"), ("消失", "disappear")]),
],
"g9ec-5": [
    M("basic", "全国失业率属于？", "The national unemployment rate belongs to:", "b", "宏观。", "Macroeconomics.", [("一家企业的成本", "one firm’s costs"), ("宏观经济", "macroeconomics"), ("一种商品的需求", "demand for one good"), ("机会成本的定义", "the definition of opportunity cost")]),
    S("exam", "举一个微观问题。", "Give one microeconomic question.", "一种商品的价格", "个别市场即可。", "An individual market.", ["一种商品的价格", "the price of one good", "一家企业雇多少人"], 2),
    S("unit", "第 5–9 章单元：为什么一个大城市的出租车市场仍是微观？", "Chapters 5–9 unit: why is a taxi market in a large city still micro?", "它仍是一个市场，不是整个经济", "规模大不等于宏观。", "Size is not the whole economy.", ["一个市场", "one market", "not the whole economy"], 2),
],
"g9ec-6": [
    S("basic", "配置资源的三个基本问题，写出其中两个。", "Name two of the three basic questions.", "生产什么和如何生产", "还有为谁生产。", "And for whom.", ["生产什么和如何生产", "what and how", "what and for whom"], 2),
    M("exam", "市场经济中资源主要被什么引导？", "In a market, resources are guided mainly by:", "c", "价格和利润。", "Prices and profit.", [("没有任何价格的配额", "a quota and no prices"), ("抽签", "a random draw"), ("价格和利润", "prices and profit"), ("不需要信息", "no information")]),
    S("unit", "单元：为什么路灯说明纯市场可能供给不足？", "Unit: why do street lights show a pure market may under-provide?", "很难向每个使用者收费，一人使用不妨碍别人", "公共品。", "A public good.", ["很难收费", "hard to charge", "public good"], 3),
],
"g9ec-7": [
    M("basic", "只有本品价格下降时，需求会？", "If only this good’s price falls, demand:", "a", "沿曲线延伸。", "Extends along the curve.", [("沿曲线延伸", "extends along the curve"), ("整条曲线向左", "the curve shifts left"), ("供给一定向左", "supply must shift left"), ("变成自由物品", "becomes a free good")]),
    S("exam", "说出两个使需求曲线平移的因素。", "Name two factors that shift demand.", "收入和偏好", "还有相关价格、人口、广告。", "Also related prices, population, advertising.", ["收入和偏好", "income and tastes", "收入和人口"], 2),
    M("unit", "单元：巴士票价上升后更多人骑车。对自行车来说巴士是？", "Unit: dearer bus fares, more cycling. Buses are, for bicycles:", "b", "替代品。", "A substitute.", [("互补品所以需求下降", "a complement, so demand falls"), ("替代品，需求增加", "a substitute, so demand rises"), ("自由物品", "a free good"), ("宏观总量", "a macro total")]),
],
"g9ec-8": [
    M("basic", "技术改进使供给？", "Better technology shifts supply:", "c", "向右。", "Right.", [("一定向左", "certainly left"), ("不动", "not at all"), ("向右", "right"), ("变成需求", "into demand")]),
    S("exam", "间接税通常使供给曲线？", "An indirect tax usually makes supply:", "向左移动", "成本上升。", "Costs rise.", ["向左移动", "shift left", "decreases supply"], 2),
    S("unit", "单元：面粉涨价为什么是供给平移而不是沿曲线移动？", "Unit: why is dearer flour a shift of bread supply, not a movement?", "变的是成本，不是面包自己的售价", "自己的价格才沿曲线走。", "Only the good’s own price moves you along the curve.", ["变的是成本", "the cost changed", "not the selling price"], 3),
],
"g9ec-9": [
    M("basic", "价格低于均衡时最可能？", "When price is below equilibrium:", "b", "短缺，价格上升。", "Shortage, price rises.", [("剩余且价格上升", "surplus and price rises"), ("短缺，价格上升", "shortage and price rises"), ("供给向左", "supply shifts left"), ("需求消失", "demand disappears")]),
    S("exam", "需求增加、供给不变，均衡价格？", "Demand increases, supply unchanged. Equilibrium price?", "上升", "同时数量也上升。", "Quantity rises too.", ["上升", "rises", "increases"], 1),
    S("challenge", "需求和供给同时向右，哪一个一定上升？", "If demand and supply both shift right, what must rise?", "均衡数量", "价格不一定。", "Price may not.", ["均衡数量", "equilibrium quantity", "quantity"], 2),
    write("unit", "单元 8 分练习：讨论价格机制是否总能把资源用到最需要的地方。要有因果链和相反论点。", "Unit 8-mark practice: discuss whether the price mechanism always sends resources where they are most needed.", "见解析。", "价格传递购买意愿，但付得起不等于最需要，公共品也会供给不足。", "Prices transmit willingness to pay, but ability to pay is not need, and public goods may be under-provided.", ["price", "profit", "income", "public", "价格", "利润"], 3, 8),
],
"g9ph-1": [
    N("basic", "尺子下落 0.20 m，g=9.8。反应时间约多少秒？保留两位小数。", "A ruler falls 0.20 m, g=9.8. Reaction time to 2 d.p.?", "0.20", "约 0.20 s。", "About 0.20 s.", 2, 0.02),
    S("exam", "求梯度时三角形应当怎样取？", "How should the triangle for a gradient be taken?", "尽量大", "减小读数误差。", "To reduce reading error.", ["尽量大", "as large as possible", "large triangle"], 1),
    S("unit", "测量单元：为什么量筒要平视弯月面？", "Measurement unit: why read the meniscus at eye level?", "避免视差", "视线偏高或偏低都会读错。", "To avoid parallax.", ["视差", "parallax", "eye level"], 2),
],
"g9ph-2": [
    N("basic", "从静止以 3 m/s² 加速 4 s，末速度？", "From rest at 3 m/s² for 4 s. Final speed?", "12", "v=at=12。", "v=at=12.", 1, 0),
    N("exam", "上题位移是多少 m？", "Displacement in that motion, in m?", "24", "s=½×4×12=24。", "s=½×4×12=24.", 2, 0),
    M("unit", "运动单元：v–t 图的水平直线（不在零上）表示？", "Motion unit: a horizontal v–t line not on zero means:", "c", "匀速。", "Constant velocity.", [("静止", "rest"), ("匀加速", "constant acceleration"), ("匀速", "constant velocity"), ("位移为零", "zero displacement")]),
],
"g9ph-3": [
    N("basic", "自由下落 1 s，g=9.8，大约下落多少 m？", "Free fall for 1 s, g=9.8. Distance in m?", "4.9", "½gt²=4.9。", "½gt²=4.9.", 1, 0.1),
    M("exam", "真空中铁球和羽毛同时释放，结果是？", "In a vacuum a ball and a feather are released together.", "a", "同时落地。", "They land together.", [("同时落地", "they land together"), ("铁球一定先到", "the ball must arrive first"), ("羽毛加速度更大", "the feather accelerates more"), ("加速度都是 0", "both have zero acceleration")]),
    S("unit", "运动单元：最高点加速度为什么不是 0？", "Motion unit: why is acceleration not 0 at the highest point?", "速度为 0，但重力仍在，加速度仍约为 g 向下", "加速度不是速度。", "Acceleration is not speed.", ["仍约为 g", "still about g", "gravity still acts"], 2),
],
"g9ph-4": [
    N("basic", "质量 40 kg，g=9.8。重量多少 N？", "Mass 40 kg, g=9.8. Weight in N?", "392", "40×9.8。", "40×9.8.", 1, 0),
    N("exam", "质量 96 g，排水体积 40 cm³。密度 g/cm³？", "Mass 96 g, displaced volume 40 cm³. Density?", "2.4", "96/40=2.4。", "96/40=2.4.", 2, 0.01),
    S("unit", "密度单元：不规则固体的体积为什么要用两个水位的差？", "Density unit: why is the volume of an irregular solid a difference of two levels?", "最终水位包含原来的水", "物体体积是上升的那一部分。", "The final level includes the original water.", ["包含原来的水", "includes the original water", "V2-V1"], 2),
],
"g9ph-5": [
    N("basic", "力 4 N，伸长 0.08 m。k 是多少 N/m？", "Force 4 N, extension 0.08 m. k in N/m?", "50", "4/0.08=50。", "4/0.08=50.", 2, 0),
    S("exam", "伸长等于哪两个长度之差？", "Extension is the difference of which two lengths?", "加载后的长度减原长", "不是总长度本身。", "Not the total length.", ["加载后减原长", "loaded length minus original", "new minus original"], 1),
    M("unit", "力单元：超过弹性限度后撤力，弹簧将？", "Forces unit: after the elastic limit, removing the force means the spring:", "d", "不能回到原长。", "Does not return.", [("一定更短且仍服从胡克定律", "must be shorter and still obey Hooke"), ("梯度变成质量", "gradient becomes mass"), ("一定回到原长", "must return"), ("不能回到原长", "does not return")]),
],
"g9ph-6": [
    N("basic", "合力 12 N，质量 3 kg。加速度？", "Resultant 12 N, mass 3 kg. Acceleration?", "4", "12/3=4。", "12/3=4.", 1, 0),
    N("exam", "向右 15 N，摩擦 6 N。合力？", "15 N right, friction 6 N. Resultant?", "9", "15-6=9。", "15-6=9.", 1, 0),
    S("unit", "力单元：受力图为什么不能画物体施加给别人的力？", "Forces unit: why not draw the forces the object exerts on other things?", "受力图只研究这一个物体受到的力", "否则合力会算错。", "Otherwise the resultant is wrong.", ["只画受到的力", "only forces on the object"], 2),
],
"g9ph-7": [
    M("basic", "终端速度时空气阻力与重量？", "At terminal velocity, air resistance and weight are:", "a", "大小相等。", "Equal.", [("大小相等", "equal"), ("阻力一定更大", "resistance must be larger"), ("重量变为 0", "weight is zero"), ("两者都是 0", "both are zero")]),
    S("exam", "刚释放时加速度大约等于什么？", "Just after release, acceleration is about:", "g", "阻力几乎为零。", "Resistance is almost zero.", ["g", "9.8", "9.8 m/s^2"], 1),
    M("unit", "力单元：降落伞打开且阻力突然大于重量时，人将？", "Forces unit: parachute opens and resistance exceeds weight. The person:", "c", "减速直到较小的新终端速度。", "Slows to a smaller terminal velocity.", [("立刻更快", "immediately faster"), ("加速度变为 g 且速度不变", "acceleration g and speed unchanged"), ("减速直到较小的新终端速度", "slows to a smaller new terminal velocity"), ("质量变为 0", "mass becomes zero")]),
],
"g9ch-1-1": [
    M("basic", "气体最容易被压缩，主要因为？", "A gas is easiest to compress mainly because:", "b", "粒子之间空隙大。", "Large gaps.", [("粒子不运动", "particles do not move"), ("空隙大", "large gaps"), ("比固体更规则", "more regular than a solid"), ("没有能量", "no energy")]),
    S("exam", "加热曲线的水平段表示什么？", "A flat section on a heating curve shows:", "状态变化", "温度不变仍在吸热。", "Change of state.", ["状态变化", "a change of state", "熔化或沸腾"], 1),
    S("unit", "物态单元：为什么熔化时温度不变不能说没有吸热？", "States unit: why does a constant temperature during melting not mean no heat is absorbed?", "能量用来克服粒子间作用力", "温度和能量不是同一件事。", "Energy overcomes forces.", ["克服作用力", "overcomes forces", "energy is still absorbed"], 2),
],
"g9ch-1-2": [
    M("basic", "氨与氯化氢的白烟更靠近？", "The white ring forms nearer:", "c", "氯化氢一端。", "The HCl end.", [("氨一端因为氨更重", "ammonia, because it is heavier"), ("永远在正中", "always the middle"), ("氯化氢一端", "the HCl end"), ("管外", "outside the tube")]),
    N("exam", "扩散较慢的气体，相对分子质量更接近 17 还是 36.5？填数字。", "The slower gas has Mr closer to 17 or 36.5? Enter the number.", "36.5", "更重更慢。", "Heavier is slower.", 1, 0),
    S("unit", "物态单元：为什么不能说只有氨在动？", "States unit: why not say only ammonia is moving?", "两边都在扩散，只是速率不同", "白烟是相遇点。", "Both diffuse; the rates differ.", ["两边都在扩散", "both diffuse", "rates differ"], 2),
],
"g9ch-12-1": [
    S("basic", "你改变的量叫什么变量？", "The variable you change is called:", "independent", "自变量。", "Independent.", ["independent", "自变量", "independent variable"], 1),
    M("exam", "从食盐水得到晶体，应？", "To get crystals from salt solution:", "c", "蒸发。", "Evaporate.", [("只用过滤", "filtration only"), ("层析", "chromatography"), ("蒸发", "evaporation"), ("扩散管", "a diffusion tube")]),
    S("unit", "实验单元：比较温度对溶解的影响时，固体质量应当？", "Techniques unit: when comparing temperature and dissolving, the mass of solid should be:", "保持不变", "它是控制变量。", "It is a control.", ["保持不变", "kept the same", "constant"], 1),
],
"g9ch-12-2": [
    N("basic", "斑点 2 cm，前沿 8 cm。Rf？", "Spot 2 cm, front 8 cm. Rf?", "0.25", "2/8=0.25。", "2/8=0.25.", 1, 0.01),
    M("exam", "两种沸点不同的互溶液体，用？", "Two miscible liquids with different boiling points:", "d", "分馏。", "Fractional distillation.", [("过滤", "filtration"), ("磁铁", "a magnet"), ("无溶剂层析", "chromatography with no solvent"), ("分馏", "fractional distillation")]),
    S("unit", "分离单元：层析基线为什么用铅笔？", "Separation unit: why pencil for the baseline?", "钢笔墨水会溶解并上升", "会和样品混在一起。", "Ink would travel.", ["墨水会上升", "ink would move", "pencil is insoluble"], 1),
],
"g9ch-2-1": [
    S("basic", "铝的质子数是 13。电子排布？", "Aluminium, proton number 13. Configuration?", "2,8,3", "2+8+3=13。", "2+8+3=13.", ["2,8,3", "2.8.3"], 1),
    M("exam", "决定元素种类的是？", "The element is decided by:", "a", "质子数。", "Proton number.", [("质子数", "proton number"), ("中子数", "neutron number"), ("熔点", "melting point"), ("颜色", "colour")]),
    S("unit", "Topic 2 单元：同一族元素化学性质相似，是因为什么相同？", "Topic 2 unit: elements in the same group are chemically similar because what is the same?", "最外层电子数", "不是质量数。", "The number of outer electrons.", ["最外层电子数", "outer electrons", "valence electrons"], 2),
],
"g9ch-2-2": [
    N("basic", "50% 质量数 10 与 50% 质量数 12。Ar？", "50% mass 10 and 50% mass 12. Ar?", "11", "(500+600)/100=11。", "(500+600)/100=11.", 2, 0),
    S("exam", "同位素之间相同的是质子数还是中子数？", "Isotopes share proton number or neutron number?", "质子数", "中子数不同。", "Neutron numbers differ.", ["质子数", "proton number"], 1),
    N("unit", "Topic 2 单元：氯 75% 为 35，25% 为 37。Ar？", "Topic 2 unit: chlorine 75% 35 and 25% 37. Ar?", "35.5", "35.5。", "35.5.", 2, 0),
],
"g9ch-2-3": [
    S("basic", "Na+ 的电子排布，由 2,8,1 变成？", "Na+ from 2,8,1 becomes:", "2,8", "失去一个电子。", "Loses one electron.", ["2,8"], 1),
    S("exam", "Ca2+ 与 Cl- 的化学式？", "Formula of Ca2+ with Cl-?", "CaCl2", "一个 +2 需要两个 -1。", "One +2 needs two -1.", ["CaCl2", "CaCl₂"], 2),
    M("unit", "Topic 2 单元：固态氯化钠不导电，因为？", "Topic 2 unit: solid NaCl does not conduct because:", "b", "离子不能自由移动。", "Ions cannot move.", [("没有带电粒子", "no charged particles"), ("离子不能移动", "ions cannot move"), ("它是简单分子", "it is simple molecular"), ("电子像石墨一样离域", "electrons are delocalised as in graphite")]),
],
"g9ch-2-4": [
    S("basic", "共价键是什么样的电子对？", "A covalent bond is what kind of pair?", "共享电子对", "通常在非金属之间。", "Usually between non-metals.", ["共享电子对", "a shared pair", "shared pair"], 1),
    M("exam", "简单分子熔点低，主要因为？", "Simple molecules have low melting points mainly because:", "a", "分子间力弱。", "Weak forces between molecules.", [("分子间力弱", "weak intermolecular forces"), ("共价键很弱", "covalent bonds are weak"), ("它们是金属", "they are metals"), ("离子自由移动", "ions move freely")]),
    S("unit", "Topic 2 单元：熔化水时破坏的是什么，不是什么？", "Topic 2 unit: melting water overcomes what, and not what?", "破坏分子间力，不是把 H-O 共价键扯断", "内部的键仍然很强。", "The bonds inside stay strong.", ["分子间力", "intermolecular forces", "not the covalent bonds"], 3),
],
"g9ch-2-5": [
    M("basic", "固体金属导电是由于？", "A solid metal conducts because of:", "c", "可移动的离域电子。", "Mobile delocalised electrons.", [("正离子离开晶格", "ions leaving the lattice"), ("分子间力", "intermolecular forces"), ("离域电子", "delocalised electrons"), ("中子", "neutrons")]),
    S("exam", "金刚石熔点高，是因为熔化必须克服什么？", "Diamond’s high melting point: melting must overcome what?", "许多强共价键", "巨型共价。", "Many strong covalent bonds.", ["许多强共价键", "many strong covalent bonds"], 2),
    M("unit", "Topic 2 单元：既软又能导电的固体是？", "Topic 2 unit: which solid is both soft and able to conduct?", "b", "石墨。", "Graphite.", [("金刚石", "diamond"), ("石墨", "graphite"), ("氯化钠晶体", "sodium chloride"), ("干冰", "dry ice")]),
],
"g9ch-3-1": [
    N("basic", "H2O 的 Mr，H=1，O=16。", "Mr of H2O, H=1, O=16.", "18", "1+1+16。", "1+1+16.", 1, 0),
    N("exam", "CO2 的 Mr，C=12，O=16。", "Mr of CO2.", "44", "12+32。", "12+32.", 1, 0),
    N("challenge", "Na2O 的 Mr，Na=23，O=16。", "Mr of Na2O.", "62", "46+16。", "46+16.", 2, 0),
    N("unit", "计量单元：CaCO3 的 Mr，Ca=40，C=12，O=16。", "Stoichiometry unit: Mr of CaCO3.", "100", "40+12+48。", "40+12+48.", 2, 0),
    S("unit", "计量单元：为什么这一节先不要把克换算成摩尔？", "Stoichiometry unit: why not convert grams to moles yet?", "摩尔是下一步，这一节是化学式和相对质量", "先把 Mr 算稳。", "The mole comes next.", ["摩尔是下一步", "the mole is next", "relative mass first"], 2),
],
"g9bi-2-1": [
    N("basic", "图像 15 mm，实际 0.03 mm。放大倍数？", "Image 15 mm, actual 0.03 mm. Magnification?", "500", "15/0.03=500。", "15/0.03=500.", 2, 0),
    M("exam", "根细胞通常没有？", "A root cell usually lacks:", "c", "叶绿体。", "Chloroplasts.", [("细胞壁", "a cell wall"), ("细胞核", "a nucleus"), ("叶绿体", "chloroplasts"), ("细胞膜", "a membrane")]),
    S("unit", "细胞单元：为什么毫米和微米不能直接相除求放大倍数？", "Cells unit: why not divide millimetres by micrometres for magnification?", "单位必须相同", "先换算。", "The units must match.", ["单位必须相同", "units must match", "convert first"], 2),
],
"g9bi-3-1": [
    M("basic", "渗透特指哪种物质通过部分透膜？", "Osmosis names which substance through a partially permeable membrane?", "a", "水。", "Water.", [("水", "water"), ("淀粉", "starch"), ("蛋白质", "protein"), ("任何溶质且不需要膜", "any solute and no membrane")]),
    N("exam", "初质量 8.0 g，末质量 7.2 g。百分变化？用负数。", "Start 8.0 g, end 7.2 g. Percentage change, negative if a loss.", "-10", "(7.2-8)/8×100=-10。", "(7.2-8)/8×100=-10.", 2, 0),
    S("unit", "渗透单元：计划里至少要保持不变的两个量，写出一个。", "Osmosis unit: name one variable that must stay constant.", "温度", "还有时间、大小、体积。", "Also time, size, volume.", ["温度", "temperature", "时间", "time", "体积"], 1),
],
"g9bi-4-1": [
    M("basic", "碘液变蓝黑说明有？", "Iodine turning blue-black shows:", "b", "淀粉。", "Starch.", [("还原糖", "reducing sugar"), ("淀粉", "starch"), ("蛋白质", "protein"), ("脂肪", "fat")]),
    S("exam", "检验还原糖除了试剂还必须？", "Besides the reagent, a reducing-sugar test also needs:", "加热", "本尼迪特要加热。", "Heat Benedict’s.", ["加热", "heat"], 1),
    S("unit", "分子单元：为什么砖红色不能写成精确的克数？", "Molecules unit: why is brick-red not an exact mass in grams?", "它只是半定量的颜色", "要比对照。", "It is only semi-quantitative.", ["半定量", "semi-quantitative", "not an exact mass"], 2),
],
"g9bi-5-1": [
    M("basic", "酶在过高温度下失去活性，主要因为？", "An enzyme loses activity at too high a temperature mainly because:", "b", "活性部位变形。", "The active site changes shape.", [("底物都变成氧", "all substrate became oxygen"), ("活性部位变形", "the active site changes shape"), ("变成淀粉", "it becomes starch"), ("pH 一定变成 7", "pH must become 7")]),
    S("exam", "过氧化氢酶的底物是？", "Substrate of catalase?", "过氧化氢", "产物是水和氧。", "Products are water and oxygen.", ["过氧化氢", "hydrogen peroxide", "H2O2"], 1),
    S("unit", "酶单元：低温和变性有什么不同？", "Enzymes unit: how is a low temperature different from denaturation?", "低温只是变慢，升温可恢复；变性通常不能恢复", "形状没有在低温下被破坏。", "The shape is not destroyed by cold.", ["可以恢复", "can recover", "not denatured"], 2),
],
"g9bi-1-1": [
    M("basic", "没有真正细胞核的是？", "Which has no true nucleus?", "d", "细菌。", "Bacteria.", [("植物", "plants"), ("真菌", "fungi"), ("原生生物", "protoctists"), ("细菌", "bacteria")]),
    S("exam", "鸟类体表最明显的特征？", "The body covering that most clearly marks birds?", "羽毛", "不是“会飞”。", "Not “it flies”.", ["羽毛", "feathers"], 1),
    S("unit", "分类单元：为什么会飞不足以把蝙蝠分成鸟？", "Classification unit: why is flight not enough to call a bat a bird?", "蝙蝠有毛和乳汁，是哺乳类", "要看皮肤和生殖。", "Look at skin and reproduction.", ["哺乳类", "mammal", "fur and milk"], 2),
],
"g9bi-7-1": [
    M("basic", "缺铁更可能导致？", "Lack of iron is more likely to cause:", "b", "贫血。", "Anaemia.", [("坏血病", "scurvy"), ("贫血", "anaemia"), ("只改变头发颜色的遗传病", "a genetic hair-colour condition"), ("质壁分离", "plasmolysis")]),
    S("exam", "吸收的主要部位？", "Main site of absorption?", "小肠", "不是大肠。", "Not the large intestine.", ["小肠", "small intestine"], 1),
    M("unit", "营养单元：维生素 D 缺乏最直接关联？", "Nutrition unit: lack of vitamin D is most directly linked to:", "a", "佝偻病。", "Rickets.", [("佝偻病", "rickets"), ("坏血病", "scurvy"), ("碘液不变色", "iodine staying yellow"), ("酶在低温变性", "enzymes denaturing in the cold")]),
],
"g9bi-7-2": [
    M("basic", "胆汁的作用是？", "Bile:", "c", "乳化脂肪，它不是酶。", "Emulsifies fat. It is not an enzyme.", [("把淀粉变成麦芽糖", "turns starch into maltose"), ("作为蛋白酶", "acts as a protease"), ("乳化脂肪", "emulsifies fat"), ("在大肠吸收葡萄糖", "absorbs glucose in the large intestine")]),
    S("exam", "脂肪酶的两种产物？", "Two products of lipase?", "脂肪酸和甘油", "不是氨基酸。", "Not amino acids.", ["脂肪酸和甘油", "fatty acids and glycerol"], 2),
    S("unit", "消化单元：绒毛壁只有一层细胞，对吸收有什么好处？", "Digestion unit: the villus wall is one cell thick. What is the advantage?", "扩散距离短", "适应要写作用。", "A short diffusion distance.", ["扩散距离短", "short diffusion distance"], 2),
],
}
