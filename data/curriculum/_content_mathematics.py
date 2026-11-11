"""Grade 8 Mathematics — complete bilingual course (Cambridge Lower Secondary Mathematics 0862 Stage 8)."""
from _helpers import opts
from _course_util import Course, maps_from_units, svg, INK, ACCENT
from _apply import add_lesson, add_extra_questions, add_sets
from _compact import bullets, diffs, body as pack_body

UNIT_OF, CHAPTER_OF = maps_from_units("mathematics")
C = Course("mathematics", UNIT_OF, CHAPTER_OF, recent={
    "mathematics-8-1-2": "2026-11-12T09:00:00+08:00",
    "mathematics-8-2-2": "2026-11-11T09:00:00+08:00",
    "mathematics-8-7-2": "2026-11-10T09:00:00+08:00",
    "mathematics-8-9-3": "2026-11-09T09:00:00+08:00",
}, tag="ma")

def fig(inner, w=520, h=220):
    return svg(inner.replace("{INK}", INK).replace("{ACC}", ACCENT), w=w, h=h)

D_LINE = fig("""
  <line x1="60" y1="190" x2="500" y2="190" {INK}/>
  <line x1="80" y1="200" x2="80" y2="20" {INK}/>
  <polyline points="80,190 200,130 400,30" {ACC}/>
  <text x="420" y="40" font-size="13" fill="currentColor">y = mx + c</text>
  <text x="490" y="210" font-size="12" fill="currentColor">x</text>
  <text x="50" y="28" font-size="12" fill="currentColor">y</text>
""")
D_CIRC = fig("""
  <circle cx="180" cy="110" r="70" {INK}/>
  <line x1="180" y1="110" x2="250" y2="110" {ACC}/>
  <text x="200" y="100" font-size="13" fill="#b85c38">r</text>
  <text x="280" y="80" font-size="14" fill="currentColor">C = 2πr</text>
  <text x="280" y="110" font-size="14" fill="currentColor">A = πr²</text>
""")
D_VEC = fig("""
  <line x1="80" y1="160" x2="260" y2="60" {ACC}/>
  <polygon points="260,60 246,62 252,74" fill="#b85c38"/>
  <text x="180" y="90" font-size="13" fill="#b85c38">(6, -4) wait</text>
  <text x="160" y="50" font-size="13" fill="currentColor">translation vector</text>
  <line x1="80" y1="160" x2="80" y2="40" {INK} stroke-dasharray="4 3"/>
  <line x1="80" y1="160" x2="300" y2="160" {INK} stroke-dasharray="4 3"/>
  <text x="40" y="100" font-size="12" fill="currentColor">y</text>
  <text x="200" y="180" font-size="12" fill="currentColor">x</text>
""")

LESSONS = []

def L(sid, title_zh, title_en, obj_zh, obj_en, points, explain_zh, explain_en, ex_zh, ex_en, traps, questions, diagram=None):
    kp_zh, kp_en = bullets(points)
    body_zh, body_en = pack_body(explain_zh, explain_en, ex_zh, ex_en)
    diff_zh, diff_en = diffs(traps)
    LESSONS.append(dict(
        id=sid, title_zh=title_zh, title_en=title_en,
        obj_zh=obj_zh, obj_en=obj_en, kp_zh=kp_zh, kp_en=kp_en,
        body_zh=body_zh, body_en=body_en, diff_zh=diff_zh, diff_en=diff_en,
        questions=questions, diagram=diagram or "",
    ))

# ---------- 8.1 ----------
L("mathematics-8-1-1", "数位与近似", "Place value and rounding",
  "本节你将学会用数位理解整数与小数，并按要求把数四舍五入到指定数位。",
  "This lesson you will use place value for integers and decimals, and round numbers to a required place.",
  [("每个数位的值是右边相邻数位的 $10$ 倍，是左边的十分之一。", "Each place is worth $10$ times the place to its right, and one tenth of the place to its left."),
   ("四舍五入看**下一位**：满 $5$ 则入，否则舍。", "To round, look at the next digit: $5$ or more rounds up, otherwise you leave it."),
   ("可四舍五入到最近的 $10$、$100$、$1000$，或到小数点后一位、两位等。", "You can round to the nearest $10$, $100$ or $1000$, or to one or two decimal places."),
   ("近似值要写清精确到哪一位，以免被当成准确值。", "State the place you rounded to, so the value is not mistaken for an exact figure.")],
  r"""数位是理解大小的骨架。例如在 $3\,047.26$ 里，$4$ 在十位，表示 $40$；$2$ 在十分位，表示 $0.2$。把一个数四舍五入，是为了给出合适的近似，而不是随便丢掉数字。

规则要看“被保留的最后一位”的下一位。例如把 $3\,047$ 四舍五入到最近的 $100$：看十位的 $4$，不足 $5$，所以是 $3\,000$。把 $3.46$ 保留一位小数：看百分位的 $6$，要入上去，得到 $3.5$。""",
  r"""Place value is the framework for size. In $3\,047.26$, the $4$ is in the tens place and means $40$; the $2$ is in the tenths place and means $0.2$. Rounding gives a suitable approximation; it is not the same as deleting digits at random.

Look at the digit after the last one you are keeping. Rounding $3\,047$ to the nearest $100$: the tens digit is $4$, which is less than $5$, so the result is $3\,000$. Rounding $3.46$ to one decimal place: the hundredths digit is $6$, so it rounds up to $3.5$.""",
  r"""把 $7\,250$ 四舍五入到最近的 $100$，以及把 $6.35$ 保留一位小数。

**解：** $7\,250$ 的十位是 $5$，按“满 $5$ 则入”，得到 $7\,300$。$6.35$ 的百分位是 $5$，保留一位小数得 $6.4$。""",
  r"""Round $7\,250$ to the nearest $100$, and round $6.35$ to one decimal place.

**Solution:** In $7\,250$ the tens digit is $5$, so it rounds up to $7\,300$. In $6.35$ the hundredths digit is $5$, so to one decimal place it becomes $6.4$.""",
  [("看错数位，例如把十分位当成十位。", "Reading the wrong place, for example treating tenths as tens."),
   ("该看下一位时却看了再下一位。", "Looking two digits ahead instead of the next digit."),
   ("逢 $5$ 时犹豫。本课采用常见规则：下一位是 $5$ 或更大就入。", "Hesitating at $5$. In this course, $5$ or more rounds up.")],
  [
    dict(type="mcq", stem_zh="在 $4\\,086.37$ 中，数字 $3$ 表示？", stem_en="In $4\\,086.37$, the digit $3$ stands for:",
         answer="c", exp_zh="$3$ 在十分位，表示 $0.3$。", exp_en="The $3$ is in the tenths place, so it means $0.3$.",
         options=opts(("$3$", "$3$"), ("$30$", "$30$"), ("$0.3$", "$0.3$"), ("$0.03$", "$0.03$"))),
    dict(type="numeric", stem_zh="把 $3\\,047$ 四舍五入到最近的 $100$。", stem_en="Round $3\\,047$ to the nearest $100$.",
         answer=3000, exp_zh="十位是 $4$，不足 $5$，所以是 $3\\,000$。", exp_en="The tens digit is $4$, so it rounds to $3\\,000$.", tolerance=0),
    dict(type="numeric", stem_zh="把 $7\\,250$ 四舍五入到最近的 $100$。", stem_en="Round $7\\,250$ to the nearest $100$.",
         answer=7300, exp_zh="十位是 $5$，入上去得到 $7\\,300$。", exp_en="The tens digit is $5$, so it rounds up to $7\\,300$.", tolerance=0),
    dict(type="numeric", stem_zh="把 $3.46$ 四舍五入到一位小数。", stem_en="Round $3.46$ to one decimal place.",
         answer=3.5, exp_zh="百分位是 $6$，保留一位小数得 $3.5$。", exp_en="The hundredths digit is $6$, so it becomes $3.5$.", tolerance=0.01),
    dict(type="numeric", stem_zh="把 $6.35$ 四舍五入到一位小数。", stem_en="Round $6.35$ to one decimal place.",
         answer=6.4, exp_zh="百分位是 $5$，入上去得 $6.4$。", exp_en="The hundredths digit is $5$, so it becomes $6.4$.", tolerance=0.01),
    dict(type="mcq", stem_zh="把 $48.162$ 四舍五入到两位小数，结果是？", stem_en="Round $48.162$ to two decimal places.",
         answer="b", exp_zh="千分位是 $2$，不足 $5$，所以是 $48.16$。", exp_en="The thousandths digit is $2$, so the result is $48.16$.",
         options=opts(("$48.17$", "$48.17$"), ("$48.16$", "$48.16$"), ("$48.20$", "$48.20$"), ("$48.10$", "$48.10$"))),
  ])

L("mathematics-8-1-2", "指数、因数与倍数", "Indices, factors and multiples",
  "本节你将学会使用正整数指数与零指数、指数律，并求最高公因数与最低公倍数。",
  "This lesson you will use positive and zero indices and the index laws, and find highest common factors and lowest common multiples.",
  [("$a^n$ 表示 $n$ 个 $a$ 相乘；$a^0=1$（$a\\neq 0$）。", "$a^n$ means $n$ factors of $a$; $a^0=1$ ($a\\neq 0$)."),
   ("同底数：$a^m\\times a^n=a^{m+n}$，$a^m\\div a^n=a^{m-n}$（$a\\neq 0$）。", "Same base: $a^m\\times a^n=a^{m+n}$, $a^m\\div a^n=a^{m-n}$ ($a\\neq 0$)."),
   ("质因数分解把整数写成质数的乘积。", "Prime factorisation writes a whole number as a product of primes."),
   ("HCF 取共有质因数的最低次幂；LCM 取全部质因数的最高次幂。", "The HCF takes the lowest power of shared primes; the LCM takes the highest power of every prime that appears.")],
  r"""第 8 阶段的指数先集中在正整数指数和零指数。$2^5=32$。同底数相乘，指数相加；相除，指数相减。$5^0=1$。还要注意 $(-3)^2=9$，但 $-3^2=-9$，因为后者是“先算 $3^2$ 再取负”。

求 $24$ 与 $36$ 的 HCF 和 LCM，先分解：$24=2^3\times 3$，$36=2^2\times 3^2$。HCF $=2^2\times 3=12$，LCM $=2^3\times 3^2=72$。可用 $\operatorname{HCF}\times\operatorname{LCM}=$ 两数之积来检验。""",
  r"""Stage 8 indices start with positive and zero powers. $2^5=32$. For the same base, multiply by adding indices and divide by subtracting them. $5^0=1$. Also note that $(-3)^2=9$ but $-3^2=-9$, because the second expression squares $3$ first and then takes the negative.

To find the HCF and LCM of $24$ and $36$, factorise: $24=2^3\times 3$, $36=2^2\times 3^2$. HCF $=2^2\times 3=12$, LCM $=2^3\times 3^2=72$. You can check with $\operatorname{HCF}\times\operatorname{LCM}=$ the product of the two numbers.""",
  r"""计算 $2^5\times 2^3$，并求 $18$ 与 $24$ 的 HCF。

**解：** $2^5\times 2^3=2^8=256$。$18=2\times 3^2$，$24=2^3\times 3$，HCF $=2\times 3=6$。""",
  r"""Evaluate $2^5\times 2^3$ and find the HCF of $18$ and $24$.

**Solution:** $2^5\times 2^3=2^8=256$. $18=2\times 3^2$, $24=2^3\times 3$, so HCF $=2\times 3=6$.""",
  [("把指数相乘当成底数相加，或把 $a^m\\times a^n$ 写成 $a^{mn}$。", "Adding the bases, or writing $a^m\\times a^n$ as $a^{mn}$."),
   ("以 $0$ 为底却写 $0^0$，或把 $a^0$ 写成 $0$。", "Writing $0^0$, or claiming that $a^0=0$."),
   ("把 HCF 和 LCM 求反：HCF 应取最低次幂。", "Swapping HCF and LCM: the HCF uses the lowest powers.")],
  [
    dict(type="numeric", stem_zh="计算 $2^5\\times 2^3$。", stem_en="Evaluate $2^5\\times 2^3$.",
         answer=256, exp_zh="$2^{5+3}=2^8=256$。", exp_en="$2^{5+3}=2^8=256$.", tolerance=0),
    dict(type="numeric", stem_zh="计算 $3^6\\div 3^4$。", stem_en="Evaluate $3^6\\div 3^4$.",
         answer=9, exp_zh="$3^{6-4}=3^2=9$。", exp_en="$3^{6-4}=3^2=9$.", tolerance=0),
    dict(type="numeric", stem_zh="$7^0$ 等于多少？（$7\\neq 0$）", stem_en="What is $7^0$? ($7\\neq 0$)",
         answer=1, exp_zh="非零数的零次幂等于 $1$。", exp_en="A non-zero number to the power $0$ equals $1$.", tolerance=0),
    dict(type="numeric", stem_zh="求 $18$ 与 $24$ 的最高公因数（HCF）。", stem_en="Find the HCF of $18$ and $24$.",
         answer=6, exp_zh="$18=2\\times 3^2$，$24=2^3\\times 3$，HCF $=2\\times 3=6$。", exp_en="$18=2\\times 3^2$, $24=2^3\\times 3$, HCF $=2\\times 3=6$.", tolerance=0),
    dict(type="numeric", stem_zh="求 $18$ 与 $24$ 的最低公倍数（LCM）。", stem_en="Find the LCM of $18$ and $24$.",
         answer=72, exp_zh="LCM $=2^3\\times 3^2=8\\times 9=72$。", exp_en="LCM $=2^3\\times 3^2=8\\times 9=72$.", tolerance=0),
    dict(type="mcq", stem_zh="$(-3)^2$ 与 $-3^2$ 分别等于？", stem_en="What are $(-3)^2$ and $-3^2$?",
         answer="d", exp_zh="$(-3)^2=9$，而 $-3^2=-9$。", exp_en="$(-3)^2=9$, but $-3^2=-9$.",
         options=opts(("$9$ 和 $9$", "$9$ and $9$"), ("$-9$ 和 $-9$", "$-9$ and $-9$"), ("$-9$ 和 $9$", "$-9$ and $9$"), ("$9$ 和 $-9$", "$9$ and $-9$"))),
  ])

L("mathematics-8-1-3", "整数与小数运算", "Calculating with integers and decimals",
  "本节你将学会正确进行整数与小数的四则运算，并遵守运算顺序。",
  "This lesson you will calculate with integers and decimals, following the correct order of operations.",
  [("运算顺序：括号、指数（含根），再乘除（从左到右），再加减（从左到右）。", "Order: brackets, indices (including roots), then multiply and divide left to right, then add and subtract left to right."),
   ("小数加减要对齐小数点。", "Line up decimal points when adding or subtracting decimals."),
   ("小数乘法：先按整数乘，再数因数中的小数位数。", "For decimal multiplication, multiply as whole numbers, then count decimal places in the factors."),
   ("小数除法：被除数和除数同乘 $10$ 的幂，使除数变成整数。", "For decimal division, multiply dividend and divisor by the same power of $10$ so the divisor is a whole number."),
   ("负数运算要单独看符号，再算绝对值。", "With negatives, deal with the sign separately from the absolute values.")],
  r"""第 8 阶段要求运算又快又准，关键是顺序和数位。例如 $3+4\times 5=23$，不是 $35$。小数加法把小数点对齐：$3.6+0.45=4.05$。

乘法 $1.2\times 0.3$：先算 $12\times 3=36$，因数里一共有两位小数，所以是 $0.36$。除法 $1.44\div 0.12$：两边同乘 $100$，变成 $144\div 12=12$。""",
  r"""Stage 8 asks for accurate calculation with a reliable order of operations. For example $3+4\times 5=23$, not $35$. When adding decimals, line up the points: $3.6+0.45=4.05$.

For $1.2\times 0.3$, first compute $12\times 3=36$. The factors have two decimal places in total, so the product is $0.36$. For $1.44\div 0.12$, multiply both numbers by $100$ to obtain $144\div 12=12$.""",
  r"""计算 $12-3\times 2^2$ 和 $2.4\div 0.06$。

**解：** 先算指数 $2^2=4$，再乘：$3\times 4=12$，最后 $12-12=0$。$2.4\div 0.06$：两边乘 $100$，得 $240\div 6=40$。""",
  r"""Evaluate $12-3\times 2^2$ and $2.4\div 0.06$.

**Solution:** Indices first: $2^2=4$. Then $3\times 4=12$, so $12-12=0$. For $2.4\div 0.06$, multiply both by $100$ to get $240\div 6=40$.""",
  [("从左到右把加减做在乘除前面。", "Working left to right through addition before multiplication."),
   ("小数乘法忘记数小数位。", "Forgetting to count decimal places in a product."),
   ("除小数时只移动了除数或只移动了被除数。", "Moving the point in only the divisor or only the dividend.")],
  [
    dict(type="numeric", stem_zh="计算 $3+4\\times 5$。", stem_en="Evaluate $3+4\\times 5$.",
         answer=23, exp_zh="先乘后加：$20+3=23$。", exp_en="Multiply first: $20+3=23$.", tolerance=0),
    dict(type="numeric", stem_zh="计算 $12-3\\times 2^2$。", stem_en="Evaluate $12-3\\times 2^2$.",
         answer=0, exp_zh="$2^2=4$，$3\\times 4=12$，$12-12=0$。", exp_en="$2^2=4$, $3\\times 4=12$, $12-12=0$.", tolerance=0),
    dict(type="numeric", stem_zh="计算 $1.2\\times 0.3$。", stem_en="Evaluate $1.2\\times 0.3$.",
         answer=0.36, exp_zh="$12\\times 3=36$，共两位小数，得 $0.36$。", exp_en="$12\\times 3=36$, two decimal places, so $0.36$.", tolerance=0.001),
    dict(type="numeric", stem_zh="计算 $2.4\\div 0.06$。", stem_en="Evaluate $2.4\\div 0.06$.",
         answer=40, exp_zh="两边乘 $100$ 得 $240\\div 6=40$。", exp_en="Multiply both by $100$: $240\\div 6=40$.", tolerance=0),
    dict(type="numeric", stem_zh="计算 $3.6+0.45$。", stem_en="Evaluate $3.6+0.45$.",
         answer=4.05, exp_zh="对齐小数点：$3.60+0.45=4.05$。", exp_en="Line up the points: $3.60+0.45=4.05$.", tolerance=0.001),
    dict(type="mcq", stem_zh="计算 $-8+3\\times(-2)$ 的结果是？", stem_en="What is $-8+3\\times(-2)$?",
         answer="b", exp_zh="先乘：$3\\times(-2)=-6$，再 $-8+(-6)=-14$。", exp_en="Multiply first: $3\\times(-2)=-6$, then $-8+(-6)=-14$.",
         options=opts(("$-10$", "$-10$"), ("$-14$", "$-14$"), ("$14$", "$14$"), ("$-2$", "$-2$"))),
  ])

L("mathematics-8-2-1", "代数式、表达式与公式", "Manipulating algebra, expressions and formulae",
  "本节你将学会化简代数式、展开括号、代入求值，并变形简单公式。",
  "This lesson you will simplify expressions, expand brackets, substitute values, and rearrange simple formulae.",
  [("同类项才能合并：$3x+5x=8x$，但 $3x+5$ 不能合成一项。", "Only like terms combine: $3x+5x=8x$, but $3x+5$ cannot be written as a single term."),
   ("展开：$a(b+c)=ab+ac$。", "Expand: $a(b+c)=ab+ac$."),
   ("代入时先把数值放进括号，再按运算顺序计算。", "When substituting, put values in brackets first, then follow the order of operations."),
   ("变形公式时，两边做同样的运算，把目标字母单独留在一边。", "To rearrange a formula, do the same to both sides until the target letter is alone.")],
  r"""代数用字母代表数。化简是把能合并的项合并，使式子更短、更清楚。$4a+3b-a=3a+3b$。展开括号则是把乘法分配进去：$2(x+5)=2x+10$。

代入是把字母换成数。求 $3x^2$ 当 $x=-2$ 时的值：$3(-2)^2=3\times 4=12$，不要算成 $-12$。公式变形与解方程是同一思路，例如由 $v=s/t$ 得 $s=vt$。""",
  r"""Algebra uses letters for numbers. Simplifying means collecting like terms so the expression is shorter and clearer: $4a+3b-a=3a+3b$. Expanding means using the distributive law: $2(x+5)=2x+10$.

Substitution means replacing a letter with a number. If $x=-2$, then $3x^2=3(-2)^2=3\times 4=12$, not $-12$. Rearranging a formula uses the same idea as solving an equation: from $v=s/t$ you obtain $s=vt$.""",
  r"""化简 $5(x-2)+3x$，并由 $A=lw$ 用 $A$ 和 $l$ 表示 $w$。

**解：** $5x-10+3x=8x-10$。两边同除以 $l$（$l\\neq 0$），得 $w=A/l$。""",
  r"""Simplify $5(x-2)+3x$, and make $w$ the subject of $A=lw$.

**Solution:** $5x-10+3x=8x-10$. Divide both sides by $l$ ($l\\neq 0$) to get $w=A/l$.""",
  [("把 $3x+5$ 写成 $8x$。", "Writing $3x+5$ as $8x$."),
   ("代入负数时忘记平方结果为正。", "Forgetting that the square of a negative is positive."),
   ("变形公式时只动一边。", "Changing only one side of a formula.")],
  [
    dict(type="short", stem_zh="化简 $4a+3b-a$。", stem_en="Simplify $4a+3b-a$.",
         answer="3a+3b", accepted=["3a+3b", "3a + 3b", "3(a+b)", "3a+3b ", "3a＋3b"],
         answer_zh="$3a+3b$", answer_en="$3a+3b$", exp_zh="$4a-a=3a$，再加上 $3b$。", exp_en="$4a-a=3a$, then add $3b$."),
    dict(type="short", stem_zh="展开并化简 $5(x-2)+3x$。", stem_en="Expand and simplify $5(x-2)+3x$.",
         answer="8x-10", accepted=["8x-10", "8x - 10", "-10+8x", "8x−10"],
         answer_zh="$8x-10$", answer_en="$8x-10$", exp_zh="$5x-10+3x=8x-10$。", exp_en="$5x-10+3x=8x-10$."),
    dict(type="numeric", stem_zh="当 $x=-2$ 时，$3x^2$ 的值是多少？", stem_en="What is the value of $3x^2$ when $x=-2$?",
         answer=12, exp_zh="$3(-2)^2=3\\times 4=12$。", exp_en="$3(-2)^2=3\\times 4=12$.", tolerance=0),
    dict(type="short", stem_zh="由 $A=lw$ 用 $A$ 和 $l$ 表示 $w$。", stem_en="Make $w$ the subject of $A=lw$.",
         answer="w=A/l", accepted=["w=A/l", "w = A/l", "w=A÷l", "w＝A/l"],
         answer_zh="$w=A/l$", answer_en="$w=A/l$", exp_zh="两边同除以 $l$。", exp_en="Divide both sides by $l$."),
    dict(type="mcq", stem_zh="$2(x+5)$ 展开后是？", stem_en="The expansion of $2(x+5)$ is:",
         answer="a", exp_zh="$2x+10$。", exp_en="$2x+10$.",
         options=opts(("$2x+10$", "$2x+10$"), ("$2x+5$", "$2x+5$"), ("$x+10$", "$x+10$"), ("$2x+7$", "$2x+7$"))),
    dict(type="numeric", stem_zh="当 $a=3$，$b=4$ 时，$2a+5b$ 等于多少？", stem_en="If $a=3$ and $b=4$, what is $2a+5b$?",
         answer=26, exp_zh="$2\\times 3+5\\times 4=6+20=26$。", exp_en="$2\\times 3+5\\times 4=6+20=26$.", tolerance=0),
  ])

L("mathematics-8-2-2", "方程与不等式", "Equations and inequalities",
  "本节你将学会解一元一次方程与简单不等式，并在数轴上表示解集。",
  "This lesson you will solve linear equations and simple inequalities in one unknown, and show solution sets on a number line.",
  [("解方程时两边做同样的运算，保持相等。", "When you solve an equation, do the same to both sides so equality is kept."),
   ("先去括号或合并同类项，再把未知数移到一边。", "Expand or collect like terms first, then gather the unknown on one side."),
   ("不等式的解通常是一个范围，不是单个数。", "The solution of an inequality is usually a range, not a single number."),
   ("两边同乘或同除一个负数时，不等号要反向。", "If you multiply or divide both sides by a negative number, reverse the inequality sign.")],
  r"""方程是在找使两边相等的未知数。例如 $2x+5=17$，两边减 $5$ 得 $2x=12$，再除以 $2$ 得 $x=6$。可用代入检验。

不等式如 $2x+1>7$ 的解法类似，得到 $x>3$。所有大于 $3$ 的数都是解。若从 $-2x>6$ 两边除以 $-2$，必须写成 $x<-3$。""",
  r"""An equation asks for the unknown that makes both sides equal. From $2x+5=17$, subtract $5$ to get $2x=12$, then divide by $2$ to get $x=6$. Check by substituting back.

An inequality such as $2x+1>7$ is solved in a similar way and gives $x>3$. Every number greater than $3$ is a solution. If you start from $-2x>6$ and divide by $-2$, you must write $x<-3$.""",
  r"""解 $3(x-2)=12$ 和 $5-2x\\le 1$。

**解：** $3x-6=12$，$3x=18$，$x=6$。$5-2x\\le 1$，$-2x\\le -4$，两边除以 $-2$ 并反向，得 $x\\ge 2$。""",
  r"""Solve $3(x-2)=12$ and $5-2x\\le 1$.

**Solution:** $3x-6=12$, so $3x=18$ and $x=6$. From $5-2x\\le 1$, $-2x\\le -4$. Divide by $-2$ and reverse the sign: $x\\ge 2$.""",
  [("移项时忘记变号。", "Forgetting to change the sign when a term moves side."),
   ("两边除以负数却不反向不等号。", "Dividing by a negative without reversing the inequality."),
   ("把不等式的解写成一个数。", "Writing a single number as the solution of an inequality.")],
  [
    dict(type="numeric", stem_zh="解方程 $2x+5=17$。$x$ 等于多少？", stem_en="Solve $2x+5=17$. What is $x$?",
         answer=6, exp_zh="$2x=12$，$x=6$。", exp_en="$2x=12$, so $x=6$.", tolerance=0),
    dict(type="numeric", stem_zh="解方程 $3(x-2)=12$。$x$ 等于多少？", stem_en="Solve $3(x-2)=12$. What is $x$?",
         answer=6, exp_zh="$3x-6=12$，$3x=18$，$x=6$。", exp_en="$3x-6=12$, $3x=18$, $x=6$.", tolerance=0),
    dict(type="mcq", stem_zh="$2x+1>7$ 的解是？", stem_en="The solution of $2x+1>7$ is:",
         answer="c", exp_zh="$2x>6$，所以 $x>3$。", exp_en="$2x>6$, so $x>3$.",
         options=opts(("$x>7$", "$x>7$"), ("$x=3$", "$x=3$"), ("$x>3$", "$x>3$"), ("$x<3$", "$x<3$"))),
    dict(type="mcq", stem_zh="由 $-2x>6$ 可得？", stem_en="From $-2x>6$ you obtain:",
         answer="a", exp_zh="两边除以 $-2$ 要反向，得 $x<-3$。", exp_en="Divide by $-2$ and reverse: $x<-3$.",
         options=opts(("$x<-3$", "$x<-3$"), ("$x>-3$", "$x>-3$"), ("$x<-6$", "$x<-6$"), ("$x>6$", "$x>6$"))),
    dict(type="mcq", stem_zh="$5-2x\\le 1$ 的解是？", stem_en="The solution of $5-2x\\le 1$ is:",
         answer="d", exp_zh="$-2x\\le -4$，反向后 $x\\ge 2$。", exp_en="$-2x\\le -4$, then reverse to get $x\\ge 2$.",
         options=opts(("$x\\le 2$", "$x\\le 2$"), ("$x=2$ 只取等号", "$x=2$ only"), ("$x>2$", "$x>2$"), ("$x\\ge 2$", "$x\\ge 2$"))),
    dict(type="numeric", stem_zh="解方程 $4x-3=2x+9$。$x$ 等于多少？", stem_en="Solve $4x-3=2x+9$. What is $x$?",
         answer=6, exp_zh="$4x-2x=9+3$，$2x=12$，$x=6$。", exp_en="$4x-2x=9+3$, $2x=12$, $x=6$.", tolerance=0),
  ])

