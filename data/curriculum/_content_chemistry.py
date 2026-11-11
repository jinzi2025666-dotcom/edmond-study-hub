"""Grade 8 Chemistry — complete bilingual course (Cambridge Science 0893 Stage 8)."""
from _helpers import opts
from _course_util import Course, maps_from_units, svg, INK, ACCENT
from _apply import add_lesson, add_extra_questions, add_sets

UNIT_OF, CHAPTER_OF = maps_from_units("chemistry")
C = Course("chemistry", UNIT_OF, CHAPTER_OF, recent={
    "chemistry-8Cm-1": "2026-11-12T09:00:00+08:00",
    "chemistry-8Cp-1": "2026-11-11T09:00:00+08:00",
    "chemistry-8Cc-2": "2026-11-10T09:00:00+08:00",
    "chemistry-8ES-2": "2026-11-09T09:00:00+08:00",
}, tag="ch")


def fig(inner, w=520, h=220):
    return svg(inner.replace("{INK}", INK).replace("{ACC}", ACCENT), w=w, h=h)


D_RUTH = fig("""
  <circle cx="160" cy="110" r="14" {ACC}/>
  <circle cx="160" cy="110" r="55" {INK}/>
  <circle cx="160" cy="110" r="90" {INK}/>
  <circle cx="215" cy="110" r="6" fill="currentColor"/>
  <circle cx="70" cy="110" r="6" fill="currentColor"/>
  <circle cx="160" cy="20" r="6" fill="currentColor"/>
  <text x="130" y="114" font-size="9" fill="#b85c38">nucleus</text>
  <text x="280" y="70" font-size="13" fill="currentColor">electrons in the space</text>
  <text x="280" y="90" font-size="13" fill="currentColor">around the nucleus</text>
  <text x="280" y="140" font-size="13" fill="currentColor">almost all the mass</text>
  <text x="280" y="160" font-size="13" fill="currentColor">is in the tiny nucleus</text>
""")
D_CHROM = fig("""
  <rect x="80" y="30" width="70" height="170" {INK}/>
  <line x1="80" y1="180" x2="150" y2="180" {ACC}/>
  <circle cx="115" cy="170" r="4" fill="#b85c38"/>
  <circle cx="115" cy="110" r="5" fill="currentColor"/>
  <circle cx="115" cy="70" r="5" fill="currentColor"/>
  <line x1="80" y1="40" x2="150" y2="40" {INK} stroke-dasharray="4 3"/>
  <text x="170" y="45" font-size="12" fill="currentColor">solvent front</text>
  <text x="170" y="115" font-size="12" fill="currentColor">spot</text>
  <text x="170" y="184" font-size="12" fill="currentColor">baseline</text>
  <text x="300" y="110" font-size="14" fill="currentColor">Rf = d_spot / d_solvent</text>
""")
D_SOLUB = fig("""
  <line x1="70" y1="190" x2="480" y2="190" {INK}/>
  <line x1="70" y1="190" x2="70" y2="25" {INK}/>
  <text x="16" y="30" font-size="12" fill="currentColor">solubility</text>
  <text x="430" y="212" font-size="12" fill="currentColor">temperature</text>
  <polyline points="70,170 160,140 260,100 360,70 450,50" {ACC}/>
  <text x="200" y="60" font-size="13" fill="#b85c38">typical salt: solubility rises with T</text>
""")
D_ENERGY = fig("""
  <text x="110" y="28" font-size="13" fill="currentColor">exothermic</text>
  <line x1="70" y1="60" x2="200" y2="60" {ACC}/>
  <text x="70" y="52" font-size="11" fill="currentColor">reactants</text>
  <line x1="130" y1="60" x2="130" y2="150" {INK}/>
  <polygon points="130,150 124,138 136,138" fill="currentColor"/>
  <line x1="70" y1="150" x2="200" y2="150" {INK}/>
  <text x="70" y="168" font-size="11" fill="currentColor">products (lower energy)</text>
  <text x="330" y="28" font-size="13" fill="currentColor">endothermic</text>
  <line x1="290" y1="150" x2="420" y2="150" {ACC}/>
  <text x="290" y="168" font-size="11" fill="currentColor">reactants</text>
  <line x1="350" y1="150" x2="350" y2="60" {INK}/>
  <polygon points="350,60 344,72 356,72" fill="currentColor"/>
  <line x1="290" y1="60" x2="420" y2="60" {INK}/>
  <text x="290" y="52" font-size="11" fill="currentColor">products (higher energy)</text>
""")
D_CONC = fig("""
  <rect x="80" y="50" width="90" height="140" {INK}/>
  <rect x="80" y="90" width="90" height="100" fill="currentColor" opacity="0.12"/>
  <text x="95" y="40" font-size="12" fill="currentColor">same solute</text>
  <text x="88" y="170" font-size="12" fill="#b85c38">smaller V</text>
  <rect x="260" y="50" width="160" height="140" {INK}/>
  <rect x="260" y="90" width="160" height="100" fill="currentColor" opacity="0.08"/>
  <text x="300" y="40" font-size="12" fill="currentColor">same solute</text>
  <text x="300" y="170" font-size="12" fill="#b85c38">larger V, lower concentration</text>
""")

LESSONS = []

def L(**kw):
    LESSONS.append(kw)

# ----- 8Cm.01 -----
L(
    id="chemistry-8Cm-1",
    title_zh="卢瑟福原子模型", title_en="The Rutherford model of the atom",
    obj_zh="本节你将学会用卢瑟福模型描述原子：很小的原子核含有质子和中子，电子在核周围的空间中运动。",
    obj_en="This lesson you will describe the Rutherford model: a tiny nucleus contains protons and neutrons, and electrons move in the space around it.",
    kp_zh="""- 原子大部分是空的：质量几乎全部集中在中心很小的**原子核**里。
- 原子核含有**质子**和**中子**；**电子**在核周围的空间中。
- 模型来自α粒子散射：大多数α粒子几乎直线穿过金箔，少数发生大角度偏转。
- 大角度偏转说明正电荷和质量集中在很小的核上。
- 本阶段用这个模型解释结构即可，不必引入后续电子层的计算公式。""",
    kp_en="""- An atom is mostly empty space: almost all the mass is in a tiny central **nucleus**.
- The nucleus contains **protons** and **neutrons**; **electrons** occupy the space around it.
- The model comes from alpha-particle scattering: most particles go nearly straight through gold foil; a few are deflected through large angles.
- Large deflections show that positive charge and mass are concentrated in a very small nucleus.
- At this stage, use the model to describe structure; you do not need later shell-equation detail.""",
    body_zh=r"""卢瑟福模型是第 8 阶段化学认识原子的起点。它要我们记住两件事：原子**不是**实心的均匀小球；正电荷和绝大部分质量都挤在中心一个极小的核里。

金箔实验可以这样理解。如果原子像“实心布丁”，带正电、质量较大的α粒子穿过时只会被轻轻偏转。实际上，绝大多数α粒子几乎不改变方向，说明它们大部分时间在走空旷的空间；极少数几乎被弹回，说明它们遇上了又小又“硬”（质量很大、带正电）的东西——这就是**原子核**。

在这个模型里：核内有质子和中子；电子在核周围的空间中；核的体积远小于整个原子，所以原子大部分是空的。

## 例题

为什么绝大多数α粒子能几乎直线穿过金箔，却仍有少数偏转很大？

**解：** 原子内部大部分是空的，所以多数α粒子不会靠近核。一旦α粒子非常接近带正电的核，同种电荷相斥，再加上核的质量很大，就会出现大角度偏转。""",
    body_en=r"""The Rutherford model is the Stage 8 starting point for atomic structure. Remember two ideas: an atom is **not** a solid uniform ball; positive charge and almost all the mass are packed into a very small central nucleus.

The gold-foil experiment makes sense in those terms. If atoms were like a solid “pudding”, alpha particles (positive and fairly massive) would only be deflected gently. In fact, most travel almost straight on, so they spend most of their time in empty space. A very small number bounce back, so they have met something tiny, massive and positive — the **nucleus**.

In the model the nucleus contains protons and neutrons, electrons occupy the space around it, and the nucleus is far smaller than the atom, so an atom is mostly empty space.

## Worked example

Why do most alpha particles go almost straight through gold foil, while a few are deflected sharply?

**Solution:** Most of the atom is empty space, so most particles never go near a nucleus. If an alpha particle approaches the positive nucleus closely, like charges repel. The nucleus is also massive, so the deflection can be large.""",
    diff_zh="""- **把电子画进核里。** 质子和中子在核内，电子在核外的空间中。
- **以为原子是实心的。** 否则不会有那么多α粒子几乎不偏转。
- **把“少数大偏转”说成“全部被弹回”。** 大偏转很少，正因为核很小。""",
    diff_en="""- **Putting electrons inside the nucleus.** Protons and neutrons are in the nucleus; electrons are in the space around it.
- **Treating the atom as solid.** Otherwise most alpha particles would not go almost straight on.
- **Saying that all alpha particles bounce back.** Large deflections are rare because the nucleus is very small.""",
    diagram=D_RUTH,
    questions=[
        dict(type="mcq", stem_zh="在卢瑟福模型中，原子核里有什么？", stem_en="In the Rutherford model, what does the nucleus contain?",
             answer="b", exp_zh="核内是质子和中子；电子在核周围的空间中。", exp_en="The nucleus contains protons and neutrons; electrons occupy the space around it.",
             options=opts(("只有电子", "electrons only"), ("质子和中子", "protons and neutrons"),
                          ("只有中子和电子", "neutrons and electrons only"), ("均匀分布的正电荷布丁", "a pudding of spread-out positive charge"))),
        dict(type="mcq", stem_zh="金箔实验中，大多数α粒子几乎直线穿过，这说明什么？", stem_en="In the gold-foil experiment, most alpha particles travel almost straight on. This suggests that:",
             answer="c", exp_zh="原子内部大部分是空的，所以多数α粒子不会靠近核。", exp_en="An atom is mostly empty space, so most alpha particles never go near a nucleus.",
             options=opts(("原子是实心的", "atoms are solid throughout"), ("电子都在核的正中央", "all electrons sit at the exact centre of the nucleus"),
                          ("原子大部分是空的", "atoms are mostly empty space"), ("金箔没有原子", "gold foil contains no atoms"))),
        dict(type="mcq", stem_zh="少数α粒子发生很大偏转，最合理的解释是？", stem_en="A few alpha particles are deflected through large angles. The best explanation is that:",
             answer="a", exp_zh="正电荷和质量集中在很小的核上，靠近它的α粒子会被强烈排斥。", exp_en="Positive charge and mass are concentrated in a tiny nucleus, which strongly repels a close alpha particle.",
             options=opts(("正电荷和质量集中在很小的核上", "positive charge and mass are concentrated in a tiny nucleus"),
                          ("电子质量极大，能把α粒子弹回", "electrons are extremely massive and can bounce alpha particles back"),
                          ("α粒子都带负电", "alpha particles are all negatively charged"),
                          ("金原子没有原子核", "gold atoms have no nucleus"))),
        dict(type="short", stem_zh="用一句话说明：原子的质量主要在哪里？", stem_en="In one sentence, where is most of the mass of an atom?",
             answer="nucleus", accepted=["nucleus", "the nucleus", "atomic nucleus", "in the nucleus", "原子核", "在原子核里", "核里", "几乎全部在原子核里"],
             answer_zh="几乎全部在原子核里。", answer_en="Almost all of it is in the nucleus.",
             exp_zh="质量几乎全部集中在很小的原子核中；电子质量比核小得多。", exp_en="Almost all the mass is in the tiny nucleus; electrons contribute very little."),
        dict(type="mcq", stem_zh="下列哪一项符合卢瑟福模型？", stem_en="Which statement matches the Rutherford model?",
             answer="d", exp_zh="电子在核周围的空间中，不在核内。", exp_en="Electrons occupy the space around the nucleus, not the inside of it.",
             options=opts(("电子和质子都在核内，中子在核外", "electrons and protons are in the nucleus and neutrons are outside"),
                          ("原子是带正电的实心球，电子嵌在里面", "the atom is a solid positive ball with electrons stuck inside"),
                          ("原子核占据了原子的大部分体积", "the nucleus fills most of the volume of the atom"),
                          ("电子在原子核周围的空间中运动", "electrons move in the space around the nucleus"))),
        dict(type="mcq", stem_zh="α粒子带正电。它被原子核强烈推开，说明原子核带什么电？", stem_en="Alpha particles are positive. They are strongly pushed away from the nucleus, so the nucleus is:",
             answer="b", exp_zh="同种电荷相斥，因此核带正电。", exp_en="Like charges repel, so the nucleus is positive.",
             options=opts(("负电", "negative"), ("正电", "positive"), ("不带电", "uncharged"), ("时正时负", "sometimes positive and sometimes negative"))),
    ],
)

# ----- 8Cm.02 -----
L(
    id="chemistry-8Cm-2",
    title_zh="质子、中子与电子的电荷", title_en="Charges of protons, neutrons and electrons",
    obj_zh="本节你将学会说出质子、中子和电子的相对电荷，并解释原子为什么整体不带电。",
    obj_en="This lesson you will state the relative charges of protons, neutrons and electrons, and explain why an atom is overall uncharged.",
    kp_zh="""- **质子**相对电荷为 $+1$；**电子**为 $-1$；**中子**为 $0$（不带电）。
- 质子和中子的相对质量约为 $1$；电子质量小得多，常看作约 $0$（相对该标度）。
- 原子整体呈电中性：质子数等于电子数，正负电荷抵消。
- 电荷种类由粒子决定，不随原子种类随意改变。
- 离子是原子得失电子后形成的，本课先把中性原子分清。""",
    kp_en="""- A **proton** has relative charge $+1$; an **electron** has $-1$; a **neutron** has $0$ (no charge).
- Protons and neutrons have relative mass about $1$; an electron’s mass is much smaller and is often treated as about $0$ on that scale.
- An atom is overall electrically neutral: the number of protons equals the number of electrons, so the charges cancel.
- The charge of each particle is a fixed property.
- Ions form when atoms gain or lose electrons; this lesson first makes the neutral atom clear.""",
    body_zh=r"""把三种粒子的电荷记牢，后面解释“核吸住电子”和“原子为何不带电”才会顺。

相对电荷：

- 质子：$+1$
- 电子：$-1$
- 中子：$0$

一个中性原子里，质子的数目等于电子的数目。例如一个原子有 $11$ 个质子，它也有 $11$ 个电子，总电荷为 $11\times(+1)+11\times(-1)=0$。中子不改变电荷，只增加核的质量。

相对质量上也要能区分：质子和中子差不多重，电子则轻得多。所以原子质量几乎都在核里，这与上一节的卢瑟福模型一致。

## 例题

某中性原子有 $8$ 个质子和 $8$ 个中子。它有多少个电子？总相对电荷是多少？

**解：** 中性原子电子数等于质子数，所以有 $8$ 个电子。总电荷 $8-8=0$。中子不影响电荷。""",
    body_en=r"""Once the charges of the three particles are secure, it becomes easier to explain why the nucleus holds electrons and why an atom is uncharged.

Relative charges:

- proton: $+1$
- electron: $-1$
- neutron: $0$

In a neutral atom the number of protons equals the number of electrons. If an atom has $11$ protons it also has $11$ electrons, and the total charge is $11\times(+1)+11\times(-1)=0$. Neutrons do not change the charge; they add mass to the nucleus.

On the relative-mass scale, protons and neutrons are about the same, and an electron is much lighter. That is why almost all the mass of an atom is in the nucleus, which matches the Rutherford model.

## Worked example

A neutral atom has $8$ protons and $8$ neutrons. How many electrons does it have, and what is the total relative charge?

**Solution:** In a neutral atom the electron number equals the proton number, so there are $8$ electrons. The total charge is $8-8=0$. Neutrons do not affect charge.""",
    diff_zh="""- **把中子当成带负电。** 中子不带电；带负电的是电子。
- **把电子数写成等于中子数。** 中性原子里电子数等于质子数。
- **记反质子和电子的符号。** 质子为正，电子为负。""",
    diff_en="""- **Giving the neutron a negative charge.** Neutrons are uncharged; electrons are negative.
- **Setting the electron number equal to the neutron number.** In a neutral atom it equals the proton number.
- **Swapping the signs.** Protons are positive and electrons are negative.""",
    questions=[
        dict(type="mcq", stem_zh="电子的相对电荷是？", stem_en="The relative charge of an electron is:",
             answer="c", exp_zh="电子为 $-1$，质子为 $+1$，中子为 $0$。", exp_en="An electron is $-1$, a proton is $+1$ and a neutron is $0$.",
             options=opts(("$+1$", "$+1$"), ("$0$", "$0$"), ("$-1$", "$-1$"), ("$+2$", "$+2$"))),
        dict(type="mcq", stem_zh="中子的相对电荷是？", stem_en="The relative charge of a neutron is:",
             answer="b", exp_zh="中子不带电，相对电荷为 $0$。", exp_en="A neutron is uncharged, so its relative charge is $0$.",
             options=opts(("$+1$", "$+1$"), ("$0$", "$0$"), ("$-1$", "$-1$"), ("与电子相同", "the same as an electron"))),
        dict(type="numeric", stem_zh="某中性原子有 $17$ 个质子。它有多少个电子？", stem_en="A neutral atom has $17$ protons. How many electrons does it have?",
             answer=17, exp_zh="中性原子中电子数等于质子数，所以是 $17$。", exp_en="In a neutral atom the electron number equals the proton number, so $17$.", tolerance=0),
        dict(type="mcq", stem_zh="为什么中性原子整体不带电？", stem_en="Why is a neutral atom overall uncharged?",
             answer="a", exp_zh="质子的正电荷与等量电子的负电荷抵消；中子不贡献电荷。", exp_en="The protons’ positive charge is cancelled by an equal number of electrons; neutrons add no charge.",
             options=opts(("质子数等于电子数，电荷抵消", "the numbers of protons and electrons are equal, so the charges cancel"),
                          ("原子里没有带电粒子", "the atom contains no charged particles"),
                          ("中子把所有电荷吸收了", "neutrons absorb all the charge"),
                          ("电子质量为零所以没有电荷", "electrons have zero mass and therefore no charge"))),
        dict(type="mcq", stem_zh="关于相对质量，下列说法正确的是？", stem_en="Which statement about relative mass is correct?",
             answer="d", exp_zh="质子和中子相对质量约 $1$，电子小得多，所以质量几乎都在核里。", exp_en="Protons and neutrons have relative mass about $1$; an electron is much lighter, so almost all the mass is in the nucleus.",
             options=opts(("电子比质子重得多", "an electron is much heavier than a proton"),
                          ("中子的电荷为 $+1$，所以最重", "a neutron has charge $+1$ and is therefore the heaviest"),
                          ("三种粒子相对质量都约为 $1$", "all three particles have relative mass about $1$"),
                          ("质子与中子差不多重，电子轻得多", "protons and neutrons are similar in mass; an electron is much lighter"))),
        dict(type="short", stem_zh="写出质子的相对电荷（用 $+1$、$-1$ 或 $0$）。", stem_en="State the relative charge of a proton (use $+1$, $-1$ or $0$).",
             answer="+1", accepted=["+1", "1", "+ 1", "正1", "+1（正）"],
             answer_zh="$+1$", answer_en="$+1$",
             exp_zh="质子带正电，相对电荷为 $+1$。", exp_en="A proton is positive, so its relative charge is $+1$."),
    ],
)

