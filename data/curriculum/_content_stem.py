"""Mathematics, sciences and related sample content."""
from _helpers import Q, KP, SET, opts

# ---------------------------------------------------------------------------
# Mathematics
# ---------------------------------------------------------------------------
KP_MA_IND_ZH = r"""
## 指数在说什么？

第 8 阶段数学 **单元 8.1** 要求使用正整数指数与零指数，并掌握乘除的指数律。$a^n$ 表示 $n$ 个 $a$ 相乘。例如 $2^5 = 2\times 2\times 2\times 2\times 2 = 32$。

## 要点

1. **乘除指数律**（底数相同）：
   - $a^m \times a^n = a^{m+n}$
   - $a^m \div a^n = a^{m-n}$（$a \neq 0$）
2. **零指数**：$a^0 = 1$（$a \neq 0$）。
3. **运算顺序**：括号、指数（含平方根与立方根）、乘除、加减。
4. **平方与立方**：能识别正负平方数与立方数，并求对应的平方根、立方根。注意 $(-3)^2 = 9$，但 $-3^2 = -9$。
5. **因数与倍数**：
   - 质因数分解把一个整数写成质数的乘积，例如 $24 = 2^3 \times 3$。
   - **最高公倍数（HCF）** 取各质因数的最低次幂。
   - **最小公倍数（LCM）** 取各质因数的最高次幂。

## 例题

计算 $2^5 \times 2^3$，并求 $24$ 与 $36$ 的 HCF 与 LCM。

**解：**

$$2^5 \times 2^3 = 2^{5+3} = 2^8 = 256$$

$$24 = 2^3 \times 3,\quad 36 = 2^2 \times 3^2$$

$$\operatorname{HCF}(24,36) = 2^2 \times 3 = 12$$

$$\operatorname{LCM}(24,36) = 2^3 \times 3^2 = 8 \times 9 = 72$$

检验：$\operatorname{HCF}\times\operatorname{LCM} = 12\times 72 = 864$，且 $24\times 36 = 864$，两者一致。
"""

KP_MA_IND_EN = r"""
## What an index is saying

Stage 8 Mathematics **Unit 8.1** uses positive and zero indices and the index laws for multiplication and division. $a^n$ means $n$ factors of $a$. For example $2^5 = 2\times 2\times 2\times 2\times 2 = 32$.

## Key points

1. **Index laws** (same base):
   - $a^m \times a^n = a^{m+n}$
   - $a^m \div a^n = a^{m-n}$ ($a \neq 0$)
2. **Zero index:** $a^0 = 1$ ($a \neq 0$).
3. **Order of operations:** brackets, indices (including square and cube roots), then multiply and divide, then add and subtract.
4. **Squares and cubes:** recognise square and cube numbers, including negatives where they exist, and the corresponding roots. Note that $(-3)^2 = 9$ but $-3^2 = -9$.
5. **Factors and multiples:**
   - Prime factorisation writes a whole number as a product of primes, e.g. $24 = 2^3 \times 3$.
   - The **highest common factor (HCF)** takes the lowest power of each shared prime.
   - The **lowest common multiple (LCM)** takes the highest power of each prime that appears.

## Worked example

Evaluate $2^5 \times 2^3$, and find the HCF and LCM of $24$ and $36$.

**Solution**

$$2^5 \times 2^3 = 2^{5+3} = 2^8 = 256$$

$$24 = 2^3 \times 3,\quad 36 = 2^2 \times 3^2$$

$$\operatorname{HCF}(24,36) = 2^2 \times 3 = 12$$

$$\operatorname{LCM}(24,36) = 2^3 \times 3^2 = 8 \times 9 = 72$$

Check: $\operatorname{HCF}\times\operatorname{LCM} = 12\times 72 = 864$, and $24\times 36 = 864$.
"""

KP_MA_EQ_ZH = r"""
## 方程是在找未知数的值

**单元 8.2** 关注代数变形、方程与不等式。解方程时，两边做**同样**的运算，以保持相等。

## 要点

1. **整理**：先展开括号，再合并同类项。
2. **未知数移到一边，常数移到另一边**。移动加减项时变号。
3. **两边除以未知数的系数**，得到 $x$ 的值。
4. **两边都有未知数**时，先把含 $x$ 的项集中。例如 $3x-5=2x+7$。
5. **检验**：把答案代回原方程。
6. **不等式**（如 $2x+3>11$）解法与方程类似，但：
   - 解集往往是一个范围，例如 $x>4$；
   - **两边乘或除以负数时，不等号必须反向**。
7. **数轴表示**：空心圆表示不包含该点（$>$ 或 $<$），实心圆表示包含（$\geq$ 或 $\leq$）。

## 例题

解方程 $3x-5=2x+7$，再解不等式 $5-2x \leq 11$。

**解方程：**

$$
\begin{aligned}
3x-5 &= 2x+7 \\
3x-2x &= 7+5 \\
x &= 12
\end{aligned}
$$

检验：$3\times 12-5=31$，$2\times 12+7=31$。两边相等。

**解不等式：**

$$
\begin{aligned}
5-2x &\leq 11 \\
-2x &\leq 6 \\
x &\geq -3
\end{aligned}
$$

最后一步两边除以 $-2$，不等号由 $\leq$ 变为 $\geq$。
"""

KP_MA_EQ_EN = r"""
## An equation asks for the value of an unknown

**Unit 8.2** covers algebraic manipulation, equations and inequalities. Whatever you do to one side of an equation, do the same to the other, so that equality is kept.

## Key points

1. **Tidy first:** expand brackets, then collect like terms.
2. **Collect the unknown on one side and constants on the other.** Addition or subtraction changes sign when a term moves.
3. **Divide both sides by the coefficient** of the unknown.
4. **When the unknown appears on both sides,** collect those terms first. Example: $3x-5=2x+7$.
5. **Check** by substituting back into the original equation.
6. **Inequalities** such as $2x+3>11$ are solved in a similar way, with two extra cares:
   - the solution is usually a range, e.g. $x>4$;
   - **if you multiply or divide both sides by a negative number, reverse the inequality sign.**
7. **On a number line:** an open circle means the end point is not included ($>$ or $<$); a filled circle means it is included ($\geq$ or $\leq$).

## Worked example

Solve $3x-5=2x+7$, then solve $5-2x \leq 11$.

**Equation**

$$
\begin{aligned}
3x-5 &= 2x+7 \\
3x-2x &= 7+5 \\
x &= 12
\end{aligned}
$$

Check: $3\times 12-5=31$ and $2\times 12+7=31$.

**Inequality**

$$
\begin{aligned}
5-2x &\leq 11 \\
-2x &\leq 6 \\
x &\geq -3
\end{aligned}
$$

In the last step both sides were divided by $-2$, so $\leq$ became $\geq$.
"""