L("mathematics-8-3-1", "四边形与多边形", "Quadrilaterals and polygons",
  "本节你将学会识别常见四边形和多边形，并使用内角和等性质。",
  "This lesson you will recognise common quadrilaterals and polygons and use properties such as the sum of interior angles.",
  [("$n$ 边多边形内角和是 $(n-2)\\times 180^\\circ$。", "The sum of interior angles of an $n$-sided polygon is $(n-2)\\times 180^\\circ$."),
   ("四边形内角和是 $360^\\circ$。", "The interior angles of a quadrilateral add to $360^\\circ$."),
   ("正方形、长方形、菱形、平行四边形、梯形各有特定的边角与平行性质。", "Squares, rectangles, rhombi, parallelograms and trapeziums have their own side, angle and parallel properties."),
   ("正多边形每一个内角相等。", "In a regular polygon every interior angle is equal.")],
  r"""先根据边数和性质给图形命名，再算角。四边形内角和 $360^\\circ$，所以三个角为 $80^\\circ$、$90^\\circ$、$110^\\circ$ 时，第四个角是 $80^\\circ$。五边形内角和 $(5-2)\\times 180^\\circ=540^\\circ$。正五边形每个内角 $540^\\circ\\div 5=108^\\circ$。

平行四边形对边平行且相等，对角相等；长方形四个角都是直角；菱形四边相等；正方形兼有两者。""",
  r"""Name a shape from its sides and properties, then find angles. The angles in a quadrilateral add to $360^\\circ$, so if three angles are $80^\\circ$, $90^\\circ$ and $110^\\circ$, the fourth is $80^\\circ$. A pentagon has angle sum $(5-2)\\times 180^\\circ=540^\\circ$. Each interior angle of a regular pentagon is $540^\\circ\\div 5=108^\\circ$.

In a parallelogram, opposite sides are parallel and equal, and opposite angles are equal. A rectangle has four right angles; a rhombus has four equal sides; a square has both sets of properties.""",
  r"""正六边形的每一个内角是多少度？

**解：** 内角和 $(6-2)\\times 180^\\circ=720^\\circ$，每个内角 $720^\\circ\\div 6=120^\\circ$。""",
  r"""What is each interior angle of a regular hexagon?

**Solution:** The sum is $(6-2)\\times 180^\\circ=720^\\circ$, so each angle is $720^\\circ\\div 6=120^\\circ$.""",
  [("把内角和记成 $n\\times 180^\\circ$。应为 $(n-2)\\times 180^\\circ$。", "Using $n\\times 180^\\circ$ instead of $(n-2)\\times 180^\\circ$."),
   ("把菱形与长方形的性质说反。", "Swapping the properties of a rhombus and a rectangle."),
   ("不规则多边形也用“每个内角=总和除以边数”。", "Dividing the sum by $n$ for a polygon that is not regular.")],
  [
    dict(type="numeric", stem_zh="四边形三个内角为 $80^\\circ$、$90^\\circ$、$110^\\circ$。第四个内角是多少度？",
         stem_en="Three angles of a quadrilateral are $80^\\circ$, $90^\\circ$ and $110^\\circ$. What is the fourth angle in degrees?",
         answer=80, exp_zh="$360-80-90-110=80$。", exp_en="$360-80-90-110=80$.", tolerance=0),
    dict(type="numeric", stem_zh="五边形的内角和是多少度？", stem_en="What is the sum of the interior angles of a pentagon, in degrees?",
         answer=540, exp_zh="$(5-2)\\times 180=540$。", exp_en="$(5-2)\\times 180=540$.", tolerance=0),
    dict(type="numeric", stem_zh="正六边形的每一个内角是多少度？", stem_en="Each interior angle of a regular hexagon, in degrees?",
         answer=120, exp_zh="$720\\div 6=120$。", exp_en="$720\\div 6=120$.", tolerance=0),
    dict(type="mcq", stem_zh="哪一个性质属于菱形，却不一定属于普通长方形？", stem_en="Which property belongs to a rhombus but not necessarily to a rectangle that is not a square?",
         answer="b", exp_zh="菱形四边相等；普通长方形对边相等，邻边一般不等。", exp_en="A rhombus has four equal sides; an ordinary rectangle has equal opposite sides, but adjacent sides need not be equal.",
         options=opts(("四个角都是直角", "four right angles"), ("四条边都相等", "four equal sides"),
                      ("只有一条边", "only one side"), ("内角和不是 $360^\\circ$", "an angle sum other than $360^\\circ$"))),
    dict(type="numeric", stem_zh="正八边形的内角和是多少度？", stem_en="The sum of interior angles of a regular octagon, in degrees?",
         answer=1080, exp_zh="$(8-2)\\times 180=1080$。", exp_en="$(8-2)\\times 180=1080$.", tolerance=0),
    dict(type="mcq", stem_zh="平行四边形一定具有的性质是？", stem_en="A parallelogram always has:",
         answer="a", exp_zh="对边平行且相等，对角相等。", exp_en="Opposite sides parallel and equal, and opposite angles equal.",
         options=opts(("对边平行", "opposite sides parallel"), ("四个角都是直角", "four right angles"),
                      ("四边一定都相等", "four sides that must all be equal"), ("只有一组对边平行", "exactly one pair of parallel sides"))),
  ])

L("mathematics-8-3-2", "面积、周长与圆周", "Area, perimeter and circumference",
  "本节你将学会计算常见平面图形的周长和面积，包括圆的周长与面积。",
  "This lesson you will calculate the perimeter and area of common plane shapes, including the circumference and area of a circle.",
  [("周长是封闭图形边界的总长度；面积是它所围的面的大小。", "Perimeter is the total length of the boundary; area is the size of the surface enclosed."),
   ("矩形面积 $l\\times w$，三角形面积 $\\dfrac{1}{2}bh$，平行四边形面积 $b\\times h$（$h$ 是垂直高度）。", "Rectangle $l\\times w$; triangle $\\dfrac{1}{2}bh$; parallelogram $b\\times h$ (perpendicular height)."),
   ("圆的周长 $C=2\\pi r=\\pi d$，面积 $A=\\pi r^2$。", "Circumference $C=2\\pi r=\\pi d$; area $A=\\pi r^2$."),
   ("复合图形可分割成已知图形再相加或相减。", "A composite shape can be split into known shapes, then added or subtracted.")],
  r"""先分清问的是“边有多长”还是“面有多大”。单位也不同：周长是 $\\mathrm{cm}$，面积是 $\\mathrm{cm}^2$。圆的公式里要用半径还是直径，看题目给的是哪一个。$d=2r$。若题目要求用 $\\pi$ 表示，就保留 $\\pi$；若要求近似值，按题目指定取 $3.14$ 或计算器的 $\\pi$。

本站数值题若未特别说明，圆的计算取 $\\pi=3.14$ 的合理近似，或在可用精确值时保留整数答案。""",
  r"""First decide whether the question asks how long the boundary is, or how much surface is enclosed. The units differ: centimetres for perimeter, square centimetres for area. For a circle, use radius or diameter according to what is given: $d=2r$. If the question asks for an answer in terms of $\\pi$, keep $\\pi$; if it asks for an approximation, use $3.14$ or the calculator value as instructed.

In numerical questions on this site, unless told otherwise, use a sensible approximation such as $\\pi=3.14$, or give an exact integer where it arises cleanly.""",
  r"""半径 $5\\ \\mathrm{cm}$ 的圆，面积是多少 $\\mathrm{cm}^2$？（取 $\\pi=3.14$）长 $8\\ \\mathrm{cm}$、宽 $3\\ \\mathrm{cm}$ 的矩形，周长是多少厘米？

**解：** 面积 $3.14\\times 5^2=3.14\\times 25=78.5$。周长 $2(8+3)=22$。""",
  r"""A circle has radius $5\\ \\mathrm{cm}$. What is its area in $\\mathrm{cm}^2$? (Use $\\pi=3.14$.) A rectangle is $8\\ \\mathrm{cm}$ by $3\\ \\mathrm{cm}$. What is its perimeter in centimetres?

**Solution:** Area $3.14\\times 5^2=3.14\\times 25=78.5$. Perimeter $2(8+3)=22$.""",
  [("把 $2\\pi r$ 和 $\\pi r^2$ 用反。", "Swapping $2\\pi r$ and $\\pi r^2$."),
   ("三角形用斜边当高，而不是垂直高度。", "Using a sloping side as the height of a triangle."),
   ("面积用长度单位，或忘记平方。", "Giving area in a length unit, or forgetting to square.")],
  [
    dict(type="numeric", stem_zh="长 $8\\ \\mathrm{cm}$、宽 $3\\ \\mathrm{cm}$ 的矩形，周长是多少厘米？",
         stem_en="A rectangle is $8\\ \\mathrm{cm}$ by $3\\ \\mathrm{cm}$. Perimeter in centimetres?",
         answer=22, exp_zh="$2(8+3)=22$。", exp_en="$2(8+3)=22$.", tolerance=0),
    dict(type="numeric", stem_zh="该矩形的面积是多少平方厘米？", stem_en="What is the area of that rectangle, in square centimetres?",
         answer=24, exp_zh="$8\\times 3=24$。", exp_en="$8\\times 3=24$.", tolerance=0),
    dict(type="numeric", stem_zh="底 $10\\ \\mathrm{cm}$、高 $6\\ \\mathrm{cm}$ 的三角形，面积是多少平方厘米？",
         stem_en="A triangle has base $10\\ \\mathrm{cm}$ and height $6\\ \\mathrm{cm}$. Area in square centimetres?",
         answer=30, exp_zh="$\\dfrac{1}{2}\\times 10\\times 6=30$。", exp_en="$\\dfrac{1}{2}\\times 10\\times 6=30$.", tolerance=0),
    dict(type="numeric", stem_zh="半径 $5\\ \\mathrm{cm}$ 的圆，面积是多少平方厘米？（$\\pi=3.14$）",
         stem_en="A circle has radius $5\\ \\mathrm{cm}$. Area in square centimetres? (Use $\\pi=3.14$.)",
         answer=78.5, exp_zh="$3.14\\times 25=78.5$。", exp_en="$3.14\\times 25=78.5$.", tolerance=0.05),
    dict(type="numeric", stem_zh="半径 $5\\ \\mathrm{cm}$ 的圆，周长是多少厘米？（$\\pi=3.14$）",
         stem_en="A circle has radius $5\\ \\mathrm{cm}$. Circumference in centimetres? (Use $\\pi=3.14$.)",
         answer=31.4, exp_zh="$2\\times 3.14\\times 5=31.4$。", exp_en="$2\\times 3.14\\times 5=31.4$.", tolerance=0.05),
    dict(type="mcq", stem_zh="直径 $10\\ \\mathrm{cm}$ 的圆，半径是？", stem_en="A circle has diameter $10\\ \\mathrm{cm}$. Its radius is:",
         answer="c", exp_zh="半径是直径的一半，为 $5\\ \\mathrm{cm}$。", exp_en="The radius is half the diameter, $5\\ \\mathrm{cm}$.",
         options=opts(("$10\\ \\mathrm{cm}$", "$10\\ \\mathrm{cm}$"), ("$20\\ \\mathrm{cm}$", "$20\\ \\mathrm{cm}$"),
                      ("$5\\ \\mathrm{cm}$", "$5\\ \\mathrm{cm}$"), ("$2.5\\ \\mathrm{cm}$", "$2.5\\ \\mathrm{cm}$"))),
  ], diagram=D_CIRC)

L("mathematics-8-3-3", "立体图形、表面积与体积", "3D shapes, surface area and volume",
  "本节你将学会识别棱柱与圆柱等立体，并计算它们的表面积和体积。",
  "This lesson you will recognise prisms and cylinders and calculate their surface area and volume.",
  [("棱柱的两个底面全等且平行，侧面是矩形（直棱柱）。", "A prism has two congruent, parallel bases and, for a right prism, rectangular sides."),
   ("棱柱或圆柱的体积 $=$ 底面积 $\\times$ 高。", "Volume of a prism or cylinder $=$ area of cross-section $\\times$ height (or length)."),
   ("圆柱体积 $V=\\pi r^2 h$，侧面积 $2\\pi rh$，全面积还要加上两个底面。", "Cylinder: $V=\\pi r^2 h$, curved surface $2\\pi rh$; add two bases for the total surface area."),
   ("体积单位是立方单位，表面积是平方单位。", "Volume uses cubic units; surface area uses square units.")],
  r"""先认出“沿着一个方向拉出来的”立体：三角形底的三棱柱，矩形底的长方体，圆形底的圆柱。体积都是“底面积乘以高”。长方体 $V=lwh$。圆柱把圆面积 $\\pi r^2$ 乘以高。

表面积是把所有外表面的面积加起来。若一个面被贴住或开口，题目会说明不要算那个面。""",
  r"""First recognise a solid “stretched” along one direction: a triangular prism, a cuboid, or a cylinder. In each case the volume is the area of the cross-section times the length or height. For a cuboid, $V=lwh$. For a cylinder, multiply the circle area $\\pi r^2$ by the height.

Surface area is the total of all the outer faces. If a face is closed off or open, the question will tell you not to include it.""",
  r"""长 $5\\ \\mathrm{cm}$、宽 $3\\ \\mathrm{cm}$、高 $4\\ \\mathrm{cm}$ 的长方体，体积是多少？一个圆柱半径 $3\\ \\mathrm{cm}$、高 $10\\ \\mathrm{cm}$，体积是多少？（$\\pi=3.14$）

**解：** $5\\times 3\\times 4=60\\ \\mathrm{cm}^3$。圆柱 $3.14\\times 3^2\\times 10=3.14\\times 90=282.6\\ \\mathrm{cm}^3$。""",
  r"""A cuboid is $5\\ \\mathrm{cm}$ by $3\\ \\mathrm{cm}$ by $4\\ \\mathrm{cm}$. What is its volume? A cylinder has radius $3\\ \\mathrm{cm}$ and height $10\\ \\mathrm{cm}$. What is its volume? (Use $\\pi=3.14$.)

**Solution:** $5\\times 3\\times 4=60\\ \\mathrm{cm}^3$. The cylinder is $3.14\\times 3^2\\times 10=3.14\\times 90=282.6\\ \\mathrm{cm}^3$.""",
  [("把表面积和体积的单位写反。", "Swapping the units for surface area and volume."),
   ("圆柱体积用 $2\\pi r h$ 而不是 $\\pi r^2 h$。", "Using $2\\pi rh$ for volume instead of $\\pi r^2 h$."),
   ("底面积不用垂直于长度的截面。", "Using a face that is not the cross-section perpendicular to the length.")],
  [
    dict(type="numeric", stem_zh="长方体 $5\\ \\mathrm{cm}$ 乘 $3\\ \\mathrm{cm}$ 乘 $4\\ \\mathrm{cm}$，体积是多少立方厘米？",
         stem_en="A cuboid is $5\\ \\mathrm{cm}$ by $3\\ \\mathrm{cm}$ by $4\\ \\mathrm{cm}$. Volume in cubic centimetres?",
         answer=60, exp_zh="$5\\times 3\\times 4=60$。", exp_en="$5\\times 3\\times 4=60$.", tolerance=0),
    dict(type="numeric", stem_zh="该长方体的表面积是多少平方厘米？", stem_en="The total surface area of that cuboid, in square centimetres?",
         answer=94, exp_zh="$2(5\\times 3+5\\times 4+3\\times 4)=2(15+20+12)=94$。", exp_en="$2(5\\times 3+5\\times 4+3\\times 4)=2(15+20+12)=94$.", tolerance=0),
    dict(type="numeric", stem_zh="圆柱半径 $3\\ \\mathrm{cm}$、高 $10\\ \\mathrm{cm}$，体积是多少立方厘米？（$\\pi=3.14$）",
         stem_en="A cylinder has radius $3\\ \\mathrm{cm}$ and height $10\\ \\mathrm{cm}$. Volume in cubic centimetres? ($\\pi=3.14$)",
         answer=282.6, exp_zh="$3.14\\times 9\\times 10=282.6$。", exp_en="$3.14\\times 9\\times 10=282.6$.", tolerance=0.1),
    dict(type="mcq", stem_zh="直三棱柱的体积等于？", stem_en="The volume of a right triangular prism equals:",
         answer="b", exp_zh="三角形底面积乘以棱柱的长度（高）。", exp_en="The area of the triangular cross-section times the length of the prism.",
         options=opts(("三个矩形面积之和", "the sum of three rectangle areas only"),
                      ("三角形底面积乘以长度", "the triangular cross-sectional area times the length"),
                      ("只等于三条棱的和", "only the sum of three edges"),
                      ("$2\\pi r$", "$2\\pi r$"))),
    dict(type="numeric", stem_zh="底面积 $12\\ \\mathrm{cm}^2$、长 $7\\ \\mathrm{cm}$ 的棱柱，体积是多少立方厘米？",
         stem_en="A prism has cross-sectional area $12\\ \\mathrm{cm}^2$ and length $7\\ \\mathrm{cm}$. Volume in cubic centimetres?",
         answer=84, exp_zh="$12\\times 7=84$。", exp_en="$12\\times 7=84$.", tolerance=0),
    dict(type="mcq", stem_zh="体积的单位应是？", stem_en="The unit of volume should be:",
         answer="a", exp_zh="立方单位，例如 $\\mathrm{cm}^3$。", exp_en="A cubic unit, such as $\\mathrm{cm}^3$.",
         options=opts(("立方单位，如 $\\mathrm{cm}^3$", "a cubic unit such as $\\mathrm{cm}^3$"),
                      ("只能是 $\\mathrm{cm}$", "only $\\mathrm{cm}$"), ("只能是 $\\mathrm{cm}^2$", "only $\\mathrm{cm}^2$"),
                      ("没有单位", "no unit"))),
  ])

L("mathematics-8-4-1", "比较数的大小", "Comparing numbers",
  "本节你将学会把分数、小数和百分数写成可比较的形式，并正确比较它们的大小。",
  "This lesson you will write fractions, decimals and percentages in comparable forms and order them correctly.",
  [("比较前先统一形式：都变成小数、都变成百分数，或都变成同分母分数。", "Before comparing, use one form: all decimals, all percentages, or fractions with a common denominator."),
   ("$\\dfrac{1}{2}=0.5=50\\%$。", "$\\dfrac{1}{2}=0.5=50\\%$."),
   ("百分数除以 $100$ 就得到小数或分数。", "Divide a percentage by $100$ to get a decimal or a fraction."),
   ("不要只比较分子或只比较分母。", "Do not compare numerators alone, or denominators alone.")],
  r"""$\\dfrac{3}{5}$、$0.55$ 和 $62\\%$ 哪一个最大？先统一：$\\dfrac{3}{5}=0.6=60\\%$，$0.55=55\\%$，$62\\%=0.62$。所以 $62\\%$ 最大，$\\dfrac{3}{5}$ 其次，$0.55$ 最小。

也可以把它们都写成百分数或都写成分母为 $100$ 的分数。选择你算得最稳的方法。""",
  r"""Which is largest: $\\dfrac{3}{5}$, $0.55$ or $62\\%$? Use one form: $\\dfrac{3}{5}=0.6=60\\%$, $0.55=55\\%$, $62\\%=0.62$. So $62\\%$ is largest, then $\\dfrac{3}{5}$, then $0.55$.

You can equally well use percentages throughout, or fractions with denominator $100$. Choose the conversion you can do most reliably.""",
  r"""把 $\\dfrac{2}{5}$、$0.45$ 和 $40\\%$ 从小到大排列。

**解：** $\\dfrac{2}{5}=0.4=40\\%$，与 $40\\%$ 相等；$0.45=45\\%$ 最大。顺序是 $\\dfrac{2}{5}=40\\%<0.45$。""",
  r"""Write $\\dfrac{2}{5}$, $0.45$ and $40\\%$ in ascending order.

**Solution:** $\\dfrac{2}{5}=0.4=40\\%$, equal to $40\\%$; $0.45=45\\%$ is larger. The order is $\\dfrac{2}{5}=40\\%<0.45$.""",
  [("只看分子就判断分数大小。", "Comparing fractions by looking only at the numerators."),
   ("把 $0.8$ 当成 $8\\%$。应为 $80\\%$。", "Reading $0.8$ as $8\\%$; it is $80\\%$."),
   ("百分数与小数之间漏除或漏乘 $100$。", "Forgetting to divide or multiply by $100$ when converting.")],
  [
    dict(type="mcq", stem_zh="$\\dfrac{3}{5}$、$0.55$、$62\\%$ 中最大的是？", stem_en="Which is the largest of $\\dfrac{3}{5}$, $0.55$ and $62\\%$?",
         answer="c", exp_zh="$60\\%$、$55\\%$、$62\\%$，所以 $62\\%$ 最大。", exp_en="They are $60\\%$, $55\\%$ and $62\\%$, so $62\\%$ is largest.",
         options=opts(("$\\dfrac{3}{5}$", "$\\dfrac{3}{5}$"), ("$0.55$", "$0.55$"), ("$62\\%$", "$62\\%$"), ("三者相等", "they are equal"))),
    dict(type="mcq", stem_zh="$0.8$ 等于？", stem_en="$0.8$ is equal to:",
         answer="b", exp_zh="$0.8=80\\%=\\dfrac{4}{5}$。", exp_en="$0.8=80\\%=\\dfrac{4}{5}$.",
         options=opts(("$8\\%$", "$8\\%$"), ("$80\\%$", "$80\\%$"), ("$0.08\\%$", "$0.08\\%$"), ("$800\\%$", "$800\\%$"))),
    dict(type="mcq", stem_zh="$\\dfrac{2}{5}$ 与 $40\\%$ 的关系是？", stem_en="How do $\\dfrac{2}{5}$ and $40\\%$ compare?",
         answer="a", exp_zh="两者都等于 $0.4$，相等。", exp_en="Both equal $0.4$, so they are equal.",
         options=opts(("相等", "they are equal"), ("$\\dfrac{2}{5}$ 更大", "$\\dfrac{2}{5}$ is larger"),
                      ("$40\\%$ 更大", "$40\\%$ is larger"), ("无法比较", "they cannot be compared"))),
    dict(type="mcq", stem_zh="下列从小到大排列正确的是？", stem_en="Which list is in ascending order?",
         answer="d", exp_zh="$0.3=30\\%$，$\\dfrac{1}{3}\\approx 33\\%$，$35\\%$。", exp_en="$0.3=30\\%$, $\\dfrac{1}{3}\\approx 33\\%$, $35\\%$.",
         options=opts(("$35\\%$，$\\dfrac{1}{3}$，$0.3$", "$35\\%$, $\\dfrac{1}{3}$, $0.3$"),
                      ("$\\dfrac{1}{3}$，$0.3$，$35\\%$", "$\\dfrac{1}{3}$, $0.3$, $35\\%$"),
                      ("$35\\%$，$0.3$，$\\dfrac{1}{3}$", "$35\\%$, $0.3$, $\\dfrac{1}{3}$"),
                      ("$0.3$，$\\dfrac{1}{3}$，$35\\%$", "$0.3$, $\\dfrac{1}{3}$, $35\\%$"))),
    dict(type="numeric", stem_zh="$\\dfrac{3}{4}$ 写成百分数是多少？（只填数字，不含 %）", stem_en="Write $\\dfrac{3}{4}$ as a percentage (number only, without the % sign).",
         answer=75, exp_zh="$\\dfrac{3}{4}=0.75=75\\%$。", exp_en="$\\dfrac{3}{4}=0.75=75\\%$.", tolerance=0),
    dict(type="numeric", stem_zh="$45\\%$ 写成小数是多少？", stem_en="Write $45\\%$ as a decimal.",
         answer=0.45, exp_zh="除以 $100$ 得 $0.45$。", exp_en="Divide by $100$ to get $0.45$.", tolerance=0.001),
  ])

