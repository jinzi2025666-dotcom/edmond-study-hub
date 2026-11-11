"""Computer Science, Economics and coding exercises."""
from _helpers import Q, KP, SET, opts

# ---------------------------------------------------------------------------
# Computer Science
# ---------------------------------------------------------------------------
KP_CS_AL_ZH = r"""
## 先想清楚步骤，再写代码

第 8 阶段计算 **单元 8.2 It’s all in the planning** 强调：算法是解决问题的有序步骤。写程序之前，应先把步骤分解，并用**伪代码**或流程图表示。

## 要点

1. **分解（decomposition）**：把大问题拆成可管理的小问题。例如“判断成绩是否及格”可拆成：输入分数 → 判断 → 输出结果。
2. **三种基本结构**：
   - **顺序（sequence）**：按步骤依次执行；
   - **选择（selection）**：根据条件走不同路径（`IF...THEN...ELSE...ENDIF`）；
   - **循环（iteration）**：重复执行（`FOR` 或 `WHILE`）。
3. **伪代码**不是某一种必须编译的语言，但应保持一致、清晰。本站示例采用常见课堂写法：关键字大写，缩进表示层次。
4. 一个好算法应当：**有限步骤内结束**、每一步明确、能处理合理的输入。
5. 流程图用标准符号：椭圆表示开始/结束，平行四边形表示输入/输出，矩形表示处理，菱形表示判断。

## 例题

用伪代码表示：输入一个整数，若为偶数则输出 `even`，否则输出 `odd`。

```
INPUT number
IF number MOD 2 = 0 THEN
    OUTPUT "even"
ELSE
    OUTPUT "odd"
ENDIF
```

对应的 Python 思路是 `if number % 2 == 0:`。你可以在本站的**代码练习区**亲自运行类似练习。
"""

KP_CS_AL_EN = r"""
## Plan the steps before you write code

Stage 8 Computing **Unit 8.2 It’s all in the planning** treats an algorithm as an ordered set of steps for solving a problem. Before coding, decompose the task and express it in **pseudocode** or a flowchart.

## Key points

1. **Decomposition** breaks a large problem into manageable parts. “Report whether a mark is a pass” becomes: input the mark → decide → output the result.
2. **Three basic constructs:**
   - **sequence:** steps in order;
   - **selection:** different paths according to a condition (`IF...THEN...ELSE...ENDIF`);
   - **iteration:** repetition (`FOR` or `WHILE`).
3. **Pseudocode** is not a language that must compile, but it should be consistent and clear. Examples on this site use a common classroom style: keywords in capitals, indent for structure.
4. A sound algorithm **finishes in a finite number of steps**, has unambiguous instructions, and can handle reasonable input.
5. Flowcharts use standard shapes: ovals for start/end, parallelograms for input/output, rectangles for processes, diamonds for decisions.

## Worked example

Write pseudocode that inputs an integer and outputs `even` if it is even, otherwise `odd`.

```
INPUT number
IF number MOD 2 = 0 THEN
    OUTPUT "even"
ELSE
    OUTPUT "odd"
ENDIF
```

The matching Python idea is `if number % 2 == 0:`. You can run similar tasks in this site’s **code practice area**.
"""

KP_CS_NET_ZH = r"""
## 网络把计算机连在一起——也把风险连在一起

**单元 8.1 Building networks** 关注网络结构与安全。网络使资源共享和通信成为可能，但数据在传输中也可能被截获或破坏。

## 要点

1. **按范围**：
   - **LAN（局域网）**：较小区域，如家庭、教室、一栋楼；
   - **WAN（广域网）**：更大范围，因特网是许多网络互连而成的全球网络。
2. **拓扑（topology）** 描述设备如何连接。常见有：
   - **星型**：各设备连到中心设备（如交换机）；一节点故障通常不影响其他节点，但中心故障影响全网；
   - **总线型**：共享一条主干；布线简单，但主干故障影响较大；
   - **网状**：多条路径，可靠性高，成本和复杂度也高。
3. **有线与无线**：有线（如以太网电缆）通常更稳定、往往更安全；无线更灵活，但信号可能受干扰，也需要更认真地设置安全措施。
4. **基本安全措施**（第 8 阶段层面）：
   - 强密码与不共享账号；
   - **防火墙** 按规则过滤流量；
   - **加密** 使截获的数据难以读懂；
   - 谨慎对待附件与未知链接，更新系统以减少恶意软件风险。
5. 设计网络时要同时考虑：**连通、可扩展、安全**。

## 例子

教室里的电脑连到一台交换机，再连到路由器访问因特网，这是星型 LAN 接入 WAN。如果教室没有密码的开放 Wi‑Fi，外人就可能进入同一网络——这就是“便利而未设防”的典型风险。
"""