questions_ma = [
    Q("q-ma-ind-01", "mathematics", "mathematics-8-1", "numeric",
      "计算 $2^5 \\times 2^3$。",
      "Evaluate $2^5 \\times 2^3$.",
      "256",
      "底数相同则指数相加：$2^{5+3}=2^8=256$。",
      "Add the indices when the base is the same: $2^{5+3}=2^8=256$.",
      knowledge_id="kp-mathematics-indices", tolerance=0,
      published_at="2026-11-10T15:00:00+08:00"),
    Q("q-ma-ind-02", "mathematics", "mathematics-8-1", "numeric",
      "$24$ 与 $36$ 的最高公因数（HCF）是多少？",
      "What is the highest common factor (HCF) of $24$ and $36$?",
      "12",
      "$24=2^3\\times 3$，$36=2^2\\times 3^2$，最低次幂相乘得 $2^2\\times 3=12$。",
      "$24=2^3\\times 3$ and $36=2^2\\times 3^2$. The lowest powers give $2^2\\times 3=12$.",
      knowledge_id="kp-mathematics-indices", tolerance=0),
    Q("q-ma-ind-03", "mathematics", "mathematics-8-1", "numeric",
      "$24$ 与 $36$ 的最小公倍数（LCM）是多少？",
      "What is the lowest common multiple (LCM) of $24$ and $36$?",
      "72",
      "最高次幂相乘：$2^3\\times 3^2=8\\times 9=72$。",
      "The highest powers give $2^3\\times 3^2=8\\times 9=72$.",
      knowledge_id="kp-mathematics-indices", tolerance=0),
    Q("q-ma-ind-04", "mathematics", "mathematics-8-1", "mcq",
      "若 $a\\neq 0$，则 $a^0$ 等于？",
      "If $a\\neq 0$, what is $a^0$?",
      "b",
      "任何非零数的零次幂等于 $1$。",
      "Any non-zero number to the power zero equals $1$.",
      opts(("$0$", "$0$"), ("$1$", "$1$"), ("$a$", "$a$"), ("未定义", "Undefined")),
      knowledge_id="kp-mathematics-indices"),
    Q("q-ma-eq-01", "mathematics", "mathematics-8-2", "numeric",
      "解方程 $3x-5=2x+7$，求 $x$。",
      "Solve $3x-5=2x+7$. Find $x$.",
      "12",
      "两边减去 $2x$ 再加 $5$，得 $x=12$。检验：$3\\times 12-5=31$，$2\\times 12+7=31$。",
      "Subtract $2x$ and add $5$ to both sides to obtain $x=12$. Check: both sides equal $31$.",
      knowledge_id="kp-mathematics-equations", tolerance=0,
      published_at="2026-11-10T15:10:00+08:00"),
    Q("q-ma-eq-02", "mathematics", "mathematics-8-2", "mcq",
      "解不等式 $5-2x\\leq 11$ 时，两边除以 $-2$ 以后，正确的结果是？",
      "When solving $5-2x\\leq 11$, what is the correct result after dividing by $-2$?",
      "c",
      "先得 $-2x\\leq 6$。两边除以负数，不等号反向，故 $x\\geq -3$。",
      "You reach $-2x\\leq 6$. Dividing by a negative reverses the sign, so $x\\geq -3$.",
      opts(("$x\\leq -3$", "$x\\leq -3$"),
           ("$x\\leq 3$", "$x\\leq 3$"),
           ("$x\\geq -3$", "$x\\geq -3$"),
           ("$x\\geq 3$", "$x\\geq 3$")),
      knowledge_id="kp-mathematics-equations"),
    Q("q-ma-eq-03", "mathematics", "mathematics-8-2", "numeric",
      "解方程 $4(x-1)=2x+10$，求 $x$。",
      "Solve $4(x-1)=2x+10$. Find $x$.",
      "7",
      "展开得 $4x-4=2x+10$，$2x=14$，$x=7$。",
      "Expand: $4x-4=2x+10$, so $2x=14$ and $x=7$.",
      knowledge_id="kp-mathematics-equations", tolerance=0),
    Q("q-ma-frac-01", "mathematics", "mathematics-8-4", "numeric",
      "一件原价 $\\$80$ 的夹克降价 $15\\%$。现价是多少美元？（只写数字）",
      "A jacket priced at $\\$80$ is reduced by $15\\%$. What is the new price in dollars? (number only)",
      "68",
      "现价是原价的 $85\\%$：$80\\times 0.85=68$。或先算减少量 $80\\times 0.15=12$，再 $80-12=68$。",
      "The new price is $85\\%$ of $80$: $80\\times 0.85=68$. Alternatively, the reduction is $12$, and $80-12=68$.",
      tolerance=0.01),
    Q("q-ma-circ-01", "mathematics", "mathematics-8-3", "numeric",
      "圆的半径是 $7\\ \\text{cm}$。若取 $\\pi=\\dfrac{22}{7}$，周长是多少厘米？",
      "A circle has radius $7\\ \\text{cm}$. Using $\\pi=\\dfrac{22}{7}$, what is the circumference in centimetres?",
      "44",
      "周长 $C=2\\pi r=2\\times\\dfrac{22}{7}\\times 7=44$。",
      "Circumference $C=2\\pi r=2\\times\\dfrac{22}{7}\\times 7=44$.",
      tolerance=0.05),
    Q("q-ma-prob-01", "mathematics", "mathematics-8-5", "numeric",
      "一枚公平骰子掷出“大于 $4$”的理论概率是多少？请用最简分数作答。",
      "A fair ordinary die is rolled. What is the theoretical probability of a score greater than $4$? Give a fraction in lowest terms.",
      "1/3",
      "大于 $4$ 的结果是 $5$ 和 $6$，共 $2$ 个，总共 $6$ 个等可能结果，故 $\\dfrac{2}{6}=\\dfrac{1}{3}$。小数 $0.333\\ldots$ 也可。",
      "The favourable outcomes are $5$ and $6$, so $\\dfrac{2}{6}=\\dfrac{1}{3}$.",
      tolerance=0.01),
    Q("q-ma-seq-01", "mathematics", "mathematics-8-7", "numeric",
      "一个等差数列的第 $n$ 项是 $3n+1$。第 $10$ 项是多少？",
      "The $n$th term of a sequence is $3n+1$. What is the 10th term?",
      "31",
      "把 $n=10$ 代入：$3\\times 10+1=31$。",
      "Substitute $n=10$: $3\\times 10+1=31$.",
      tolerance=0),
    Q("q-ma-stat-01", "mathematics", "mathematics-8-9", "numeric",
      "一组数据为 $2, 5, 5, 6, 12$。这组数据的中位数是多少？",
      "The data set is $2, 5, 5, 6, 12$. What is the median?",
      "5",
      "五个数已按大小排列，正中间（第 3 个）是 $5$。注意众数也是 $5$，但本题问的是中位数。",
      "Five values in order: the middle (3rd) value is $5$.",
      tolerance=0),
]

knowledge_ma = [
    KP("kp-mathematics-indices", "mathematics", "mathematics-8-1", "mathematics-8-1-2",
       "指数律、质因数、HCF 与 LCM",
       "Index laws, prime factors, HCF and LCM",
       KP_MA_IND_ZH, KP_MA_IND_EN,
       ["q-ma-ind-01", "q-ma-ind-02", "q-ma-ind-03", "q-ma-ind-04"],
       "2026-11-10T15:00:00+08:00",
       "同底数乘加指、除减指；用质因数取最低或最高次幂求 HCF 与 LCM。",
       "Multiply by adding indices, divide by subtracting; use prime factors to find HCF and LCM."),
    KP("kp-mathematics-equations", "mathematics", "mathematics-8-2", "mathematics-8-2-2",
       "一元方程与不等式",
       "Linear equations and inequalities",
       KP_MA_EQ_ZH, KP_MA_EQ_EN,
       ["q-ma-eq-01", "q-ma-eq-02", "q-ma-eq-03"],
       "2026-10-18T10:00:00+08:00",
       "两边做同样运算；乘除负数时，不等号要反向。",
       "Do the same to both sides; reverse the inequality if you multiply or divide by a negative."),
]