L("mathematics-8-4-2", "分数运算", "Calculating with fractions",
  "本节你将学会进行分数的加减乘除，包括带分数与不同分母的情况。",
  "This lesson you will add, subtract, multiply and divide fractions, including mixed numbers and different denominators.",
  [("加减时先通分，分母相同后才加减分子。", "For addition and subtraction, first use a common denominator, then add or subtract the numerators."),
   ("乘法：分子乘分子，分母乘分母，能约分先约分。", "Multiplication: multiply numerators and multiply denominators, cancelling first if you can."),
   ("除法：除以一个分数等于乘它的倒数。", "Division: dividing by a fraction is multiplying by its reciprocal."),
   ("带分数先化为假分数再算，通常更稳妥。", "Convert mixed numbers to improper fractions before calculating, which is usually safer.")],
  r"""$\\dfrac{1}{2}+\\dfrac{1}{3}$ 要先通分到 $6$：$\\dfrac{3}{6}+\\dfrac{2}{6}=\\dfrac{5}{6}$。乘法 $\\dfrac{2}{3}\\times\\dfrac{5}{8}=\\dfrac{10}{24}=\\dfrac{5}{12}$。除法 $\\dfrac{3}{4}\\div\\dfrac{2}{5}=\\dfrac{3}{4}\\times\\dfrac{5}{2}=\\dfrac{15}{8}$。

整数除以分数，例如 $6\\div\\dfrac{1}{2}=6\\times 2=12$，意思是“一半有多少份在 $6$ 里”。""",
  r"""$\\dfrac{1}{2}+\\dfrac{1}{3}$ needs a common denominator of $6$: $\\dfrac{3}{6}+\\dfrac{2}{6}=\\dfrac{5}{6}$. Multiplication: $\\dfrac{2}{3}\\times\\dfrac{5}{8}=\\dfrac{10}{24}=\\dfrac{5}{12}$. Division: $\\dfrac{3}{4}\\div\\dfrac{2}{5}=\\dfrac{3}{4}\\times\\dfrac{5}{2}=\\dfrac{15}{8}$.

An integer divided by a fraction, such as $6\\div\\dfrac{1}{2}=6\\times 2=12$, asks how many halves are in $6$.""",
  r"""计算 $1\\dfrac{1}{2}\\times\\dfrac{2}{3}$。

**解：** $1\\dfrac{1}{2}=\\dfrac{3}{2}$，$\\dfrac{3}{2}\\times\\dfrac{2}{3}=1$。""",
  r"""Evaluate $1\\dfrac{1}{2}\\times\\dfrac{2}{3}$.

**Solution:** $1\\dfrac{1}{2}=\\dfrac{3}{2}$, and $\\dfrac{3}{2}\\times\\dfrac{2}{3}=1$.""",
  [("分母不同却直接加减分子。", "Adding numerators without a common denominator."),
   ("除法时乘了原分数而不是倒数。", "Multiplying by the fraction itself instead of its reciprocal."),
   ("约分约错，或最后没有化简。", "Cancelling incorrectly, or leaving an unsimplified answer.")],
  [
    dict(type="short", stem_zh="计算 $\\dfrac{1}{2}+\\dfrac{1}{3}$。", stem_en="Evaluate $\\dfrac{1}{2}+\\dfrac{1}{3}$.",
         answer="5/6", accepted=["5/6", "5 / 6", "\\frac{5}{6}", "5⁄6"],
         answer_zh="$\\dfrac{5}{6}$", answer_en="$\\dfrac{5}{6}$", exp_zh="通分为 $\\dfrac{3}{6}+\\dfrac{2}{6}$。", exp_en="Common denominator: $\\dfrac{3}{6}+\\dfrac{2}{6}$."),
    dict(type="short", stem_zh="计算 $\\dfrac{2}{3}\\times\\dfrac{5}{8}$（请化简）。", stem_en="Evaluate $\\dfrac{2}{3}\\times\\dfrac{5}{8}$ (give the simplified form).",
         answer="5/12", accepted=["5/12", "5 / 12", "\\frac{5}{12}"],
         answer_zh="$\\dfrac{5}{12}$", answer_en="$\\dfrac{5}{12}$", exp_zh="$\\dfrac{10}{24}=\\dfrac{5}{12}$。", exp_en="$\\dfrac{10}{24}=\\dfrac{5}{12}$."),
    dict(type="short", stem_zh="计算 $\\dfrac{3}{4}\\div\\dfrac{2}{5}$。", stem_en="Evaluate $\\dfrac{3}{4}\\div\\dfrac{2}{5}$.",
         answer="15/8", accepted=["15/8", "15 / 8", "1 7/8", "1 7/8", "1.875", "7/8+1", "1\\frac{7}{8}"],
         answer_zh="$\\dfrac{15}{8}$", answer_en="$\\dfrac{15}{8}$", exp_zh="乘倒数：$\\dfrac{3}{4}\\times\\dfrac{5}{2}=\\dfrac{15}{8}$。", exp_en="Multiply by the reciprocal: $\\dfrac{3}{4}\\times\\dfrac{5}{2}=\\dfrac{15}{8}$."),
    dict(type="numeric", stem_zh="计算 $6\\div\\dfrac{1}{2}$。", stem_en="Evaluate $6\\div\\dfrac{1}{2}$.",
         answer=12, exp_zh="$6\\times 2=12$。", exp_en="$6\\times 2=12$.", tolerance=0),
    dict(type="numeric", stem_zh="计算 $1\\dfrac{1}{2}\\times\\dfrac{2}{3}$。", stem_en="Evaluate $1\\dfrac{1}{2}\\times\\dfrac{2}{3}$.",
         answer=1, exp_zh="$\\dfrac{3}{2}\\times\\dfrac{2}{3}=1$。", exp_en="$\\dfrac{3}{2}\\times\\dfrac{2}{3}=1$.", tolerance=0),
    dict(type="short", stem_zh="计算 $\\dfrac{5}{6}-\\dfrac{1}{3}$。", stem_en="Evaluate $\\dfrac{5}{6}-\\dfrac{1}{3}$.",
         answer="1/2", accepted=["1/2", "0.5", "3/6", "\\frac{1}{2}"],
         answer_zh="$\\dfrac{1}{2}$", answer_en="$\\dfrac{1}{2}$", exp_zh="$\\dfrac{5}{6}-\\dfrac{2}{6}=\\dfrac{3}{6}=\\dfrac{1}{2}$。", exp_en="$\\dfrac{5}{6}-\\dfrac{2}{6}=\\dfrac{3}{6}=\\dfrac{1}{2}$."),
  ])

L("mathematics-8-4-3", "百分数变化、比与比例", "Percentage change, ratio and proportion",
  "本节你将学会计算百分数增减，并使用比和比例解决问题。",
  "This lesson you will calculate percentage increase and decrease, and use ratio and proportion to solve problems.",
  [("百分数变化 $=\\dfrac{\\text{实际变化量}}{\\text{原来的量}}\\times 100\\%$。", "Percentage change $=\\dfrac{\\text{actual change}}{\\text{original amount}}\\times 100\\%$."),
   ("增加 $20\\%$ 后等于原来的 $1.20$ 倍；减少 $20\\%$ 后等于 $0.80$ 倍。", "An increase of $20\\%$ gives $1.20$ times the original; a decrease of $20\\%$ gives $0.80$ times."),
   ("比 $a:b$ 表示两个量的相对大小，可化简。", "The ratio $a:b$ compares two quantities and can be simplified."),
   ("成比例时，对应两边的比相等，可用倍数或方程来求未知量。", "In a proportion, corresponding ratios are equal; use a multiplier or an equation to find an unknown.")],
  r"""原价 $\$50$ 的书包涨到 $\$60$，增加了 $\$10$，百分数增加是 $10/50=20\\%$。若一件衣服打八折，现价是原价的 $80\\%$。

比 $12:18$ 可约成 $2:3$。按 $2:3$ 把 $\$40$ 分成两份：总份数 $5$，一份 $\$8$，所以是 $\$16$ 和 $\$24$。如果 $3$ 本同样的本子要 $\$12$，那么 $5$ 本要 $\$20$，因为单价不变，成正比例。""",
  r"""A bag rises from $\$50$ to $\$60$. The increase is $\$10$, so the percentage increase is $10/50=20\\%$. A coat at $20\\%$ off costs $80\\%$ of the original price.

The ratio $12:18$ simplifies to $2:3$. To share $\$40$ in the ratio $2:3$, there are $5$ parts, each $\$8$, so the shares are $\$16$ and $\$24$. If $3$ identical books cost $\$12$, then $5$ cost $\$20$, because the unit price is constant and the quantities are in direct proportion.""",
  r"""把 $\$60$ 按 $1:2$ 分成两份。

**解：** 总份数 $3$，一份 $\$20$，所以是 $\$20$ 与 $\$40$。""",
  r"""Share $\$60$ in the ratio $1:2$.

**Solution:** There are $3$ parts, each $\$20$, so the shares are $\$20$ and $\$40$.""",
  [("百分数变化除以新的量而不是原来的量。", "Dividing the change by the new amount instead of the original."),
   ("增加 $20\\%$ 再减少 $20\\%$ 以为回到原值。第二次的基数已经变了。", "Thinking an increase of $20\\%$ followed by a decrease of $20\\%$ returns to the start. The base has changed."),
   ("按比分配时忘记先求一份的值。", "Sharing in a ratio without first finding the value of one part.")],
  [
    dict(type="numeric", stem_zh="价格从 $\$50$ 涨到 $\$60$。百分数增加是多少？（只填数字）",
         stem_en="A price rises from $\$50$ to $\$60$. What is the percentage increase (number only)?",
         answer=20, exp_zh="$10/50\\times 100\\%=20\\%$。", exp_en="$10/50\\times 100\\%=20\\%$.", tolerance=0),
    dict(type="numeric", stem_zh="原价 $\$80$ 的商品打八折（即现价为 $80\\%$）。现价是多少美元？",
         stem_en="An item priced at $\$80$ is sold at $80\\%$ of that price. What is the sale price in dollars?",
         answer=64, exp_zh="$80\\times 0.80=64$。", exp_en="$80\\times 0.80=64$.", tolerance=0),
    dict(type="short", stem_zh="把比 $12:18$ 化成最简整数比。", stem_en="Simplify the ratio $12:18$.",
         answer="2:3", accepted=["2:3", "2 : 3", "2比3"],
         answer_zh="$2:3$", answer_en="$2:3$", exp_zh="同除以 $6$。", exp_en="Divide both parts by $6$."),
    dict(type="numeric", stem_zh="按 $2:3$ 分配 $\$40$，较小的一份是多少美元？",
         stem_en="Share $\$40$ in the ratio $2:3$. What is the smaller share in dollars?",
         answer=16, exp_zh="总份数 $5$，一份 $\$8$，$2$ 份 $\$16$。", exp_en="$5$ parts, each $\$8$, so $2$ parts are $\$16$.", tolerance=0),
    dict(type="numeric", stem_zh="$3$ 本同样的本子要 $\$12$。$5$ 本要多少美元？",
         stem_en="$3$ identical books cost $\$12$. How many dollars do $5$ cost?",
         answer=20, exp_zh="每本 $\$4$，$5$ 本 $\$20$。", exp_en="Each book is $\$4$, so $5$ cost $\$20$.", tolerance=0),
    dict(type="mcq", stem_zh="一件商品先涨 $20\\%$ 再降 $20\\%$，最终价格与原价相比？",
         stem_en="A price rises by $20\\%$ and then falls by $20\\%$. Compared with the start, the final price is:",
         answer="b", exp_zh="变成原价的 $1.2\\times 0.8=0.96$，比原来低 $4\\%$。", exp_en="It becomes $1.2\\times 0.8=0.96$ of the original, so $4\\%$ lower.",
         options=opts(("相同", "the same"), ("更低", "lower"), ("更高", "higher"), ("无法确定", "impossible to tell"))),
  ])

L("mathematics-8-5-1", "互补事件与复合事件", "Complementary and combined events",
  "本节你将学会使用互补事件，并计算简单的互斥或独立复合事件的概率。",
  "This lesson you will use complementary events and find probabilities of simple mutually exclusive or independent combined events.",
  [("概率在 $0$ 与 $1$ 之间（或 $0\\%$ 到 $100\\%$）。", "A probability lies between $0$ and $1$ (or $0\\%$ to $100\\%$)."),
   ("互补事件：$P(\\text{not } A)=1-P(A)$。", "Complement: $P(\\text{not } A)=1-P(A)$."),
   ("互斥事件不能同时发生，满足 $P(A\\text{ or }B)=P(A)+P(B)$。", "Mutually exclusive events cannot happen together: $P(A\\text{ or }B)=P(A)+P(B)$."),
   ("独立事件互不影响，满足 $P(A\\text{ and }B)=P(A)\\times P(B)$。", "Independent events do not affect each other: $P(A\\text{ and }B)=P(A)\\times P(B)$.")],
  r"""公平骰子掷出偶数的概率是 $3/6=1/2$，那么“不是偶数”的概率是 $1-1/2=1/2$。掷出 $5$ 或 $6$ 是互斥的，概率 $1/6+1/6=1/3$。

两枚公平硬币都朝上为正面，若两次互不影响，概率是 $\\dfrac{1}{2}\\times\\dfrac{1}{2}=\\dfrac{1}{4}$。先判断事件是否互斥或独立，再决定是加还是乘。""",
  r"""The probability of an even number on a fair die is $3/6=1/2$, so the probability of “not even” is $1-1/2=1/2$. Rolling a $5$ or a $6$ are mutually exclusive, so the probability is $1/6+1/6=1/3$.

The probability that two fair coins both show heads, if the tosses do not affect each other, is $\\dfrac{1}{2}\\times\\dfrac{1}{2}=\\dfrac{1}{4}$. First decide whether events are mutually exclusive or independent, then decide whether to add or multiply.""",
  r"""袋中有 $3$ 红 $2$ 蓝共 $5$ 球，随机取一球。求取出红球的概率，以及连续两次放回摸球都是红色的概率。

**解：** $P(\\text{红})=3/5$。放回后两次独立，$P(\\text{两次都红})=\\dfrac{3}{5}\\times\\dfrac{3}{5}=\\dfrac{9}{25}$。""",
  r"""A bag has $3$ red and $2$ blue balls, $5$ in all. One ball is chosen at random. Find the probability it is red, and the probability that two draws with replacement are both red.

**Solution:** $P(\\text{red})=3/5$. With replacement the draws are independent, so $P(\\text{both red})=\\dfrac{3}{5}\\times\\dfrac{3}{5}=\\dfrac{9}{25}$.""",
  [("互斥时用乘法，独立时用加法。应反过来记清。", "Multiplying for mutually exclusive events, or adding for independent ones. Keep the rules the other way round."),
   ("互补事件用 $1+P(A)$。", "Using $1+P(A)$ for the complement."),
   ("不放回抽取仍按独立事件直接相乘且概率不变。", "Treating draws without replacement as independent with unchanged probabilities.")],
  [
    dict(type="short", stem_zh="公平骰子掷出偶数的概率是多少？（用最简分数）", stem_en="What is the probability of an even number on a fair die? (Give a simplified fraction.)",
         answer="1/2", accepted=["1/2", "0.5", "3/6", "50%"],
         answer_zh="$\\dfrac{1}{2}$", answer_en="$\\dfrac{1}{2}$", exp_zh="偶数有 $2,4,6$ 共三个结果。", exp_en="There are three even outcomes: $2,4,6$."),
    dict(type="short", stem_zh="若 $P(A)=0.3$，则 $P(\\text{not }A)$ 是多少？", stem_en="If $P(A)=0.3$, what is $P(\\text{not }A)$?",
         answer="0.7", accepted=["0.7", "7/10", "70%"],
         answer_zh="$0.7$", answer_en="$0.7$", exp_zh="$1-0.3=0.7$。", exp_en="$1-0.3=0.7$."),
    dict(type="short", stem_zh="公平骰子掷出 $5$ 或 $6$ 的概率是多少？", stem_en="What is the probability of a $5$ or a $6$ on a fair die?",
         answer="1/3", accepted=["1/3", "2/6", "0.333", "0.33"],
         answer_zh="$\\dfrac{1}{3}$", answer_en="$\\dfrac{1}{3}$", exp_zh="互斥，相加得 $2/6=1/3$。", exp_en="They are mutually exclusive, so add: $2/6=1/3$."),
    dict(type="short", stem_zh="两枚公平硬币都是正面的概率是多少？", stem_en="What is the probability that two fair coins both show heads?",
         answer="1/4", accepted=["1/4", "0.25", "25%"],
         answer_zh="$\\dfrac{1}{4}$", answer_en="$\\dfrac{1}{4}$", exp_zh="独立，相乘 $\\dfrac{1}{2}\\times\\dfrac{1}{2}$。", exp_en="Independent, so multiply $\\dfrac{1}{2}\\times\\dfrac{1}{2}$."),
    dict(type="short", stem_zh="袋中 $3$ 红 $2$ 蓝。随机取一球为红的概率是多少？", stem_en="A bag has $3$ red and $2$ blue balls. Probability a randomly chosen ball is red?",
         answer="3/5", accepted=["3/5", "0.6", "60%"],
         answer_zh="$\\dfrac{3}{5}$", answer_en="$\\dfrac{3}{5}$", exp_zh="一共 $5$ 个球，红色 $3$ 个。", exp_en="There are $5$ balls, of which $3$ are red."),
    dict(type="short", stem_zh="上题中放回后再摸一次，两次都是红的概率是多少？", stem_en="In that bag, with replacement, what is the probability that two draws are both red?",
         answer="9/25", accepted=["9/25", "0.36"],
         answer_zh="$\\dfrac{9}{25}$", answer_en="$\\dfrac{9}{25}$", exp_zh="$\\dfrac{3}{5}\\times\\dfrac{3}{5}=\\dfrac{9}{25}$。", exp_en="$\\dfrac{3}{5}\\times\\dfrac{3}{5}=\\dfrac{9}{25}$."),
  ])

L("mathematics-8-5-2", "实验概率", "Experimental probability",
  "本节你将学会用相对频率估计概率，并说明实验次数增多时估计通常会更稳定。",
  "This lesson you will use relative frequency to estimate probability, and explain that estimates usually settle as the number of trials increases.",
  [("实验概率（相对频率）$=\\dfrac{\\text{某结果出现的次数}}{\\text{实验总次数}}$。", "Experimental probability (relative frequency) $=\\dfrac{\\text{number of times the outcome occurs}}{\\text{number of trials}}$."),
   ("它是对理论概率的估计，不一定恰好相等。", "It is an estimate of a theoretical probability and need not match it exactly."),
   ("实验次数越多，相对频率通常越接近理论值。", "As the number of trials increases, the relative frequency usually gets closer to the theoretical value."),
   ("个别几次的结果波动很大，不能据此断定骰子一定不公平。", "A few trials can fluctuate a lot; that alone does not prove a die is unfair.")],
  r"""一枚图钉被投掷 $80$ 次，钉尖朝上 $28$ 次，相对频率是 $28/80=0.35$。这并不证明下一次朝上的理论概率“恰好是 $0.35$”，只是当前最好的估计之一。

若再投很多很多次，估计往往会稳定下来。公平骰子掷 $6$ 次可能一次都没有 $6$，这很正常；掷 $600$ 次时，相对频率通常会更接近 $1/6$。""",
  r"""A drawing pin lands point up $28$ times in $80$ throws, so the relative frequency is $28/80=0.35$. That does not prove the theoretical probability of the next throw is “exactly $0.35$”; it is one of the best estimates you have so far.

If you continue for many more trials, the estimate usually settles. A fair die rolled $6$ times may show no sixes at all, which is not surprising; in $600$ rolls the relative frequency is usually closer to $1/6$.""",
  r"""掷一枚硬币 $50$ 次，正面出现 $22$ 次。估计正面朝上的概率，并说明若只掷 $2$ 次就得到两个正面，为什么不能立刻断定硬币两面都是正面。

**解：** 估计为 $22/50=0.44$。两次实验太少，波动很大，不足以推翻“公平硬币”的合理模型。""",
  r"""A coin is tossed $50$ times and lands heads $22$ times. Estimate the probability of heads, and explain why two heads in only two tosses would not immediately prove both sides are heads.

**Solution:** The estimate is $22/50=0.44$. Two trials are far too few; the result can easily fluctuate and does not overturn a reasonable fair-coin model.""",
  [("把相对频率当成下一次必然发生的保证。", "Treating a relative frequency as a guarantee for the next trial."),
   ("用很少的次数就断定理论概率。", "Deciding the theoretical probability from very few trials."),
   ("分子分母写反。", "Writing the fraction upside down.")],
  [
    dict(type="numeric", stem_zh="图钉投掷 $80$ 次，钉尖朝上 $28$ 次。相对频率是多少？（用小数）",
         stem_en="A pin lands point up $28$ times in $80$ throws. What is the relative frequency as a decimal?",
         answer=0.35, exp_zh="$28/80=0.35$。", exp_en="$28/80=0.35$.", tolerance=0.01),
    dict(type="numeric", stem_zh="硬币掷 $50$ 次，正面 $22$ 次。估计正面概率（小数）。",
         stem_en="A coin lands heads $22$ times in $50$ tosses. Estimate the probability of heads as a decimal.",
         answer=0.44, exp_zh="$22/50=0.44$。", exp_en="$22/50=0.44$.", tolerance=0.01),
    dict(type="mcq", stem_zh="实验次数增多时，相对频率通常会？", stem_en="As the number of trials increases, the relative frequency usually:",
         answer="b", exp_zh="更接近理论概率。", exp_en="Gets closer to the theoretical probability.",
         options=opts(("一定变成 $0$", "becomes $0$ for certain"), ("更接近理论值", "gets closer to the theoretical value"),
                      ("不再是估计", "stops being an estimate"), ("必须恰好等于 $1$", "must become exactly $1$"))),
    dict(type="mcq", stem_zh="公平骰子掷 $6$ 次没有出现 $6$，较合理的说法是？",
         stem_en="A fair die is rolled $6$ times with no six. A fair comment is:",
         answer="a", exp_zh="次数很少，这完全可能发生，不能立刻断定骰子不公平。", exp_en="With few trials this can easily happen, so it does not immediately prove the die is unfair.",
         options=opts(("次数很少，不能立刻断定骰子不公平", "there are few trials, so this does not immediately prove the die is unfair"),
                      ("骰子一定做了手脚", "the die must be biased"),
                      ("理论概率现在变成 $0$", "the theoretical probability is now $0$"),
                      ("相对频率永远无法使用", "relative frequency can never be used"))),
    dict(type="short", stem_zh="写出相对频率的计算公式。", stem_en="Write the formula for relative frequency.",
         answer="frequency / number of trials",
         accepted=["frequency / number of trials", "times it happens / total trials", "出现次数/总次数", "某结果次数除以实验总次数"],
         answer_zh="某结果出现次数 $/$ 实验总次数。", answer_en="number of times the outcome occurs $/$ number of trials.",
         exp_zh="这是对概率的实验估计。", exp_en="This is an experimental estimate of a probability."),
    dict(type="mcq", stem_zh="理论概率与实验概率的关系是？", stem_en="The relationship between theoretical and experimental probability is:",
         answer="c", exp_zh="实验值是估计，不一定恰好等于理论值。", exp_en="The experimental value is an estimate and need not equal the theoretical value exactly.",
         options=opts(("二者必须每次都恰好相等", "they must be exactly equal every time"),
                      ("实验值永远不能使用", "the experimental value can never be used"),
                      ("实验值是估计，通常随次数增多而靠近理论值", "the experimental value is an estimate and usually approaches the theoretical value as trials increase"),
                      ("理论概率不能用于骰子", "theoretical probability cannot be used for dice"))),
  ])