# ----- 8Cm.03 -----
L(
    id="chemistry-8Cm-3",
    title_zh="静电引力与原子", title_en="Electrostatic attraction in atoms",
    obj_zh="本节你将学会用正负电荷之间的静电引力，解释原子核为什么能把电子留在周围。",
    obj_en="This lesson you will use electrostatic attraction between opposite charges to explain why the nucleus holds electrons around it.",
    kp_zh="""- **同种电荷相斥，异种电荷相吸。**
- 原子核因质子而带**正电**，电子带**负电**，因此核与电子相互吸引。
- 这种吸引力叫**静电引力**，它把电子留在核周围的空间中。
- 中子不带电，不提供这种吸引，但增加核的质量。
- 若没有这种吸引，电子就不会稳定地留在原子里。""",
    kp_en="""- **Like charges repel; opposite charges attract.**
- The nucleus is **positive** because of its protons; electrons are **negative**, so the nucleus and electrons attract each other.
- This **electrostatic attraction** holds the electrons in the space around the nucleus.
- Neutrons are uncharged, so they do not provide this attraction, but they add mass.
- Without the attraction, electrons would not stay in the atom.""",
    body_zh=r"""静电现象其实就是电荷之间的推和拉。同种电荷互相推开，异种电荷互相拉近。原子能保持完整，靠的就是这一点。

原子核里有质子，所以核带正电。电子带负电。正负相吸，电子就被留在核周围的空间中。中子不带电，对这种吸引没有贡献。

这也解释了金箔实验里α粒子（带正电）靠近核时会被推开：那是**同种电荷相斥**，和核吸电子的“异种相吸”是同一套规则的两面。

## 例题

如果电子带的是正电，原子还能靠静电作用保持现在这样的结构吗？

**解：** 不能按同样方式。若电子也带正电，它们会与核相互排斥，而不是被核吸引，电子就无法稳定地留在核周围。""",
    body_en=r"""Electrostatics is about pushes and pulls between charges. Like charges repel; opposite charges attract. That is what holds an atom together.

The nucleus contains protons, so it is positive. Electrons are negative. Opposite charges attract, so electrons stay in the space around the nucleus. Neutrons are uncharged and do not provide this attraction.

The same rule explains why a positive alpha particle is pushed away if it comes close to a nucleus: that is **like charges repelling**, the other side of the same idea as the nucleus attracting electrons.

## Worked example

If electrons were positive, could an atom still be held together in the same way by electrostatic forces?

**Solution:** Not in the same way. Positive electrons would be repelled by the positive nucleus, not attracted, so they would not stay around the nucleus.""",
    diff_zh="""- **说成中子把电子吸住。** 提供吸引的是带正电的质子（整个核）。
- **把“核吸电子”说成“电子吸质子所以电子进了核”。** 电子仍在核外空间中运动，只是被核拉住。
- **记反相吸相斥。** 异种相吸，同种相斥。""",
    diff_en="""- **Saying that neutrons hold the electrons.** The attraction comes from the positive protons (the nucleus as a whole).
- **Thinking attraction means electrons fall into the nucleus.** Electrons still occupy the space around the nucleus; they are held there, not pulled inside in this model.
- **Reversing attract and repel.** Opposite charges attract; like charges repel.""",
    questions=[
        dict(type="mcq", stem_zh="原子核能把电子留在周围，主要是因为？", stem_en="The nucleus holds electrons around it mainly because:",
             answer="b", exp_zh="核带正电、电子带负电，异种电荷相互吸引。", exp_en="The nucleus is positive and electrons are negative, so opposite charges attract.",
             options=opts(("中子带负电，吸引电子", "neutrons are negative and attract electrons"),
                          ("核带正电，电子带负电，异种电荷相吸", "the nucleus is positive and electrons are negative, so they attract"),
                          ("电子质量很大，掉不出去", "electrons are so massive that they cannot leave"),
                          ("同种电荷相吸", "like charges attract"))),
        dict(type="mcq", stem_zh="下列哪一对会相互吸引？", stem_en="Which pair attracts each other?",
             answer="a", exp_zh="质子与电子是异种电荷，相互吸引。", exp_en="A proton and an electron have opposite charges, so they attract.",
             options=opts(("质子与电子", "a proton and an electron"), ("质子与质子", "a proton and a proton"),
                          ("电子与电子", "an electron and an electron"), ("中子与中子（因电荷）", "two neutrons, because of charge"))),
        dict(type="mcq", stem_zh="中子在“核吸引电子”这件事里扮演什么角色？", stem_en="What role do neutrons play in the nucleus attracting electrons?",
             answer="c", exp_zh="中子不带电，不提供静电吸引；它们主要增加核的质量。", exp_en="Neutrons are uncharged, so they do not provide electrostatic attraction; they mainly add mass.",
             options=opts(("中子带正电，是主要吸引力来源", "neutrons are positive and are the main source of attraction"),
                          ("中子带负电，把电子推开", "neutrons are negative and push electrons away"),
                          ("中子不带电，不提供这种静电吸引", "neutrons are uncharged and do not provide this attraction"),
                          ("中子负责抵消电子的质量", "neutrons cancel the mass of the electrons"))),
        dict(type="short", stem_zh="用四个字或一句话写出电荷相互作用的基本规则（相吸／相斥）。", stem_en="State the basic rule for how charges interact (attract / repel).",
             answer="opposite attract, like repel",
             accepted=["opposite attract, like repel", "like charges repel, opposite charges attract",
                       "异种相吸，同种相斥", "同种电荷相斥，异种电荷相吸", "异种电荷相吸，同种电荷相斥"],
             answer_zh="异种电荷相吸，同种电荷相斥。", answer_en="Opposite charges attract; like charges repel.",
             exp_zh="这是解释核吸电子、以及α粒子被核推开的同一条规则。", exp_en="The same rule explains both the nucleus holding electrons and alpha particles being pushed away."),
        dict(type="mcq", stem_zh="α粒子靠近原子核时被推开，是因为？", stem_en="An alpha particle is pushed away as it approaches a nucleus because:",
             answer="d", exp_zh="α粒子和核都带正电，同种电荷相斥。", exp_en="Both the alpha particle and the nucleus are positive, so like charges repel.",
             options=opts(("α粒子带负电，被核吸引后又弹回", "the alpha particle is negative, is attracted, then bounces"),
                          ("中子把α粒子弹开", "neutrons bounce the alpha particle away"),
                          ("电子质量太大", "electrons are too massive"),
                          ("α粒子与核都带正电，同种电荷相斥", "both are positive, so like charges repel"))),
        dict(type="mcq", stem_zh="若没有静电引力，最可能出现的情况是？", stem_en="If there were no electrostatic attraction, what would be most likely?",
             answer="a", exp_zh="电子不会被核留在周围，原子无法保持现在的结构。", exp_en="Electrons would not be held around the nucleus, so atoms would not keep their present structure.",
             options=opts(("电子不会被留在核周围", "electrons would not be held around the nucleus"),
                          ("中子会立刻变成质子", "neutrons would instantly become protons"),
                          ("原子质量全部消失", "all atomic mass would vanish"),
                          ("α粒子不再带电", "alpha particles would lose their charge"))),
    ],
)

# ----- 8Cm.04 -----
L(
    id="chemistry-8Cm-4",
    title_zh="纯度", title_en="Purity",
    obj_zh="本节你将学会说明什么是纯净物，以及如何用熔点和沸点判断物质是否纯。",
    obj_en="This lesson you will explain what a pure substance is and how melting and boiling points can be used as evidence of purity.",
    kp_zh="""- **纯净物**只含一种元素或一种化合物，组成固定。
- **混合物**含有两种或更多物质，组成可以改变。
- 纯净物有**固定、尖锐**的熔点与沸点。
- 杂质通常使熔点**降低**、熔程变宽，并使沸点**升高**或沸腾温度范围变宽。
- 测定熔点或沸点，并与数据手册比较，是判断纯度的常用方法。""",
    kp_en="""- A **pure substance** contains only one element or one compound and has a fixed composition.
- A **mixture** contains two or more substances; its composition can vary.
- A pure substance has a **sharp, fixed** melting point and boiling point.
- Impurities usually **lower** the melting point and widen the melting range, and they can **raise** the boiling point or widen the boiling range.
- Measuring melting or boiling point and comparing with a data book is a common test of purity.""",
    body_zh=r"""第 8 阶段的“纯度”不是日常口语里的“很干净”，而是：**样品里是否只有一种物质**。蒸馏水是纯的化合物；空气、海水、盐水则是混合物。

纯净物在加热时，会在一个确定的温度熔化或沸腾。例如纯冰在 $0^\circ\mathrm{C}$ 熔化（标准条件下），温度在熔化过程中保持稳定。若水里溶了盐，冰会在更低的温度开始熔化，而且熔化过程会跨过一段温度范围。

把测到的熔点或沸点与可靠数据比较：若温度对不上，或熔程很宽，样品就可能不纯。这在实验室鉴定固体时特别有用。

## 例题

某固体的数据手册熔点为 $80^\circ\mathrm{C}$。样品从 $74^\circ\mathrm{C}$ 开始熔化，到 $79^\circ\mathrm{C}$ 才熔化完。这说明什么？

**解：** 熔点偏低且熔程较宽，说明样品很可能含有杂质，不是纯净物。""",
    body_en=r"""At Stage 8, **purity** does not just mean “looks clean”. It means: does the sample contain only one substance? Distilled water is a pure compound. Air, sea water and salt solution are mixtures.

A pure substance melts or boils at a definite temperature. Pure ice, for example, melts at $0^\circ\mathrm{C}$ under standard conditions, and the temperature stays steady while it melts. If salt is dissolved in the water, melting starts at a lower temperature and happens over a range.

Compare a measured melting or boiling point with a reliable data value. If the temperature does not match, or the range is wide, the sample is probably impure. This is especially useful for identifying solids in the laboratory.

## Worked example

A data book gives a solid’s melting point as $80^\circ\mathrm{C}$. A sample starts melting at $74^\circ\mathrm{C}$ and only finishes at $79^\circ\mathrm{C}$. What does this suggest?

**Solution:** The melting point is lower than expected and the range is wide, so the sample is likely to contain impurities and is not pure.""",
    diff_zh="""- **把“看起来干净”当成纯。** 澄清的盐水仍是混合物。
- **以为杂质一定提高熔点。** 常见情况是熔点降低、熔程变宽。
- **把化合物当成混合物。** 化合物如水、二氧化碳是纯净物（只含一种物质），尽管它们由不同元素组成。""",
    diff_en="""- **Treating “looks clean” as pure.** Clear salt water is still a mixture.
- **Assuming impurities always raise the melting point.** They usually lower it and widen the range.
- **Calling a compound a mixture.** A compound such as water or carbon dioxide is a pure substance (one substance), even though it contains more than one element.""",
    questions=[
        dict(type="mcq", stem_zh="下列哪一项是纯净物？", stem_en="Which of the following is a pure substance?",
             answer="c", exp_zh="蒸馏水只含一种化合物。空气、海水和盐水都是混合物。", exp_en="Distilled water is a single compound. Air, sea water and salt solution are mixtures.",
             options=opts(("空气", "air"), ("海水", "sea water"), ("蒸馏水", "distilled water"), ("盐水", "salt solution"))),
        dict(type="mcq", stem_zh="纯净物在熔化时，温度通常怎样？", stem_en="While a pure substance melts, its temperature usually:",
             answer="a", exp_zh="纯净物有尖锐、固定的熔点，熔化过程中温度保持在该值附近。", exp_en="A pure substance has a sharp, fixed melting point, so the temperature stays at that value while it melts.",
             options=opts(("保持在一个固定的熔点", "stays at a fixed melting point"),
                          ("一直均匀上升，没有平台", "rises steadily with no plateau"),
                          ("一定会先升高再降低", "must rise and then fall"),
                          ("无法测定", "cannot be measured"))),
        dict(type="mcq", stem_zh="杂质对固体熔点的典型影响是？", stem_en="A typical effect of impurities on the melting point of a solid is to:",
             answer="b", exp_zh="杂质通常使熔点降低，并且熔化发生在一段温度范围内。", exp_en="Impurities usually lower the melting point and make melting happen over a range.",
             options=opts(("使熔点升高且更加尖锐", "raise it and make it sharper"),
                          ("使熔点降低且熔程变宽", "lower it and widen the melting range"),
                          ("对熔点没有任何影响", "have no effect at all"),
                          ("使固体无法再熔化", "stop the solid melting at all"))),
        dict(type="short", stem_zh="为什么测定熔点并与数据手册比较，可以帮助判断样品是否纯？", stem_en="Why can measuring a melting point and comparing it with a data-book value help you judge purity?",
             answer="pure substances have a sharp fixed melting point",
             accepted=["pure substances have a sharp fixed melting point", "impurities lower and widen the melting point",
                       "纯净物有固定尖锐的熔点，对不上或熔程宽说明可能不纯", "熔点偏低或熔程宽说明可能有杂质"],
             answer_zh="纯净物有固定而尖锐的熔点；若测值对不上或熔程较宽，样品可能不纯。",
             answer_en="A pure substance has a sharp, fixed melting point; a mismatch or a wide range suggests the sample is impure.",
             exp_zh="把实验值与可靠数据比较，是实验室常用的纯度证据。", exp_en="Comparing the experimental value with a reliable data value is common laboratory evidence of purity."),
        dict(type="mcq", stem_zh="澄清的糖水是纯净物吗？", stem_en="Is a clear sugar solution a pure substance?",
             answer="d", exp_zh="看起来澄清仍是水和糖的混合物，组成可以改变。", exp_en="It may look clear, but it is a mixture of water and sugar, and the composition can vary.",
             options=opts(("是，因为看起来透明", "yes, because it looks transparent"),
                          ("是，因为糖是化合物", "yes, because sugar is a compound"),
                          ("是，因为它能导电", "yes, because it can conduct electricity"),
                          ("不是，它是混合物", "no, it is a mixture"))),
        dict(type="mcq", stem_zh="二氧化碳（$\mathrm{CO_2}$）是一种化合物。它属于？", stem_en="Carbon dioxide ($\mathrm{CO_2}$) is a compound. It is:",
             answer="a", exp_zh="化合物是一种物质，属于纯净物；混合物至少含两种物质。", exp_en="A compound is one substance, so it is pure; a mixture contains two or more substances.",
             options=opts(("纯净物", "a pure substance"), ("混合物，因为含有两种元素", "a mixture, because it contains two elements"),
                          ("一定不纯，因为是气体", "impure by definition because it is a gas"),
                          ("既不是纯净物也不是混合物", "neither pure nor a mixture"))),
    ],
)

# ----- 8Cp.01 -----
L(
    id="chemistry-8Cp-1",
    title_zh="溶液的浓度", title_en="Concentration of a solution",
    obj_zh="本节你将学会说明浓度的含义，并用溶质质量除以溶液体积进行简单计算。",
    obj_en="This lesson you will explain what concentration means and calculate it from the mass of solute and the volume of solution.",
    kp_zh="""- **溶液**由**溶质**溶解在**溶剂**中形成。
- **浓度**表示一定体积溶液里溶质的多少。
- 常用单位：$\mathrm{g/dm^3}$（每立方分米克）。$1\ \mathrm{dm^3}=1000\ \mathrm{cm^3}=1\ \mathrm{L}$。
- 计算公式：$\text{concentration}=\dfrac{\text{mass of solute}}{\text{volume of solution}}$。
- 同样质量的溶质，体积越大，浓度越低。""",
    kp_en="""- A **solution** is formed when a **solute** dissolves in a **solvent**.
- **Concentration** tells you how much solute is in a given volume of solution.
- A common unit is $\mathrm{g/dm^3}$ (grams per cubic decimetre). $1\ \mathrm{dm^3}=1000\ \mathrm{cm^3}=1\ \mathrm{L}$.
- Use $\text{concentration}=\dfrac{\text{mass of solute}}{\text{volume of solution}}$.
- For the same mass of solute, a larger volume means a lower concentration.""",
    body_zh=r"""一杯糖水可以很“甜”，也可以很淡。差别不在杯子大小本身，而在**同样体积里溶解了多少糖**。这就是浓度。

计算时要把单位配套。若质量用克，体积用立方分米，浓度就是 $\mathrm{g/dm^3}$。如果体积以立方厘米给出，先除以 $1000$ 换成 $\mathrm{dm^3}$。

$$\text{concentration}=\frac{\text{mass of solute}}{\text{volume of solution}}$$

## 例题 1

$8\ \mathrm{g}$ 盐溶解后配成 $0.50\ \mathrm{dm^3}$ 溶液。浓度是多少 $\mathrm{g/dm^3}$？

$$\frac{8}{0.50}=16\ \mathrm{g/dm^3}.$$

## 例题 2

$12\ \mathrm{g}$ 溶质配成 $250\ \mathrm{cm^3}$ 溶液。浓度是多少 $\mathrm{g/dm^3}$？

先换单位：$250\ \mathrm{cm^3}=0.250\ \mathrm{dm^3}$，所以浓度是 $12/0.250=48\ \mathrm{g/dm^3}$。若忘记换单位，直接除以 $250$，答案会差一千倍。""",
    body_en=r"""A sugar solution can taste strong or weak. The difference is not the size of the cup by itself, but **how much sugar is dissolved in a given volume**. That is concentration.

Keep the units consistent. If mass is in grams and volume is in cubic decimetres, concentration is in $\mathrm{g/dm^3}$. If the volume is given in cubic centimetres, divide by $1000$ first to convert to $\mathrm{dm^3}$.

$$\text{concentration}=\frac{\text{mass of solute}}{\text{volume of solution}}$$

## Worked example 1

$8\ \mathrm{g}$ of salt is dissolved to make $0.50\ \mathrm{dm^3}$ of solution. What is the concentration in $\mathrm{g/dm^3}$?

$$\frac{8}{0.50}=16\ \mathrm{g/dm^3}.$$

## Worked example 2

$12\ \mathrm{g}$ of solute is made up to $250\ \mathrm{cm^3}$ of solution. What is the concentration in $\mathrm{g/dm^3}$?

Convert units first: $250\ \mathrm{cm^3}=0.250\ \mathrm{dm^3}$, so the concentration is $12/0.250=48\ \mathrm{g/dm^3}$. If you forget to convert and divide by $250$, the answer is a thousand times too small.""",
    diff_zh="""- **体积单位没换算。** $250\ \mathrm{cm^3}$ 不是 $250\ \mathrm{dm^3}$。
- **把溶剂体积当成溶液体积。** 题目若给出配成的溶液总体积，就用溶液体积。
- **以为加水后溶质质量也变。** 加水使体积变大、浓度变小，溶质质量不变。""",
    diff_en="""- **Forgetting the volume conversion.** $250\ \mathrm{cm^3}$ is not $250\ \mathrm{dm^3}$.
- **Using the solvent volume when the question gives the volume of solution.** Use the volume of solution after it has been made up.
- **Thinking the mass of solute changes when you add water.** Adding water increases the volume and lowers the concentration; the mass of solute stays the same.""",
    diagram=D_CONC,
    questions=[
        dict(type="numeric", stem_zh="$8\\ \\mathrm{g}$ 盐配成 $0.50\\ \\mathrm{dm^3}$ 溶液。浓度是多少 $\\mathrm{g/dm^3}$？",
             stem_en="$8\\ \\mathrm{g}$ of salt is made up to $0.50\\ \\mathrm{dm^3}$ of solution. What is the concentration in $\\mathrm{g/dm^3}$?",
             answer=16, exp_zh="$8/0.50=16\\ \\mathrm{g/dm^3}$。", exp_en="$8/0.50=16\\ \\mathrm{g/dm^3}$.", tolerance=0),
        dict(type="numeric", stem_zh="$12\\ \\mathrm{g}$ 溶质配成 $250\\ \\mathrm{cm^3}$ 溶液。浓度是多少 $\\mathrm{g/dm^3}$？",
             stem_en="$12\\ \\mathrm{g}$ of solute is made up to $250\\ \\mathrm{cm^3}$ of solution. Concentration in $\\mathrm{g/dm^3}$?",
             answer=48, exp_zh="$250\\ \\mathrm{cm^3}=0.250\\ \\mathrm{dm^3}$，$12/0.250=48$。", exp_en="$250\\ \\mathrm{cm^3}=0.250\\ \\mathrm{dm^3}$, so $12/0.250=48$.", tolerance=0),
        dict(type="mcq", stem_zh="同样质量的溶质，加水使溶液体积变大后，浓度会怎样？", stem_en="If you add water so that the volume of a solution increases, but the mass of solute stays the same, the concentration:",
             answer="b", exp_zh="溶质质量不变、体积变大，浓度降低。", exp_en="The mass of solute is unchanged and the volume is larger, so the concentration falls.",
             options=opts(("升高", "increases"), ("降低", "decreases"), ("一定不变", "must stay the same"), ("先升高后降低", "rises then falls"))),
        dict(type="mcq", stem_zh="$1\\ \\mathrm{dm^3}$ 等于多少 $\\mathrm{cm^3}$？", stem_en="$1\\ \\mathrm{dm^3}$ is equal to how many $\\mathrm{cm^3}$?",
             answer="c", exp_zh="$1\\ \\mathrm{dm^3}=1000\\ \\mathrm{cm^3}=1\\ \\mathrm{L}$。", exp_en="$1\\ \\mathrm{dm^3}=1000\\ \\mathrm{cm^3}=1\\ \\mathrm{L}$.",
             options=opts(("$10$", "$10$"), ("$100$", "$100$"), ("$1000$", "$1000$"), ("$1$", "$1$"))),
        dict(type="numeric", stem_zh="浓度为 $20\\ \\mathrm{g/dm^3}$ 的溶液有 $0.40\\ \\mathrm{dm^3}$。其中溶质质量是多少克？",
             stem_en="A solution has concentration $20\\ \\mathrm{g/dm^3}$ and volume $0.40\\ \\mathrm{dm^3}$. What is the mass of solute in grams?",
             answer=8, exp_zh="质量 $=$ 浓度 $\\times$ 体积 $=20\\times 0.40=8\\ \\mathrm{g}$。", exp_en="Mass $=$ concentration $\\times$ volume $=20\\times 0.40=8\\ \\mathrm{g}$.", tolerance=0),
        dict(type="short", stem_zh="写出用溶质质量和溶液体积计算浓度的公式。", stem_en="Write the formula for concentration in terms of mass of solute and volume of solution.",
             answer="mass/volume", accepted=["mass/volume", "mass / volume", "c=m/v", "C=m/V", "concentration = mass/volume",
                                            "浓度=质量/体积", "浓度＝溶质质量/溶液体积", "m/v"],
             answer_zh="浓度 $=$ 溶质质量 $/$ 溶液体积。", answer_en="concentration $=$ mass of solute $/$ volume of solution.",
             exp_zh="单位要配套，例如 $\\mathrm{g}$ 与 $\\mathrm{dm^3}$。", exp_en="Keep units consistent, for example $\\mathrm{g}$ and $\\mathrm{dm^3}$."),
    ],
)