KP_CS_NET_EN = r"""
## Networks connect computers — and they connect risks

**Unit 8.1 Building networks** is about network structure and security. Networks let us share resources and communicate, but data in transit can also be intercepted or damaged.

## Key points

1. **By scale:**
   - a **LAN (local area network)** covers a small area such as a home, a classroom or a building;
   - a **WAN (wide area network)** covers a larger area. The internet is a global network of networks.
2. **Topology** describes how devices are connected. Common examples:
   - **star:** each device links to a central device (such as a switch); a leaf fault usually stays local, but the centre is a critical point;
   - **bus:** devices share a backbone; cabling is simple, but a backbone fault is serious;
   - **mesh:** many paths give high reliability, at higher cost and complexity.
3. **Wired and wireless:** wired links (such as Ethernet cable) are often more stable and can be easier to keep private; wireless is more flexible but can suffer interference and needs careful security settings.
4. **Basic security** at Stage 8 level includes:
   - strong passwords and not sharing accounts;
   - a **firewall** that filters traffic by rules;
   - **encryption**, so intercepted data is hard to read;
   - care with attachments and unknown links, and updates to reduce malware risk.
5. Network design should consider **connectivity, scale and security** together.

## Example

Classroom computers join a switch, which joins a router to the internet: a star LAN that connects to a WAN. An open classroom Wi‑Fi with no password is a typical case of convenience without protection.
"""