L("mathematics-8-6-1", "角、方位角与测量", "Angles, bearings and measurement",
  "本节你将学会使用平行线中的角、三角形内角和，以及用三位数方位角表示方向。",
  "This lesson you will use angles with parallel lines, the angle sum of a triangle, and three-figure bearings.",
  [("三角形内角和 $180^\\circ$，直线上的邻角和 $180^\\circ$，周角 $360^\\circ$。", "Angles in a triangle add to $180^\\circ$; adjacent angles on a straight line add to $180^\\circ$; a full turn is $360^\\circ$."),
   ("平行线被截线所截：同位角相等，内错角相等，同旁内角互补。", "When a transversal cuts parallel lines: corresponding angles are equal, alternate angles are equal, co-interior angles add to $180^\\circ$."),
   ("方位角从正北起按顺时针测量，写成三位数，例如 $075^\\circ$。", "A bearing is measured clockwise from north and written with three figures, for example $075^\\circ$."),
   ("反向方位角通常相差 $180^\\circ$。", "The reverse bearing usually differs by $180^\\circ$.")],
  r"""先在图上标出已知角，再找能用的关系。若两条直线平行，看到“F”形是同位角，“Z”形是内错角，“C”形是同旁内角。

从学校看图书馆的方位角是 $075^\\circ$，则从图书馆看学校大约是 $075^\\circ+180^\\circ=255^\\circ$。若加上 $180^\\circ$ 后超过 $360^\\circ$，就减去 $360^\\circ$。""",
  r"""Mark the given angles, then use a relationship you can justify. If two lines are parallel, an “F” shape shows corresponding angles, a “Z” shows alternate angles, and a “C” shows co-interior angles.

If the bearing of the library from the school is $075^\\circ$, the bearing of the school from the library is about $075^\\circ+180^\\circ=255^\\circ$. If adding $180^\\circ$ goes past $360^\\circ$, subtract $360^\\circ$.""",
  r"""三角形两个角是 $50^\\circ$ 和 $60^\\circ$。第三个角是多少？从 $A$ 看 $B$ 的方位角是 $200^\\circ$，从 $B$ 看 $A$ 呢？

**解：** 第三个角 $180-50-60=70^\\circ$。反向方位角 $200-180=20^\\circ$，写成 $020^\\circ$。""",
  r"""Two angles in a triangle are $50^\\circ$ and $60^\\circ$. What is the third? The bearing of $B$ from $A$ is $200^\\circ$. What is the bearing of $A$ from $B$?

**Solution:** The third angle is $180-50-60=70^\\circ$. The reverse bearing is $200-180=20^\\circ$, written $020^\\circ$.""",
  [("方位角从东或从自己面前量，而不是从正北顺时针。", "Measuring a bearing from east, or from ahead of you, instead of clockwise from north."),
   ("漏写三位数，把 $75^\\circ$ 写成方位角却不写成 $075^\\circ$。", "Dropping the three-figure form and writing a bearing as $75^\\circ$ instead of $075^\\circ$."),
   ("平行线中把同旁内角当成相等。", "Treating co-interior angles as equal rather than supplementary.")],
  [
    dict(type="numeric", stem_zh="三角形两角为 $50^\\circ$ 和 $60^\\circ$。第三个角是多少度？",
         stem_en="Two angles in a triangle are $50^\\circ$ and $60^\\circ$. The third angle in degrees?",
         answer=70, exp_zh="$180-50-60=70$。", exp_en="$180-50-60=70$.", tolerance=0),
    dict(type="numeric", stem_zh="一条直线上的邻角之一是 $110^\\circ$。另一个是多少度？",
         stem_en="One of two adjacent angles on a straight line is $110^\\circ$. The other, in degrees?",
         answer=70, exp_zh="$180-110=70$。", exp_en="$180-110=70$.", tolerance=0),
    dict(type="mcq", stem_zh="方位角 $075^\\circ$ 表示？", stem_en="The bearing $075^\\circ$ means:",
         answer="b", exp_zh="从正北起顺时针 $75^\\circ$。", exp_en="$75^\\circ$ clockwise from north.",
         options=opts(("从正东起逆时针 $75^\\circ$", "$75^\\circ$ anticlockwise from east"),
                      ("从正北起顺时针 $75^\\circ$", "$75^\\circ$ clockwise from north"),
                      ("从正南起 $75^\\circ$", "$75^\\circ$ from south"),
                      ("从正北起逆时针 $75^\\circ$", "$75^\\circ$ anticlockwise from north"))),
    dict(type="short", stem_zh="从 $A$ 看 $B$ 的方位角是 $200^\\circ$。从 $B$ 看 $A$ 的方位角是多少？（三位数）",
         stem_en="The bearing of $B$ from $A$ is $200^\\circ$. What is the bearing of $A$ from $B$? (three figures)",
         answer="020", accepted=["020", "020°", "020^\\circ", "20", "020 degrees"],
         answer_zh="$020^\\circ$", answer_en="$020^\\circ$", exp_zh="$200-180=20$，写成 $020^\\circ$。", exp_en="$200-180=20$, written $020^\\circ$."),
    dict(type="mcq", stem_zh="两条平行线被截线所截，同位角？", stem_en="When a transversal cuts parallel lines, corresponding angles are:",
         answer="a", exp_zh="同位角相等。", exp_en="Equal.",
         options=opts(("相等", "equal"), ("相加为 $90^\\circ$", "adding to $90^\\circ$"),
                      ("一定都是 $180^\\circ$", "each $180^\\circ$ for certain"), ("无法比较", "impossible to compare"))),
    dict(type="mcq", stem_zh="平行线中的同旁内角？", stem_en="Co-interior angles with parallel lines:",
         answer="c", exp_zh="相加为 $180^\\circ$。", exp_en="Add to $180^\\circ$.",
         options=opts(("一定相等且都是锐角", "are equal and both acute"), ("相加为 $90^\\circ$", "add to $90^\\circ$"),
                      ("相加为 $180^\\circ$", "add to $180^\\circ$"), ("相加为 $360^\\circ$", "add to $360^\\circ$"))),
  ])

L("mathematics-8-6-2", "作图与中点", "Construction and midpoints",
  "本节你将学会说明常见尺规作图的目标，并使用中点与垂直平分线的性质。",
  "This lesson you will describe the aims of common ruler-and-compass constructions and use properties of midpoints and perpendicular bisectors.",
  [("线段的中点把线段分成两条相等的部分。", "The midpoint of a segment divides it into two equal parts."),
   ("垂直平分线上的点到线段两端距离相等。", "Every point on the perpendicular bisector of a segment is equidistant from the two endpoints."),
   ("角平分线上的点到角两边的垂直距离相等。", "Every point on the angle bisector is equidistant from the two arms of the angle."),
   ("作图要保留弧痕，题目常要求写出简要步骤或理由。", "Leave construction arcs visible; questions often ask for brief steps or reasons.")],
  r"""中点不是“看起来大概在中间”，而是到两端距离相等的点。连接两点后，线段中点的坐标是两端坐标的平均数：若 $A(2,1)$、$B(8,5)$，中点是 $\\left(\\dfrac{2+8}{2},\\dfrac{1+5}{2}\\right)=(5,3)$。

垂直平分线既过中点又垂直于该线段。要找“到 $A$、$B$ 等距”的点，就落在 $AB$ 的垂直平分线上。课堂上用圆规以两端为圆心、大于一半的半径画弧，两弧交点的连线就是垂直平分线。""",
  r"""A midpoint is not “roughly in the middle”: it is the point equally far from both ends. The midpoint of $A(2,1)$ and $B(8,5)$ is the average of the coordinates: $\\left(\\dfrac{2+8}{2},\\dfrac{1+5}{2}\\right)=(5,3)$.

A perpendicular bisector passes through the midpoint and is at right angles to the segment. Points equidistant from $A$ and $B$ lie on the perpendicular bisector of $AB$. In class, arcs with centres at the endpoints and radius more than half of $AB$ meet at two points; the line through those points is the perpendicular bisector.""",
  r"""求 $A(2,1)$ 与 $B(8,5)$ 的中点。为什么垂直平分线上的点到 $A$、$B$ 距离相等？

**解：** 中点 $(5,3)$。这是垂直平分线的性质：它上面每一个点到线段两端等距。""",
  r"""Find the midpoint of $A(2,1)$ and $B(8,5)$. Why is a point on the perpendicular bisector equidistant from $A$ and $B$?

**Solution:** The midpoint is $(5,3)$. That is the defining property of the perpendicular bisector: every point on it is the same distance from the two endpoints.""",
  [("把中点当成两端坐标相减而不是取平均。", "Subtracting coordinates instead of averaging them to find a midpoint."),
   ("圆规半径小于线段一半，导致两弧不相交。", "Choosing a compass radius shorter than half the segment, so the arcs do not meet."),
   ("把“等距”说成“一定在线段上”。垂直平分线上的点大多不在线段上。", "Thinking an equidistant point must lie on the segment. Most points on the perpendicular bisector do not.")],
  [
    dict(type="short", stem_zh="$A(2,1)$、$B(8,5)$ 的中点坐标是什么？", stem_en="What is the midpoint of $A(2,1)$ and $B(8,5)$?",
         answer="(5,3)", accepted=["(5,3)", "(5, 3)", "5,3", "(5,3)"],
         answer_zh="$(5,3)$", answer_en="$(5,3)$", exp_zh="分别取平均：$(5,3)$。", exp_en="Average the coordinates: $(5,3)$."),
    dict(type="short", stem_zh="$C(0,-2)$、$D(6,4)$ 的中点是什么？", stem_en="What is the midpoint of $C(0,-2)$ and $D(6,4)$?",
         answer="(3,1)", accepted=["(3,1)", "(3, 1)", "3,1"],
         answer_zh="$(3,1)$", answer_en="$(3,1)$", exp_zh="$\\left(\\dfrac{0+6}{2},\\dfrac{-2+4}{2}\\right)=(3,1)$。", exp_en="$\\left(\\dfrac{0+6}{2},\\dfrac{-2+4}{2}\\right)=(3,1)$."),
    dict(type="mcq", stem_zh="线段垂直平分线上的点到两端？", stem_en="A point on the perpendicular bisector of a segment is:",
         answer="a", exp_zh="到两端距离相等。", exp_en="Equidistant from the two endpoints.",
         options=opts(("距离相等", "equidistant from the endpoints"), ("只到其中一个端点距离为零", "at distance zero from one endpoint only"),
                      ("一定是端点本身", "must be an endpoint"), ("到两端距离之差一定为 $90$", "must have distances differing by $90$"))),
    dict(type="mcq", stem_zh="作线段的垂直平分线时，圆规半径应？", stem_en="When constructing the perpendicular bisector of a segment, the compass radius should be:",
         answer="c", exp_zh="大于线段长度的一半，两弧才能相交。", exp_en="Greater than half the length of the segment, so the arcs meet.",
         options=opts(("必须等于 $0$", "exactly $0$"), ("必须小于一半", "less than half the segment"),
                      ("大于一半", "greater than half the segment"), ("只能等于整条线段", "equal to the whole segment only"))),
    dict(type="mcq", stem_zh="角平分线上的点到角两边的垂直距离？", stem_en="A point on an angle bisector is:",
         answer="b", exp_zh="到两边的垂直距离相等。", exp_en="Equidistant from the two arms (perpendicular distances).",
         options=opts(("一定不相等", "never equal"), ("相等", "equidistant from the two arms"),
                      ("只能是角的顶点", "must be the vertex only"), ("没有几何意义", "has no geometric meaning"))),
    dict(type="numeric", stem_zh="线段 $PQ$ 长 $10\\ \\mathrm{cm}$。中点到 $P$ 的距离是多少厘米？",
         stem_en="Segment $PQ$ is $10\\ \\mathrm{cm}$ long. How many centimetres is it from $P$ to the midpoint?",
         answer=5, exp_zh="中点平分线段，为 $5\\ \\mathrm{cm}$。", exp_en="The midpoint halves the segment, so $5\\ \\mathrm{cm}$.", tolerance=0),
  ])

L("mathematics-8-7-1", "数列与函数", "Sequences and functions",
  "本节你将学会求出线性数列的通项，并用函数机器或映射理解输入与输出。",
  "This lesson you will find the $n$th term of a linear sequence and use function machines or mappings for inputs and outputs.",
  [("等差数列每次增加（或减少）一个常数，称为公差。", "An arithmetic sequence goes up or down by a constant difference."),
   ("第 $n$ 项常可写成 $an+b$ 的形式。$a$ 就是公差。", "The $n$th term can often be written $an+b$, where $a$ is the common difference."),
   ("函数把一个输入变成唯一的输出。", "A function turns an input into a single output."),
   ("若 $f(x)=3x-1$，则 $f(4)=11$。", "If $f(x)=3x-1$, then $f(4)=11$.")],
  r"""数列 $5,8,11,14,\\ldots$ 每次加 $3$。与 $3n$ 比较：$3,6,9,12,\\ldots$ 每项都比给定数列少 $2$，所以通项是 $3n+2$。检验：$n=1$ 时 $5$，$n=2$ 时 $8$。

函数可以看成一台机器：输入 $x$，先乘 $3$ 再减 $1$，输出 $3x-1$。同一个输入只能对应一个输出。""",
  r"""The sequence $5,8,11,14,\\ldots$ increases by $3$ each time. Compare with $3n$: $3,6,9,12,\\ldots$ is $2$ less than the given sequence in each position, so the $n$th term is $3n+2$. Check: $n=1$ gives $5$, $n=2$ gives $8$.

A function can be seen as a machine: input $x$, multiply by $3$ and subtract $1$, output $3x-1$. One input must give one output.""",
  r"""求 $4,7,10,13,\\ldots$ 的第 $n$ 项，并求 $f(x)=2x+5$ 当 $x=6$ 时的值。

**解：** 公差 $3$，通项 $3n+1$。$f(6)=12+5=17$。""",
  r"""Find the $n$th term of $4,7,10,13,\\ldots$, and find $f(6)$ if $f(x)=2x+5$.

**Solution:** The common difference is $3$, so the $n$th term is $3n+1$. $f(6)=12+5=17$.""",
  [("把公差当成第 $1$ 项，写成 $n+3$ 却去描述每次加 $3$ 且首项为 $5$ 的数列。", "Using $n+3$ for a sequence that starts at $5$ and goes up by $3$."),
   ("通项里的 $n$ 从 $0$ 开始却按从 $1$ 检验。本课 $n$ 从 $1$ 开始。", "Starting $n$ at $0$ but checking as if $n$ starts at $1$. In this course $n$ starts at $1$."),
   ("一个输入给出两个不同输出却仍称为函数。", "Calling a rule a function when one input gives two different outputs.")],
  [
    dict(type="short", stem_zh="数列 $5,8,11,14,\\ldots$ 的第 $n$ 项是什么？", stem_en="What is the $n$th term of $5,8,11,14,\\ldots$?",
         answer="3n+2", accepted=["3n+2", "3n + 2", "2+3n"],
         answer_zh="$3n+2$", answer_en="$3n+2$", exp_zh="公差 $3$，与 $3n$ 相比多 $2$。", exp_en="Difference $3$; $2$ more than $3n$."),
    dict(type="short", stem_zh="数列 $4,7,10,13,\\ldots$ 的第 $n$ 项是什么？", stem_en="What is the $n$th term of $4,7,10,13,\\ldots$?",
         answer="3n+1", accepted=["3n+1", "3n + 1", "1+3n"],
         answer_zh="$3n+1$", answer_en="$3n+1$", exp_zh="公差 $3$，第 $1$ 项是 $4=3+1$。", exp_en="Difference $3$; first term $4=3+1$."),
    dict(type="numeric", stem_zh="上一问的数列第 $10$ 项是多少？", stem_en="What is the $10$th term of that sequence?",
         answer=31, exp_zh="$3\\times 10+1=31$。", exp_en="$3\\times 10+1=31$.", tolerance=0),
    dict(type="numeric", stem_zh="若 $f(x)=3x-1$，则 $f(4)$ 等于多少？", stem_en="If $f(x)=3x-1$, what is $f(4)$?",
         answer=11, exp_zh="$12-1=11$。", exp_en="$12-1=11$.", tolerance=0),
    dict(type="numeric", stem_zh="若 $f(x)=2x+5$，则 $f(6)$ 等于多少？", stem_en="If $f(x)=2x+5$, what is $f(6)$?",
         answer=17, exp_zh="$12+5=17$。", exp_en="$12+5=17$.", tolerance=0),
    dict(type="mcq", stem_zh="数列 $20,17,14,11,\\ldots$ 的第 $n$ 项是？", stem_en="The $n$th term of $20,17,14,11,\\ldots$ is:",
         answer="d", exp_zh="公差 $-3$，通项 $-3n+23$ 或 $23-3n$。", exp_en="Difference $-3$, so $23-3n$.",
         options=opts(("$3n+20$", "$3n+20$"), ("$n-3$", "$n-3$"), ("$20n$", "$20n$"), ("$23-3n$", "$23-3n$"))),
  ])

L("mathematics-8-7-2", "直线的图像与方程", "Graphs and equations of straight lines",
  "本节你将学会画出直线 $y=mx+c$，并从图或方程中读出斜率和截距。",
  "This lesson you will draw the line $y=mx+c$ and read the gradient and intercept from a graph or an equation.",
  [("$y=mx+c$ 中，$m$ 是斜率，$c$ 是与 $y$ 轴的交点。", "In $y=mx+c$, $m$ is the gradient and $c$ is the intercept on the $y$-axis."),
   ("斜率 $=\\dfrac{\\text{竖直变化}}{\\text{水平变化}}$。", "Gradient $=\\dfrac{\\text{vertical change}}{\\text{horizontal change}}$."),
   ("$m>0$ 向右上升，$m<0$ 向右下降，$m=0$ 是水平线。", "If $m>0$ the line rises to the right; if $m<0$ it falls; if $m=0$ it is horizontal."),
   ("$x=k$ 是竖直线，不能写成 $y=mx+c$ 的有限 $m$。", "A line $x=k$ is vertical and cannot be written as $y=mx+c$ with a finite $m$.")],
  r"""先标出 $c$：直线与 $y$ 轴交于 $(0,c)$。再从这一点按斜率“右移 $1$，上移 $m$”（若 $m$ 是分数就按分子分母移动）。例如 $y=2x-1$ 交 $y$ 轴于 $-1$，斜率为 $2$。

已知两点也可求斜率。过 $(1,3)$ 和 $(4,9)$ 的直线，斜率 $(9-3)/(4-1)=2$。""",
  r"""Plot $c$ first: the line meets the $y$-axis at $(0,c)$. From there, use the gradient: one step right and $m$ up (or use the numerator and denominator if $m$ is a fraction). For example $y=2x-1$ meets the $y$-axis at $-1$ and has gradient $2$.

You can also find a gradient from two points. Through $(1,3)$ and $(4,9)$ the gradient is $(9-3)/(4-1)=2$.""",
  r"""直线 $y=-\\dfrac{1}{2}x+3$ 的斜率和 $y$ 轴截距分别是什么？

**解：** $m=-1/2$，$c=3$。向右下降，与 $y$ 轴交于 $(0,3)$。""",
  r"""What are the gradient and $y$-intercept of $y=-\\dfrac{1}{2}x+3$?

**Solution:** $m=-1/2$ and $c=3$. The line falls to the right and meets the $y$-axis at $(0,3)$.""",
  [("把 $c$ 当成斜率、$m$ 当成截距。", "Swapping $m$ and $c$."),
   ("斜率写反成水平除以竖直。", "Writing gradient as horizontal change over vertical change."),
   ("把 $x=2$ 说成斜率是 $2$ 的水平线。它是竖直线。", "Calling $x=2$ a horizontal line of gradient $2$. It is vertical.")],
  [
    dict(type="mcq", stem_zh="$y=2x-1$ 的斜率是？", stem_en="The gradient of $y=2x-1$ is:",
         answer="a", exp_zh="$m=2$。", exp_en="$m=2$.",
         options=opts(("$2$", "$2$"), ("$-1$", "$-1$"), ("$1$", "$1$"), ("$0$", "$0$"))),
    dict(type="numeric", stem_zh="$y=2x-1$ 与 $y$ 轴交点的纵坐标是多少？", stem_en="The $y$-intercept of $y=2x-1$ is:",
         answer=-1, exp_zh="$c=-1$。", exp_en="$c=-1$.", tolerance=0),
    dict(type="numeric", stem_zh="过 $(1,3)$ 和 $(4,9)$ 的直线，斜率是多少？",
         stem_en="What is the gradient of the line through $(1,3)$ and $(4,9)$?",
         answer=2, exp_zh="$(9-3)/(4-1)=2$。", exp_en="$(9-3)/(4-1)=2$.", tolerance=0),
    dict(type="mcq", stem_zh="$y=-\\dfrac{1}{2}x+3$ 的图像向右是？", stem_en="As $x$ increases, the line $y=-\\dfrac{1}{2}x+3$:",
         answer="c", exp_zh="斜率为负，向右下降。", exp_en="The gradient is negative, so it falls to the right.",
         options=opts(("上升", "rises"), ("水平", "is horizontal"), ("下降", "falls"), ("竖直", "is vertical"))),
    dict(type="mcq", stem_zh="直线 $x=2$ 是？", stem_en="The line $x=2$ is:",
         answer="b", exp_zh="竖直线，斜率为无限，不能写成有限的 $m$。", exp_en="Vertical, with undefined (infinite) gradient.",
         options=opts(("斜率为 $2$ 的水平线", "a horizontal line of gradient $2$"), ("竖直线", "a vertical line"),
                      ("斜率为 $2$ 的斜线", "a slanted line of gradient $2$"), ("与 $y$ 轴交于 $2$", "a line with $y$-intercept $2$"))),
    dict(type="numeric", stem_zh="$y=3$ 这条直线的斜率是多少？", stem_en="What is the gradient of the line $y=3$?",
         answer=0, exp_zh="水平线斜率为 $0$。", exp_en="A horizontal line has gradient $0$.", tolerance=0),
  ], diagram=D_LINE)

L("mathematics-8-8-1", "平移与向量", "Translations and vectors",
  "本节你将学会用列向量描述平移，并完成简单的向量加减。",
  "This lesson you will describe translations with column vectors and add or subtract simple vectors.",
  [("平移把每个点沿同一方向移动同样的距离，图形全等，方向不变。", "A translation moves every point the same distance in the same direction; the image is congruent and does not turn."),
   ("列向量 $\\begin{pmatrix} a \\\\ b \\end{pmatrix}$ 表示向右 $a$、向上 $b$（负号则相反）。", "The column vector $\\begin{pmatrix} a \\\\ b \\end{pmatrix}$ means $a$ right and $b$ up (negatives reverse those directions)."),
   ("向量相加：对应分量相加。", "To add vectors, add corresponding components."),
   ("平移可逆：反向向量把图像移回原处。", "A translation can be reversed: the opposite vector takes the image back.")],
  r"""点 $(2,1)$ 按 $\\begin{pmatrix} 3 \\\\ -4 \\end{pmatrix}$ 平移后到 $(5,-3)$。所有点都右移 $3$、下移 $4$，所以线段长度和角度不变，只是位置变了。

$\\begin{pmatrix} 3 \\\\ -1 \\end{pmatrix}+\\begin{pmatrix} 2 \\\\ 5 \\end{pmatrix}=\\begin{pmatrix} 5 \\\\ 4 \\end{pmatrix}$。连续两次平移，效果等于这两个向量之和。""",
  r"""The point $(2,1)$ translated by $\\begin{pmatrix} 3 \\\\ -4 \\end{pmatrix}$ arrives at $(5,-3)$. Every point moves $3$ right and $4$ down, so lengths and angles stay the same; only the position changes.

$\\begin{pmatrix} 3 \\\\ -1 \\end{pmatrix}+\\begin{pmatrix} 2 \\\\ 5 \\end{pmatrix}=\\begin{pmatrix} 5 \\\\ 4 \\end{pmatrix}$. Two translations in succession have the same effect as the sum of the two vectors.""",
  r"""点 $P(1,4)$ 平移到 $P'(6,2)$。写出平移向量。

**解：** 右移 $5$，下移 $2$，向量为 $\\begin{pmatrix} 5 \\\\ -2 \\end{pmatrix}$。""",
  r"""Point $P(1,4)$ is translated to $P'(6,2)$. Write the translation vector.

**Solution:** $5$ right and $2$ down, so the vector is $\\begin{pmatrix} 5 \\\\ -2 \\end{pmatrix}$.""",
  [("把上下分量写反，或把向左写成正的第一分量。", "Swapping the vertical component, or writing a leftward move as a positive first component."),
   ("以为平移会改变图形大小。", "Thinking a translation changes the size of the shape."),
   ("向量相加时把分量相乘。", "Multiplying components instead of adding them.")],
  [
    dict(type="short", stem_zh="$(2,1)$ 按 $\\begin{pmatrix} 3 \\\\ -4 \\end{pmatrix}$ 平移后的坐标是什么？",
         stem_en="What are the coordinates of $(2,1)$ after translation by $\\begin{pmatrix} 3 \\\\ -4 \\end{pmatrix}$?",
         answer="(5,-3)", accepted=["(5,-3)", "(5, -3)", "5,-3"],
         answer_zh="$(5,-3)$", answer_en="$(5,-3)$", exp_zh="$2+3=5$，$1-4=-3$。", exp_en="$2+3=5$, $1-4=-3$."),
    dict(type="short", stem_zh="$P(1,4)$ 平移到 $P'(6,2)$。平移向量是什么？",
         stem_en="$P(1,4)$ is translated to $P'(6,2)$. What is the column vector?",
         answer="(5,-2)", accepted=["(5,-2)", "\\begin{pmatrix}5\\\\-2\\end{pmatrix}", "(5, -2)", "5,-2"],
         answer_zh="$\\begin{pmatrix} 5 \\\\ -2 \\end{pmatrix}$", answer_en="$\\begin{pmatrix} 5 \\\\ -2 \\end{pmatrix}$",
         exp_zh="$6-1=5$，$2-4=-2$。", exp_en="$6-1=5$, $2-4=-2$."),
    dict(type="short", stem_zh="$\\begin{pmatrix} 3 \\\\ -1 \\end{pmatrix}+\\begin{pmatrix} 2 \\\\ 5 \\end{pmatrix}$ 等于什么？",
         stem_en="What is $\\begin{pmatrix} 3 \\\\ -1 \\end{pmatrix}+\\begin{pmatrix} 2 \\\\ 5 \\end{pmatrix}$?",
         answer="(5,4)", accepted=["(5,4)", "(5, 4)", "5,4"],
         answer_zh="$\\begin{pmatrix} 5 \\\\ 4 \\end{pmatrix}$", answer_en="$\\begin{pmatrix} 5 \\\\ 4 \\end{pmatrix}$",
         exp_zh="分量分别相加。", exp_en="Add the components."),
    dict(type="mcq", stem_zh="平移会改变图形的？", stem_en="A translation changes a shape’s:",
         answer="d", exp_zh="只改变位置，不改变大小、形状和朝向。", exp_en="Position only, not size, shape or orientation.",
         options=opts(("大小", "size"), ("形状", "shape"), ("朝向", "orientation"), ("位置", "position"))),
    dict(type="short", stem_zh="把图形按 $\\begin{pmatrix} 4 \\\\ -1 \\end{pmatrix}$ 移回去，应使用什么向量？",
         stem_en="Which vector reverses a translation by $\\begin{pmatrix} 4 \\\\ -1 \\end{pmatrix}$?",
         answer="(-4,1)", accepted=["(-4,1)", "(-4, 1)", "-4,1"],
         answer_zh="$\\begin{pmatrix} -4 \\\\ 1 \\end{pmatrix}$", answer_en="$\\begin{pmatrix} -4 \\\\ 1 \\end{pmatrix}$",
         exp_zh="取相反向量。", exp_en="Use the opposite vector."),
    dict(type="mcq", stem_zh="向量 $\\begin{pmatrix} -2 \\\\ 5 \\end{pmatrix}$ 表示？", stem_en="The vector $\\begin{pmatrix} -2 \\\\ 5 \\end{pmatrix}$ means:",
         answer="a", exp_zh="向左 $2$，向上 $5$。", exp_en="$2$ left and $5$ up.",
         options=opts(("向左 $2$，向上 $5$", "$2$ left and $5$ up"), ("向右 $2$，向下 $5$", "$2$ right and $5$ down"),
                      ("向左 $5$，向上 $2$", "$5$ left and $2$ up"), ("向右 $5$，向上 $2$", "$5$ right and $2$ up"))),
  ], diagram=D_VEC)