# ----- 8Cp.02 -----
L(
    id="chemistry-8Cp-2",
    title_zh="纸层析法", title_en="Paper chromatography",
    obj_zh="本节你将学会说明纸层析如何分离混合物，并计算、解释 $R_f$ 值。",
    obj_en="This lesson you will explain how paper chromatography separates a mixture, and calculate and interpret $R_f$ values.",
    kp_zh="""- 纸层析可把混合物中的不同溶解成分分开。
- 样品点在**起点线**上，起点线要在溶剂液面**上方**；用铅笔而不是钢笔划线。
- 溶剂沿滤纸上升，不同成分上升的距离往往不同。
- $$R_f=\dfrac{\text{斑点移动的距离}}{\text{溶剂移动的距离}}$$，数值在 $0$ 与 $1$ 之间。
- 把未知斑点的 $R_f$ 与已知纯物质在**同一条件下**比较，可帮助鉴定。""",
    kp_en="""- Paper chromatography can separate dissolved substances in a mixture.
- Spot the sample on a **baseline** that stays **above** the solvent; draw the line in pencil, not ink.
- The solvent rises up the paper and different substances often travel different distances.
- $$R_f=\dfrac{\text{distance travelled by the spot}}{\text{distance travelled by the solvent}}$$, a value between $0$ and $1$.
- Compare an unknown $R_f$ with a known pure substance under the **same conditions** to help identify it.""",
    body_zh=r"""纸层析利用的是：不同物质在流动的溶剂和静止的滤纸之间“分配”的程度不同，所以走得有快有慢。

操作要点：起点线用铅笔画，因为石墨不会溶于常见溶剂；若用钢笔，墨水自己也会上升，把结果弄乱。样品点要在液面上方，否则固体还没随溶剂展开就被直接溶解冲走。

实验结束时，量出溶剂前沿到起点线的距离，以及每个斑点中心到起点线的距离：

$$R_f=\frac{d_{\text{spot}}}{d_{\text{solvent}}}$$

$R_f$ 没有单位，不能大于 $1$（斑点不能超过溶剂前沿）。同一物质在相同溶剂、相同温度下 $R_f$ 应相近，因此可与标准样品对照。

## 例题

溶剂前沿距起点线 $6.0\ \mathrm{cm}$，某斑点距起点线 $4.8\ \mathrm{cm}$。$R_f$ 是多少？

$$R_f=4.8/6.0=0.80.$$""",
    body_en=r"""Paper chromatography works because different substances are shared differently between the moving solvent and the stationary paper, so they travel at different speeds.

Practical points: draw the baseline in pencil, because graphite does not dissolve in the usual solvents. Ink from a pen would travel too and spoil the result. Keep the spots above the solvent surface, or the sample dissolves straight into the beaker instead of moving up the paper.

At the end, measure the distance from the baseline to the solvent front, and from the baseline to the centre of each spot:

$$R_f=\frac{d_{\text{spot}}}{d_{\text{solvent}}}$$

$R_f$ has no unit and cannot be greater than $1$ (a spot cannot overtake the solvent front). The same substance should give a similar $R_f$ in the same solvent at the same temperature, so you can compare it with a standard.

## Worked example

The solvent front is $6.0\ \mathrm{cm}$ from the baseline and a spot is $4.8\ \mathrm{cm}$ from the baseline. What is $R_f$?

$$R_f=4.8/6.0=0.80.$$""",
    diff_zh="""- **把 $R_f$ 写成溶剂距离除以斑点距离。** 分子是斑点距离。
- **起点线浸入溶剂。** 样品会被洗掉。
- **用钢笔划线。** 墨水会一起展开。
- **在不同溶剂下直接比较 $R_f$。** 条件必须相同。""",
    diff_en="""- **Writing $R_f$ as solvent distance divided by spot distance.** The spot distance is the numerator.
- **Letting the baseline sit in the solvent.** The sample washes off.
- **Drawing the line in ink.** The ink travels as well.
- **Comparing $R_f$ values from different solvents.** Conditions must be the same.""",
    diagram=D_CHROM,
    questions=[
        dict(type="numeric", stem_zh="溶剂前沿距起点线 $6.0\\ \\mathrm{cm}$，斑点距起点线 $4.8\\ \\mathrm{cm}$。$R_f$ 是多少？",
             stem_en="The solvent front is $6.0\\ \\mathrm{cm}$ from the baseline and a spot is $4.8\\ \\mathrm{cm}$ from the baseline. What is $R_f$?",
             answer=0.8, exp_zh="$4.8/6.0=0.80$。", exp_en="$4.8/6.0=0.80$.", tolerance=0.01),
        dict(type="mcq", stem_zh="起点线为什么要用铅笔而不是钢笔？", stem_en="Why should the baseline be drawn in pencil rather than pen?",
             answer="a", exp_zh="石墨不溶于常见溶剂；墨水会随溶剂上升，干扰结果。", exp_en="Graphite does not dissolve in the usual solvents; ink would travel and interfere.",
             options=opts(("铅笔痕迹不会随溶剂上升，墨水会", "pencil will not travel with the solvent, but ink will"),
                          ("铅笔比钢笔更细，所以 $R_f$ 一定是 $1$", "pencil is thinner, so $R_f$ must be $1$"),
                          ("钢笔会使滤纸带电", "pen ink charges the paper"),
                          ("规定不能用黑色", "the rules ban the colour black"))),
        dict(type="mcq", stem_zh="起点线如果浸在溶剂里，主要问题是？", stem_en="If the baseline sits in the solvent, the main problem is that:",
             answer="c", exp_zh="样品会直接溶解到溶剂中，无法在纸上正常展开。", exp_en="The sample dissolves into the solvent and does not travel properly up the paper.",
             options=opts(("$R_f$ 会永远等于 $1$", "$R_f$ will always equal $1$"),
                          ("溶剂无法上升", "the solvent cannot rise"),
                          ("样品会被洗进溶剂里", "the sample washes into the solvent"),
                          ("滤纸会立刻变成纯净物", "the paper instantly becomes a pure substance"))),
        dict(type="mcq", stem_zh="某样品展开后出现两个斑点。这说明什么？", stem_en="A sample produces two spots. This suggests that:",
             answer="b", exp_zh="样品含有至少两种能被该溶剂分开的成分，因此是混合物。", exp_en="The sample contains at least two substances that the solvent can separate, so it is a mixture.",
             options=opts(("样品一定是一种元素", "the sample must be an element"),
                          ("样品是含有至少两种成分的混合物", "the sample is a mixture of at least two substances"),
                          ("实验一定失败了", "the experiment must have failed"),
                          ("$R_f$ 一定大于 $1$", "$R_f$ must be greater than $1$"))),
        dict(type="numeric", stem_zh="溶剂移动了 $10.0\\ \\mathrm{cm}$，斑点移动了 $3.5\\ \\mathrm{cm}$。$R_f$ 是多少？",
             stem_en="The solvent travels $10.0\\ \\mathrm{cm}$ and a spot travels $3.5\\ \\mathrm{cm}$. What is $R_f$?",
             answer=0.35, exp_zh="$3.5/10.0=0.35$。", exp_en="$3.5/10.0=0.35$.", tolerance=0.01),
        dict(type="mcq", stem_zh="下列关于 $R_f$ 的说法正确的是？", stem_en="Which statement about $R_f$ is correct?",
             answer="d", exp_zh="$R_f$ 在 $0$ 与 $1$ 之间，且只有在相同条件下才宜与标准样品比较。", exp_en="$R_f$ lies between $0$ and $1$, and should be compared with a standard only under the same conditions.",
             options=opts(("$R_f$ 可以大于 $1$", "$R_f$ can be greater than $1$"),
                          ("不同溶剂中 $R_f$ 一定相同", "$R_f$ is always the same in every solvent"),
                          ("$R_f$ 的单位是厘米", "$R_f$ is measured in centimetres"),
                          ("$R_f$ 介于 $0$ 与 $1$ 之间，比较时条件要相同", "$R_f$ is between $0$ and $1$, and conditions must match when you compare"))),
    ],
)

# ----- 8Cc.01 -----
L(
    id="chemistry-8Cc-1",
    title_zh="用文字方程式描述反应", title_en="Using word equations to describe reactions",
    obj_zh="本节你将学会用文字方程式写出反应物和生成物，并说明箭头表示什么。",
    obj_en="This lesson you will write word equations that show reactants and products, and explain what the arrow means.",
    kp_zh="""- **反应物**在箭头左边，**生成物**在箭头右边。
- 箭头表示“反应生成”，不是普通等号；物质在反应中重新组合成新物质。
- 有两种或更多物质时，用 $+$ 连接。
- 文字方程式用物质名称，不写化学式（本阶段先掌握文字式）。
- 例如：镁 $+$ 氧气 $\\rightarrow$ 氧化镁。""",
    kp_en="""- **Reactants** are on the left of the arrow; **products** are on the right.
- The arrow means “react to form”, not an ordinary equals sign; atoms are rearranged into new substances.
- Use $+$ when there are two or more substances on a side.
- A word equation uses names, not formulae, at this stage.
- For example: magnesium $+$ oxygen $\\rightarrow$ magnesium oxide.""",
    body_zh=r"""化学反应会生成与原来不同的物质。文字方程式是用名称把这件事写清楚的方法。

格式是：

$$\text{reactant(s)}\rightarrow\text{product(s)}$$

左边是加入反应、将被改变的物质，右边是新生成的物质。加号只表示“和”，不表示算术相加。箭头也不表示两边质量数字已经配平到化学式层面——本阶段先把名称和方向写对。

燃烧、金属与氧气、酸与金属等都可以这样写。例如碳在氧气中完全燃烧：

碳 $+$ 氧气 $\rightarrow$ 二氧化碳。

## 例题

氢气在氧气中燃烧生成水。写出文字方程式。

**解：** 氢 $+$ 氧 $\rightarrow$ 水（或氢气 $+$ 氧气 $\rightarrow$ 水）。不要把水写在左边。""",
    body_en=r"""A chemical reaction makes new substances that are different from the starting materials. A word equation records this with names.

The pattern is:

$$\text{reactant(s)}\rightarrow\text{product(s)}$$

The left-hand side lists the substances that take part and are changed. The right-hand side lists the new substances formed. A plus sign only means “and”; it is not an arithmetic plus. The arrow also does not mean that formulae have already been balanced — at this stage, get the names and the direction right.

Combustion, metals with oxygen, and metals with acids can all be written this way. For complete combustion of carbon in oxygen:

carbon $+$ oxygen $\rightarrow$ carbon dioxide.

## Worked example

Hydrogen burns in oxygen to form water. Write the word equation.

**Solution:** hydrogen $+$ oxygen $\rightarrow$ water. Do not put water on the left.""",
    diff_zh="""- **把生成物写在左边。** 箭头指向生成物。
- **用等号代替箭头。** 课堂规范用箭头表示反应。
- **漏写某一种反应物或生成物。** 先根据文字描述列出所有名称再写。""",
    diff_en="""- **Putting products on the left.** The arrow points towards the products.
- **Using an equals sign instead of an arrow.** The classroom convention is an arrow.
- **Missing a reactant or a product.** List every name from the description before you write the equation.""",
    questions=[
        dict(type="mcq", stem_zh="文字方程式中，箭头右边写的是？", stem_en="In a word equation, the right-hand side of the arrow shows the:",
             answer="b", exp_zh="右边是生成物，左边是反应物。", exp_en="Products are on the right; reactants are on the left.",
             options=opts(("反应物", "reactants"), ("生成物", "products"), ("催化剂只有名称", "catalysts only"), ("溶剂", "the solvent"))),
        dict(type="short", stem_zh="写出：镁在氧气中燃烧生成氧化镁。", stem_en="Write the word equation: magnesium burns in oxygen to form magnesium oxide.",
             answer="magnesium + oxygen -> magnesium oxide",
             accepted=["magnesium + oxygen -> magnesium oxide", "magnesium + oxygen → magnesium oxide",
                       "镁+氧气→氧化镁", "镁＋氧→氧化镁", "镁 + 氧气 → 氧化镁"],
             answer_zh="镁 $+$ 氧气 $\\rightarrow$ 氧化镁", answer_en="magnesium $+$ oxygen $\\rightarrow$ magnesium oxide",
             exp_zh="反应物在左：镁和氧气；生成物在右：氧化镁。", exp_en="Reactants on the left: magnesium and oxygen; product on the right: magnesium oxide."),
        dict(type="mcq", stem_zh="碳完全燃烧生成二氧化碳。正确的文字方程式是？", stem_en="Carbon burns completely to form carbon dioxide. Which word equation is correct?",
             answer="a", exp_zh="碳和氧气是反应物，二氧化碳是生成物。", exp_en="Carbon and oxygen are the reactants; carbon dioxide is the product.",
             options=opts(("碳 $+$ 氧气 $\\rightarrow$ 二氧化碳", "carbon $+$ oxygen $\\rightarrow$ carbon dioxide"),
                          ("二氧化碳 $\\rightarrow$ 碳 $+$ 氧气", "carbon dioxide $\\rightarrow$ carbon $+$ oxygen"),
                          ("碳 $\\rightarrow$ 氧气 $+$ 二氧化碳", "carbon $\\rightarrow$ oxygen $+$ carbon dioxide"),
                          ("氧气 $\\rightarrow$ 碳", "oxygen $\\rightarrow$ carbon"))),
        dict(type="mcq", stem_zh="文字方程式里的 $+$ 表示什么？", stem_en="In a word equation, $+$ means:",
             answer="c", exp_zh="它表示“和”，把同一边的几种物质连起来，不是把质量数字相加。", exp_en="It means “and”, joining substances on the same side; it is not adding mass numbers.",
             options=opts(("两边质量已经配平到化学式", "the formulae are already balanced"),
                          ("温度一定升高", "the temperature must rise"),
                          ("“和”，连接同一边的物质", "“and”, joining substances on the same side"),
                          ("反应停止", "the reaction has stopped"))),
        dict(type="short", stem_zh="氢气在氧气中燃烧生成水。写出文字方程式。", stem_en="Hydrogen burns in oxygen to form water. Write the word equation.",
             answer="hydrogen + oxygen -> water",
             accepted=["hydrogen + oxygen -> water", "hydrogen + oxygen → water", "氢气+氧气→水", "氢＋氧→水", "氢气 + 氧气 → 水"],
             answer_zh="氢气 $+$ 氧气 $\\rightarrow$ 水", answer_en="hydrogen $+$ oxygen $\\rightarrow$ water",
             exp_zh="不要把水写在箭头左边。", exp_en="Do not put water on the left of the arrow."),
        dict(type="mcq", stem_zh="下列说法正确的是？", stem_en="Which statement is correct?",
             answer="d", exp_zh="化学反应中原子重新组合成新物质；文字方程式用名称记录这一过程。", exp_en="In a chemical reaction, atoms are rearranged into new substances; a word equation records this with names.",
             options=opts(("文字方程式的箭头可以随意反向，意义不变", "you can reverse the arrow with no change of meaning"),
                          ("反应物就是新生成的物质", "reactants are the new substances formed"),
                          ("文字方程式必须写出电子电荷", "a word equation must show electron charges"),
                          ("反应物变成新的生成物，用箭头表示这个方向", "reactants form new products; the arrow shows that direction"))),
    ],
)

# ----- 8Cc.02 -----
L(
    id="chemistry-8Cc-2",
    title_zh="放热与吸热过程", title_en="Exothermic and endothermic processes",
    obj_zh="本节你将学会区分放热过程和吸热过程，并能根据温度变化作出判断。",
    obj_en="This lesson you will distinguish exothermic and endothermic processes and use temperature change as evidence.",
    kp_zh="""- **放热**过程向周围释放能量，周围温度通常**升高**。
- **吸热**过程从周围吸收能量，周围温度通常**降低**。
- 燃烧是常见的放热反应；许多热分解反应是吸热的。
- 可用温度计测量反应前后周围（或混合物）的温度变化作为证据。
- 能量守恒：放出的能量来自化学能储存的变化，不是凭空产生。""",
    kp_en="""- An **exothermic** process transfers energy to the surroundings, so the temperature of the surroundings usually **rises**.
- An **endothermic** process takes in energy from the surroundings, so the temperature usually **falls**.
- Combustion is a common exothermic reaction; many thermal decompositions are endothermic.
- A thermometer reading before and after is evidence of the temperature change of the surroundings (or the mixture).
- Energy is conserved: energy released comes from a change in chemical stores, not from nowhere.""",
    body_zh=r"""判断放热还是吸热，关键看**能量往哪边走**，以及周围的温度如何变化。

如果反应把能量释放给周围，周围变得更热，这是放热。燃料燃烧、许多金属与酸的反应都是例子。如果反应从周围吸收能量，周围变得更冷，这是吸热。例如某些盐溶解时烧杯变凉，或需要持续加热才能分解的反应。

示意图上，放热过程中生成物的能量储存低于反应物；吸热则相反。本阶段先会看温度证据，不必计算能量数值。

## 例题

把镁条放入稀酸，温度从 $21^\circ\mathrm{C}$ 升到 $28^\circ\mathrm{C}$。这是放热还是吸热？

**解：** 周围（混合物）温度升高，能量被释放出来，所以是放热。""",
    body_en=r"""To decide whether a change is exothermic or endothermic, ask **which way energy is transferred**, and what happens to the temperature of the surroundings.

If the change releases energy to the surroundings, they get hotter: the change is exothermic. Burning a fuel, and many reactions of metals with acids, are examples. If the change takes in energy, the surroundings get colder: the change is endothermic. Some salts do this when they dissolve, and some decompositions need a continuous supply of heat.

On a simple energy diagram, products of an exothermic change have a lower energy store than the reactants; the opposite is true for an endothermic change. At this stage, use temperature evidence; you do not need to calculate energy values.

## Worked example

Magnesium is added to dilute acid and the temperature rises from $21^\circ\mathrm{C}$ to $28^\circ\mathrm{C}$. Is this exothermic or endothermic?

**Solution:** The temperature of the surroundings (the mixture) rises, so energy has been released. The reaction is exothermic.""",
    diff_zh="""- **只看“需要点火”就说是吸热。** 燃烧常常要先点燃，一旦开始却是放热的。
- **把体系和周围说反。** 放热是体系向周围放能，周围升温。
- **以为吸热就是没有能量变化。** 吸热同样有能量转移，只是方向相反。""",
    diff_en="""- **Calling every reaction that needs a flame endothermic.** Combustion often needs lighting, but once started it is exothermic.
- **Swapping the system and the surroundings.** Exothermic means energy is transferred to the surroundings, which warm up.
- **Thinking endothermic means “no energy change”.** Energy is still transferred, but in the opposite direction.""",
    diagram=D_ENERGY,
    questions=[
        dict(type="mcq", stem_zh="放热过程中，周围的温度通常？", stem_en="In an exothermic process, the temperature of the surroundings usually:",
             answer="a", exp_zh="放热向周围释放能量，周围温度升高。", exp_en="Energy is released to the surroundings, so their temperature rises.",
             options=opts(("升高", "rises"), ("降低", "falls"), ("一定保持 $0^\\circ\\mathrm{C}$", "must stay at $0^\\circ\\mathrm{C}$"), ("无法判断", "cannot be judged"))),
        dict(type="mcq", stem_zh="某盐溶于水后烧杯外壁变凉。这个过程是？", stem_en="A salt dissolves in water and the outside of the beaker feels colder. The process is:",
             answer="b", exp_zh="周围温度降低，说明过程从周围吸能，是吸热。", exp_en="The surroundings get colder, so the process takes in energy: it is endothermic.",
             options=opts(("放热", "exothermic"), ("吸热", "endothermic"), ("没有能量转移", "there is no energy transfer"), ("一定是燃烧", "it must be combustion"))),
        dict(type="mcq", stem_zh="燃烧蜡烛，最合适的分类是？", stem_en="Burning a candle is best classified as:",
             answer="c", exp_zh="燃烧向周围释放能量（光和热），是放热反应。", exp_en="Combustion releases energy (light and heat) to the surroundings, so it is exothermic.",
             options=opts(("吸热，因为先要点火", "endothermic, because it has to be lit"),
                          ("既不放热也不吸热", "neither exothermic nor endothermic"),
                          ("放热", "exothermic"),
                          ("只在真空中放热", "exothermic only in a vacuum"))),
        dict(type="short", stem_zh="温度从 $21^\\circ\\mathrm{C}$ 升到 $28^\\circ\\mathrm{C}$ 的反应，应称为放热还是吸热？", stem_en="A reaction whose mixture rises from $21^\\circ\\mathrm{C}$ to $28^\\circ\\mathrm{C}$ is exothermic or endothermic?",
             answer="exothermic", accepted=["exothermic", "放热", "放热反应", "exothermic reaction"],
             answer_zh="放热", answer_en="exothermic",
             exp_zh="混合物（周围）温度升高，说明能量被释放。", exp_en="The temperature of the mixture (surroundings) rose, so energy was released."),
        dict(type="mcq", stem_zh="许多热分解反应需要持续加热才能进行。它们通常是？", stem_en="Many thermal decompositions need a continuous supply of heat. They are usually:",
             answer="d", exp_zh="需要不断从周围吸收能量，通常是吸热过程。", exp_en="They take in energy from the surroundings, so they are usually endothermic.",
             options=opts(("放热，因为很热", "exothermic, because they are hot"),
                          ("与能量无关", "unrelated to energy"),
                          ("一定是混合物在熔化", "always a mixture melting"),
                          ("吸热", "endothermic"))),
        dict(type="mcq", stem_zh="关于放热与吸热，正确的是？", stem_en="Which statement is correct?",
             answer="a", exp_zh="两者都有能量转移，只是方向不同；可用温度变化作为证据。", exp_en="Both involve energy transfer, but in opposite directions; temperature change is evidence.",
             options=opts(("两者都有能量转移，方向相反", "both involve energy transfer, in opposite directions"),
                          ("只有放热才遵守能量观念", "only exothermic changes involve energy"),
                          ("吸热过程中周围一定会沸腾", "the surroundings must boil in an endothermic change"),
                          ("温度计不能作为证据", "a thermometer cannot provide evidence"))),
    ],
)