questions_cs = [
    Q("q-cs-al-01", "computer-science", "computer-science-8-2", "mcq",
      "把一个大问题拆成若干较小问题，这一做法称为？",
      "Breaking a large problem into smaller manageable parts is called:",
      "b",
      "这是分解（decomposition），是算法设计的第一步。",
      "This is decomposition, a first step in designing an algorithm.",
      opts(("加密", "Encryption"),
           ("分解", "Decomposition"),
           ("拓扑", "Topology"),
           ("校验和", "A checksum")),
      knowledge_id="kp-cs-algorithms"),
    Q("q-cs-al-02", "computer-science", "computer-science-8-2", "mcq",
      "伪代码中的 `IF...THEN...ELSE...ENDIF` 属于哪一种结构？",
      "In pseudocode, `IF...THEN...ELSE...ENDIF` is an example of:",
      "c",
      "根据条件选择不同路径，属于选择（selection）。",
      "Choosing a path according to a condition is selection.",
      opts(("顺序", "Sequence"),
           ("循环", "Iteration"),
           ("选择", "Selection"),
           ("仅用于输出", "Output only")),
      knowledge_id="kp-cs-algorithms"),
    Q("q-cs-al-03", "computer-science", "computer-science-8-2", "short",
      "若要用伪代码判断一个数是否为偶数，常用哪一种运算？（可写 MOD 或 %）",
      "Which operation is commonly used in pseudocode to test whether a number is even? (You may write MOD or %.)",
      "MOD",
      "用 `number MOD 2 = 0`（或 Python 中的 `%`）判断能否被 2 整除。",
      "Use `number MOD 2 = 0` (or `%` in Python) to test divisibility by 2.",
      knowledge_id="kp-cs-algorithms",
      accepted=["MOD", "mod", "%", "modulo", "modulus", "取余", "求余", "模运算"]),
    Q("q-cs-net-01", "computer-science", "computer-science-8-1", "mcq",
      "覆盖一间教室或一栋楼的网络，通常称为？",
      "A network that covers a classroom or a single building is usually called a:",
      "a",
      "这是局域网 LAN。WAN 覆盖更大范围。",
      "That is a LAN. A WAN covers a much larger area.",
      opts(("LAN", "LAN"),
           ("WAN", "WAN"),
           ("只可能是因特网本身", "the internet itself, and nothing else"),
           ("CPU", "CPU")),
      knowledge_id="kp-cs-networks",
      published_at="2026-11-07T11:00:00+08:00"),
    Q("q-cs-net-02", "computer-science", "computer-science-8-1", "short",
      "星型拓扑中，各设备通常连接到哪一种中心设备？（可写 switch / 交换机，或 hub）",
      "In a star topology, devices usually connect to which central device? (e.g. switch or hub)",
      "switch",
      "常见答案是交换机（switch），旧式网络也可能是集线器（hub）。路由器常用于连接不同网络。",
      "A switch is the usual modern answer; a hub is also accepted. A router more often links different networks.",
      knowledge_id="kp-cs-networks",
      accepted=["switch", "a switch", "hub", "a hub", "交换机", "集线器", "switch or hub", "交换机或集线器"]),
    Q("q-cs-net-03", "computer-science", "computer-science-8-1", "mcq",
      "下列哪一项是基本的网络安全措施？",
      "Which of the following is a basic network security measure?",
      "d",
      "强密码、防火墙、加密和谨慎对待未知链接都是基础措施。把密码写在公共黑板并不是安全措施。",
      "Strong passwords, firewalls, encryption and care with unknown links are basic measures. Writing the password on a public board is not.",
      opts(("把密码写在教室黑板并保持不变", "Write the password on the classroom board and never change it"),
           ("关闭所有更新，以免软件变化", "Turn off all updates so that software never changes"),
           ("向所有来信附件一律打开", "Open every email attachment"),
           ("使用防火墙并启用加密（如安全的 Wi‑Fi）", "Use a firewall and enable encryption, such as secured Wi‑Fi")),
      knowledge_id="kp-cs-networks"),
    Q("q-cs-data-01", "computer-science", "computer-science-8-3", "numeric",
      "在标准 ASCII 中，大写字母 `A` 的编码是 $65$。字母 `C` 的编码是多少？",
      "In standard ASCII, `A` is coded as $65$. What is the code for `C`?",
      "67",
      "字母按顺序排列：`A` 为 $65$，`B` 为 $66$，`C` 为 $67$。",
      "The letters are in order: `A` is $65$, `B` is $66$, `C` is $67$.",
      tolerance=0),
    Q("q-cs-val-01", "computer-science", "computer-science-8-5", "mcq",
      "输入年龄时限制“必须是 $0$ 到 $120$ 之间的数字”，这主要属于？",
      "Restricting an age entry to “a number between $0$ and $120$” is mainly an example of:",
      "b",
      "这是数据校验（validation）：在输入时检查数据是否合理。核对（verification）则是检查数据是否与原件一致，例如双输入。",
      "This is validation: checking that data is reasonable at the point of entry. Verification checks that data matches the source, for example by double entry.",
      opts(("加密", "Encryption"),
           ("校验（validation）", "Validation"),
           ("拓扑设计", "Topology design"),
           ("只是美观问题，与数据质量无关", "A cosmetic issue only, unrelated to data quality"))),
    Q("q-cs-test-01", "computer-science", "computer-science-8-4", "mcq",
      "测试程序时，为什么需要准备不同类型的测试数据？",
      "Why should a test plan include different types of test data?",
      "c",
      "正常值、边界值和无效值能帮助发现在不同条件下的错误，而不仅是“碰巧一次跑通”。",
      "Typical, boundary and invalid data help you find errors in different conditions, not just one lucky successful run.",
      opts(("为了让程序看起来更长", "To make the program look longer"),
           ("因为测试数据越多，计算机就会自动改对逻辑错误", "Because more data will automatically repair logic errors"),
           ("以检查正常、边界和无效输入下程序是否按预期工作",
            "To check that the program behaves as expected with typical, boundary and invalid input"),
           ("测试计划只用于硬件，不用于程序", "Test plans are only used for hardware, never for programs"))),
    Q("q-cs-bug-01", "computer-science", "computer-science-8-6", "short",
      "程序能运行，但计算结果总是少 $1$。这更可能是哪一类错误？请回答“逻辑错误”或 “logic error”。",
      "A program runs, but the result is always 1 too small. Which type of error is this more likely to be? Write “logic error” or the Chinese equivalent.",
      "logic error",
      "能运行说明通常不是让程序无法执行的语法错误；结果不对属于逻辑错误。",
      "If it runs, it is usually not a syntax error that stops execution. A wrong result points to a logic error.",
      accepted=["logic error", "logic", "logical error", "逻辑错误", "逻辑", "logic-error"]),
]