sets_ma = [
    SET("practice-mathematics-number-algebra", "mathematics", "mathematics-8-1", "practice",
        "练习组 · 指数与方程",
        "Practice set · Indices and equations",
        ["q-ma-ind-01", "q-ma-ind-04", "q-ma-ind-02", "q-ma-eq-01", "q-ma-eq-02", "q-ma-frac-01"],
        published_at="2026-11-10T16:00:00+08:00"),
    SET("paper-mathematics-a", "mathematics", "mathematics-8-1", "paper",
        "本站练习卷 A · 数与代数",
        "Practice Paper A · Number and algebra",
        ["q-ma-ind-01", "q-ma-ind-02", "q-ma-ind-03", "q-ma-ind-04", "q-ma-eq-01",
         "q-ma-eq-02", "q-ma-eq-03", "q-ma-frac-01", "q-ma-prob-01", "q-ma-seq-01"],
        time_limit=30, published_at="2026-10-25T09:00:00+08:00"),
]

# ---------------------------------------------------------------------------
# Physics
# ---------------------------------------------------------------------------
KP_PH_SP_ZH = r"""
## 速度把路程与时间联系起来

第 8 阶段科学物理部分要求会计算速度，并会绘制、解释简单的路程—时间图像：

$$v = \frac{s}{t}$$

其中 $v$ 是速度，$s$ 是路程（距离），$t$ 是时间。常用单位是 $\text{m/s}$ 或 $\text{km/h}$。

## 要点

1. **统一单位**：若路程是千米、时间是小时，速度就是 $\text{km/h}$。把 $72\\ \\text{km/h}$ 换成 $\text{m/s}$：先乘 $1000$，再除以 $3600$，即除以 $3.6$，得 $20\\ \\text{m/s}$。
2. **路程—时间图像**：
   - 图像的**斜率（坡度）表示速度**；
   - 水平线段表示静止（速度为 $0$）；
   - 更陡的直线表示更大的恒定速度；
   - 回到出发点时，路程是累计走过的距离，位移则可能为零——第 8 阶段课图通常把纵轴标为 distance（路程）。
3. **平衡力与运动**：平衡力（合力为零）时，物体保持静止或匀速直线运动；非平衡力会改变速度（加速、减速或转向）。

## 例题

一辆自行车 $10$ 秒内前进 $150\\ \\text{m}$，速度是多少？若后 $5$ 秒它停在原地，这段在路程—时间图像上是什么样子？

**解：**

$$v = \frac{150}{10} = 15\\ \\text{m/s}$$

后 $5$ 秒路程不再增加，图像是一段水平线。前 $10$ 秒则是一条向上的直线，斜率等于 $15\\ \\text{m/s}$。
"""

KP_PH_SP_EN = r"""
## Speed links distance and time

Stage 8 Physics requires you to calculate speed and to draw and interpret simple distance–time graphs:

$$v = \frac{s}{t}$$

where $v$ is speed, $s$ is distance and $t$ is time. Common units are $\text{m/s}$ or $\text{km/h}$.

## Key points

1. **Keep units consistent.** If distance is in kilometres and time in hours, speed is in $\text{km/h}$. To change $72\\ \\text{km/h}$ into $\text{m/s}$, multiply by $1000$ and divide by $3600$ (that is, divide by $3.6$) to get $20\\ \\text{m/s}$.
2. **On a distance–time graph:**
   - the **gradient (slope) is the speed**;
   - a horizontal segment means the object is stationary (speed $0$);
   - a steeper straight line means a greater constant speed;
   - Stage 8 graphs usually plot distance (the length travelled), not displacement.
3. **Balanced forces and motion.** When forces are balanced (resultant zero), an object stays at rest or keeps a steady speed in a straight line. Unbalanced forces change the velocity (speed up, slow down or change direction).

## Worked example

A bicycle travels $150\\ \\text{m}$ in $10\\ \\text{s}$. What is its speed? If it then stays still for $5\\ \\text{s}$, what does that look like on a distance–time graph?

**Solution**

$$v = \frac{150}{10} = 15\\ \\text{m/s}$$

In the next $5\\ \\text{s}$ the distance does not increase, so the graph is a horizontal line. The first $10\\ \\text{s}$ is an upward straight line with gradient $15\\ \\text{m/s}$.
"""

KP_PH_REF_ZH = r"""
## 反射定律

光线射到光滑平面（如平面镜）时会发生反射。第 8 阶段要求描述平面反射，并使用反射定律。

## 要点

1. 先画**法线**：过入射点、垂直于镜面的虚线。
2. **入射角 $i$**：入射光线与法线的夹角（不是与镜面的夹角）。
3. **反射角 $r$**：反射光线与法线的夹角。
4. **反射定律**：$i = r$。入射光线、法线、反射光线在同一平面内。
5. 平面镜成的像是**正立、等大、看起来在镜后**的虚像，物距等于像距。

## 例题

一束光以与镜面成 $30^\\circ$ 的方向射向平面镜。入射角是多少？反射角是多少？

**解：** 法线垂直于镜面，所以入射角是 $90^\\circ-30^\\circ=60^\\circ$。由反射定律，反射角也是 $60^\\circ$。反射光线与镜面的夹角同样是 $30^\\circ$。

常见错误：把“与镜面的夹角”当成入射角。
"""

KP_PH_REF_EN = r"""
## The law of reflection

Light reflects when it meets a smooth plane surface such as a plane mirror. Stage 8 asks you to describe reflection at a plane surface and to use the law of reflection.

## Key points

1. Draw the **normal** first: a dashed line through the point of incidence, perpendicular to the mirror.
2. The **angle of incidence $i$** is the angle between the incident ray and the normal (not the angle with the mirror).
3. The **angle of reflection $r$** is the angle between the reflected ray and the normal.
4. **The law of reflection:** $i = r$. The incident ray, the normal and the reflected ray lie in the same plane.
5. The image in a plane mirror is **upright, the same size, and virtual** (it appears behind the mirror). Object distance equals image distance.

## Worked example

A ray meets a plane mirror at $30^\\circ$ to the surface of the mirror. What is the angle of incidence? What is the angle of reflection?

**Solution.** The normal is perpendicular to the mirror, so $i = 90^\\circ-30^\\circ=60^\\circ$. By the law of reflection, $r=60^\\circ$ as well. The reflected ray also makes $30^\\circ$ with the mirror.

A common error is to treat the angle with the mirror as the angle of incidence.
"""