# ----- 8Cc.03 -----
L(
    id="chemistry-8Cc-3",
    title_zh="金属的反应性", title_en="Reactivity of metals",
    obj_zh="本节你将学会比较常见金属的反应性，并用反应性解释置换现象。",
    obj_en="This lesson you will compare the reactivity of common metals and use the reactivity series to explain displacement.",
    kp_zh="""- 金属的反应性不同：有的很容易与水、酸或氧气反应，有的很难。
- 一条常用（由高到低）的顺序是：钾、钠、钙、镁、铝、锌、铁、铜、银、金。
- 更活泼的金属可以把不那么活泼的金属从它的化合物溶液中**置换**出来。
- 铜、银、金与稀酸或冷水通常很难反应，所以常出现在自然界或用于管道、首饰。
- 观察气泡快慢、温度升高程度，可比较与酸反应的剧烈程度。""",
    kp_en="""- Metals differ in reactivity: some react readily with water, acid or oxygen; others barely react.
- A useful order, from more to less reactive, is: potassium, sodium, calcium, magnesium, aluminium, zinc, iron, copper, silver, gold.
- A **more reactive** metal can **displace** a less reactive metal from a solution of its compound.
- Copper, silver and gold barely react with dilute acid or cold water, so they are found native or used in pipes and jewellery.
- The speed of bubbling and the temperature rise can be used to compare reactions with acid.""",
    body_zh=r"""不是所有金属都一样“活泼”。钾、钠遇水就很剧烈；镁、锌与稀酸会较快产生氢气；铜放入稀盐酸则几乎看不到气泡。把这些观察排成一条**反应性顺序**，就可以预测反应会不会发生。

置换是检验顺序的好方法。例如把锌放入硫酸铜溶液，锌更活泼，会把铜“挤”出来，溶液蓝色变浅，并出现红棕色的铜。若把铜放入硫酸锌溶液，通常观察不到置换，因为铜不如锌活泼。

文字方程式可以写成：锌 $+$ 硫酸铜 $\rightarrow$ 硫酸锌 $+$ 铜。

## 例题

铁能不能把铜从硫酸铜溶液中置换出来？铜能不能把铁从硫酸亚铁中置换出来？

**解：** 铁比铜活泼，所以铁可以置换铜；铜不能置换铁。""",
    body_en=r"""Not all metals are equally reactive. Potassium and sodium react vigorously with water; magnesium and zinc produce hydrogen fairly quickly with dilute acid; copper in dilute hydrochloric acid shows almost no bubbling. Arranging these observations into a **reactivity series** lets you predict whether a reaction will happen.

Displacement is a good test of the order. Zinc in copper sulfate solution is more reactive than copper, so zinc displaces copper: the blue colour fades and brown copper appears. Copper in zinc sulfate usually gives no displacement, because copper is less reactive than zinc.

The word equation is: zinc $+$ copper sulfate $\rightarrow$ zinc sulfate $+$ copper.

## Worked example

Can iron displace copper from copper sulfate solution? Can copper displace iron from iron sulfate?

**Solution:** Iron is more reactive than copper, so iron can displace copper. Copper cannot displace iron.""",
    diff_zh="""- **记反顺序。** 钾、钠最活泼，金、银很不活泼。
- **以为任何金属都能置换任何其他金属。** 只有更活泼的才能置换较弱的。
- **把生锈快慢与“能否置换”完全混为一谈。** 可以用观察来比较，但要以反应性顺序为准。""",
    diff_en="""- **Reversing the order.** Potassium and sodium are high; gold and silver are low.
- **Assuming any metal can displace any other.** Only a more reactive metal displaces a less reactive one.
- **Treating rusting speed as the only rule.** Observations help, but use the reactivity series to decide displacement.""",
    questions=[
        dict(type="mcq", stem_zh="下列金属中，通常最不活泼的是？", stem_en="Which of these metals is usually the least reactive?",
             answer="d", exp_zh="金的反应性很低；钾、钠、镁都活泼得多。", exp_en="Gold is very unreactive; potassium, sodium and magnesium are much more reactive.",
             options=opts(("钾", "potassium"), ("钠", "sodium"), ("镁", "magnesium"), ("金", "gold"))),
        dict(type="mcq", stem_zh="把锌放入硫酸铜溶液，通常会观察到？", stem_en="Zinc is placed in copper sulfate solution. You would usually observe:",
             answer="a", exp_zh="锌比铜活泼，置换出铜，可能看到红棕色固体，蓝色变浅。", exp_en="Zinc is more reactive than copper, so copper is displaced: brown solid may appear and the blue colour fades.",
             options=opts(("出现铜，溶液蓝色变浅", "copper appears and the blue colour fades"),
                          ("锌立刻变成金", "zinc instantly turns into gold"),
                          ("完全没有任何变化，因为锌不活泼", "no change at all, because zinc is unreactive"),
                          ("铜把锌置换出来", "copper displaces zinc"))),
        dict(type="mcq", stem_zh="铜放入硫酸锌溶液，最可能的结果是？", stem_en="Copper is placed in zinc sulfate solution. The most likely result is:",
             answer="c", exp_zh="铜不如锌活泼，不能置换锌，通常无明显反应。", exp_en="Copper is less reactive than zinc, so it cannot displace zinc; there is usually no reaction.",
             options=opts(("迅速置换出锌", "zinc is displaced rapidly"),
                          ("生成大量氢气", "a large volume of hydrogen is produced"),
                          ("没有置换反应", "no displacement reaction"),
                          ("铜变成钾", "copper turns into potassium"))),
        dict(type="short", stem_zh="写出锌与硫酸铜反应的文字方程式。", stem_en="Write the word equation for zinc reacting with copper sulfate.",
             answer="zinc + copper sulfate -> zinc sulfate + copper",
             accepted=["zinc + copper sulfate -> zinc sulfate + copper", "zinc + copper sulfate → zinc sulfate + copper",
                       "锌+硫酸铜→硫酸锌+铜", "锌 + 硫酸铜 → 硫酸锌 + 铜"],
             answer_zh="锌 $+$ 硫酸铜 $\\rightarrow$ 硫酸锌 $+$ 铜", answer_en="zinc $+$ copper sulfate $\\rightarrow$ zinc sulfate $+$ copper",
             exp_zh="更活泼的锌把铜置换出来。", exp_en="More reactive zinc displaces copper."),
        dict(type="mcq", stem_zh="比较金属与稀酸反应时，一个合理的观察是？", stem_en="A fair observation when comparing metals with dilute acid is:",
             answer="b", exp_zh="气泡快慢或温度升高等，可比较反应剧烈程度（控制酸的浓度和温度等条件）。", exp_en="The rate of bubbling or the temperature rise can be compared if conditions such as acid concentration and temperature are controlled.",
             options=opts(("金属的颜色决定反应性", "the colour of the metal decides reactivity"),
                          ("在相同条件下看冒泡快慢或升温多少", "compare bubbling or temperature rise under the same conditions"),
                          ("只有金会与稀酸迅速反应", "only gold reacts quickly with dilute acid"),
                          ("所有金属与酸的反应完全相同", "every metal reacts in exactly the same way with acid"))),
        dict(type="mcq", stem_zh="铁能否把铜从硫酸铜中置换出来？", stem_en="Can iron displace copper from copper sulfate?",
             answer="a", exp_zh="铁比铜活泼，可以置换铜。", exp_en="Iron is more reactive than copper, so it can displace copper.",
             options=opts(("能，因为铁比铜更活泼", "yes, because iron is more reactive than copper"),
                          ("不能，因为铁最不活泼", "no, because iron is the least reactive metal"),
                          ("能，因为铜比铁更活泼", "yes, because copper is more reactive than iron"),
                          ("不能，因为置换只发生在气体中", "no, because displacement only happens in gases"))),
    ],
)

# ----- 8Cc.04 -----
L(
    id="chemistry-8Cc-4",
    title_zh="不纯产物与惰性物质", title_en="Impure products and inert substances",
    obj_zh="本节你将学会解释为什么得到的产物可能不纯，以及惰性物质如何影响产物的量。",
    obj_en="This lesson you will explain why a product may be impure and how an inert substance affects the amount of product.",
    kp_zh="""- 实验室或工业上得到的**产物不一定纯**：可能混有未反应完的反应物、其他生成物或杂质。
- **惰性物质**在该反应条件下几乎不反应（例如某些情况下的氮气，或混在样品中的沙子）。
- 若样品里有惰性杂质，能真正参加反应的反应物就变少，**有用产物的质量会比“全部都是纯反应物”时更少**。
- 需要纯产物时，往往还要分离和提纯（过滤、结晶、蒸馏等）。
- 不要把“有杂质”和“没有发生反应”混为一谈。""",
    kp_en="""- The **product** you collect is not always pure: unreacted starting material, other products or impurities may still be mixed with it.
- An **inert substance** barely reacts under the conditions (for example nitrogen in some situations, or sand mixed into a sample).
- If a sample contains an inert impurity, less of the useful reactant can take part, so the **mass of useful product is smaller** than if the reactant had been pure.
- Extra separation and purification (filtering, crystallising, distilling) may be needed when a pure product is required.
- Do not confuse “the product is impure” with “no reaction happened”.""",
    body_zh=r"""文字方程式写的是理想情况：反应物全部按描述变成生成物。真实实验里，事情往往更乱。

可能的原因包括：反应没有进行完全，还有剩余反应物；同时发生了别的反应；或者一开始的固体里就混了不参加反应的东西。这些都会让你称到的“产物”不纯，或使纯产物偏少。

惰性物质本身不提供目标产物。例如一块“锌”里若掺了不会反应的沙子，同样质量的样品里真正的锌就更少，与酸反应产生的氢气也会更少。空气中的氮气在许多燃烧反应里也近似惰性：它不一定进入生成物，却占据了一部分气体体积。

## 例题

两份质量相同的镁条，一份更纯，一份混有不会反应的杂质。它们在充足氧气中燃烧，哪一份生成的氧化镁更多？

**解：** 更纯的那一份可反应的镁更多，因此生成的氧化镁更多。""",
    body_en=r"""A word equation describes an ideal case: the reactants named turn into the products named. In a real experiment the picture is often messier.

The reaction may be incomplete, so some reactant remains. Another reaction may happen at the same time. The starting solid may already contain something that does not react. Any of these can make the collected “product” impure, or reduce the mass of pure product.

An inert substance does not make the target product. If a sample of “zinc” is mixed with unreactive sand, there is less real zinc in the same mass of sample, so less hydrogen is made with acid. Nitrogen in air is also nearly inert in many combustions: it does not necessarily enter the product, but it occupies part of the gas volume.

## Worked example

Two magnesium ribbons have the same mass. One is purer; the other is mixed with an unreactive impurity. Both burn in plentiful oxygen. Which sample produces more magnesium oxide?

**Solution:** The purer sample contains more magnesium that can react, so it produces more magnesium oxide.""",
    diff_zh="""- **以为写出文字方程式，产物就一定纯。** 方程式不保证实验样品纯净或反应完全。
- **把惰性杂质当成会增加产物。** 它占用质量，却不生成目标产物。
- **把空气中所有气体都当成氧气。** 氮气通常不支持那样的燃烧反应。""",
    diff_en="""- **Assuming a word equation guarantees a pure product.** The equation does not guarantee a pure sample or a complete reaction.
- **Thinking an inert impurity increases the product.** It adds mass but does not make the target product.
- **Treating all of the air as oxygen.** Nitrogen does not usually take part in that kind of combustion.""",
    questions=[
        dict(type="mcq", stem_zh="惰性物质在该反应中的典型行为是？", stem_en="An inert substance in a reaction typically:",
             answer="b", exp_zh="惰性物质几乎不反应，不会变成目标产物。", exp_en="It barely reacts and does not turn into the target product.",
             options=opts(("比所有反应物都更活泼", "is more reactive than every reactant"),
                          ("几乎不反应", "barely reacts"),
                          ("一定使产物质量增加", "must increase the mass of product"),
                          ("把方程式中的箭头反过来", "reverses the arrow in the equation"))),
        dict(type="mcq", stem_zh="同样质量的锌，一份纯，一份混有沙子（不反应）。与足量稀酸反应，纯锌产生的氢气？", stem_en="Two equal masses of zinc are used with excess dilute acid. One sample is pure; the other is mixed with unreactive sand. The pure zinc produces:",
             answer="a", exp_zh="纯样品中可反应的锌更多，产生的氢气更多。", exp_en="The pure sample contains more zinc that can react, so it produces more hydrogen.",
             options=opts(("更多", "more hydrogen"), ("更少", "less hydrogen"), ("一定完全相同", "exactly the same amount"), ("为零，因为纯物质不反应", "none, because pure substances do not react"))),
        dict(type="mcq", stem_zh="收集到的固体产物熔点比数据手册更低、熔程更宽，可能说明？", stem_en="A collected solid product melts lower and over a wider range than the data-book value. This may mean:",
             answer="c", exp_zh="产物可能不纯，混有杂质或未反应物。", exp_en="The product may be impure, mixed with impurities or unreacted material.",
             options=opts(("产物一定是一种元素", "the product must be an element"),
                          ("反应完全没有发生", "no reaction occurred at all"),
                          ("产物可能含有杂质", "the product may contain impurities"),
                          ("熔点数据永远不能用于产物", "melting points can never be used for products"))),
        dict(type="short", stem_zh="为什么样品里的惰性杂质会减少有用产物的质量？", stem_en="Why does an inert impurity in a sample reduce the mass of useful product?",
             answer="less reactant can react",
             accepted=["less reactant can react", "inert impurity does not make product",
                       "可反应的反应物变少", "惰性杂质不生成目标产物", "同样质量里真正能反应的物质更少"],
             answer_zh="同样质量的样品里，能反应的物质变少，惰性杂质又不生成目标产物。",
             answer_en="There is less reactant that can react in the same mass of sample, and the inert impurity does not make the target product.",
             exp_zh="惰性成分占用质量，却不参加生成目标产物的反应。", exp_en="The inert part adds mass but does not take part in making the target product."),
        dict(type="mcq", stem_zh="空气中的氮气在许多燃烧反应里可看作？", stem_en="In many combustion reactions, nitrogen in air can be treated as:",
             answer="d", exp_zh="氮气在这些反应里往往近似惰性，不一定进入燃烧产物。", exp_en="Nitrogen is often nearly inert in these reactions and does not necessarily enter the combustion product.",
             options=opts(("最主要的燃料", "the main fuel"),
                          ("比氧气更活泼的反应物", "a more reactive reactant than oxygen"),
                          ("纯净物所以一定参加反应", "a pure substance, so it must react"),
                          ("近似惰性的气体", "a nearly inert gas"))),
        dict(type="mcq", stem_zh="若需要纯的晶体产物，实验后通常还要？", stem_en="If you need a pure crystalline product, after the reaction you often have to:",
             answer="a", exp_zh="通过过滤、结晶等步骤分离和提纯。", exp_en="Separate and purify, for example by filtering and crystallising.",
             options=opts(("分离并提纯", "separate and purify it"),
                          ("加入更多惰性沙子", "add more inert sand"),
                          ("把文字方程式的箭头反过来写", "write the word equation backwards"),
                          ("停止测量熔点，因为已经纯了", "stop checking melting points, because it must already be pure"))),
    ],
)

# ----- 8Cc.05 -----
L(
    id="chemistry-8Cc-5",
    title_zh="盐的溶解度与温度", title_en="Solubility of salts and temperature",
    obj_zh="本节你将学会描述大多数盐的溶解度如何随温度变化，并会读简单的溶解度曲线。",
    obj_en="This lesson you will describe how the solubility of most salts changes with temperature and read a simple solubility curve.",
    kp_zh="""- **溶解度**表示在一定温度下，一定量溶剂（常为 $100\ \mathrm{g}$ 水）最多能溶解多少溶质。
- 对**大多数盐**，温度升高，溶解度**增大**。
- 溶解度曲线以温度为横轴、溶解度为纵轴。
- 热的饱和溶液冷却时，多余的溶质可能**结晶**析出。
- 溶解达到最大后，再加入溶质会剩下固体，那是饱和溶液。""",
    kp_en="""- **Solubility** is the maximum amount of solute that can dissolve in a given amount of solvent (often $100\ \mathrm{g}$ of water) at a stated temperature.
- For **most salts**, solubility **increases** as temperature rises.
- A solubility curve has temperature on the horizontal axis and solubility on the vertical axis.
- When a hot saturated solution cools, extra solute may **crystallise** out.
- After the maximum has dissolved, added solid remains undissolved: the solution is saturated.""",
    body_zh=r"""同样一杯水，热水往往比冷水能溶解更多的盐。第 8 阶段要求把这个观察说准确：对大多数盐，溶解度随温度升高而增大。

溶解度要标明温度，因为 $20^\circ\mathrm{C}$ 和 $60^\circ\mathrm{C}$ 的值不同。曲线上某一点表示该温度下刚好饱和时能溶解的质量。若实际溶解的量低于曲线，溶液尚未饱和；若冷却后数值高于新温度下的溶解度，多余部分通常会结晶出来。这正是提纯盐时常用的冷却结晶。

注意：这是“大多数盐”的规律，不要推广成“所有物质都如此”（例如氧气在水中的溶解度反而随温度升高而降低，那不是本课的盐）。

## 例题

某盐在 $20^\circ\mathrm{C}$ 的溶解度为 $30\ \mathrm{g}/100\ \mathrm{g}$ 水，在 $70^\circ\mathrm{C}$ 为 $80\ \mathrm{g}/100\ \mathrm{g}$ 水。把 $70^\circ\mathrm{C}$ 的饱和溶液 $100\ \mathrm{g}$ 水冷却到 $20^\circ\mathrm{C}$，大约会析出多少克晶体？

**解：** $80-30=50\ \mathrm{g}$。""",
    body_en=r"""The same volume of water can often dissolve more salt when it is hot than when it is cold. Stage 8 asks you to state this carefully: for most salts, solubility increases as temperature increases.

A solubility value must include a temperature, because the figures at $20^\circ\mathrm{C}$ and $60^\circ\mathrm{C}$ are different. A point on a solubility curve shows how much dissolves at that temperature in a saturated solution. If the amount dissolved is below the curve, the solution is not yet saturated. If a solution is cooled so that the amount dissolved is above the new solubility, the extra usually crystallises out. That is the idea behind purifying a salt by cooling crystallisation.

The pattern is for **most salts**. Do not turn it into “every substance behaves this way” (the solubility of oxygen in water, for example, falls as temperature rises — and that is not a salt in this lesson).

## Worked example

A salt has solubility $30\ \mathrm{g}/100\ \mathrm{g}$ water at $20^\circ\mathrm{C}$ and $80\ \mathrm{g}/100\ \mathrm{g}$ water at $70^\circ\mathrm{C}$. A saturated solution in $100\ \mathrm{g}$ of water is cooled from $70^\circ\mathrm{C}$ to $20^\circ\mathrm{C}$. About how many grams of crystals form?

**Solution:** $80-30=50\ \mathrm{g}$.""",
    diff_zh="""- **忘记写温度。** 离开温度谈溶解度不完整。
- **以为冷却后溶质质量会消失。** 多出来的部分通常变成晶体，还在体系里。
- **把曲线读反。** 横轴是温度，纵轴是溶解度。""",
    diff_en="""- **Omitting the temperature.** A solubility value is incomplete without it.
- **Thinking the extra solute vanishes on cooling.** It usually appears as crystals and is still in the system.
- **Reading the axes the wrong way round.** Temperature is usually horizontal; solubility is vertical.""",
    diagram=D_SOLUB,
    questions=[
        dict(type="mcq", stem_zh="对大多数盐来说，温度升高时溶解度通常？", stem_en="For most salts, as temperature rises, solubility usually:",
             answer="a", exp_zh="大多数盐的溶解度随温度升高而增大。", exp_en="The solubility of most salts increases as temperature increases.",
             options=opts(("增大", "increases"), ("一定变为零", "must become zero"), ("与温度无关", "does not depend on temperature"), ("先突然变成气体", "suddenly turns into a gas first"))),
        dict(type="numeric", stem_zh="某盐在 $20^\\circ\\mathrm{C}$ 溶解度为 $30\\ \\mathrm{g}/100\\ \\mathrm{g}$ 水，在 $70^\\circ\\mathrm{C}$ 为 $80\\ \\mathrm{g}/100\\ \\mathrm{g}$ 水。把 $100\\ \\mathrm{g}$ 水中的饱和溶液从 $70^\\circ\\mathrm{C}$ 冷到 $20^\\circ\\mathrm{C}$，约析出多少克晶体？",
             stem_en="A salt dissolves $30\\ \\mathrm{g}/100\\ \\mathrm{g}$ water at $20^\\circ\\mathrm{C}$ and $80\\ \\mathrm{g}/100\\ \\mathrm{g}$ water at $70^\\circ\\mathrm{C}$. A saturated solution in $100\\ \\mathrm{g}$ water is cooled from $70^\\circ\\mathrm{C}$ to $20^\\circ\\mathrm{C}$. About how many grams of crystals form?",
             answer=50, exp_zh="$80-30=50\\ \\mathrm{g}$。", exp_en="$80-30=50\\ \\mathrm{g}$.", tolerance=0),
        dict(type="mcq", stem_zh="饱和溶液的含义是？", stem_en="A saturated solution is one that:",
             answer="c", exp_zh="在该温度下已溶解了最大量溶质，再加固体会剩下不溶。", exp_en="It already holds the maximum solute at that temperature; extra solid remains undissolved.",
             options=opts(("溶剂里完全没有溶质", "contains no solute at all"),
                          ("温度必须是 $0^\\circ\\mathrm{C}$", "must be at $0^\\circ\\mathrm{C}$"),
                          ("在该温度下不能再溶解更多溶质", "cannot dissolve any more solute at that temperature"),
                          ("一定是纯净物", "must be a pure substance"))),
        dict(type="mcq", stem_zh="热的盐的饱和溶液缓慢冷却，常用于？", stem_en="Slowly cooling a hot saturated solution of a salt is often used to:",
             answer="b", exp_zh="冷却结晶可让多余溶质以晶体形式析出，常用于提纯。", exp_en="Cooling crystallisation lets extra solute come out as crystals, often used to purify a salt.",
             options=opts(("把盐变成惰性气体", "turn the salt into an inert gas"),
                          ("使盐结晶析出从而提纯", "crystallise the salt and so purify it"),
                          ("提高所有气体的溶解度", "increase the solubility of every gas"),
                          ("测量 $R_f$", "measure $R_f$"))),
        dict(type="short", stem_zh="为什么谈论溶解度时必须说明温度？", stem_en="Why must a solubility value include a temperature?",
             answer="solubility depends on temperature",
             accepted=["solubility depends on temperature", "it changes with temperature",
                       "溶解度随温度变化", "不同温度溶解度不同", "必须标明温度因为溶解度随温度改变"],
             answer_zh="溶解度随温度变化，不标明温度就不完整。",
             answer_en="Solubility changes with temperature, so the value is incomplete without it.",
             exp_zh="例如同一盐在 $20^\\circ\\mathrm{C}$ 和 $70^\\circ\\mathrm{C}$ 的溶解度通常不同。",
             exp_en="The same salt usually has different solubilities at $20^\\circ\\mathrm{C}$ and at $70^\\circ\\mathrm{C}$."),
        dict(type="mcq", stem_zh="溶解度曲线上，横轴通常表示？", stem_en="On a typical solubility curve, the horizontal axis usually shows:",
             answer="d", exp_zh="横轴是温度，纵轴是溶解度。", exp_en="Temperature is usually horizontal; solubility is vertical.",
             options=opts(("$R_f$", "$R_f$"), ("原子核电荷", "nuclear charge"), ("反应性顺序", "the reactivity series"), ("温度", "temperature"))),
    ],
)