L("mathematics-8-8-2", "反射、旋转与放大", "Reflections, rotations and enlargements",
  "本节你将学会完成反射、旋转和放大，并说明哪些变换保持全等、哪些改变大小。",
  "This lesson you will carry out reflections, rotations and enlargements, and state which transformations preserve congruence and which change size.",
  [("反射是关于一条镜射线的翻转，全等，但朝向通常相反。", "A reflection flips a shape in a mirror line; the image is congruent but usually reversed."),
   ("旋转是绕一个中心转过一个角，全等，朝向保持。", "A rotation turns a shape about a centre through an angle; the image is congruent and orientation is kept."),
   ("放大需要中心和正比例尺 $k$。长度变为原来的 $k$ 倍，角不变。", "An enlargement needs a centre and a positive scale factor $k$. Lengths become $k$ times as long; angles are unchanged."),
   ("$k>1$ 变大，$0<k<1$ 变小；$k=1$ 大小不变。", "If $k>1$ the image is larger; if $0<k<1$ it is smaller; if $k=1$ the size is unchanged.")],
  r"""反射时，从一点到镜射线的垂线，像点在另一侧同样远处。旋转时，每一点到中心的距离不变，与中心连线转过相同的角。

放大不是“随便画大一点”：每一点与中心的连线方向不变，距离乘以 $k$。若 $A$ 到中心是 $2\\ \\mathrm{cm}$，$k=3$，则 $A'$ 在同一射线上，距离为 $6\\ \\mathrm{cm}$。面积变为原来的 $k^2$ 倍。""",
  r"""In a reflection, the image of a point is the same perpendicular distance from the mirror line, on the other side. In a rotation, the distance from the centre stays the same, and the line to the centre turns through the same angle.

An enlargement is not “draw it a bit bigger”: the direction from the centre to each point stays the same, and the distance is multiplied by $k$. If $A$ is $2\\ \\mathrm{cm}$ from the centre and $k=3$, then $A'$ lies on the same ray, $6\\ \\mathrm{cm}$ from the centre. Areas are multiplied by $k^2$.""",
  r"""一个图形按比例尺 $3$ 放大。一条原来 $4\\ \\mathrm{cm}$ 的边变成多长？面积如何变？

**解：** 边长变成 $12\\ \\mathrm{cm}$。面积变为原来的 $9$ 倍。""",
  r"""A shape is enlarged with scale factor $3$. What happens to a side of $4\\ \\mathrm{cm}$, and to the area?

**Solution:** The side becomes $12\\ \\mathrm{cm}$. The area becomes $9$ times as large.""",
  [("把放大当成平移或只把图形挪远一点而不按中心放缩。", "Treating an enlargement as a translation, or moving the shape without scaling from the centre."),
   ("以为反射后仍与原图形可以不翻转就重合。朝向通常相反。", "Thinking a reflection can be matched to the original without a flip. Orientation is usually reversed."),
   ("面积也只乘 $k$ 而不是 $k^2$。", "Multiplying area by $k$ instead of $k^2$.")],
  [
    dict(type="numeric", stem_zh="比例尺为 $3$ 的放大，把 $4\\ \\mathrm{cm}$ 的边变成多少厘米？",
         stem_en="An enlargement of scale factor $3$ turns a $4\\ \\mathrm{cm}$ side into how many centimetres?",
         answer=12, exp_zh="$4\\times 3=12$。", exp_en="$4\\times 3=12$.", tolerance=0),
    dict(type="numeric", stem_zh="比例尺为 $3$ 时，面积变为原来的多少倍？",
         stem_en="With scale factor $3$, the area becomes how many times as large?",
         answer=9, exp_zh="面积比例是 $3^2=9$。", exp_en="The area factor is $3^2=9$.", tolerance=0),
    dict(type="mcq", stem_zh="下列哪一种变换通常会改变图形的大小？", stem_en="Which transformation usually changes the size of a shape?",
         answer="c", exp_zh="放大（比例尺不是 $1$ 时）改变大小；平移、反射、旋转保持全等。", exp_en="Enlargement (when the scale factor is not $1$) changes size; translation, reflection and rotation keep congruence.",
         options=opts(("平移", "translation"), ("反射", "reflection"), ("放大（比例尺 $\\neq 1$）", "enlargement (scale factor $\\neq 1$)"), ("旋转", "rotation"))),
    dict(type="mcq", stem_zh="反射后的像与原图形相比，通常？", stem_en="Compared with the original, a reflected image is usually:",
         answer="b", exp_zh="全等但朝向相反（翻转）。", exp_en="Congruent but with reversed orientation (flipped).",
         options=opts(("大小改变", "a different size"), ("全等但翻转", "congruent but flipped"),
                      ("变成完全不同的边数", "a different number of sides"), ("只平移而不翻转", "translated with no flip"))),
    dict(type="numeric", stem_zh="比例尺为 $\\dfrac{1}{2}$ 的放大，把 $10\\ \\mathrm{cm}$ 的边变成多少厘米？",
         stem_en="An enlargement of scale factor $\\dfrac{1}{2}$ turns a $10\\ \\mathrm{cm}$ side into how many centimetres?",
         answer=5, exp_zh="$10\\times \\dfrac{1}{2}=5$。", exp_en="$10\\times \\dfrac{1}{2}=5$.", tolerance=0),
    dict(type="mcq", stem_zh="绕一点旋转 $90^\\circ$ 后，点到旋转中心的距离？", stem_en="After a rotation of $90^\\circ$ about a centre, the distance from a point to the centre:",
         answer="a", exp_zh="保持不变。", exp_en="Stays the same.",
         options=opts(("不变", "stays the same"), ("一定加倍", "must double"), ("一定变为零", "must become zero"), ("一定减半", "must halve"))),
  ])

L("mathematics-8-9-1", "数据类型与收集方法", "Data types and collection methods",
  "本节你将学会区分分类数据与数值数据，以及离散与连续，并选择合适的收集方法。",
  "This lesson you will distinguish categorical and numerical data, and discrete and continuous data, and choose a suitable collection method.",
  [("分类数据是名称或类别，例如最喜欢的颜色。", "Categorical data are names or categories, such as favourite colour."),
   ("数值数据是数。离散数据通常可数，如人数；连续数据可在一段范围内取值，如身高。", "Numerical data are numbers. Discrete data are usually counted, such as number of people; continuous data can take values in a range, such as height."),
   ("收集方法包括问卷、观察、测量和实验。方法要匹配问题。", "Collection methods include questionnaires, observation, measurement and experiment. The method should match the question."),
   ("样本应尽量避免明显偏差，问题不应有诱导性。", "A sample should avoid obvious bias, and questions should not lead the respondent.")],
  r"""“你最喜欢的运动是什么”得到分类数据。“你家有几口人”是离散的数值数据。“你的身高是多少”是连续数据，因为理论上可以是某一范围内的任何值，只是测量精度有限。

若要了解全校学生对食堂的看法，只问篮球队队员就不合适，因为样本可能偏差。问卷选项应清楚、互不重叠。""",
  r"""“What is your favourite sport?” gives categorical data. “How many people live in your home?” is discrete numerical data. “What is your height?” is continuous, because in principle any value in a range is possible, even if measurement is only accurate to a certain degree.

If you want the views of a whole school on the canteen, asking only the basketball team is unwise, because the sample may be biased. Questionnaire options should be clear and should not overlap.""",
  r"""判断下列数据的类型：鞋码、到校时间（以分钟计的精确计时）、最喜欢的科目。

**解：** 鞋码通常视为离散数值（或有时当分类）；到校用时是连续数值；最喜欢的科目是分类数据。""",
  r"""Classify these: shoe size, time taken to travel to school (measured in minutes with a precise timer), and favourite subject.

**Solution:** Shoe size is usually discrete numerical (sometimes treated as categorical); journey time is continuous numerical; favourite subject is categorical.""",
  [("把身高当成离散，只因为记录成了整数厘米。类型取决于量本身。", "Calling height discrete just because it was recorded to the nearest centimetre. The type depends on the quantity itself."),
   ("用一个有偏差的样本代表全体。", "Using a biased sample to stand for the whole group."),
   ("问卷选项互相重叠，例如 $0$–$5$ 和 $5$–$10$。", "Overlapping questionnaire options, such as $0$–$5$ and $5$–$10$.")],
  [
    dict(type="mcq", stem_zh="“最喜欢的颜色”属于？", stem_en="“Favourite colour” is:",
         answer="a", exp_zh="分类数据。", exp_en="Categorical data.",
         options=opts(("分类数据", "categorical data"), ("连续数值数据", "continuous numerical data"),
                      ("只能是实验概率", "experimental probability only"), ("向量", "a vector"))),
    dict(type="mcq", stem_zh="身高通常属于？", stem_en="Height is usually:",
         answer="c", exp_zh="连续数值数据。", exp_en="Continuous numerical data.",
         options=opts(("分类数据", "categorical"), ("离散且只能是颜色", "discrete and only a colour"),
                      ("连续数值数据", "continuous numerical data"), ("不是数据", "not data"))),
    dict(type="mcq", stem_zh="“家庭人口数”通常属于？", stem_en="“Number of people in a household” is usually:",
         answer="b", exp_zh="离散数值数据。", exp_en="Discrete numerical data.",
         options=opts(("连续数据", "continuous data"), ("离散数值数据", "discrete numerical data"),
                      ("只能是分类颜色", "categorical colour only"), ("不是数据", "not data"))),
    dict(type="mcq", stem_zh="要了解全校学生对食堂的看法，只调查篮球队，主要问题是？",
         stem_en="To learn the whole school’s views on the canteen, asking only the basketball team is a problem mainly because:",
         answer="d", exp_zh="样本可能有偏差，不能代表全体。", exp_en="The sample may be biased and may not represent the whole school.",
         options=opts(("数据一定是向量", "the data must be vectors"), ("身高不能被测量", "height cannot be measured"),
                      ("分类数据不存在", "categorical data do not exist"), ("样本可能有偏差", "the sample may be biased"))),
    dict(type="mcq", stem_zh="问卷选项 $0$–$5$ 和 $5$–$10$ 的问题是？", stem_en="The problem with options $0$–$5$ and $5$–$10$ is that they:",
         answer="a", exp_zh="在 $5$ 处重叠，有的人不知如何选。", exp_en="Overlap at $5$, so some people would not know which to tick.",
         options=opts(("相互重叠", "overlap"), ("一定是连续向量", "must be continuous vectors"),
                      ("只能用于反射", "can only be used for reflections"), ("完全正确，无需改进", "are already perfect"))),
    dict(type="short", stem_zh="举出一个连续数值数据的例子。", stem_en="Give one example of continuous numerical data.",
         answer="height", accepted=["height", "weight", "time", "temperature", "length", "身高", "体重", "时间", "温度", "长度"],
         answer_zh="例如身高、时间或温度。", answer_en="For example height, time or temperature.",
         exp_zh="连续数据可在某一范围内取值。", exp_en="Continuous data can take values in a range."),
  ])

L("mathematics-8-9-2", "记录与解释数据", "Recording and interpreting data",
  "本节你将学会用表格、条形图、饼图或折线图记录并解读数据，选择合适的图像。",
  "This lesson you will record and interpret data using tables, bar charts, pie charts or line graphs, and choose a suitable diagram.",
  [("条形图适合分类数据或离散数据的频数。", "A bar chart is suitable for frequencies of categorical or discrete data."),
   ("饼图用扇形表示各部分占整体的比例，各部分之和应为全部。", "A pie chart uses sectors for parts of a whole; the parts should add to the whole."),
   ("折线图适合表示随时间变化的趋势。", "A line graph is suitable for showing a trend over time."),
   ("读图时要看标题、坐标轴的量和单位，不要只看图形“看起来陡”。", "When you read a graph, use the title and the quantities and units on the axes; do not judge only by how steep it looks.")],
  r"""先选对图。比较各爱好的人数，用条形图清楚；表示“各部分占全班的比例”，饼图合适；记录一周气温变化，折线图更好。饼图中，若全班 $30$ 人有 $5$ 人选择某项，对应圆心角是 $\\dfrac{5}{30}\\times 360^\\circ=60^\\circ$。

解读时写出具体数字和比较，而不是只说“很多”或“很少”。""",
  r"""Choose the diagram first. Frequencies of favourite hobbies are clear on a bar chart; parts of a class total suit a pie chart; temperature over a week is better as a line graph. On a pie chart, if $5$ out of $30$ students choose an option, the angle is $\\dfrac{5}{30}\\times 360^\\circ=60^\\circ$.

When you interpret, quote actual figures and comparisons, rather than only writing “many” or “few”.""",
  r"""全班 $24$ 人，有 $6$ 人最喜欢篮球。饼图中该项目的圆心角是多少？

**解：** $\\dfrac{6}{24}\\times 360^\\circ=90^\\circ$。""",
  r"""In a class of $24$, $6$ students prefer basketball. What angle should that sector have on a pie chart?

**Solution:** $\\dfrac{6}{24}\\times 360^\\circ=90^\\circ$.""",
  [("用饼图表示没有“总体为 $100\\%$”的互不相关的量。", "Using a pie chart for quantities that are not parts of one whole."),
   ("折线图的纵轴不是从 $0$ 开始时，却把斜率夸大成“翻了几倍”。要读刻度。", "Ignoring the scale when the vertical axis does not start at $0$, and overstating a slope as a huge increase."),
   ("条形图的直条宽度或间隔不统一，造成误导。", "Misleading bar charts with unequal bar widths or gaps.")],
  [
    dict(type="numeric", stem_zh="全班 $24$ 人中有 $6$ 人喜欢篮球。饼图中该扇形的圆心角是多少度？",
         stem_en="In a class of $24$, $6$ prefer basketball. The pie-chart angle in degrees?",
         answer=90, exp_zh="$6/24\\times 360=90$。", exp_en="$6/24\\times 360=90$.", tolerance=0),
    dict(type="numeric", stem_zh="$30$ 人中有 $5$ 人选择某项。对应圆心角是多少度？",
         stem_en="$5$ out of $30$ choose an option. The sector angle in degrees?",
         answer=60, exp_zh="$5/30\\times 360=60$。", exp_en="$5/30\\times 360=60$.", tolerance=0),
    dict(type="mcq", stem_zh="表示一周气温变化，最合适的是？", stem_en="To show temperature over a week, the most suitable diagram is usually a:",
         answer="c", exp_zh="折线图适合趋势。", exp_en="A line graph suits a trend over time.",
         options=opts(("只显示一个点的饼图", "a pie chart with only one point"), ("反射图", "a reflection diagram"),
                      ("折线图", "line graph"), ("旋转中心", "a centre of rotation"))),
    dict(type="mcq", stem_zh="比较各爱好的人数，较合适的是？", stem_en="To compare frequencies of favourite hobbies, a suitable diagram is a:",
         answer="a", exp_zh="条形图适合分类频数。", exp_en="A bar chart suits categorical frequencies.",
         options=opts(("条形图", "bar chart"), ("只能用 $y=mx+c$", "only $y=mx+c$"),
                      ("只能用方位角", "only bearings"), ("垂直平分线", "a perpendicular bisector"))),
    dict(type="mcq", stem_zh="读图时最应该先看？", stem_en="When reading a graph you should first look at:",
         answer="b", exp_zh="标题、坐标轴的量和单位。", exp_en="The title and the quantities and units on the axes.",
         options=opts(("只看颜色好不好看", "only whether the colours look nice"), ("标题与坐标轴的量和单位", "the title and the quantities and units on the axes"),
                      ("忽略刻度", "the graph while ignoring the scale"), ("只看是否“看起来陡”", "only whether it looks steep"))),
    dict(type="mcq", stem_zh="饼图各部分加起来应？", stem_en="The parts of a pie chart should add to:",
         answer="d", exp_zh="表示一个总体，应为全部（$360^\\circ$ 或 $100\\%$）。", exp_en="They represent one whole, so they should make $360^\\circ$ or $100\\%$.",
         options=opts(("任意一个小于 $10^\\circ$ 的角", "any angle less than $10^\\circ$"), ("只有 $90^\\circ$", "only $90^\\circ$"),
                      ("无法确定", "an unknown total"), ("整个总体", "the whole"))),
  ])

L("mathematics-8-9-3", "描述统计量", "Using descriptive statistics",
  "本节你将学会计算并解释平均数、中位数、众数和极差，并判断哪一个更合适。",
  "This lesson you will calculate and interpret the mean, median, mode and range, and judge which is more suitable.",
  [("平均数是总和除以个数。", "The mean is the total divided by the number of values."),
   ("中位数是按大小排列后最中间的值（偶数个则取中间两个的平均）。", "The median is the middle value when the data are ordered (or the mean of the two middle values if there is an even number)."),
   ("众数是出现次数最多的值，可能不止一个，也可能没有。", "The mode is the most frequent value; there may be more than one mode, or no mode."),
   ("极差 $=$ 最大值 $-$ 最小值，描述离散程度。", "The range $=$ largest $-$ smallest and describes spread."),
   ("有极端值时，中位数往往比平均数更能代表“典型”水平。", "If there are extreme values, the median often represents a typical level better than the mean.")],
  r"""数据 $2,3,3,5,12$。平均数 $(2+3+3+5+12)/5=5$。按顺序已排好，中位数是 $3$。众数是 $3$。极差 $12-2=10$。这里 $12$ 较大，把平均数拉到 $5$，比多数数据都大，所以中位数 $3$ 可能更恰当。

选用哪一个统计量，要看问题：想看最常见的选项用众数；想看中间水平用中位数；需要考虑每一个值、且没有离谱极端值时，平均数有用。""",
  r"""For the data $2,3,3,5,12$, the mean is $(2+3+3+5+12)/5=5$. The list is already ordered, so the median is $3$. The mode is $3$. The range is $12-2=10$. The value $12$ is large and pulls the mean up to $5$, which is bigger than most of the numbers, so the median $3$ may be more typical.

Which statistic you choose depends on the question: use the mode for the most common category, the median for a typical middle value, and the mean when every value should count and extreme values are not distorting the picture.""",
  r"""求 $4,7,7,10$ 的平均数、中位数、众数和极差。

**解：** 平均数 $28/4=7$。中位数是中间两个 $7$ 与 $7$ 的平均，仍是 $7$。众数是 $7$。极差 $10-4=6$。""",
  r"""Find the mean, median, mode and range of $4,7,7,10$.

**Solution:** The mean is $28/4=7$. The median is the mean of the two middle $7$s, still $7$. The mode is $7$. The range is $10-4=6$.""",
  [("未排序就取中位数。", "Reading the median from an unordered list."),
   ("把极差当成平均数。", "Calling the range the mean."),
   ("有极端值时仍坚持平均数一定最能代表全组。", "Insisting that the mean must be the most representative when there is an extreme value.")],
  [
    dict(type="numeric", stem_zh="数据 $2,3,3,5,12$ 的平均数是多少？", stem_en="What is the mean of $2,3,3,5,12$?",
         answer=5, exp_zh="总和 $25$，除以 $5$ 得 $5$。", exp_en="The total is $25$, divided by $5$ is $5$.", tolerance=0),
    dict(type="numeric", stem_zh="这组数据的中位数是多少？", stem_en="What is the median of that list?",
         answer=3, exp_zh="中间的数是 $3$。", exp_en="The middle value is $3$.", tolerance=0),
    dict(type="numeric", stem_zh="这组数据的众数是多少？", stem_en="What is the mode of that list?",
         answer=3, exp_zh="$3$ 出现两次，次数最多。", exp_en="$3$ appears twice, more than any other value.", tolerance=0),
    dict(type="numeric", stem_zh="这组数据的极差是多少？", stem_en="What is the range of that list?",
         answer=10, exp_zh="$12-2=10$。", exp_en="$12-2=10$.", tolerance=0),
    dict(type="numeric", stem_zh="$4,7,7,10$ 的平均数是多少？", stem_en="What is the mean of $4,7,7,10$?",
         answer=7, exp_zh="$28/4=7$。", exp_en="$28/4=7$.", tolerance=0),
    dict(type="mcq", stem_zh="一组收入数据里有一个特别大的值。若要表示“典型”收入，往往更合适的是？",
         stem_en="A data set of incomes includes one unusually large value. To represent a typical income, it is often better to use the:",
         answer="b", exp_zh="中位数较少受极端值影响。", exp_en="The median is less affected by an extreme value.",
         options=opts(("一定用极差", "range only"), ("中位数", "median"), ("只有众数且必须是最大收入", "mode, which must be the largest income"),
                      ("忽略所有数据", "ignore all the data"))),
  ])

L("mathematics-8-9-4", "统计循环", "The statistical cycle",
  "本节你将学会按统计循环来计划、收集、整理、呈现并作出有限度的结论。",
  "This lesson you will plan, collect, organise, present and draw cautious conclusions, following the statistical cycle.",
  [("一个常用循环是：提出问题 → 设计并收集 → 整理呈现 → 解释结论 → 必要时回到问题再改进。", "A useful cycle is: pose a question → plan and collect → organise and present → interpret and conclude → return to the question and improve if needed."),
   ("问题要具体，才能决定收集什么数据。", "The question must be specific enough to decide what data to collect."),
   ("结论不能超出样本所能支持的范围，并应指出局限。", "Conclusions should not go beyond what the sample can support, and limitations should be stated."),
   ("若方法有偏差或图像有误导，结论就不可靠，需要回到计划阶段。", "If the method is biased or the diagram is misleading, the conclusion is weak and you should return to the planning stage.")],
  r"""统计不是“先画一张好看的图再找一句话”。应先有一个清楚的问题，例如“八年级学生通常花多少分钟做数学作业？”，再决定向谁问、问多少人、用问卷还是记录本。收集后整理成表和图，计算合适的统计量，最后回答问题，并说明样本是否太小、是否有偏差。

如果发现只问了同一个辅导班的同学，就应承认局限，或重新抽样。这就是循环：结论可以引出更好的下一个问题。""",
  r"""Statistics is not “draw a handsome chart and then invent a sentence”. Start with a clear question, such as “How many minutes do Year 8 students typically spend on mathematics homework?”, then decide whom to ask, how many people, and whether to use a questionnaire or a log. After collecting, organise the data in tables and diagrams, calculate suitable statistics, and answer the question, stating whether the sample was small or biased.

If you find you only asked students from one tuition class, you should admit the limitation or sample again. That is the cycle: a conclusion can lead to a better next question.""",
  r"""一项调查只在篮球训练后询问“你每周运动多久”，就得出“全校学生运动时间都很长”。问题在哪里？下一步该做什么？

**解：** 样本有偏差，结论超出了样本范围。应扩大到更有代表性的样本，或把结论限制在“受访的篮球队员”。""",
  r"""A survey asks “How long do you exercise each week?” only after basketball training, then concludes that “all students in the school exercise for a long time”. What is wrong, and what should happen next?

**Solution:** The sample is biased and the conclusion goes beyond the sample. Use a more representative sample, or restrict the conclusion to the basketball players who were asked.""",
  [("还没有问题就先收集一堆无关数据。", "Collecting a pile of unrelated data before there is a question."),
   ("从很小或有偏差的样本推出关于全体的绝对结论。", "Drawing an absolute conclusion about a whole population from a small or biased sample."),
   ("发现方法有问题却不回到计划阶段。", "Spotting a weak method but not returning to the planning stage.")],
  [
    dict(type="mcq", stem_zh="统计循环通常从哪里开始？", stem_en="The statistical cycle usually begins with:",
         answer="a", exp_zh="先提出一个清楚的问题。", exp_en="A clear question.",
         options=opts(("提出清楚的问题", "a clear question"), ("先随意画图再找问题", "drawing a random diagram and inventing a question later"),
                      ("先写出与数据无关的绝对结论", "writing an absolute conclusion with no data"), ("先计算任意一个向量", "calculating a random vector"))),
    dict(type="mcq", stem_zh="只在篮球训练后调查运动时间，却推论全校，主要问题是？",
         stem_en="Asking about exercise time only after basketball training, then speaking for the whole school, is a problem mainly because:",
         answer="c", exp_zh="样本有偏差，结论超出范围。", exp_en="The sample is biased and the conclusion goes too far.",
         options=opts(("运动时间不是数据", "exercise time is not data"), ("饼图角度必须是 $1^\\circ$", "a pie chart must use an angle of $1^\\circ$"),
                      ("样本有偏差", "the sample is biased"), ("平均数不能计算", "a mean cannot be calculated"))),
    dict(type="mcq", stem_zh="发现问卷有诱导性之后，应该？", stem_en="After you find that a questionnaire is leading, you should:",
         answer="b", exp_zh="回到计划阶段，改进问题或重新收集。", exp_en="Return to the planning stage, improve the questions or collect again.",
         options=opts(("忽略问题，直接下更强的结论", "ignore it and state a stronger conclusion"),
                      ("回到计划并改进方法", "return to planning and improve the method"),
                      ("把所有数据删除且不再学习统计", "delete all data and never study statistics again"),
                      ("把分类数据全部改成向量", "turn all categorical data into vectors"))),
    dict(type="short", stem_zh="写出统计循环中的四个主要阶段（简要即可）。", stem_en="List the main stages of the statistical cycle (briefly).",
         answer="question, collect, present, conclude",
         accepted=["question, collect, present, conclude", "pose, collect, organise, interpret",
                   "提出问题、收集、整理呈现、解释结论", "问题、收集、呈现、结论"],
         answer_zh="提出问题、设计收集、整理呈现、解释结论（并可改进后再循环）。",
         answer_en="Pose a question, plan and collect, organise and present, interpret and conclude (then improve and repeat if needed).",
         exp_zh="不同教材用词略有差别，阶段意思对即可。", exp_en="Wording varies; the idea of the stages matters."),
    dict(type="mcq", stem_zh="好的统计结论应当？", stem_en="A good statistical conclusion should:",
         answer="d", exp_zh="与问题对应，不超出样本，并指出局限。", exp_en="Match the question, stay within the sample, and state limitations.",
         options=opts(("完全不看数据", "ignore the data completely"), ("推广到任何未调查的群体且不说明", "extend to any unsurveyed group with no comment"),
                      ("只夸图表好看", "only praise how attractive the chart looks"), ("回答原问题，并承认局限", "answer the original question and admit limitations"))),
    dict(type="mcq", stem_zh="问题“八年级学生通常花多少分钟做数学作业？”比“学生怎么样？”更好，是因为？",
         stem_en="“How many minutes do Year 8 students typically spend on mathematics homework?” is better than “How are students?” mainly because:",
         answer="a", exp_zh="问题具体，能决定收集什么数据。", exp_en="It is specific enough to decide what data to collect.",
         options=opts(("它更具体，能决定收集什么", "it is more specific, so you can decide what to collect"),
                      ("它不能被调查", "it cannot be investigated"),
                      ("它不需要单位", "it needs no units"),
                      ("它已经是最终结论", "it is already a final conclusion"))),
  ])