knowledge_cs = [
    KP("kp-cs-algorithms", "computer-science", "computer-science-8-2", "computer-science-8-2-1",
       "算法、分解与伪代码",
       "Algorithms, decomposition and pseudocode",
       KP_CS_AL_ZH, KP_CS_AL_EN,
       ["q-cs-al-01", "q-cs-al-02", "q-cs-al-03"],
       "2026-10-12T10:00:00+08:00",
       "先分解问题，再用顺序、选择和循环写出清晰的伪代码。",
       "Decompose the problem, then express it clearly with sequence, selection and iteration."),
    KP("kp-cs-networks", "computer-science", "computer-science-8-1", "computer-science-8-1-1",
       "网络类型、拓扑与基本安全",
       "Network types, topologies and basic security",
       KP_CS_NET_ZH, KP_CS_NET_EN,
       ["q-cs-net-01", "q-cs-net-02", "q-cs-net-03"],
       "2026-11-07T11:00:00+08:00",
       "区分 LAN 与 WAN，理解星型等拓扑，并用密码、防火墙与加密保护网络。",
       "Distinguish LAN and WAN, understand topologies such as star, and protect networks with passwords, firewalls and encryption."),
]

sets_cs = [
    SET("practice-cs-algorithms-networks", "computer-science", "computer-science-8-2", "practice",
        "练习组 · 算法与网络",
        "Practice set · Algorithms and networks",
        ["q-cs-al-01", "q-cs-al-02", "q-cs-al-03", "q-cs-net-01", "q-cs-net-02", "q-cs-val-01"],
        published_at="2026-11-07T12:00:00+08:00"),
    SET("paper-cs-a", "computer-science", "computer-science-8-1", "paper",
        "本站练习卷 A · 网络、算法与数据",
        "Practice Paper A · Networks, algorithms and data",
        ["q-cs-al-01", "q-cs-al-02", "q-cs-al-03", "q-cs-net-01", "q-cs-net-03",
         "q-cs-net-02", "q-cs-data-01", "q-cs-val-01", "q-cs-test-01", "q-cs-bug-01"],
        time_limit=25, published_at="2026-10-21T09:00:00+08:00"),
]

coding_exercises = [
    {
        "id": "code-hello-name",
        "title_zh": "输入与输出：打招呼",
        "title_en": "Input and output: a greeting",
        "brief_zh": "从一行输入读取姓名，输出 `Hello, 姓名`。例如输入 `Edmond`，应输出 `Hello, Edmond`。注意大小写、逗号和空格要一致，行末可有换行。",
        "brief_en": "Read a name from one line of input and print `Hello, name`. For input `Edmond`, print `Hello, Edmond`. Match the capitalisation, comma and space; a trailing newline is fine.",
        "starter": "name = input()\n# print a greeting\n",
        "solution": "name = input()\nprint(\"Hello, \" + name)\n",
        "tests": [
            {"stdin": "Edmond\n", "stdout": "Hello, Edmond\n"},
            {"stdin": "Maya\n", "stdout": "Hello, Maya\n"},
        ],
    },
    {
        "id": "code-even-odd",
        "title_zh": "选择结构：偶数还是奇数",
        "title_en": "Selection: even or odd",
        "brief_zh": "读取一个整数。若是偶数，只输出 `even`；否则只输出 `odd`（小写）。例如输入 `7` 应输出 `odd`。",
        "brief_en": "Read one integer. If it is even, print only `even`; otherwise print only `odd` (lowercase). For example, input `7` should print `odd`.",
        "starter": "n = int(input())\n# use if / else\n",
        "solution": "n = int(input())\nif n % 2 == 0:\n    print(\"even\")\nelse:\n    print(\"odd\")\n",
        "tests": [
            {"stdin": "8\n", "stdout": "even\n"},
            {"stdin": "7\n", "stdout": "odd\n"},
            {"stdin": "0\n", "stdout": "even\n"},
        ],
    },
    {
        "id": "code-sum-loop",
        "title_zh": "循环：从 1 加到 n",
        "title_en": "Iteration: sum from 1 to n",
        "brief_zh": "读取正整数 $n$，输出 $1+2+\\cdots+n$ 的和。请使用循环（`for` 或 `while`）来练习迭代，而不是只写一个公式（公式在数学上正确，但本题要练循环）。",
        "brief_en": "Read a positive integer $n$ and print the sum $1+2+\\cdots+n$. Use a loop (`for` or `while`) so that you practise iteration, not only the shortcut formula (the formula is mathematically fine, but this exercise is about loops).",
        "starter": "n = int(input())\ntotal = 0\n# use a loop to add 1..n\nprint(total)\n",
        "solution": "n = int(input())\ntotal = 0\nfor i in range(1, n + 1):\n    total = total + i\nprint(total)\n",
        "tests": [
            {"stdin": "5\n", "stdout": "15\n"},
            {"stdin": "1\n", "stdout": "1\n"},
            {"stdin": "10\n", "stdout": "55\n"},
        ],
    },
]