# ----- 8ES.01 resources -----
L(
    id="chemistry-8ES-1",
    title_zh="可再生与不可再生资源", title_en="Renewable and non-renewable resources",
    obj_zh="本节你将学会区分可再生与不可再生资源，并能各举出合适的例子。",
    obj_en="This lesson you will distinguish renewable and non-renewable resources and give suitable examples of each.",
    kp_zh="""- **不可再生资源**被消耗的速度远快于自然补充，例如煤、石油、天然气、许多金属矿。
- **可再生资源**可以在人类使用的时间尺度上补充，例如太阳能、风能、可持续管理的木材、水电（需合理管理）。
- 可再生并不等于“没有任何环境影响”。
- 回收金属、节约使用，可以减少对不可再生矿藏的依赖。
- 本主题属于科学 0893 的地球与太空相关内容，本站放在化学便于分科复习。""",
    kp_en="""- **Non-renewable resources** are used up much faster than nature can replace them, for example coal, oil, natural gas and many metal ores.
- **Renewable resources** can be replaced on a human timescale, for example solar power, wind, sustainably managed timber and (if well managed) hydroelectric power.
- Renewable does not mean “no environmental impact”.
- Recycling metals and using them carefully reduces pressure on non-renewable ores.
- This topic sits in the Earth and Space strand of Science 0893; it is placed under Chemistry on this site for subject review.""",
    body_zh=r"""资源是我们从地球获得、用来生活和生产的物质与能源。分类时要问：它被用掉以后，能不能在较短的人类时间尺度上再补回来？

煤、石油、天然气是古代生物经漫长地质过程形成的，今天用掉一吨，不可能在几年内再生成一吨，所以是不可再生的。许多金属矿也是如此。太阳辐射、风、以及在可持续砍伐和再种植前提下的木材，则可以不断获得，属于可再生。

要注意两个易混点。第一，可再生不是“永远无害”：水电站会改变河流生态，风电也有土地和材料问题。第二，一种资源的分类取决于如何使用：如果森林砍伐快于再生长，那份木材的使用就不再可持续。

## 例题

铝土矿和太阳能，哪一个是不可再生资源？为什么回收铝仍然有意义？

**解：** 铝土矿是不可再生的。回收铝可以减少开采新矿，并通常节省冶炼所需的大量能量。""",
    body_en=r"""Resources are materials and energy we take from the Earth to live and to manufacture things. To classify one, ask: once we have used it, can it be replaced on a reasonably short human timescale?

Coal, oil and natural gas formed from ancient living things over very long geological times. Using a tonne today does not make a new tonne in a few years, so they are non-renewable. Many metal ores are similar. Sunlight, wind, and timber that is cut and replanted sustainably can be obtained again and again, so they are renewable.

Two traps are worth avoiding. Renewable does not mean “harmless”: a dam changes a river, and wind farms still use land and materials. Also, classification can depend on use: if a forest is cut faster than it regrows, that use of timber is no longer sustainable.

## Worked example

Which is non-renewable, bauxite (aluminium ore) or solar energy? Why is recycling aluminium still worthwhile?

**Solution:** Bauxite is non-renewable. Recycling aluminium reduces the need to mine new ore and usually saves a large amount of energy used in extraction.""",
    diff_zh="""- **把可再生当成完全没有环境影响。** 分类依据是能否补充，不是“零影响”。
- **把金属当成可再生，只因为可以回收。** 矿藏本身不可再生；回收是在延长已开采金属的使用。
- **把木材一律写成不可再生。** 可持续管理时，木材可以是可再生资源。""",
    diff_en="""- **Treating renewable as zero environmental impact.** The test is whether the resource can be replaced, not whether use is impact-free.
- **Calling a metal renewable just because it can be recycled.** The ore itself is non-renewable; recycling stretches the metal already extracted.
- **Labelling all timber non-renewable.** Sustainably managed timber can be renewable.""",
    questions=[
        dict(type="mcq", stem_zh="下列哪一项是不可再生资源？", stem_en="Which of the following is a non-renewable resource?",
             answer="c", exp_zh="石油形成极慢，属于不可再生；风、太阳能和可持续木材是可再生的。", exp_en="Oil forms far too slowly to be replaced, so it is non-renewable; wind, solar and sustainable timber are renewable.",
             options=opts(("风能", "wind energy"), ("太阳能", "solar energy"), ("石油", "oil"), ("可持续管理的木材", "sustainably managed timber"))),
        dict(type="mcq", stem_zh="可再生资源的核心含义是？", stem_en="The core idea of a renewable resource is that it:",
             answer="a", exp_zh="能在人类使用的时间尺度上得到补充。", exp_en="Can be replaced on a human timescale of use.",
             options=opts(("能在人类使用的时间尺度上补充", "can be replaced on a human timescale"),
                          ("使用时一定完全没有环境影响", "has zero environmental impact when used"),
                          ("只能是金属", "must be a metal"),
                          ("不能被人类利用", "cannot be used by people"))),
        dict(type="mcq", stem_zh="回收铝罐主要的意义是？", stem_en="A main reason to recycle aluminium cans is to:",
             answer="b", exp_zh="减少对新矿的需求和通常所需的大量提炼能量。矿本身仍是不可再生的。", exp_en="Reduce demand for new ore and the large amount of energy usually needed to extract it. The ore itself is still non-renewable.",
             options=opts(("让铝土矿立刻变成可再生资源", "turn bauxite into a renewable resource immediately"),
                          ("减少开采新矿并节省提炼能量", "reduce new mining and save extraction energy"),
                          ("使铝不能再被使用", "stop aluminium being used again"),
                          ("把铝变成石油", "turn aluminium into oil"))),
        dict(type="short", stem_zh="各举一个可再生资源和一个不可再生资源的例子。", stem_en="Give one example of a renewable resource and one example of a non-renewable resource.",
             answer="solar and coal",
             accepted=["solar and coal", "wind and oil", "sustainable timber and natural gas", "hydro and coal",
                       "太阳能和煤", "风能和石油", "可持续木材和天然气", "水电和煤", "太阳和石油"],
             answer_zh="例如：太阳能（可再生）和煤（不可再生）。", answer_en="For example: solar energy (renewable) and coal (non-renewable).",
             exp_zh="只要一对分类正确即可，例如风与石油、可持续木材与天然气。", exp_en="Any correctly classified pair is fine, such as wind and oil, or sustainable timber and natural gas."),
        dict(type="mcq", stem_zh="若森林砍伐快于再生长，这样使用木材应当看作？", stem_en="If a forest is cut down faster than it can regrow, that use of timber should be seen as:",
             answer="d", exp_zh="补充跟不上消耗，这种使用就不再可持续，不能简单称为可再生利用。", exp_en="Replacement cannot keep up, so the use is not sustainable and should not simply be called renewable use.",
             options=opts(("一定仍然完全可再生且无影响", "still fully renewable and impact-free"),
                          ("把木材变成了金属矿", "turning timber into a metal ore"),
                          ("与分类无关", "irrelevant to classification"),
                          ("不再是可持续的利用", "no longer a sustainable use"))),
        dict(type="mcq", stem_zh="煤、石油、天然气被归为不可再生，主要是因为？", stem_en="Coal, oil and natural gas are classed as non-renewable mainly because:",
             answer="a", exp_zh="它们的自然形成远慢于人类消耗的速度。", exp_en="They form naturally far more slowly than humans use them.",
             options=opts(("自然形成远慢于被消耗的速度", "they form far more slowly than they are used"),
                          ("它们不是化合物", "they are not compounds"),
                          ("它们不能燃烧", "they cannot be burned"),
                          ("它们只存在于实验室", "they exist only in laboratories"))),
    ],
)

# ----- 8ES.02 climate vs weather -----
L(
    id="chemistry-8ES-2",
    title_zh="气候与天气", title_en="Climate and weather",
    obj_zh="本节你将学会区分气候和天气，并说明为什么不能用一两天的天气来否定气候趋势。",
    obj_en="This lesson you will distinguish climate from weather and explain why a day or two of weather cannot disprove a climate trend.",
    kp_zh="""- **天气**是某地在短时间内的大气状况：气温、降雨、风速、云量等，可逐日变化。
- **气候**是某地长期（通常按几十年衡量）的平均天气状况及其变化范围。
- 新加坡的气候是热带的、全年温暖潮湿；某一天突然相对凉爽，仍只是天气。
- 气候描述可用“通常”“平均”“季节型”等词语；天气描述则针对具体日期。
- 个别极端冷日或热日，不能单独用来证明或否定长期气候变化。""",
    kp_en="""- **Weather** is the state of the atmosphere at a place over a short time: temperature, rain, wind, cloud — and it can change from day to day.
- **Climate** is the long-term pattern of weather at a place (typically over decades), including averages and the usual range.
- Singapore’s climate is tropical, warm and humid through the year; one cooler day is still weather.
- Climate is described with words such as “usually”, “average” and “seasonal”; weather is tied to a particular date.
- A single unusually cold or hot day cannot, by itself, prove or disprove a long-term climate change.""",
    body_zh=r"""天气和气候常被混用，但时间尺度不同。问“明天会不会下雨”是在问天气；问“这个地方通常是不是又热又湿”是在问气候。

气候需要长期记录才能说清楚，因为任何地方都会有晴有雨、有偏热有偏凉。科学家用很多年的数据来描述平均值和常见范围。因此，不能拿“今年某周特别凉”或“某天特别热”单独作为否定或证明全球气候正在变化的证据。那只是短期波动。

对八年级而言，先把词用准：预报、今天、本周，多半是天气；某地的长期型态，才是气候。

## 例题

有人说：“这周连续三天很凉快，所以长期变暖不可能。”这个推理错在哪里？

**解：** 三天属于天气的短期变化，不能单独推翻用几十年数据描述的气候趋势。""",
    body_en=r"""Weather and climate are often mixed up, but they use different timescales. “Will it rain tomorrow?” is a weather question. “Is this place usually hot and humid?” is a climate question.

Climate needs a long record, because every place has wet days and dry days, warmer spells and cooler spells. Scientists use many years of data to describe the average and the usual range. That is why “it was unusually cool this week” or “it was very hot one afternoon” cannot, on its own, disprove or prove a long-term change in global climate. Those are short-term fluctuations.

For Year 8, use the words accurately: a forecast, today, or this week is usually weather; the long-term pattern of a place is climate.

## Worked example

Someone says: “It has been cool for three days, so long-term warming cannot be happening.” What is wrong with this reasoning?

**Solution:** Three days are short-term weather. They cannot, by themselves, overturn a climate trend described with decades of data.""",
    diff_zh="""- **用一天的天气否定气候。** 气候看长期型态。
- **把气候说成“永远每天都一样”。** 气候包含正常的变化范围和季节差异。
- **把“气候”只理解成全球变暖这一个话题。** 先掌握定义，再讨论长期变化。""",
    diff_en="""- **Using one day’s weather to deny a climate pattern.** Climate is about the long term.
- **Saying climate means “every day is identical”.** Climate includes a normal range and seasonal differences.
- **Treating “climate” as only the topic of global warming.** Learn the definition first, then discuss long-term change.""",
    questions=[
        dict(type="mcq", stem_zh="“明天下午有雷阵雨”描述的是？", stem_en="“There will be a thunderstorm tomorrow afternoon” describes:",
             answer="b", exp_zh="针对具体时间的短期状况，是天气。", exp_en="It is a short-term condition for a specific time, so it is weather.",
             options=opts(("气候", "climate"), ("天气", "weather"), ("地壳运动", "crustal movement"), ("纯净物", "a pure substance"))),
        dict(type="mcq", stem_zh="“该地区多年平均年降雨量很高，全年温暖”描述的是？", stem_en="“This region has a high average annual rainfall and is warm all year” describes:",
             answer="a", exp_zh="这是长期平均状况，属于气候。", exp_en="This is a long-term average pattern, so it is climate.",
             options=opts(("气候", "climate"), ("只是明天的天气预报", "only tomorrow’s forecast"),
                          ("一次火山喷发", "a single volcanic eruption"), ("溶解度", "solubility"))),
        dict(type="mcq", stem_zh="为什么不能只用连续三天偏凉来否定长期变暖趋势？", stem_en="Why can three cooler days not, by themselves, disprove a long-term warming trend?",
             answer="c", exp_zh="三天是天气的短期波动；气候趋势需要长期数据。", exp_en="Three days are short-term weather; a climate trend needs a long record.",
             options=opts(("因为天气不能被测量", "because weather cannot be measured"),
                          ("因为气候必须每天完全相同", "because climate means every day is identical"),
                          ("因为那只是短期天气，气候看长期记录", "because that is short-term weather, and climate uses a long record"),
                          ("因为温度计只能测气候，不能测天气", "because thermometers can measure climate but not weather"))),
        dict(type="short", stem_zh="用一句话区分天气和气候。", stem_en="In one sentence, distinguish weather and climate.",
             answer="weather is short term, climate is long term",
             accepted=["weather is short term, climate is long term", "weather: short-term; climate: long-term average",
                       "天气是短期的，气候是长期的平均状况", "天气看短时间，气候看长期型态"],
             answer_zh="天气是短期的大气状况，气候是长期的平均天气型态。",
             answer_en="Weather is the short-term state of the atmosphere; climate is the long-term pattern of weather.",
             exp_zh="关键差别是时间尺度：日、周相对年、十年。", exp_en="The key difference is timescale: days or weeks versus years or decades."),
        dict(type="mcq", stem_zh="新加坡某一天比平常稍凉，这最适合称为？", stem_en="A day in Singapore that is a little cooler than usual is best described as:",
             answer="d", exp_zh="这是短期变化，属于天气；气候仍然是热带温暖潮湿。", exp_en="It is a short-term variation, so it is weather; the climate is still tropical, warm and humid.",
             options=opts(("气候已经变成极地", "the climate has become polar"),
                          ("天气和气候是同一个词", "weather and climate mean the same"),
                          ("长期气候记录被这一天完全改写", "this one day rewrites the long-term climate record"),
                          ("一次天气变化，不等于气候已经改变", "a weather variation, not by itself a change of climate"))),
        dict(type="mcq", stem_zh="描述气候时，下列哪一种说法最合适？", stem_en="Which is the most suitable way to describe climate?",
             answer="a", exp_zh="用长期平均和通常范围，而不是只引用某一天。", exp_en="Use long-term averages and the usual range, not a single day alone.",
             options=opts(("用多年的平均状况和通常范围", "use averages and the usual range over many years"),
                          ("只用昨天中午的气温", "use only yesterday’s midday temperature"),
                          ("完全不需要数据", "use no data at all"),
                          ("只用一天的云量", "use cloud cover from one day only"))),
    ],
)

# ----- 8ES.03 long-term climate -----
L(
    id="chemistry-8ES-3",
    title_zh="地球气候的长期循环与大气变化", title_en="Long-term climate cycles and atmospheric change",
    obj_zh="本节你将学会说明地球气候可以在很长的时间里循环变化，并且大气成分变化会影响气候。",
    obj_en="This lesson you will explain that Earth’s climate can change in long cycles, and that changes in the atmosphere can affect climate.",
    kp_zh="""- 地球气候并非永恒不变，历史上有过冰期和相对温暖的时期，存在**长期循环**。
- 自然因素包括地球轨道与轴向的缓慢变化、火山喷发向大气注入尘埃和气体等。
- 大气成分（例如二氧化碳等温室气体）会影响地球保留的能量，从而影响气候。
- 今天的变化要放在长期记录中理解，同时也要区分自然循环与人类活动的额外影响。
- 本课建立观念，不要求记忆复杂的循环周期数字。""",
    kp_en="""- Earth’s climate is not fixed for ever. There have been ice ages and warmer periods: **long-term cycles** exist.
- Natural factors include slow changes in Earth’s orbit and tilt, and volcanoes injecting dust and gases into the atmosphere.
- The composition of the atmosphere (for example greenhouse gases such as carbon dioxide) affects how much energy Earth keeps, and so affects climate.
- Today’s changes should be read against the long record, while also distinguishing natural cycles from extra human influences.
- This lesson builds the idea; you do not need to memorise detailed cycle lengths.""",
    body_zh=r"""气候不但因季节而变，在更长的尺度上也会变。地质和冰芯等记录显示，地球经历过多次寒冷的冰期和比较温暖的间冰期。这说明气候有自然的长期起伏。

原因是多方面的。地球绕太阳运行的轨道和地轴倾斜会非常缓慢地改变，到达不同地区的阳光随之变化。大规模火山喷发把尘埃和气体送进大气，可能在一段时间里挡住部分阳光，使地表变凉。大气里某些气体能留住更多能量，浓度改变时，长期平均温度也可能改变。

学习时要同时避免两种简单化：一种是“气候以前变过，所以今天任何变化都不必在意”；另一种是“完全没有自然循环”。更准确的说法是：自然循环存在，而人类燃烧化石燃料等活动会额外改变大气成分。把资源使用与大气、气候联系起来，是本章把地球内容放在化学里的原因之一。

## 例题

为什么说“火山喷发可以暂时影响气候”，却不能把某一次喷发当成全部气候历史的唯一原因？

**解：** 一次喷发可能在较短时期内改变大气、影响气温，但长期循环还有轨道变化、大气成分的长期改变等多种因素。""",
    body_en=r"""Climate does not only change with the seasons. On much longer timescales it changes too. Geological and ice-core records show ice ages and warmer intervals between them. So climate has natural long-term rises and falls.

Several factors matter. Earth’s orbit and the tilt of its axis change very slowly, which changes how sunlight is distributed. Large volcanic eruptions can send dust and gases into the atmosphere and block some sunlight for a time, cooling the surface. Some gases in the atmosphere keep more energy in, so if their concentrations change, the long-term average temperature may change as well.

Avoid two over-simple stories: “climate has changed before, so nothing today matters”, and “there are no natural cycles at all”. A fairer Year 8 statement is that natural cycles exist, and that human activities such as burning fossil fuels add extra changes to the atmosphere. Linking resource use to the atmosphere and climate is one reason this Earth topic sits under Chemistry here.

## Worked example

Why can we say “a volcanic eruption can affect climate for a time” without treating one eruption as the only cause of all climate history?

**Solution:** An eruption may change the atmosphere and temperatures for a period, but long-term cycles also involve other factors, such as orbital changes and longer-term shifts in atmospheric composition.""",
    diff_zh="""- **把天气波动直接叫作冰期循环。** 长期循环的时间尺度远长于几天或几年。
- **只用一个因素解释全部气候历史。** 轨道、火山、大气成分等都可能有贡献。
- **以为承认自然循环就不能再讨论人类影响。** 两者可以同时存在。""",
    diff_en="""- **Calling a spell of weather an ice-age cycle.** Long cycles run over far longer times than days or a few years.
- **Using a single factor to explain all of climate history.** Orbit, volcanoes and atmospheric composition can all contribute.
- **Thinking that natural cycles rule out any human influence.** Both can exist together.""",
    questions=[
        dict(type="mcq", stem_zh="关于地球气候，较准确的说法是？", stem_en="A fair statement about Earth’s climate is that:",
             answer="b", exp_zh="气候并非永恒不变，历史上有过冰期和较暖期等长期变化。", exp_en="Climate is not fixed for ever; there have been long-term changes such as ice ages and warmer periods.",
             options=opts(("气候从未发生过任何变化", "climate has never changed at all"),
                          ("气候会在很长的时间尺度上变化，存在长期循环", "climate can change over long timescales and there are long-term cycles"),
                          ("气候每小时精确重复一次循环", "climate repeats an exact cycle every hour"),
                          ("只有天气存在，气候不存在", "only weather exists; climate does not"))),
        dict(type="mcq", stem_zh="大规模火山喷发可能在一段时间里使地表变凉，是因为？", stem_en="A large volcanic eruption may cool the surface for a time because:",
             answer="a", exp_zh="喷发把尘埃和气体送进大气，可能挡住部分阳光。", exp_en="It can inject dust and gases into the atmosphere, which may block some sunlight.",
             options=opts(("尘埃和气体进入大气，可能挡住部分阳光", "dust and gases enter the atmosphere and may block some sunlight"),
                          ("火山会立刻停止地球公转", "volcanoes instantly stop Earth orbiting the Sun"),
                          ("火山把所有海洋变成纯净物", "volcanoes turn all oceans into pure substances"),
                          ("火山只改变明天一小时的天气预报，不影响大气", "volcanoes change only one hour of tomorrow’s forecast and not the atmosphere"))),
        dict(type="mcq", stem_zh="大气中某些气体浓度改变，可能影响气候，是因为它们可以？", stem_en="A change in the concentration of some atmospheric gases may affect climate because those gases can:",
             answer="c", exp_zh="某些气体（如二氧化碳）会影响地球保留的能量。", exp_en="Some gases (such as carbon dioxide) affect how much energy Earth keeps.",
             options=opts(("消灭地球的磁场", "destroy Earth’s magnetic field"),
                          ("把所有盐的溶解度变为零", "make the solubility of every salt zero"),
                          ("影响地球保留多少能量", "affect how much energy Earth keeps"),
                          ("停止天气的发生", "stop weather happening at all"))),
        dict(type="short", stem_zh="举出一个可导致气候长期变化的自然因素。", stem_en="Give one natural factor that can contribute to long-term climate change.",
             answer="volcanic eruptions",
             accepted=["volcanic eruptions", "volcanoes", "changes in Earth's orbit", "changes in tilt", "orbital changes", "atmospheric composition",
                       "火山喷发", "火山", "地球轨道变化", "地轴倾斜变化", "大气成分变化"],
             answer_zh="例如火山喷发，或地球轨道与轴向的缓慢变化。",
             answer_en="For example volcanic eruptions, or slow changes in Earth’s orbit and tilt.",
             exp_zh="自然因素不止一种，答对其中一类即可。", exp_en="There is more than one natural factor; any appropriate one is fine."),
        dict(type="mcq", stem_zh="“以前也有自然的气候循环，所以今天人类活动不可能有影响。”这个推论的问题是？", stem_en="“Natural climate cycles existed in the past, so human activity cannot have an effect today.” The problem with this claim is:",
             answer="d", exp_zh="自然循环与人类对大气的额外影响可以同时存在，前者并不能自动排除后者。", exp_en="Natural cycles and extra human effects on the atmosphere can exist together; the first does not automatically rule out the second.",
             options=opts(("气候循环每小时发生一次，所以说法成立", "climate cycles happen every hour, so the claim is true"),
                          ("人类活动从来不会改变大气", "human activity never changes the atmosphere"),
                          ("天气和气候是同一个词", "weather and climate are the same word"),
                          ("自然循环的存在并不能自动排除额外的人类影响", "natural cycles do not automatically rule out extra human influences"))),
        dict(type="mcq", stem_zh="把化石燃料使用与气候联系起来，是因为燃烧会？", stem_en="Fossil-fuel use is linked to climate because burning them can:",
             answer="a", exp_zh="燃烧化石燃料会改变大气成分（例如增加二氧化碳），从而可能影响地球保留的能量。", exp_en="Burning fossil fuels changes the atmosphere (for example by adding carbon dioxide), which can affect how much energy Earth keeps.",
             options=opts(("改变大气成分，从而可能影响地球保留的能量", "change atmospheric composition, which may affect how much energy Earth keeps"),
                          ("立刻把气候变成天气", "instantly turn climate into weather"),
                          ("使所有资源变为可再生", "make every resource renewable"),
                          ("只改变金属的反应性顺序", "only change the metal reactivity series"))),
    ],
)