def X(section, **q):
    return (section, q)

def block(rows):
    return add_extra_questions(C, rows)

PR81 = block([
    X("mathematics-8-1-1", type="numeric", id="q-ma-81-pr01", stem_zh="把 $2\\,460$ 四舍五入到最近的 $100$。", stem_en="Round $2\\,460$ to the nearest $100$.", answer=2500, exp_zh="十位是 $6$，入上去得 $2\\,500$。", exp_en="Tens digit $6$, so $2\\,500$.", tolerance=0),
    X("mathematics-8-1-1", type="numeric", id="q-ma-81-pr02", stem_zh="把 $9.15$ 四舍五入到一位小数。", stem_en="Round $9.15$ to one decimal place.", answer=9.2, exp_zh="百分位是 $5$，得 $9.2$。", exp_en="Hundredths digit $5$, so $9.2$.", tolerance=0.01),
    X("mathematics-8-1-2", type="numeric", id="q-ma-81-pr03", stem_zh="计算 $5^4\\div 5^2$。", stem_en="Evaluate $5^4\\div 5^2$.", answer=25, exp_zh="$5^2=25$。", exp_en="$5^2=25$.", tolerance=0),
    X("mathematics-8-1-2", type="numeric", id="q-ma-81-pr04", stem_zh="求 $12$ 与 $18$ 的 HCF。", stem_en="HCF of $12$ and $18$?", answer=6, exp_zh="HCF $=6$。", exp_en="HCF $=6$.", tolerance=0),
    X("mathematics-8-1-2", type="numeric", id="q-ma-81-pr05", stem_zh="求 $12$ 与 $18$ 的 LCM。", stem_en="LCM of $12$ and $18$?", answer=36, exp_zh="LCM $=36$。", exp_en="LCM $=36$.", tolerance=0),
    X("mathematics-8-1-3", type="numeric", id="q-ma-81-pr06", stem_zh="计算 $8-2\\times 3$。", stem_en="Evaluate $8-2\\times 3$.", answer=2, exp_zh="先乘：$8-6=2$。", exp_en="Multiply first: $8-6=2$.", tolerance=0),
    X("mathematics-8-1-3", type="numeric", id="q-ma-81-pr07", stem_zh="计算 $0.6\\times 0.4$。", stem_en="Evaluate $0.6\\times 0.4$.", answer=0.24, exp_zh="$0.24$。", exp_en="$0.24$.", tolerance=0.001),
    X("mathematics-8-1-3", type="numeric", id="q-ma-81-pr08", stem_zh="计算 $3.6\\div 0.12$。", stem_en="Evaluate $3.6\\div 0.12$.", answer=30, exp_zh="$360\\div 12=30$。", exp_en="$360\\div 12=30$.", tolerance=0),
])
PA81 = block([
    X("mathematics-8-1-1", type="numeric", id="q-ma-81-pa01", stem_zh="$5\\,203.8$ 中数字 $8$ 表示多少？", stem_en="In $5\\,203.8$, what value does the digit $8$ represent?", answer=0.8, exp_zh="十分位：$0.8$。", exp_en="Tenths: $0.8$.", tolerance=0.01),
    X("mathematics-8-1-1", type="numeric", id="q-ma-81-pa02", stem_zh="把 $14\\,500$ 四舍五入到最近的 $1\\,000$。", stem_en="Round $14\\,500$ to the nearest $1\\,000$.", answer=15000, exp_zh="得 $15\\,000$。", exp_en="Gives $15\\,000$.", tolerance=0),
    X("mathematics-8-1-2", type="numeric", id="q-ma-81-pa03", stem_zh="计算 $2^3\\times 2^2$。", stem_en="Evaluate $2^3\\times 2^2$.", answer=32, exp_zh="$2^5=32$。", exp_en="$2^5=32$.", tolerance=0),
    X("mathematics-8-1-2", type="numeric", id="q-ma-81-pa04", stem_zh="$4^0$ 等于多少？", stem_en="What is $4^0$?", answer=1, exp_zh="等于 $1$。", exp_en="Equals $1$.", tolerance=0),
    X("mathematics-8-1-2", type="numeric", id="q-ma-81-pa05", stem_zh="求 $20$ 与 $30$ 的 HCF。", stem_en="HCF of $20$ and $30$?", answer=10, exp_zh="HCF $=10$。", exp_en="HCF $=10$.", tolerance=0),
    X("mathematics-8-1-2", type="numeric", id="q-ma-81-pa06", stem_zh="求 $20$ 与 $30$ 的 LCM。", stem_en="LCM of $20$ and $30$?", answer=60, exp_zh="LCM $=60$。", exp_en="LCM $=60$.", tolerance=0),
    X("mathematics-8-1-3", type="numeric", id="q-ma-81-pa07", stem_zh="计算 $18\\div 3+2^2$。", stem_en="Evaluate $18\\div 3+2^2$.", answer=10, exp_zh="$6+4=10$。", exp_en="$6+4=10$.", tolerance=0),
    X("mathematics-8-1-3", type="numeric", id="q-ma-81-pa08", stem_zh="计算 $2.5+0.75$。", stem_en="Evaluate $2.5+0.75$.", answer=3.25, exp_zh="$3.25$。", exp_en="$3.25$.", tolerance=0.001),
    X("mathematics-8-1-3", type="numeric", id="q-ma-81-pa09", stem_zh="计算 $1.5\\times 0.2$。", stem_en="Evaluate $1.5\\times 0.2$.", answer=0.3, exp_zh="$0.3$。", exp_en="$0.3$.", tolerance=0.001),
    X("mathematics-8-1-1", type="mcq", id="q-ma-81-pa10", stem_zh="把 $6.249$ 四舍五入到两位小数？", stem_en="Round $6.249$ to two decimal places.", answer="a", exp_zh="得 $6.25$。", exp_en="Gives $6.25$.", options=opts(("$6.25$", "$6.25$"), ("$6.24$", "$6.24$"), ("$6.20$", "$6.20$"), ("$6.30$", "$6.30$"))),
    X("mathematics-8-1-3", type="mcq", id="q-ma-81-pa11", stem_zh="计算 $10-6\\div 2$？", stem_en="What is $10-6\\div 2$?", answer="c", exp_zh="$10-3=7$。", exp_en="$10-3=7$.", options=opts(("$2$", "$2$"), ("$8$", "$8$"), ("$7$", "$7$"), ("$4$", "$4$"))),
])

PR82 = block([
    X("mathematics-8-2-1", type="short", id="q-ma-82-pr01", stem_zh="化简 $7x-2x+4$。", stem_en="Simplify $7x-2x+4$.", answer="5x+4", accepted=["5x+4", "5x + 4", "4+5x"], answer_zh="$5x+4$", answer_en="$5x+4$", exp_zh="合并同类项。", exp_en="Collect like terms."),
    X("mathematics-8-2-1", type="short", id="q-ma-82-pr02", stem_zh="展开 $3(y-4)$。", stem_en="Expand $3(y-4)$.", answer="3y-12", accepted=["3y-12", "3y - 12"], answer_zh="$3y-12$", answer_en="$3y-12$", exp_zh="分配律。", exp_en="Distributive law."),
    X("mathematics-8-2-1", type="numeric", id="q-ma-82-pr03", stem_zh="当 $x=5$ 时，$4x-3$ 等于多少？", stem_en="If $x=5$, what is $4x-3$?", answer=17, exp_zh="$20-3=17$。", exp_en="$20-3=17$.", tolerance=0),
    X("mathematics-8-2-1", type="short", id="q-ma-82-pr04", stem_zh="由 $C=2\\pi r$ 用 $C$ 表示 $r$（可用 $r=C/(2\\pi)$）。", stem_en="Make $r$ the subject of $C=2\\pi r$.", answer="r=C/(2pi)", accepted=["r=C/(2pi)", "r=C/(2π)", "r=C/2π", "r=C/(2\\pi)", "r＝C/(2π)"], answer_zh="$r=C/(2\\pi)$", answer_en="$r=C/(2\\pi)$", exp_zh="两边同除以 $2\\pi$。", exp_en="Divide both sides by $2\\pi$."),
    X("mathematics-8-2-2", type="numeric", id="q-ma-82-pr05", stem_zh="解 $x+9=15$。$x=$？", stem_en="Solve $x+9=15$. $x=$", answer=6, exp_zh="$x=6$。", exp_en="$x=6$.", tolerance=0),
    X("mathematics-8-2-2", type="numeric", id="q-ma-82-pr06", stem_zh="解 $5x=45$。$x=$？", stem_en="Solve $5x=45$. $x=$", answer=9, exp_zh="$x=9$。", exp_en="$x=9$.", tolerance=0),
    X("mathematics-8-2-2", type="mcq", id="q-ma-82-pr07", stem_zh="$x-3>5$ 的解是？", stem_en="The solution of $x-3>5$ is:", answer="b", exp_zh="$x>8$。", exp_en="$x>8$.", options=opts(("$x>5$", "$x>5$"), ("$x>8$", "$x>8$"), ("$x=8$", "$x=8$"), ("$x<8$", "$x<8$"))),
    X("mathematics-8-2-2", type="mcq", id="q-ma-82-pr08", stem_zh="$-x<4$ 的解是？", stem_en="The solution of $-x<4$ is:", answer="a", exp_zh="两边乘 $-1$ 反向，得 $x>-4$。", exp_en="Multiply by $-1$ and reverse: $x>-4$.", options=opts(("$x>-4$", "$x>-4$"), ("$x<-4$", "$x<-4$"), ("$x>4$", "$x>4$"), ("$x=4$", "$x=4$"))),
])
PA82 = block([
    X("mathematics-8-2-1", type="short", id="q-ma-82-pa01", stem_zh="化简 $2(a+3)+a$。", stem_en="Simplify $2(a+3)+a$.", answer="3a+6", accepted=["3a+6", "3a + 6", "3(a+2)"], answer_zh="$3a+6$", answer_en="$3a+6$", exp_zh="$2a+6+a=3a+6$。", exp_en="$2a+6+a=3a+6$."),
    X("mathematics-8-2-1", type="numeric", id="q-ma-82-pa02", stem_zh="当 $t=-3$ 时，$t^2+1$ 等于多少？", stem_en="If $t=-3$, what is $t^2+1$?", answer=10, exp_zh="$9+1=10$。", exp_en="$9+1=10$.", tolerance=0),
    X("mathematics-8-2-1", type="short", id="q-ma-82-pa03", stem_zh="由 $P=4s$ 用 $P$ 表示 $s$。", stem_en="Make $s$ the subject of $P=4s$.", answer="s=P/4", accepted=["s=P/4", "s = P/4"], answer_zh="$s=P/4$", answer_en="$s=P/4$", exp_zh="两边除以 $4$。", exp_en="Divide by $4$."),
    X("mathematics-8-2-2", type="numeric", id="q-ma-82-pa04", stem_zh="解 $3x+4=19$。$x=$？", stem_en="Solve $3x+4=19$. $x=$", answer=5, exp_zh="$3x=15$，$x=5$。", exp_en="$3x=15$, $x=5$.", tolerance=0),
    X("mathematics-8-2-2", type="numeric", id="q-ma-82-pa05", stem_zh="解 $2(x+3)=14$。$x=$？", stem_en="Solve $2(x+3)=14$. $x=$", answer=4, exp_zh="$x+3=7$，$x=4$。", exp_en="$x+3=7$, $x=4$.", tolerance=0),
    X("mathematics-8-2-2", type="numeric", id="q-ma-82-pa06", stem_zh="解 $7x-2=3x+10$。$x=$？", stem_en="Solve $7x-2=3x+10$. $x=$", answer=3, exp_zh="$4x=12$，$x=3$。", exp_en="$4x=12$, $x=3$.", tolerance=0),
    X("mathematics-8-2-2", type="mcq", id="q-ma-82-pa07", stem_zh="$3x\\le 12$ 的解是？", stem_en="The solution of $3x\\le 12$ is:", answer="c", exp_zh="$x\\le 4$。", exp_en="$x\\le 4$.", options=opts(("$x\\ge 4$", "$x\\ge 4$"), ("$x=12$", "$x=12$"), ("$x\\le 4$", "$x\\le 4$"), ("$x>4$", "$x>4$"))),
    X("mathematics-8-2-2", type="mcq", id="q-ma-82-pa08", stem_zh="$1-x>3$ 的解是？", stem_en="The solution of $1-x>3$ is:", answer="b", exp_zh="$-x>2$，$x<-2$。", exp_en="$-x>2$, so $x<-2$.", options=opts(("$x>-2$", "$x>-2$"), ("$x<-2$", "$x<-2$"), ("$x>2$", "$x>2$"), ("$x= -1$", "$x=-1$"))),
    X("mathematics-8-2-1", type="mcq", id="q-ma-82-pa09", stem_zh="$3x+4$ 与 $3(x+4)$ 是否恒等？", stem_en="Are $3x+4$ and $3(x+4)$ identically equal?", answer="d", exp_zh="后者是 $3x+12$，不相等。", exp_en="The second is $3x+12$, not the same.", options=opts(("是，永远相同", "yes, always the same"), ("是，因为都有 $3$ 和 $4$", "yes, because both contain $3$ and $4$"), ("无法比较", "cannot be compared"), ("不是，$3(x+4)=3x+12$", "no: $3(x+4)=3x+12$"))),
    X("mathematics-8-2-1", type="numeric", id="q-ma-82-pa10", stem_zh="当 $x=10$ 时，$\\dfrac{x}{2}+1$ 等于多少？", stem_en="If $x=10$, what is $\\dfrac{x}{2}+1$?", answer=6, exp_zh="$5+1=6$。", exp_en="$5+1=6$.", tolerance=0),
    X("mathematics-8-2-2", type="numeric", id="q-ma-82-pa11", stem_zh="解 $\\dfrac{x}{3}=7$。$x=$？", stem_en="Solve $\\dfrac{x}{3}=7$. $x=$", answer=21, exp_zh="$x=21$。", exp_en="$x=21$.", tolerance=0),
])

PR83 = block([
    X("mathematics-8-3-1", type="numeric", id="q-ma-83-pr01", stem_zh="四边形三角为 $70^\\circ$、$95^\\circ$、$100^\\circ$。第四角多少度？", stem_en="Three angles of a quadrilateral are $70^\\circ$, $95^\\circ$, $100^\\circ$. Fourth angle in degrees?", answer=95, exp_zh="$360-265=95$。", exp_en="$360-265=95$.", tolerance=0),
    X("mathematics-8-3-1", type="numeric", id="q-ma-83-pr02", stem_zh="正五边形每个内角多少度？", stem_en="Each interior angle of a regular pentagon, in degrees?", answer=108, exp_zh="$540\\div 5=108$。", exp_en="$540\\div 5=108$.", tolerance=0),
    X("mathematics-8-3-2", type="numeric", id="q-ma-83-pr03", stem_zh="边长 $6\\ \\mathrm{cm}$ 的正方形，面积多少平方厘米？", stem_en="Area of a square of side $6\\ \\mathrm{cm}$, in square centimetres?", answer=36, exp_zh="$6^2=36$。", exp_en="$6^2=36$.", tolerance=0),
    X("mathematics-8-3-2", type="numeric", id="q-ma-83-pr04", stem_zh="直径 $8\\ \\mathrm{cm}$ 的圆周长多少厘米？（$\\pi=3.14$）", stem_en="Circumference of a circle of diameter $8\\ \\mathrm{cm}$? ($\\pi=3.14$)", answer=25.12, exp_zh="$3.14\\times 8=25.12$。", exp_en="$3.14\\times 8=25.12$.", tolerance=0.05),
    X("mathematics-8-3-2", type="numeric", id="q-ma-83-pr05", stem_zh="底 $8$、高 $5$ 的平行四边形面积？", stem_en="Area of a parallelogram with base $8$ and height $5$?", answer=40, exp_zh="$8\\times 5=40$。", exp_en="$8\\times 5=40$.", tolerance=0),
    X("mathematics-8-3-3", type="numeric", id="q-ma-83-pr06", stem_zh="正方体棱长 $4\\ \\mathrm{cm}$，体积多少立方厘米？", stem_en="Volume of a cube of edge $4\\ \\mathrm{cm}$, in cubic centimetres?", answer=64, exp_zh="$4^3=64$。", exp_en="$4^3=64$.", tolerance=0),
    X("mathematics-8-3-3", type="numeric", id="q-ma-83-pr07", stem_zh="该正方体的表面积多少平方厘米？", stem_en="Total surface area of that cube, in square centimetres?", answer=96, exp_zh="$6\\times 16=96$。", exp_en="$6\\times 16=96$.", tolerance=0),
    X("mathematics-8-3-3", type="numeric", id="q-ma-83-pr08", stem_zh="底面积 $20$、高 $5$ 的棱柱体积？", stem_en="Volume of a prism with cross-section $20$ and length $5$?", answer=100, exp_zh="$20\\times 5=100$。", exp_en="$20\\times 5=100$.", tolerance=0),
])
PA83 = block([
    X("mathematics-8-3-1", type="numeric", id="q-ma-83-pa01", stem_zh="六边形内角和多少度？", stem_en="Sum of interior angles of a hexagon, in degrees?", answer=720, exp_zh="$(6-2)\\times 180=720$。", exp_en="$(6-2)\\times 180=720$.", tolerance=0),
    X("mathematics-8-3-1", type="numeric", id="q-ma-83-pa02", stem_zh="正九边形内角和多少度？", stem_en="Sum of interior angles of a regular nonagon, in degrees?", answer=1260, exp_zh="$(9-2)\\times 180=1260$。", exp_en="$(9-2)\\times 180=1260$.", tolerance=0),
    X("mathematics-8-3-2", type="numeric", id="q-ma-83-pa03", stem_zh="半径 $7\\ \\mathrm{cm}$ 的圆面积？（$\\pi=\\dfrac{22}{7}$）", stem_en="Area of a circle of radius $7\\ \\mathrm{cm}$? Use $\\pi=\\dfrac{22}{7}$.", answer=154, exp_zh="$\\dfrac{22}{7}\\times 49=154$。", exp_en="$\\dfrac{22}{7}\\times 49=154$.", tolerance=0),
    X("mathematics-8-3-2", type="numeric", id="q-ma-83-pa04", stem_zh="直角边 $6$ 与 $8$ 的直角三角形面积？", stem_en="Area of a right triangle with legs $6$ and $8$?", answer=24, exp_zh="$\\dfrac{1}{2}\\times 6\\times 8=24$。", exp_en="$\\dfrac{1}{2}\\times 6\\times 8=24$.", tolerance=0),
    X("mathematics-8-3-2", type="numeric", id="q-ma-83-pa05", stem_zh="长 $12$、宽 $5$ 的矩形周长？", stem_en="Perimeter of a $12$ by $5$ rectangle?", answer=34, exp_zh="$2(12+5)=34$。", exp_en="$2(12+5)=34$.", tolerance=0),
    X("mathematics-8-3-3", type="numeric", id="q-ma-83-pa06", stem_zh="长方体 $6\\times 2\\times 3$ 的体积？", stem_en="Volume of a $6\\times 2\\times 3$ cuboid?", answer=36, exp_zh="$36$。", exp_en="$36$.", tolerance=0),
    X("mathematics-8-3-3", type="numeric", id="q-ma-83-pa07", stem_zh="该长方体表面积？", stem_en="Total surface area of that cuboid?", answer=72, exp_zh="$2(12+18+6)=72$。", exp_en="$2(12+18+6)=72$.", tolerance=0),
    X("mathematics-8-3-3", type="numeric", id="q-ma-83-pa08", stem_zh="圆柱半径 $2$、高 $7$，体积？（$\\pi=\\dfrac{22}{7}$）", stem_en="Volume of a cylinder with radius $2$ and height $7$? Use $\\pi=\\dfrac{22}{7}$.", answer=88, exp_zh="$\\dfrac{22}{7}\\times 4\\times 7=88$。", exp_en="$\\dfrac{22}{7}\\times 4\\times 7=88$.", tolerance=0),
    X("mathematics-8-3-1", type="mcq", id="q-ma-83-pa09", stem_zh="长方形一定有？", stem_en="A rectangle always has:", answer="a", exp_zh="四个直角。", exp_en="Four right angles.", options=opts(("四个直角", "four right angles"), ("四边一定都相等", "four equal sides always"), ("只有一条边", "only one side"), ("内角和为 $180^\\circ$", "an angle sum of $180^\\circ$"))),
    X("mathematics-8-3-2", type="mcq", id="q-ma-83-pa10", stem_zh="圆的面积公式是？", stem_en="The area of a circle is:", answer="c", exp_zh="$\\pi r^2$。", exp_en="$\\pi r^2$.", options=opts(("$2\\pi r$", "$2\\pi r$"), ("$\\pi d$", "$\\pi d$"), ("$\\pi r^2$", "$\\pi r^2$"), ("$2r$", "$2r$"))),
    X("mathematics-8-3-3", type="mcq", id="q-ma-83-pa11", stem_zh="圆柱体积公式是？", stem_en="The volume of a cylinder is:", answer="b", exp_zh="$\\pi r^2 h$。", exp_en="$\\pi r^2 h$.", options=opts(("$2\\pi r h$", "$2\\pi r h$"), ("$\\pi r^2 h$", "$\\pi r^2 h$"), ("$2\\pi r$", "$2\\pi r$"), ("$\\pi r^2$", "$\\pi r^2$ only, with no height"))),
])

PR84 = block([
    X("mathematics-8-4-1", type="numeric", id="q-ma-84-pr01", stem_zh="$\\dfrac{2}{5}$ 写成百分数是多少？（只填数字）", stem_en="Write $\\dfrac{2}{5}$ as a percentage (number only).", answer=40, exp_zh="$40\\%$。", exp_en="$40\\%$.", tolerance=0),
    X("mathematics-8-4-1", type="numeric", id="q-ma-84-pr02", stem_zh="$15\\%$ 写成小数是多少？", stem_en="Write $15\\%$ as a decimal.", answer=0.15, exp_zh="$0.15$。", exp_en="$0.15$.", tolerance=0.001),
    X("mathematics-8-4-2", type="short", id="q-ma-84-pr03", stem_zh="$\\dfrac{1}{6}+\\dfrac{1}{3}=$？", stem_en="$\\dfrac{1}{6}+\\dfrac{1}{3}=$", answer="1/2", accepted=["1/2", "3/6", "0.5"], answer_zh="$\\dfrac{1}{2}$", answer_en="$\\dfrac{1}{2}$", exp_zh="$\\dfrac{1}{6}+\\dfrac{2}{6}=\\dfrac{1}{2}$。", exp_en="Equals $\\dfrac{1}{2}$."),
    X("mathematics-8-4-2", type="numeric", id="q-ma-84-pr04", stem_zh="$8\\div\\dfrac{1}{4}=$？", stem_en="$8\\div\\dfrac{1}{4}=$", answer=32, exp_zh="$8\\times 4=32$。", exp_en="$8\\times 4=32$.", tolerance=0),
    X("mathematics-8-4-3", type="numeric", id="q-ma-84-pr05", stem_zh="从 $\$40$ 涨到 $\$50$，百分数增加是多少？", stem_en="Percentage increase from $\$40$ to $\$50$ (number only)?", answer=25, exp_zh="$10/40=25\\%$。", exp_en="$10/40=25\\%$.", tolerance=0),
    X("mathematics-8-4-3", type="short", id="q-ma-84-pr06", stem_zh="化简 $16:24$。", stem_en="Simplify $16:24$.", answer="2:3", accepted=["2:3", "2 : 3"], answer_zh="$2:3$", answer_en="$2:3$", exp_zh="同除以 $8$。", exp_en="Divide by $8$."),
    X("mathematics-8-4-3", type="numeric", id="q-ma-84-pr07", stem_zh="按 $1:3$ 分配 $\$80$，较小一份是多少？", stem_en="Share $\$80$ in the ratio $1:3$. Smaller share?", answer=20, exp_zh="一份 $\$20$。", exp_en="One part is $\$20$.", tolerance=0),
    X("mathematics-8-4-3", type="numeric", id="q-ma-84-pr08", stem_zh="$4$ 支笔 $\$12$。$7$ 支同样的笔多少钱？", stem_en="$4$ pens cost $\$12$. Cost of $7$ identical pens?", answer=21, exp_zh="每支 $\$3$，$7$ 支 $\$21$。", exp_en="$3$ each, so $21$.", tolerance=0),
])
PA84 = block([
    X("mathematics-8-4-1", type="mcq", id="q-ma-84-pa01", stem_zh="$\\dfrac{4}{5}$、$0.7$、$90\\%$ 中最大的是？", stem_en="Largest of $\\dfrac{4}{5}$, $0.7$, $90\\%$?", answer="c", exp_zh="$80\\%$、$70\\%$、$90\\%$。", exp_en="$80\\%$, $70\\%$, $90\\%$.", options=opts(("$\\dfrac{4}{5}$", "$\\dfrac{4}{5}$"), ("$0.7$", "$0.7$"), ("$90\\%$", "$90\\%$"), ("一样大", "equal"))),
    X("mathematics-8-4-1", type="numeric", id="q-ma-84-pa02", stem_zh="$0.03$ 写成百分数是多少？（只填数字）", stem_en="Write $0.03$ as a percentage (number only).", answer=3, exp_zh="$3\\%$。", exp_en="$3\\%$.", tolerance=0),
    X("mathematics-8-4-2", type="short", id="q-ma-84-pa03", stem_zh="$\\dfrac{5}{8}-\\dfrac{1}{4}=$？", stem_en="$\\dfrac{5}{8}-\\dfrac{1}{4}=$", answer="3/8", accepted=["3/8", "0.375"], answer_zh="$\\dfrac{3}{8}$", answer_en="$\\dfrac{3}{8}$", exp_zh="$\\dfrac{5}{8}-\\dfrac{2}{8}=\\dfrac{3}{8}$。", exp_en="$\\dfrac{3}{8}$."),
    X("mathematics-8-4-2", type="short", id="q-ma-84-pa04", stem_zh="$\\dfrac{3}{5}\\times\\dfrac{10}{9}=$？（最简）", stem_en="Simplify $\\dfrac{3}{5}\\times\\dfrac{10}{9}$.", answer="2/3", accepted=["2/3"], answer_zh="$\\dfrac{2}{3}$", answer_en="$\\dfrac{2}{3}$", exp_zh="约分后得 $\\dfrac{2}{3}$。", exp_en="Cancels to $\\dfrac{2}{3}$."),
    X("mathematics-8-4-2", type="short", id="q-ma-84-pa05", stem_zh="$\\dfrac{2}{3}\\div\\dfrac{4}{9}=$？", stem_en="$\\dfrac{2}{3}\\div\\dfrac{4}{9}=$", answer="3/2", accepted=["3/2", "1.5", "1 1/2"], answer_zh="$\\dfrac{3}{2}$", answer_en="$\\dfrac{3}{2}$", exp_zh="$\\dfrac{2}{3}\\times\\dfrac{9}{4}=\\dfrac{3}{2}$。", exp_en="$\\dfrac{3}{2}$."),
    X("mathematics-8-4-3", type="numeric", id="q-ma-84-pa06", stem_zh="$\$120$ 减少 $25\\%$ 后是多少？", stem_en="What is $\$120$ after a $25\\%$ decrease?", answer=90, exp_zh="$120\\times 0.75=90$。", exp_en="$120\\times 0.75=90$.", tolerance=0),
    X("mathematics-8-4-3", type="numeric", id="q-ma-84-pa07", stem_zh="从 $80$ 降到 $60$，百分数减少是多少？", stem_en="Percentage decrease from $80$ to $60$ (number only)?", answer=25, exp_zh="$20/80=25\\%$。", exp_en="$20/80=25\\%$.", tolerance=0),
    X("mathematics-8-4-3", type="numeric", id="q-ma-84-pa08", stem_zh="按 $3:5$ 分配 $\$56$，较大一份是多少？", stem_en="Share $\$56$ in the ratio $3:5$. Larger share?", answer=35, exp_zh="一份 $\$7$，$5$ 份 $\$35$。", exp_en="Each part $\$7$, so $5$ parts $\$35$.", tolerance=0),
    X("mathematics-8-4-1", type="mcq", id="q-ma-84-pa09", stem_zh="$\\dfrac{1}{4}$ 等于？", stem_en="$\\dfrac{1}{4}$ equals:", answer="b", exp_zh="$0.25=25\\%$。", exp_en="$0.25=25\\%$.", options=opts(("$0.4$", "$0.4$"), ("$0.25$", "$0.25$"), ("$2.5$", "$2.5$"), ("$0.025$", "$0.025$"))),
    X("mathematics-8-4-3", type="mcq", id="q-ma-84-pa10", stem_zh="正比例意味着？", stem_en="Direct proportion means:", answer="a", exp_zh="一个量变为若干倍，另一个量变为相同的倍数。", exp_en="If one quantity is multiplied by a factor, so is the other.", options=opts(("一个量乘若干倍，另一个量也乘相同倍数", "if one quantity is multiplied by a factor, so is the other"), ("一个量增加，另一个必须减少", "if one increases the other must decrease"), ("比不能化简", "a ratio cannot be simplified"), ("百分数不能超过 $10$", "a percentage cannot exceed $10$"))),
    X("mathematics-8-4-3", type="numeric", id="q-ma-84-pa11", stem_zh="$\$50$ 增加 $10\\%$ 后再减少 $10\\%$，最终是多少？", stem_en="$\$50$ increases by $10\\%$ then decreases by $10\\%$. Final amount?", answer=49.5, exp_zh="$55$ 再减 $10\\%$ 得 $49.5$。", exp_en="$55$ then minus $10\\%$ is $49.5$.", tolerance=0.05),
])