# ---------------------------------------------------------------------------
# Economics
# ---------------------------------------------------------------------------
KP_EC_SC_ZH = r"""
## 基本经济问题从“不够”开始

剑桥 IGCSE 经济（0455）**第 1 单元 The basic economic problem** 是八年级入门的核心。资源是有限的，人的欲望是无限的，于是必须作出选择。

## 要点

1. **稀缺（scarcity）**：有限的资源无法同时满足所有欲望。稀缺是相对的，即使富裕社会也存在稀缺。
2. **经济物品与自由物品**：经济物品是稀缺的、通常要用价格或代价才能获得；自由物品（如未被污染、未加限制的空气在某些情境下）不因稀缺而需要支付。课堂上要能举例，也要知道“自由物品”会随情境变化。
3. **生产要素**及其报酬：
   - **土地（land）**：自然资源 → 地租（rent）；
   - **劳动（labour）**：人的体力与脑力 → 工资（wages）；
   - **资本（capital）**：用于生产的人造资源（机器、厂房、工具）→ 利息（interest）；
   - **企业才能（enterprise）**：组织生产并承担风险 → 利润（profit）。
4. **机会成本**：作出选择时，**次优方案被放弃的价值**。选了课后篮球，就放弃了用同一段时间整理错题——机会成本是整理错题所能带来的收获。
5. **生产可能性曲线（PPC / PPG）**：
   - 曲线上的点：资源被充分利用时的最大产量组合；
   - 曲线内的点：资源未充分利用（失业、闲置）；
   - 曲线外的点：以现有资源无法达到；
   - 曲线外移：生产能力提高（技术进步、资源增加等）。

## 例题

一个学生晚自习只有 $2$ 小时，可以做数学练习或写英语作文。若把 $2$ 小时都用来做数学，机会成本是什么？

**解：** 机会成本是这 $2$ 小时本来可以完成的英语作文（次优用途），而不是“所有没做的事情”的总和，也不是数学练习本身。
"""

KP_EC_SC_EN = r"""
## The basic economic problem starts from “not enough”

Cambridge IGCSE Economics (0455) **Unit 1 The basic economic problem** is the heart of a Year 8 foundation. Resources are limited and wants are unlimited, so choices have to be made.

## Key points

1. **Scarcity** means limited resources cannot satisfy all wants at once. Scarcity is relative: it exists in rich societies too.
2. **Economic goods and free goods.** Economic goods are scarce and usually command a price or a cost. Free goods (for example clean air in some settings) are not scarce in that context. Be ready with examples, and notice that the classification can depend on the situation.
3. **Factors of production** and their rewards:
   - **land:** natural resources → rent;
   - **labour:** human effort, physical and mental → wages;
   - **capital:** man-made resources used in production (machines, buildings, tools) → interest;
   - **enterprise:** organising production and taking risks → profit.
4. **Opportunity cost** is the value of the **next-best alternative forgone**. If you choose basketball after school, you give up using the same time for your mistake book — that review is the opportunity cost.
5. **The production possibility curve (PPC):**
   - a point *on* the curve: the maximum combinations when resources are fully used;
   - a point *inside*: resources are not fully used (unemployment or idle capacity);
   - a point *outside*: unattainable with current resources;
   - an outward shift: productive capacity has grown (better technology, more resources, and so on).

## Worked example

A student has only two hours of evening study and can either practise mathematics or write an English composition. If both hours go to mathematics, what is the opportunity cost?

**Solution.** The opportunity cost is the English composition that could have been written in those two hours (the next-best use) — not the sum of every possible unused activity, and not the maths practice itself.
"""