def X(section, **q):
    return (section, q)

# Chapter practice / paper questions (unique; not reused as lesson practice)
CM_PR = add_extra_questions(C, [
    X("chemistry-8Cm-1", type="mcq", id="q-ch-8Cm-pr01",
      stem_zh="卢瑟福模型认为原子的质量几乎全部位于？", stem_en="In the Rutherford model, almost all the mass of an atom is in the:",
      answer="a", exp_zh="质量几乎全部在很小的原子核里。", exp_en="Almost all the mass is in the tiny nucleus.",
      options=opts(("原子核", "nucleus"), ("电子云的最外沿且电子最重", "the outer edge, because electrons are the heaviest"),
                   ("原子外的真空中", "the vacuum outside the atom"), ("中子单独组成的外壳", "a shell made only of neutrons"))),
    X("chemistry-8Cm-1", type="mcq", id="q-ch-8Cm-pr02",
      stem_zh="大多数α粒子几乎直线穿过金箔，主要因为？", stem_en="Most alpha particles go almost straight through gold foil mainly because:",
      answer="c", exp_zh="原子大部分是空的。", exp_en="An atom is mostly empty space.",
      options=opts(("金原子没有电荷", "gold atoms have no charge"), ("α粒子不带电", "alpha particles are uncharged"),
                   ("原子大部分是空的", "atoms are mostly empty space"), ("电子把所有α粒子吸住后又放行", "electrons catch every alpha particle and then release it"))),
    X("chemistry-8Cm-2", type="mcq", id="q-ch-8Cm-pr03",
      stem_zh="质子、中子、电子的相对电荷依次是？", stem_en="The relative charges of a proton, a neutron and an electron are:",
      answer="b", exp_zh="质子 $+1$，中子 $0$，电子 $-1$。", exp_en="Proton $+1$, neutron $0$, electron $-1$.",
      options=opts(("$0, +1, -1$", "$0, +1, -1$"), ("$+1, 0, -1$", "$+1, 0, -1$"), ("$-1, 0, +1$", "$-1, 0, +1$"), ("$+1, -1, 0$", "$+1, -1, 0$"))),
    X("chemistry-8Cm-2", type="numeric", id="q-ch-8Cm-pr04",
      stem_zh="某中性原子有 $12$ 个质子和 $12$ 个中子。电子数是多少？", stem_en="A neutral atom has $12$ protons and $12$ neutrons. How many electrons does it have?",
      answer=12, exp_zh="中性原子电子数等于质子数，为 $12$。中子不影响电荷。", exp_en="In a neutral atom, electrons equal protons, so $12$. Neutrons do not affect charge.", tolerance=0),
    X("chemistry-8Cm-3", type="mcq", id="q-ch-8Cm-pr05",
      stem_zh="电子被留在核周围，是因为？", stem_en="Electrons are held around the nucleus because:",
      answer="d", exp_zh="核带正电、电子带负电，异种电荷相吸。", exp_en="The nucleus is positive and electrons are negative, so opposite charges attract.",
      options=opts(("同种电荷相吸", "like charges attract"), ("中子带负电", "neutrons are negative"),
                   ("电子比核更重", "electrons are heavier than the nucleus"), ("异种电荷相吸", "opposite charges attract"))),
    X("chemistry-8Cm-4", type="mcq", id="q-ch-8Cm-pr06",
      stem_zh="判断固体是否纯，常用的证据是？", stem_en="A useful piece of evidence for whether a solid is pure is:",
      answer="a", exp_zh="纯净物有尖锐、固定的熔点，可与数据手册比较。", exp_en="A pure substance has a sharp, fixed melting point that can be compared with a data book.",
      options=opts(("测定熔点并与数据比较", "measure the melting point and compare it with data"),
                   ("只看颜色是否鲜艳", "only check whether the colour looks bright"),
                   ("称一次质量即可，不必看温度", "weigh it once; temperature is irrelevant"),
                   ("看它是否含有超过一种元素——化合物都不是纯净物", "see if it contains more than one element — compounds are never pure"))),
    X("chemistry-8Cm-4", type="mcq", id="q-ch-8Cm-pr07",
      stem_zh="杂质对固体熔点的典型影响是？", stem_en="Impurities typically affect the melting point of a solid by:",
      answer="b", exp_zh="通常使熔点降低、熔程变宽。", exp_en="They usually lower it and widen the range.",
      options=opts(("使熔点升高且更尖锐", "raising it and making it sharper"), ("使熔点降低且熔程变宽", "lowering it and widening the range"),
                   ("使固体无法存在", "stopping the solid existing"), ("把熔点永远固定在 $100^\\circ\\mathrm{C}$", "fixing it at $100^\\circ\\mathrm{C}$ for ever"))),
    X("chemistry-8Cm-3", type="short", id="q-ch-8Cm-pr08",
      stem_zh="同种电荷之间是相吸还是相斥？", stem_en="Do like charges attract or repel?",
      answer="repel", accepted=["repel", "they repel", "相斥", "互相排斥", "同种相斥"],
      answer_zh="相斥。", answer_en="They repel.",
      exp_zh="同种相斥，异种相吸。", exp_en="Like charges repel; opposite charges attract."),
])

CM_PA = add_extra_questions(C, [
    X("chemistry-8Cm-1", type="mcq", id="q-ch-8Cm-pa01",
      stem_zh="少数α粒子发生大角度偏转，说明原子核？", stem_en="A few alpha particles are deflected through large angles. This shows that the nucleus is:",
      answer="c", exp_zh="正电荷和质量集中在很小的、质量很大的核上。", exp_en="Positive charge and mass are concentrated in a tiny, massive nucleus.",
      options=opts(("体积占满整个原子", "large enough to fill the atom"), ("不带电", "uncharged"),
                   ("很小且集中了正电荷和质量", "tiny, with concentrated positive charge and mass"), ("由电子组成", "made of electrons"))),
    X("chemistry-8Cm-1", type="mcq", id="q-ch-8Cm-pa02",
      stem_zh="卢瑟福模型中，电子位于？", stem_en="In the Rutherford model, electrons are located:",
      answer="a", exp_zh="电子在原子核周围的空间中。", exp_en="Electrons occupy the space around the nucleus.",
      options=opts(("核周围的空间中", "in the space around the nucleus"), ("只在核的内部", "only inside the nucleus"),
                   ("全部在金箔表面", "all on the surface of the gold foil"), ("质子的内部", "inside protons"))),
    X("chemistry-8Cm-2", type="mcq", id="q-ch-8Cm-pa03",
      stem_zh="中子的相对电荷和相对质量（近似）分别是？", stem_en="A neutron’s relative charge and approximate relative mass are:",
      answer="d", exp_zh="电荷为 $0$，相对质量约 $1$。", exp_en="Charge $0$ and relative mass about $1$.",
      options=opts(("$-1$，约 $0$", "$-1$, about $0$"), ("$+1$，约 $0$", "$+1$, about $0$"),
                   ("$0$，约 $0$", "$0$, about $0$"), ("$0$，约 $1$", "$0$, about $1$"))),
    X("chemistry-8Cm-2", type="numeric", id="q-ch-8Cm-pa04",
      stem_zh="中性原子有 $9$ 个质子。电子数是多少？", stem_en="A neutral atom has $9$ protons. How many electrons does it have?",
      answer=9, exp_zh="中性原子电子数等于质子数。", exp_en="In a neutral atom, electrons equal protons.", tolerance=0),
    X("chemistry-8Cm-3", type="mcq", id="q-ch-8Cm-pa05",
      stem_zh="α粒子被核推开，是因为？", stem_en="An alpha particle is pushed away from a nucleus because:",
      answer="b", exp_zh="两者都带正电，同种电荷相斥。", exp_en="Both are positive, so like charges repel.",
      options=opts(("两者都带负电", "both are negative"), ("两者都带正电，同种相斥", "both are positive, so like charges repel"),
                   ("中子带强正电", "neutrons are strongly positive"), ("电子质量极大", "electrons are extremely massive"))),
    X("chemistry-8Cm-3", type="mcq", id="q-ch-8Cm-pa06",
      stem_zh="把电子留在原子里的力是？", stem_en="The force that holds electrons in the atom is:",
      answer="a", exp_zh="核与电子之间的静电引力。", exp_en="Electrostatic attraction between the nucleus and the electrons.",
      options=opts(("静电引力", "electrostatic attraction"), ("只有重力", "gravity alone"),
                   ("中子之间的排斥", "repulsion between neutrons"), ("熔点降低", "a lowered melting point"))),
    X("chemistry-8Cm-4", type="mcq", id="q-ch-8Cm-pa07",
      stem_zh="下列哪一种是混合物？", stem_en="Which of these is a mixture?",
      answer="c", exp_zh="空气含有多种气体，是混合物；蒸馏水和纯二氧化碳是纯净物。", exp_en="Air contains several gases, so it is a mixture; distilled water and pure carbon dioxide are pure substances.",
      options=opts(("蒸馏水", "distilled water"), ("纯二氧化碳", "pure carbon dioxide"), ("空气", "air"), ("只由一种元素组成的样品", "a sample that is a single element"))),
    X("chemistry-8Cm-4", type="mcq", id="q-ch-8Cm-pa08",
      stem_zh="某固体数据熔点为 $120^\\circ\\mathrm{C}$，样品在 $110$–$118^\\circ\\mathrm{C}$ 熔化。较合理的结论是？",
      stem_en="A solid should melt at $120^\\circ\\mathrm{C}$, but a sample melts from $110$ to $118^\\circ\\mathrm{C}$. A reasonable conclusion is:",
      answer="d", exp_zh="熔点偏低且熔程宽，样品可能不纯。", exp_en="The melting point is low and the range is wide, so the sample may be impure.",
      options=opts(("样品一定更纯", "the sample must be purer than the data-book substance"),
                   ("熔点数据没有用", "melting points are not useful"),
                   ("样品一定是一种气体", "the sample must be a gas"),
                   ("样品可能含有杂质", "the sample may contain impurities"))),
    X("chemistry-8Cm-2", type="short", id="q-ch-8Cm-pa09",
      stem_zh="为什么中性原子整体电荷为零？", stem_en="Why is the overall charge of a neutral atom zero?",
      answer="equal protons and electrons",
      accepted=["equal protons and electrons", "proton number equals electron number", "charges cancel",
                "质子数等于电子数", "正负电荷抵消", "质子与电子数目相等，电荷抵消"],
      answer_zh="质子数等于电子数，正负电荷抵消。", answer_en="The numbers of protons and electrons are equal, so the charges cancel.",
      exp_zh="中子不贡献电荷。", exp_en="Neutrons do not contribute charge."),
    X("chemistry-8Cm-1", type="mcq", id="q-ch-8Cm-pa10",
      stem_zh="若原子是带均匀正电的实心球，α粒子散射最可能怎样？", stem_en="If atoms were solid balls of spread-out positive charge, alpha scattering would most likely show:",
      answer="b", exp_zh="不会出现少数非常大的偏转，因为没有又小又集中的核。", exp_en="There would not be a few very large deflections, because there would be no tiny concentrated nucleus.",
      options=opts(("更多粒子几乎被弹回", "even more particles bouncing almost straight back"),
                   ("几乎只有小角度偏转，很少有极大偏转", "only small deflections, with very few huge ones"),
                   ("所有粒子都停在箔的表面", "every particle stopping on the surface of the foil"),
                   ("电子全部掉进核里", "all electrons falling into the nucleus"))),
    X("chemistry-8Cm-4", type="mcq", id="q-ch-8Cm-pa11",
      stem_zh="纯净物的沸点通常是？", stem_en="The boiling point of a pure substance is usually:",
      answer="a", exp_zh="纯净物有固定、尖锐的沸点。", exp_en="A pure substance has a sharp, fixed boiling point.",
      options=opts(("固定而尖锐的", "sharp and fixed"), ("完全无法测定的", "impossible to measure"),
                   ("一定比所有混合物都低很多且无范围可言", "always far lower than any mixture, with no range idea"),
                   ("与纯度无关", "unrelated to purity"))),
    X("chemistry-8Cm-3", type="mcq", id="q-ch-8Cm-pa12",
      stem_zh="中子不提供核与电子之间的静电吸引，因为中子？", stem_en="Neutrons do not provide the electrostatic attraction between the nucleus and electrons because they:",
      answer="c", exp_zh="中子不带电。", exp_en="Neutrons are uncharged.",
      options=opts(("质量为零", "have zero mass"), ("带负电", "are negative"), ("不带电", "are uncharged"), ("位于核外", "are outside the nucleus"))),
])

CP_PR = add_extra_questions(C, [
    X("chemistry-8Cp-1", type="numeric", id="q-ch-8Cp-pr01",
      stem_zh="$10\\ \\mathrm{g}$ 溶质配成 $0.25\\ \\mathrm{dm^3}$ 溶液。浓度是多少 $\\mathrm{g/dm^3}$？",
      stem_en="$10\\ \\mathrm{g}$ of solute is made up to $0.25\\ \\mathrm{dm^3}$ of solution. Concentration in $\\mathrm{g/dm^3}$?",
      answer=40, exp_zh="$10/0.25=40$。", exp_en="$10/0.25=40$.", tolerance=0),
    X("chemistry-8Cp-1", type="numeric", id="q-ch-8Cp-pr02",
      stem_zh="$5.0\\ \\mathrm{g}$ 溶质配成 $200\\ \\mathrm{cm^3}$ 溶液。浓度是多少 $\\mathrm{g/dm^3}$？",
      stem_en="$5.0\\ \\mathrm{g}$ of solute is made up to $200\\ \\mathrm{cm^3}$ of solution. Concentration in $\\mathrm{g/dm^3}$?",
      answer=25, exp_zh="$200\\ \\mathrm{cm^3}=0.200\\ \\mathrm{dm^3}$，$5.0/0.200=25$。", exp_en="$200\\ \\mathrm{cm^3}=0.200\\ \\mathrm{dm^3}$, so $5.0/0.200=25$.", tolerance=0),
    X("chemistry-8Cp-1", type="mcq", id="q-ch-8Cp-pr03",
      stem_zh="加水稀释溶液（溶质质量不变）时，浓度？", stem_en="When a solution is diluted with water (mass of solute unchanged), concentration:",
      answer="b", exp_zh="体积变大，浓度降低。", exp_en="The volume increases, so the concentration falls.",
      options=opts(("升高", "increases"), ("降低", "decreases"), ("必为 $0$", "must become $0$"), ("与体积无关", "does not depend on volume"))),
    X("chemistry-8Cp-2", type="numeric", id="q-ch-8Cp-pr04",
      stem_zh="溶剂移动 $8.0\\ \\mathrm{cm}$，斑点移动 $2.0\\ \\mathrm{cm}$。$R_f$ 是多少？",
      stem_en="The solvent travels $8.0\\ \\mathrm{cm}$ and a spot travels $2.0\\ \\mathrm{cm}$. What is $R_f$?",
      answer=0.25, exp_zh="$2.0/8.0=0.25$。", exp_en="$2.0/8.0=0.25$.", tolerance=0.01),
    X("chemistry-8Cp-2", type="mcq", id="q-ch-8Cp-pr05",
      stem_zh="纸层析中，起点线应在溶剂液面的？", stem_en="In paper chromatography, the baseline should be:",
      answer="a", exp_zh="起点线要在液面上方，以免样品被洗掉。", exp_en="The baseline must sit above the solvent surface so the sample is not washed off.",
      options=opts(("上方", "above the solvent surface"), ("下方并浸没", "below the surface, submerged"),
                   ("溶剂瓶外面的桌面上", "on the bench outside the beaker"), ("溶剂前沿的上面且先于实验划上墨水", "above the solvent front, already drawn in ink"))),
    X("chemistry-8Cp-2", type="mcq", id="q-ch-8Cp-pr06",
      stem_zh="两个斑点说明样品？", stem_en="Two spots suggest that the sample:",
      answer="c", exp_zh="至少含有两种可被分开的成分，是混合物。", exp_en="Contains at least two substances that can be separated, so it is a mixture.",
      options=opts(("一定是一种元素", "must be an element"), ("$R_f$ 一定大于 $1$", "must have $R_f>1$"),
                   ("是混合物", "is a mixture"), ("实验失败，因为纯净物必须有两个斑点", "failed, because a pure substance must show two spots"))),
    X("chemistry-8Cp-1", type="short", id="q-ch-8Cp-pr07",
      stem_zh="$1\\ \\mathrm{dm^3}$ 等于多少 $\\mathrm{cm^3}$？", stem_en="How many $\\mathrm{cm^3}$ are there in $1\\ \\mathrm{dm^3}$?",
      answer="1000", accepted=["1000", "1 000", "1000 cm3", "1000 cm^3", "$1000$", "一千"],
      answer_zh="$1000$", answer_en="$1000$",
      exp_zh="$1\\ \\mathrm{dm^3}=1000\\ \\mathrm{cm^3}=1\\ \\mathrm{L}$。", exp_en="$1\\ \\mathrm{dm^3}=1000\\ \\mathrm{cm^3}=1\\ \\mathrm{L}$."),
    X("chemistry-8Cp-2", type="mcq", id="q-ch-8Cp-pr08",
      stem_zh="比较 $R_f$ 来鉴定物质时，必须？", stem_en="To identify a substance by comparing $R_f$ values, you must:",
      answer="d", exp_zh="在相同条件（溶剂、温度等）下与已知样品比较。", exp_en="Compare with a known sample under the same conditions (solvent, temperature and so on).",
      options=opts(("改用完全不同的溶剂却直接比较数字", "change the solvent completely and still compare the numbers directly"),
                   ("让 $R_f$ 大于 $1$", "make $R_f$ greater than $1$"),
                   ("用钢笔重画起点线", "redraw the baseline in ink"),
                   ("在相同条件下与已知物质比较", "compare with a known substance under the same conditions"))),
])

