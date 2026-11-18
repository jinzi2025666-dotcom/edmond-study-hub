"""Grade 9 Computer Science — IGCSE 0478-style, CA1.2 coverage.

Included: program life cycle, flowcharts, pseudocode against Python,
totalling, counting, minimum, maximum and average, validation, verification,
test data, trace tables, writing algorithms, sub-routines, and 1D arrays.
Linear search, bubble sort and 2D arrays are outside this paper.
"""
from __future__ import annotations


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


def num(zh, en, answer, ez, ee, marks=1, tolerance=0, accepted=None):
    q = dict(type="numeric", stem_zh=zh, stem_en=en, answer=str(answer), exp_zh=ez, exp_en=ee, marks=marks, tolerance=tolerance)
    if accepted:
        q["accepted"] = accepted
    return q


def write(qid, zh, en, answer, ez, ee, keywords, keyword_min, marks):
    return dict(type="structured", id=qid, stem_zh=zh, stem_en=en, answer=answer, exp_zh=ez, exp_en=ee, keywords=keywords, keyword_min=keyword_min, marks=marks)


SPEC = {
    "subject_id": "computer-science",
    "tag": "g9cs",
    "chapters": [
        {
            "id": "g9-cs-7",
            "code": "7",
            "order": 1,
            "title_zh": "第 7 章 · 算法设计与问题求解",
            "title_en": "Chapter 7 · Algorithm design and problem-solving",
            "note_zh": "本阶段范围是 7.1–7.3、7.4 里的求和、计数、最小、最大与平均，以及 7.5–7.9。查找和排序不在这份练习卷里。",
            "note_en": "This stage covers 7.1–7.3, the total, count, minimum, maximum and average parts of 7.4, and 7.5–7.9. Searching and sorting are not on this paper.",
            "practice_minutes": 25,
            "units": [
                {
                    "id": "g9-cs-7-u1",
                    "code": "7.1–7.3",
                    "order": 1,
                    "title_zh": "生命周期、流程图与伪代码",
                    "title_en": "Life cycle, flowcharts and pseudocode",
                    "lessons": [
                        L(
                            "g9cs-7-1", "7.1",
                            "程序开发的生命周期",
                            "The program development life cycle",
                            "能按分析、设计、编码、测试说明一个问题如何被拆开并变成可运行的程序。",
                            "Describe how a problem is broken down and turned into a working program through analysis, design, coding and testing.",
                            [
                                ("分析：弄清输入、输出和限制，并把大问题拆成子问题。这就是分解。", "Analysis: identify inputs, outputs and limits, and split the problem into sub-problems. That split is decomposition."),
                                ("设计：选择结构，画结构图或流程图，或先写伪代码。", "Design: choose the structure, and draw a structure diagram or flowchart, or write pseudocode first."),
                                ("编码：把设计翻译成 Python 等语言。翻译错误会变成语法错误。", "Coding: translate the design into a language such as Python. A translation error becomes a syntax error."),
                                ("测试：用正常、边界和异常数据检查逻辑，而不是只运行一次。", "Testing: use normal, boundary and abnormal data. One successful run is not a test."),
                            ],
                            "四个阶段会来回走。测试发现逻辑错误，往往要回到设计，而不是在末尾再写一行碰运气。结构图从上到下：整个任务在顶上，子任务在下面。例如“统计一次小测”可以拆成输入每一分、累加、计数、最后求平均。\n\n考试若问某个活动属于哪一阶段，先看它在产生代码之前还是之后。画流程图是设计；改掉一个写错的冒号是编码；准备一个刚好等于上限的数据是测试。",
                            "The four stages loop. A logic error found in testing usually sends you back to design, not to one extra hopeful line at the end. A structure diagram is top-down: the whole task on top, sub-tasks underneath. “Process a short test” might split into input each mark, total, count, then average.\n\nIf a question asks which stage an activity belongs to, ask whether it happens before there is code. Drawing a flowchart is design. Fixing a mistyped colon is coding. Preparing a value exactly on the upper limit is testing.",
                            "“把‘找最高分’再分成：先假定第一个是最高，再逐个比较。”这是哪一阶段的工作？\n\n**解：** 分析里的分解，也可以视为设计的开始。它还没有写具体的 Python。",
                            "“Split ‘find the highest mark’ into: assume the first is the highest, then compare one by one.” Which stage is that?\n\n**Solution:** Decomposition in analysis, or the start of design. It is not Python yet.",
                            [
                                ("把测试理解成“能运行就结束”。", "Treating testing as “it ran, so it is finished”."),
                                ("还没弄清输入输出就开始写代码。", "Writing code before the inputs and outputs are clear."),
                            ],
                            [
                                mcq("画出流程图通常属于？", "Drawing a flowchart usually belongs to:", "b", "设计。", "Design.", [("分析完成后就不再发生的测试", "testing, which never follows analysis"), ("设计", "design"), ("只在程序出售之后", "only after the program is sold"), ("给计算机装系统", "installing an operating system")]),
                                short("把大问题拆成子问题叫什么？", "What is the splitting of a large problem into sub-problems called?", "decomposition", "分解。", "Decomposition.", ["decomposition", "分解", "decompose"], 2),
                                mcq("发现公式写错、结果始终差一截，最应回到哪一阶段检查？", "A formula is wrong and every result is off. Which stage should you return to first?", "a", "设计（算法），而不只是多运行一次。", "Design — the algorithm — not another run of the same code.", [("设计中的算法", "the algorithm in the design"), ("只更换显示器", "only changing the monitor"), ("不再输入任何数据", "refusing all input"), ("把变量名改得更长", "making variable names longer")]),
                            ],
                        ),
                        L(
                            "g9cs-7-2", "7.2",
                            "流程图",
                            "Flowcharts",
                            "能认出起止、输入输出、处理和判断四种符号，并顺着箭头读出分支。",
                            "Recognise terminator, input/output, process and decision symbols, and follow the arrows through a branch.",
                            [
                                ("椭圆或圆角矩形表示开始和结束。", "An oval or rounded rectangle is start or stop."),
                                ("平行四边形表示输入或输出。", "A parallelogram is input or output."),
                                ("矩形表示过程，例如 total ← total + mark。", "A rectangle is a process, for example total ← total + mark."),
                                ("菱形表示判断，必须有两个出口，通常标 YES 和 NO。", "A diamond is a decision and needs two exits, usually labelled YES and NO."),
                            ],
                            "读流程图时用手指沿箭头走，不要跳着看文字。判断框的两个出口都要能回到某处或到达结束，否则算法会断掉。循环就是一个判断把箭头送回前面的过程框。\n\n流程图适合看结构，不适合写很长的算式。复杂的平均分算法用伪代码更清楚；流程图用来确认“先输入，再判断，再累加”的顺序。",
                            "Follow the arrows with a finger. Do not jump between labels. Both exits of a decision must lead somewhere, or the algorithm breaks. A loop is a decision whose arrow returns to an earlier process.\n\nA flowchart is good for structure and poor for a long formula. Pseudocode is clearer for an average. The chart is there to check the order: input, then decide, then add.",
                            "“如果分数大于最高分，就更新最高分。”这应画成什么符号？\n\n**解：** 一个菱形（分数是否大于最高分），YES 的一边接一个矩形（最高分 ← 分数）。NO 的一边跳过那个矩形。",
                            "“If the mark is greater than the highest, update the highest.” Which symbols?\n\n**Solution:** A diamond (is the mark greater?), with YES leading to a rectangle (highest ← mark). NO skips that rectangle.",
                            [
                                ("判断框只画一个出口。", "A decision with only one exit."),
                                ("把输入画成矩形，把计算画成平行四边形。", "Drawing input as a rectangle and a calculation as a parallelogram."),
                            ],
                            [
                                mcq("流程图中的菱形表示？", "A diamond in a flowchart means:", "c", "判断。", "A decision.", [("开始", "start"), ("输入", "input"), ("判断", "a decision"), ("一条必须执行的赋值", "an assignment that must always run")]),
                                mcq("total ← total + mark 应放在？", "total ← total + mark belongs in:", "a", "矩形的过程框。", "A process rectangle.", [("矩形", "a rectangle"), ("菱形的两个出口上同时写", "both exits of a diamond at once"), ("表示开始的椭圆里", "the start oval"), ("箭头本身", "the arrow itself")]),
                                short("判断框通常要有几个出口？", "How many exits does a decision usually have?", "2", "YES 和 NO。", "YES and NO.", ["2", "two", "两个"], 1),
                            ],
                        ),
                        L(
                            "g9cs-7-3", "7.3",
                            "伪代码与 Python",
                            "Pseudocode and Python",
                            "能把课堂使用的伪代码写成对应的 Python，并说出两种写法容易混的地方。",
                            "Turn the class pseudocode into Python, and name the places where the two notations are easy to mix up.",
                            [
                                ("赋值：伪代码用 ←，Python 用 =。比较相等时 Python 用 ==。", "Assignment: pseudocode uses ←, Python uses =. Python uses == to compare."),
                                ("选择：IF … THEN … ELSE … ENDIF。Python 用缩进和冒号，没有 ENDIF。", "Selection: IF … THEN … ELSE … ENDIF. Python uses a colon and indentation, and has no ENDIF."),
                                ("循环：FOR i ← 1 TO n … NEXT i。Python 的 range(1, n+1) 才包含 n。", "Iteration: FOR i ← 1 TO n … NEXT i. Python’s range(1, n+1) is what includes n."),
                                ("输入输出：INPUT / OUTPUT 对应 input() / print()。input() 得到的是字符串，要算数先转换。", "INPUT / OUTPUT correspond to input() / print(). input() returns a string; convert it before arithmetic."),
                            ],
                            "伪代码是给人读的设计，不是某一种编译器的方言。考试卷按课程里的伪代码指南书写：关键词大写，赋值用左箭头。Python 是你们在编辑器里真正运行的那种。两边描述同一个算法，记号不同。\n\n最常见的丢分是 FOR 的终点。伪代码 `FOR i ← 1 TO 3` 会取 1、2、3。Python `range(1, 3)` 只取 1、2。要三个数就写 `range(1, 4)`。另一个常见错误是把 INPUT 得到的文字 7 直接相加，结果变成字符串拼接。",
                            "Pseudocode is a design for a reader, not one compiler’s dialect. On paper, follow the class guide: keywords in capitals, assignment with a left arrow. Python is what you actually run. Both can describe the same algorithm.\n\nThe usual lost mark is the end of FOR. `FOR i ← 1 TO 3` takes 1, 2 and 3. Python `range(1, 3)` takes 1 and 2. Three values need `range(1, 4)`. The other usual error is adding the string `\"7\"` from input(), which concatenates instead of adding.",
                            "伪代码：\n\n```\nINPUT mark\ntotal ← total + mark\n```\n\n若 mark 以 Python 的 input() 读入，正确的加法是 `total = total + int(mark)`，而不是 `total = total + mark`。",
                            "Pseudocode:\n\n```\nINPUT mark\ntotal ← total + mark\n```\n\nIf mark is read with Python’s input(), the addition is `total = total + int(mark)`, not `total = total + mark`.",
                            [
                                ("Python 里用 ← 赋值。", "Using ← for assignment in Python."),
                                ("range(1, n) 被当成包含 n。", "Treating range(1, n) as if it included n."),
                                ("忘记 ENDIF / NEXT 与缩进是两种写法，不要混在同一段答案里。", "Mixing ENDIF / NEXT with indentation in the same answer."),
                            ],
                            [
                                short("伪代码的赋值符号是什么？", "What symbol does pseudocode use for assignment?", "←", "左箭头，不是等号。", "A left arrow, not an equals sign.", ["←", "<-", "left arrow"], 1),
                                short("Python 中要得到 1、2、3，range 应怎样写？", "Which range call in Python produces 1, 2 and 3?", "range(1, 4)", "右端不包含。", "The right-hand end is excluded.", ["range(1, 4)", "range(1,4)"], 2),
                                mcq("INPUT 进 Python 后，做加法前通常要？", "After INPUT in Python, before you add, you usually need to:", "d", "把字符串转换成整数或小数。", "Convert the string to an integer or a float.", [("什么都不用做", "do nothing"), ("改成流程图", "turn it into a flowchart"), ("乘以 0", "multiply by 0"), ("转换成 int 或 float", "convert it to int or float")]),
                            ],
                        ),
                    ],
                },
                {
                    "id": "g9-cs-7-u2",
                    "code": "7.4–7.9",
                    "order": 2,
                    "title_zh": "求和、检验、追踪与写算法",
                    "title_en": "Totals, checks, traces and writing algorithms",
                    "lessons": [
                        L(
                            "g9cs-7-4", "7.4.1–7.4.3",
                            "求和、计数、最小、最大与平均",
                            "Totalling, counting, minimum, maximum and average",
                            "会写出并手工执行这五种标准处理。本阶段练习不包括线性查找和冒泡排序。",
                            "Write and hand-trace these five standard processes. Linear search and bubble sort are not part of this stage.",
                            [
                                ("求和：total ← 0，然后 total ← total + 每一个值。", "Totalling: total ← 0, then total ← total + each value."),
                                ("计数：count ← 0，只在条件成立时 count ← count + 1。", "Counting: count ← 0, and count ← count + 1 only when the condition is true."),
                                ("最大：先把第一个值赋给 max，后面只在遇到更大的值时更新。最小同理用更小。", "Maximum: set max to the first value, then update only when a later value is greater. Minimum uses less than."),
                                ("平均 = total / count。count 为 0 时不能除。", "Average = total / count. Do not divide when count is 0."),
                            ],
                            "这五个算法都是一遍扫描。它们不需要把每个数存下来，除非后面还要再用这些数——那是数组那一节的理由。初值一定要在循环外面。把 total ← 0 放进循环，总和会被反复清零。\n\n最大和最小不要从 0 开始，除非你能保证所有数都是正的或都是负的。用第一个数据作初值，对正数和负数都安全。平均要用实际计数，不能用循环的上限代替，因为有些输入可能被条件跳过。",
                            "All five are one-pass scans. They do not store every value unless you need the values again later — that is the reason for an array. Initialise outside the loop. If total ← 0 sits inside the loop, the total is wiped on every pass.\n\nDo not start maximum or minimum at 0 unless you know every value is positive, or every value is negative. The first value is safe for both. An average uses the real count, not the upper bound of the loop, because some inputs may have been skipped.",
                            "数据 4、7、1、9。\n\n总和 $4+7+1+9 = 21$。大于 5 的计数是 2（7 和 9）。最大是 9，最小是 1。若这四个都计入，平均是 $21/4 = 5.25$。",
                            "Data: 4, 7, 1, 9.\n\nThe total is $4+7+1+9 = 21$. The count of values greater than 5 is 2 (7 and 9). The maximum is 9 and the minimum is 1. If all four count, the average is $21/4 = 5.25$.",
                            [
                                ("计数器在条件不成立时也加 1。", "Adding 1 to the counter when the condition is false."),
                                ("最大值初值设为 0，而数据里全是负数。", "Starting the maximum at 0 when every value is negative."),
                                ("总数除以循环次数，而不是除以真正计入的个数。", "Dividing the total by the number of loops instead of by the number actually counted."),
                            ],
                            [
                                num("从 4、7、1、9 求和。总和是多少？", "Total the values 4, 7, 1 and 9. What is the total?", "21", "$4+7+1+9 = 21$。", "$4+7+1+9 = 21$.", 1, 0),
                                num("其中大于 5 的数有几个？", "How many of those values are greater than 5?", "2", "7 和 9。", "7 and 9.", 1, 0),
                                num("这四个数的平均数是多少？", "What is the average of the four values?", "5.25", "$21/4 = 5.25$。", "$21/4 = 5.25$.", 2, 0.01, ["5.25", "21/4"]),
                            ],
                        ),
                        L(
                            "g9cs-7-5", "7.5–7.7",
                            "验证、校验与测试数据",
                            "Validation, verification and test data",
                            "能区分验证与校验，并能为一条例规则举出正常、边界和异常数据。",
                            "Tell validation from verification, and give normal, boundary and abnormal data for one rule.",
                            [
                                ("验证（validation）检查数据是否合理：范围、类型、长度、是否存在、格式。", "Validation checks whether data is reasonable: range, type, length, presence, format."),
                                ("校验（verification）检查数据是否按原样录入：两次输入，或肉眼核对。", "Verification checks whether data was transcribed as intended: double entry, or a visual check."),
                                ("合理的数据仍可能是录错的。两者回答的不是同一个问题。", "Reasonable data can still be the wrong data. The two checks answer different questions."),
                                ("测试数据要有正常值、边界值（刚好接受和刚好拒绝）和异常值。", "Test data needs a normal value, boundary values (just accepted and just rejected) and an abnormal value."),
                            ],
                            "年龄必须是 11 到 18 的整数。范围验证会接受 11 和 18，拒绝 10 和 19，也会拒绝 “fifteen”。它不能发现学生把 16 误打成 17：17 是合理的，只是不是事实。那要靠校验，例如把年龄输入两遍，不一致就重新输入。\n\n设计测试数据时四个数就够说明问题：15（正常）、11（边界接受）、10（边界拒绝）、-3 或一个字母（异常）。不要只写“输入一个错误的数”。",
                            "Age must be an integer from 11 to 18. A range check accepts 11 and 18, rejects 10 and 19, and rejects “fifteen”. It cannot catch a student who types 17 instead of 16: 17 is reasonable and simply untrue. That needs verification, for example entering the age twice and rejecting a mismatch.\n\nFour items of test data are enough: 15 (normal), 11 (boundary, accepted), 10 (boundary, rejected), and -3 or a letter (abnormal). Do not only write “enter a wrong number”.",
                            "“分数必须在 0 和 100 之间。”下列哪个是边界上应被接受的值？\n\n**解：** 0 和 100。101 和 -1 是刚好不被接受的边界异常。只写 50 只能说明正常数据。",
                            "“A mark must be from 0 to 100.” Which values sit on the boundary and should be accepted?\n\n**Solution:** 0 and 100. 101 and -1 are the boundary values that should be rejected. 50 only shows normal data.",
                            [
                                ("把两次输入叫做验证。", "Calling double entry validation."),
                                ("边界测试只写区间中间的数。", "A boundary test that only uses a value in the middle of the range."),
                                ("认为通过范围检查的数据一定是正确的事实。", "Assuming that data which passes a range check must be the true fact."),
                            ],
                            [
                                mcq("两次输入同一个学号并比较，这是？", "Entering an ID twice and comparing the two entries is:", "b", "校验。", "Verification.", [("范围验证", "range validation"), ("校验", "verification"), ("求平均", "finding an average"), ("分解", "decomposition")]),
                                short("年龄规则是 11 到 18。写出一个应被接受的边界值。", "The age rule is 11 to 18. Give one boundary value that should be accepted.", "11", "11 或 18。", "11 or 18.", ["11", "18"], 1),
                                short("同一规则下，写出一个异常数据的例子。", "For the same rule, give one example of abnormal data.", "-1", "超出范围或类型不对都可以。", "Outside the range, or the wrong type.", ["-1", "10", "19", "fifteen", "A", "-3"], 2),
                            ],
                        ),
                        L(
                            "g9cs-7-8", "7.8",
                            "追踪表",
                            "Trace tables",
                            "能为一段短算法填写追踪表：每一列是一个变量，每一行是一次变化之后的值。",
                            "Complete a trace table for a short algorithm: one column per variable, and a new row after each change.",
                            [
                                ("列包括每一个会变的变量，有输出时再加一列 OUTPUT。", "Columns are the variables that change, plus OUTPUT if anything is output."),
                                ("一行只记录一次赋值或一次输出之后的状态。", "A row records the state after one assignment or one output."),
                                ("循环要展开。不要在一行里写“重复三次”。", "Unroll a loop. Do not write “repeat three times” in a single row."),
                                ("最后一行的值就是算法结束时的值，用来对答案。", "The last row is the state when the algorithm stops, and it is what you check against."),
                            ],
                            "追踪表是在纸上当计算机。条件不成立时不要假装循环体又执行了一次。WHILE 先判断再执行；REPEAT 先执行再判断，所以 REPEAT 的循环体至少一次。\n\n写数字时每一步都写，即使某个变量这一步没变，也可以沿用上一行，但改变了的那一格一定要新写。阅卷人要看见 max 或 total 是在哪一步改的。",
                            "A trace table is you being the computer. Do not pretend the body ran when the condition was false. WHILE tests before the body. REPEAT runs the body before the test, so the body happens at least once.\n\nWrite every step. You may carry an unchanged value down, but a cell that changes must be written again. The marker needs to see the step where max or total changed.",
                            "追踪：\n\n```\nx ← 1\ntotal ← 0\nWHILE x <= 3 DO\n    total ← total + x\n    x ← x + 1\nENDWHILE\n```\n\n**过程：** (x, total) 从 (1, 0) 到 (2, 1)、(3, 3)、(4, 6)。结束时 total = 6，x = 4。",
                            "Trace:\n\n```\nx ← 1\ntotal ← 0\nWHILE x <= 3 DO\n    total ← total + x\n    x ← x + 1\nENDWHILE\n```\n\n**Steps:** (x, total) goes (1, 0) → (2, 1) → (3, 3) → (4, 6). At the end total = 6 and x = 4.",
                            [
                                ("WHILE 的条件已经为假，仍再加一次。", "Adding once more after a WHILE condition has become false."),
                                ("把循环前的初值忘了写进表里。", "Leaving the initial values off the table."),
                                ("REPEAT 和 WHILE 都当成先判断。", "Treating REPEAT and WHILE as if both tested first."),
                            ],
                            [
                                num("上例结束时 total 是多少？", "In the example above, what is total at the end?", "6", "1+2+3 = 6。", "1+2+3 = 6.", 2, 0),
                                num("上例结束时 x 是多少？", "In the example above, what is x at the end?", "4", "x 变成 4 后条件失败。", "x becomes 4 and the condition then fails.", 1, 0),
                                mcq("REPEAT … UNTIL 的循环体至少执行几次？", "How many times does a REPEAT … UNTIL body run at minimum?", "a", "一次。", "Once.", [("一次", "once"), ("零次", "never"), ("和 FOR 一样必须是 n 次", "exactly n times, like every FOR"), ("两次，因为有 UNTIL", "twice, because of UNTIL")]),
                            ],
                        ),
                        L(
                            "g9cs-7-9", "7.9",
                            "把解法写成算法",
                            "Writing an algorithm",
                            "能根据一句任务写出完整、可追踪的伪代码，包含初值、循环、条件和输出。",
                            "Turn a one-sentence task into complete pseudocode that can be traced, with initial values, a loop, a condition and an output.",
                            [
                                ("先用一句话写输入和输出，再写伪代码。", "Write the inputs and outputs in one sentence before the pseudocode."),
                                ("每一个累加器和计数器都要在循环前赋初值。", "Give every total and counter a starting value before the loop."),
                                ("条件要写完整。不要写 “IF bigger”。", "Write the whole condition. Do not write “IF bigger”."),
                                ("结束前 OUTPUT 题目要求的那个结果，不多输出调试用的句子。", "Before the end, OUTPUT the result the question asked for, not a line of debugging chat."),
                            ],
                            "卷面上的“写一个算法”通常只要伪代码，不要整篇 Python，除非题目点名。结构可以是：输入个数 n，然后 FOR 循环读入并处理，最后输出。若个数未知、用一个特殊值结束，就用 WHILE 或 REPEAT，并写清那个结束值不算进数据。\n\n写完后用两个数自己追踪一遍。追踪失败就还不能交。查找和排序的标准算法本阶段不考；不要用一段冒泡排序代替题目要的求和或计数。",
                            "A “write an algorithm” question usually wants pseudocode, not a full Python program, unless it names Python. A sound shape is: input n, then a FOR loop that reads and processes, then an output. If the count is unknown and a sentinel ends the list, use WHILE or REPEAT, and do not treat the sentinel as data.\n\nTrace two values yourself before you finish. If the trace fails, it is not ready. The standard search and sort algorithms are not on this paper. Do not replace a required total or count with a bubble sort.",
                            "任务：读入 5 个整数，输出其中负数的个数。\n\n```\ncount ← 0\nFOR i ← 1 TO 5\n    INPUT n\n    IF n < 0 THEN\n        count ← count + 1\n    ENDIF\nNEXT i\nOUTPUT count\n```",
                            "Task: read five integers and output how many are negative.\n\n```\ncount ← 0\nFOR i ← 1 TO 5\n    INPUT n\n    IF n < 0 THEN\n        count ← count + 1\n    ENDIF\nNEXT i\nOUTPUT count\n```",
                            [
                                ("忘了 count ← 0。", "Forgetting count ← 0."),
                                ("结束值也被当成一个有效数据。", "Treating the sentinel as one more piece of data."),
                                ("只写中文步骤，没有赋值、判断和循环。", "Writing prose steps with no assignment, condition or loop."),
                            ],
                            [
                                short("计数器应在什么位置赋成 0？", "Where should a counter be set to 0?", "before the loop", "在循环外面、循环开始之前。", "Outside the loop, before it starts.", ["before the loop", "循环前", "outside the loop"], 1),
                                mcq("题目说“写伪代码”，最好提交？", "If the question says “write pseudocode”, the best submission is:", "c", "使用 ←、IF、FOR/NEXT 的伪代码。", "Pseudocode using ←, IF and FOR/NEXT.", [("一整页无关的注释", "a page of unrelated comments"), ("只有流程图且没有题目要求的步骤", "only a chart that skips the required steps"), ("带 ←、IF 和循环的伪代码", "pseudocode with ←, IF and a loop"), ("一段冒泡排序，不管题目要的是计数", "a bubble sort, whatever the question asked")]),
                                short("用特殊值 -1 结束输入时，-1 应该怎样处理？", "If the sentinel -1 ends the input, what should happen to -1?", "not counted as data", "它不是一个有效数据。", "It is not a data value.", ["not counted as data", "不要计入", "ignored", "not data"], 2),
                            ],
                        ),
                    ],
                },
            ],
        },
        {
            "id": "g9-cs-8",
            "code": "8",
            "order": 2,
            "title_zh": "第 8 章 · 编程：子程序与一维数组",
            "title_en": "Chapter 8 · Programming: sub-routines and 1D arrays",
            "note_zh": "8.1 子程序，以及 8.2.1 一维数组。二维数组不在本阶段。",
            "note_en": "8.1 sub-routines, and 8.2.1 one-dimensional arrays. Two-dimensional arrays are not in this stage.",
            "practice_minutes": 20,
            "units": [{
                "id": "g9-cs-8-u1",
                "code": "8.1–8.2.1",
                "order": 1,
                "title_zh": "子程序与一维数组",
                "title_en": "Sub-routines and one-dimensional arrays",
                "lessons": [
                    L(
                        "g9cs-8-1", "8.1",
                        "子程序：过程与函数",
                        "Sub-routines: procedures and functions",
                        "能区分过程与函数，并说明参数、局部变量和全局变量。",
                        "Tell a procedure from a function, and explain parameters, local variables and global variables.",
                        [
                            ("子程序是一段有名字、可以反复调用的算法。", "A sub-routine is a named piece of algorithm that can be called again."),
                            ("过程（PROCEDURE）执行动作，不一定送回一个值。函数（FUNCTION）必须 RETURN 一个值。", "A PROCEDURE performs an action and need not send a value back. A FUNCTION must RETURN a value."),
                            ("参数是调用时传进去的数据。局部变量只在子程序内部存在。", "A parameter is data passed in at the call. A local variable exists only inside the sub-routine."),
                            ("全局变量在整个程序里都能改。能用参数解决的，就不要靠全局变量传递。", "A global variable can be changed from anywhere. If a parameter will do, do not pass the value through a global."),
                        ],
                        "把“求平均”写成函数，是因为它要交还一个数。把“打印一张成绩单”写成过程，是因为它的目的是输出动作。调用函数时，返回值要有去处：`average ← Mean(total, count)`。调用过程则是 `CALL PrintReport(name)`。\n\nPython 里两者都用 `def`。有 `return` 的相当于函数；没有 return、只产生输出的相当于过程。考试若要伪代码，仍要写出 PROCEDURE 或 FUNCTION，不要只写 def。",
                        "“Find the average” is a function because it has to hand a number back. “Print a mark sheet” is a procedure because its purpose is the action of output. A function call needs somewhere for the result: `average ← Mean(total, count)`. A procedure call is `CALL PrintReport(name)`.\n\nIn Python both use `def`. A `return` makes it a function; output with no return is closer to a procedure. If the paper wants pseudocode, write PROCEDURE or FUNCTION, not only def.",
                        "下面哪一个应当是函数？\n\nA. 在屏幕上显示欢迎语。\nB. 根据总价和税率算出应付金额并交还给主程序。\n\n**解：** B。它要返回一个数。A 是过程。",
                        "Which of these should be a function?\n\nA. Display a welcome line.\nB. Work out the amount due from a total and a tax rate, and hand it back.\n\n**Solution:** B. It must return a number. A is a procedure.",
                        [
                            ("函数没有 RETURN。", "A function with no RETURN."),
                            ("用全局变量代替本来应作为参数传入的分数。", "Using a global variable for a mark that should have been a parameter."),
                            ("在伪代码答案里只写 Python 的 def，没有说明是过程还是函数。", "Answering in pseudocode with only Python’s def, and never saying procedure or function."),
                        ],
                        [
                            mcq("必须把一个结果交还调用处的是？", "Which of these must hand a result back to the caller?", "b", "函数。", "A function.", [("过程", "a procedure"), ("函数", "a function"), ("流程图的箭头", "a flowchart arrow"), ("注释", "a comment")]),
                            short("只在子程序内部有效的变量叫什么？", "What is a variable that exists only inside the sub-routine called?", "local", "局部变量。", "A local variable.", ["local", "a local variable", "局部变量"], 1),
                            mcq("打印欢迎语、不需要返回值，更适合写成？", "A welcome message with no value to return is better written as:", "a", "过程。", "A procedure.", [("过程", "a procedure"), ("必须返回字符串长度的函数", "a function that must return the string length"), ("一维数组", "a one-dimensional array"), ("范围验证", "a range check")]),
                        ],
                    ),
                    L(
                        "g9cs-8-2", "8.2.1",
                        "一维数组",
                        "One-dimensional arrays",
                        "会声明并使用一维数组，并说明什么时候必须保存全部数据，而不能只保留一个总和。",
                        "Declare and use a one-dimensional array, and say when every value must be kept rather than only a running total.",
                        [
                            ("一维数组用一个名字和一个下标保存一列同一类型的数据。", "A one-dimensional array stores a list of one type under one name and an index."),
                            ("本课程的伪代码数组从 1 编号到 n。Python 的 list 从 0 编号到 n-1。", "In this course’s pseudocode, arrays run from 1 to n. A Python list runs from 0 to n-1."),
                            ("只求总和时可以不保存每个数。若求完平均后还要数出“高于平均的个数”，就必须先把每个数留下。", "A total alone does not need every value stored. Counting how many are above the average, after the average is known, does."),
                            ("用循环访问每一个下标。不要把 A[i] 写成一个新的变量名 A i。", "Visit every index in a loop. Do not turn A[i] into a new variable name."),
                        ],
                        "声明可以写成 `DECLARE Mark : ARRAY[1:5] OF INTEGER`。`Mark[3] ← 80` 把 80 放进第 3 格。求和仍是 total 从 0 开始，下标从 1 走到 5。\n\n“高于平均”需要两遍：第一遍求和并求平均，第二遍用同一个数组计数。如果第一遍就把每个输入丢掉，第二遍没有数据可读。这就是数组相对于“边读边加”的理由。二维表（行和列）本阶段不要求。",
                            "A declaration may look like `DECLARE Mark : ARRAY[1:5] OF INTEGER`. `Mark[3] ← 80` stores 80 in cell 3. The total still starts at 0, and the index runs from 1 to 5.\n\n“Above average” needs two passes: one to total and average, one to count using the same array. If the first pass throws each input away, the second pass has nothing to read. That is why an array is different from adding as you go. A two-dimensional table, with rows and columns, is not required at this stage.",
                        "Mark[1] = 3，Mark[2] = 8，Mark[3] = 2。\n\n`Mark[2]` 的值是 8。三格的和是 13。平均是 $13/3$，约 4.33。大于平均的只有 8，计数为 1。若只用边读边加，算完平均后就无法再找出那个 8。",
                        "Mark[1] = 3, Mark[2] = 8, Mark[3] = 2.\n\n`Mark[2]` is 8. The total of the three cells is 13. The average is $13/3$, about 4.33. Only 8 is above it, so the count is 1. A running total that discards each input cannot find that 8 afterwards.",
                        [
                            ("伪代码里把第一格写成 Mark[0]。", "Writing the first cell as Mark[0] in this course’s pseudocode."),
                            ("Python 里把第一格写成 marks[1]，从而漏掉 marks[0]。", "In Python, treating marks[1] as the first cell and skipping marks[0]."),
                            ("明明还要第二遍使用数据，却没有用数组。", "Needing a second pass and not using an array."),
                        ],
                        [
                            num("Mark[1] = 3，Mark[2] = 8，Mark[3] = 2。Mark[2] 是多少？", "Mark[1] = 3, Mark[2] = 8, Mark[3] = 2. What is Mark[2]?", "8", "下标 2 是第二格。", "Index 2 is the second cell.", 1, 0),
                            num("这三个数的和是多少？", "What is the total of the three cells?", "13", "3+8+2 = 13。", "3+8+2 = 13.", 1, 0),
                            short("什么时候必须用数组，而不能只保留总和？", "When must you use an array, rather than keeping only a total?", "when the values are needed again", "还要再次使用每一个数时。", "When each value is needed again.", ["when the values are needed again", "需要第二遍", "a second pass", "需要再次使用每个数"], 2),
                        ],
                    ),
                ],
            }],
        },
    ],
    "paper": {
        "id": "paper-g9-cs",
        "title_zh": "练习卷 · 算法、伪代码与一维数组（50 分）",
        "title_en": "Practice paper · algorithms, pseudocode and 1D arrays (50 marks)",
        "minutes": 50,
        "published": "2026-11-18T13:00:00+08:00",
        "items": [
            ("g9cs-7-1", mcq("生命周期里，在写代码之前把步骤用流程图表示，属于？", "Showing the steps as a flowchart before coding belongs to:", "b", "设计。", "Design.", [("测试", "testing"), ("设计", "design"), ("只属于维护", "maintenance only"), ("验证数据是否被录错", "verification of a transcription")], 1)),
            ("g9cs-7-1", short("把“统计小测”拆成输入、求和、计数、求平均。这个拆分叫什么？", "Splitting “process a test” into input, total, count and average is called:", "decomposition", "分解。", "Decomposition.", ["decomposition", "分解"], 2)),
            ("g9cs-7-2", mcq("流程图里表示判断的符号是？", "Which flowchart symbol is a decision?", "c", "菱形。", "A diamond.", [("平行四边形", "a parallelogram"), ("矩形", "a rectangle"), ("菱形", "a diamond"), ("一条直线没有出口", "a line with no exit")], 1)),
            ("g9cs-7-3", short("伪代码用 ENDIF 结束的结构，在 Python 里靠什么表示结束？", "A structure that pseudocode ends with ENDIF is ended in Python by:", "indentation", "缩进，而不是 ENDIF。", "Indentation, not ENDIF.", ["indentation", "indent", "缩进"], 2)),
            ("g9cs-7-3", short("要让 Python 依次取出 1、2、3、4、5，range 怎样写？", "Which range produces 1, 2, 3, 4, 5 in Python?", "range(1, 6)", "右端要写成 6。", "The right-hand end must be 6.", ["range(1, 6)", "range(1,6)"], 2)),
            ("g9cs-7-4", num("输入 4、7、1、9。按求和算法，total 的最终值是多少？", "Inputs: 4, 7, 1, 9. What is the final total?", "21", "21。", "21.", 3, 0)),
            ("g9cs-7-4", num("同一组数里，大于 5 的计数是多少？", "In the same list, how many values are greater than 5?", "2", "两个。", "Two.", 3, 0)),
            ("g9cs-7-4", num("同一组数的最大值是多少？", "What is the maximum of the same list?", "9", "9。", "9.", 2, 0)),
            ("g9cs-7-4", num("若四个数都计入，平均数是多少？", "If all four values count, what is the average?", "5.25", "21/4。", "21/4.", 3, 0.01, ["5.25", "21/4"])),
            ("g9cs-7-5", mcq("检查“分数在 0 到 100 之间”属于？", "Checking that a mark is from 0 to 100 is:", "a", "范围验证。", "Range validation.", [("范围验证", "range validation"), ("两次输入的校验", "double-entry verification"), ("求数组平均", "finding an array average"), ("声明全局变量", "declaring a global variable")], 2)),
            ("g9cs-7-5", short("把同一学号输入两次并比较，这是验证还是校验？", "Entering the same ID twice and comparing is validation or verification?", "verification", "校验。", "Verification.", ["verification", "校验"], 2)),
            ("g9cs-7-5", short("规则：整数分数 0 到 100。写出一个应被拒绝的边界值。", "Rule: integer marks from 0 to 100. Give one boundary value that should be rejected.", "101", "101 或 -1。", "101 or -1.", ["101", "-1", "100.5"], 3)),
            ("g9cs-7-8", num(
                "追踪后 total 是多少？\n\n```\nx ← 1\ntotal ← 0\nWHILE x <= 3 DO\n    total ← total + x\n    x ← x + 1\nENDWHILE\n```",
                "After the trace, what is total?\n\n```\nx ← 1\ntotal ← 0\nWHILE x <= 3 DO\n    total ← total + x\n    x ← x + 1\nENDWHILE\n```",
                "6", "1+2+3。", "1+2+3.", 3, 0)),
            ("g9cs-7-8", num("同一段算法结束时 x 是多少？", "When that algorithm stops, what is x?", "4", "条件失败时 x 已经是 4。", "x is already 4 when the condition fails.", 2, 0)),
            ("g9cs-7-9", write(
                "q-g9cs-write",
                "用伪代码写一个算法：读入 5 个整数，输出其中负数的个数。要有初值、循环、条件和输出。系统按要点给分。",
                "Write pseudocode that reads five integers and outputs how many are negative. Include a starting value, a loop, a condition and an output. Key points are marked automatically.",
                "见解析中的一种写法。",
                "一种写法：\n\n```\ncount ← 0\nFOR i ← 1 TO 5\n    INPUT n\n    IF n < 0 THEN\n        count ← count + 1\n    ENDIF\nNEXT i\nOUTPUT count\n```",
                "One version:\n\n```\ncount ← 0\nFOR i ← 1 TO 5\n    INPUT n\n    IF n < 0 THEN\n        count ← count + 1\n    ENDIF\nNEXT i\nOUTPUT count\n```",
                ["count", "FOR", "INPUT", "IF", "OUTPUT", "NEXT"],
                4,
                8,
            )),
            ("g9cs-8-1", short("需要把平均值交还给主程序时，应使用过程还是函数？", "If the average must be handed back to the main program, do you use a procedure or a function?", "function", "函数要返回值。", "A function returns a value.", ["function", "函数", "a function"], 3)),
            ("g9cs-8-2", num("A[1]=3，A[2]=8，A[3]=2。按本课程的下标，A[2] 是多少？", "A[1]=3, A[2]=8, A[3]=2. Using this course’s indexing, what is A[2]?", "8", "第二格。", "The second cell.", 4, 0)),
            ("g9cs-8-2", short("已经算出平均后，还要数“高于平均的个数”。为什么不能只保留总和？", "After the average is known you must count how many are above it. Why is a total alone not enough?", "the values are needed again", "每个数还要再读一次。", "Each value has to be read again.", ["the values are needed again", "需要第二遍", "second pass", "需要再次使用每个数"], 4)),
        ],
    },
}