KP_EC_DS_ZH = r"""
## 市场用价格来配置资源

**第 2 单元 The allocation of resources** 说明：在市场中，买者与卖者通过价格相互作用。八年级先抓住需求、供给与均衡。

## 要点

1. **需求（demand）**：在其他条件不变时（ceteris paribus），价格越高，需求量通常越低——需求曲线向右下倾斜。
2. **供给（supply）**：其他条件不变时，价格越高，供给量通常越高——供给曲线向右上倾斜。
3. **沿曲线移动与曲线移动**：
   - 价格变化 → 沿同一条需求或供给曲线移动（需求量 / 供给量变化）；
   - 非价格因素变化 → 整条曲线移动（需求 / 供给变化）。例如收入上升可能使正常商品的需求曲线右移；原料成本上升常使供给曲线左移。
4. **均衡**：需求量等于供给量时的价格与数量。
   - 价格高于均衡：过剩（surplus），价格有下降压力；
   - 价格低于均衡：短缺（shortage），价格有上升压力。
5. **弹性入门**：需求的价格弹性描述需求量对价格变化的敏感程度。八年级先建立“有的商品对价格更敏感”这一直觉，细算可放到后续。

## 例题

某校食堂三明治均衡价格为 $\$3$。若把价格暂时定在 $\$4$，且其他条件不变，市场上会出现过剩还是短缺？为什么？

**解：** 价格高于均衡，需求量减少、供给量增加，出现**过剩**。要出清市场，价格有下降的压力，直到供需再次相等。
"""

KP_EC_DS_EN = r"""
## Markets allocate resources through prices

**Unit 2 The allocation of resources** shows how buyers and sellers interact through price. At Year 8 foundation level, hold on to demand, supply and equilibrium.

## Key points

1. **Demand:** other things being equal (ceteris paribus), a higher price usually means a lower quantity demanded — the demand curve slopes down from left to right.
2. **Supply:** other things being equal, a higher price usually means a higher quantity supplied — the supply curve slopes up.
3. **Movement along a curve versus a shift of the curve:**
   - a change in price → a movement along the same demand or supply curve (change in quantity demanded or supplied);
   - a change in a non-price factor → a shift of the whole curve (change in demand or supply). For example, higher income may shift the demand for a normal good to the right; higher input costs often shift supply to the left.
4. **Equilibrium** is the price and quantity at which quantity demanded equals quantity supplied.
   - a price above equilibrium: a surplus, with downward pressure on price;
   - a price below equilibrium: a shortage, with upward pressure on price.
5. **Elasticity (introductory):** price elasticity of demand describes how responsive quantity demanded is to a price change. At Year 8 it is enough to build the idea that some goods are more price-sensitive than others; detailed calculation can come later.

## Worked example

The equilibrium price of a canteen sandwich is $\\$3$. If the price is temporarily set at $\\$4$, other things equal, is there a surplus or a shortage? Why?

**Solution.** The price is above equilibrium, so quantity demanded falls and quantity supplied rises: there is a **surplus**. To clear the market, price is under pressure to fall until the two quantities are equal again.
"""