questions_ph = [
    Q("q-ph-sp-01", "physics", "physics-8Pf", "numeric",
      "一辆自行车在 $10\\ \\text{s}$ 内前进 $150\\ \\text{m}$。速度是多少 $\\text{m/s}$？",
      "A bicycle travels $150\\ \\text{m}$ in $10\\ \\text{s}$. What is its speed in $\\text{m/s}$?",
      "15",
      "使用 $v=s/t=150/10=15\\ \\text{m/s}$。",
      "Use $v=s/t=150/10=15\\ \\text{m/s}$.",
      knowledge_id="kp-physics-speed", tolerance=0.01,
      published_at="2026-11-09T14:00:00+08:00"),
    Q("q-ph-sp-02", "physics", "physics-8Pf", "numeric",
      "把 $72\\ \\text{km/h}$ 换算成 $\\text{m/s}$。",
      "Convert $72\\ \\text{km/h}$ into $\\text{m/s}$.",
      "20",
      "$72\\times 1000 \\div 3600 = 72\\div 3.6 = 20\\ \\text{m/s}$。",
      "$72\\times 1000 \\div 3600 = 72\\div 3.6 = 20\\ \\text{m/s}$.",
      knowledge_id="kp-physics-speed", tolerance=0.01),
    Q("q-ph-sp-03", "physics", "physics-8Pf", "mcq",
      "在路程—时间图像上，一段水平直线表示什么？",
      "On a distance–time graph, what does a horizontal straight section show?",
      "b",
      "路程不随时间增加，物体静止，速度为零。",
      "Distance is not increasing, so the object is stationary and the speed is zero.",
      opts(("物体在加速", "The object is accelerating"),
           ("物体静止", "The object is stationary"),
           ("物体在反向运动", "The object is moving backwards"),
           ("速度正在均匀增大", "The speed is increasing steadily")),
      knowledge_id="kp-physics-speed"),
    Q("q-ph-ref-01", "physics", "physics-8Ps", "numeric",
      "光线与平面镜镜面的夹角为 $30^\\circ$。入射角是多少度？（只写数字）",
      "A ray meets a plane mirror at $30^\\circ$ to the surface. What is the angle of incidence in degrees? (number only)",
      "60",
      "入射角从法线量起：$90-30=60$。",
      "The angle of incidence is measured from the normal: $90-30=60$.",
      knowledge_id="kp-physics-reflection", tolerance=0),
    Q("q-ph-ref-02", "physics", "physics-8Ps", "mcq",
      "反射定律指出：",
      "The law of reflection states that:",
      "a",
      "入射角等于反射角，两者都从法线量起。",
      "The angle of incidence equals the angle of reflection, both measured from the normal.",
      opts(("入射角等于反射角", "the angle of incidence equals the angle of reflection"),
           ("入射角等于光线与镜面的夹角", "the angle of incidence equals the angle with the mirror"),
           ("反射光线一定沿法线射出", "the reflected ray always leaves along the normal"),
           ("只有彩色光才反射", "only coloured light is reflected")),
      knowledge_id="kp-physics-reflection"),
    Q("q-ph-mom-01", "physics", "physics-8Pf", "numeric",
      "一个大小为 $12\\ \\text{N}$ 的力，垂直力臂为 $0.5\\ \\text{m}$。力矩是多少 $\\text{N m}$？",
      "A force of $12\\ \\text{N}$ has a perpendicular distance of $0.5\\ \\text{m}$ from the pivot. What is the moment in $\\text{N m}$?",
      "6",
      "力矩 $M=F\\times d=12\\times 0.5=6\\ \\text{N m}$。",
      "Moment $M=F\\times d=12\\times 0.5=6\\ \\text{N m}$.",
      tolerance=0.01),
    Q("q-ph-pr-01", "physics", "physics-8Pf", "numeric",
      "一个 $20\\ \\text{N}$ 的力作用在 $4\\ \\text{m}^2$ 的面积上。压强是多少 $\\text{N/m}^2$？",
      "A force of $20\\ \\text{N}$ acts on an area of $4\\ \\text{m}^2$. What is the pressure in $\\text{N/m}^2$?",
      "5",
      "压强 $p=F/A=20/4=5\\ \\text{N/m}^2$。",
      "Pressure $p=F/A=20/4=5\\ \\text{N/m}^2$.",
      tolerance=0.01),
    Q("q-ph-mag-01", "physics", "physics-8Pe", "mcq",
      "关于电磁铁，下列哪一项是正确的？",
      "Which statement about an electromagnet is correct?",
      "c",
      "电磁铁由绕在铁芯上的线圈通电形成，可通过改变电流、匝数等调节强弱，并能开关。",
      "An electromagnet is a coil (often on an iron core) that becomes magnetic when current flows. Its strength can be changed, and it can be switched off.",
      opts(("一旦做成，磁场永远无法关闭", "Once made, its magnetic field can never be switched off"),
           ("它不需要电流", "It does not need an electric current"),
           ("通电线圈可产生磁场，并常绕在铁芯上", "A current-carrying coil produces a field, often wound on an iron core"),
           ("电磁铁只能排斥、不能吸引", "An electromagnet can only repel, never attract"))),
    Q("q-ph-es-01", "physics", "physics-8ES", "mcq",
      "地球具有磁场，主要是因为：",
      "The Earth has a magnetic field mainly because:",
      "b",
      "第 8 阶段要求知道：地核的作用使地球像一块磁铁，从而具有磁场。",
      "Stage 8 requires the idea that the Earth’s core acts as a magnet, which is why Earth has a magnetic field.",
      opts(("地表全被铁矿覆盖", "the surface is entirely covered with iron ore"),
           ("地核起着磁体的作用", "the core acts as a magnet"),
           ("月球反射阳光", "the Moon reflects sunlight"),
           ("大气中氮气占 $78\\%$", "the atmosphere is $78\\%$ nitrogen"))),
    Q("q-ph-light-01", "physics", "physics-8Ps", "mcq",
      "白光通过三棱镜后展开成彩色光谱，这一现象称为？",
      "White light is spread into a spectrum of colours by a prism. What is this called?",
      "d",
      "这是色散（dispersion）：白光由多种色光组成。",
      "This is dispersion: white light is made of many colours.",
      opts(("反射", "Reflection"),
           ("衍射", "Diffraction"),
           ("蒸发", "Evaporation"),
           ("色散", "Dispersion"))),
]

knowledge_ph = [
    KP("kp-physics-speed", "physics", "physics-8Pf", "physics-8Pf-1",
       "速度与路程—时间图像",
       "Speed and distance–time graphs",
       KP_PH_SP_ZH, KP_PH_SP_EN,
       ["q-ph-sp-01", "q-ph-sp-02", "q-ph-sp-03"],
       "2026-11-09T14:00:00+08:00",
       "速度等于路程除以时间；图像的斜率表示速度，水平段表示静止。",
       "Speed is distance divided by time; the gradient of the graph is speed, and a horizontal line means stationary."),
    KP("kp-physics-reflection", "physics", "physics-8Ps", "physics-8Ps-1",
       "平面反射与反射定律",
       "Reflection at a plane surface and the law of reflection",
       KP_PH_REF_ZH, KP_PH_REF_EN,
       ["q-ph-ref-01", "q-ph-ref-02"],
       "2026-10-16T10:00:00+08:00",
       "入射角与反射角都从法线量起，并且相等。",
       "Angles of incidence and reflection are measured from the normal and are equal."),
]

sets_ph = [
    SET("practice-physics-motion-light", "physics", "physics-8Pf", "practice",
        "练习组 · 运动与反射",
        "Practice set · Motion and reflection",
        ["q-ph-sp-01", "q-ph-sp-02", "q-ph-sp-03", "q-ph-ref-01", "q-ph-ref-02", "q-ph-mom-01"],
        published_at="2026-11-09T15:00:00+08:00"),
    SET("paper-physics-a", "physics", "physics-8Pf", "paper",
        "本站练习卷 A · 力、运动与光",
        "Practice Paper A · Forces, motion and light",
        ["q-ph-sp-01", "q-ph-sp-02", "q-ph-sp-03", "q-ph-mom-01", "q-ph-pr-01",
         "q-ph-ref-01", "q-ph-ref-02", "q-ph-light-01", "q-ph-mag-01", "q-ph-es-01"],
        time_limit=25, published_at="2026-10-24T09:00:00+08:00"),
]

