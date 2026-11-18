"""Grade 9 Mathematics — IGCSE 0580 and Additional Mathematics 0606, topics 1–8.

Order matches the term: accuracy and recurring decimals, indices and surds,
quadratics, sets, graphs, polynomials, functions, coordinate geometry.
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


def chapter(n, code, title_zh, title_en, lesson):
    return {
        "id": f"g9-maths-{n}",
        "code": code,
        "order": n,
        "title_zh": title_zh,
        "title_en": title_en,
        "practice_minutes": 15,
        "units": [{
            "id": f"g9-maths-{n}-u1",
            "code": str(n),
            "order": 1,
            "title_zh": title_zh,
            "title_en": title_en,
            "lessons": [lesson],
        }],
    }


SPEC = {
    "subject_id": "mathematics",
    "tag": "g9ma",
    "chapters": [
        chapter(1, "0580 · 1", "数、精确度与循环小数", "Numbers, accuracy and recurring decimals", L(
            "g9ma-1", "1",
            "上下界与循环小数",
            "Bounds and recurring decimals",
            "会求一个已四舍五入的量的下界和上界，并把循环小数写成最简分数。",
            "Find the lower and upper bounds of a rounded measurement, and write a recurring decimal as a fraction in lowest terms.",
            [
                ("精确到小数点后 1 位时，下界比读数小 $0.05$，上界比读数大 $0.05$。", "To 1 decimal place, the lower bound is $0.05$ below the reading and the upper bound is $0.05$ above it."),
                ("写成区间时，常用下界 $\\le x <$ 上界，因为正好等于上界会进到下一位。", "As an interval, the usual form is lower bound $\\le x <$ upper bound, because a value exactly on the upper bound rounds up."),
                ("纯循环小数：设 $x$ 等于该数，乘 $10^n$（$n$ 为循环节位数），再相减。", "For a purely recurring decimal, set $x$ equal to it, multiply by $10^n$ where $n$ is the length of the repeating block, then subtract."),
                ("相减后得到的分数要约分。", "Cancel the fraction you obtain."),
            ],
            "测量值 $6.4\\,\\mathrm{cm}$（精确到 $0.1\\,\\mathrm{cm}$）表示真实长度 $x$ 满足 $6.35 \\le x < 6.45$。问“下界”就写 $6.35$，问“上界”写 $6.45$。两个量相乘求最大可能值时，用各自的上界相乘；求最小可能值时用下界。若其中一个量在分母上，最大结果反而要用较小的分母。\n\n循环小数 $0.\\dot{2}\\dot{7}$ 的循环节有两位，所以乘 $100$：$100x = 27.\\dot{2}\\dot{7}$，$99x = 27$，$x = 27/99 = 3/11$。",
            "A length of $6.4\\,\\mathrm{cm}$ to the nearest $0.1\\,\\mathrm{cm}$ means $6.35 \\le x < 6.45$. The lower bound is $6.35$ and the upper bound is $6.45$. For a maximum product, multiply upper bounds; for a minimum product, multiply lower bounds. If a quantity is in the denominator, the maximum uses the smaller denominator.\n\nFor $0.\\dot{2}\\dot{7}$ the block has two digits, so multiply by $100$: $100x = 27.\\dot{2}\\dot{7}$, $99x = 27$, and $x = 27/99 = 3/11$.",
            "把 $0.\\dot{1}\\dot{6}$ 写成最简分数。\n\n设 $x = 0.161616\\ldots$，则 $100x = 16.1616\\ldots$，$99x = 16$，$x = 16/99$。$16$ 与 $99$ 没有大于 $1$ 的公因数，所以最简分数是 $16/99$。",
            "Write $0.\\dot{1}\\dot{6}$ as a fraction in lowest terms.\n\nLet $x = 0.161616\\ldots$. Then $100x = 16.1616\\ldots$, so $99x = 16$ and $x = 16/99$. $16$ and $99$ have no common factor greater than $1$, so the fraction is already $16/99$.",
            [
                ("把精确到 $0.1$ 的上界写成加 $0.1$，而不是加 $0.05$。", "Adding $0.1$ for a 1-decimal-place upper bound instead of $0.05$."),
                ("循环节有两位，却只乘了 $10$。", "Multiplying by $10$ when the repeating block has two digits."),
                ("分数没有约分。", "Leaving a fraction uncancelled."),
            ],
            [
                num("长度 $8.6\\,\\mathrm{cm}$，精确到小数点后 1 位。下界是多少厘米？", "A length is $8.6\\,\\mathrm{cm}$ to 1 decimal place. What is the lower bound, in centimetres?", "8.35", "精确到 $0.1$ 时，下界减 $0.05$。", "To the nearest $0.1$, subtract $0.05$.", 1, 0),
                num("同一长度的上界是多少厘米？", "For the same length, what is the upper bound, in centimetres?", "8.65", "上界是 $8.6 + 0.05$。", "The upper bound is $8.6 + 0.05$.", 1, 0),
                short("把 $0.\\dot{2}\\dot{7}$ 写成最简分数。", "Write $0.\\dot{2}\\dot{7}$ as a fraction in lowest terms.", "3/11", "$27/99 = 3/11$。", "$27/99 = 3/11$.", ["3/11", "27/99"], 2),
            ],
        )),
        chapter(2, "0580 · 2", "指数与根式", "Indices and surds", L(
            "g9ma-2", "2",
            "指数定律与根式化简",
            "Index laws and simplifying surds",
            "会用负指数、分数指数，并把根式化成最简形式、分母有理化。",
            "Use negative and fractional indices, write a surd in simplest form, and rationalise a denominator.",
            [
                ("$a^m \\times a^n = a^{m+n}$，$a^m \\div a^n = a^{m-n}$，$(a^m)^n = a^{mn}$。", "$a^m \\times a^n = a^{m+n}$, $a^m \\div a^n = a^{m-n}$, $(a^m)^n = a^{mn}$."),
                ("$a^{-n} = 1/a^n$，$a^{1/n} = \\sqrt[n]{a}$，$a^{m/n} = (\\sqrt[n]{a})^m$。", "$a^{-n} = 1/a^n$, $a^{1/n} = \\sqrt[n]{a}$, $a^{m/n} = (\\sqrt[n]{a})^m$."),
                ("$\\sqrt{ab} = \\sqrt{a}\\sqrt{b}$。把平方因数开出来，例如 $\\sqrt{48} = 4\\sqrt{3}$。", "$\\sqrt{ab} = \\sqrt{a}\\sqrt{b}$. Take square factors out: $\\sqrt{48} = 4\\sqrt{3}$."),
                ("分母有理化：单项乘同一个根式；两项乘共轭。", "To rationalise, multiply a single-term denominator by the same surd, and a two-term denominator by its conjugate."),
            ],
            "分数指数先开方再乘方，数字会小一些。$8^{2/3} = (8^{1/3})^2 = 2^2 = 4$。负指数是倒数，不是负数：$16^{-1/2} = 1/4$，不是 $-4$。\n\n根式相加必须是同类根式。$\\sqrt{12} + \\sqrt{27} = 2\\sqrt{3} + 3\\sqrt{3} = 5\\sqrt{3}$。分母是 $\\sqrt{5}-1$ 时，乘 $\\sqrt{5}+1$，因为乘积是 $5-1 = 4$。",
            "Take the root before the power so the numbers stay smaller. $8^{2/3} = (8^{1/3})^2 = 2^2 = 4$. A negative index is a reciprocal, not a negative number: $16^{-1/2} = 1/4$, not $-4$.\n\nSurds add only when they are like terms. $\\sqrt{12} + \\sqrt{27} = 2\\sqrt{3} + 3\\sqrt{3} = 5\\sqrt{3}$. If the denominator is $\\sqrt{5}-1$, multiply by $\\sqrt{5}+1$, because the product is $5-1 = 4$.",
            "化简 $\\dfrac{6}{\\sqrt{3}}$。\n\n乘 $\\sqrt{3}/\\sqrt{3}$：$6\\sqrt{3}/3 = 2\\sqrt{3}$。",
            "Simplify $\\dfrac{6}{\\sqrt{3}}$.\n\nMultiply by $\\sqrt{3}/\\sqrt{3}$: $6\\sqrt{3}/3 = 2\\sqrt{3}$.",
            [
                ("把 $a^{-2}$ 算成 $-a^2$。", "Treating $a^{-2}$ as $-a^2$."),
                ("$\\sqrt{48}$ 只写成 $\\sqrt{16 \\times 3}$，没有把 $4$ 开出来。", "Leaving $\\sqrt{48}$ as $\\sqrt{16 \\times 3}$ and not taking the $4$ outside."),
                ("不同根式直接把根号内的数相加。", "Adding the numbers inside unlike surds."),
            ],
            [
                num("计算 $8^{2/3}$。", "Evaluate $8^{2/3}$.", "4", "$(8^{1/3})^2 = 4$。", "$(8^{1/3})^2 = 4$.", 1, 0),
                num("计算 $16^{-1/2}$。", "Evaluate $16^{-1/2}$.", "0.25", "等于 $1/4$。", "This is $1/4$.", 1, 0, ["1/4", "0.25"]),
                short("把 $\\sqrt{48}$ 写成 $k\\sqrt{3}$ 的形式。", "Write $\\sqrt{48}$ in the form $k\\sqrt{3}$.", "4√3", "$\\sqrt{48} = \\sqrt{16 \\times 3} = 4\\sqrt{3}$。", "$\\sqrt{48} = \\sqrt{16 \\times 3} = 4\\sqrt{3}$.", ["4√3", "4sqrt(3)", "4*sqrt(3)"], 2),
            ],
        )),
        chapter(3, "0580/0606 · 3", "二次方程与不等式", "Quadratic equations and inequalities", L(
            "g9ma-3", "3",
            "配方、判别式、不等式与非线性方程组",
            "Completing the square, the discriminant, inequalities and non-linear pairs",
            "会因式分解或配方解二次方程，用判别式判断根的情况，解二次不等式，并解一个线性与一个二次组成的方程组。",
            "Solve a quadratic by factorising or completing the square, use the discriminant, solve a quadratic inequality, and solve a linear equation paired with a quadratic.",
            [
                ("$x^2 + bx + c = 0$ 可配方为 $\\left(x + \\dfrac{b}{2}\\right)^2 - \\left(\\dfrac{b}{2}\\right)^2 + c = 0$。", "$x^2 + bx + c = 0$ completes to $\\left(x + \\dfrac{b}{2}\\right)^2 - \\left(\\dfrac{b}{2}\\right)^2 + c = 0$."),
                ("判别式 $\\Delta = b^2 - 4ac$。$\\Delta > 0$ 两个不同实根，$= 0$ 两个相等实根，$< 0$ 无实根。", "The discriminant is $\\Delta = b^2 - 4ac$. If $\\Delta > 0$ there are two distinct real roots, if $= 0$ one repeated real root, if $< 0$ no real roots."),
                ("二次不等式先找根，再看抛物线在根的外侧还是内侧为正。", "For a quadratic inequality, find the roots, then see whether the parabola is positive outside or between them."),
                ("非线性方程组：用线性式代入二次式，得到一个一元二次方程。", "For a non-linear pair, substitute the linear expression into the quadratic so that one quadratic in one unknown remains."),
            ],
            "草图帮助检查不等式。$y = x^2 - 5x + 6 = (x-2)(x-3)$ 开口向上，在 $x = 2$ 与 $x = 3$ 之间为负，所以 $x^2 - 5x + 6 \\le 0$ 的解是 $2 \\le x \\le 3$。严格大于号则不包括等号，并写成两段：$x < 2$ 或 $x > 3$。\n\n判别式只判断实数根的个数，不直接给出根。方程组代入后如果得到两个解，要分别代回求另一个未知数，两个配对都要写。",
            "A sketch checks an inequality. $y = x^2 - 5x + 6 = (x-2)(x-3)$ opens upwards and is negative between $x = 2$ and $x = 3$, so $x^2 - 5x + 6 \\le 0$ has solution $2 \\le x \\le 3$. A strict inequality excludes the equals sign and, outside the roots, is written in two parts: $x < 2$ or $x > 3$.\n\nThe discriminant counts real roots; it does not give them. After substitution, each root of the quadratic must be paired with the other unknown.",
            "解 $\\begin{cases} y = x + 1 \\\\ y = x^2 \\end{cases}$。\n\n代入：$x^2 - x - 1 = 0$。判别式 $1 + 4 = 5$，两根为 $x = \\dfrac{1 \\pm \\sqrt{5}}{2}$，对应的 $y$ 各加 $1$。",
            "Solve $\\begin{cases} y = x + 1 \\\\ y = x^2 \\end{cases}$.\n\nSubstitute: $x^2 - x - 1 = 0$. The discriminant is $1 + 4 = 5$, so $x = \\dfrac{1 \\pm \\sqrt{5}}{2}$, and each $y$ is that value plus $1$.",
            [
                ("配方时只写出 $\\left(x + \\dfrac{b}{2}\\right)^2$，忘了减去 $\\left(\\dfrac{b}{2}\\right)^2$。", "Completing the square and forgetting to subtract $\\left(\\dfrac{b}{2}\\right)^2$."),
                ("开口向上的二次式，把“大于零”写成两个根之间。", "For a positive-leading quadratic, writing “greater than zero” as the region between the roots."),
                ("方程组只写出 $x$，没有配上 $y$。", "Giving $x$ from a pair of equations and never pairing $y$."),
            ],
            [
                short("把 $x^2 + 6x + 2$ 配成 $(x+h)^2 + k$。", "Write $x^2 + 6x + 2$ in the form $(x+h)^2 + k$.", "(x+3)^2-7", "$(x+3)^2 - 9 + 2 = (x+3)^2 - 7$。", "$(x+3)^2 - 9 + 2 = (x+3)^2 - 7$.", ["(x+3)^2-7", "(x+3)^2 - 7"], 2),
                mcq("$2x^2 + 3x + 5 = 0$ 的判别式是 $-11$。根的情况是？", "The discriminant of $2x^2 + 3x + 5 = 0$ is $-11$. The roots are:", "c", "没有实数根。", "There are no real roots.", [("两个不同实根", "two distinct real roots"), ("一个重复实根", "one repeated real root"), ("没有实数根", "no real roots"), ("两个相等的虚数，仍可在实数轴上标出", "two equal non-real roots that can still be plotted on the real axis")]),
                short("解不等式 $x^2 - 5x + 6 > 0$。", "Solve $x^2 - 5x + 6 > 0$.", "x<2 or x>3", "开口向上，大于零在两根外侧。", "The parabola opens upwards, so it is positive outside the roots.", ["x<2 or x>3", "x < 2 or x > 3"], 2),
            ],
        )),
        chapter(4, "0580 · 4", "集合与韦恩图", "Sets and Venn diagrams", L(
            "g9ma-4", "4",
            "集合记号与韦恩图计数",
            "Set notation and counting on a Venn diagram",
            "会读写 $\\in$、$\\cap$、$\\cup$、$A'$ 和 $n(A)$，并用两集合公式填写韦恩图。",
            "Read and write $\\in$, $\\cap$, $\\cup$, $A'$ and $n(A)$, and fill a two-set Venn diagram with the union formula.",
            [
                ("$n(A \\cup B) = n(A) + n(B) - n(A \\cap B)$。减一次是因为交集被加了两次。", "$n(A \\cup B) = n(A) + n(B) - n(A \\cap B)$. Subtract once because the intersection was added twice."),
                ("只属于 $A$ 的人数是 $n(A) - n(A \\cap B)$。", "The number in $A$ only is $n(A) - n(A \\cap B)$."),
                ("$A'$ 是全集中不属于 $A$ 的部分，包含 $B$ 的“只属于 $B$”以及两者之外。", "$A'$ is the part of the universal set outside $A$. It includes “$B$ only” and the region outside both."),
                ("填图时先填交集，再填只属于一边的，最后填外面。", "Fill the intersection first, then each “only” region, then the outside."),
            ],
            "全集 $\\xi$ 里的“两者都不”等于 $n(\\xi) - n(A \\cup B)$。如果题目给的是百分数，公式照旧，只要单位一致。记号 $A \\subset B$ 表示 $A$ 的每个元素都在 $B$ 里，此时 $n(A \\cup B) = n(B)$。\n\n三集合的题本阶段先把两两交集和中间三者交集分开；本课的练习以两集合为主。",
            "“Neither” is $n(\\xi) - n(A \\cup B)$. Percentages use the same formula if the units match. $A \\subset B$ means every element of $A$ is in $B$, so $n(A \\cup B) = n(B)$.\n\nThree-set questions need the pairwise regions kept separate from the very centre. The practice here stays with two sets.",
            "某班 $30$ 人，$n(A) = 18$，$n(B) = 16$，$n(A \\cap B) = 7$。求两者都不的人数。\n\n$n(A \\cup B) = 18 + 16 - 7 = 27$。两者都不 $= 30 - 27 = 3$。",
            "In a class of $30$, $n(A) = 18$, $n(B) = 16$ and $n(A \\cap B) = 7$. Find how many are in neither.\n\n$n(A \\cup B) = 18 + 16 - 7 = 27$. Neither $= 30 - 27 = 3$.",
            [
                ("交集加了两次，却没有减去。", "Adding the intersection twice and not subtracting it."),
                ("把 $n(A)$ 当成“只属于 $A$”。", "Reading $n(A)$ as “$A$ only”."),
                ("“两者都不”误用成 $n(A') \\cap n(B)$ 这种把人数再求交的写法。", "Writing “neither” as if the counts themselves were sets."),
            ],
            [
                num("$n(A) = 12$，$n(B) = 9$，$n(A \\cap B) = 4$。求 $n(A \\cup B)$。", "$n(A) = 12$, $n(B) = 9$, $n(A \\cap B) = 4$. Find $n(A \\cup B)$.", "17", "$12 + 9 - 4 = 17$。", "$12 + 9 - 4 = 17$.", 1, 0),
                num("上题中只属于 $A$ 的人数是多少？", "In the same question, how many are in $A$ only?", "8", "$12 - 4 = 8$。", "$12 - 4 = 8$.", 1, 0),
                mcq("若 $A \\subset B$，则 $n(A \\cup B)$ 等于？", "If $A \\subset B$, then $n(A \\cup B)$ equals:", "b", "等于 $n(B)$。", "It equals $n(B)$.", [("$n(A) + n(B)$", "$n(A) + n(B)$"), ("$n(B)$", "$n(B)$"), ("$0$", "$0$"), ("$n(A) - n(B)$", "$n(A) - n(B)$")]),
            ],
        )),
        chapter(5, "0580 · 5", "函数图像", "Graphs of functions", L(
            "g9ma-5", "5",
            "识别一次、二次、三次、反比与指数图像",
            "Recognising linear, quadratic, cubic, reciprocal and exponential graphs",
            "根据形状判断图像类型，并说出每种图像的一个关键特征。",
            "Identify a graph from its shape, and state one key feature of each type.",
            [
                ("一次：$y = mx + c$，直线。$m$ 是梯度，$c$ 是 $y$ 截距。", "Linear: $y = mx + c$, a straight line. $m$ is the gradient and $c$ is the $y$-intercept."),
                ("二次：$y = ax^2 + bx + c$，抛物线。$a > 0$ 开口向上。", "Quadratic: $y = ax^2 + bx + c$, a parabola. If $a > 0$ it opens upwards."),
                ("三次：$y = ax^3 + \\cdots$，两端朝相反方向，可有一个拐点。", "Cubic: $y = ax^3 + \\cdots$, the ends go in opposite directions, and there can be a point of inflection."),
                ("反比 $y = k/x$ 有两条分支，不与坐标轴相交；指数 $y = a^x$（$a > 1$）过 $(0, 1)$ 且始终为正。", "A reciprocal $y = k/x$ has two branches and does not meet the axes. An exponential $y = a^x$ with $a > 1$ passes through $(0, 1)$ and stays positive."),
            ],
            "识别时先看是否为直线，再看两端是否同向。二次两端同向；三次两端反向。反比图像靠近坐标轴时会变得很陡，但永远碰不到轴，所以有渐近线 $x = 0$ 和 $y = 0$。指数图像不会落到 $x$ 轴下面，并且在 $x = 0$ 时 $a^0 = 1$。\n\n题目若只给草图不给式子，用这些特征就够，不必先求出方程。",
            "Look first for a straight line, then for whether the ends go the same way. A quadratic’s ends agree; a cubic’s ends disagree. A reciprocal graph becomes steep near an axis but never meets it, so $x = 0$ and $y = 0$ are asymptotes. An exponential graph does not go below the $x$-axis, and $a^0 = 1$ when $x = 0$.\n\nIf the question gives a sketch and no equation, these features are enough. You do not need the equation first.",
            "草图过 $(0, 1)$，在 $x$ 增大时上升，且始终在 $x$ 轴上方。\n\n**解：** 这是指数图像，例如 $y = 2^x$。它不是 $y = x^2$，因为抛物线会到 $y = 0$ 并在顶点两侧都有。",
            "A sketch passes through $(0, 1)$, rises as $x$ increases, and stays above the $x$-axis.\n\n**Solution:** It is exponential, for example $y = 2^x$. It is not $y = x^2$, because a parabola meets $y = 0$ and exists on both sides of the vertex.",
            [
                ("把两端反向的三次图像说成抛物线。", "Calling a cubic, whose ends go opposite ways, a parabola."),
                ("认为 $y = 2^x$ 会经过原点。", "Thinking $y = 2^x$ passes through the origin."),
                ("认为 $y = 1/x$ 在原点有值。", "Thinking $y = 1/x$ has a value at the origin."),
            ],
            [
                mcq("两端朝相反方向、可穿过原点的平滑曲线，最可能是？", "A smooth curve whose ends go in opposite directions, and which may pass through the origin, is most likely:", "c", "三次函数。", "A cubic.", [("一次", "linear"), ("二次", "quadratic"), ("三次", "cubic"), ("指数", "exponential")]),
                mcq("$y = 3^x$ 一定经过哪一点？", "$y = 3^x$ must pass through which point?", "a", "$(0, 1)$。", "$(0, 1)$.", [("(0, 1)", "(0, 1)"), ("(1, 0)", "(1, 0)"), ("(0, 0)", "(0, 0)"), ("(3, 0)", "(3, 0)")]),
                short("$y = 1/x$ 的两条渐近线是什么？", "What are the two asymptotes of $y = 1/x$?", "x=0 and y=0", "坐标轴本身。", "The axes themselves.", ["x=0 and y=0", "the axes", "x=0, y=0", "坐标轴"], 1),
            ],
        )),
        chapter(6, "0606 · 6", "多项式因式与三次图像", "Polynomial factors and cubic graphs", L(
            "g9ma-6", "6",
            "余式定理、因式定理与比较系数",
            "Remainder theorem, factor theorem and comparing coefficients",
            "会用余式定理求余数，用因式定理找一次因式，并比较系数确定待定常数。",
            "Use the remainder theorem, find a linear factor with the factor theorem, and compare coefficients to find an unknown constant.",
            [
                ("$f(x)$ 除以 $(x - a)$ 的余数是 $f(a)$。", "The remainder when $f(x)$ is divided by $(x - a)$ is $f(a)$."),
                ("若 $f(a) = 0$，则 $(x - a)$ 是因式。", "If $f(a) = 0$, then $(x - a)$ is a factor."),
                ("候选的 $a$ 先试常数项因数与首项系数因数的商。", "Try values of $a$ from factors of the constant term over factors of the leading coefficient."),
                ("长除法或比较系数都可以把三次式写成一次式乘二次式。", "Long division or comparing coefficients writes a cubic as a linear factor times a quadratic."),
            ],
            "例如 $f(x) = x^3 - 6x^2 + 11x - 6$。$f(1) = 1 - 6 + 11 - 6 = 0$，所以 $(x - 1)$ 是因式。再试 $f(2) = 8 - 24 + 22 - 6 = 0$，$f(3) = 27 - 54 + 33 - 6 = 0$。因此 $f(x) = (x-1)(x-2)(x-3)$。三次图像与 $x$ 轴的交点就是这些根。\n\n若 $x^3 + px + q \\equiv (x-1)(x^2 + 2x + r)$，展开右边再比较 $x^2$、$x$ 和常数项的系数，可以求出 $p$、$q$、$r$。",
            "For example, $f(x) = x^3 - 6x^2 + 11x - 6$. $f(1) = 1 - 6 + 11 - 6 = 0$, so $(x - 1)$ is a factor. Also $f(2) = 0$ and $f(3) = 0$, so $f(x) = (x-1)(x-2)(x-3)$. A cubic graph meets the $x$-axis at these roots.\n\nIf $x^3 + px + q \\equiv (x-1)(x^2 + 2x + r)$, expand the right-hand side and compare coefficients of $x^2$, $x$ and the constant term.",
            "求 $f(x) = x^3 - 4x^2 + x + 6$ 除以 $(x - 2)$ 的余数。\n\n余数 $= f(2) = 8 - 16 + 2 + 6 = 0$。余数是 $0$，所以 $(x-2)$ 也是因式。",
            "Find the remainder when $f(x) = x^3 - 4x^2 + x + 6$ is divided by $(x - 2)$.\n\nThe remainder is $f(2) = 8 - 16 + 2 + 6 = 0$. The remainder is $0$, so $(x-2)$ is also a factor.",
            [
                ("除以 $(x + 2)$ 时误算 $f(2)$，而应算 $f(-2)$。", "Dividing by $(x + 2)$ and evaluating $f(2)$ instead of $f(-2)$."),
                ("找到一个因式后，没有把三次式除完就停止。", "Finding one factor and stopping before the cubic is fully factorised."),
                ("比较系数时漏掉展开后的 $x^2$ 项。", "Comparing coefficients and missing the $x^2$ term after expanding."),
            ],
            [
                num("$f(x) = x^3 - 4x^2 + x + 6$。$f(2)$ 等于多少？", "$f(x) = x^3 - 4x^2 + x + 6$. What is $f(2)$?", "0", "$8 - 16 + 2 + 6 = 0$。", "$8 - 16 + 2 + 6 = 0$.", 1, 0),
                short("由上题，$f(x)$ 有一个一次因式是什么？", "From the previous result, one linear factor of $f(x)$ is:", "(x-2)", "因为 $f(2) = 0$。", "Because $f(2) = 0$.", ["(x-2)", "x-2", "(x - 2)"], 1),
                num("$g(x) = x^3 + 2x^2 - 5x - 6$。$g(-1)$ 等于多少？", "$g(x) = x^3 + 2x^2 - 5x - 6$. What is $g(-1)$?", "0", "$-1 + 2 + 5 - 6 = 0$。", "$-1 + 2 + 5 - 6 = 0$.", 2, 0),
            ],
        )),
        chapter(7, "0580/0606 · 7", "函数", "Functions", L(
            "g9ma-7", "7",
            "定义域、值域、复合函数与反函数",
            "Domain, range, composite functions and inverses",
            "会写定义域和值域，按“先内后外”计算复合函数，并求一次函数的反函数。",
            "State a domain and a range, evaluate a composite function inside first, and find the inverse of a linear function.",
            [
                ("定义域是允许的输入，值域是对应得到的输出。", "The domain is the allowed inputs. The range is the outputs that actually occur."),
                ("本课程中 $fg(x)$ 表示 $f(g(x))$：先做 $g$，再做 $f$。", "In this course $fg(x)$ means $f(g(x))$: do $g$ first, then $f$."),
                ("反函数把输出送回原来的输入。一次函数 $f(x) = ax + b$ 的反函数是 $f^{-1}(x) = \\dfrac{x - b}{a}$。", "An inverse sends an output back to the input. For $f(x) = ax + b$, $f^{-1}(x) = \\dfrac{x - b}{a}$."),
                ("不是一一对应的函数在整个实数上没有反函数，需要先限制定义域。", "A function that is not one-to-one has no inverse on all real numbers until the domain is restricted."),
            ],
            "$f(x) = \\sqrt{x - 2}$ 要求 $x - 2 \\ge 0$，定义域是 $x \\ge 2$，值域是 $y \\ge 0$。先把根号下的式子写出来，再写限制，不要只写“$x$ 要合理”。\n\n复合函数交换顺序通常会改变结果。若 $f(x) = 2x + 1$，$g(x) = x^2$，则 $fg(x) = 2x^2 + 1$，而 $gf(x) = (2x + 1)^2$。反函数可以用“设 $y = f(x)$，改写成 $x = \\cdots$，再对调字母”来求，并用 $ff^{-1}(x) = x$ 检查。",
            "For $f(x) = \\sqrt{x - 2}$, $x - 2 \\ge 0$, so the domain is $x \\ge 2$ and the range is $y \\ge 0$. Write the expression under the root before you write the restriction.\n\nOrder matters. If $f(x) = 2x + 1$ and $g(x) = x^2$, then $fg(x) = 2x^2 + 1$ but $gf(x) = (2x + 1)^2$. To find an inverse, set $y = f(x)$, rearrange for $x$, then swap the letters. Check with $ff^{-1}(x) = x$.",
            "求 $f(x) = 3x - 1$ 的反函数。\n\n$y = 3x - 1$，$y + 1 = 3x$，$x = \\dfrac{y + 1}{3}$。所以 $f^{-1}(x) = \\dfrac{x + 1}{3}$。检查：$f(1) = 2$，$f^{-1}(2) = 1$。",
            "Find the inverse of $f(x) = 3x - 1$.\n\n$y = 3x - 1$, so $x = \\dfrac{y + 1}{3}$. Thus $f^{-1}(x) = \\dfrac{x + 1}{3}$. Check: $f(1) = 2$ and $f^{-1}(2) = 1$.",
            [
                ("把 $fg$ 做成先 $f$ 后 $g$。", "Doing $f$ before $g$ in $fg$."),
                ("反函数只把 $x$ 和 $y$ 对调，没有先解出 $x$。", "Swapping letters before rearranging for $x$."),
                ("$\\sqrt{x - 2}$ 的定义域写成 $x \\ge 0$。", "Writing the domain of $\\sqrt{x - 2}$ as $x \\ge 0$."),
            ],
            [
                short("$f(x) = 2x + 1$，$g(x) = x^2$。$fg(x)$ 是什么？", "$f(x) = 2x + 1$, $g(x) = x^2$. What is $fg(x)$?", "2x^2+1", "先平方，再乘 $2$ 加 $1$。", "Square first, then multiply by $2$ and add $1$.", ["2x^2+1", "2x^2 + 1"], 2),
                short("$f(x) = 3x - 1$ 的反函数是什么？", "What is the inverse of $f(x) = 3x - 1$?", "(x+1)/3", "解出 $x$ 再换字母。", "Rearrange for $x$, then swap letters.", ["(x+1)/3", "(x + 1)/3"], 2),
                short("$f(x) = \\sqrt{x - 2}$ 的定义域是什么？", "What is the domain of $f(x) = \\sqrt{x - 2}$?", "x≥2", "根号内大于等于 $0$。", "The expression under the root is at least $0$.", ["x≥2", "x >= 2", "x≥2", "x > = 2"], 1),
            ],
        )),
        chapter(8, "0580/0606 · 8", "坐标几何", "Coordinate geometry", L(
            "g9ma-8", "8",
            "直线方程、平行与垂直",
            "Equations of straight lines, parallel and perpendicular",
            "会由两点求直线方程，并写出与已知直线平行或垂直的直线。",
            "Find the equation of a line through two points, and write a line parallel or perpendicular to a given line.",
            [
                ("梯度 $m = \\dfrac{y_2 - y_1}{x_2 - x_1}$。", "The gradient is $m = \\dfrac{y_2 - y_1}{x_2 - x_1}$."),
                ("点斜式：$y - y_1 = m(x - x_1)$。", "Point-gradient form: $y - y_1 = m(x - x_1)$."),
                ("平行直线梯度相等。垂直直线（都不竖直时）梯度乘积为 $-1$。", "Parallel lines have equal gradients. Perpendicular lines, if neither is vertical, have gradients whose product is $-1$."),
                ("竖直线写成 $x = k$，没有梯度；与它垂直的是水平线 $y = c$。", "A vertical line is $x = k$ and has no gradient. A line perpendicular to it is horizontal, $y = c$."),
            ],
            "先算梯度，再代入一个已知点。过 $(0, 1)$ 和 $(4, 3)$ 的梯度是 $(3-1)/(4-0) = 1/2$，方程 $y - 1 = \\dfrac{1}{2}x$，即 $y = \\dfrac{1}{2}x + 1$。与它平行的直线梯度仍是 $1/2$；与它垂直的梯度是 $-2$。\n\n整理到 $y = mx + c$ 后再读梯度。$2x + y - 4 = 0$ 写成 $y = -2x + 4$，梯度是 $-2$，不是 $2$。",
            "Find the gradient first, then use one known point. Through $(0, 1)$ and $(4, 3)$ the gradient is $(3-1)/(4-0) = 1/2$, so $y - 1 = \\dfrac{1}{2}x$, or $y = \\dfrac{1}{2}x + 1$. A parallel line still has gradient $1/2$. A perpendicular line has gradient $-2$.\n\nRearrange to $y = mx + c$ before you read the gradient. $2x + y - 4 = 0$ is $y = -2x + 4$, so the gradient is $-2$, not $2$.",
            "求过 $(2, 5)$、与 $y = 3x - 1$ 垂直的直线。\n\n已知梯度 $3$，垂直梯度 $-1/3$。$y - 5 = -\\dfrac{1}{3}(x - 2)$。",
            "Find the line through $(2, 5)$ perpendicular to $y = 3x - 1$.\n\nThe given gradient is $3$, so the perpendicular gradient is $-1/3$. $y - 5 = -\\dfrac{1}{3}(x - 2)$.",
            [
                ("分子分母的点的顺序不一致，梯度符号算反。", "Using the points in a different order on the top and the bottom, so the sign of the gradient flips."),
                ("垂直梯度写成相反数，而不是负倒数。", "Using the negative of the gradient instead of the negative reciprocal."),
                ("从一般式里把 $x$ 的系数直接当成梯度。", "Taking the coefficient of $x$ in general form as the gradient."),
            ],
            [
                num("过 $(1, 4)$ 和 $(3, 10)$ 的直线，梯度是多少？", "What is the gradient of the line through $(1, 4)$ and $(3, 10)$?", "3", "$(10-4)/(3-1) = 3$。", "$(10-4)/(3-1) = 3$.", 1, 0),
                short("上题直线的方程写成 $y = mx + c$。", "Write the equation of that line as $y = mx + c$.", "y=3x+1", "$y - 4 = 3(x - 1)$，所以 $y = 3x + 1$。", "$y - 4 = 3(x - 1)$, so $y = 3x + 1$.", ["y=3x+1", "y = 3x + 1"], 2),
                short("与 $y = 2x - 5$ 垂直的直线，梯度是多少？", "What is the gradient of a line perpendicular to $y = 2x - 5$?", "-1/2", "负倒数是 $-1/2$。", "The negative reciprocal is $-1/2$.", ["-1/2", "-0.5"], 1),
            ],
        )),
    ],
    "paper": {
        "id": "paper-g9-maths",
        "title_zh": "练习卷 · 第 1–8 专题综合",
        "title_en": "Practice paper · Topics 1–8",
        "minutes": 60,
        "published": "2026-11-18T11:00:00+08:00",
        "items": [
            ("g9ma-1", num("$4.7$ 精确到小数点后 1 位。求下界。", "$4.7$ is correct to 1 decimal place. Find the lower bound.", "4.65", "减 $0.05$。", "Subtract $0.05$.", 2, 0)),
            ("g9ma-1", short("把 $0.\\dot{1}\\dot{8}$ 写成最简分数。", "Write $0.\\dot{1}\\dot{8}$ in lowest terms.", "2/11", "$18/99 = 2/11$。", "$18/99 = 2/11$.", ["2/11", "18/99"], 2)),
            ("g9ma-2", num("计算 $16^{3/4}$。", "Evaluate $16^{3/4}$.", "8", "$16^{1/4} = 2$，$2^3 = 8$。", "$16^{1/4} = 2$, and $2^3 = 8$.", 2, 0)),
            ("g9ma-2", short("化简 $\\sqrt{75}$。", "Simplify $\\sqrt{75}$.", "5√3", "$\\sqrt{25 \\times 3} = 5\\sqrt{3}$。", "$\\sqrt{25 \\times 3} = 5\\sqrt{3}$.", ["5√3", "5sqrt(3)", "5*sqrt(3)"], 2)),
            ("g9ma-3", short("解 $x^2 - 7x + 12 = 0$。", "Solve $x^2 - 7x + 12 = 0$.", "x=3 or x=4", "$(x-3)(x-4) = 0$。", "$(x-3)(x-4) = 0$.", ["x=3 or x=4", "3 and 4", "x=3, x=4", "3, 4"], 3)),
            ("g9ma-3", mcq("$x^2 + x + 4 = 0$ 的判别式是 $1 - 16 = -15$。这个方程？", "The discriminant of $x^2 + x + 4 = 0$ is $1 - 16 = -15$. The equation has:", "d", "没有实数根。", "No real roots.", [("两个不同实根", "two distinct real roots"), ("一个实根", "one real root"), ("无穷多个实根", "infinitely many real roots"), ("没有实数根", "no real roots")], 1)),
            ("g9ma-3", short("解 $x^2 - x - 6 > 0$。", "Solve $x^2 - x - 6 > 0$.", "x<-2 or x>3", "$(x-3)(x+2) > 0$。", "$(x-3)(x+2) > 0$.", ["x<-2 or x>3", "x < -2 or x > 3"], 3)),
            ("g9ma-3", short("解 $\\begin{cases} y = x - 1 \\\\ y = x^2 - 3 \\end{cases}$，写出两组 $(x, y)$。", "Solve the pair and give both points $(x, y)$.", "(2, 1) and (-1, -2)", "代入得 $x^2 - x - 2 = 0$，$(x-2)(x+1) = 0$。", "Substitution gives $x^2 - x - 2 = 0$, so $(x-2)(x+1) = 0$.", ["(2, 1) and (-1, -2)", "(2,1), (-1,-2)", "x=2, y=1 and x=-1, y=-2"], 4)),
            ("g9ma-4", num("$n(P) = 14$，$n(Q) = 11$，$n(P \\cap Q) = 5$。求 $n(P \\cup Q)$。", "$n(P) = 14$, $n(Q) = 11$, $n(P \\cap Q) = 5$. Find $n(P \\cup Q)$.", "20", "$14 + 11 - 5 = 20$。", "$14 + 11 - 5 = 20$.", 2, 0)),
            ("g9ma-5", mcq("图像有两支，以坐标轴为渐近线。它最可能是？", "A graph has two branches and the axes as asymptotes. It is most likely:", "b", "$y = k/x$。", "$y = k/x$.", [("$y = x^2$", "$y = x^2$"), ("$y = k/x$", "$y = k/x$"), ("$y = 2^x$", "$y = 2^x$"), ("$y = x + 1$", "$y = x + 1$")], 1)),
            ("g9ma-6", num("$f(x) = x^3 - 6x^2 + 11x - 6$。$f(1)$ 是多少？", "$f(x) = x^3 - 6x^2 + 11x - 6$. What is $f(1)$?", "0", "$1 - 6 + 11 - 6 = 0$，所以 $(x-1)$ 是因式。", "$1 - 6 + 11 - 6 = 0$, so $(x-1)$ is a factor.", 2, 0)),
            ("g9ma-7", short("$f(x) = x + 4$，$g(x) = 3x$。按本课程的顺序，$fg(4)$ 等于多少？", "Using this course’s order, what is $fg(4)$ if $f(x) = x + 4$ and $g(x) = 3x$?", "16", "先 $g(4) = 12$，再 $f(12) = 16$。", "$g(4) = 12$, then $f(12) = 16$.", ["16"], 2)),
            ("g9ma-7", short("$f(x) = 5x - 2$ 的反函数是什么？", "What is the inverse of $f(x) = 5x - 2$?", "(x+2)/5", "$x = (y+2)/5$。", "$x = (y+2)/5$.", ["(x+2)/5", "(x + 2)/5"], 2)),
            ("g9ma-8", short("直线过 $(0, 1)$ 与 $(4, 3)$。写出 $y = mx + c$ 形式的方程。", "A line passes through $(0, 1)$ and $(4, 3)$. Write it as $y = mx + c$.", "y=(1/2)x+1", "梯度 $1/2$，截距 $1$。", "The gradient is $1/2$ and the intercept is $1$.", ["y=(1/2)x+1", "y=0.5x+1", "y = x/2 + 1", "y=x/2+1"], 3)),
            ("g9ma-8", short("求过 $(0, 1)$、与 $y = 4x + 7$ 垂直的直线方程（$y = mx + c$）。", "Find the line through $(0, 1)$ perpendicular to $y = 4x + 7$, in the form $y = mx + c$.", "y=-x/4+1", "垂直梯度 $-1/4$，截距已经是 $1$。", "The perpendicular gradient is $-1/4$, and the intercept is already $1$.", ["y=-x/4+1", "y=-0.25x+1", "y = -x/4 + 1"], 3)),
        ],
    },
}