PR85 = block([
    X("mathematics-8-5-1", type="short", id="q-ma-85-pr01", stem_zh="公平骰子掷出 $1$ 的概率？", stem_en="Probability of a $1$ on a fair die?", answer="1/6", accepted=["1/6"], answer_zh="$\\dfrac{1}{6}$", answer_en="$\\dfrac{1}{6}$", exp_zh="六个等可能结果。", exp_en="Six equally likely outcomes."),
    X("mathematics-8-5-1", type="short", id="q-ma-85-pr02", stem_zh="$P(A)=0.85$，$P(\\text{not }A)=$？", stem_en="If $P(A)=0.85$, $P(\\text{not }A)=$", answer="0.15", accepted=["0.15", "15/100", "3/20"], answer_zh="$0.15$", answer_en="$0.15$", exp_zh="$1-0.85=0.15$。", exp_en="$1-0.85=0.15$."),
    X("mathematics-8-5-1", type="short", id="q-ma-85-pr03", stem_zh="公平硬币连续两次都是反面的概率？", stem_en="Probability two fair coins both show tails?", answer="1/4", accepted=["1/4", "0.25"], answer_zh="$\\dfrac{1}{4}$", answer_en="$\\dfrac{1}{4}$", exp_zh="独立事件相乘。", exp_en="Multiply independent probabilities."),
    X("mathematics-8-5-1", type="short", id="q-ma-85-pr04", stem_zh="袋中 $4$ 白 $6$ 黑，取一球为白的概率？", stem_en="Bag: $4$ white, $6$ black. Probability of white?", answer="2/5", accepted=["2/5", "4/10", "0.4"], answer_zh="$\\dfrac{2}{5}$", answer_en="$\\dfrac{2}{5}$", exp_zh="$4/10=2/5$。", exp_en="$4/10=2/5$."),
    X("mathematics-8-5-2", type="numeric", id="q-ma-85-pr05", stem_zh="掷 $200$ 次出现 $35$ 次六点，相对频率（小数）？", stem_en="A six occurs $35$ times in $200$ rolls. Relative frequency as a decimal?", answer=0.175, exp_zh="$35/200=0.175$。", exp_en="$35/200=0.175$.", tolerance=0.005),
    X("mathematics-8-5-2", type="mcq", id="q-ma-85-pr06", stem_zh="相对频率是？", stem_en="Relative frequency is:", answer="b", exp_zh="对概率的实验估计。", exp_en="An experimental estimate of a probability.", options=opts(("理论概率的保证值", "a guaranteed theoretical probability"), ("实验估计", "an experimental estimate"), ("永远等于 $1$", "always equal to $1$"), ("不能使用", "unusable"))),
    X("mathematics-8-5-2", type="mcq", id="q-ma-85-pr07", stem_zh="试验次数很少时，相对频率？", stem_en="With very few trials, relative frequency:", answer="a", exp_zh="可能波动很大。", exp_en="Can fluctuate a lot.", options=opts(("可能波动很大", "can fluctuate a lot"), ("必须等于理论值", "must equal the theoretical value"), ("没有意义且永远为 $0$", "is meaningless and always $0$"), ("等于样本的极差", "equals the range of the sample"))),
    X("mathematics-8-5-1", type="short", id="q-ma-85-pr08", stem_zh="公平骰子掷出小于 $3$ 的概率？", stem_en="Probability of a number less than $3$ on a fair die?", answer="1/3", accepted=["1/3", "2/6"], answer_zh="$\\dfrac{1}{3}$", answer_en="$\\dfrac{1}{3}$", exp_zh="$1$ 或 $2$，共 $2/6$。", exp_en="$1$ or $2$ gives $2/6=1/3$."),
])
PA85 = block([
    X("mathematics-8-5-1", type="short", id="q-ma-85-pa01", stem_zh="公平骰子掷出奇数的概率？", stem_en="Probability of an odd number on a fair die?", answer="1/2", accepted=["1/2", "3/6", "0.5"], answer_zh="$\\dfrac{1}{2}$", answer_en="$\\dfrac{1}{2}$", exp_zh="$1,3,5$。", exp_en="$1,3,5$."),
    X("mathematics-8-5-1", type="short", id="q-ma-85-pa02", stem_zh="公平骰子掷出 $1$ 或 $2$ 或 $3$ 的概率？", stem_en="Probability of a $1$, $2$ or $3$ on a fair die?", answer="1/2", accepted=["1/2", "3/6"], answer_zh="$\\dfrac{1}{2}$", answer_en="$\\dfrac{1}{2}$", exp_zh="互斥相加 $3/6$。", exp_en="Add mutually exclusive outcomes."),
    X("mathematics-8-5-1", type="short", id="q-ma-85-pa03", stem_zh="两枚公平骰子都掷出 $6$ 的概率？", stem_en="Probability that two fair dice both show $6$?", answer="1/36", accepted=["1/36"], answer_zh="$\\dfrac{1}{36}$", answer_en="$\\dfrac{1}{36}$", exp_zh="$\\dfrac{1}{6}\\times\\dfrac{1}{6}$。", exp_en="$\\dfrac{1}{6}\\times\\dfrac{1}{6}$."),
    X("mathematics-8-5-1", type="short", id="q-ma-85-pa04", stem_zh="袋中 $2$ 绿 $3$ 黄，放回摸两次都绿的概率？", stem_en="Bag: $2$ green, $3$ yellow. With replacement, probability both green?", answer="4/25", accepted=["4/25", "0.16"], answer_zh="$\\dfrac{4}{25}$", answer_en="$\\dfrac{4}{25}$", exp_zh="$\\dfrac{2}{5}\\times\\dfrac{2}{5}$。", exp_en="$\\dfrac{2}{5}\\times\\dfrac{2}{5}$."),
    X("mathematics-8-5-2", type="numeric", id="q-ma-85-pa05", stem_zh="投 $250$ 次，某面朝上 $40$ 次，相对频率？", stem_en="An outcome occurs $40$ times in $250$ trials. Relative frequency?", answer=0.16, exp_zh="$40/250=0.16$。", exp_en="$40/250=0.16$.", tolerance=0.005),
    X("mathematics-8-5-2", type="mcq", id="q-ma-85-pa06", stem_zh="理论概率 $1/6$ 的骰子，掷 $6$ 次没有六点，说明？", stem_en="A die with theoretical probability $1/6$ shows no six in $6$ rolls. This:", answer="c", exp_zh="次数少，完全可能，不能立即断定不公平。", exp_en="Is possible with few trials and does not immediately prove unfairness.", options=opts(("一定不公平", "proves it is unfair"), ("理论概率变为 $0$", "makes the theoretical probability $0$"), ("次数少，不能立即断定不公平", "does not immediately prove it is unfair, because there are few trials"), ("相对频率不能计算", "means relative frequency cannot be calculated"))),
    X("mathematics-8-5-1", type="mcq", id="q-ma-85-pa07", stem_zh="互斥事件 $A$ 或 $B$ 的概率是？", stem_en="For mutually exclusive $A$ or $B$, the probability is:", answer="a", exp_zh="相加。", exp_en="The sum.", options=opts(("$P(A)+P(B)$", "$P(A)+P(B)$"), ("$P(A)\\times P(B)$", "$P(A)\\times P(B)$"), ("$P(A)-P(B)$ 一定", "$P(A)-P(B)$ always"), ("$1+P(A)$", "$1+P(A)$"))),
    X("mathematics-8-5-1", type="mcq", id="q-ma-85-pa08", stem_zh="独立事件 $A$ 与 $B$ 同时发生的概率是？", stem_en="For independent $A$ and $B$, $P(A\\text{ and }B)$ is:", answer="b", exp_zh="相乘。", exp_en="The product.", options=opts(("$P(A)+P(B)$", "$P(A)+P(B)$"), ("$P(A)\\times P(B)$", "$P(A)\\times P(B)$"), ("一定是 $1$", "always $1$"), ("一定是 $0$", "always $0$"))),
    X("mathematics-8-5-2", type="mcq", id="q-ma-85-pa09", stem_zh="实验次数增加，相对频率通常？", stem_en="As trials increase, relative frequency usually:", answer="d", exp_zh="更接近理论值。", exp_en="Approaches the theoretical value.", options=opts(("变为负数", "becomes negative"), ("必须等于 $2$", "must equal $2$"), ("不再波动且等于极差", "stops fluctuating and equals the range"), ("更接近理论概率", "gets closer to the theoretical probability"))),
    X("mathematics-8-5-1", type="short", id="q-ma-85-pa10", stem_zh="公平骰子掷出不小于 $5$ 的概率？", stem_en="Probability of at least $5$ on a fair die?", answer="1/3", accepted=["1/3", "2/6"], answer_zh="$\\dfrac{1}{3}$", answer_en="$\\dfrac{1}{3}$", exp_zh="$5$ 或 $6$。", exp_en="$5$ or $6$."),
    X("mathematics-8-5-2", type="short", id="q-ma-85-pa11", stem_zh="写出相对频率公式。", stem_en="Write the relative-frequency formula.", answer="frequency/trials", accepted=["frequency/trials", "times/total", "出现次数/总次数", "某结果次数除以总次数"], answer_zh="出现次数 $/$ 总次数。", answer_en="frequency $/$ number of trials.", exp_zh="这是实验估计。", exp_en="It is an experimental estimate."),
])

PR86 = block([
    X("mathematics-8-6-1", type="numeric", id="q-ma-86-pr01", stem_zh="三角形两角 $40^\\circ$、$70^\\circ$，第三角多少度？", stem_en="Two angles of a triangle are $40^\\circ$ and $70^\\circ$. Third angle?", answer=70, exp_zh="$180-110=70$。", exp_en="$180-110=70$.", tolerance=0),
    X("mathematics-8-6-1", type="numeric", id="q-ma-86-pr02", stem_zh="平角上邻角之一 $125^\\circ$，另一角多少度？", stem_en="One adjacent angle on a straight line is $125^\\circ$. The other?", answer=55, exp_zh="$180-125=55$。", exp_en="$180-125=55$.", tolerance=0),
    X("mathematics-8-6-1", type="short", id="q-ma-86-pr03", stem_zh="方位角 $040^\\circ$ 的反向（三位数）？", stem_en="Reverse of bearing $040^\\circ$ (three figures)?", answer="220", accepted=["220", "220°"], answer_zh="$220^\\circ$", answer_en="$220^\\circ$", exp_zh="$40+180=220$。", exp_en="$40+180=220$."),
    X("mathematics-8-6-1", type="mcq", id="q-ma-86-pr04", stem_zh="方位角从哪一边、朝哪个方向量？", stem_en="A bearing is measured:", answer="a", exp_zh="从正北起顺时针。", exp_en="Clockwise from north.", options=opts(("从正北起顺时针", "clockwise from north"), ("从正东起逆时针", "anticlockwise from east"), ("从正南起", "from south"), ("任意方向", "in any direction"))),
    X("mathematics-8-6-2", type="short", id="q-ma-86-pr05", stem_zh="$(-2,4)$ 与 $(6,0)$ 的中点？", stem_en="Midpoint of $(-2,4)$ and $(6,0)$?", answer="(2,2)", accepted=["(2,2)", "(2, 2)"], answer_zh="$(2,2)$", answer_en="$(2,2)$", exp_zh="平均得 $(2,2)$。", exp_en="The averages are $(2,2)$."),
    X("mathematics-8-6-2", type="numeric", id="q-ma-86-pr06", stem_zh="长 $16\\ \\mathrm{cm}$ 的线段，中点到一端多少厘米？", stem_en="A segment is $16\\ \\mathrm{cm}$. Distance from one end to the midpoint?", answer=8, exp_zh="$8$。", exp_en="$8$.", tolerance=0),
    X("mathematics-8-6-2", type="mcq", id="q-ma-86-pr07", stem_zh="垂直平分线上的点到两端？", stem_en="A point on the perpendicular bisector is:", answer="b", exp_zh="等距。", exp_en="Equidistant from the endpoints.", options=opts(("只靠近一个端点", "closer to one endpoint only"), ("到两端等距", "equidistant from the endpoints"), ("一定在线段上", "must lie on the segment"), ("距离之差为 $180$", "has distances differing by $180$"))),
    X("mathematics-8-6-1", type="mcq", id="q-ma-86-pr08", stem_zh="平行线的内错角？", stem_en="Alternate angles with parallel lines are:", answer="c", exp_zh="相等。", exp_en="Equal.", options=opts(("相加为 $90^\\circ$", "supplementary at $90^\\circ$"), ("一定互余", "complementary"), ("相等", "equal"), ("无法确定", "unknown"))),
])
PA86 = block([
    X("mathematics-8-6-1", type="numeric", id="q-ma-86-pa01", stem_zh="周角是多少度？", stem_en="A full turn is how many degrees?", answer=360, exp_zh="$360$。", exp_en="$360$.", tolerance=0),
    X("mathematics-8-6-1", type="numeric", id="q-ma-86-pa02", stem_zh="与 $250^\\circ$ 方位角反向的三位数方位角是多少？（填数字）", stem_en="Reverse of bearing $250^\\circ$ (three-figure number only)?", answer=70, exp_zh="$250-180=70$，写成 $070^\\circ$。填 $70$ 或理解为 $070$。", exp_en="$250-180=70$, written $070^\\circ$.", tolerance=0),
    X("mathematics-8-6-1", type="short", id="q-ma-86-pa03", stem_zh="把方位角 $70^\\circ$ 写成三位数形式。", stem_en="Write the bearing $70^\\circ$ in three figures.", answer="070", accepted=["070", "070°"], answer_zh="$070^\\circ$", answer_en="$070^\\circ$", exp_zh="不足三位前面补 $0$。", exp_en="Pad with a leading zero."),
    X("mathematics-8-6-1", type="mcq", id="q-ma-86-pa04", stem_zh="平行线的同旁内角？", stem_en="Co-interior angles with parallel lines:", answer="a", exp_zh="互补。", exp_en="Add to $180^\\circ$.", options=opts(("相加为 $180^\\circ$", "add to $180^\\circ$"), ("相等", "are equal"), ("相加为 $90^\\circ$", "add to $90^\\circ$"), ("相加为 $360^\\circ$", "add to $360^\\circ$"))),
    X("mathematics-8-6-2", type="short", id="q-ma-86-pa05", stem_zh="$(1,-5)$ 与 $(7,3)$ 的中点？", stem_en="Midpoint of $(1,-5)$ and $(7,3)$?", answer="(4,-1)", accepted=["(4,-1)", "(4, -1)"], answer_zh="$(4,-1)$", answer_en="$(4,-1)$", exp_zh="平均得 $(4,-1)$。", exp_en="Averages give $(4,-1)$."),
    X("mathematics-8-6-2", type="mcq", id="q-ma-86-pa06", stem_zh="角平分线上的点到两边的垂直距离？", stem_en="A point on an angle bisector is:", answer="d", exp_zh="相等。", exp_en="Equidistant from the arms.", options=opts(("一定不等", "never equal"), ("只能是顶点", "only the vertex"), ("没有意义", "meaningless"), ("到两边等距", "equidistant from the two arms"))),
    X("mathematics-8-6-2", type="mcq", id="q-ma-86-pa07", stem_zh="作垂直平分线时，圆规半径应？", stem_en="For a perpendicular bisector, the compass radius should be:", answer="b", exp_zh="大于一半。", exp_en="Greater than half the segment.", options=opts(("小于一半", "less than half"), ("大于一半", "greater than half"), ("必须为零", "zero"), ("必须等于整段", "equal to the whole segment only"))),
    X("mathematics-8-6-1", type="numeric", id="q-ma-86-pa08", stem_zh="同位角之一为 $110^\\circ$，另一同位角多少度（平行线）？", stem_en="One corresponding angle is $110^\\circ$ (parallel lines). The other, in degrees?", answer=110, exp_zh="同位角相等。", exp_en="Corresponding angles are equal.", tolerance=0),
    X("mathematics-8-6-1", type="numeric", id="q-ma-86-pa09", stem_zh="同旁内角之一为 $110^\\circ$，另一个多少度（平行线）？", stem_en="One co-interior angle is $110^\\circ$ (parallel lines). The other?", answer=70, exp_zh="$180-110=70$。", exp_en="$180-110=70$.", tolerance=0),
    X("mathematics-8-6-1", type="mcq", id="q-ma-86-pa10", stem_zh="三角形内角和是？", stem_en="The angle sum of a triangle is:", answer="c", exp_zh="$180^\\circ$。", exp_en="$180^\\circ$.", options=opts(("$90^\\circ$", "$90^\\circ$"), ("$360^\\circ$", "$360^\\circ$"), ("$180^\\circ$", "$180^\\circ$"), ("$270^\\circ$", "$270^\\circ$"))),
    X("mathematics-8-6-2", type="mcq", id="q-ma-86-pa11", stem_zh="中点把线段分成？", stem_en="The midpoint divides a segment into:", answer="a", exp_zh="两条相等的部分。", exp_en="Two equal parts.", options=opts(("两条相等的部分", "two equal parts"), ("三条部分", "three parts"), ("比例一定是 $1:2$", "the ratio $1:2$ only"), ("无法确定的部分", "unknown parts"))),
])

PR87 = block([
    X("mathematics-8-7-1", type="short", id="q-ma-87-pr01", stem_zh="$2,6,10,14,\\ldots$ 的第 $n$ 项？", stem_en="$n$th term of $2,6,10,14,\\ldots$?", answer="4n-2", accepted=["4n-2", "4n - 2"], answer_zh="$4n-2$", answer_en="$4n-2$", exp_zh="公差 $4$，首项 $2$。", exp_en="Difference $4$, first term $2$."),
    X("mathematics-8-7-1", type="numeric", id="q-ma-87-pr02", stem_zh="该数列第 $8$ 项？", stem_en="The $8$th term of that sequence?", answer=30, exp_zh="$4\\times 8-2=30$。", exp_en="$4\\times 8-2=30$.", tolerance=0),
    X("mathematics-8-7-1", type="numeric", id="q-ma-87-pr03", stem_zh="$f(x)=5x-4$，$f(3)=$？", stem_en="If $f(x)=5x-4$, $f(3)=$", answer=11, exp_zh="$15-4=11$。", exp_en="$15-4=11$.", tolerance=0),
    X("mathematics-8-7-2", type="numeric", id="q-ma-87-pr04", stem_zh="$y=-3x+7$ 的斜率？", stem_en="Gradient of $y=-3x+7$?", answer=-3, exp_zh="$m=-3$。", exp_en="$m=-3$.", tolerance=0),
    X("mathematics-8-7-2", type="numeric", id="q-ma-87-pr05", stem_zh="$y=-3x+7$ 的 $y$ 截距？", stem_en="$y$-intercept of $y=-3x+7$?", answer=7, exp_zh="$c=7$。", exp_en="$c=7$.", tolerance=0),
    X("mathematics-8-7-2", type="numeric", id="q-ma-87-pr06", stem_zh="过 $(0,1)$ 和 $(2,7)$ 的斜率？", stem_en="Gradient through $(0,1)$ and $(2,7)$?", answer=3, exp_zh="$(7-1)/(2-0)=3$。", exp_en="$(7-1)/(2-0)=3$.", tolerance=0),
    X("mathematics-8-7-2", type="mcq", id="q-ma-87-pr07", stem_zh="$y=-x$ 向右？", stem_en="As $x$ increases, $y=-x$:", answer="b", exp_zh="下降。", exp_en="Falls.", options=opts(("上升", "rises"), ("下降", "falls"), ("水平", "is horizontal"), ("竖直", "is vertical"))),
    X("mathematics-8-7-1", type="mcq", id="q-ma-87-pr08", stem_zh="函数的一个输入对应？", stem_en="A function gives, for one input:", answer="a", exp_zh="唯一输出。", exp_en="Exactly one output.", options=opts(("唯一输出", "exactly one output"), ("必须两个输出", "two outputs always"), ("不能有输出", "no output"), ("无限个互不相同的输出", "infinitely many different outputs always"))),
])
PA87 = block([
    X("mathematics-8-7-1", type="short", id="q-ma-87-pa01", stem_zh="$9,6,3,0,\\ldots$ 的第 $n$ 项？", stem_en="$n$th term of $9,6,3,0,\\ldots$?", answer="12-3n", accepted=["12-3n", "-3n+12", "12 - 3n"], answer_zh="$12-3n$", answer_en="$12-3n$", exp_zh="公差 $-3$。", exp_en="Difference $-3$."),
    X("mathematics-8-7-1", type="numeric", id="q-ma-87-pa02", stem_zh="$g(x)=10-2x$，$g(4)=$？", stem_en="If $g(x)=10-2x$, $g(4)=$", answer=2, exp_zh="$10-8=2$。", exp_en="$10-8=2$.", tolerance=0),
    X("mathematics-8-7-2", type="numeric", id="q-ma-87-pa03", stem_zh="$y=\\dfrac{2}{3}x-5$ 的 $y$ 截距？", stem_en="$y$-intercept of $y=\\dfrac{2}{3}x-5$?", answer=-5, exp_zh="$c=-5$。", exp_en="$c=-5$.", tolerance=0),
    X("mathematics-8-7-2", type="mcq", id="q-ma-87-pa04", stem_zh="该直线的斜率是？", stem_en="The gradient of that line is:", answer="c", exp_zh="$\\dfrac{2}{3}$。", exp_en="$\\dfrac{2}{3}$.", options=opts(("$-5$", "$-5$"), ("$0$", "$0$"), ("$\\dfrac{2}{3}$", "$\\dfrac{2}{3}$"), ("$3$", "$3$"))),
    X("mathematics-8-7-2", type="numeric", id="q-ma-87-pa05", stem_zh="过 $(2,5)$ 和 $(6,5)$ 的斜率？", stem_en="Gradient through $(2,5)$ and $(6,5)$?", answer=0, exp_zh="水平线，$m=0$。", exp_en="Horizontal, so $m=0$.", tolerance=0),
    X("mathematics-8-7-2", type="mcq", id="q-ma-87-pa06", stem_zh="$x=-1$ 是？", stem_en="The line $x=-1$ is:", answer="a", exp_zh="竖直线。", exp_en="Vertical.", options=opts(("竖直线", "vertical"), ("水平线", "horizontal"), ("斜率 $-1$ 的斜线", "a slanted line of gradient $-1$"), ("$y$ 截距为 $-1$", "a line with $y$-intercept $-1$"))),
    X("mathematics-8-7-1", type="numeric", id="q-ma-87-pa07", stem_zh="$1,5,9,13,\\ldots$ 的第 $20$ 项？", stem_en="The $20$th term of $1,5,9,13,\\ldots$?", answer=77, exp_zh="$4n-3$，当 $n=20$ 时为 $77$。", exp_en="$4n-3$ gives $77$ when $n=20$.", tolerance=0),
    X("mathematics-8-7-2", type="mcq", id="q-ma-87-pa08", stem_zh="$y=mx+c$ 中 $c$ 表示？", stem_en="In $y=mx+c$, $c$ is the:", answer="b", exp_zh="$y$ 轴截距。", exp_en="$y$-intercept.", options=opts(("斜率", "gradient"), ("$y$ 轴截距", "$y$-intercept"), ("一定是斜率的倒数", "always the reciprocal of the gradient"), ("水平变化", "horizontal change only"))),
    X("mathematics-8-7-1", type="mcq", id="q-ma-87-pa09", stem_zh="等差数列的特征是？", stem_en="An arithmetic sequence has:", answer="d", exp_zh="公差一定。", exp_en="A constant common difference.", options=opts(("每次乘同一个分数且不能加减", "a constant multiplier and no addition"), ("没有规则", "no pattern"), ("第 $n$ 项一定是 $n^2$", "an $n$th term that must be $n^2$"), ("每次增加或减少同一个常数", "a constant difference each time"))),
    X("mathematics-8-7-2", type="numeric", id="q-ma-87-pa10", stem_zh="$y=4$ 的斜率？", stem_en="Gradient of $y=4$?", answer=0, exp_zh="水平线。", exp_en="A horizontal line.", tolerance=0),
    X("mathematics-8-7-2", type="numeric", id="q-ma-87-pa11", stem_zh="过 $(1,2)$ 与 $(3,8)$ 的斜率？", stem_en="Gradient through $(1,2)$ and $(3,8)$?", answer=3, exp_zh="$(8-2)/(3-1)=3$。", exp_en="$(8-2)/(3-1)=3$.", tolerance=0),
])