# ---------------------------------------------------------------------------
# Chemistry
# ---------------------------------------------------------------------------
KP_CH_AT_ZH = r"""
## 卢瑟福如何改写原子图像

第 8 阶段化学要求描述**卢瑟福原子模型**，并知道质子、中子、电子的电荷。

在卢瑟福指导的金箔实验（盖革—马斯登实验）中，一束正电的 $\alpha$ 粒子射向很薄的金箔：

- **绝大多数**粒子几乎沿直线穿过，说明原子内部大部分是空的；
- **少数**发生偏转，极少数甚至被弹回，说明原子中心有一个**体积很小、质量很大、带正电的核**。

卢瑟福据此提出：原子由中心的正电核与周围的电子组成。后来人们确认核内还有**中子**（不带电）。第 8 阶段把这些电荷关系一并掌握即可。

## 要点

1. **电荷**：$\\text{电子为负}$，$\\text{质子为正}$，$\\text{中子不带电}$。
2. 在中性原子中，质子数等于电子数。
3. **静电引力**：正电荷与负电荷相互吸引，这是把单个原子约束在一起的力（核吸引电子）。
4. 原子的质量几乎集中在核上；电子质量很小。

## 模型的限度

卢瑟福模型成功解释了散射结果，但并未完整说明电子如何排布。科学模型会随证据更新，这正是“思考与科学工作方式”所强调的。
"""

KP_CH_AT_EN = r"""
## How Rutherford changed the picture of the atom

Stage 8 Chemistry asks you to describe the **Rutherford model** of the atom and to know the charges of the proton, neutron and electron.

In the gold-foil experiment (Geiger–Marsden), directed by Rutherford, a beam of positively charged $\alpha$ particles was fired at a very thin gold foil:

- **Most** particles went almost straight through, so most of the atom is empty space;
- **A few** were deflected, and a very small number bounced back, so the centre of the atom contains a **tiny, massive, positively charged nucleus**.

Rutherford proposed a positive nucleus with electrons around it. Neutrons (with no charge) were later identified in the nucleus. Stage 8 expects you to know these charge relationships together.

## Key points

1. **Charges:** electrons are negative, protons are positive, neutrons have no charge.
2. In a neutral atom, the number of protons equals the number of electrons.
3. **Electrostatic attraction** between positive and negative charge is what holds an individual atom together (the nucleus attracts the electrons).
4. Almost all of the atom’s mass is in the nucleus; electrons have very small mass.

## A limit of the model

The Rutherford model explains the scattering results but does not give a full account of how electrons are arranged. Scientific models change as evidence grows — a point emphasised in Thinking and Working Scientifically.
"""

KP_CH_TH_ZH = r"""
## 反应会吸热，也会放热

第 8 阶段要求：用**文字方程式**描述反应；并知道有些过程是**放热（exothermic）**或**吸热（endothermic）**，可借温度变化来识别。

## 要点

1. **文字方程式**按“反应物 → 生成物”来写，状态有时会注明，但本阶段先写对物质名称。
   - 例如：镁 + 氧气 → 氧化镁
2. **放热过程**：把能量释放给周围，周围温度**上升**。常见例子：燃烧、许多中和反应、呼吸作用。
3. **吸热过程**：从周围吸收能量，周围温度**下降**。常见例子：某些盐的溶解、热分解反应、光合作用。
4. 判断时看的是**周围环境**的温度，而不是“系统内部感觉”。
5. 反应不一定得到单一纯净产物，有时会得到混合物，需要分离。
6. 有些物质在一般条件下很难反应，可称为**惰性（inert）**，例如常温下的金。

## 例题

氢氧化镁用于中和过多胃酸（盐酸）。写出文字方程式，并判断该中和通常是放热还是吸热。

**解：**

盐酸 + 氢氧化镁 → 氯化镁 + 水

许多中和反应是放热的：若在烧杯中进行，混合物温度通常会升高。课堂上应以温度计的读数为准，而不是只凭记忆。
"""

KP_CH_TH_EN = r"""
## Reactions can release heat or take it in

Stage 8 asks you to describe reactions with **word equations**, and to know that some processes are **exothermic** or **endothermic**, identified by a temperature change.

## Key points

1. A **word equation** is written as reactants → products. States can be added later; at this stage, get the names right.
   - Example: magnesium + oxygen → magnesium oxide
2. An **exothermic** process transfers energy to the surroundings; the temperature of the surroundings **rises**. Common examples: combustion, many neutralisation reactions, respiration.
3. An **endothermic** process takes in energy from the surroundings; the temperature of the surroundings **falls**. Common examples: dissolving some salts, thermal decomposition, photosynthesis.
4. Judge by the temperature of the **surroundings**, not by a vague sense of “inside the reaction”.
5. A reaction does not always give a single pure product; an impure mixture may need separating.
6. Some substances are generally unreactive and may be described as **inert** — gold at room temperature is a familiar example.

## Worked example

Magnesium hydroxide is used to neutralise excess hydrochloric acid in the stomach. Write a word equation, and say whether neutralisation is usually exo- or endothermic.

**Solution**

hydrochloric acid + magnesium hydroxide → magnesium chloride + water

Many neutralisation reactions are exothermic: in a beaker the mixture usually warms up. In class, trust a thermometer reading rather than memory alone.
"""