questions_ec = [
    Q("q-ec-sc-01", "economics", "economics-1", "mcq",
      "稀缺指的是？",
      "Scarcity means that:",
      "b",
      "稀缺是指有限资源无法满足所有欲望，它推动人们作出选择。",
      "Scarcity means limited resources cannot satisfy all wants, which forces choices to be made.",
      opts(("所有物品的价格都为零", "every good has a price of zero"),
           ("有限的资源无法满足无限的欲望", "limited resources cannot satisfy unlimited wants"),
           ("只有贫穷国家才需要作选择", "only poor countries have to make choices"),
           ("资本不再是生产要素", "capital is no longer a factor of production")),
      knowledge_id="kp-economics-scarcity",
      published_at="2026-11-07T20:00:00+08:00"),
    Q("q-ec-sc-02", "economics", "economics-1", "short",
      "企业才能（enterprise）这一生产要素的报酬通常称为什么？",
      "What is the usual reward to the factor of production called enterprise?",
      "profit",
      "土地→地租，劳动→工资，资本→利息，企业才能→利润（profit）。",
      "Land → rent, labour → wages, capital → interest, enterprise → profit.",
      knowledge_id="kp-economics-scarcity",
      accepted=["profit", "profits", "利润", "profit (profit)"]),
    Q("q-ec-sc-03", "economics", "economics-1", "mcq",
      "一个学生把晚自习两小时全部用来做数学，而本来次优选择是写英语作文。机会成本是？",
      "A student uses both evening-study hours for mathematics; the next-best option was an English composition. The opportunity cost is:",
      "c",
      "机会成本是被放弃的次优方案：那篇英语作文，而不是“所有没做的事”，也不是数学练习本身。",
      "Opportunity cost is the next-best alternative forgone: the composition, not every unused activity, and not the maths itself.",
      opts(("数学练习本身", "the mathematics practice itself"),
           ("该生曾经想过的一切事情的总和", "the sum of everything the student has ever thought of doing"),
           ("被放弃的那篇英语作文", "the English composition that was given up"),
           ("零，因为学习没有成本", "zero, because study has no cost")),
      knowledge_id="kp-economics-scarcity"),
    Q("q-ec-ppc-01", "economics", "economics-1", "mcq",
      "生产可能性曲线内部的一点表示：",
      "A point inside a production possibility curve shows that:",
      "a",
      "曲线内的点表示资源未被充分利用，现有资源本可以生产得更多。",
      "A point inside the curve means resources are not fully used; more could be produced with current resources.",
      opts(("资源未被充分利用", "resources are not being used fully"),
           ("以现有资源不可能达到", "the combination is impossible with current resources"),
           ("一定已经达到最大出口", "exports must already be at a maximum"),
           ("机会成本为零且永远不变", "opportunity cost is zero and never changes")),
      knowledge_id="kp-economics-scarcity"),
    Q("q-ec-ds-01", "economics", "economics-2", "mcq",
      "在其他条件不变时，商品价格上升，通常会导致：",
      "Other things being equal, a rise in the price of a good usually leads to:",
      "b",
      "沿需求曲线向上移动，需求量下降（不是整条需求曲线一定向左移动）。",
      "There is a movement up the demand curve and a fall in quantity demanded (not automatically a leftward shift of the whole demand curve).",
      opts(("需求曲线一定向右移动", "an automatic rightward shift of the demand curve"),
           ("需求量下降", "a fall in quantity demanded"),
           ("供给量一定下降", "an automatic fall in quantity supplied"),
           ("均衡数量一定上升", "an automatic rise in equilibrium quantity")),
      knowledge_id="kp-economics-demand"),
    Q("q-ec-ds-02", "economics", "economics-2", "mcq",
      "若价格被定在均衡价格之上，市场通常会出现：",
      "If price is set above the equilibrium price, the market usually has:",
      "d",
      "价格偏高时，供给量大于需求量，出现过剩（surplus）。",
      "At a price above equilibrium, quantity supplied exceeds quantity demanded: a surplus.",
      opts(("短缺", "a shortage"),
           ("需求无穷大", "infinite demand"),
           ("供给为零", "zero supply"),
           ("过剩", "a surplus")),
      knowledge_id="kp-economics-demand",
      published_at="2026-11-07T20:10:00+08:00"),
    Q("q-ec-ds-03", "economics", "economics-2", "short",
      "原料成本上升，通常会使供给曲线向哪个方向移动？请回答“左”或 “left”。",
      "A rise in raw-material costs usually shifts the supply curve in which direction? Answer “left” or the Chinese equivalent.",
      "left",
      "成本上升，在每一价格上生产者愿意供给的数量减少，供给曲线向左移动。",
      "Higher costs mean less is supplied at each price, so the supply curve shifts to the left.",
      knowledge_id="kp-economics-demand",
      accepted=["left", "to the left", "leftward", "leftwards", "左", "向左", "左移", "向左移动"]),
    Q("q-ec-el-01", "economics", "economics-2", "mcq",
      "关于需求的价格弹性，八年级最恰当的理解是？",
      "Which is the most appropriate Year 8 understanding of price elasticity of demand?",
      "a",
      "它描述需求量对价格变化的敏感程度。有的商品更敏感，有的不那么敏感。",
      "It describes how responsive quantity demanded is to a change in price. Some goods are more sensitive than others.",
      opts(("它描述需求量对价格变化有多敏感", "It describes how sensitive quantity demanded is to a price change"),
           ("它等于政府的税率", "It is equal to the government’s tax rate"),
           ("它只用于描述天气", "It is used only to describe the weather"),
           ("它表示企业永远不应改变价格", "It means a firm should never change price")),
      knowledge_id="kp-economics-demand"),
    Q("q-ec-mac-01", "economics", "economics-4", "mcq",
      "通货膨胀指的是？",
      "Inflation refers to:",
      "c",
      "通货膨胀是一般物价水平的持续上升，从而降低货币的购买力。单个商品涨价不一定等于通货膨胀。",
      "Inflation is a sustained rise in the general price level, which reduces the purchasing power of money. A rise in one price is not automatically inflation.",
      opts(("一种商品一次偶然降价", "a one-off fall in the price of a single good"),
           ("人口在一年内减少", "a fall in population in a single year"),
           ("一般物价水平持续上升", "a sustained rise in the general price level"),
           ("失业率恰好为零", "unemployment exactly equal to zero"))),
    Q("q-ec-tr-01", "economics", "economics-6", "mcq",
      "国际贸易中“专业化”的主要好处是？",
      "A main benefit of specialisation in international trade is that countries can:",
      "b",
      "专业化使各国把资源集中在相对更擅长的生产上，再通过贸易获得更丰富的商品组合。",
      "Specialisation lets countries concentrate on what they are relatively better at producing, then trade for a wider mix of goods.",
      opts(("完全不需要任何资源", "do without any resources at all"),
           ("集中生产相对擅长的产品并通过贸易获益", "concentrate on what they are relatively better at and gain from trade"),
           ("自动取消一切机会成本", "cancel all opportunity cost automatically"),
           ("保证贸易限制永远是最好的政策", "guarantee that trade restrictions are always the best policy"))),
]