PR88 = block([
    X("mathematics-8-8-1", type="short", id="q-ma-88-pr01", stem_zh="$(0,5)$ 按 $\\begin{pmatrix} -1 \\\\ 3 \\end{pmatrix}$ 平移后？", stem_en="$(0,5)$ translated by $\\begin{pmatrix} -1 \\\\ 3 \\end{pmatrix}$?", answer="(-1,8)", accepted=["(-1,8)", "(-1, 8)"], answer_zh="$(-1,8)$", answer_en="$(-1,8)$", exp_zh="$0-1=-1$，$5+3=8$。", exp_en="$0-1=-1$, $5+3=8$."),
    X("mathematics-8-8-1", type="short", id="q-ma-88-pr02", stem_zh="$(3,3)$ 到 $(3,0)$ 的平移向量？", stem_en="Vector taking $(3,3)$ to $(3,0)$?", answer="(0,-3)", accepted=["(0,-3)", "(0, -3)"], answer_zh="$\\begin{pmatrix} 0 \\\\ -3 \\end{pmatrix}$", answer_en="$\\begin{pmatrix} 0 \\\\ -3 \\end{pmatrix}$", exp_zh="只向下 $3$。", exp_en="$3$ down only."),
    X("mathematics-8-8-1", type="short", id="q-ma-88-pr03", stem_zh="$\\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix}+\\begin{pmatrix} -4 \\\\ 0 \\end{pmatrix}=$？", stem_en="$\\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix}+\\begin{pmatrix} -4 \\\\ 0 \\end{pmatrix}=$", answer="(-3,2)", accepted=["(-3,2)", "(-3, 2)"], answer_zh="$\\begin{pmatrix} -3 \\\\ 2 \\end{pmatrix}$", answer_en="$\\begin{pmatrix} -3 \\\\ 2 \\end{pmatrix}$", exp_zh="分量相加。", exp_en="Add components."),
    X("mathematics-8-8-2", type="numeric", id="q-ma-88-pr04", stem_zh="比例尺 $4$ 把 $5\\ \\mathrm{cm}$ 变成多少厘米？", stem_en="Scale factor $4$ turns $5\\ \\mathrm{cm}$ into how many centimetres?", answer=20, exp_zh="$20$。", exp_en="$20$.", tolerance=0),
    X("mathematics-8-8-2", type="numeric", id="q-ma-88-pr05", stem_zh="比例尺 $4$ 时，面积变为原来的多少倍？", stem_en="With scale factor $4$, area becomes how many times as large?", answer=16, exp_zh="$4^2=16$。", exp_en="$4^2=16$.", tolerance=0),
    X("mathematics-8-8-2", type="numeric", id="q-ma-88-pr06", stem_zh="比例尺 $\\dfrac{1}{4}$ 把 $20\\ \\mathrm{cm}$ 变成多少厘米？", stem_en="Scale factor $\\dfrac{1}{4}$ turns $20\\ \\mathrm{cm}$ into?", answer=5, exp_zh="$5$。", exp_en="$5$.", tolerance=0),
    X("mathematics-8-8-2", type="mcq", id="q-ma-88-pr07", stem_zh="保持全等且通常翻转朝向的是？", stem_en="Which keeps congruence but usually reverses orientation?", answer="c", exp_zh="反射。", exp_en="Reflection.", options=opts(("平移", "translation"), ("放大 $k=3$", "enlargement with $k=3$"), ("反射", "reflection"), ("没有任何变换", "no transformation"))),
    X("mathematics-8-8-1", type="mcq", id="q-ma-88-pr08", stem_zh="平移不改变？", stem_en="A translation does not change:", answer="a", exp_zh="大小、形状和朝向。", exp_en="Size, shape or orientation.", options=opts(("大小和朝向", "size and orientation"), ("位置", "position"), ("图形所在的坐标原点必须移动到像点", "the requirement that the origin must move to the image"), ("所有点的坐标必须保持不变", "the need for every coordinate to stay the same"))),
])
PA88 = block([
    X("mathematics-8-8-1", type="short", id="q-ma-88-pa01", stem_zh="$(-2,-1)$ 按 $\\begin{pmatrix} 5 \\\\ 2 \\end{pmatrix}$ 平移后？", stem_en="$(-2,-1)$ translated by $\\begin{pmatrix} 5 \\\\ 2 \\end{pmatrix}$?", answer="(3,1)", accepted=["(3,1)", "(3, 1)"], answer_zh="$(3,1)$", answer_en="$(3,1)$", exp_zh="$(3,1)$。", exp_en="$(3,1)$."),
    X("mathematics-8-8-1", type="short", id="q-ma-88-pa02", stem_zh="反向于 $\\begin{pmatrix} -6 \\\\ 3 \\end{pmatrix}$ 的向量？", stem_en="The opposite of $\\begin{pmatrix} -6 \\\\ 3 \\end{pmatrix}$?", answer="(6,-3)", accepted=["(6,-3)", "(6, -3)"], answer_zh="$\\begin{pmatrix} 6 \\\\ -3 \\end{pmatrix}$", answer_en="$\\begin{pmatrix} 6 \\\\ -3 \\end{pmatrix}$", exp_zh="各分量变号。", exp_en="Change the signs."),
    X("mathematics-8-8-2", type="numeric", id="q-ma-88-pa03", stem_zh="比例尺 $5$，面积变为原来的多少倍？", stem_en="Scale factor $5$: area factor?", answer=25, exp_zh="$25$。", exp_en="$25$.", tolerance=0),
    X("mathematics-8-8-2", type="mcq", id="q-ma-88-pa04", stem_zh="旋转保持？", stem_en="A rotation preserves:", answer="b", exp_zh="到中心的距离、大小和朝向。", exp_en="Distance from the centre, size and orientation.", options=opts(("大小改变", "a change of size"), ("到中心的距离", "distance from the centre"), ("一定把图形翻转", "a flip for certain"), ("比例尺必须是 $3$", "a scale factor that must be $3$"))),
    X("mathematics-8-8-2", type="mcq", id="q-ma-88-pa05", stem_zh="$0<k<1$ 的放大会让图形？", stem_en="An enlargement with $0<k<1$ makes the shape:", answer="a", exp_zh="变小。", exp_en="Smaller.", options=opts(("变小", "smaller"), ("一定翻转", "flipped for certain"), ("变成平移", "a translation"), ("面积变为 $k$ 倍而不是 $k^2$ 倍且变大", "larger, with area multiplied by $k$ not $k^2$"))),
    X("mathematics-8-8-1", type="mcq", id="q-ma-88-pa06", stem_zh="$\\begin{pmatrix} 0 \\\\ -4 \\end{pmatrix}$ 表示？", stem_en="$\\begin{pmatrix} 0 \\\\ -4 \\end{pmatrix}$ means:", answer="d", exp_zh="向下 $4$。", exp_en="$4$ down.", options=opts(("向右 $4$", "$4$ right"), ("向左 $4$", "$4$ left"), ("向上 $4$", "$4$ up"), ("向下 $4$", "$4$ down"))),
    X("mathematics-8-8-2", type="mcq", id="q-ma-88-pa07", stem_zh="下列会改变大小的是？", stem_en="Which changes size?", answer="c", exp_zh="比例尺不是 $1$ 的放大。", exp_en="Enlargement with scale factor not $1$.", options=opts(("平移", "translation"), ("旋转 $90^\\circ$", "rotation of $90^\\circ$"), ("比例尺 $2$ 的放大", "enlargement with scale factor $2$"), ("反射", "reflection"))),
    X("mathematics-8-8-1", type="short", id="q-ma-88-pa08", stem_zh="$(4,1)$ 到 $(-1,1)$ 的向量？", stem_en="Vector from $(4,1)$ to $(-1,1)$?", answer="(-5,0)", accepted=["(-5,0)", "(-5, 0)"], answer_zh="$\\begin{pmatrix} -5 \\\\ 0 \\end{pmatrix}$", answer_en="$\\begin{pmatrix} -5 \\\\ 0 \\end{pmatrix}$", exp_zh="向左 $5$。", exp_en="$5$ left."),
    X("mathematics-8-8-2", type="numeric", id="q-ma-88-pa09", stem_zh="中心到 $A$ 为 $3\\ \\mathrm{cm}$，$k=2$，中心到 $A'$ 多少厘米？", stem_en="If $A$ is $3\\ \\mathrm{cm}$ from the centre and $k=2$, how far is $A'$ from the centre?", answer=6, exp_zh="$6$。", exp_en="$6$.", tolerance=0),
    X("mathematics-8-8-2", type="mcq", id="q-ma-88-pa10", stem_zh="放大时，角的大小？", stem_en="Under enlargement, angles:", answer="a", exp_zh="不变。", exp_en="Stay the same.", options=opts(("不变", "stay the same"), ("都乘以 $k$", "are all multiplied by $k$"), ("都变成 $90^\\circ$", "all become $90^\\circ$"), ("都消失", "all vanish"))),
    X("mathematics-8-8-1", type="mcq", id="q-ma-88-pa11", stem_zh="两次平移的合成相当于？", stem_en="Two translations composed are equivalent to:", answer="b", exp_zh="向量相加后的一次平移。", exp_en="One translation by the sum of the vectors.", options=opts(("一次反射", "a reflection"), ("向量之和对应的一次平移", "a single translation by the sum of the vectors"), ("一次放大 $k=2$", "an enlargement with $k=2$"), ("图形大小改变", "a change in size"))),
])

PR89 = block([
    X("mathematics-8-9-1", type="mcq", id="q-ma-89-pr01", stem_zh="“最喜欢的水果”是？", stem_en="“Favourite fruit” is:", answer="a", exp_zh="分类数据。", exp_en="Categorical.", options=opts(("分类数据", "categorical"), ("连续数值", "continuous numerical"), ("向量", "a vector"), ("不是数据", "not data"))),
    X("mathematics-8-9-1", type="mcq", id="q-ma-89-pr02", stem_zh="体重通常是？", stem_en="Mass (weight) is usually:", answer="c", exp_zh="连续数值。", exp_en="Continuous numerical.", options=opts(("分类", "categorical"), ("只能是离散颜色", "discrete colour only"), ("连续数值", "continuous numerical"), ("不是数据", "not data"))),
    X("mathematics-8-9-2", type="numeric", id="q-ma-89-pr03", stem_zh="$18$ 人中 $3$ 人选择某项，饼图圆心角多少度？", stem_en="$3$ out of $18$ choose an option. Pie-chart angle?", answer=60, exp_zh="$3/18\\times 360=60$。", exp_en="$3/18\\times 360=60$.", tolerance=0),
    X("mathematics-8-9-2", type="mcq", id="q-ma-89-pr04", stem_zh="表示随时间变化的趋势，宜用？", stem_en="A trend over time is best shown by a:", answer="b", exp_zh="折线图。", exp_en="Line graph.", options=opts(("只含一项的饼图且无时间轴", "a one-sector pie chart with no time axis"), ("折线图", "line graph"), ("旋转中心", "centre of rotation"), ("方位角", "bearing only"))),
    X("mathematics-8-9-3", type="numeric", id="q-ma-89-pr05", stem_zh="$1,2,2,5$ 的平均数？", stem_en="Mean of $1,2,2,5$?", answer=2.5, exp_zh="$10/4=2.5$。", exp_en="$10/4=2.5$.", tolerance=0.01),
    X("mathematics-8-9-3", type="numeric", id="q-ma-89-pr06", stem_zh="这组数据的众数？", stem_en="Mode of that list?", answer=2, exp_zh="$2$ 出现两次。", exp_en="$2$ appears twice.", tolerance=0),
    X("mathematics-8-9-3", type="numeric", id="q-ma-89-pr07", stem_zh="这组数据的极差？", stem_en="Range of that list?", answer=4, exp_zh="$5-1=4$。", exp_en="$5-1=4$.", tolerance=0),
    X("mathematics-8-9-4", type="mcq", id="q-ma-89-pr08", stem_zh="统计循环首先应？", stem_en="The statistical cycle should first:", answer="d", exp_zh="提出清楚的问题。", exp_en="Pose a clear question.", options=opts(("随意下结论", "state a random conclusion"), ("忽略局限", "ignore limitations"), ("先画无关的图", "draw an unrelated diagram"), ("提出清楚的问题", "pose a clear question"))),
])
PA89 = block([
    X("mathematics-8-9-1", type="mcq", id="q-ma-89-pa01", stem_zh="鞋子的双数（几双）通常是？", stem_en="The number of pairs of shoes is usually:", answer="b", exp_zh="离散数值。", exp_en="Discrete numerical.", options=opts(("连续", "continuous"), ("离散数值", "discrete numerical"), ("不是数据", "not data"), ("只能是分类颜色", "categorical colour only"))),
    X("mathematics-8-9-1", type="mcq", id="q-ma-89-pa02", stem_zh="只在校门口问“你是否常坐车上学”来代表全区学生，问题是？", stem_en="Asking only at one school gate to represent every student in the district is a problem because:", answer="a", exp_zh="样本可能偏差。", exp_en="The sample may be biased.", options=opts(("样本可能偏差", "the sample may be biased"), ("数据不能是分类的", "data cannot be categorical"), ("时间不能测量", "time cannot be measured"), ("平均数不存在", "a mean cannot exist"))),
    X("mathematics-8-9-2", type="numeric", id="q-ma-89-pa03", stem_zh="$40$ 人中 $10$ 人选择某项，圆心角多少度？", stem_en="$10$ out of $40$. Pie-chart angle?", answer=90, exp_zh="$90$。", exp_en="$90$.", tolerance=0),
    X("mathematics-8-9-2", type="mcq", id="q-ma-89-pa04", stem_zh="比较各类频数，宜用？", stem_en="To compare category frequencies, use a:", answer="c", exp_zh="条形图。", exp_en="Bar chart.", options=opts(("竖直线 $x=2$", "the vertical line $x=2$"), ("放大中心", "enlargement centre"), ("条形图", "bar chart"), ("只有斜率", "gradient only"))),
    X("mathematics-8-9-3", type="numeric", id="q-ma-89-pa05", stem_zh="$6,8,9,9,13$ 的中位数？", stem_en="Median of $6,8,9,9,13$?", answer=9, exp_zh="中间是 $9$。", exp_en="The middle value is $9$.", tolerance=0),
    X("mathematics-8-9-3", type="numeric", id="q-ma-89-pa06", stem_zh="这组数据的平均数？", stem_en="Mean of that list?", answer=9, exp_zh="$45/5=9$。", exp_en="$45/5=9$.", tolerance=0),
    X("mathematics-8-9-3", type="mcq", id="q-ma-89-pa07", stem_zh="有极端大值时，更适合代表典型水平的常常是？", stem_en="With an extreme large value, a typical level is often better given by the:", answer="d", exp_zh="中位数。", exp_en="Median.", options=opts(("极差", "range"), ("一定用平均数", "mean only"), ("最大的那个数", "the largest number"), ("中位数", "median"))),
    X("mathematics-8-9-4", type="mcq", id="q-ma-89-pa08", stem_zh="发现样本有偏差后应？", stem_en="After finding a biased sample you should:", answer="a", exp_zh="回到计划，改进方法或限制结论。", exp_en="Return to planning, improve the method or restrict the conclusion.", options=opts(("回到计划并改进或限制结论", "return to planning and improve or restrict the conclusion"), ("把结论写得更绝对", "make the conclusion more absolute"), ("删除问题本身", "delete the question itself"), ("忽略数据来源", "ignore where the data came from"))),
    X("mathematics-8-9-4", type="mcq", id="q-ma-89-pa09", stem_zh="好的结论应当？", stem_en="A good conclusion should:", answer="b", exp_zh="回答问题并承认局限。", exp_en="Answer the question and admit limitations.", options=opts(("完全离开原问题", "leave the original question"), ("回答问题并承认局限", "answer the question and admit limitations"), ("不看图和表", "ignore tables and diagrams"), ("推广到所有未调查对象且不说明", "extend to everyone unsurveyed with no comment"))),
    X("mathematics-8-9-3", type="numeric", id="q-ma-89-pa10", stem_zh="$3,10$ 两个数的中位数（偶数个数据取平均）？", stem_en="Median of the two values $3$ and $10$?", answer=6.5, exp_zh="$(3+10)/2=6.5$。", exp_en="$(3+10)/2=6.5$.", tolerance=0.01),
    X("mathematics-8-9-2", type="mcq", id="q-ma-89-pa11", stem_zh="读图时必须看？", stem_en="When reading a graph you must look at:", answer="c", exp_zh="标题与轴的量和单位。", exp_en="The title and the quantities and units on the axes.", options=opts(("只看颜色", "only the colours"), ("只看是否陡", "only whether it looks steep"), ("标题与轴的量和单位", "the title and the quantities and units on the axes"), ("忽略刻度", "the picture while ignoring the scale"))),
])

COMP = block([
    X("mathematics-8-1-2", type="numeric", id="q-ma-comp-01", stem_zh="计算 $2^6\\div 2^3$。", stem_en="Evaluate $2^6\\div 2^3$.", answer=8, exp_zh="$2^3=8$。", exp_en="$2^3=8$.", tolerance=0),
    X("mathematics-8-1-3", type="numeric", id="q-ma-comp-02", stem_zh="计算 $4+18\\div 6$。", stem_en="Evaluate $4+18\\div 6$.", answer=7, exp_zh="$4+3=7$。", exp_en="$4+3=7$.", tolerance=0),
    X("mathematics-8-2-2", type="numeric", id="q-ma-comp-03", stem_zh="解 $6x-5=19$。$x=$？", stem_en="Solve $6x-5=19$. $x=$", answer=4, exp_zh="$6x=24$，$x=4$。", exp_en="$6x=24$, $x=4$.", tolerance=0),
    X("mathematics-8-3-2", type="numeric", id="q-ma-comp-04", stem_zh="半径 $10\\ \\mathrm{cm}$ 的圆周长？（$\\pi=3.14$）", stem_en="Circumference of a circle of radius $10\\ \\mathrm{cm}$? ($\\pi=3.14$)", answer=62.8, exp_zh="$2\\times 3.14\\times 10=62.8$。", exp_en="$62.8$.", tolerance=0.05),
    X("mathematics-8-3-3", type="numeric", id="q-ma-comp-05", stem_zh="长方体 $4\\times 5\\times 6$ 的体积？", stem_en="Volume of a $4\\times 5\\times 6$ cuboid?", answer=120, exp_zh="$120$。", exp_en="$120$.", tolerance=0),
    X("mathematics-8-4-3", type="numeric", id="q-ma-comp-06", stem_zh="从 $\$80$ 涨到 $\$100$，百分数增加？", stem_en="Percentage increase from $\$80$ to $\$100$ (number only)?", answer=25, exp_zh="$20/80=25\\%$。", exp_en="$25\\%$.", tolerance=0),
    X("mathematics-8-4-2", type="short", id="q-ma-comp-07", stem_zh="$\\dfrac{2}{5}+\\dfrac{1}{10}=$？", stem_en="$\\dfrac{2}{5}+\\dfrac{1}{10}=$", answer="1/2", accepted=["1/2", "5/10", "0.5"], answer_zh="$\\dfrac{1}{2}$", answer_en="$\\dfrac{1}{2}$", exp_zh="$\\dfrac{4}{10}+\\dfrac{1}{10}=\\dfrac{1}{2}$。", exp_en="$\\dfrac{1}{2}$."),
    X("mathematics-8-5-1", type="short", id="q-ma-comp-08", stem_zh="公平骰子掷出大于 $4$ 的概率？", stem_en="Probability of a number greater than $4$ on a fair die?", answer="1/3", accepted=["1/3", "2/6"], answer_zh="$\\dfrac{1}{3}$", answer_en="$\\dfrac{1}{3}$", exp_zh="$5$ 或 $6$。", exp_en="$5$ or $6$."),
    X("mathematics-8-6-1", type="numeric", id="q-ma-comp-09", stem_zh="三角形两角 $55^\\circ$、$65^\\circ$，第三角？", stem_en="Two angles $55^\\circ$ and $65^\\circ$. Third angle?", answer=60, exp_zh="$60$。", exp_en="$60$.", tolerance=0),
    X("mathematics-8-7-1", type="short", id="q-ma-comp-10", stem_zh="$3,8,13,18,\\ldots$ 的第 $n$ 项？", stem_en="$n$th term of $3,8,13,18,\\ldots$?", answer="5n-2", accepted=["5n-2", "5n - 2"], answer_zh="$5n-2$", answer_en="$5n-2$", exp_zh="公差 $5$。", exp_en="Difference $5$."),
    X("mathematics-8-7-2", type="numeric", id="q-ma-comp-11", stem_zh="过 $(0,2)$ 和 $(4,10)$ 的斜率？", stem_en="Gradient through $(0,2)$ and $(4,10)$?", answer=2, exp_zh="$8/4=2$。", exp_en="$8/4=2$.", tolerance=0),
    X("mathematics-8-8-1", type="short", id="q-ma-comp-12", stem_zh="$(1,-3)$ 按 $\\begin{pmatrix} 2 \\\\ 5 \\end{pmatrix}$ 平移后？", stem_en="$(1,-3)$ translated by $\\begin{pmatrix} 2 \\\\ 5 \\end{pmatrix}$?", answer="(3,2)", accepted=["(3,2)", "(3, 2)"], answer_zh="$(3,2)$", answer_en="$(3,2)$", exp_zh="$(3,2)$。", exp_en="$(3,2)$."),
    X("mathematics-8-8-2", type="numeric", id="q-ma-comp-13", stem_zh="比例尺 $2$ 时面积变为原来的多少倍？", stem_en="Area factor when the scale factor is $2$?", answer=4, exp_zh="$2^2=4$。", exp_en="$2^2=4$.", tolerance=0),
    X("mathematics-8-9-3", type="numeric", id="q-ma-comp-14", stem_zh="$4,5,5,6$ 的平均数？", stem_en="Mean of $4,5,5,6$?", answer=5, exp_zh="$20/4=5$。", exp_en="$20/4=5$.", tolerance=0),
    X("mathematics-8-9-2", type="numeric", id="q-ma-comp-15", stem_zh="$36$ 人中 $9$ 人选择某项，饼图圆心角？", stem_en="$9$ out of $36$. Pie-chart angle?", answer=90, exp_zh="$90$。", exp_en="$90$.", tolerance=0),
])

for lesson in LESSONS:
    add_lesson(C, lesson)

def chap_title(n, zh, en):
    return n, zh, en

chapters_meta = [
    ("mathematics-8-1", "数与运算", "Number and calculation", PR81, PA81, 15, 25),
    ("mathematics-8-2", "代数表示与变形", "Algebraic representation and manipulation", PR82, PA82, 15, 25),
    ("mathematics-8-3", "平面图形与立体图形", "2D and 3D shape", PR83, PA83, 15, 25),
    ("mathematics-8-4", "分数、小数、百分数、比与比例", "Fractions, decimals, percentages, ratio and proportion", PR84, PA84, 15, 25),
    ("mathematics-8-5", "概率", "Probability", PR85, PA85, 12, 22),
    ("mathematics-8-6", "角与作图", "Angles and construction", PR86, PA86, 15, 22),
    ("mathematics-8-7", "数列、函数与图像", "Sequences, functions and graphs", PR87, PA87, 15, 22),
    ("mathematics-8-8", "变换", "Transformations", PR88, PA88, 12, 22),
    ("mathematics-8-9", "统计", "Statistics", PR89, PA89, 15, 25),
]
set_rows = []
for cid, zh, en, pr, pa, t1, t2 in chapters_meta:
    set_rows.append(dict(kind="practice", chapter=cid, title_zh=f"本章练习 · {zh}", title_en=f"Chapter practice · {en}", qids=pr, minutes=t1))
    set_rows.append(dict(kind="paper", chapter=cid, title_zh=f"本章测试卷 · {zh}", title_en=f"Chapter test · {en}", qids=pa, minutes=t2))

add_sets(C, set_rows, comprehensive=dict(
    id="paper-mathematics-8-comprehensive",
    title_zh="八年级数学综合测试卷", title_en="Grade 8 Mathematics comprehensive paper",
    qids=COMP, minutes=35, published="2026-11-12T09:00:00+08:00",
))

knowledge_ma = C.knowledge
questions_ma = C.questions
sets_ma = C.sets