questions_ch = [
    Q("q-ch-at-01", "chemistry", "chemistry-8Cm", "mcq",
      "金箔实验中，绝大多数 $\\alpha$ 粒子几乎直线穿过，说明什么？",
      "In the gold-foil experiment, most $\\alpha$ particles went almost straight through. What does this suggest?",
      "b",
      "大多数粒子未受明显偏转，说明原子内部大部分是空的。",
      "Most particles were not deflected much, so most of the atom is empty space.",
      opts(("原子是实心的布丁", "The atom is a solid pudding"),
           ("原子内部大部分是空的", "Most of the atom is empty space"),
           ("电子全部集中在核内", "All the electrons are inside the nucleus"),
           ("金箔没有原子", "Gold foil contains no atoms")),
      knowledge_id="kp-chemistry-atom",
      published_at="2026-11-06T13:00:00+08:00"),
    Q("q-ch-at-02", "chemistry", "chemistry-8Cm", "short",
      "中子的电荷是什么？（可写“无”“0”或 “no charge”）",
      "What is the charge of a neutron? (You may write “none”, “0” or “no charge”.)",
      "0",
      "中子不带电，电荷为 $0$。",
      "A neutron has no charge (zero charge).",
      knowledge_id="kp-chemistry-atom",
      accepted=["0", "zero", "none", "no charge", "uncharged", "neutral", "无", "不带电", "零", "没有电荷"]),
    Q("q-ch-at-03", "chemistry", "chemistry-8Cm", "mcq",
      "把单个原子约束在一起的力，主要是？",
      "What mainly holds an individual atom together?",
      "c",
      "正电的核与负电的电子之间的静电引力。",
      "Electrostatic attraction between the positive nucleus and the negative electrons.",
      opts(("重力为主", "Mostly gravity"),
           ("磁铁的南北极", "The north and south poles of a bar magnet"),
           ("正负电荷之间的静电引力", "Electrostatic attraction between positive and negative charge"),
           ("空气压力", "Air pressure")),
      knowledge_id="kp-chemistry-atom"),
    Q("q-ch-th-01", "chemistry", "chemistry-8Cc", "mcq",
      "若反应使烧杯中液体温度升高，该反应最可能是？",
      "If a reaction makes the liquid in a beaker warmer, the reaction is most likely:",
      "a",
      "周围温度上升，说明过程放热（exothermic）。",
      "A rise in the temperature of the surroundings indicates an exothermic process.",
      opts(("放热的", "exothermic"),
           ("吸热的", "endothermic"),
           ("一定没有生成物", "sure to have no products"),
           ("一定是物理变化", "sure to be only a physical change")),
      knowledge_id="kp-chemistry-thermo"),
    Q("q-ch-th-02", "chemistry", "chemistry-8Cc", "short",
      "写出文字方程式：镁在氧气中燃烧。（可用中文或英文物质名，中间用箭头。）",
      "Write a word equation for magnesium burning in oxygen. Use an arrow between names.",
      "镁+氧气→氧化镁",
      "镁 + 氧气 → 氧化镁；或 magnesium + oxygen → magnesium oxide。",
      "magnesium + oxygen → magnesium oxide.",
      knowledge_id="kp-chemistry-thermo",
      accepted=[
          "镁+氧气→氧化镁", "镁＋氧气→氧化镁", "镁 + 氧气 → 氧化镁",
          "镁+氧→氧化镁",
          "magnesium + oxygen → magnesium oxide",
          "magnesium+oxygen→magnesium oxide",
          "magnesium + oxygen -> magnesium oxide",
      ]),
    Q("q-ch-ch-01", "chemistry", "chemistry-8Cp", "mcq",
      "纸层析法的主要用途是？",
      "What is paper chromatography mainly used for?",
      "d",
      "纸层析可分离混合物中的物质，并帮助鉴别样品中有哪些成分。",
      "Paper chromatography can separate substances in a sample and help to identify them.",
      opts(("测量原子的质量", "Measuring the mass of an atom"),
           ("把水变成氧气", "Turning water into oxygen"),
           ("产生电流", "Producing an electric current"),
           ("分离并帮助鉴别样品中的物质", "Separating and helping to identify substances in a sample"))),
    Q("q-ch-met-01", "chemistry", "chemistry-8Cc", "mcq",
      "下列金属中，通常最不活泼的是？",
      "Which of these metals is usually the least reactive?",
      "c",
      "第 8 阶段比较钠、钾、钙、镁、锌、铁、铜、金、银等与氧、水、稀酸的反应。金的反应性很低。",
      "Stage 8 compares metals including sodium, potassium, calcium, magnesium, zinc, iron, copper, gold and silver. Gold is very unreactive.",
      opts(("钾", "Potassium"),
           ("钠", "Sodium"),
           ("金", "Gold"),
           ("钙", "Calcium"))),
    Q("q-ch-conc-01", "chemistry", "chemistry-8Cp", "mcq",
      "溶液更浓，指的是在一定体积溶剂中：",
      "A more concentrated solution means that, in a given volume of solvent,",
      "b",
      "浓度与一定体积溶剂（或溶液）中溶质粒子的多少有关。",
      "Concentration is about how many solute particles are present in a volume of solvent (or solution).",
      opts(("溶剂粒子更少，与溶质无关", "there are fewer solvent particles, regardless of solute"),
           ("溶质粒子更多", "there are more solute particles"),
           ("温度一定更高", "the temperature must be higher"),
           ("容器一定更大", "the container must be larger"))),
    Q("q-ch-res-01", "chemistry", "chemistry-8ES", "mcq",
      "下列哪一项属于不可再生资源？",
      "Which of the following is a non-renewable resource?",
      "a",
      "化石燃料形成极慢，属于不可再生资源；风能、潮汐能、太阳能属于可再生资源。",
      "Fossil fuels form far too slowly to be replaced on a human timescale. Wind, tidal and solar power are renewable.",
      opts(("化石燃料", "Fossil fuels"),
           ("风能", "Wind power"),
           ("潮汐能", "Tidal power"),
           ("太阳能", "Solar power"))),
    Q("q-ch-cli-01", "chemistry", "chemistry-8ES", "short",
      "用一句话区别“天气”和“气候”。",
      "In one sentence, what is the difference between weather and climate?",
      "天气是短时间的大气状况，气候是一个地区长期的平均天气状况",
      "天气指某地某时的大气状况；气候是一个地区在较长时期里的一般天气状况。",
      "Weather is the state of the atmosphere at a particular time; climate is the typical weather of an area over a long period.",
      accepted=[
          "天气是短时间的大气状况，气候是一个地区长期的平均天气状况",
          "天气是短期的，气候是长期的平均状况",
          "天气短期，气候长期",
          "weather is short term, climate is long term",
          "weather is the conditions at a time, climate is the typical weather over a long period",
          "weather is short-term atmospheric conditions; climate is the average over a long period",
      ]),
]

knowledge_ch = [
    KP("kp-chemistry-atom", "chemistry", "chemistry-8Cm", "chemistry-8Cm-1",
       "卢瑟福原子模型与粒子电荷",
       "The Rutherford atom and the charges of particles",
       KP_CH_AT_ZH, KP_CH_AT_EN,
       ["q-ch-at-01", "q-ch-at-02", "q-ch-at-03"],
       "2026-11-06T13:00:00+08:00",
       "原子大部分是空的，中心有很小的正电核；电子负、质子正、中子不带电。",
       "Atoms are mostly empty space with a tiny positive nucleus; electrons are negative, protons positive, neutrons uncharged."),
    KP("kp-chemistry-thermo", "chemistry", "chemistry-8Cc", "chemistry-8Cc-1",
       "文字方程式与放热、吸热反应",
       "Word equations and exothermic or endothermic change",
       KP_CH_TH_ZH, KP_CH_TH_EN,
       ["q-ch-th-01", "q-ch-th-02"],
       "2026-10-15T10:00:00+08:00",
       "用“反应物 → 生成物”书写；周围升温为放热，降温为吸热。",
       "Write reactants → products; a temperature rise of the surroundings is exothermic, a fall is endothermic."),
]

sets_ch = [
    SET("practice-chemistry-atom-energy", "chemistry", "chemistry-8Cm", "practice",
        "练习组 · 原子与能量变化",
        "Practice set · Atoms and energy change",
        ["q-ch-at-01", "q-ch-at-02", "q-ch-at-03", "q-ch-th-01", "q-ch-th-02", "q-ch-ch-01"],
        published_at="2026-11-06T14:00:00+08:00"),
    SET("paper-chemistry-a", "chemistry", "chemistry-8Cm", "paper",
        "本站练习卷 A · 原子、反应与资源",
        "Practice Paper A · Atoms, reactions and resources",
        ["q-ch-at-01", "q-ch-at-02", "q-ch-at-03", "q-ch-th-01", "q-ch-th-02",
         "q-ch-ch-01", "q-ch-met-01", "q-ch-conc-01", "q-ch-res-01", "q-ch-cli-01"],
        time_limit=25, published_at="2026-10-23T09:00:00+08:00"),
]