CP_PA = add_extra_questions(C, [
    X("chemistry-8Cp-1", type="numeric", id="q-ch-8Cp-pa01",
      stem_zh="浓度为 $15\\ \\mathrm{g/dm^3}$ 的溶液有 $0.80\\ \\mathrm{dm^3}$。溶质质量是多少克？",
      stem_en="A solution of concentration $15\\ \\mathrm{g/dm^3}$ has volume $0.80\\ \\mathrm{dm^3}$. Mass of solute in grams?",
      answer=12, exp_zh="$15\\times 0.80=12\\ \\mathrm{g}$。", exp_en="$15\\times 0.80=12\\ \\mathrm{g}$.", tolerance=0),
    X("chemistry-8Cp-1", type="numeric", id="q-ch-8Cp-pa02",
      stem_zh="$9.0\\ \\mathrm{g}$ 溶质配成 $500\\ \\mathrm{cm^3}$ 溶液。浓度是多少 $\\mathrm{g/dm^3}$？",
      stem_en="$9.0\\ \\mathrm{g}$ of solute is made up to $500\\ \\mathrm{cm^3}$. Concentration in $\\mathrm{g/dm^3}$?",
      answer=18, exp_zh="$500\\ \\mathrm{cm^3}=0.500\\ \\mathrm{dm^3}$，$9.0/0.500=18$。", exp_en="$500\\ \\mathrm{cm^3}=0.500\\ \\mathrm{dm^3}$, so $9.0/0.500=18$.", tolerance=0),
    X("chemistry-8Cp-1", type="mcq", id="q-ch-8Cp-pa03",
      stem_zh="浓度的含义是？", stem_en="Concentration means:",
      answer="a", exp_zh="一定体积溶液中溶质的多少。", exp_en="How much solute is in a given volume of solution.",
      options=opts(("一定体积溶液里溶质的多少", "how much solute is in a given volume of solution"),
                   ("溶剂的沸点", "the boiling point of the solvent"),
                   ("只有 $R_f$", "only $R_f$"),
                   ("原子核里中子的数目", "the number of neutrons in a nucleus"))),
    X("chemistry-8Cp-2", type="numeric", id="q-ch-8Cp-pa04",
      stem_zh="溶剂前沿距起点 $12.0\\ \\mathrm{cm}$，斑点距起点 $9.0\\ \\mathrm{cm}$。$R_f$？",
      stem_en="The solvent front is $12.0\\ \\mathrm{cm}$ from the baseline and a spot is $9.0\\ \\mathrm{cm}$ from the baseline. $R_f$?",
      answer=0.75, exp_zh="$9.0/12.0=0.75$。", exp_en="$9.0/12.0=0.75$.", tolerance=0.01),
    X("chemistry-8Cp-2", type="mcq", id="q-ch-8Cp-pa05",
      stem_zh="为什么 $R_f$ 不能大于 $1$？", stem_en="Why can $R_f$ not be greater than $1$?",
      answer="b", exp_zh="斑点不能跑到溶剂前沿的前面。", exp_en="A spot cannot travel beyond the solvent front.",
      options=opts(("因为浓度不能大于 $1\\ \\mathrm{g/dm^3}$", "because concentration cannot exceed $1\\ \\mathrm{g/dm^3}$"),
                   ("因为斑点不能超过溶剂前沿", "because a spot cannot travel beyond the solvent front"),
                   ("因为要用钢笔记录", "because results must be recorded in ink"),
                   ("因为纯净物的 $R_f$ 规定为 $2$", "because a pure substance is defined to have $R_f=2$"))),
    X("chemistry-8Cp-2", type="mcq", id="q-ch-8Cp-pa06",
      stem_zh="起点线用铅笔，是因为石墨？", stem_en="The baseline is drawn in pencil because graphite:",
      answer="c", exp_zh="石墨不溶于常见层析溶剂。", exp_en="Graphite does not dissolve in the usual chromatography solvents.",
      options=opts(("会比样品跑得更快", "travels faster than the sample"), ("带有很强的核电荷", "has a very large nuclear charge"),
                   ("不随常见溶剂上升", "does not travel with the usual solvents"), ("使 $R_f$ 自动等于 $0$", "forces $R_f$ to be $0$"))),
    X("chemistry-8Cp-1", type="mcq", id="q-ch-8Cp-pa07",
      stem_zh="同样溶质质量，溶液体积减半（未析出固体），浓度？", stem_en="If the mass of solute is unchanged and the volume of solution is halved (no solid appears), the concentration:",
      answer="d", exp_zh="体积减半，浓度加倍。", exp_en="Halving the volume doubles the concentration.",
      options=opts(("减半", "is halved"), ("不变", "stays the same"), ("变为零", "becomes zero"), ("加倍", "doubles"))),
    X("chemistry-8Cp-2", type="mcq", id="q-ch-8Cp-pa08",
      stem_zh="只有一个斑点，是否一定证明样品是纯净物？", stem_en="Does a single spot always prove that a sample is pure?",
      answer="a", exp_zh="在该溶剂中可能有两种物质走得一样远；单斑点是支持证据，但不是绝对证明。", exp_en="Two substances might travel the same distance in that solvent; a single spot is supporting evidence, not absolute proof.",
      options=opts(("不一定，可能只是该溶剂无法分开某些成分", "not necessarily; the solvent might not separate some substances"),
                   ("一定，因为 $R_f$ 只能是整数", "yes, because $R_f$ must be a whole number"),
                   ("一定，因为混合物不能产生斑点", "yes, because mixtures cannot produce spots"),
                   ("不一定，因为纯净物必须有三个斑点", "not necessarily, because a pure substance must show three spots"))),
    X("chemistry-8Cp-1", type="short", id="q-ch-8Cp-pa09",
      stem_zh="写出浓度的计算公式（质量与体积）。", stem_en="Write the formula for concentration (mass and volume).",
      answer="mass/volume", accepted=["mass/volume", "c=m/v", "C=m/V", "concentration = mass/volume", "浓度=质量/体积", "溶质质量/溶液体积"],
      answer_zh="浓度 $=$ 溶质质量 $/$ 溶液体积。", answer_en="concentration $=$ mass of solute $/$ volume of solution.",
      exp_zh="单位要配套。", exp_en="Keep the units consistent."),
    X("chemistry-8Cp-2", type="mcq", id="q-ch-8Cp-pa10",
      stem_zh="量 $R_f$ 时，斑点距离应量到？", stem_en="When measuring $R_f$, the spot distance should be taken to the:",
      answer="b", exp_zh="通常量到斑点中心。", exp_en="Usually to the centre of the spot.",
      options=opts(("烧杯底部", "bottom of the beaker"), ("斑点中心", "centre of the spot"),
                   ("实验室门口", "door of the laboratory"), ("溶剂瓶的商标", "label on the solvent bottle"))),
    X("chemistry-8Cp-1", type="numeric", id="q-ch-8Cp-pa11",
      stem_zh="要把 $6.0\\ \\mathrm{g}$ 溶质配成 $20\\ \\mathrm{g/dm^3}$ 的溶液，需要多少 $\\mathrm{dm^3}$ 溶液体积？",
      stem_en="What volume of solution, in $\\mathrm{dm^3}$, is needed to make a $20\\ \\mathrm{g/dm^3}$ solution containing $6.0\\ \\mathrm{g}$ of solute?",
      answer=0.3, exp_zh="体积 $=$ 质量 $/$ 浓度 $=6.0/20=0.30\\ \\mathrm{dm^3}$。", exp_en="Volume $=$ mass $/$ concentration $=6.0/20=0.30\\ \\mathrm{dm^3}$.", tolerance=0.01),
])

CC_PR = add_extra_questions(C, [
    X("chemistry-8Cc-1", type="short", id="q-ch-8Cc-pr01",
      stem_zh="写出碳完全燃烧生成二氧化碳的文字方程式。", stem_en="Write the word equation for carbon burning completely to form carbon dioxide.",
      answer="carbon + oxygen -> carbon dioxide",
      accepted=["carbon + oxygen -> carbon dioxide", "carbon + oxygen → carbon dioxide", "碳+氧气→二氧化碳", "碳 + 氧气 → 二氧化碳"],
      answer_zh="碳 $+$ 氧气 $\\rightarrow$ 二氧化碳", answer_en="carbon $+$ oxygen $\\rightarrow$ carbon dioxide",
      exp_zh="反应物在左，生成物在右。", exp_en="Reactants on the left, product on the right."),
    X("chemistry-8Cc-1", type="mcq", id="q-ch-8Cc-pr02",
      stem_zh="文字方程式的箭头表示？", stem_en="The arrow in a word equation means:",
      answer="b", exp_zh="表示反应生成（方向），不是普通等号。", exp_en="It means “react to form” (a direction), not an ordinary equals sign.",
      options=opts(("两边温度一定相同", "the temperatures must be equal"), ("反应生成（方向）", "react to form (a direction)"),
                   ("溶质质量除以体积", "mass of solute divided by volume"), ("样品一定纯", "the sample must be pure"))),
    X("chemistry-8Cc-2", type="mcq", id="q-ch-8Cc-pr03",
      stem_zh="混合物温度下降，该过程最可能是？", stem_en="If the temperature of a mixture falls, the process is most likely:",
      answer="a", exp_zh="周围温度降低，通常是吸热。", exp_en="The surroundings got colder, so it is usually endothermic.",
      options=opts(("吸热", "endothermic"), ("放热", "exothermic"), ("没有能量变化", "there is no energy change"), ("一定是燃烧", "combustion for certain"))),
    X("chemistry-8Cc-2", type="mcq", id="q-ch-8Cc-pr04",
      stem_zh="燃烧通常是？", stem_en="Combustion is usually:",
      answer="c", exp_zh="燃烧向周围释放能量，是放热。", exp_en="Combustion releases energy to the surroundings, so it is exothermic.",
      options=opts(("吸热，因为要点火", "endothermic, because it is lit"), ("与温度无关", "unrelated to temperature"),
                   ("放热", "exothermic"), ("只会降低周围温度", "only able to cool the surroundings"))),
    X("chemistry-8Cc-3", type="mcq", id="q-ch-8Cc-pr05",
      stem_zh="更活泼的金属可以？", stem_en="A more reactive metal can:",
      answer="d", exp_zh="把较不活泼的金属从它的化合物溶液中置换出来。", exp_en="Displace a less reactive metal from a solution of its compound.",
      options=opts(("把所有更活泼的金属都置换出来", "displace every metal that is more reactive"),
                   ("把金变成钾", "turn gold into potassium"),
                   ("使文字方程式不能书写", "make word equations impossible"),
                   ("置换较不活泼金属的化合物溶液中的该金属", "displace a less reactive metal from a solution of its compound"))),
    X("chemistry-8Cc-4", type="mcq", id="q-ch-8Cc-pr06",
      stem_zh="样品中的惰性杂质通常会使有用产物？", stem_en="An inert impurity in a sample usually makes the useful product:",
      answer="a", exp_zh="可反应的反应物变少，有用产物质量减少。", exp_en="Less reactant can react, so the mass of useful product falls.",
      options=opts(("质量比纯样品时更少", "smaller in mass than with a pure sample"), ("质量一定增加", "larger in mass for certain"),
                   ("变成可再生资源", "become a renewable resource"), ("熔点自动变得更尖锐", "have a sharper melting point automatically"))),
    X("chemistry-8Cc-5", type="numeric", id="q-ch-8Cc-pr07",
      stem_zh="某盐在 $30^\\circ\\mathrm{C}$ 溶解度 $40\\ \\mathrm{g}/100\\ \\mathrm{g}$ 水，在 $80^\\circ\\mathrm{C}$ 为 $90\\ \\mathrm{g}/100\\ \\mathrm{g}$ 水。$100\\ \\mathrm{g}$ 水的饱和溶液从 $80^\\circ\\mathrm{C}$ 冷到 $30^\\circ\\mathrm{C}$，约析出多少克？",
      stem_en="A salt has solubility $40\\ \\mathrm{g}/100\\ \\mathrm{g}$ water at $30^\\circ\\mathrm{C}$ and $90\\ \\mathrm{g}/100\\ \\mathrm{g}$ water at $80^\\circ\\mathrm{C}$. A saturated solution in $100\\ \\mathrm{g}$ water cools from $80^\\circ\\mathrm{C}$ to $30^\\circ\\mathrm{C}$. Grams of crystals, approximately?",
      answer=50, exp_zh="$90-40=50\\ \\mathrm{g}$。", exp_en="$90-40=50\\ \\mathrm{g}$.", tolerance=0),
    X("chemistry-8Cc-5", type="mcq", id="q-ch-8Cc-pr08",
      stem_zh="大多数盐的溶解度随温度升高通常？", stem_en="As temperature rises, the solubility of most salts usually:",
      answer="b", exp_zh="大多数盐溶解度增大。", exp_en="The solubility of most salts increases.",
      options=opts(("减小到零", "falls to zero"), ("增大", "increases"), ("与温度无关", "does not change with temperature"), ("变成 $R_f$", "becomes an $R_f$ value"))),
])

CC_PA = add_extra_questions(C, [
    X("chemistry-8Cc-1", type="short", id="q-ch-8Cc-pa01",
      stem_zh="写出镁在氧气中燃烧生成氧化镁的文字方程式。", stem_en="Write the word equation for magnesium burning in oxygen to form magnesium oxide.",
      answer="magnesium + oxygen -> magnesium oxide",
      accepted=["magnesium + oxygen -> magnesium oxide", "magnesium + oxygen → magnesium oxide", "镁+氧气→氧化镁", "镁 + 氧气 → 氧化镁"],
      answer_zh="镁 $+$ 氧气 $\\rightarrow$ 氧化镁", answer_en="magnesium $+$ oxygen $\\rightarrow$ magnesium oxide",
      exp_zh="反应物在左，生成物在右。", exp_en="Reactants left, product right."),
    X("chemistry-8Cc-1", type="mcq", id="q-ch-8Cc-pa02",
      stem_zh="氢气燃烧生成水。哪一项把生成物写对了位置？", stem_en="Hydrogen burns to form water. Which places the product correctly?",
      answer="c", exp_zh="水是生成物，应在箭头右边。", exp_en="Water is the product, so it belongs on the right of the arrow.",
      options=opts(("水 $+$ 氢气 $\\rightarrow$ 氧气", "water $+$ hydrogen $\\rightarrow$ oxygen"),
                   ("水 $\\rightarrow$ 氢气 $+$ 氧气（作为该燃烧的正向方程式）", "water $\\rightarrow$ hydrogen $+$ oxygen, as the forward combustion equation"),
                   ("氢气 $+$ 氧气 $\\rightarrow$ 水", "hydrogen $+$ oxygen $\\rightarrow$ water"),
                   ("氧气 $\\rightarrow$ 氢气", "oxygen $\\rightarrow$ hydrogen"))),
    X("chemistry-8Cc-2", type="mcq", id="q-ch-8Cc-pa03",
      stem_zh="温度从 $18^\\circ\\mathrm{C}$ 升到 $26^\\circ\\mathrm{C}$ 的反应是？", stem_en="A reaction whose mixture rises from $18^\\circ\\mathrm{C}$ to $26^\\circ\\mathrm{C}$ is:",
      answer="a", exp_zh="周围温度升高，是放热。", exp_en="The surroundings warmed, so it is exothermic.",
      options=opts(("放热", "exothermic"), ("吸热", "endothermic"), ("既不放热也不吸热", "neither"), ("只能在真空中发生", "possible only in a vacuum"))),
    X("chemistry-8Cc-2", type="mcq", id="q-ch-8Cc-pa04",
      stem_zh="需要持续加热才能进行的热分解，通常是？", stem_en="A thermal decomposition that needs continuous heating is usually:",
      answer="b", exp_zh="不断从周围吸能，通常是吸热。", exp_en="It takes in energy from the surroundings, so it is usually endothermic.",
      options=opts(("放热", "exothermic"), ("吸热", "endothermic"), ("与能量无关", "unrelated to energy"), ("浓度计算错误", "a concentration error"))),
    X("chemistry-8Cc-3", type="mcq", id="q-ch-8Cc-pa05",
      stem_zh="锌放入硫酸铜溶液，铜放入硫酸锌溶液。预期是？", stem_en="Zinc is placed in copper sulfate, and copper is placed in zinc sulfate. You expect:",
      answer="d", exp_zh="锌能置换铜；铜不能置换锌。", exp_en="Zinc can displace copper; copper cannot displace zinc.",
      options=opts(("两次都没有反应", "no reaction in either case"), ("两次都置换得同样彻底", "equally complete displacement in both"),
                   ("只有铜能置换锌", "only copper can displace zinc"), ("只有锌能置换铜", "only zinc can displace copper"))),
    X("chemistry-8Cc-3", type="mcq", id="q-ch-8Cc-pa06",
      stem_zh="下列通常最活泼的是？", stem_en="Which is usually the most reactive?",
      answer="a", exp_zh="钾很活泼；铜、银、金都不活泼。", exp_en="Potassium is highly reactive; copper, silver and gold are not.",
      options=opts(("钾", "potassium"), ("铜", "copper"), ("银", "silver"), ("金", "gold"))),
    X("chemistry-8Cc-4", type="mcq", id="q-ch-8Cc-pa07",
      stem_zh="同样质量的镁，混有不反应杂质的那一份在足量氧气中燃烧，氧化镁会？",
      stem_en="Two equal masses of magnesium are burned in excess oxygen. The sample mixed with an unreactive impurity produces:",
      answer="c", exp_zh="可反应的镁更少，氧化镁更少。", exp_en="Less magnesium can react, so less magnesium oxide is produced.",
      options=opts(("更多氧化镁", "more magnesium oxide"), ("与纯样品完全一样多", "exactly as much as the pure sample"),
                   ("更少氧化镁", "less magnesium oxide"), ("只生成沙子", "only sand"))),
    X("chemistry-8Cc-4", type="mcq", id="q-ch-8Cc-pa08",
      stem_zh="收集到的产物不纯，可能是因为？", stem_en="A collected product may be impure because:",
      answer="b", exp_zh="可能混有未反应物、其他生成物或原有杂质。", exp_en="It may still contain unreacted starting material, other products or original impurities.",
      options=opts(("文字方程式禁止提纯", "word equations forbid purification"),
                   ("可能混有未反应物或其他物质", "unreacted material or other substances may still be mixed with it"),
                   ("纯净物不能有熔点", "pure substances cannot have melting points"),
                   ("惰性物质一定增加目标产物", "inert substances always increase the target product"))),
    X("chemistry-8Cc-5", type="numeric", id="q-ch-8Cc-pa09",
      stem_zh="某盐 $20^\\circ\\mathrm{C}$ 溶解度 $25\\ \\mathrm{g}/100\\ \\mathrm{g}$ 水，$60^\\circ\\mathrm{C}$ 为 $70\\ \\mathrm{g}/100\\ \\mathrm{g}$ 水。$100\\ \\mathrm{g}$ 水的饱和溶液从 $60^\\circ\\mathrm{C}$ 冷到 $20^\\circ\\mathrm{C}$，约析出多少克？",
      stem_en="Solubility is $25\\ \\mathrm{g}/100\\ \\mathrm{g}$ water at $20^\\circ\\mathrm{C}$ and $70\\ \\mathrm{g}/100\\ \\mathrm{g}$ water at $60^\\circ\\mathrm{C}$. Saturated solution in $100\\ \\mathrm{g}$ water cools from $60^\\circ\\mathrm{C}$ to $20^\\circ\\mathrm{C}$. Approximate grams of crystals?",
      answer=45, exp_zh="$70-25=45\\ \\mathrm{g}$。", exp_en="$70-25=45\\ \\mathrm{g}$.", tolerance=0),
    X("chemistry-8Cc-5", type="mcq", id="q-ch-8Cc-pa10",
      stem_zh="饱和溶液是指在该温度下？", stem_en="A saturated solution at a given temperature:",
      answer="a", exp_zh="已溶解最大量溶质，再加固体会剩下。", exp_en="Already holds the maximum solute; extra solid remains undissolved.",
      options=opts(("不能再溶解更多溶质", "cannot dissolve any more solute"), ("完全没有溶质", "contains no solute"),
                   ("温度必须高于 $100^\\circ\\mathrm{C}$", "must be above $100^\\circ\\mathrm{C}$"), ("一定是元素", "must be an element"))),
    X("chemistry-8Cc-3", type="short", id="q-ch-8Cc-pa11",
      stem_zh="写出锌与硫酸铜反应的文字方程式。", stem_en="Write the word equation for zinc with copper sulfate.",
      answer="zinc + copper sulfate -> zinc sulfate + copper",
      accepted=["zinc + copper sulfate -> zinc sulfate + copper", "zinc + copper sulfate → zinc sulfate + copper", "锌+硫酸铜→硫酸锌+铜", "锌 + 硫酸铜 → 硫酸锌 + 铜"],
      answer_zh="锌 $+$ 硫酸铜 $\\rightarrow$ 硫酸锌 $+$ 铜", answer_en="zinc $+$ copper sulfate $\\rightarrow$ zinc sulfate $+$ copper",
      exp_zh="锌更活泼，置换出铜。", exp_en="More reactive zinc displaces copper."),
    X("chemistry-8Cc-2", type="mcq", id="q-ch-8Cc-pa12",
      stem_zh="判断放热或吸热，最直接的课堂证据常常是？", stem_en="In class, the most direct evidence for exothermic or endothermic is often:",
      answer="d", exp_zh="测量周围或混合物的温度变化。", exp_en="Measuring the temperature change of the surroundings or the mixture.",
      options=opts(("$R_f$ 值", "the $R_f$ value"), ("原子核电荷", "nuclear charge"),
                   ("金属是不是金色", "whether the metal looks gold"), ("温度升高还是降低", "whether the temperature rises or falls"))),
])