knowledge_ec = [
    KP("kp-economics-scarcity", "economics", "economics-1", "economics-1-1",
       "稀缺、生产要素与机会成本",
       "Scarcity, factors of production and opportunity cost",
       KP_EC_SC_ZH, KP_EC_SC_EN,
       ["q-ec-sc-01", "q-ec-sc-02", "q-ec-sc-03", "q-ec-ppc-01"],
       "2026-11-07T20:00:00+08:00",
       "资源有限、欲望无限，选择就会产生机会成本；PPC 帮助我们看见权衡。",
       "Limited resources and unlimited wants force choices and opportunity cost; the PPC makes the trade-off visible."),
    KP("kp-economics-demand", "economics", "economics-2", "economics-2-2",
       "需求、供给与市场均衡",
       "Demand, supply and market equilibrium",
       KP_EC_DS_ZH, KP_EC_DS_EN,
       ["q-ec-ds-01", "q-ec-ds-02", "q-ec-ds-03", "q-ec-el-01"],
       "2026-10-11T10:00:00+08:00",
       "价格变化沿曲线移动；非价格因素使曲线移动。均衡时需求量等于供给量。",
       "Price changes cause movements along a curve; non-price factors shift the curve. At equilibrium, quantity demanded equals quantity supplied."),
]

sets_ec = [
    SET("practice-economics-foundation", "economics", "economics-1", "practice",
        "练习组 · 稀缺与市场入门",
        "Practice set · Scarcity and markets",
        ["q-ec-sc-01", "q-ec-sc-02", "q-ec-sc-03", "q-ec-ds-01", "q-ec-ds-02", "q-ec-ppc-01"],
        published_at="2026-11-07T21:00:00+08:00"),
    SET("paper-economics-a", "economics", "economics-1", "paper",
        "本站练习卷 A · IGCSE 经济入门",
        "Practice Paper A · IGCSE economics foundation",
        ["q-ec-sc-01", "q-ec-sc-02", "q-ec-sc-03", "q-ec-ppc-01", "q-ec-ds-01",
         "q-ec-ds-02", "q-ec-ds-03", "q-ec-el-01", "q-ec-mac-01", "q-ec-tr-01"],
        time_limit=25, published_at="2026-10-20T09:00:00+08:00"),
]