# ---------------------------------------------------------------------------
# Biology
# ---------------------------------------------------------------------------
KP_BI_BL_ZH = r"""
## 血液在运输，也在保护

第 8 阶段生物学要求描述血液的组成与功能，范围限定为：

- **红细胞**：运输氧气；
- **白细胞**：抵御病原体；
- **血浆**：运输血细胞、营养物质和二氧化碳。

（血小板等其他成分在后续课程更常作为重点，本阶段先掌握上面三项。）

## 要点

1. 血液是流动的组织，在心脏推动下在体内循环。
2. 红细胞含有**血红蛋白**，能与氧结合，把氧从肺运到组织。成熟红细胞没有细胞核，这与它腾出空间携带氧有关（可作拓展，考试先抓“运氧”这一核心功能）。
3. 白细胞种类多样，但本阶段核心是：**保护身体，对抗病原体**（致病微生物）。
4. 血浆是淡黄色的液体部分，细胞悬浮其中，并运输溶解的营养（如葡萄糖）、二氧化碳以及细胞本身。
5. 结构与功能相联系：红细胞的功能是运氧，白细胞的功能是防御，血浆的功能是运输。

## 不要与呼吸作用混淆

血液把氧气运到细胞，细胞在**线粒体**里进行有氧呼吸。运输氧气是血液的工作；释放能量是呼吸作用的工作。
"""

KP_BI_BL_EN = r"""
## Blood transports, and it also protects

Stage 8 Biology asks you to describe the components of blood and their functions, limited to:

- **red blood cells** transporting oxygen;
- **white blood cells** protecting against pathogens;
- **plasma** transporting blood cells, nutrients and carbon dioxide.

(Other parts such as platelets become more of a focus later. Master these three first.)

## Key points

1. Blood is a circulating tissue, moved by the heart.
2. Red blood cells contain **haemoglobin**, which binds oxygen and carries it from the lungs to the tissues. (Mature human red cells have no nucleus, which relates to space for oxygen — treat that as extension; the core function is oxygen transport.)
3. White blood cells are of several types, but the Stage 8 core idea is that they **protect against pathogens** (disease-causing microorganisms).
4. Plasma is the pale liquid in which cells are carried. It transports dissolved nutrients (such as glucose), carbon dioxide, and the blood cells themselves.
5. Link structure to function: red cells — oxygen; white cells — defence; plasma — transport.

## Do not confuse this with respiration

Blood delivers oxygen to cells; the cells then carry out aerobic respiration in **mitochondria**. Carrying oxygen is a job of the blood; releasing energy is a job of respiration.
"""

KP_BI_RE_ZH = r"""
## 有氧呼吸：在线粒体里受控地释放能量

第 8 阶段要求知道：有氧呼吸发生在植物和动物细胞的**线粒体**中，并且是能量的**受控释放**。还要会使用摘要文字方程式：

$$\text{葡萄糖} + \text{氧气} \rightarrow \text{二氧化碳} + \text{水}$$

英文：

$$\text{glucose} + \text{oxygen} \rightarrow \text{carbon dioxide} + \text{water}$$

## 要点

1. **呼吸作用 $\neq$ 呼吸运动（breathing）。**
   - 呼吸运动是空气进出肺（膈肌与肋间肌的作用）；
   - 呼吸作用是细胞内释放能量的化学反应。
2. 释放的能量用于生命活动（如肌肉收缩、保持体温、物质运输），不是“制造”能量——能量从葡萄糖等贮能物质中释放出来。
3. “受控”意味着能量不是像燃烧那样一次性全部放出，而是经过酶催化的步骤逐步释放。
4. 发生场所是线粒体，因此线粒体多的细胞（如肌肉细胞）呼吸作用更旺盛。
5. 肺中的气体交换（氧进入血液、二氧化碳离开血液）为有氧呼吸提供原料并带走产物，但气体交换本身不是呼吸作用。

## 例题

有人说：“我们一停止呼吸运动，呼吸作用也就不存在了，所以两者是同一件事。” 请判断并改正。

**解：** 说法不正确。停止呼吸运动后，体内暂时还能利用已有的氧继续进行一段时间的呼吸作用，但氧会很快用尽。两者紧密联系，却不是同一过程：一个是通气，一个是细胞里的化学反应。
"""

KP_BI_RE_EN = r"""
## Aerobic respiration: a controlled release of energy in mitochondria

Stage 8 requires you to know that aerobic respiration occurs in the **mitochondria** of plant and animal cells, and that it gives a **controlled release of energy**. You should also use the summary word equation:

$$\text{glucose} + \text{oxygen} \rightarrow \text{carbon dioxide} + \text{water}$$

## Key points

1. **Respiration is not the same as breathing.**
   - Breathing is the movement of air into and out of the lungs (the action of the diaphragm and intercostal muscles);
   - Respiration is a chemical process in cells that releases energy.
2. The energy released is used for life processes (muscle contraction, keeping warm, transport). Energy is not “created”; it is released from stores such as glucose.
3. “Controlled” means the energy is not released in one burst as in a fire, but in enzyme-catalysed steps.
4. The site is the mitochondrion, so cells with many mitochondria (such as muscle cells) can respire more actively.
5. Gas exchange in the lungs supplies oxygen and removes carbon dioxide for aerobic respiration, but gas exchange itself is not respiration.

## Worked example

Someone says: “If breathing stops, respiration stops at the same instant, so they are the same process.” Judge and correct this.

**Solution.** The claim is wrong. If breathing stops, cells can continue to respire for a short time using oxygen already present, until that oxygen runs out. The two processes are closely linked but not the same: one is ventilation, the other is a chemical reaction in cells.
"""