ES_PR = add_extra_questions(C, [
    X("chemistry-8ES-1", type="mcq", id="q-ch-8ES-pr01",
      stem_zh="石油属于？", stem_en="Oil is:",
      answer="b", exp_zh="石油形成极慢，是不可再生资源。", exp_en="Oil forms far too slowly, so it is non-renewable.",
      options=opts(("可再生资源", "a renewable resource"), ("不可再生资源", "a non-renewable resource"),
                   ("一种气候，不是资源", "a type of climate, not a resource"), ("纯净的元素气体", "a pure elemental gas"))),
    X("chemistry-8ES-1", type="mcq", id="q-ch-8ES-pr02",
      stem_zh="风能通常被归为？", stem_en="Wind energy is usually classed as:",
      answer="a", exp_zh="能在人类时间尺度上不断获得，属于可再生。", exp_en="It can be obtained again and again on a human timescale, so it is renewable.",
      options=opts(("可再生资源", "renewable"), ("不可再生矿藏", "a non-renewable ore"),
                   ("只能是混合物", "a mixture only"), ("与资源分类无关", "unrelated to resource classification"))),
    X("chemistry-8ES-1", type="mcq", id="q-ch-8ES-pr03",
      stem_zh="回收金属的主要意义之一是？", stem_en="One main reason to recycle metals is to:",
      answer="c", exp_zh="减少对新矿的依赖并节省提炼能量。", exp_en="Reduce demand for new ore and save extraction energy.",
      options=opts(("让矿藏立刻变成可再生", "make the ore renewable at once"), ("禁止所有金属使用", "ban all use of metals"),
                   ("减少开采并节省能量", "reduce mining and save energy"), ("把气候改名为天气", "rename climate as weather"))),
    X("chemistry-8ES-2", type="mcq", id="q-ch-8ES-pr04",
      stem_zh="“今天最高气温 $32^\\circ\\mathrm{C}$”描述的是？", stem_en="“Today’s maximum temperature is $32^\\circ\\mathrm{C}$” describes:",
      answer="d", exp_zh="针对具体一天，是天气。", exp_en="It refers to a particular day, so it is weather.",
      options=opts(("长期气候循环的全部历史", "the whole history of long-term climate cycles"),
                   ("一种不可再生资源", "a non-renewable resource"),
                   ("原子结构", "atomic structure"),
                   ("天气", "weather"))),
    X("chemistry-8ES-2", type="mcq", id="q-ch-8ES-pr05",
      stem_zh="长期平均降雨和气温型态属于？", stem_en="A long-term pattern of average rainfall and temperature is:",
      answer="a", exp_zh="这是气候。", exp_en="This is climate.",
      options=opts(("气候", "climate"), ("只是下一小时的预报", "only the forecast for the next hour"),
                   ("纯度", "purity"), ("层析", "chromatography"))),
    X("chemistry-8ES-2", type="short", id="q-ch-8ES-pr06",
      stem_zh="为什么一两天的天气不能单独否定长期气候趋势？", stem_en="Why can a day or two of weather not, by itself, disprove a long-term climate trend?",
      answer="climate needs a long record",
      accepted=["climate needs a long record", "weather is short term", "气候看长期，天气是短期", "短期天气不能单独推翻长期记录", "时间尺度不同"],
      answer_zh="天气是短期的，气候趋势需要长期记录。", answer_en="Weather is short-term; a climate trend needs a long record.",
      exp_zh="不能用几天的波动代替几十年的型态。", exp_en="A few days of fluctuation cannot replace a pattern over decades."),
    X("chemistry-8ES-3", type="mcq", id="q-ch-8ES-pr07",
      stem_zh="地球气候在很长的时间里？", stem_en="Over very long times, Earth’s climate:",
      answer="b", exp_zh="会变化，存在冰期等长期循环。", exp_en="Can change; there are long-term cycles such as ice ages.",
      options=opts(("从未变化", "has never changed"), ("可以变化，存在长期循环", "can change, and there are long-term cycles"),
                   ("每分钟精确重复", "repeats exactly every minute"), ("与大气完全无关", "is completely unrelated to the atmosphere"))),
    X("chemistry-8ES-3", type="mcq", id="q-ch-8ES-pr08",
      stem_zh="燃烧化石燃料与气候相关，是因为可能？", stem_en="Burning fossil fuels is linked to climate because it may:",
      answer="a", exp_zh="改变大气成分，影响地球保留的能量。", exp_en="Change atmospheric composition, affecting how much energy Earth keeps.",
      options=opts(("改变大气成分，影响地球保留的能量", "change the atmosphere and how much energy Earth keeps"),
                   ("把所有资源变为可再生", "make every resource renewable"),
                   ("停止天气出现", "stop weather occurring"),
                   ("只改变中子电荷", "only change the charge of neutrons"))),
])

ES_PA = add_extra_questions(C, [
    X("chemistry-8ES-1", type="mcq", id="q-ch-8ES-pa01",
      stem_zh="煤属于不可再生资源，主要因为？", stem_en="Coal is non-renewable mainly because:",
      answer="c", exp_zh="自然形成远慢于被消耗。", exp_en="It forms naturally far more slowly than it is used.",
      options=opts(("它不能燃烧", "it cannot be burned"), ("它是一种天气", "it is a type of weather"),
                   ("形成速度远慢于使用速度", "it forms far more slowly than it is used"), ("它一定是纯净的元素", "it must be a pure element"))),
    X("chemistry-8ES-1", type="mcq", id="q-ch-8ES-pa02",
      stem_zh="可持续管理的木材通常可视为？", stem_en="Sustainably managed timber can usually be regarded as:",
      answer="a", exp_zh="补充跟得上使用时，属于可再生。", exp_en="If replacement keeps up with use, it is renewable.",
      options=opts(("可再生资源", "a renewable resource"), ("金属矿", "a metal ore"),
                   ("不可再生化石燃料", "a non-renewable fossil fuel"), ("一种 $R_f$ 值", "an $R_f$ value"))),
    X("chemistry-8ES-1", type="mcq", id="q-ch-8ES-pa03",
      stem_zh="“可再生”等于“完全没有环境影响”吗？", stem_en="Does “renewable” mean “zero environmental impact”?",
      answer="b", exp_zh="分类依据是能否补充，不是零影响。", exp_en="The test is whether it can be replaced, not whether use has zero impact.",
      options=opts(("是，定义就是零影响", "yes, that is the definition"), ("不是，分类依据是能否在人类时间尺度上补充", "no, the test is whether it can be replaced on a human timescale"),
                   ("是，所以水电站没有任何生态影响", "yes, so a dam has no ecological effects"), ("不是，因为可再生资源不能被使用", "no, because renewable resources cannot be used"))),
    X("chemistry-8ES-2", type="mcq", id="q-ch-8ES-pa04",
      stem_zh="“该地全年高温多雨是多年平均状况”描述的是？", stem_en="“The place is hot and wet through the year, as a long-term average” describes:",
      answer="d", exp_zh="长期型态是气候。", exp_en="A long-term pattern is climate.",
      options=opts(("明天的小时预报", "an hourly forecast for tomorrow"), ("一次火山喷发的全部影响", "the entire effect of one volcanic eruption"),
                   ("溶液浓度", "concentration of a solution"), ("气候", "climate"))),
    X("chemistry-8ES-2", type="mcq", id="q-ch-8ES-pa05",
      stem_zh="连续几天偏凉，最准确的说法是？", stem_en="A run of cooler days is most accurately described as:",
      answer="a", exp_zh="这是天气的短期变化，不能单独改写气候定义。", exp_en="It is short-term weather and does not, by itself, rewrite the climate.",
      options=opts(("天气的短期变化", "a short-term weather variation"), ("气候已经变成极地", "the climate has become polar"),
                   ("证明长期循环不存在", "proof that long-term cycles do not exist"), ("资源分类的唯一依据", "the only basis for classifying resources"))),
    X("chemistry-8ES-2", type="short", id="q-ch-8ES-pa06",
      stem_zh="写出天气和气候在时间尺度上的差别。", stem_en="State the difference in timescale between weather and climate.",
      answer="weather short term, climate long term",
      accepted=["weather short term, climate long term", "weather: days; climate: decades", "天气短期，气候长期", "天气看天或周，气候看年或十年"],
      answer_zh="天气是短期的，气候是长期的。", answer_en="Weather is short-term; climate is long-term.",
      exp_zh="气候通常用多年至几十年的记录来描述。", exp_en="Climate is usually described with a record of many years to decades."),
    X("chemistry-8ES-3", type="mcq", id="q-ch-8ES-pa07",
      stem_zh="大规模火山喷发可能暂时使地表变凉，因为？", stem_en="A large eruption may cool the surface for a time because:",
      answer="c", exp_zh="尘埃和气体可能挡住部分阳光。", exp_en="Dust and gases may block some sunlight.",
      options=opts(("它停止了地球公转", "it stops Earth orbiting"), ("它把气候改写成天气这个词", "it renames climate as weather"),
                   ("尘埃和气体进入大气，可能挡住部分阳光", "dust and gases enter the atmosphere and may block some sunlight"),
                   ("它使所有盐立即结晶", "it makes every salt crystallise at once"))),
    X("chemistry-8ES-3", type="mcq", id="q-ch-8ES-pa08",
      stem_zh="大气成分变化可能影响气候，是因为它可以影响？", stem_en="A change in atmospheric composition may affect climate because it can affect:",
      answer="b", exp_zh="某些气体影响地球保留多少能量。", exp_en="Some gases affect how much energy Earth keeps.",
      options=opts(("质子的相对电荷（使之变成 $-4$）", "the relative charge of a proton, turning it into $-4$"),
                   ("地球保留多少能量", "how much energy Earth keeps"),
                   ("纸层析必须用钢笔的规定", "a rule that chromatography must use ink"),
                   ("明天一小时的唯一天气定义", "the only possible definition of one hour of weather"))),
    X("chemistry-8ES-3", type="mcq", id="q-ch-8ES-pa09",
      stem_zh="承认存在自然气候循环，意味着？", stem_en="Recognising natural climate cycles means:",
      answer="a", exp_zh="自然循环可以与人类对大气的额外影响同时存在。", exp_en="Natural cycles can exist alongside extra human influences on the atmosphere.",
      options=opts(("自然循环与人类影响可以同时存在", "natural cycles and human influences can exist together"),
                   ("今天任何大气变化都不可能与人类有关", "no atmospheric change today can involve humans"),
                   ("天气不再存在", "weather no longer exists"),
                   ("化石燃料是可再生的", "fossil fuels are renewable"))),
    X("chemistry-8ES-1", type="short", id="q-ch-8ES-pa10",
      stem_zh="各举一个可再生与不可再生资源的例子。", stem_en="Give one renewable and one non-renewable example.",
      answer="solar and coal",
      accepted=["solar and coal", "wind and oil", "hydro and natural gas", "sustainable timber and coal",
                "太阳能和煤", "风能和石油", "水电和天然气", "可持续木材和煤"],
      answer_zh="例如太阳能与煤。", answer_en="For example solar energy and coal.",
      exp_zh="分类正确即可。", exp_en="Any correctly classified pair is fine."),
    X("chemistry-8ES-3", type="mcq", id="q-ch-8ES-pa11",
      stem_zh="地球轨道或地轴倾斜的缓慢变化，可能影响气候，是因为会改变？", stem_en="Slow changes in Earth’s orbit or tilt may affect climate because they change:",
      answer="d", exp_zh="到达不同地区的阳光分布会改变。", exp_en="They change how sunlight is distributed across the Earth.",
      options=opts(("质子质量变为零", "the mass of a proton to zero"), ("金属反应性顺序的课堂名称", "the classroom name of the reactivity series"),
                   ("$R_f$ 必须大于 $2$", "$R_f$, which must then exceed $2$"), ("到达不同地区的阳光分布", "how sunlight is distributed"))),
])

COMP = add_extra_questions(C, [
    X("chemistry-8Cm-1", type="mcq", id="q-ch-comp-01",
      stem_zh="卢瑟福模型中，原子核含有？", stem_en="In the Rutherford model, the nucleus contains:",
      answer="b", exp_zh="质子和中子；电子在核外空间。", exp_en="Protons and neutrons; electrons are in the space around it.",
      options=opts(("只有电子", "electrons only"), ("质子和中子", "protons and neutrons"),
                   ("只有电子和中子", "electrons and neutrons only"), ("均匀的正电布丁", "a spread-out positive pudding"))),
    X("chemistry-8Cm-2", type="numeric", id="q-ch-comp-02",
      stem_zh="中性原子有 $20$ 个质子。电子数是多少？", stem_en="A neutral atom has $20$ protons. How many electrons does it have?",
      answer=20, exp_zh="中性原子电子数等于质子数。", exp_en="Electrons equal protons in a neutral atom.", tolerance=0),
    X("chemistry-8Cm-3", type="mcq", id="q-ch-comp-03",
      stem_zh="核把电子留在周围，靠的是？", stem_en="The nucleus holds electrons around it by:",
      answer="a", exp_zh="异种电荷的静电吸引。", exp_en="Electrostatic attraction between opposite charges.",
      options=opts(("静电吸引", "electrostatic attraction"), ("中子的负电荷", "the negative charge of neutrons"),
                   ("电子比核更重", "electrons being heavier than the nucleus"), ("同种电荷相吸", "like charges attracting"))),
    X("chemistry-8Cm-4", type="mcq", id="q-ch-comp-04",
      stem_zh="杂质对固体熔点的典型影响是使之？", stem_en="Impurities typically make the melting point of a solid:",
      answer="c", exp_zh="降低并且熔程变宽。", exp_en="Lower, with a wider range.",
      options=opts(("升高且更尖锐", "higher and sharper"), ("无法被讨论", "impossible to discuss"),
                   ("降低且熔程变宽", "lower, with a wider range"), ("永远等于溶剂前沿", "always equal to the solvent front"))),
    X("chemistry-8Cp-1", type="numeric", id="q-ch-comp-05",
      stem_zh="$16\\ \\mathrm{g}$ 溶质配成 $0.40\\ \\mathrm{dm^3}$ 溶液。浓度是多少 $\\mathrm{g/dm^3}$？",
      stem_en="$16\\ \\mathrm{g}$ of solute is made up to $0.40\\ \\mathrm{dm^3}$. Concentration in $\\mathrm{g/dm^3}$?",
      answer=40, exp_zh="$16/0.40=40$。", exp_en="$16/0.40=40$.", tolerance=0),
    X("chemistry-8Cp-2", type="numeric", id="q-ch-comp-06",
      stem_zh="溶剂移动 $5.0\\ \\mathrm{cm}$，斑点移动 $3.0\\ \\mathrm{cm}$。$R_f$？",
      stem_en="Solvent travels $5.0\\ \\mathrm{cm}$, spot travels $3.0\\ \\mathrm{cm}$. $R_f$?",
      answer=0.6, exp_zh="$3.0/5.0=0.60$。", exp_en="$3.0/5.0=0.60$.", tolerance=0.01),
    X("chemistry-8Cc-1", type="short", id="q-ch-comp-07",
      stem_zh="写出氢气在氧气中燃烧生成水的文字方程式。", stem_en="Write the word equation for hydrogen burning in oxygen to form water.",
      answer="hydrogen + oxygen -> water",
      accepted=["hydrogen + oxygen -> water", "hydrogen + oxygen → water", "氢气+氧气→水", "氢＋氧→水", "氢气 + 氧气 → 水"],
      answer_zh="氢气 $+$ 氧气 $\\rightarrow$ 水", answer_en="hydrogen $+$ oxygen $\\rightarrow$ water",
      exp_zh="反应物在左，水在右。", exp_en="Reactants on the left, water on the right."),
    X("chemistry-8Cc-2", type="mcq", id="q-ch-comp-08",
      stem_zh="放热过程中，周围温度通常？", stem_en="In an exothermic process, the temperature of the surroundings usually:",
      answer="d", exp_zh="向周围释放能量，温度升高。", exp_en="Energy is released to the surroundings, so the temperature rises.",
      options=opts(("降低", "falls"), ("保持无法测量", "becomes unmeasurable"),
                   ("必须降到 $0^\\circ\\mathrm{C}$", "must fall to $0^\\circ\\mathrm{C}$"), ("升高", "rises"))),
    X("chemistry-8Cc-3", type="mcq", id="q-ch-comp-09",
      stem_zh="铁能否置换硫酸铜中的铜？", stem_en="Can iron displace copper from copper sulfate?",
      answer="a", exp_zh="铁比铜活泼，可以置换。", exp_en="Iron is more reactive than copper, so it can.",
      options=opts(("能，因为铁更活泼", "yes, because iron is more reactive"), ("不能，因为铁最不活泼", "no, because iron is the least reactive metal"),
                   ("能，因为铜更活泼", "yes, because copper is more reactive"), ("不能，因为置换只发生在气体中", "no, because displacement happens only in gases"))),
    X("chemistry-8Cc-5", type="numeric", id="q-ch-comp-10",
      stem_zh="某盐 $20^\\circ\\mathrm{C}$ 溶解度 $20\\ \\mathrm{g}/100\\ \\mathrm{g}$ 水，$80^\\circ\\mathrm{C}$ 为 $65\\ \\mathrm{g}/100\\ \\mathrm{g}$ 水。$100\\ \\mathrm{g}$ 水的饱和溶液从 $80^\\circ\\mathrm{C}$ 冷到 $20^\\circ\\mathrm{C}$，约析出多少克？",
      stem_en="Solubility $20\\ \\mathrm{g}/100\\ \\mathrm{g}$ water at $20^\\circ\\mathrm{C}$ and $65\\ \\mathrm{g}/100\\ \\mathrm{g}$ water at $80^\\circ\\mathrm{C}$. Saturated solution in $100\\ \\mathrm{g}$ water cools from $80^\\circ\\mathrm{C}$ to $20^\\circ\\mathrm{C}$. Approximate grams of crystals?",
      answer=45, exp_zh="$65-20=45\\ \\mathrm{g}$。", exp_en="$65-20=45\\ \\mathrm{g}$.", tolerance=0),
    X("chemistry-8Cc-4", type="mcq", id="q-ch-comp-11",
      stem_zh="惰性杂质使同样质量样品产生的有用产物通常？", stem_en="An inert impurity usually makes the useful product from the same mass of sample:",
      answer="b", exp_zh="可反应物变少，产物减少。", exp_en="Less reactant can react, so there is less product.",
      options=opts(("增加", "increase"), ("减少", "decrease"), ("变成气候", "become climate"), ("使 $R_f>1$", "force $R_f>1$"))),
    X("chemistry-8ES-1", type="mcq", id="q-ch-comp-12",
      stem_zh="太阳能通常属于？", stem_en="Solar energy is usually:",
      answer="a", exp_zh="可在人类时间尺度上不断获得，是可再生资源。", exp_en="It can be obtained on a human timescale, so it is renewable.",
      options=opts(("可再生资源", "a renewable resource"), ("不可再生化石燃料", "a non-renewable fossil fuel"),
                   ("一种金属矿", "a metal ore"), ("只存在于实验室的纯中子", "pure neutrons that exist only in laboratories"))),
    X("chemistry-8ES-2", type="mcq", id="q-ch-comp-13",
      stem_zh="气候与天气的主要差别是？", stem_en="The main difference between climate and weather is:",
      answer="c", exp_zh="天气是短期状况，气候是长期型态。", exp_en="Weather is short-term; climate is the long-term pattern.",
      options=opts(("气候不能被描述", "climate cannot be described"), ("天气必须持续三十年才能叫天气", "weather must last thirty years to be called weather"),
                   ("天气是短期的，气候是长期的平均型态", "weather is short-term; climate is the long-term average pattern"),
                   ("二者完全相同", "they are exactly the same"))),
    X("chemistry-8ES-3", type="mcq", id="q-ch-comp-14",
      stem_zh="下列哪一项是可能影响气候的自然因素？", stem_en="Which of these is a natural factor that can affect climate?",
      answer="d", exp_zh="大规模火山喷发可把尘埃和气体送进大气。", exp_en="A large volcanic eruption can inject dust and gases into the atmosphere.",
      options=opts(("把起点线画进溶剂", "placing the baseline in the solvent"), ("测量一个样品的 $R_f$ 且条件完全不同却直接比较", "comparing $R_f$ values from completely different conditions"),
                   ("把电子画进原子核并称之为唯一气候原因", "putting electrons in the nucleus and calling that the only cause of climate"),
                   ("大规模火山喷发", "a large volcanic eruption"))),
    X("chemistry-8ES-3", type="mcq", id="q-ch-comp-15",
      stem_zh="下列说法较准确的是？", stem_en="Which statement is the fairest?",
      answer="a", exp_zh="自然的长期循环存在，同时人类活动也可以额外改变大气。", exp_en="Natural long-term cycles exist, and human activity can also change the atmosphere further.",
      options=opts(("自然循环存在，人类活动也可以额外改变大气", "natural cycles exist, and human activity can also change the atmosphere further"),
                   ("只要过去有过冰期，今天大气成分就不可能受人类影响", "ice ages in the past mean the atmosphere cannot be affected by humans today"),
                   ("天气等于气候，也等于资源分类", "weather equals climate and also equals resource classification"),
                   ("化石燃料是可再生的，因为它们能燃烧", "fossil fuels are renewable because they can burn"))),
])

# Apply lessons now (after helpers exist; lessons were only stored)
for lesson in LESSONS:
    add_lesson(C, lesson)

add_sets(C, [
    dict(kind="practice", chapter="chemistry-8Cm", title_zh="本章练习 · 物质及其结构", title_en="Chapter practice · Materials and their structure", qids=CM_PR, minutes=15),
    dict(kind="paper", chapter="chemistry-8Cm", title_zh="本章测试卷 · 物质及其结构", title_en="Chapter test · Materials and their structure", qids=CM_PA, minutes=25),
    dict(kind="practice", chapter="chemistry-8Cp", title_zh="本章练习 · 物质的性质", title_en="Chapter practice · Properties of materials", qids=CP_PR, minutes=15),
    dict(kind="paper", chapter="chemistry-8Cp", title_zh="本章测试卷 · 物质的性质", title_en="Chapter test · Properties of materials", qids=CP_PA, minutes=22),
    dict(kind="practice", chapter="chemistry-8Cc", title_zh="本章练习 · 物质的变化", title_en="Chapter practice · Changes to materials", qids=CC_PR, minutes=15),
    dict(kind="paper", chapter="chemistry-8Cc", title_zh="本章测试卷 · 物质的变化", title_en="Chapter test · Changes to materials", qids=CC_PA, minutes=25),
    dict(kind="practice", chapter="chemistry-8ES", title_zh="本章练习 · 地球上的循环与资源", title_en="Chapter practice · Cycles on Earth and resources", qids=ES_PR, minutes=12),
    dict(kind="paper", chapter="chemistry-8ES", title_zh="本章测试卷 · 地球上的循环与资源", title_en="Chapter test · Cycles on Earth and resources", qids=ES_PA, minutes=20),
], comprehensive=dict(
    id="paper-chemistry-8-comprehensive",
    title_zh="八年级化学综合测试卷", title_en="Grade 8 Chemistry comprehensive paper",
    qids=COMP, minutes=35, published="2026-11-12T09:00:00+08:00",
))

knowledge_ch = C.knowledge
questions_ch = C.questions
sets_ch = C.sets