questions_bi = [
    Q("q-bi-bl-01", "biology", "biology-8Bs", "mcq",
      "红细胞的主要功能是？",
      "What is the main function of red blood cells, as required at Stage 8?",
      "b",
      "第 8 阶段明确：红细胞运输氧气。白细胞对抗病原体，血浆运输血细胞、营养和二氧化碳。",
      "Stage 8 states that red blood cells transport oxygen. White cells protect against pathogens; plasma transports cells, nutrients and carbon dioxide.",
      opts(("抵御病原体", "Protecting against pathogens"),
           ("运输氧气", "Transporting oxygen"),
           ("产生神经冲动", "Producing nerve impulses"),
           ("消化淀粉", "Digesting starch")),
      knowledge_id="kp-biology-blood"),
    Q("q-bi-bl-02", "biology", "biology-8Bs", "short",
      "血浆除了运输血细胞，还运输哪两种物质？（第 8 阶段要求）",
      "Besides blood cells, name two things plasma transports (as required at Stage 8).",
      "营养物质和二氧化碳",
      "血浆运输血细胞、营养物质和二氧化碳。答 nutrients 与 carbon dioxide 即可。",
      "Plasma transports blood cells, nutrients and carbon dioxide.",
      knowledge_id="kp-biology-blood",
      accepted=[
          "营养物质和二氧化碳", "营养和二氧化碳", "养分和二氧化碳",
          "nutrients and carbon dioxide", "nutrients and co2",
          "carbon dioxide and nutrients", "co2 and nutrients",
          "营养物质、二氧化碳",
      ]),
    Q("q-bi-bl-03", "biology", "biology-8Bs", "mcq",
      "白细胞的功能是？",
      "What is the function of white blood cells?",
      "c",
      "白细胞保护身体，对抗病原体。",
      "White blood cells protect against pathogens.",
      opts(("把氧气运到肌肉", "Transporting oxygen to muscle"),
           ("只运输二氧化碳", "Transporting carbon dioxide only"),
           ("抵御病原体", "Protecting against pathogens"),
           ("把血液变成血浆", "Turning blood into plasma")),
      knowledge_id="kp-biology-blood"),
    Q("q-bi-re-01", "biology", "biology-8Bp", "short",
      "写出有氧呼吸的摘要文字方程式（中文或英文）。",
      "Write the summary word equation for aerobic respiration (Chinese or English).",
      "葡萄糖+氧气→二氧化碳+水",
      "葡萄糖 + 氧气 → 二氧化碳 + 水；glucose + oxygen → carbon dioxide + water。",
      "glucose + oxygen → carbon dioxide + water.",
      knowledge_id="kp-biology-respiration",
      accepted=[
          "葡萄糖+氧气→二氧化碳+水", "葡萄糖＋氧气→二氧化碳＋水",
          "葡萄糖 + 氧气 → 二氧化碳 + 水",
          "glucose + oxygen → carbon dioxide + water",
          "glucose+oxygen→carbon dioxide+water",
          "glucose + oxygen -> carbon dioxide + water",
      ],
      published_at="2026-11-09T19:00:00+08:00"),
    Q("q-bi-re-02", "biology", "biology-8Bp", "mcq",
      "有氧呼吸发生在细胞的哪一结构中？",
      "In which cell structure does aerobic respiration occur?",
      "d",
      "有氧呼吸发生在线粒体中，是受控的能量释放。",
      "Aerobic respiration occurs in mitochondria and gives a controlled release of energy.",
      opts(("细胞壁", "The cell wall"),
           ("液泡", "The sap vacuole"),
           ("叶绿体", "The chloroplast"),
           ("线粒体", "The mitochondria")),
      knowledge_id="kp-biology-respiration",
      published_at="2026-11-09T19:00:00+08:00"),
    Q("q-bi-re-03", "biology", "biology-8Bp", "mcq",
      "关于呼吸运动（breathing）和呼吸作用（respiration），正确的是？",
      "Which statement about breathing and respiration is correct?",
      "a",
      "呼吸运动是空气进出肺；呼吸作用是细胞内释放能量的化学反应。两者相关但不是同一过程。",
      "Breathing is air moving in and out of the lungs; respiration is a chemical process in cells that releases energy.",
      opts(("两者相关但不是同一过程", "They are linked but they are not the same process"),
           ("两个词永远表示同一件事", "The two words always mean the same thing"),
           ("植物只进行呼吸运动，不进行呼吸作用", "Plants only breathe; they do not respire"),
           ("呼吸作用只在肺里进行", "Respiration happens only in the lungs")),
      knowledge_id="kp-biology-respiration"),
    Q("q-bi-diet-01", "biology", "biology-8Bp", "mcq",
      "第 8 阶段所指的均衡饮食，不包括下列哪一类作为所列营养素？",
      "Which of the following is not one of the listed constituents of a balanced diet at Stage 8?",
      "c",
      "所列包括蛋白质、糖类、脂肪和油、水、矿物质（钙和铁）以及维生素（A、C、D）。“塑料”不是营养素。",
      "The list includes protein, carbohydrates, fats and oils, water, minerals (calcium and iron) and vitamins (A, C and D). Plastic is not a nutrient.",
      opts(("蛋白质", "Protein"),
           ("维生素 C", "Vitamin C"),
           ("塑料", "Plastic"),
           ("铁", "Iron"))),
    Q("q-bi-lung-01", "biology", "biology-8Bs", "mcq",
      "氧从肺泡进入血液，主要依靠哪一种过程？",
      "Oxygen moves from the air in the alveoli into the blood mainly by which process?",
      "b",
      "第 8 阶段要求描述氧和二氧化碳在血液与肺泡空气之间的扩散。",
      "Stage 8 requires the diffusion of oxygen and carbon dioxide between blood and the air in the lungs.",
      opts(("主动运输为主，且不需要浓度差", "Active transport, with no need for a concentration difference"),
           ("扩散", "Diffusion"),
           ("蒸腾", "Transpiration"),
           ("同化", "Assimilation"))),
    Q("q-bi-eco-01", "biology", "biology-8Be", "mcq",
      "有毒物质沿食物链浓度越来越高，这一现象称为？",
      "Toxic substances becoming more concentrated along a food chain is called:",
      "d",
      "这是生物累积（bioaccumulation），会对生态系统中的生物造成影响。",
      "This is bioaccumulation, which can harm organisms in an ecosystem.",
      opts(("光合作用", "Photosynthesis"),
           ("蒸腾作用", "Transpiration"),
           ("传粉", "Pollination"),
           ("生物累积", "Bioaccumulation"))),
    Q("q-bi-joint-01", "biology", "biology-8Bs", "mcq",
      "肘关节主要是哪一种关节？拮抗肌如何使之运动？",
      "The elbow is mainly which type of joint, and how do antagonistic muscles move it?",
      "a",
      "肘是铰链关节（hinge）。拮抗肌成对工作：一块收缩时另一块舒张，从而拉动骨。",
      "The elbow is a hinge joint. Antagonistic muscles work in pairs: one contracts while the other relaxes, moving the bone.",
      opts(("铰链关节；肌肉成对，一缩一舒", "A hinge joint; muscles work in pairs, one contracting and one relaxing"),
           ("球窝关节；只需一块肌肉持续收缩", "A ball-and-socket joint; only one muscle must stay contracted"),
           ("它不是关节", "It is not a joint"),
           ("铰链关节；两块肌肉必须同时收缩且同时舒张", "A hinge joint; both muscles must contract and relax together"))),
]

knowledge_bi = [
    KP("kp-biology-blood", "biology", "biology-8Bs", "biology-8Bs-2",
       "血液的组成与功能",
       "Components of blood and their functions",
       KP_BI_BL_ZH, KP_BI_BL_EN,
       ["q-bi-bl-01", "q-bi-bl-02", "q-bi-bl-03"],
       "2026-10-14T10:00:00+08:00",
       "红细胞运氧，白细胞抵御病原体，血浆运输血细胞、营养和二氧化碳。",
       "Red cells carry oxygen, white cells defend against pathogens, and plasma transports cells, nutrients and carbon dioxide."),
    KP("kp-biology-respiration", "biology", "biology-8Bp", "biology-8Bp-4",
       "有氧呼吸与呼吸运动的区别",
       "Aerobic respiration, and how it differs from breathing",
       KP_BI_RE_ZH, KP_BI_RE_EN,
       ["q-bi-re-01", "q-bi-re-02", "q-bi-re-03"],
       "2026-11-09T19:00:00+08:00",
       "有氧呼吸在线粒体中进行：葡萄糖 + 氧气 → 二氧化碳 + 水。",
       "Aerobic respiration occurs in mitochondria: glucose + oxygen → carbon dioxide + water."),
]

sets_bi = [
    SET("practice-biology-blood-respiration", "biology", "biology-8Bs", "practice",
        "练习组 · 血液与呼吸作用",
        "Practice set · Blood and respiration",
        ["q-bi-bl-01", "q-bi-bl-03", "q-bi-bl-02", "q-bi-re-02", "q-bi-re-01", "q-bi-re-03"],
        published_at="2026-11-09T19:30:00+08:00"),
    SET("paper-biology-a", "biology", "biology-8Bs", "paper",
        "本站练习卷 A · 人体与生命过程",
        "Practice Paper A · The body and life processes",
        ["q-bi-bl-01", "q-bi-bl-02", "q-bi-bl-03", "q-bi-re-01", "q-bi-re-02",
         "q-bi-re-03", "q-bi-diet-01", "q-bi-lung-01", "q-bi-joint-01", "q-bi-eco-01"],
        time_limit=25, published_at="2026-10-22T09:00:00+08:00"),
]
