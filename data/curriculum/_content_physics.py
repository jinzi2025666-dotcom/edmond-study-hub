"""Grade 8 Physics — complete bilingual course (Cambridge Science 0893 Stage 8)."""
from _phys_util import PQ, lesson, pset, svg, INK, COPPER, opts
from _helpers import opts as _opts

def fig(src: str):
    return svg(src.replace("{INK}", INK).replace("{COP}", COPPER))

D_SPEED = fig("""
  <line x1="40" y1="180" x2="500" y2="180" {INK}/>
  <polygon points="500,180 488,174 488,186" fill="currentColor"/>
  <text x="470" y="200" font-size="13" fill="currentColor">s</text>
  <circle cx="80" cy="150" r="16" {INK}/>
  <circle cx="80" cy="150" r="3" fill="currentColor"/>
  <line x1="80" y1="166" x2="80" y2="180" {INK}/>
  <circle cx="280" cy="150" r="16" {INK}/>
  <circle cx="280" cy="150" r="3" fill="currentColor"/>
  <line x1="280" y1="166" x2="280" y2="180" {INK}/>
  <line x1="80" y1="120" x2="280" y2="120" {COP}/>
  <polygon points="280,120 268,114 268,126" fill="#b85c38"/>
  <text x="150" y="110" font-size="14" fill="#b85c38">s = 150 m</text>
  <text x="140" y="50" font-size="14" fill="currentColor">t = 10 s</text>
  <text x="320" y="155" font-size="14" fill="currentColor">v = s / t</text>
""")
D_GRAPH = fig("""
  <line x1="60" y1="200" x2="500" y2="200" {INK}/>
  <line x1="60" y1="200" x2="60" y2="20" {INK}/>
  <polygon points="60,20 54,32 66,32" fill="currentColor"/>
  <polygon points="500,200 488,194 488,206" fill="currentColor"/>
  <text x="44" y="28" font-size="12" fill="currentColor">s</text>
  <text x="490" y="216" font-size="12" fill="currentColor">t</text>
  <polyline points="60,200 200,80 320,80 460,30" {COP}/>
  <text x="110" y="160" font-size="12" fill="#b85c38">A</text>
  <text x="240" y="70" font-size="12" fill="#b85c38">B</text>
  <text x="380" y="70" font-size="12" fill="#b85c38">C</text>
""")
D_FORCES = fig("""
  <rect x="180" y="80" width="160" height="70" {INK}/>
  <text x="230" y="122" font-size="14" fill="currentColor">box</text>
  <line x1="180" y1="115" x2="80" y2="115" {COP}/>
  <polygon points="80,115 92,109 92,121" fill="#b85c38"/>
  <text x="90" y="100" font-size="13" fill="#b85c38">8 N</text>
  <line x1="340" y1="115" x2="440" y2="115" {COP}/>
  <polygon points="440,115 428,109 428,121" fill="#b85c38"/>
  <text x="360" y="100" font-size="13" fill="#b85c38">8 N</text>
  <text x="155" y="190" font-size="13" fill="currentColor">balanced, resultant = 0</text>
""")
D_MOMENT = fig("""
  <line x1="40" y1="110" x2="480" y2="110" {INK}/>
  <polygon points="260,128 248,110 272,110" fill="currentColor"/>
  <line x1="260" y1="110" x2="260" y2="170" {INK}/>
  <text x="248" y="188" font-size="12" fill="currentColor">pivot</text>
  <line x1="100" y1="110" x2="100" y2="40" {COP}/>
  <polygon points="100,40 94,52 106,52" fill="#b85c38"/>
  <text x="70" y="30" font-size="13" fill="#b85c38">F = 12 N</text>
  <line x1="100" y1="150" x2="260" y2="150" {INK} stroke-dasharray="4 3"/>
  <text x="155" y="168" font-size="12" fill="currentColor">d = 0.5 m</text>
  <text x="300" y="60" font-size="14" fill="currentColor">M = F x d</text>
""")
D_PRESSURE = fig("""
  <rect x="70" y="140" width="160" height="16" {INK}/>
  <rect x="115" y="60" width="70" height="80" {INK}/>
  <text x="125" y="50" font-size="13" fill="currentColor">same F</text>
  <text x="90" y="180" font-size="12" fill="#b85c38">larger A, smaller p</text>
  <rect x="310" y="140" width="160" height="16" {INK}/>
  <rect x="372" y="40" width="36" height="100" {INK}/>
  <text x="350" y="30" font-size="13" fill="currentColor">same F</text>
  <text x="320" y="180" font-size="12" fill="#b85c38">smaller A, larger p</text>
""")
D_PARTICLES = fig("""
  <rect x="50" y="30" width="200" height="160" {INK}/>
  <text x="110" y="24" font-size="13" fill="currentColor">gas</text>
  <circle cx="90" cy="70" r="5" fill="currentColor"/>
  <circle cx="150" cy="90" r="5" fill="currentColor"/>
  <circle cx="200" cy="60" r="5" fill="currentColor"/>
  <circle cx="120" cy="130" r="5" fill="currentColor"/>
  <circle cx="180" cy="140" r="5" fill="currentColor"/>
  <line x1="200" y1="60" x2="230" y2="48" {COP}/>
  <text x="60" y="210" font-size="12" fill="currentColor">collisions with walls give pressure</text>
  <rect x="300" y="80" width="180" height="110" {INK}/>
  <text x="350" y="74" font-size="13" fill="currentColor">liquid</text>
  <circle cx="340" cy="110" r="5" fill="currentColor"/>
  <circle cx="380" cy="120" r="5" fill="currentColor"/>
  <circle cx="420" cy="108" r="5" fill="currentColor"/>
  <circle cx="360" cy="150" r="5" fill="currentColor"/>
  <circle cx="410" cy="155" r="5" fill="currentColor"/>
  <circle cx="340" cy="170" r="5" fill="currentColor"/>
""")
D_DIFFUSION = fig("""
  <rect x="40" y="40" width="200" height="140" {INK}/>
  <rect x="240" y="40" width="200" height="140" {INK}/>
  <text x="100" y="30" font-size="13" fill="currentColor">t = 0</text>
  <text x="300" y="30" font-size="13" fill="currentColor">later</text>
  <circle cx="80" cy="80" r="4" fill="#b85c38"/>
  <circle cx="100" cy="110" r="4" fill="#b85c38"/>
  <circle cx="90" cy="140" r="4" fill="#b85c38"/>
  <circle cx="180" cy="90" r="4" fill="currentColor"/>
  <circle cx="200" cy="130" r="4" fill="currentColor"/>
  <circle cx="290" cy="80" r="4" fill="#b85c38"/>
  <circle cx="360" cy="100" r="4" fill="#b85c38"/>
  <circle cx="400" cy="140" r="4" fill="#b85c38"/>
  <circle cx="310" cy="150" r="4" fill="currentColor"/>
  <circle cx="380" cy="70" r="4" fill="currentColor"/>
  <text x="40" y="200" font-size="12" fill="currentColor">particles spread by their own motion</text>
""")
D_REFLECT = fig("""
  <line x1="40" y1="180" x2="480" y2="180" {INK}/>
  <text x="400" y="200" font-size="12" fill="currentColor">mirror</text>
  <line x1="260" y1="40" x2="260" y2="180" {INK} stroke-dasharray="4 3"/>
  <text x="268" y="54" font-size="12" fill="currentColor">normal</text>
  <line x1="80" y1="50" x2="260" y2="180" {COP}/>
  <line x1="260" y1="180" x2="440" y2="50" {COP}/>
  <text x="110" y="90" font-size="13" fill="#b85c38">i</text>
  <text x="390" y="90" font-size="13" fill="#b85c38">r</text>
  <text x="200" y="30" font-size="13" fill="currentColor">i = r</text>
""")
D_REFRACT = fig("""
  <line x1="40" y1="120" x2="480" y2="120" {INK}/>
  <text x="400" y="110" font-size="12" fill="currentColor">air</text>
  <text x="400" y="150" font-size="12" fill="currentColor">glass</text>
  <line x1="260" y1="20" x2="260" y2="200" {INK} stroke-dasharray="4 3"/>
  <line x1="80" y1="20" x2="260" y2="120" {COP}/>
  <line x1="260" y1="120" x2="330" y2="200" {COP}/>
  <text x="140" y="50" font-size="13" fill="#b85c38">i</text>
  <text x="290" y="170" font-size="13" fill="#b85c38">r</text>
  <text x="40" y="210" font-size="12" fill="currentColor">slows down, bends towards the normal</text>
""")
D_DISPERSION = fig("""
  <line x1="30" y1="110" x2="160" y2="110" {INK}/>
  <text x="40" y="100" font-size="12" fill="currentColor">white</text>
  <polygon points="160,40 160,180 280,110" {INK}/>
  <line x1="240" y1="100" x2="480" y2="60" stroke="#b85c38" fill="none" stroke-width="1.6"/>
  <line x1="240" y1="110" x2="480" y2="110" {INK}/>
  <line x1="240" y1="120" x2="480" y2="160" {INK}/>
  <text x="400" y="54" font-size="12" fill="#b85c38">red</text>
  <text x="400" y="104" font-size="12" fill="currentColor">green</text>
  <text x="400" y="176" font-size="12" fill="currentColor">violet</text>
""")
D_COLOUR = fig("""
  <circle cx="180" cy="110" r="58" {INK}/>
  <circle cx="250" cy="110" r="58" {INK}/>
  <circle cx="215" cy="160" r="58" {INK}/>
  <text x="150" y="90" font-size="12" fill="currentColor">R</text>
  <text x="270" y="90" font-size="12" fill="currentColor">G</text>
  <text x="205" y="200" font-size="12" fill="currentColor">B</text>
  <text x="330" y="80" font-size="13" fill="currentColor">R + G = yellow</text>
  <text x="330" y="108" font-size="13" fill="currentColor">R + B = magenta</text>
  <text x="330" y="136" font-size="13" fill="currentColor">G + B = cyan</text>
  <text x="330" y="164" font-size="13" fill="#b85c38">R + G + B = white</text>
""")
D_FIELD = fig("""
  <rect x="230" y="70" width="60" height="90" {INK}/>
  <text x="244" y="108" font-size="13" fill="currentColor">N</text>
  <text x="246" y="142" font-size="13" fill="currentColor">S</text>
  <path d="M230,90 C140,90 140,140 230,140" {COP}/>
  <path d="M290,90 C380,90 380,140 290,140" {COP}/>
  <path d="M230,80 C120,70 120,160 230,150" {INK}/>
  <path d="M290,80 C400,70 400,160 290,150" {INK}/>
  <text x="40" y="200" font-size="12" fill="currentColor">lines leave N and enter S outside the magnet</text>
""")
D_ELECTRO = fig("""
  <rect x="200" y="50" width="36" height="120" {INK}/>
  <text x="204" y="44" font-size="11" fill="currentColor">iron</text>
  <path d="M190,70 C160,70 160,90 190,90 C220,90 220,110 190,110 C160,110 160,130 190,130 C220,130 220,150 190,150" {COP}/>
  <line x1="220" y1="70" x2="340" y2="70" {INK}/>
  <line x1="220" y1="150" x2="340" y2="150" {INK}/>
  <rect x="340" y="90" width="50" height="40" {INK}/>
  <text x="350" y="114" font-size="12" fill="currentColor">cell</text>
  <text x="40" y="200" font-size="12" fill="currentColor">current in a coil, often on an iron core</text>
""")
D_TURNS = fig("""
  <rect x="80" y="60" width="24" height="100" {INK}/>
  <path d="M74,80 C58,80 58,96 74,96 C90,96 90,112 74,112 C58,112 58,128 74,128" {COP}/>
  <text x="60" y="180" font-size="12" fill="currentColor">fewer turns</text>
  <rect x="300" y="60" width="24" height="100" {INK}/>
  <path d="M294,70 C278,70 278,82 294,82 C310,82 310,94 294,94 C278,94 278,106 294,106 C310,106 310,118 294,118 C278,118 278,130 294,130 C310,130 310,142 294,142" {COP}/>
  <text x="270" y="180" font-size="12" fill="currentColor">more turns (same current)</text>
""")
D_EARTH = fig("""
  <circle cx="220" cy="110" r="70" {INK}/>
  <ellipse cx="220" cy="110" rx="28" ry="48" {INK} stroke-dasharray="3 2"/>
  <text x="208" y="114" font-size="11" fill="currentColor">core</text>
  <path d="M220,40 C120,40 80,110 120,170" {COP}/>
  <path d="M220,40 C320,40 360,110 320,170" {COP}/>
  <text x="300" y="200" font-size="12" fill="currentColor">the core acts as a magnet</text>
""")
D_GALAXY = fig("""
  <ellipse cx="260" cy="110" rx="160" ry="50" {INK}/>
  <ellipse cx="260" cy="110" rx="90" ry="28" {INK}/>
  <circle cx="260" cy="110" r="8" fill="#b85c38"/>
  <circle cx="200" cy="100" r="2.2" fill="currentColor"/>
  <circle cx="320" cy="120" r="2.2" fill="currentColor"/>
  <circle cx="150" cy="125" r="2" fill="currentColor"/>
  <circle cx="360" cy="95" r="2" fill="currentColor"/>
  <text x="40" y="200" font-size="12" fill="currentColor">stars, gas and dust, with planetary systems</text>
""")
D_ASTEROID = fig("""
  <circle cx="160" cy="110" r="54" {INK}/>
  <text x="140" y="114" font-size="13" fill="currentColor">Sun</text>
  <circle cx="280" cy="80" r="10" {INK}/>
  <circle cx="340" cy="140" r="8" {INK}/>
  <circle cx="400" cy="90" r="6" {INK}/>
  <path d="M230,110 C260,60 380,60 430,100" {INK} stroke-dasharray="3 3"/>
  <text x="300" y="200" font-size="12" fill="currentColor">rocks smaller than planets</text>
""")

knowledge, questions, sets = [], [], []

def add(les, qs=None):
    knowledge.append(les)
    if qs:
        questions.extend(qs)

# ----- 8Pf.s01 Calculating speed -----
qs = [
    PQ("q-ph-s01-01","physics-8Pf-s01","numeric",
       r"一辆自行车在 $10\ \text{s}$ 内前进 $150\ \text{m}$。速度是多少 $\text{m/s}$？",
       r"A bicycle travels $150\ \text{m}$ in $10\ \text{s}$. What is its speed in $\text{m/s}$?",
       "15", r"使用 $v=s/t=150/10=15\ \text{m/s}$。", r"Use $v=s/t=150/10=15\ \text{m/s}$.", tolerance=0.01),
    PQ("q-ph-s01-02","physics-8Pf-s01","numeric",
       r"把 $72\ \text{km/h}$ 换算成 $\text{m/s}$。",
       r"Convert $72\ \text{km/h}$ into $\text{m/s}$.",
       "20", r"$72\div 3.6=20\ \text{m/s}$（或先乘 $1000$ 再除以 $3600$）。",
       r"$72\div 3.6=20\ \text{m/s}$ (or multiply by $1000$ then divide by $3600$).", tolerance=0.01),
    PQ("q-ph-s01-03","physics-8Pf-s01","numeric",
       r"一辆汽车以 $15\ \text{m/s}$ 匀速行驶 $2$ 分钟。路程是多少米？",
       r"A car travels at a steady $15\ \text{m/s}$ for $2$ minutes. How far does it go, in metres?",
       "1800", r"先把时间换成秒：$2\times 60=120\ \text{s}$。$s=vt=15\times 120=1800\ \text{m}$。不要把 $2$ 分钟直接代入公式。",
       r"Convert time first: $2\times 60=120\ \text{s}$. Then $s=vt=15\times 120=1800\ \text{m}$. Do not put $2$ minutes straight into the formula.", tolerance=0),
    PQ("q-ph-s01-04","physics-8Pf-s01","mcq",
       "计算速度时，下列哪一种做法是正确的？",
       "Which practice is correct when calculating speed?",
       "c", r"路程与时间的单位必须配套。例如米配秒得到 $\text{m/s}$；千米配小时得到 $\text{km/h}$。",
       r"Distance and time units must match: metres with seconds give $\text{m/s}$; kilometres with hours give $\text{km/h}$.",
       options=_opts(("把千米直接除以秒，不必换单位", "Divide kilometres by seconds with no conversion"),
                     ("时间永远用分钟", "Always leave time in minutes"),
                     (r"先统一单位，再代入 $v=s/t$", r"Convert to consistent units, then use $v=s/t$"),
                     ("速度与单位无关", "Speed does not depend on units"))),
    PQ("q-ph-s01-05","physics-8Pf-s01","numeric",
       r"把 $10\ \text{m/s}$ 换算成 $\text{km/h}$。",
       r"Convert $10\ \text{m/s}$ into $\text{km/h}$.",
       "36", r"乘以 $3.6$：$10\times 3.6=36\ \text{km/h}$。", r"Multiply by $3.6$: $10\times 3.6=36\ \text{km/h}$.", tolerance=0.01),
    PQ("q-ph-s01-06","physics-8Pf-s01","short",
       r"写出计算速度的公式（可用符号 $v,s,t$ 或文字）。",
       r"Write the formula for speed (symbols $v,s,t$ or words).",
       "v=s/t", r"速度 = 路程 / 时间，即 $v=s/t$。", r"Speed = distance / time, or $v=s/t$.",
       accepted=["v=s/t","v = s/t","v=s÷t","speed=distance/time","speed = distance / time","速度=路程/时间","速度＝路程／时间","v = d/t","v=d/t"]),
    PQ("q-ph-s01-07","physics-8Pf-s01","numeric",
       r"一名学生跑完 $200\ \text{m}$ 用了 $40\ \text{s}$。平均速度是多少 $\text{m/s}$？",
       r"A student runs $200\ \text{m}$ in $40\ \text{s}$. What is the average speed in $\text{m/s}$?",
       "5", r"$v=200/40=5\ \text{m/s}$。", r"$v=200/40=5\ \text{m/s}$.", tolerance=0.01),
    PQ("q-ph-s01-08","physics-8Pf-s01","mcq",
       r"第 8 阶段公式 $v=s/t$ 中的 $s$ 通常表示？",
       r"In the Stage 8 formula $v=s/t$, $s$ usually stands for:",
       "b", r"这里 $s$ 表示路程（走过的距离）。位移需要考虑方向，本阶段课图与计算通常用路程。",
       "Here $s$ is distance (the length travelled). Displacement includes direction; Stage 8 calculations usually use distance.",
       options=_opts(("只表示位移，不考虑路程", "Displacement only, never distance"),
                     ("路程（走过的距离）", "Distance (the length travelled)"),
                     ("加速度", "Acceleration"),
                     ("质量", "Mass"))),
]
add(lesson("physics-8Pf-s01","计算速度","Calculating speed",
r"本节你将学会用 $v=s/t$ 计算速度，并在 $\text{m/s}$ 与 $\text{km/h}$ 之间正确换算。",
r"You will learn to calculate speed with $v=s/t$, and to convert correctly between $\text{m/s}$ and $\text{km/h}$.",
r"""- 速度衡量物体走得有多快：$v=s/t$。
- $s$ 是路程（走过的距离），$t$ 是所用时间。
- 常用单位：$\text{m/s}$，$\text{km/h}$。单位必须配套。
- $\text{km/h}\rightarrow\text{m/s}$：除以 $3.6$；$\text{m/s}\rightarrow\text{km/h}$：乘以 $3.6$。
- 平均速度用总路程除以总时间。""",
r"""- Speed measures how fast something travels: $v=s/t$.
- $s$ is distance (the length travelled) and $t$ is the time taken.
- Common units: $\text{m/s}$ and $\text{km/h}$. Units must match.
- $\text{km/h}\rightarrow\text{m/s}$: divide by $3.6$; $\text{m/s}\rightarrow\text{km/h}$: multiply by $3.6$.
- Average speed is total distance divided by total time.""",
r"""速度把路程和时间连在一起。第 8 阶段科学要求会使用：

$$v=\frac{s}{t}$$

如果路程用米、时间用秒，速度就是米每秒（$\text{m/s}$）。如果路程用千米、时间用小时，速度就是千米每小时（$\text{km/h}$）。

**单位换算**是最容易出错的地方。把千米换成米要乘 $1000$，把小时换成秒要乘 $3600$，所以

$$72\ \text{km/h}=72\times\frac{1000}{3600}=72\div 3.6=20\ \text{m/s}.$$

反过来，$10\ \text{m/s}=10\times 3.6=36\ \text{km/h}$。

## 例题 1

自行车在 $10\ \text{s}$ 内前进 $150\ \text{m}$。速度是多少？

$$v=\frac{150}{10}=15\ \text{m/s}.$$

## 例题 2

汽车以 $15\ \text{m/s}$ 行驶 $2$ 分钟，走了多远？

时间必须先换成秒：$t=2\times 60=120\ \text{s}$。然后 $s=vt=15\times 120=1800\ \text{m}$。若把 $t=2$ 直接代入，答案会错两个数量级。

本阶段公式中的 $s$ 通常指路程，也就是走过的长度，一般不考虑方向。""",
r"""Speed links distance and time. Stage 8 Science asks you to use

$$v=\frac{s}{t}$$

If distance is in metres and time in seconds, speed is in metres per second ($\text{m/s}$). If distance is in kilometres and time in hours, speed is in kilometres per hour ($\text{km/h}$).

**Unit conversion** is the usual trap. Kilometres to metres is $\times 1000$, hours to seconds is $\times 3600$, so

$$72\ \text{km/h}=72\times\frac{1000}{3600}=72\div 3.6=20\ \text{m/s}.$$

The other way, $10\ \text{m/s}=10\times 3.6=36\ \text{km/h}$.

## Worked example 1

A bicycle travels $150\ \text{m}$ in $10\ \text{s}$. What is its speed?

$$v=\frac{150}{10}=15\ \text{m/s}.$$

## Worked example 2

A car travels at $15\ \text{m/s}$ for $2$ minutes. How far does it go?

Convert time first: $t=2\times 60=120\ \text{s}$. Then $s=vt=15\times 120=1800\ \text{m}$. Putting $t=2$ straight into the formula gives an answer that is wrong by two orders of magnitude.

At this stage $s$ is usually distance — the length travelled — not displacement (which also has a direction).""",
r"""- **单位没有统一。** 用分钟或千米去配米和秒，结果会差很多。先换单位，再代入公式。
- **把 2 分钟当成 $t=2$。** 国际单位制中时间要用秒，或明确使用小时与千米。
- **路程和位移混用。** 本阶段 $v=s/t$ 的 $s$ 一般是走过的距离；来回跑一圈，路程不是零。""",
r"""- **Inconsistent units.** Mixing minutes or kilometres with metres and seconds gives a badly wrong value. Convert first, then substitute.
- **Using $t=2$ for 2 minutes.** SI time is in seconds, unless you are deliberately working in hours with kilometres.
- **Mixing up distance and displacement.** In $v=s/t$ at this stage, $s$ is usually the length travelled; a there-and-back trip does not have zero distance.""",
[q["id"] for q in qs], diagram=D_SPEED))
questions += qs

# ----- 8Pf.s02 graphs -----
qs = [
    PQ("q-ph-s02-01","physics-8Pf-s02","mcq",
       "在路程—时间图像上，一段水平直线表示什么？",
       "On a distance–time graph, what does a horizontal straight section show?",
       "b", "路程不随时间增加，物体静止，速度为零。",
       "Distance is not increasing, so the object is stationary and the speed is zero.",
       options=_opts(("物体在加速", "The object is accelerating"),
                     ("物体静止", "The object is stationary"),
                     ("物体在反向运动", "The object is moving backwards"),
                     ("速度正在均匀增大", "The speed is increasing steadily"))),
    PQ("q-ph-s02-02","physics-8Pf-s02","mcq",
       "路程—时间图像上直线更陡，通常表示？",
       "A steeper straight line on a distance–time graph usually means:",
       "a", "斜率（坡度）等于速度，更陡表示在相同时间内路程增加得更多，即速度更大。",
       "The gradient equals speed; a steeper line means more distance in the same time, so a greater speed.",
       options=_opts(("恒定速度更大", "a greater constant speed"),
                     ("一定在减速", "the object must be slowing down"),
                     ("时间走得更快", "time itself is running faster"),
                     ("物体一定更重", "the object must be heavier"))),
    PQ("q-ph-s02-03","physics-8Pf-s02","numeric",
       r"某图像在 $4\ \text{s}$ 内路程从 $0$ 均匀增加到 $20\ \text{m}$。这段的速度是多少 $\text{m/s}$？",
       r"On a graph, distance increases steadily from $0$ to $20\ \text{m}$ in $4\ \text{s}$. What is the speed in this interval, in $\text{m/s}$?",
       "5", r"斜率 $=\Delta s/\Delta t=20/4=5\ \text{m/s}$。", r"Gradient $=\Delta s/\Delta t=20/4=5\ \text{m/s}$.", tolerance=0.01),
    PQ("q-ph-s02-04","physics-8Pf-s02","mcq",
       "路程—时间图像的斜率（坡度）表示什么？",
       "The gradient (slope) of a distance–time graph represents:",
       "c", "斜率是路程的变化除以时间的变化，也就是速度。加速度要看速度—时间图像的斜率。",
       "Gradient is change in distance divided by change in time, which is speed. Acceleration is the gradient of a speed–time graph.",
       options=_opts(("加速度", "Acceleration"),
                     ("力", "Force"),
                     ("速度", "Speed"),
                     ("质量", "Mass"))),
    PQ("q-ph-s02-05","physics-8Pf-s02","short",
       "若图像先是向上的斜线，接着是一段水平线，物体后来在做什么？",
       "A graph shows an upward straight line and then a horizontal section. What is the object doing in the later part?",
       "stationary", "水平段表示路程不再增加，物体静止（停下）。",
       "The horizontal part means distance is no longer increasing: the object is stationary (it has stopped).",
       accepted=["stationary","at rest","stopped","rest","静止","停下","停止","它静止","the object is stationary","it is stationary"]),
    PQ("q-ph-s02-06","physics-8Pf-s02","numeric",
       r"从 $t=0$ 到 $t=3\ \text{s}$，路程从 $2\ \text{m}$ 均匀增到 $14\ \text{m}$。速度是多少 $\text{m/s}$？",
       r"From $t=0$ to $t=3\ \text{s}$, distance rises steadily from $2\ \text{m}$ to $14\ \text{m}$. What is the speed in $\text{m/s}$?",
       "4", r"$\Delta s=14-2=12\ \text{m}$，$\Delta t=3\ \text{s}$，速度 $=12/3=4\ \text{m/s}$。不要误用 $14/3$。",
       r"$\Delta s=14-2=12\ \text{m}$, $\Delta t=3\ \text{s}$, so speed $=12/3=4\ \text{m/s}$. Do not use $14/3$.", tolerance=0.01),
    PQ("q-ph-s02-07","physics-8Pf-s02","mcq",
       "一段笔直向上的斜线（斜率不变）表示物体在这段时间内？",
       "A straight upward line (constant gradient) means that, in that interval, the object:",
       "b", "斜率不变就是速度恒定。曲线的斜率变化才表示速度在变。本阶段先掌握简单直线图像。",
       "A constant gradient means constant speed. A changing gradient (a curve) would mean a changing speed. Stage 8 starts with simple straight-line graphs.",
       options=_opts(("速度一直在增大", "has a steadily increasing speed"),
                     ("以恒定速度运动", "moves at a constant speed"),
                     ("一定静止", "must be stationary"),
                     ("加速度等于斜率", "has acceleration equal to the gradient"))),
]
add(lesson("physics-8Pf-s02","路程—时间图像","Distance–time graphs",
"本节你将学会绘制并解读简单的路程—时间图像：用斜率求速度，辨认静止与匀速。",
"You will learn to draw and interpret simple distance–time graphs: use the gradient to find speed, and recognise rest and steady motion.",
r"""- 横轴是时间 $t$，纵轴是路程 $s$。
- **斜率（坡度）表示速度**：$v=\Delta s/\Delta t$。
- 水平线段：路程不变，物体**静止**，速度为 $0$。
- 更陡的直线：恒定速度更大。
- 笔直斜线：速度恒定。第 8 阶段以简单直线图像为主。""",
r"""- Time $t$ is on the horizontal axis, distance $s$ on the vertical axis.
- The **gradient (slope) is the speed**: $v=\Delta s/\Delta t$.
- A horizontal segment: distance is not changing, so the object is **stationary** and speed is $0$.
- A steeper straight line: a greater constant speed.
- A straight slope: constant speed. Stage 8 focuses on simple straight-line graphs.""",
r"""路程—时间图像把运动“画”出来。横轴为时间，纵轴为路程。

图像上一段直线的**斜率**等于这段的速度：

$$v=\frac{\Delta s}{\Delta t}=\frac{s_2-s_1}{t_2-t_1}.$$

因此：

- 水平线：$\Delta s=0$，速度为零，物体停下；
- 斜线越陡，同样时间内路程增加越多，速度越大；
- 斜率不变（直线），速度恒定。

看示意图：A 段向上，物体在运动；B 段水平，物体静止；C 段更陡，后来的速度比 A 段更大。

## 例题

一段直线在 $4\ \text{s}$ 内把路程从 $0$ 增加到 $20\ \text{m}$。

$$v=\frac{20-0}{4}=5\ \text{m/s}.$$

若路程从 $2\ \text{m}$ 增到 $14\ \text{m}$，不要用 $14$ 直接去除以时间，而要用变化量 $12\ \text{m}$。

第 8 阶段的课图通常把纵轴标为 distance（路程）。路程一般只增不减；不要把它读成可正可负的位移。""",
r"""A distance–time graph draws the motion. Time is horizontal, distance is vertical.

The **gradient** of a straight section is the speed in that interval:

$$v=\frac{\Delta s}{\Delta t}=\frac{s_2-s_1}{t_2-t_1}.$$

So:

- a horizontal line means $\Delta s=0$, speed zero, the object has stopped;
- a steeper line means more distance in the same time, so a greater speed;
- a constant gradient (a straight line) means constant speed.

In the sketch, section A slopes up (the object is moving), section B is flat (it is at rest), and section C is steeper (a greater speed than in A).

## Worked example

A straight line rises from $0$ to $20\ \text{m}$ in $4\ \text{s}$.

$$v=\frac{20-0}{4}=5\ \text{m/s}.$$

If distance goes from $2\ \text{m}$ to $14\ \text{m}$, do not divide $14$ by the time; use the change, $12\ \text{m}$.

Stage 8 graphs usually plot distance. Distance typically does not fall; do not read the axis as a displacement that can go negative.""",
r"""- **把斜率当成加速度。** 加速度是速度—时间图像的斜率。在 $s$–$t$ 图像上，斜率是速度。
- **只用终点路程去除以时间。** 要从这段的 $\Delta s$ 和 $\Delta t$ 来算，注意起点不一定是零。
- **看见斜线就说“在加速”。** 直线斜向上表示匀速，不是加速。""",
r"""- **Calling the gradient acceleration.** Acceleration is the gradient of a speed–time graph. On an $s$–$t$ graph the gradient is speed.
- **Dividing the final distance by time.** Use $\Delta s$ and $\Delta t$ for that interval; the line may not start at the origin.
- **Saying a sloping straight line means “accelerating”.** A straight upward line is constant speed, not increasing speed.""",
[q["id"] for q in qs], diagram=D_GRAPH))
questions += qs

# ----- 8Pf.s03 forces -----
qs = [
    PQ("q-ph-s03-01","physics-8Pf-s03","mcq",
       "作用在物体上的力平衡（合力为零）时，物体将会？",
       "When the forces on an object are balanced (resultant zero), the object will:",
       "c", "平衡力使物体保持静止，或保持匀速直线运动，而不是一定停下，也不是开始加速。",
       "Balanced forces keep an object at rest, or moving at a constant speed in a straight line — not necessarily stopped, and not starting to accelerate.",
       options=_opts(("一定立刻停下", "always stop at once"),
                     ("速度一定增大", "always speed up"),
                     ("保持静止或匀速直线运动", "stay at rest or keep a steady speed in a straight line"),
                     ("一定改变运动方向", "always change direction"))),
    PQ("q-ph-s03-02","physics-8Pf-s03","mcq",
       "非平衡力对运动的影响是？",
       "An unbalanced force affects motion by:",
       "a", "非平衡力会改变速度：加速、减速或改变方向。",
       "An unbalanced force changes velocity: it can speed an object up, slow it down or change its direction.",
       options=_opts(("使物体加速、减速或改变方向", "speeding it up, slowing it down or changing its direction"),
                     ("只能让静止的物体永远静止", "only keeping a stationary object at rest forever"),
                     ("使质量立刻变为零", "making the mass instantly zero"),
                     ("对运动没有任何影响", "having no effect on motion at all"))),
    PQ("q-ph-s03-03","physics-8Pf-s03","numeric",
       r"向右 $12\ \text{N}$、向左 $5\ \text{N}$，合力大小是多少牛顿？（只写数字）",
       r"Forces of $12\ \text{N}$ right and $5\ \text{N}$ left act on an object. What is the size of the resultant, in newtons? (number only)",
       "7", r"同一直线上，合力为较大的力减去较小的力：$12-5=7\ \text{N}$，方向向右。",
       r"On a straight line, the resultant is the larger force minus the smaller: $12-5=7\ \text{N}$, to the right.", tolerance=0),
    PQ("q-ph-s03-04","physics-8Pf-s03","mcq",
       "一本书静放在桌上。对书而言，下列说法正确的是？",
       "A book rests on a table. Which statement is correct about the book?",
       "d", "静止说明合力为零：重力与桌子的支持力平衡。不是“没有力”。",
       "Being at rest means the resultant is zero: weight is balanced by the support from the table. It is not “force-free”.",
       options=_opts(("书不受任何力", "No forces act on the book"),
                     ("只有重力，所以它其实在加速", "Only weight acts, so the book is really accelerating"),
                     ("合力向下，所以很快会掉下去", "The resultant is downward, so it will soon fall"),
                     ("重力与支持力平衡，合力为零", "Weight and the support force are balanced, so the resultant is zero"))),
    PQ("q-ph-s03-05","physics-8Pf-s03","short",
       "一个物体沿直线做匀速运动。作用在它上面的力是平衡的还是非平衡的？",
       "An object moves in a straight line at constant speed. Are the forces on it balanced or unbalanced?",
       "balanced", "匀速直线运动与静止一样，都是合力为零，力是平衡的。",
       "Steady motion in a straight line, like being at rest, means the resultant is zero: the forces are balanced.",
       accepted=["balanced","balanced forces","平衡","平衡力","力是平衡的","the forces are balanced"]),
    PQ("q-ph-s03-06","physics-8Pf-s03","mcq",
       "足球在草地上越滚越慢，最合理的解释是？",
       "A football rolling on grass slows down. The most reasonable explanation is:",
       "b", "摩擦力等阻力是非平衡力，使球减速。不是因为“运动需要力来维持”所以力消失了。",
       "Friction and other resistances are unbalanced forces that slow the ball. It is not that “motion needs a force to keep going” and the force has vanished.",
       options=_opts(("运动必须靠力维持，力用完了", "Motion needs a force to keep going, and that force has run out"),
                     ("阻力与运动方向相反，合力不为零", "Resistive forces opposite the motion give a non-zero resultant"),
                     ("质量突然变大", "The mass suddenly increased"),
                     ("地球停止吸引它", "The Earth stopped attracting it"))),
    PQ("q-ph-s03-07","physics-8Pf-s03","mcq",
       "向右推一只原来静止的箱子，且推力大于摩擦。箱子将会？",
       "You push a previously resting box to the right, with a push larger than friction. The box will:",
       "c", "原来静止，现在出现向右的合力，它会向右加速，而不是立刻获得恒定速度后永远不变。",
       "It was at rest; now there is a resultant to the right, so it speeds up to the right — it does not instantly take a speed that never changes.",
       options=_opts(("仍然静止，因为曾经静止", "stay at rest, because it was at rest"),
                     ("向左运动", "move to the left"),
                     ("向右加速", "accelerate to the right"),
                     ("立刻以恒定速度向右，且无法再改变", "instantly move right at a speed that can never change"))),
]
add(lesson("physics-8Pf-s03","平衡力与非平衡力","Balanced and unbalanced forces",
"本节你将学会判断力是否平衡，并说明平衡力与非平衡力如何影响运动。",
"You will learn to tell whether forces are balanced, and to describe how balanced and unbalanced forces affect motion.",
r"""- **合力（resultant）**是把几个力合并后的总效果。
- **平衡力**：合力为零。物体保持静止，或沿直线运动的速度不变。
- **非平衡力**：合力不为零。物体将加速、减速或改变方向。
- 静止并不等于不受力，只是力相互抵消。
- 力常用箭头表示：方向表示力的方向，长度可表示大小。""",
r"""- The **resultant** is the overall effect of several forces combined.
- **Balanced forces:** resultant zero. The object stays at rest, or keeps a constant speed in a straight line.
- **Unbalanced forces:** resultant not zero. The object speeds up, slows down or changes direction.
- Being at rest does not mean “no forces”, only that the forces cancel.
- Forces are often drawn as arrows: direction for the force’s direction, length for its size.""",
r"""第 8 阶段要求描述平衡力与非平衡力对运动的影响。

两个大小相等、方向相反的力，例如图中各 $8\ \text{N}$，合力为零，这对力是**平衡**的。若物体本来静止，它继续静止；若本来在做匀速直线运动，它会保持这种运动。

若一边是 $12\ \text{N}$、另一边是 $5\ \text{N}$，合力是 $7\ \text{N}$，指向较大的那个力，力是**非平衡**的，运动状态会改变。

## 例题 1

书放在桌上静止。重力向下，桌子的支持力向上，二者平衡，合力为零。不能说“书没有受力”。

## 例题 2

草地上滚动的足球会慢下来。沿运动反方向的摩擦等阻力使合力不为零，球减速。这并不能说明“运动需要持续有力才能继续”；相反，若阻力可以忽略，平衡时它会保持匀速。""",
r"""Stage 8 asks you to describe the effects of balanced and unbalanced forces on motion.

Two equal forces in opposite directions, such as $8\ \text{N}$ each in the diagram, have a resultant of zero: they are **balanced**. If the object was at rest it stays at rest; if it was already moving at a steady speed in a straight line, it keeps doing so.

If one force is $12\ \text{N}$ and the other is $5\ \text{N}$, the resultant is $7\ \text{N}$ towards the larger force. The forces are **unbalanced**, so the motion changes.

## Worked example 1

A book rests on a table. Weight acts down and the support from the table acts up. They are balanced, so the resultant is zero. It is wrong to say “no forces act on the book”.

## Worked example 2

A football rolling on grass slows down. Friction and other resistances opposite the motion make the resultant non-zero, so the ball decelerates. This does not mean “a force is needed to keep motion going”. If resistance were negligible, balanced forces would keep a steady speed.""",
r"""- **以为静止就是不受力。** 静止只说明合力为零。
- **以为运动必须靠一个力维持。** 匀速直线运动时力可以是平衡的；减速往往是因为有阻力。
- **以为非平衡力只能让物体从静止开始运动。** 它也可以让已经运动的物体变快、变慢或转弯。""",
r"""- **Thinking “at rest” means “no forces”.** Rest only means the resultant is zero.
- **Thinking motion needs a force to keep going.** Forces can be balanced during steady straight-line motion; slowing is usually due to resistance.
- **Thinking unbalanced forces only start motion from rest.** They can also speed up, slow down or turn something already moving.""",
[q["id"] for q in qs], diagram=D_FORCES))
questions += qs

# ----- 8Pf.s04 moments -----
qs = [
    PQ("q-ph-s04-01","physics-8Pf-s04","numeric",
       r"一个大小为 $12\ \text{N}$ 的力，垂直力臂为 $0.5\ \text{m}$。力矩是多少 $\text{N\,m}$？",
       r"A force of $12\ \text{N}$ has a perpendicular distance of $0.5\ \text{m}$ from the pivot. What is the moment in $\text{N\,m}$?",
       "6", r"力矩 $M=F\times d=12\times 0.5=6\ \text{N\,m}$。",
       r"Moment $M=F\times d=12\times 0.5=6\ \text{N\,m}$.", tolerance=0.01),
    PQ("q-ph-s04-02","physics-8Pf-s04","mcq",
       "计算力矩时，公式中的距离必须是？",
       "In the moment formula, the distance must be:",
       "b", "力臂是从支点到力的作用线的**垂直**距离，不是沿杆随便量的斜线长。",
       "The distance is the **perpendicular** distance from the pivot to the line of action of the force, not just any length along the bar.",
       options=_opts(("沿杆量出的任意长度", "any length measured along the bar"),
                     ("从支点到力的作用线的垂直距离", "the perpendicular distance from the pivot to the line of action of the force"),
                     ("物体的高度", "the height of the object"),
                     ("路程 $s$", "the distance travelled, $s$"))),
    PQ("q-ph-s04-03","physics-8Pf-s04","numeric",
       r"要用 $4\ \text{N}$ 的力产生 $10\ \text{N\,m}$ 的力矩，垂直力臂应为多少米？",
       r"What perpendicular distance, in metres, is needed for a $4\ \text{N}$ force to give a moment of $10\ \text{N\,m}$?",
       "2.5", r"$d=M/F=10/4=2.5\ \text{m}$。", r"$d=M/F=10/4=2.5\ \text{m}$.", tolerance=0.01),
    PQ("q-ph-s04-04","physics-8Pf-s04","mcq",
       "轻质杠杆平衡时，下列哪一项成立？",
       "For a light lever in equilibrium, which statement is true?",
       "a", "平衡时，顺时针力矩之和等于逆时针力矩之和。",
       "In equilibrium, the total clockwise moment equals the total anticlockwise moment.",
       options=_opts(("顺时针力矩之和等于逆时针力矩之和", "The total clockwise moment equals the total anticlockwise moment"),
                     ("两边的力必须相等，与距离无关", "The two forces must be equal, whatever the distances"),
                     ("力矩必须为零且力也必须为零", "Moments must be zero and all forces must be zero"),
                     ("只需一边有力", "A force on one side only is enough"))),
    PQ("q-ph-s04-05","physics-8Pf-s04","numeric",
       r"支点左边 $20\ \text{N}$ 的力距支点 $0.4\ \text{m}$。右边用 $10\ \text{N}$ 平衡，它应距支点多少米？",
       r"On the left of a pivot, a $20\ \text{N}$ force acts $0.4\ \text{m}$ away. A $10\ \text{N}$ force on the right keeps balance. How far from the pivot, in metres, should it act?",
       "0.8", r"顺时针与逆时针力矩相等：$20\times 0.4=10\times d$，所以 $d=0.8\ \text{m}$。",
       r"Clockwise and anticlockwise moments are equal: $20\times 0.4=10\times d$, so $d=0.8\ \text{m}$.", tolerance=0.01),
    PQ("q-ph-s04-06","physics-8Pf-s04","short",
       r"写出力矩的公式（可用 $M,F,d$ 或文字）。",
       r"Write the formula for a moment (symbols $M,F,d$ or words).",
       "M=Fd", r"$M=F\times d$，其中 $d$ 是垂直力臂。文字：力矩 = 力 × 垂直距离。",
       r"$M=F\times d$, where $d$ is the perpendicular distance. In words: moment = force × perpendicular distance.",
       accepted=["M=Fd","M=F*d","M=F×d","M = F d","M = F × d","M=F x d","moment=force×distance","moment = force x distance","力矩=力×距离","力矩＝力×垂直距离","力矩=力×力臂"]),
    PQ("q-ph-s04-07","physics-8Pf-s04","mcq",
       "同样大小的力，离支点越远，转向效果通常？",
       "For the same size of force, a greater distance from the pivot usually makes the turning effect:",
       "c", "力矩随垂直力臂增大而增大，所以同样的力离支点越远，越容易转动。",
       "Moment increases with perpendicular distance, so the same force turns more effectively farther from the pivot.",
       options=_opts(("一定更小", "always smaller"),
                     ("完全不变", "completely unchanged"),
                     ("更大", "greater"),
                     ("变为零", "become zero"))),
]
add(lesson("physics-8Pf-s04","力矩（转向力）","Moments (turning forces)",
r"本节你将学会识别并计算力矩：$M=F\times d$，并在简单情况下判断杠杆是否平衡。",
r"You will learn to identify and calculate moments, $M=F\times d$, and to judge whether a simple lever is balanced.",
r"""- 力矩描述力的**转向效果**。
- 公式：$M=F\times d$，单位是牛顿米（$\text{N\,m}$）。
- $d$ 必须是从支点到力的作用线的**垂直**距离。
- 平衡：顺时针力矩之和 = 逆时针力矩之和。
- 同样的力，离支点越远（垂直力臂越大），越容易转动。""",
r"""- A moment describes the **turning effect** of a force.
- Formula: $M=F\times d$, with the unit newton metre ($\text{N\,m}$).
- $d$ must be the **perpendicular** distance from the pivot to the line of action of the force.
- Equilibrium: total clockwise moment = total anticlockwise moment.
- The same force turns more effectively farther from the pivot (larger perpendicular distance).""",
r"""力不仅可以推或拉，还可以使物体绕支点转动。第 8 阶段的公式是：

$$M=F\times d$$

其中 $d$ 是**垂直力臂**。若力斜着作用，不能直接用沿杆量出的斜边长。

## 例题 1

$12\ \text{N}$ 的力，垂直力臂 $0.5\ \text{m}$：

$$M=12\times 0.5=6\ \text{N\,m}.$$

## 例题 2

轻质杠杆：左边 $20\ \text{N}$、力臂 $0.4\ \text{m}$，右边用 $10\ \text{N}$ 使它平衡。则

$$20\times 0.4=10\times d \Rightarrow d=0.8\ \text{m}.$$

这就是“小力也可以撬动重物”的道理：把力臂加长。""",
r"""A force can turn an object about a pivot as well as push or pull it. The Stage 8 formula is

$$M=F\times d$$

where $d$ is the **perpendicular** distance. If the force is at an angle, you must not simply use a slanted length along the bar.

## Worked example 1

A $12\ \text{N}$ force with perpendicular distance $0.5\ \text{m}$:

$$M=12\times 0.5=6\ \text{N\,m}.$$

## Worked example 2

A light lever has $20\ \text{N}$ on the left, $0.4\ \text{m}$ from the pivot. A $10\ \text{N}$ force on the right keeps it balanced:

$$20\times 0.4=10\times d \Rightarrow d=0.8\ \text{m}.$$

That is why a small force can turn a heavy load: increase the perpendicular distance.""",
r"""- **没有用垂直距离。** 力臂是“垂线”距离，不是随便量的长度。
- **以为两边力相等就一定平衡。** 还要看力臂：力矩相等才平衡。
- **单位写成 $\text{N/m}$。** 力矩是力与距离的乘积，单位是 $\text{N\,m}$，不是压强的 $\text{N/m}^2$。""",
r"""- **Not using perpendicular distance.** The distance in the formula is the perpendicular one, not any convenient length.
- **Thinking equal forces always balance.** Distances matter too: the moments must be equal.
- **Writing the unit as $\text{N/m}$.** A moment is force times distance, so $\text{N\,m}$, not the pressure unit $\text{N/m}^2$.""",
[q["id"] for q in qs], diagram=D_MOMENT))
questions += qs

# ----- 8Pf.s05 pressure -----
qs = [
    PQ("q-ph-s05-01","physics-8Pf-s05","numeric",
       r"一个 $20\ \text{N}$ 的力作用在 $4\ \text{m}^2$ 的面积上。压强是多少 $\text{N/m}^2$？",
       r"A force of $20\ \text{N}$ acts on an area of $4\ \text{m}^2$. What is the pressure in $\text{N/m}^2$?",
       "5", r"压强 $p=F/A=20/4=5\ \text{N/m}^2$。", r"Pressure $p=F/A=20/4=5\ \text{N/m}^2$.", tolerance=0.01),
    PQ("q-ph-s05-02","physics-8Pf-s05","mcq",
       "在大小相同的力作用下，受力面积越小，压强？",
       "For the same size of force, a smaller area means that pressure is:",
       "b", r"$p=F/A$，面积越小压强越大。刀刃、图钉尖就是这个道理。",
       r"$p=F/A$, so a smaller area gives a larger pressure. A knife edge or a drawing-pin tip works this way.",
       options=_opts(("一定更小", "always smaller"),
                     ("更大", "greater"),
                     ("一定不变", "must stay the same"),
                     ("与面积无关", "independent of area"))),
    PQ("q-ph-s05-03","physics-8Pf-s05","numeric",
       r"要用 $80\ \text{N}$ 的力在 $0.4\ \text{m}^2$ 上产生压强。压强是多少 $\text{N/m}^2$？",
       r"An $80\ \text{N}$ force acts on $0.4\ \text{m}^2$. What is the pressure in $\text{N/m}^2$?",
       "200", r"$p=80/0.4=200\ \text{N/m}^2$。", r"$p=80/0.4=200\ \text{N/m}^2$.", tolerance=0.01),
    PQ("q-ph-s05-04","physics-8Pf-s05","short",
       r"写出压强的公式（可用 $p,F,A$ 或文字）。",
       r"Write the formula for pressure (symbols $p,F,A$ or words).",
       "p=F/A", r"$p=F/A$，即压强 = 力 / 面积。", r"$p=F/A$, that is pressure = force / area.",
       accepted=["p=F/A","p = F/A","p=F÷A","pressure=force/area","pressure = force / area","压强=力/面积","压强＝力／面积"]),
    PQ("q-ph-s05-05","physics-8Pf-s05","mcq",
       "雪地靴比普通鞋更不容易陷进雪里，主要是因为？",
       "Snowshoes are less likely than ordinary shoes to sink into snow mainly because they:",
       "c", "面积更大，同一个人的重力被分摊，压强减小。不是人变轻了。",
       "They have a larger area, so the same weight is spread out and pressure falls. The person is not lighter.",
       options=_opts(("人的重力变小了", "make the person weigh less"),
                     ("雪的质量变小了", "reduce the mass of the snow"),
                     ("增大接触面积，从而减小压强", "increase the contact area and so reduce the pressure"),
                     ("把力完全取消了", "cancel the force completely"))),
    PQ("q-ph-s05-06","physics-8Pf-s05","numeric",
       r"压强为 $25\ \text{N/m}^2$，面积为 $2\ \text{m}^2$。力是多少牛顿？",
       r"The pressure is $25\ \text{N/m}^2$ on an area of $2\ \text{m}^2$. What is the force in newtons?",
       "50", r"$F=pA=25\times 2=50\ \text{N}$。", r"$F=pA=25\times 2=50\ \text{N}$.", tolerance=0),
    PQ("q-ph-s05-07","physics-8Pf-s05","mcq",
       r"压强的单位 $\text{N/m}^2$ 与力矩的单位 $\text{N\,m}$ 容易混淆。压强是？",
       r"The pressure unit $\text{N/m}^2$ is easy to confuse with the moment unit $\text{N\,m}$. Pressure is:",
       "a", r"压强是力除以面积（$\text{N/m}^2$ 或帕斯卡）；力矩是力乘以距离（$\text{N\,m}$）。",
       r"Pressure is force divided by area ($\text{N/m}^2$ or pascal); a moment is force times distance ($\text{N\,m}$).",
       options=_opts((r"力除以面积", "force divided by area"),
                     (r"力乘以距离", "force multiplied by distance"),
                     ("只与温度有关", "to do with temperature only"),
                     ("速度的另一种说法", "just another name for speed"))),
]
add(lesson("physics-8Pf-s05","压强","Pressure",
r"本节你将学会用 $p=F/A$ 解释并计算压强，说明面积如何改变压强。",
r"You will learn to explain and calculate pressure with $p=F/A$, and to say how area changes the pressure.",
r"""- 压强是力作用在某一面积上的效果：$p=F/A$。
- 单位：$\text{N/m}^2$（帕斯卡 $\text{Pa}$ 就是 $1\ \text{N/m}^2$）。
- 力一定时，面积越小，压强越大；面积越大，压强越小。
- 刀刃、图钉尖：减小面积以增大压强；雪地靴、宽履带：增大面积以减小压强。""",
r"""- Pressure is the effect of a force on an area: $p=F/A$.
- Unit: $\text{N/m}^2$ (one pascal, $\text{Pa}$, is $1\ \text{N/m}^2$).
- For a given force, a smaller area means a larger pressure; a larger area means a smaller pressure.
- A knife edge or drawing-pin tip reduces area to raise pressure; snowshoes or wide tracks increase area to lower it.""",
r"""第 8 阶段把压强说成：力作用在某一面积上所产生的效果。

$$p=\frac{F}{A}$$

同样 $80\ \text{N}$ 的力，若作用在 $0.4\ \text{m}^2$ 上，压强是 $200\ \text{N/m}^2$；若面积变成 $4\ \text{m}^2$，压强只有 $20\ \text{N/m}^2$。

## 例题

$20\ \text{N}$ 作用在 $4\ \text{m}^2$ 上：$p=20/4=5\ \text{N/m}^2$。

生活里：菜刀刃很窄，压强大，容易切入食物；雪地靴底面积大，人不容易陷进雪里——重力几乎没变，变的是面积和压强。

计算时面积要用平方米。若给的是 $\text{cm}^2$，先换单位。""",
r"""Stage 8 explains pressure as the effect of a force acting on an area:

$$p=\frac{F}{A}$$

The same $80\ \text{N}$ on $0.4\ \text{m}^2$ gives $200\ \text{N/m}^2$; on $4\ \text{m}^2$ it gives only $20\ \text{N/m}^2$.

## Worked example

$20\ \text{N}$ on $4\ \text{m}^2$: $p=20/4=5\ \text{N/m}^2$.

In everyday life a thin knife edge produces a large pressure and cuts easily; snowshoes have a large area so a person is less likely to sink — the weight is almost unchanged, but the area and the pressure change.

Use square metres for area. If you are given $\text{cm}^2$, convert first.""",
r"""- **把压强和力当成一回事。** 力可以相同，压强随面积变。
- **面积单位没换算。** $1\ \text{m}^2=10\,000\ \text{cm}^2$，弄错会差很多。
- **与力矩单位混淆。** 压强是 $\text{N/m}^2$，力矩是 $\text{N\,m}$。""",
r"""- **Treating pressure and force as the same thing.** The force can stay the same while pressure changes with area.
- **Forgetting to convert area units.** $1\ \text{m}^2=10\,000\ \text{cm}^2$; a slip here is costly.
- **Mixing up units with moments.** Pressure is $\text{N/m}^2$; a moment is $\text{N\,m}$.""",
[q["id"] for q in qs], diagram=D_PRESSURE))
questions += qs

# ----- 8Pf.s06 particle pressure -----
qs = [
    PQ("q-ph-s06-01","physics-8Pf-s06","mcq",
       "气体对器壁产生压强，主要是因为粒子？",
       "A gas exerts pressure on the walls of its container mainly because the particles:",
       "b", "气体粒子不断运动并碰撞器壁，每次碰撞都给器壁一个力，大量碰撞形成压强。",
       "Gas particles move continually and collide with the walls; each collision exerts a force, and many collisions produce pressure.",
       options=_opts(("全部静止地堆在底部", "all sit still at the bottom"),
                     ("不断运动并碰撞器壁", "move continually and collide with the walls"),
                     ("彼此吸引并把容器拉小", "attract each other and shrink the container"),
                     ("没有质量所以能穿过器壁", "have no mass and pass through the walls"))),
    PQ("q-ph-s06-02","physics-8Pf-s06","mcq",
       "温度升高时（体积大致不变），气体压强通常会？",
       "If the temperature rises (and the volume stays about the same), the pressure of a gas usually:",
       "c", "粒子运动更快，碰撞更频繁也更有力，压强增大。",
       "Particles move faster, so collisions are more frequent and harder, and the pressure rises.",
       options=_opts(("一定降至零", "always fall to zero"),
                     ("与温度完全无关", "be completely independent of temperature"),
                     ("增大，因为碰撞更频繁、更有力", "increase, because collisions are more frequent and harder"),
                     ("减小，因为粒子停止运动", "decrease, because the particles stop moving"))),
    PQ("q-ph-s06-03","physics-8Pf-s06","mcq",
       "同一温度下，把气体压缩到更小体积，压强通常？",
       "At the same temperature, compressing a gas into a smaller volume usually makes the pressure:",
       "a", "同样多的粒子在更小空间里，单位时间碰撞器壁更频繁，压强增大。",
       "The same number of particles in a smaller space hit the walls more often, so the pressure rises.",
       options=_opts(("增大", "increase"),
                     ("一定减小", "always decrease"),
                     ("保持绝对不变", "stay exactly the same"),
                     ("只取决于容器颜色", "depend only on the colour of the container"))),
    PQ("q-ph-s06-04","physics-8Pf-s06","short",
       "用粒子的观点，一句话解释气体为什么有压强。",
       "In one sentence, explain gas pressure in terms of particles.",
       "collisions", "气体粒子不断碰撞器壁，大量碰撞产生一个平均的力，从而形成压强。",
       "Gas particles continually collide with the walls; many collisions produce an average force and therefore a pressure.",
       accepted=["collisions","collision with walls","particles collide with the walls","they hit the walls","碰撞","碰撞器壁","粒子碰撞器壁","粒子不断碰撞器壁"]),
    PQ("q-ph-s06-05","physics-8Pf-s06","mcq",
       "液体内部也有压强。与气体相比，液体粒子？",
       "Liquids also exert pressure. Compared with a gas, liquid particles are:",
       "d", "液体粒子更紧密，几乎不可压缩，但仍然运动并相互碰撞，也对接触面施力。",
       "Liquid particles are much closer together and almost incompressible, but they still move and collide, and they exert forces on surfaces they touch.",
       options=_opts(("完全不动", "not moving at all"),
                     ("间距和气体完全一样", "spaced exactly as in a gas"),
                     ("可以自由飞过很大的空间", "free to fly across large empty spaces"),
                     ("靠得更近，几乎不可压缩，仍会碰撞并施力", "closer together, almost incompressible, and still collide and exert forces"))),
    PQ("q-ph-s06-06","physics-8Pf-s06","mcq",
       "给轮胎打气时压强升高，一个合理的粒子解释是？",
       "When you pump more air into a tyre, the pressure rises. A reasonable particle explanation is:",
       "b", "更多粒子在相近体积里，单位时间碰撞内壁更频繁，压强增大。",
       "More particles in a similar volume hit the inner wall more often, so the pressure rises.",
       options=_opts(("粒子变少了", "there are fewer particles"),
                     ("更多粒子更频繁地碰撞内壁", "more particles collide with the inner wall more often"),
                     ("轮胎的重力消失了", "the tyre’s weight has vanished"),
                     ("空气不再由粒子组成", "air is no longer made of particles"))),
    PQ("q-ph-s06-07","physics-8Pf-s06","mcq",
       "下列哪一项最能说明“压强来自粒子碰撞”，而不是“空气有重量所以向下压”这一种不完整的说法？",
       "Which observation best supports “pressure comes from particle collisions”, rather than the incomplete idea that “air only pushes down because it has weight”?",
       "c", "封闭容器中气体对各个方向的器壁（包括向上、向侧面）都有压强，说明是各向碰撞，不只是“向下的重量”。",
       "A gas in a closed container pushes on every wall — including upwards and sideways — which fits collisions in all directions, not only a downward weight.",
       options=_opts(("气体只会压容器底部", "A gas only pushes on the bottom of a container"),
                     ("真空中压强最大", "Pressure is greatest in a vacuum"),
                     ("气体对上、下、侧面的器壁都有压强", "A gas exerts pressure on the top, bottom and sides of a container"),
                     ("只有固体才有压强", "Only solids can exert pressure"))),
]
add(lesson("physics-8Pf-s06","用粒子模型解释压强","The particle model and pressure",
"本节你将学会用粒子的运动与碰撞，解释气体（以及液体）为什么会产生压强。",
"You will learn to use the motion and collisions of particles to explain why gases (and liquids) exert pressure.",
r"""- 气体由不断快速运动的粒子组成。
- 粒子碰撞器壁时给器壁一个力；大量碰撞形成压强。
- 温度升高：粒子更快，碰撞更频繁、更有力，压强增大（体积相近时）。
- 体积减小或粒子数增多：碰撞更频繁，压强增大。
- 液体粒子更紧密，几乎不可压缩，但仍运动并施力。""",
r"""- A gas is made of particles that move about rapidly and continually.
- When particles collide with a wall they exert a force; many collisions produce pressure.
- A higher temperature means faster particles, harder and more frequent collisions, and a higher pressure (if the volume is similar).
- A smaller volume, or more particles, means more frequent collisions and a higher pressure.
- Liquid particles are much closer and almost incompressible, but they still move and exert forces.""",
r"""第 8 阶段要求把压强和粒子模型联系起来。

气体粒子不是静止的。它们向各个方向运动，碰到器壁就反弹。每一次碰撞都是一次小小的力；在短时间内有极多次碰撞，这些力合起来就是气体压强。

因此：

- **加热**（体积差不多不变）：粒子动能增大，运动更快，碰撞更“狠”也更勤，压强升高。
- **压缩**到更小体积：同样多的粒子在更小空间里，碰撞更频繁，压强升高。
- **打进更多气体**：粒子数增多，碰撞更频繁，压强升高。

液体的粒子几乎紧挨着，所以液体很难被压缩，但对接触的面仍然有压强（例如水对容器壁、对沉在水中的物体）。

一个容易忽略的现象：封闭气体对容器的上盖也有向上的压强。这更符合“各向碰撞”，而不能只用“空气有重量所以向下压”来解释全部事实。""",
r"""Stage 8 asks you to link pressure with the particle model.

Gas particles are not still. They move in all directions and rebound from the walls. Each collision is a tiny force; hugely many collisions in a short time add up to the gas pressure.

So:

- **Heating** (with volume about the same) makes particles move faster, so collisions are harder and more frequent, and the pressure rises.
- **Compressing** into a smaller volume packs the same number of particles into less space, so collisions are more frequent and the pressure rises.
- **Pumping in more gas** increases the number of particles, so collisions are more frequent and the pressure rises.

Liquid particles sit much closer together, so a liquid is very hard to compress, but it still exerts pressure on any surface it touches (for example, water on the sides of a tank, or on an object immersed in it).

A gas in a closed container also pushes **upwards** on the lid. That fits collisions in every direction, and it is not fully explained by “air only pushes down because it has weight”.""",
r"""- **以为气体压强只是“空气的重量向下压”。** 器壁各个方向都受到压强，这来自各向碰撞。
- **忽略温度或体积的影响。** 更快的粒子、更小的空间都会改变碰撞频率和力度。
- **把液体当成完全“没有粒子运动”。** 液体几乎不可压缩，但粒子仍在运动并施力。""",
r"""- **Thinking gas pressure is only “the weight of air pushing down”.** Every wall feels pressure, from collisions in all directions.
- **Ignoring temperature or volume.** Faster particles or a smaller space change how often and how hard collisions happen.
- **Treating a liquid as if its particles do not move.** A liquid is almost incompressible, but its particles still move and exert forces.""",
[q["id"] for q in qs], diagram=D_PARTICLES))
questions += qs

# ----- 8Pf.s07 diffusion -----
qs = [
    PQ("q-ph-s07-01","physics-8Pf-s07","mcq",
       "扩散能够发生，是因为粒子？",
       "Diffusion can happen because particles:",
       "b", "粒子在不断随机运动，因而会从浓度高的区域逐渐散布到浓度低的区域。",
       "Particles move continually and randomly, so they gradually spread from where they are more concentrated to where they are less concentrated.",
       options=_opts(("完全静止", "are completely still"),
                     ("不断做无规则运动", "move continually and randomly"),
                     ("只能被外力推着走", "can only move if an outside force pushes them"),
                     ("在液体中完全不能运动", "cannot move at all in a liquid"))),
    PQ("q-ph-s07-02","physics-8Pf-s07","mcq",
       "一般来说，气体中的扩散比液体中更快，主要是因为气体粒子？",
       "Diffusion is generally faster in a gas than in a liquid mainly because gas particles:",
       "a", "气体粒子间距更大、运动更自由，彼此阻碍较少，所以扩散通常更快。液体粒子更紧密。",
       "Gas particles are more widely spaced and move more freely, with fewer collisions that hinder spreading, so diffusion is usually faster. Liquid particles are much closer.",
       options=_opts(("间距更大、运动更自由", "are more widely spaced and move more freely"),
                     ("质量一定比液体粒子大得多", "must have a much larger mass than liquid particles"),
                     ("完全不互相碰撞", "never collide with one another"),
                     ("温度一定低得多", "must be at a much lower temperature"))),
    PQ("q-ph-s07-03","physics-8Pf-s07","mcq",
       "温度升高时，扩散通常会？",
       "If the temperature rises, diffusion usually:",
       "c", "粒子平均运动更快，因而扩散加快。",
       "Particles move faster on average, so diffusion speeds up.",
       options=_opts(("停止", "stop"),
                     ("一定变慢", "always slow down"),
                     ("加快，因为粒子运动更快", "speed up, because the particles move faster"),
                     ("与温度无关", "be independent of temperature"))),
    PQ("q-ph-s07-04","physics-8Pf-s07","short",
       "用粒子的观点，简要解释香水味为什么能在房间里传播。",
       "In terms of particles, briefly explain why the smell of perfume can spread across a room.",
       "diffusion", "香水的粒子不断运动，并在空气粒子之间扩散，从浓度高的地方逐渐散布到整个房间。",
       "Perfume particles move continually and diffuse among the air particles, spreading from a region of higher concentration across the room.",
       accepted=["diffusion","they diffuse","particles spread","粒子扩散","扩散","香水粒子扩散","particles move and spread","random motion"]),
    PQ("q-ph-s07-05","physics-8Pf-s07","mcq",
       "在装满水的烧杯中滴入一滴色素，色素会慢慢散开。这主要是？",
       "A drop of dye in a beaker of water slowly spreads out. This is mainly:",
       "b", "这是液体中的扩散：色素粒子与水粒子都在运动并逐渐混合。不是整杯水被搅拌，也不是重力把颜色“拉”匀。",
       "This is diffusion in a liquid: dye particles and water particles move and gradually mix. The water need not be stirred, and gravity does not “pull the colour even”.",
       options=_opts(("必须先大力搅拌", "something that can only happen if the water is stirred hard"),
                     ("液体中的扩散", "diffusion in a liquid"),
                     ("色素变成了气体", "the dye turning into a gas"),
                     ("杯底出现了一个力把颜色拉下去", "a force at the bottom pulling the colour down"))),
    PQ("q-ph-s07-06","physics-8Pf-s07","mcq",
       "下列哪一项最准确地描述扩散的方向？",
       "Which statement describes the overall direction of diffusion most accurately?",
       "a", "总体上看，粒子从浓度较高的区域净迁移到浓度较低的区域，直到比较均匀。个别粒子路径是随机的。",
       "Overall, there is a net movement from higher to lower concentration until the mixture is more uniform. Individual particle paths are random.",
       options=_opts(("总体上从浓度高处到浓度低处", "overall, from higher to lower concentration"),
                     ("只能从低浓度到高浓度", "only from lower to higher concentration"),
                     ("粒子沿一条直线同时到达各处", "particles travel in a straight line and arrive everywhere at once"),
                     ("只在真空中发生", "it happens only in a vacuum"))),
    PQ("q-ph-s07-07","physics-8Pf-s07","mcq",
       "两瓶气体之间用细管相连后，较轻的气体往往扩散得更快。一个合理的解释是？",
       "Two gases are linked by a narrow tube. The lighter gas often diffuses faster. A reasonable explanation is that lighter particles typically:",
       "d", "在相近温度下，较轻的粒子平均速率往往更大，因而扩散更快。这是一个简化的第 8 阶段解释。",
       "At a similar temperature, lighter particles typically have a greater average speed, so they diffuse faster. This is a simplified Stage 8 explanation.",
       options=_opts(("完全不运动", "do not move at all"),
                     ("一定带有电荷", "must be electrically charged"),
                     ("只能在液体中运动", "can move only in a liquid"),
                     ("平均运动更快", "move faster on average"))),
]
add(lesson("physics-8Pf-s07","气体与液体的扩散","Diffusion of gases and liquids",
"本节你将学会用粒子模型解释气体和液体中的扩散，并比较快慢。",
"You will learn to explain diffusion in gases and liquids with the particle model, and to compare how quickly it happens.",
r"""- **扩散**是粒子从浓度较高的区域逐渐散布到浓度较低的区域。
- 原因：粒子不断做无规则运动。
- 气体中通常比液体中更快：气体粒子间距大、运动更自由。
- 温度升高，粒子运动更快，扩散加快。
- 不必搅拌也会发生，只是液体中往往较慢，肉眼要等一会儿。""",
r"""- **Diffusion** is the gradual spreading of particles from a higher to a lower concentration.
- It happens because particles move continually and randomly.
- It is usually faster in a gas than in a liquid: gas particles are more widely spaced and move more freely.
- A higher temperature means faster particles and faster diffusion.
- Stirring is not required; in a liquid it is often slow, so you may have to wait.""",
r"""打开一瓶香水，过一会儿房间里别处也能闻到。色素滴进静止的水中，颜色会慢慢散开。这些都是**扩散**。

粒子不会停在原地。它们不断无规则运动，彼此碰撞，逐渐从“较多”的地方净迁移到“较少”的地方，直到比较均匀。

为什么气体中通常更快？气体粒子之间有很大空隙，运动更自由；液体粒子几乎紧挨着，扩散仍会发生，但往往慢得多。加热后粒子平均运动更快，扩散也加快。

## 例题

不必搅拌，一滴食用色素也会在清水中慢慢散开。这不是“颜色自己有一种特殊向下的力”，而是色素粒子和水粒子都在运动并混合。

第 8 阶段只要能用粒子运动解释扩散，并比较气体与液体、不同温度即可，不必引入完整的数学公式。""",
r"""Open a bottle of perfume and after a while the smell reaches other parts of the room. A drop of dye in still water slowly spreads. Both are **diffusion**.

Particles do not stay put. They move randomly, collide, and there is a net spreading from where they are more concentrated to where they are less concentrated, until the mixture is more uniform.

Why is it usually faster in a gas? Gas particles have large spaces between them and move more freely; liquid particles are almost touching, so diffusion still happens but is often much slower. Heating makes particles move faster on average, so diffusion speeds up.

## Worked example

A drop of food colouring slowly spreads in still water with no stirring. The colour does not have a special downward force of its own; dye particles and water particles are both moving and mixing.

At Stage 8 you only need a particle explanation, and a comparison between gases and liquids or different temperatures — not a full mathematical treatment.""",
r"""- **以为扩散必须靠搅拌或风。** 搅拌会加快混合，但扩散在静止时也会发生。
- **以为液体不能扩散。** 液体中可以扩散，通常更慢。
- **把个别粒子的随机路径说成“所有粒子同时沿直线走过去”。** 总体是从高浓度到低浓度，路径是杂乱的。""",
r"""- **Thinking diffusion needs stirring or a wind.** Stirring speeds mixing, but diffusion also happens in still conditions.
- **Thinking liquids cannot diffuse.** They can; it is usually slower.
- **Describing every particle as travelling in a straight line to its destination at once.** Overall there is net movement from high to low concentration; individual paths are jumbled.""",
[q["id"] for q in qs], diagram=D_DIFFUSION))
questions += qs

# ----- 8Ps.s01 reflection -----
qs = [
    PQ("q-ph-ps01-01","physics-8Ps-s01","mcq",
       "反射定律指出，入射角与反射角？",
       "The law of reflection says that the angle of incidence and the angle of reflection are:",
       "b", "二者相等，且入射光线、法线、反射光线在同一平面内。",
       "They are equal, and the incident ray, the normal and the reflected ray lie in the same plane.",
       options=_opts(("永远相差 $90^\\circ$", r"always $90^\circ$ apart"),
                     ("相等", "equal"),
                     ("加起来一定等于 $180^\\circ$", r"always add up to $180^\circ$"),
                     ("与表面材质无关且可以任意取值", "independent of the surface and can take any values"))),
    PQ("q-ph-ps01-02","physics-8Ps-s01","mcq",
       "入射角和反射角是从哪一条线量起的？",
       "The angles of incidence and reflection are measured from:",
       "c", "必须从法线（与镜面垂直的虚线）量起，不是从镜面量起。",
       "They are measured from the normal (the dashed line at right angles to the mirror), not from the surface of the mirror.",
       options=_opts(("镜面本身", "the mirror surface itself"),
                     ("入射光线到反射光线之间", "the angle between the incident ray and the reflected ray"),
                     ("法线（与表面垂直的线）", "the normal (the line at right angles to the surface)"),
                     ("光源到眼睛的连线", "the line from the lamp to the eye"))),
    PQ("q-ph-ps01-03","physics-8Ps-s01","numeric",
       r"光线射到平面镜，入射角为 $35^\circ$。反射角是多少度？",
       r"A ray strikes a plane mirror with an angle of incidence of $35^\circ$. What is the angle of reflection, in degrees?",
       "35", r"反射定律：$i=r$，所以反射角也是 $35^\circ$。",
       r"The law of reflection: $i=r$, so the angle of reflection is also $35^\circ$.", tolerance=0),
    PQ("q-ph-ps01-04","physics-8Ps-s01","numeric",
       r"若入射光线与镜面的夹角为 $30^\circ$，入射角是多少度？",
       r"A ray makes a $30^\circ$ angle with the mirror surface. What is the angle of incidence, in degrees?",
       "60", r"法线与镜面垂直，所以入射角 $=90^\circ-30^\circ=60^\circ$，不是 $30^\circ$。",
       r"The normal is at $90^\circ$ to the mirror, so the angle of incidence is $90^\circ-30^\circ=60^\circ$, not $30^\circ$.", tolerance=0),
    PQ("q-ph-ps01-05","physics-8Ps-s01","short",
       "用一句话写出平面镜的反射定律。",
       "State the law of reflection at a plane surface in one sentence.",
       "i=r", r"入射角等于反射角（从法线量起），且入射光线、法线、反射光线在同一平面内。",
       "The angle of incidence equals the angle of reflection (measured from the normal), and the incident ray, normal and reflected ray lie in the same plane.",
       accepted=["i=r","i = r","angle of incidence equals angle of reflection","入射角等于反射角","入射角＝反射角","i equals r"]),
    PQ("q-ph-ps01-06","physics-8Ps-s01","mcq",
       "画平面镜光线图时，法线应该？",
       "When you draw a ray diagram for a plane mirror, the normal should be:",
       "a", "在入射点与镜面垂直，通常画成虚线，作为量角的基准。",
       "Drawn at right angles to the mirror at the point of incidence, usually dashed, as the reference for measuring the angles.",
       options=_opts(("过入射点并与镜面垂直，常画成虚线", "at right angles to the mirror at the point of incidence, often dashed"),
                     ("与入射光线重合", "along the incident ray"),
                     ("平行于镜面", "parallel to the mirror"),
                     ("可省略，因为角度从镜面量更方便", "left out, because it is easier to measure from the mirror"))),
    PQ("q-ph-ps01-07","physics-8Ps-s01","mcq",
       "平面镜反射可以用来？",
       "Reflection at a plane surface can be used to:",
       "d", "平面镜按定律改变光线方向，可用于观察拐角、改变光路等。第 8 阶段只要能陈述定律并画简单图。",
       "A plane mirror changes the direction of rays according to the law, for example to look around a corner or redirect a beam. Stage 8 asks you to state the law and draw a simple diagram.",
       options=_opts(("把白光分解成光谱（这是色散）", "split white light into a spectrum (that is dispersion)"),
                     ("让光线在玻璃中永远拐弯（这是折射）", "make light bend forever inside glass (that is refraction)"),
                     ("产生磁场", "produce a magnetic field"),
                     ("按 $i=r$ 改变光线方向，如用镜子观察或反射光束", "change a ray’s direction with $i=r$, for example with a mirror"))),
]
add(lesson("physics-8Ps-s01","平面反射与反射定律","Reflection at a plane surface",
r"本节你将学会陈述反射定律，从法线正确量出入射角与反射角，并画出平面镜光线图。",
r"You will learn to state the law of reflection, measure $i$ and $r$ from the normal, and draw a plane-mirror ray diagram.",
r"""- 光线射到平面镜后反射。
- **法线**过入射点，与镜面垂直，通常画成虚线。
- **入射角 $i$**、**反射角 $r$** 都从法线量起。
- 反射定律：$i=r$，且入射光线、法线、反射光线共面。
- 不要把“光线与镜面的夹角”误当成入射角。""",
r"""- A ray striking a plane mirror is reflected.
- The **normal** is at right angles to the mirror at the point of incidence, and is usually drawn dashed.
- The **angle of incidence $i$** and the **angle of reflection $r$** are both measured from the normal.
- Law of reflection: $i=r$, and the incident ray, normal and reflected ray lie in the same plane.
- Do not mistake the angle between the ray and the mirror for the angle of incidence.""",
r"""第 8 阶段光学从平面反射开始。画图时先画镜面，再在入射点作法线。

入射角是入射光线与法线的夹角，反射角是反射光线与法线的夹角。定律说它们相等：

$$i=r.$$

## 例题 1

入射角为 $35^\circ$，则反射角也是 $35^\circ$。

## 例题 2

若题目说“光线与镜面成 $30^\circ$”，入射角并不是 $30^\circ$，而是 $90^\circ-30^\circ=60^\circ$，反射角也是 $60^\circ$。

平面镜可以改变光路，例如照向拐角。本课先把定律和量角方法打牢，下一节再看光线进入另一种介质时的折射。""",
r"""Stage 8 optics begins with reflection at a plane surface. Draw the mirror first, then the normal at the point of incidence.

The angle of incidence is between the incident ray and the normal; the angle of reflection is between the reflected ray and the normal. The law says they are equal:

$$i=r.$$

## Worked example 1

If the angle of incidence is $35^\circ$, the angle of reflection is also $35^\circ$.

## Worked example 2

If a question says “the ray makes $30^\circ$ with the mirror”, the angle of incidence is not $30^\circ$. It is $90^\circ-30^\circ=60^\circ$, and the angle of reflection is $60^\circ$ too.

A plane mirror can redirect a beam, for example around a corner. Master the law and the measuring convention first; the next lesson looks at refraction when light enters another medium.""",
r"""- **从镜面而非法线量角。** 这是最常见的错误，会把 $30^\circ$ 与 $60^\circ$ 搞反。
- **以为 $i$ 与 $r$ 加起来等于 $90^\circ$ 或 $180^\circ$。** 定律是二者相等。
- **漏画法线。** 没有法线就无法正确标角。""",
r"""- **Measuring from the mirror instead of the normal.** This is the usual mistake, and it swaps $30^\circ$ and $60^\circ$.
- **Thinking $i$ and $r$ add to $90^\circ$ or $180^\circ$.** The law is that they are equal.
- **Leaving out the normal.** Without it you cannot mark the angles correctly.""",
[q["id"] for q in qs], diagram=D_REFLECT))
questions += qs

# ----- 8Ps.s02 refraction -----
qs = [
    PQ("q-ph-ps02-01","physics-8Ps-s02","mcq",
       "光线从空气斜射入玻璃时，通常会？",
       "When a ray travels from air into glass at an angle, it usually:",
       "b", "进入玻璃（光密介质）时，光线向法线偏折，折射角小于入射角。",
       "Entering glass (an optically denser medium), the ray bends towards the normal, so the angle of refraction is smaller than the angle of incidence.",
       options=_opts(("远离法线", "bend away from the normal"),
                     ("向法线偏折", "bend towards the normal"),
                     ("一定沿原方向，永不偏折", "always continue in a straight line with no bending"),
                     ("被完全反射，再也不能进入玻璃", "be totally reflected and never enter the glass"))),
    PQ("q-ph-ps02-02","physics-8Ps-s02","mcq",
       "光线从玻璃斜射回空气时，通常会？",
       "When a ray travels from glass into air at an angle, it usually:",
       "a", "进入空气（光疏介质）时，光线远离法线，折射角大于入射角。",
       "Entering air (an optically less dense medium), the ray bends away from the normal, so the angle of refraction is larger than the angle of incidence.",
       options=_opts(("远离法线", "bend away from the normal"),
                     ("向法线偏折", "bend towards the normal"),
                     ("速度不变所以不偏折", "keep the same speed and so not bend"),
                     ("颜色立刻变成单一红色", "instantly become a single red colour"))),
    PQ("q-ph-ps02-03","physics-8Ps-s02","mcq",
       "折射中的入射角和折射角同样是从哪一条线量起？",
       "In refraction, the angles of incidence and refraction are also measured from:",
       "c", "和反射一样，必须从法线量起。",
       "As with reflection, they are measured from the normal.",
       options=_opts(("界面（玻璃表面）", "the boundary (the glass surface)"),
                     ("光线本身的延长线", "the extension of the ray itself"),
                     ("法线", "the normal"),
                     ("实验桌的边缘", "the edge of the bench"))),
    PQ("q-ph-ps02-04","physics-8Ps-s02","short",
       "光线从空气垂直（沿法线）射入玻璃，方向会怎样？",
       "A ray travels from air into glass along the normal (straight on). What happens to its direction?",
       "no bending", "沿法线入射时不偏折，方向不变，但在玻璃中速度会变慢。",
       "Along the normal there is no bending: the direction stays the same, although the light slows down in the glass.",
       accepted=["no bending","does not bend","straight on","no change of direction","不偏折","不改变方向","沿直线","无折射偏折","goes straight"]),
    PQ("q-ph-ps02-05","physics-8Ps-s02","mcq",
       "空气—水界面上的折射，与空气—玻璃相比？",
       "Refraction at an air–water boundary, compared with air–glass:",
       "d", "道理相同：进入水（比空气光密）时向法线偏折。偏折程度可以不同，但规则一样。",
       "The same rule applies: entering water (optically denser than air) the ray bends towards the normal. The amount of bending may differ, but the rule is the same.",
       options=_opts(("水中光线不会折射", "light does not refract in water"),
                     ("规则完全相反", "the rule is completely reversed"),
                     ("只在海水中成立", "it only works in sea water"),
                     ("同样是进入更光密介质时向法线偏折", "again, the ray bends towards the normal when entering a denser medium"))),
    PQ("q-ph-ps02-06","physics-8Ps-s02","mcq",
       "为什么池底看起来比实际更浅，一个光学原因是？",
       "A pool can look shallower than it really is. One optical reason is:",
       "a", "从水中射向空气的光线在水面远离法线偏折，我们沿直线追迹光线，会觉得池底被“抬高”了。",
       "Rays from the water bend away from the normal at the surface; we trace them back in straight lines and the bottom appears raised.",
       options=_opts(("水中射出的光线在水面远离法线，看起来池底被抬高", "rays leaving the water bend away from the normal, so the bottom looks raised"),
                     ("水把光线全部吸收了", "the water absorbs all the light"),
                     ("这只与磁场有关", "it is only to do with magnetism"),
                     ("反射定律被破坏了", "the law of reflection has failed"))),
    PQ("q-ph-ps02-07","physics-8Ps-s02","mcq",
       "第 8 阶段讨论的空气—玻璃或空气—水折射，正确的图应画出？",
       "A correct Stage 8 diagram for air–glass or air–water refraction should show:",
       "b", "界面、法线、入射光线和折射光线，并标出从法线量起的角。不要把折射画成反射那样 $i=r$。",
       "The boundary, the normal, the incident ray and the refracted ray, with angles marked from the normal. Do not draw refraction as if $i=r$.",
       options=_opts(("只有反射光线，没有进入第二种介质的光线", "only a reflected ray, with no ray entering the second medium"),
                     ("界面、法线、入射光线和折射光线", "the boundary, the normal, the incident ray and the refracted ray"),
                     ("把玻璃画成一面普通平面镜即可", "the glass drawn simply as an ordinary plane mirror"),
                     ("不需要法线", "no need for a normal"))),
]
add(lesson("physics-8Ps-s02","空气—玻璃与空气—水的折射","Refraction at air–glass and air–water",
"本节你将学会描述光线在空气与玻璃、空气与水的界面上如何偏折，并正确从法线量角。",
"You will learn to describe how a ray bends at air–glass and air–water boundaries, and to measure the angles from the normal.",
r"""- **折射**是光线进入另一种介质时方向发生偏折。
- 角仍从**法线**量起。
- 从空气进入玻璃或水（更光密）：光线**向法线**偏折，折射角小于入射角。
- 从玻璃或水进入空气：光线**远离法线**。
- 沿法线垂直入射时，方向不偏折（但光速会改变）。""",
r"""- **Refraction** is the change in direction when light enters another medium.
- Angles are still measured from the **normal**.
- From air into glass or water (optically denser): the ray bends **towards the normal**, so the angle of refraction is smaller than the angle of incidence.
- From glass or water into air: the ray bends **away from the normal**.
- Along the normal there is no change of direction (though the speed of light does change).""",
r"""光线不只会反射，进入玻璃或水时还会**折射**。空气中光速较大，玻璃或水中光速较小。当光线斜着进入较慢的介质，它会向法线偏折；斜着进入较快的介质，则远离法线。

空气—水和空气—玻璃遵守同一条规则，只是偏折程度可以不同。

## 例题 1

光线从空气以一定入射角射入玻璃：折射光线比入射光线更靠近法线。

## 例题 2

沿法线射入时不偏折，不要为了“看起来有折射”而故意把直线画弯。

池水看起来比实际浅，是因为从水中射向空气的光线在水面远离法线，眼睛沿着直线追迹，池底的像被抬高了。

第 8 阶段要求会描述空气—玻璃和空气—水的折射并画简单图，不必引入折射率的完整计算。""",
r"""Light does not only reflect: it also **refracts** when it enters glass or water. Light is faster in air than in glass or water. A ray entering the slower medium at an angle bends towards the normal; a ray entering the faster medium bends away from the normal.

Air–water and air–glass follow the same rule; only the amount of bending may differ.

## Worked example 1

A ray goes from air into glass at an angle: the refracted ray is closer to the normal than the incident ray was.

## Worked example 2

Along the normal there is no bending — do not curve the line just to “make refraction visible”.

A pool can look shallower than it is because rays leaving the water bend away from the normal, and the eye traces them back in straight lines, so the image of the bottom is raised.

Stage 8 asks you to describe refraction at air–glass and air–water and to draw a simple diagram, not to complete a full refractive-index calculation.""",
r"""- **把折射画成 $i=r$。** 那是反射。折射时两个角一般不相等。
- **搞反“向法线 / 远离法线”。** 进入更光密（更慢）的介质：向法线；出来：远离法线。
- **仍然从界面量角。** 和反射一样，要从法线量。""",
r"""- **Drawing refraction as if $i=r$.** That is the reflection law. In refraction the two angles are usually not equal.
- **Reversing “towards / away from the normal”.** Into a denser (slower) medium: towards the normal; out again: away from it.
- **Still measuring from the boundary.** As with reflection, measure from the normal.""",
[q["id"] for q in qs], diagram=D_REFRACT))
questions += qs

# ----- 8Ps.s03 dispersion -----
qs = [
    PQ("q-ph-ps03-01","physics-8Ps-s03","mcq",
       "白光通过三棱镜后展开成光谱，这种现象称为？",
       "White light spread into a spectrum by a triangular prism is called:",
       "c", "这是色散：白光由不同颜色的光组成，它们在玻璃中偏折程度不同。",
       "This is dispersion: white light is made of different colours, which are bent by different amounts in glass.",
       options=_opts(("只发生反射", "reflection only"),
                     ("磁化", "magnetisation"),
                     ("色散", "dispersion"),
                     ("扩散", "diffusion"))),
    PQ("q-ph-ps03-02","physics-8Ps-s03","mcq",
       "在玻璃棱镜产生的光谱中，通常偏折最大的可见光是？",
       "In the spectrum produced by a glass prism, the visible colour that is usually bent the most is:",
       "a", "紫光通常偏折最大，红光偏折最小。顺序可记为红橙黄绿蓝靛紫。",
       "Violet is usually bent the most, and red the least. A useful order is red, orange, yellow, green, blue, indigo, violet.",
       options=_opts(("紫光", "violet"),
                     ("红光", "red"),
                     ("只是绿光", "green only"),
                     ("所有颜色完全相同", "all colours equally"))),
    PQ("q-ph-ps03-03","physics-8Ps-s03","mcq",
       "白光色散说明白光？",
       "The dispersion of white light shows that white light:",
       "b", "白光不是单一颜色，而是由多种色光混合而成。",
       "White light is not a single colour; it is a mixture of different colours.",
       options=_opts(("本身只有一种颜色，棱镜“制造”了其他颜色", "is itself only one colour, and the prism “creates” the others"),
                     ("由多种色光组成", "is made up of a range of colours"),
                     ("在真空中不能传播", "cannot travel in a vacuum"),
                     ("与声波是同一种波", "is the same kind of wave as sound"))),
    PQ("q-ph-ps03-04","physics-8Ps-s03","short",
       "在可见光谱里，哪一种色光通过棱镜时通常偏折最小？",
       "Which visible colour is usually bent the least by a prism?",
       "red", "红光偏折最小，紫光偏折最大。",
       "Red is bent the least, and violet the most.",
       accepted=["red","red light","红","红光"]),
    PQ("q-ph-ps03-05","physics-8Ps-s03","mcq",
       "色散能够发生，是因为不同色光在玻璃中？",
       "Dispersion happens because different colours in glass:",
       "d", "不同色光折射率不同，因而折射角不同，离开棱镜后被分开。",
       "Different colours have slightly different refractive effects, so they leave the prism in slightly different directions and separate.",
       options=_opts(("速度和方向都绝对相同", "travel at exactly the same speed and in exactly the same direction"),
                     ("全部被镜面反射，角度相同", "are all reflected from a mirror at the same angle"),
                     ("变成了带电粒子", "turn into charged particles"),
                     ("偏折程度略有不同，因而被分开", "are bent by slightly different amounts and so separate"))),
    PQ("q-ph-ps03-06","physics-8Ps-s03","mcq",
       "若把光谱中的各色光再适当会合，可能得到？",
       "If the colours of the spectrum are recombined in a suitable way, you may obtain:",
       "a", "各色光是从白光分开的，再会合可以重新得到白光。这说明棱镜并没有“制造”新的颜色。",
       "The colours were separated from white light, so recombining them can give white light again. The prism did not “create” new colours.",
       options=_opts(("白光", "white light"),
                     ("只有声波", "sound waves only"),
                     ("一个磁场", "a magnetic field"),
                     ("真空", "a vacuum"))),
    PQ("q-ph-ps03-07","physics-8Ps-s03","mcq",
       "画棱镜色散图时，白光从一边射入，另一边应画出？",
       "On a prism dispersion diagram, white light enters one side. The other side should show:",
       "c", "展开的光谱，红光偏折较小、紫光偏折较大，中间是其他可见色光。",
       "A spread spectrum, with red bent less than violet, and the other visible colours in between.",
       options=_opts(("一条不偏折的白光，完全不变", "a single undeviated white ray, unchanged"),
                     ("只有反射回原路的光线", "only a ray reflected back the way it came"),
                     ("分开的色光，红偏折较小、紫偏折较大", "separated colours, red bent less than violet"),
                     ("与入射白光完全对称的一条黑线", "a black line exactly symmetrical to the incoming white ray"))),
]
add(lesson("physics-8Ps-s03","白光的色散","Dispersion of white light",
"本节你将学会解释白光通过棱镜色散成光谱，并记住红光与紫光的偏折差异。",
"You will learn to explain how a prism disperses white light into a spectrum, and to recall how red and violet are bent differently.",
r"""- **白光**由多种可见色光混合而成。
- **色散**是这些色光被分开，形成光谱。
- 三棱镜中，不同色光偏折程度不同。
- 通常：**红光偏折最小，紫光偏折最大**。
- 顺序可记：红、橙、黄、绿、蓝、靛、紫。
- 把色光再会合，可以重新得到白光。""",
r"""- **White light** is a mixture of many visible colours.
- **Dispersion** is the separating of those colours into a spectrum.
- In a triangular prism, different colours are bent by different amounts.
- Usually, **red is bent the least and violet the most**.
- A useful order: red, orange, yellow, green, blue, indigo, violet.
- Recombining the colours can give white light again.""",
r"""让一束白光斜着通过玻璃三棱镜，屏幕上会出现一条彩色光谱，而不是一条白带。这就是**色散**。

原因不是棱镜“制造”了颜色，而是白光本来就含有不同色光。它们在玻璃中的偏折略有不同，离开第二面时就被分开了。红光偏折最小，紫光偏折最大。

## 例题

画出：一束白光射入棱镜，从另一面射出一组扇形色光，红在偏折较小的一侧，紫在偏折较大的一侧。

如果再用适当的方式把这些色光会合，可以重新得到白光。这进一步说明颜色原先就在白光里。

第 8 阶段 8Ps 讨论的是光；本阶段官方学习目标不把声音放在 8Ps 中，声音在其他学段学习。""",
r"""A beam of white light sent through a glass triangular prism produces a coloured spectrum on a screen, not a white band. That is **dispersion**.

The prism does not “create” the colours: white light already contains them. They are bent by slightly different amounts in glass, so they leave the second face separated. Red is bent the least, violet the most.

## Worked example

Draw a white ray entering the prism and a fan of colours leaving the other side, with red on the less-deviated side and violet on the more-deviated side.

If the colours are recombined in a suitable way, you can obtain white light again. That is further evidence that the colours were in the white light already.

Stage 8 8Ps is about light; the official learning objectives do not place sound in 8Ps. Sound is studied in other stages.""",
r"""- **以为棱镜创造了颜色。** 它只是把原已存在的色光分开。
- **记反红与紫的偏折。** 红最小，紫最大。
- **把色散与反射定律或扩散混为一谈。** 色散是不同色光折射程度不同。""",
r"""- **Thinking the prism creates the colours.** It only separates colours that were already there.
- **Swapping red and violet.** Red is bent least, violet most.
- **Mixing dispersion up with the reflection law or with diffusion.** Dispersion is different colours being refracted by different amounts.""",
[q["id"] for q in qs], diagram=D_DISPERSION))
questions += qs

# ----- 8Ps.s04 coloured light -----
qs = [
    PQ("q-ph-ps04-01","physics-8Ps-s04","mcq",
       "红光与绿光按一定方式叠加，通常可以得到？",
       "Red light and green light added in a suitable way usually give:",
       "b", "红加绿可以得到黄。这是色光的叠加（加色）。",
       "Red plus green can give yellow. This is addition of coloured light (additive colour).",
       options=_opts(("只有黑", "black only"),
                     ("黄", "yellow"),
                     ("与颜料完全相同的结果，所以一定是蓝", "exactly the same result as with paints, so it must be blue"),
                     ("磁场", "a magnetic field"))),
    PQ("q-ph-ps04-02","physics-8Ps-s04","mcq",
       "红、绿、蓝三束色光适当叠加，可以得到？",
       "Red, green and blue light added in a suitable way can give:",
       "a", "这三种是常用的加色三原色，适当叠加可以得到白光。",
       "These are the usual additive primary colours; added suitably they can give white light.",
       options=_opts(("白光", "white light"),
                     ("一定只有红光", "red light only, always"),
                     ("真空", "a vacuum"),
                     ("声波", "a sound wave"))),
    PQ("q-ph-ps04-03","physics-8Ps-s04","mcq",
       "白光照射一块只反射绿光、吸收其他可见光的物体，它看起来通常是？",
       "White light falls on an object that reflects only green light and absorbs the other visible colours. The object usually looks:",
       "c", "我们看到的是被反射进入眼睛的色光。只反射绿光的物体看起来是绿色的。",
       "We see the coloured light that is reflected into the eye. An object that reflects only green looks green.",
       options=_opts(("白色，因为入射光是白光", "white, because the incoming light is white"),
                     ("黑色，因为吸收了部分光", "black, because some light is absorbed"),
                     ("绿色", "green"),
                     ("没有颜色，因为光被吸收了就看不见物体", "colourless, because absorbed light means the object cannot be seen"))),
    PQ("q-ph-ps04-04","physics-8Ps-s04","mcq",
       "白光下看起来是红色的滤光片，主要作用通常是？",
       "A filter that looks red in white light usually:",
       "d", "滤光片透射某些色光、吸收另一些。红滤光片主要让红光通过，吸收大部分其他可见光。",
       "A filter transmits some colours and absorbs others. A red filter mainly lets red through and absorbs most other visible colours.",
       options=_opts(("让所有色光同样通过", "lets every colour through equally"),
                     ("把所有光都变成磁场", "turns all the light into a magnetic field"),
                     ("只反射紫外线", "reflects only ultraviolet"),
                     ("主要透射红光，吸收其他许多色光", "mainly transmits red light and absorbs many other colours"))),
    PQ("q-ph-ps04-05","physics-8Ps-s04","short",
       "几乎吸收全部可见光、几乎不反射的物体，看起来是什么颜色？",
       "What colour does an object look if it absorbs almost all visible light and reflects almost none?",
       "black", "几乎没有色光进入眼睛，物体看起来是黑色的。",
       "Almost no coloured light reaches the eye, so the object looks black.",
       accepted=["black","black colour","黑","黑色"]),
    PQ("q-ph-ps04-06","physics-8Ps-s04","mcq",
       "蓝光照射一块只能反射红光（吸收蓝光）的物体，它看起来最可能是？",
       "Blue light falls on an object that can reflect only red light (and absorbs blue). The object is most likely to look:",
       "a", "入射光中几乎没有可被反射的红光，蓝光又被吸收，进入眼睛的光很少，物体看起来很暗或接近黑色。",
       "There is almost no red light to reflect, and the blue is absorbed, so little light reaches the eye and the object looks very dark or nearly black.",
       options=_opts(("很暗或接近黑色", "very dark or nearly black"),
                     ("明亮的白色", "bright white"),
                     ("明亮的红色，与白光下完全一样", "bright red, exactly as in white light"),
                     ("绿色", "green"))),
    PQ("q-ph-ps04-07","physics-8Ps-s04","mcq",
       "色光的叠加与颜料的混合常常不同。一个关键差别是？",
       "Adding coloured lights is often different from mixing paints. A key difference is that:",
       "b", "色光叠加是把光加在一起（加色）；颜料更多地是吸收（减色）。红光加绿光可得黄，红颜料加绿颜料通常得不到明亮的黄光效果。",
       "Adding lights puts light together (additive); paints mainly absorb (subtractive). Red light plus green light can give yellow; red and green paints usually do not give a bright yellow-light effect.",
       options=_opts(("二者在任何情况下结果都完全一样", "the results are identical in every case"),
                     ("色光是叠加（加色），颜料更多是吸收（减色）", "lights add (additive); paints mainly absorb (subtractive)"),
                     ("颜料会发光，色光只会吸收", "paints emit light, and coloured light only absorbs"),
                     ("只有颜料遵守反射定律", "only paints obey the law of reflection"))),
    PQ("q-ph-ps04-08","physics-8Ps-s04","mcq",
       "绿光与品红光（品红可看作红加蓝）适当叠加，最可能得到？",
       "Green light and magenta light (magenta can be thought of as red plus blue) added suitably are most likely to give:",
       "c", "品红含红与蓝，再加绿，相当于红绿蓝会合，可得白光。这是色光叠加，不是颜料混合。",
       "Magenta contains red and blue; adding green is like bringing red, green and blue together, which can give white. This is addition of light, not mixing paint.",
       options=_opts(("只有绿", "green only"),
                     ("一定是黑", "black, always"),
                     ("白", "white"),
                     ("不可能叠加", "they cannot be added"))),
]
add(lesson("physics-8Ps-s04","色光的叠加、减弱、吸收与反射","Adding, subtracting, absorbing and reflecting coloured light",
"本节你将学会解释色光如何叠加，以及物体和滤光片如何吸收、透射或反射色光从而呈现颜色。",
"You will learn how coloured lights add, and how objects and filters absorb, transmit or reflect colours so that we see a colour.",
r"""- 色光可以**叠加**（加色）。常用三原色：红、绿、蓝；适当叠加可得白光。
- 红+绿 → 黄；红+蓝 → 品红；绿+蓝 → 青。
- 物体的颜色主要取决于它**反射**（或透射）哪些色光、**吸收**哪些色光。
- 滤光片让某些色光通过，吸收其他色光（一种“减弱”）。
- 几乎吸收全部可见光的物体看起来是黑色的。
- 色光叠加与颜料混合（减色）常常不同。""",
r"""- Coloured lights can be **added** (additive colour). Common primaries: red, green and blue; added suitably they can give white.
- Red + green → yellow; red + blue → magenta; green + blue → cyan.
- An object’s colour depends mainly on which colours it **reflects** (or transmits) and which it **absorbs**.
- A filter lets some colours through and absorbs others (a kind of “subtraction”).
- An object that absorbs almost all visible light looks black.
- Adding lights is often different from mixing paints (subtractive colour).""",
r"""第 8 阶段要求描述色光的叠加、减弱（减去某些色光）、吸收和反射。

把红光和绿光打在同一白屏上，叠加区域可以是黄色。红、绿、蓝三束适当会合可以得到白光。这是**加色**。

不透明物体的颜色，是因为它反射某些色光、吸收另一些。白光下的绿叶反射较多绿光。若只用蓝光去照一块只反射红光的物体，蓝光被吸收，又几乎没有红光可反射，物体看起来就很暗。

滤光片则是让一部分色光透射、吸收其余。红滤光片主要放行红光。

注意：颜料混合是另一种过程（更多是减色），不要把“红颜料加绿颜料”直接等同于“红光加绿光”。""",
r"""Stage 8 asks you to describe adding and subtracting coloured light, and absorption and reflection.

Shine red and green light onto the same white screen and the overlap can look yellow. Red, green and blue together can give white. This is **additive** colour.

An opaque object has a colour because it reflects some colours and absorbs others. A green leaf in white light reflects more of the green. If you light an object that can reflect only red with blue light alone, the blue is absorbed and there is almost no red to reflect, so the object looks very dark.

A filter transmits some colours and absorbs the rest. A red filter mainly passes red light.

Mixing paints is a different process (more subtractive). Do not treat “red paint plus green paint” as the same as “red light plus green light”.""",
r"""- **用颜料规则去套色光。** 红光加绿光可以得黄，颜料却常常得暗浊的颜色。
- **以为物体颜色与照明无关。** 没有相应色光可反射时，物体看起来会变暗或变色。
- **以为吸收了光的物体一定消失。** 吸收后看起来是黑或暗，物体仍在。""",
r"""- **Using paint rules for light.** Red light plus green light can give yellow; paints often give a dull colour instead.
- **Thinking an object’s colour is independent of the lighting.** If the colour it could reflect is not present, it may look dark or different.
- **Thinking an object that absorbs light must vanish.** It looks black or dark, but it is still there.""",
[q["id"] for q in qs], diagram=D_COLOUR))
questions += qs

# ----- 8Pe.s01 magnetic fields -----
qs = [
    PQ("q-ph-pe01-01","physics-8Pe-s01","mcq",
       "磁场最简明的含义是？",
       "A magnetic field is, in brief:",
       "b", "磁场是磁体周围有磁力作用的空间。",
       "A magnetic field is the region around a magnet where magnetic forces act.",
       options=_opts(("只有真空中才有的声音", "a sound that exists only in a vacuum"),
                     ("磁体周围有磁力作用的空间", "the region around a magnet where magnetic forces act"),
                     ("电流的另一种名称", "just another name for electric current"),
                     ("与磁体无关的温度场", "a temperature field unrelated to magnets"))),
    PQ("q-ph-pe01-02","physics-8Pe-s01","mcq",
       "画条形磁体的磁场方向时，磁感线在磁体外通常画成？",
       "For the field around a bar magnet, field lines outside the magnet are usually drawn:",
       "a", "在磁体外，磁感线从 N 极出发，回到 S 极。箭头表示放在该处的小磁针 N 极受力方向。",
       "Outside the magnet, field lines leave the N pole and return to the S pole. The arrows show the direction of the force on the N pole of a small compass needle.",
       options=_opts(("从 N 极出发，回到 S 极", "leaving the N pole and returning to the S pole"),
                     ("从 S 极出发，回到 N 极", "leaving the S pole and returning to the N pole"),
                     ("只画封闭的正方形，没有方向", "as closed squares with no direction"),
                     ("全部平行于地面且没有起点", "all parallel to the ground with no starting point"))),
    PQ("q-ph-pe01-03","physics-8Pe-s01","mcq",
       "磁感线画得更密的地方，通常表示磁场？",
       "Where field lines are drawn closer together, the magnetic field is usually:",
       "c", "磁感线越密，磁场越强，例如靠近磁极处。",
       "Closer field lines mean a stronger field, for example near the poles.",
       options=_opts(("更弱", "weaker"),
                     ("完全为零", "exactly zero"),
                     ("更强", "stronger"),
                     ("与疏密无关", "unrelated to how close the lines are"))),
    PQ("q-ph-pe01-04","physics-8Pe-s01","short",
       "用什么简单仪器可以显示磁体周围磁场的方向？",
       "What simple instrument can show the direction of the field around a magnet?",
       "compass", "小磁针（指南针）的 N 极指向该处磁场的方向。也可用铁屑显示磁感线的形状。",
       "A plotting compass (the N pole of a small needle) points in the direction of the field. Iron filings can show the shape of the field.",
       accepted=["compass","plotting compass","a compass","磁针","小磁针","指南针","compass needle"]),
    PQ("q-ph-pe01-05","physics-8Pe-s01","mcq",
       "两个磁极靠近时，下列说法正确的是？",
       "When two magnetic poles are brought close together, which statement is correct?",
       "d", "同名磁极相斥，异名磁极相吸。这是磁场对另一个磁极施加力的表现。",
       "Like poles repel and unlike poles attract. That is the field exerting a force on another pole.",
       options=_opts(("同名磁极相吸", "Like poles attract"),
                     ("磁极之间没有力", "There is never a force between poles"),
                     ("只有 S 极之间有力", "Only S poles exert forces"),
                     ("同名相斥，异名相吸", "Like poles repel and unlike poles attract"))),
    PQ("q-ph-pe01-06","physics-8Pe-s01","mcq",
       "磁场是一种模型。磁感线是？",
       "A magnetic field is a model. Field lines are:",
       "a", "磁感线是帮助我们描述磁场方向和强弱的图示，并不是一根根真实的绳子。",
       "Field lines are a diagram to help us describe the direction and strength of the field; they are not real strings in space.",
       options=_opts(("用来表示方向和相对强弱的图线，不是真实的绳子", "diagram lines for direction and relative strength, not real strings"),
                     ("可以捡起来的细铁丝", "thin iron wires you can pick up"),
                     ("电流本身", "the electric current itself"),
                     ("只在水中出现", "found only in water"))),
    PQ("q-ph-pe01-07","physics-8Pe-s01","mcq",
       "在条形磁体的中垂线上、离磁体较远处，与靠近磁极处相比，磁场通常？",
       "On the perpendicular bisector of a bar magnet, far from the magnet, the field compared with a point near a pole is usually:",
       "b", "远离磁体处磁感线较疏，磁场较弱。",
       "Farther away the field lines are more spaced out, so the field is weaker.",
       options=_opts(("更强", "stronger"),
                     ("更弱", "weaker"),
                     ("方向无法用磁针判断", "impossible to test with a compass"),
                     ("一定完全消失且不可再检测", "always completely gone and undetectable"))),
]
add(lesson("physics-8Pe-s01","磁场","Magnetic fields",
"本节你将学会说明什么是磁场，用磁感线描述其方向和强弱，并用小磁针探测。",
"You will learn what a magnetic field is, how to show its direction and strength with field lines, and how to explore it with a plotting compass.",
r"""- **磁场**是磁体周围有磁力作用的空间。
- 磁感线在磁体外从 **N 极指向 S 极**。
- 箭头表示放在该处的小磁针 N 极的受力方向。
- 磁感线越密，磁场越强。
- 同名磁极相斥，异名磁极相吸。
- 磁感线是模型，不是真实的绳子。""",
r"""- A **magnetic field** is the region around a magnet where magnetic forces act.
- Outside a magnet, field lines run from the **N pole to the S pole**.
- Arrows show the direction of the force on the N pole of a small compass needle.
- Closer field lines mean a stronger field.
- Like poles repel; unlike poles attract.
- Field lines are a model, not real strings.""",
r"""磁体不必接触也能吸引或排斥另一磁体，因为周围存在着**磁场**。

我们用磁感线来描述它：在磁体外从 N 到 S，靠近磁极处画得更密。把小磁针放在磁体周围，针的 N 极指向该点磁场的方向，把许多位置连起来就得到磁场图。铁屑也可以显示磁场的形状。

## 例题

画一条形磁体：两端标 N、S，外侧磁感线从 N 出发绕向 S，磁极附近线条更密。不要把箭头画成从 S 到 N。

磁场图是一种模型，帮助我们讨论“那里有力、力朝哪边、哪里更强”，并不是空间里真的嵌着线条。""",
r"""A magnet can attract or repel another magnet without touching it, because there is a **magnetic field** around it.

We describe the field with field lines: outside the magnet they run from N to S, and we draw them closer together near the poles. A plotting compass placed around the magnet points its N pole in the direction of the field at that point; joining many positions gives a field map. Iron filings can show the shape of the field.

## Worked example

Draw a bar magnet labelled N and S, with field lines leaving N and curving to S, closer together near the poles. Do not draw the arrows from S to N.

Field lines are a model. They help us talk about where a force acts, which way it acts, and where it is stronger — they are not real threads in space.""",
r"""- **把磁感线方向画反。** 磁体外是 N → S。
- **以为线条是实物。** 它只是图示。
- **忽略疏密。** 疏密表示相对强弱，不是装饰。""",
r"""- **Drawing field lines the wrong way.** Outside the magnet they go N → S.
- **Treating the lines as real objects.** They are a diagram.
- **Ignoring spacing.** Spacing shows relative strength; it is not decoration.""",
[q["id"] for q in qs], diagram=D_FIELD))
questions += qs

# ----- 8Pe.s02 making electromagnets -----
qs = [
    PQ("q-ph-pe02-01","physics-8Pe-s02","mcq",
       "最简单的电磁铁通常是？",
       "The simplest electromagnet is usually:",
       "b", "在铁芯上绕绝缘导线，通以电流，铁芯就被磁化，成为电磁铁。",
       "Insulated wire wound around an iron core, with a current in the coil, magnetises the core and makes an electromagnet.",
       options=_opts(("一块永远不能关断的永磁体", "a permanent magnet that can never be switched off"),
                     ("绕在铁芯上的线圈，并通以电流", "a coil of wire around an iron core, with a current in the coil"),
                     ("只含玻璃的棱镜", "a glass prism only"),
                     ("一根不接电路的木棒", "a wooden rod not connected to a circuit"))),
    PQ("q-ph-pe02-02","physics-8Pe-s02","mcq",
       "电磁铁相对于永磁体的一个重要优点是？",
       "An important advantage of an electromagnet compared with a permanent magnet is that it:",
       "c", "切断电流后磁性可以大大减弱或消失，因此能够开关，便于控制和放工件。",
       "When the current is switched off the magnetism can fall greatly or vanish, so it can be switched, controlled, and used to drop a load.",
       options=_opts(("永远无法控制", "can never be controlled"),
                     ("只能排斥，不能吸引", "can only repel, never attract"),
                     ("可以通断电来开关磁性", "can be switched on and off by switching the current"),
                     ("不需要任何导线", "needs no wire at all"))),
    PQ("q-ph-pe02-03","physics-8Pe-s02","mcq",
       "断开电源后，电磁铁通常会？",
       "When the current is switched off, an electromagnet usually:",
       "a", "线圈产生的磁场随之消失（铁芯可能留下很弱的剩磁），因此能放下被吸住的铁质物体。",
       "The field due to the coil disappears (the core may keep a weak remnant), so a lifted iron object can be released.",
       options=_opts(("磁性大大减弱或消失，可放下工件", "lose most or all of its magnetism, so a load can be dropped"),
                     ("变成更强的永磁体，再也放不下东西", "become a stronger permanent magnet and never release a load"),
                     ("开始发出白光色散", "begin to disperse white light"),
                     ("质量变为零", "have zero mass"))),
    PQ("q-ph-pe02-04","physics-8Pe-s02","short",
       "为什么电磁铁的线圈常用绝缘导线？",
       "Why is the wire in an electromagnet coil usually insulated?",
       "short circuit", "绝缘避免相邻线圈直接短路，电流才能沿线圈一圈圈绕过铁芯。",
       "Insulation stops neighbouring turns shorting; the current can then travel around the core turn by turn.",
       accepted=["short circuit","prevent a short","insulation prevents shorting","avoid short","防短路","防止短路","避免短路","绝缘防短路","so turns do not short"]),
    PQ("q-ph-pe02-05","physics-8Pe-s02","mcq",
       "电磁铁常用于？",
       "Electromagnets are commonly used in:",
       "d", "例如废铁场的起重电磁铁、电铃、继电器、某些门锁等，都需要可开关的磁性。",
       "Examples include scrap-yard lifting magnets, electric bells, relays and some door locks — all need magnetism that can be switched.",
       options=_opts(("只能测量路程—时间图像的斜率", "measuring the gradient of a distance–time graph only"),
                     ("代替所有平面镜", "replacing every plane mirror"),
                     ("在真空中传播声音", "sending sound through a vacuum"),
                     ("可开关的起重、电铃、继电器等", "switchable lifting, bells, relays and similar devices"))),
    PQ("q-ph-pe02-06","physics-8Pe-s02","mcq",
       "铁芯的作用主要是？",
       "The main job of the iron core is to:",
       "b", "铁是磁性材料，能使线圈的磁场大大增强并集中。常用软铁，以便断电后磁性尽快减弱。",
       "Iron is a magnetic material, so it greatly strengthens and concentrates the field of the coil. Soft iron is used so that the magnetism falls quickly when the current stops.",
       options=_opts(("让线圈变成绝缘体", "turn the coil into an insulator"),
                     ("增强并集中磁场", "strengthen and concentrate the magnetic field"),
                     ("阻止任何电流通过", "stop any current flowing"),
                     ("产生色散光谱", "produce a dispersion spectrum"))),
    PQ("q-ph-pe02-07","physics-8Pe-s02","mcq",
       "制作并使用电磁铁时，一个必要的条件是？",
       "A necessary condition when making and using an electromagnet is:",
       "a", "必须有电流通过线圈。没有电流，就没有这种可开关的磁场。",
       "There must be a current in the coil. Without a current there is no such switchable field.",
       options=_opts(("线圈中有电流", "a current in the coil"),
                     ("线圈必须浸在水银里", "the coil must be immersed in mercury"),
                     ("铁芯必须是塑料", "the core must be plastic"),
                     ("周围必须完全没有空气", "there must be no air at all around it"))),
]
add(lesson("physics-8Pe-s02","制作与使用电磁铁","Making and using electromagnets",
"本节你将学会说明电磁铁如何构成、如何开关，并举出它的一些用途。",
"You will learn how an electromagnet is made, how it is switched, and some of the ways it is used.",
r"""- 电磁铁：绝缘导线绕在**铁芯**上，线圈中通以**电流**。
- 通电时有磁场，可以吸引铁质物体。
- **断电**后磁性大大减弱或消失，因此可以开关、放下工件。
- 铁芯增强并集中磁场；常用软铁，便于迅速退磁。
- 用途：起重电磁铁、电铃、继电器、某些电磁门锁等。""",
r"""- An electromagnet: insulated wire wound around an **iron core**, with a **current** in the coil.
- When the current is on there is a field that can attract iron objects.
- When the current is **off**, the magnetism falls greatly or vanishes, so it can be switched and a load can be dropped.
- The core strengthens and concentrates the field; soft iron is used so that it demagnetises quickly.
- Uses: lifting magnets, electric bells, relays, some electromagnetic locks.""",
r"""永磁体的磁性很难随时关掉。电磁铁把线圈和铁芯结合起来：电流通过线圈时产生磁场，铁芯把磁场增强。切断电流，磁场就减弱，被吸住的废铁可以放下来。这就是废铁场起重电磁铁的原理。

导线必须绝缘，否则相邻圈会短路，电流不再一圈圈绕过铁芯。

## 例题

要做一个课堂电磁铁：用绝缘导线在铁钉上绕许多圈，接到电池和开关上。闭合开关，铁钉能吸起回形针；断开开关，回形针落下。

电铃、继电器也利用“通电吸合、断电释放”。下一节再定量讨论：哪些因素会改变电磁铁的强弱。""",
r"""A permanent magnet is hard to switch off. An electromagnet combines a coil and an iron core: a current in the coil produces a field, and the core makes that field stronger. Switch the current off and the field falls, so scrap iron can be dropped. That is the idea of a scrap-yard lifting magnet.

The wire must be insulated, otherwise neighbouring turns short and the current does not travel around the core turn by turn.

## Worked example

To make a classroom electromagnet, wind many turns of insulated wire on an iron nail and connect a cell and a switch. Close the switch and the nail can pick up paper clips; open it and the clips fall.

Bells and relays also use “attract when on, release when off”. The next lesson looks at the factors that change the strength of an electromagnet.""",
r"""- **以为电磁铁与永磁体完全一样，不能关断。** 可开关正是它的特点。
- **忽略铁芯或把铁芯换成塑料。** 铁芯对增强磁场很重要。
- **用裸导线密绕。** 容易短路，电磁铁会失效。""",
r"""- **Thinking an electromagnet is just like a permanent magnet and cannot be switched off.** Being switchable is the point.
- **Leaving out the core, or using a plastic core.** The iron core matters for a strong field.
- **Winding bare wire tightly.** It can short, and the electromagnet may fail.""",
[q["id"] for q in qs], diagram=D_ELECTRO))
questions += qs

# ----- 8Pe.s03 factors -----
qs = [
    PQ("q-ph-pe03-01","physics-8Pe-s03","mcq",
       "在其他条件相近时，增大线圈中的电流，电磁铁通常会？",
       "If other conditions are similar, increasing the current in the coil usually makes an electromagnet:",
       "b", "电流越大，磁场通常越强，能吸起的回形针往往越多。",
       "A larger current usually means a stronger field, so the electromagnet can often lift more paper clips.",
       options=_opts(("变弱", "weaker"),
                     ("变强", "stronger"),
                     ("完全失去铁芯", "lose its core completely"),
                     ("与电流无关", "independent of current"))),
    PQ("q-ph-pe03-02","physics-8Pe-s03","mcq",
       "在其他条件相近时，增加线圈匝数，电磁铁通常会？",
       "If other conditions are similar, increasing the number of turns on the coil usually makes an electromagnet:",
       "a", "匝数越多，磁场通常越强。",
       "More turns usually mean a stronger field.",
       options=_opts(("变强", "stronger"),
                     ("一定变弱", "always weaker"),
                     ("只能改变颜色", "change colour only"),
                     ("不再需要电流", "no longer need a current"))),
    PQ("q-ph-pe03-03","physics-8Pe-s03","mcq",
       "比较有铁芯与空心线圈（其他条件相近），通常？",
       "Comparing a coil with an iron core and an air-cored coil (other conditions similar), usually:",
       "c", "铁芯能显著增强磁场，有铁芯的电磁铁更强。",
       "An iron core greatly strengthens the field, so the electromagnet with a core is stronger.",
       options=_opts(("二者完全相同", "they are identical"),
                     ("空心一定更强", "the air-cored coil is always stronger"),
                     ("有铁芯的更强", "the one with an iron core is stronger"),
                     ("铁芯只会减弱磁场", "the core only weakens the field"))),
    PQ("q-ph-pe03-04","physics-8Pe-s03","short",
       "列出两个能使电磁铁更强的因素。",
       "Name two factors that can make an electromagnet stronger.",
       "current and turns", "例如：增大电流；增加匝数；加入（软）铁芯。答出其中两个即可。",
       "For example: a larger current; more turns; adding a (soft) iron core. Any two of these are enough.",
       accepted=["current and turns","current, turns","current and core","turns and core","电流和匝数","电流与匝数","电流和铁芯","匝数和铁芯","更大电流，更多匝数"]),
    PQ("q-ph-pe03-05","physics-8Pe-s03","mcq",
       "做对比实验时，要比较匝数的影响，应？",
       "In a fair test of the effect of the number of turns, you should:",
       "d", "只改变匝数，尽量保持电流、铁芯、回形针种类等其他因素不变。",
       "Change only the number of turns, and keep current, core, type of clips and other factors as steady as possible.",
       options=_opts(("同时随意改电流、铁芯和匝数", "change current, core and turns all at once, at random"),
                     ("不必记录吸起的回形针数目", "not bother recording how many clips are lifted"),
                     ("每次都换一种完全不同的测量方法且不说明", "change the measuring method every time without comment"),
                     ("只改变匝数，控制其他变量", "change only the number of turns and control the other variables"))),
    PQ("q-ph-pe03-06","physics-8Pe-s03","mcq",
       "用吸起回形针的数目比较强弱时，若电流过大导致导线明显发热，可能的问题是？",
       "If you compare strength by counting paper clips, but a very large current makes the wire heat up badly, a problem is:",
       "a", "过热可能改变电阻甚至损坏绝缘，实验不再公平，也有安全风险。电流要在安全范围内增大。",
       "Overheating can change the resistance or damage the insulation, so the test is no longer fair, and it can be unsafe. Increase the current only within a safe range.",
       options=_opts(("实验可能不再公平，且有安全风险", "the test may no longer be fair, and it may be unsafe"),
                     ("发热证明电磁铁一定变弱了", "heating proves the electromagnet must have become weaker"),
                     ("发热与实验完全无关", "heating is completely irrelevant"),
                     ("这时应立刻把铁芯换成塑料", "you should immediately replace the core with plastic"))),
    PQ("q-ph-pe03-07","physics-8Pe-s03","mcq",
       "在安全、其他条件相同的前提下，下列哪一项最能使电磁铁变强？",
       "Safely, and with other conditions the same, which change is most likely to make an electromagnet stronger?",
       "b", "更多匝数、更大电流、加上铁芯都会增强。选项中“增加匝数并保持合适电流”是有效做法。",
       "More turns, a larger current and an iron core all help. Among the options, more turns with a sensible current is an effective change.",
       options=_opts(("把线圈拆成很少几圈，并切断电源", "unwind the coil to a few turns and switch the current off"),
                     ("增加匝数，并保持合适的电流与铁芯", "increase the number of turns, keeping a sensible current and the iron core"),
                     ("拿走铁芯，并把电流降到接近零", "remove the core and reduce the current almost to zero"),
                     ("改用绝缘不良的裸线密绕并用水浇湿", "use poorly insulated bare wire, wound tightly and made wet"))),
]
add(lesson("physics-8Pe-s03","影响电磁铁强弱的因素","Factors that change electromagnet strength",
"本节你将学会指出并解释哪些因素会使电磁铁变强或变弱，并知道如何做较公平的比较。",
"You will learn which factors make an electromagnet stronger or weaker, and how to compare them fairly.",
r"""- 电磁铁强弱受多个因素影响。
- **电流更大**（在安全范围内）→ 通常更强。
- **匝数更多** → 通常更强。
- **有铁芯**（相对空心）→ 通常更强。
- 比较时要做公平实验：一次只改一个因素。
- 可用吸起回形针的数目等简单方法比较。""",
r"""- Several factors affect how strong an electromagnet is.
- A **larger current** (within a safe range) usually makes it stronger.
- **More turns** usually make it stronger.
- An **iron core** (compared with air) usually makes it stronger.
- Compare them fairly: change one factor at a time.
- A simple comparison is the number of paper clips lifted.""",
r"""第 8 阶段要求说明哪些因素会改变电磁铁的强弱。

在安全的前提下：电流越大，线圈产生的磁场通常越强；绕的圈数越多，效果通常也越强；铁芯能把磁场增强并集中，所以有铁芯比空心线圈强得多。

## 例题

两组线圈电流相同、铁芯相同，A 绕 $20$ 匝，B 绕 $50$ 匝。预期 B 能吸起更多回形针。若同时把 B 的电流也加大，就无法判断是匝数还是电流在起作用——这不是公平实验。

电流也不是越大越好到没有限制：导线会发热，过大时有危险。课堂实验要在老师指导下选择合适的电源和通电时间。""",
r"""Stage 8 asks you to describe the factors that change the strength of an electromagnet.

Safely: a larger current usually means a stronger field; more turns usually mean a stronger field; an iron core strengthens and concentrates the field, so a cored coil is much stronger than an air-cored one.

## Worked example

Two coils have the same current and the same core. A has $20$ turns, B has $50$. You would expect B to lift more paper clips. If you also increase B’s current, you can no longer tell whether turns or current made the difference — that is not a fair test.

Current cannot be increased without limit: the wire heats up, and a very large current can be unsafe. In class, choose a suitable supply and time, with your teacher’s guidance.""",
r"""- **一次改好几个因素。** 就说不清到底是什么在起作用。
- **以为电流可以无限制加大。** 要注意发热和安全。
- **忘记铁芯。** 有无铁芯往往带来很明显的差别。""",
r"""- **Changing several factors at once.** Then you cannot tell what caused the difference.
- **Thinking the current can be increased without limit.** Watch heating and safety.
- **Forgetting the core.** With or without iron often makes a large difference.""",
[q["id"] for q in qs], diagram=D_TURNS))
questions += qs

# ----- 8ES.s01 Earth's field -----
qs = [
    PQ("q-ph-es01-01","physics-8ES-s01","mcq",
       "地球周围存在着？",
       "Around the Earth there is:",
       "b", "地球有磁场，类似于一个巨大的条形磁体（这是一个模型）。",
       "The Earth has a magnetic field, similar in a simple model to that of a huge bar magnet.",
       options=_opts(("只有电场，完全没有磁场", "an electric field only, and no magnetic field"),
                     ("磁场", "a magnetic field"),
                     ("一层无法穿透的铁壳，所以没有磁场", "an impenetrable iron shell, so no magnetic field"),
                     ("与磁无关的真空墙", "a vacuum wall unrelated to magnetism"))),
    PQ("q-ph-es01-02","physics-8ES-s01","mcq",
       "指南针能够指示南北，主要是因为？",
       "A compass can show north–south mainly because:",
       "c", "小磁针在地球磁场中受力而转向，其 N 极大致指向地理北方附近（磁北）。",
       "The needle is a small magnet that turns in the Earth’s field; its N pole points roughly towards geographic north (magnetic north).",
       options=_opts(("指南针内部有小型发动机", "there is a small motor inside the compass"),
                     ("太阳光把指针推向南方", "sunlight pushes the needle south"),
                     ("地球磁场使磁针转向", "the Earth’s magnetic field turns the needle"),
                     ("指针只是随风摆动", "the needle only swings with the wind"))),
    PQ("q-ph-es01-03","physics-8ES-s01","mcq",
       "用“地球像条形磁体”的模型时，地理北极附近对应的地磁极是？",
       "In the “Earth as a bar magnet” model, the magnetic pole near the geographic North Pole is:",
       "a", "指南针的 N 极指向地理北方附近，说明那边相当于地磁 S 极（异名相吸）。这是学生常混的一点。",
       "A compass N pole points towards geographic north, so that region behaves as a magnetic S pole (unlike poles attract). This is a common mix-up.",
       options=_opts(("地磁 S 极（所以指南针 N 极被吸向那边）", "a magnetic S pole (so a compass N pole is attracted there)"),
                     ("地磁 N 极，因为地理上也叫北极", "a magnetic N pole, simply because it is called north"),
                     ("完全没有磁极", "no magnetic pole at all"),
                     ("只是一个电场中心", "only the centre of an electric field"))),
    PQ("q-ph-es01-04","physics-8ES-s01","short",
       "指南针的 N 极大致指向什么方向？",
       "Roughly which way does the N pole of a compass point?",
       "north", "大致指向地理北方，更准确说是指向磁北方向。",
       "Roughly towards geographic north, or more precisely towards magnetic north.",
       accepted=["north","magnetic north","geographic north","北","北方","磁北","地理北"]),
    PQ("q-ph-es01-05","physics-8ES-s01","mcq",
       "地球磁场的一个重要作用是？",
       "One important role of the Earth’s magnetic field is that it:",
       "d", "地球磁场可以偏转来自太空的带电粒子，对大气和地表环境有保护作用（第 8 阶段作定性了解即可）。",
       "The Earth’s field can deflect charged particles from space, giving some protection to the atmosphere and surface (a qualitative Stage 8 idea is enough).",
       options=_opts(("让地球停止自转", "stops the Earth rotating"),
                     ("代替太阳发光", "replaces the Sun as a light source"),
                     ("消灭所有引力", "cancels all gravity"),
                     ("有助于偏转部分来自太空的带电粒子", "helps to deflect some charged particles arriving from space"))),
    PQ("q-ph-es01-06","physics-8ES-s01","mcq",
       "地磁北极与地理北极？",
       "Magnetic north and geographic north:",
       "b", "二者接近但不完全重合，所以指南针指向的是磁北，与真北可能有夹角（磁偏角）。第 8 阶段知道它们不是同一点即可。",
       "They are close but not the same, so a compass points to magnetic north, which may differ from true north (magnetic declination). At Stage 8 it is enough to know they are not the same point.",
       options=_opts(("永远精确是同一点", "are always exactly the same point"),
                     ("接近但不完全是同一点", "are close but not exactly the same point"),
                     ("相距半个地球", "are half a world apart, always"),
                     ("每天对换一次位置", "swap places once a day"))),
    PQ("q-ph-es01-07","physics-8ES-s01","mcq",
       "在地球磁场的简单图中，磁感线在地球外部大致？",
       "On a simple diagram of the Earth’s field, field lines outside the Earth run roughly:",
       "a", "与条形磁体类似：在外部从地磁 N 极走向地磁 S 极。记住地理北极附近是地磁 S 极。",
       "As for a bar magnet: outside, they run from the magnetic N pole towards the magnetic S pole. Recall that a magnetic S pole lies near geographic north.",
       options=_opts(("从地磁 N 极走向地磁 S 极", "from the magnetic N pole towards the magnetic S pole"),
                     ("只沿赤道转圈，不进入高纬度", "only in circles around the equator, never at high latitudes"),
                     ("全部指向地心，与磁极无关", "all towards the Earth’s centre, unrelated to the poles"),
                     ("只存在于海洋中", "exist only over the oceans"))),
]
add(lesson("physics-8ES-s01","地球的磁场","The Earth’s magnetic field",
"本节你将学会用简单模型描述地球磁场，并解释指南针为什么能指示南北。",
"You will learn to describe the Earth’s magnetic field with a simple model, and to explain why a compass shows north–south.",
r"""- 地球周围有**磁场**，可用巨型条形磁体作简单模型。
- 指南针是小磁针，在地球磁场中转向。
- 指南针 N 极大致指向**磁北**（靠近地理北方）。
- 因此，地理北极附近相当于**地磁 S 极**（异名相吸）。
- 磁北与真北接近但不完全重合。
- 地球磁场有助于偏转部分来自太空的带电粒子。
- 官方科学把地球与太空列为独立分支；本站为便于复习，把它放在物理课程中。""",
r"""- The Earth has a **magnetic field**, modelled in a simple way as a huge bar magnet.
- A compass is a small magnet that turns in that field.
- The N pole of a compass points roughly to **magnetic north** (near geographic north).
- So the region near the geographic North Pole behaves as a **magnetic S pole** (unlike poles attract).
- Magnetic north and true north are close but not the same.
- The field helps to deflect some charged particles from space.
- Official Science lists Earth and Space as its own strand; it is placed under Physics here for subject review.""",
r"""地球像一块巨大的磁体，周围的磁场让指南针排成大致南北向。这是第 8 阶段地球与太空中与物理关系密切的一点。

容易混淆的是名称：我们把指南针指着的那边叫“北”，但按“异名相吸”，地理北极附近应对应地磁的 S 极。模型图中，地球外部的磁感线仍从地磁 N 极走向地磁 S 极。

磁北和地理北极并不完全重合，所以精密导航还要考虑磁偏角。本阶段知道二者不是同一点即可。

地球磁场还能改变部分来自太空的带电粒子的路径，对地球环境有保护作用。""",
r"""The Earth behaves like a huge magnet, and its field lines up a compass roughly north–south. This is a Stage 8 Earth and Space idea that sits close to physics.

The names are easy to mix up. We call the direction a compass points “north”, but unlike poles attract, so the region near the geographic North Pole corresponds to a magnetic S pole. On a model diagram, field lines outside the Earth still run from the magnetic N pole towards the magnetic S pole.

Magnetic north and the geographic North Pole are not exactly the same, so precise navigation allows for declination. At this stage it is enough to know they are not the same point.

The Earth’s field also changes the paths of some charged particles from space, and this gives some protection to the Earth’s environment.""",
r"""- **以为地理北极就是地磁 N 极。** 指南针 N 极指向那边，说明那边相当于地磁 S 极。
- **以为磁北与真北永远重合。** 它们接近但不相同。
- **忘记指南针本身是小磁体。** 它能转动，正是因为处于地球磁场中。""",
r"""- **Thinking geographic north is a magnetic N pole.** A compass N pole points there, so that region acts as a magnetic S pole.
- **Thinking magnetic north and true north always coincide.** They are close but not the same.
- **Forgetting that a compass is itself a small magnet.** It turns because it sits in the Earth’s field.""",
[q["id"] for q in qs], diagram=D_EARTH))
questions += qs

# ----- 8ES.s02 galaxies -----
qs = [
    PQ("q-ph-es02-01","physics-8ES-s02","mcq",
       "星系是？",
       "A galaxy is:",
       "b", "星系是由大量恒星、气体、尘埃等组成的巨大系统，靠引力聚集在一起。",
       "A galaxy is a huge system of many stars, gas and dust, held together by gravity.",
       options=_opts(("一颗单独的行星", "a single planet"),
                     ("由大量恒星、气体和尘埃组成的巨大系统", "a huge system of many stars, gas and dust"),
                     ("只含一颗恒星的小石头", "a small rock with only one star"),
                     ("地球大气的另一名称", "another name for Earth’s atmosphere"))),
    PQ("q-ph-es02-02","physics-8ES-s02","mcq",
       "太阳系所在的星系是？",
       "The galaxy that contains the Solar System is:",
       "c", "太阳和地球所在的星系是银河系（Milky Way）。",
       "The Sun and Earth lie in the Milky Way galaxy.",
       options=_opts(("一个与银河系无关的小行星群，且不含太阳", "an asteroid group unrelated to the Milky Way, with no Sun"),
                     ("只由木星组成的星系", "a galaxy made only of Jupiter"),
                     ("银河系", "the Milky Way"),
                     ("月球本身", "the Moon itself"))),
    PQ("q-ph-es02-03","physics-8ES-s02","mcq",
       "从大到小，下列顺序较合理的是？",
       "From largest to smallest, a reasonable order is:",
       "a", "宇宙中有许多星系；一个星系含有许多恒星；一颗恒星可以拥有行星系统。太阳系属于银河系。",
       "The Universe contains many galaxies; a galaxy contains many stars; a star may have a planetary system. The Solar System belongs to the Milky Way.",
       options=_opts(("星系 → 恒星（及恒星系统）→ 行星", "galaxy → star (and its system) → planet"),
                     ("行星 → 星系 → 恒星", "planet → galaxy → star"),
                     ("一粒尘埃 → 整个宇宙 → 一颗行星", "a speck of dust → the whole Universe → one planet"),
                     ("月球 → 银河系 → 一颗石子", "the Moon → the Milky Way → a pebble"))),
    PQ("q-ph-es02-04","physics-8ES-s02","short",
       "我们的太阳属于哪个星系？",
       "Which galaxy does our Sun belong to?",
       "Milky Way", "太阳属于银河系。",
       "The Sun belongs to the Milky Way.",
       accepted=["Milky Way","the Milky Way","Milky Way galaxy","银河系","银河"]),
    PQ("q-ph-es02-05","physics-8ES-s02","mcq",
       "夜空中看到的“银河”光带，主要是？",
       "The milky band of light sometimes seen in a dark night sky is mainly:",
       "d", "那是我们从银河系内部侧向看去时，大量遥远恒星发出的光叠在一起。",
       "It is the combined light of huge numbers of distant stars, seen from inside our galaxy, looking through the disc.",
       options=_opts(("近处一盏路灯的反光", "the reflection of a nearby street lamp only"),
                     ("月球表面的一条裂缝", "a crack on the Moon’s surface"),
                     ("地球磁场的可见边缘", "the visible edge of the Earth’s magnetic field"),
                     ("银河系中大量恒星的光叠在一起", "the combined light of many stars in the Milky Way"))),
    PQ("q-ph-es02-06","physics-8ES-s02","mcq",
       "宇宙中星系的数量？",
       "The number of galaxies in the Universe is:",
       "b", "宇宙中有极多星系，银河系只是其中之一，不是唯一的星系。",
       "There are a great many galaxies; the Milky Way is only one of them, not the only galaxy.",
       options=_opts(("恰好只有一个，就是银河系", "exactly one: the Milky Way"),
                     ("非常多，银河系只是其中之一", "very large; the Milky Way is only one of them"),
                     ("为零，星系并不存在", "zero; galaxies do not exist"),
                     ("恰好等于太阳系中的行星数", "exactly equal to the number of planets in the Solar System"))),
    PQ("q-ph-es02-07","physics-8ES-s02","mcq",
       "把太阳系说成“一个星系”，错在哪里？",
       "What is wrong with calling the Solar System “a galaxy”?",
       "a", "太阳系是一颗恒星及其行星等天体组成的系统，规模远小于星系。星系含有极其大量的恒星。",
       "The Solar System is one star and its planets and other bodies, much smaller than a galaxy. A galaxy contains a vast number of stars.",
       options=_opts(("太阳系只是一颗恒星及其周围天体，不是由大量恒星组成的星系", "The Solar System is one star and the bodies around it, not a huge collection of stars"),
                     ("太阳系比任何星系都大", "The Solar System is larger than any galaxy"),
                     ("星系比一颗行星还小", "A galaxy is smaller than one planet"),
                     ("这两个词永远可以互换", "The two words can always be swapped"))),
]
add(lesson("physics-8ES-s02","星系","Galaxies",
"本节你将学会说明什么是星系，并指出太阳系在银河系中的位置。",
"You will learn what a galaxy is, and where the Solar System sits in the Milky Way.",
r"""- **星系**是由大量恒星以及气体、尘埃等组成的巨大系统。
- 我们的太阳和地球位于**银河系**。
- 宇宙中有极多星系，银河系只是其中之一。
- 尺度：星系 ≫ 恒星系统（如太阳系）≫ 行星。
- 夜空中的“银河”光带，是从内部看银河系盘中大量恒星的光。""",
r"""- A **galaxy** is a huge system of many stars, together with gas and dust.
- Our Sun and Earth lie in the **Milky Way**.
- The Universe contains a great many galaxies; the Milky Way is only one of them.
- Scale: a galaxy ≫ a star system (such as the Solar System) ≫ a planet.
- The milky band in a dark sky is the combined light of many stars in the disc, seen from inside the Milky Way.""",
r"""第 8 阶段要求认识星系。把太阳系想象成“一条街上的一户人家”，银河系则是一座巨大的城市，里面有极其多的恒星。宇宙中还有许多这样的“城市”。

太阳带着地球和其他行星，一起位于银河系中。我们在晴朗、少光污染的夜晚看到的淡淡光带，就是侧向看去时众多遥远恒星的光。

## 例题

有人说“太阳系是一个星系”。这不正确：太阳系只有一颗恒星（太阳）及其行星、卫星、小行星等；星系则包含大量恒星。正确的说法是：太阳系位于银河系中。""",
r"""Stage 8 asks you to know what a galaxy is. If the Solar System is like one house on a street, a galaxy is a vast city with a huge number of stars. The Universe contains many such “cities”.

The Sun, with Earth and the other planets, lies in the Milky Way. The faint band visible on a dark, clear night is the light of many distant stars, seen looking through the disc from the inside.

## Worked example

Someone says “the Solar System is a galaxy”. That is incorrect: the Solar System is one star (the Sun) plus its planets, moons, asteroids and so on; a galaxy contains a vast number of stars. The correct statement is that the Solar System lies in the Milky Way.""",
r"""- **把太阳系叫成星系。** 二者尺度差极远。
- **以为银河系是宇宙中唯一的星系。** 还有极多其他星系。
- **搞反大小顺序。** 行星属于恒星系统，恒星系统属于星系。""",
r"""- **Calling the Solar System a galaxy.** The scales are completely different.
- **Thinking the Milky Way is the only galaxy.** There are a great many others.
- **Reversing the size order.** Planets belong to a star system; star systems belong to a galaxy.""",
[q["id"] for q in qs], diagram=D_GALAXY))
questions += qs

# ----- 8ES.s03 asteroids -----
qs = [
    PQ("q-ph-es03-01","physics-8ES-s03","mcq",
       "小行星通常是？",
       "An asteroid is usually:",
       "b", "小行星是太阳系中较小的岩石（或金属）天体，大多绕太阳运行，比行星小得多。",
       "An asteroid is a relatively small rocky (or metallic) body in the Solar System, usually orbiting the Sun, much smaller than a planet.",
       options=_opts(("和木星一样大的气体行星", "a gas planet as large as Jupiter"),
                     ("比行星小得多的岩石或金属天体", "a rocky or metallic body much smaller than a planet"),
                     ("一颗恒星", "a star"),
                     ("地球磁场的碎片", "a fragment of the Earth’s magnetic field"))),
    PQ("q-ph-es03-02","physics-8ES-s03","mcq",
       "太阳系中许多小行星主要分布在？",
       "Many asteroids in the Solar System are found mainly:",
       "c", "大量小行星位于火星与木星之间的小行星带。也有其他轨道，但本阶段先记住主小行星带。",
       "A large number lie in the asteroid belt between Mars and Jupiter. There are other orbits too, but at this stage start with the main belt.",
       options=_opts(("太阳内部", "inside the Sun"),
                     ("银河系以外很远、与太阳系无关的地方", "far outside the Milky Way, unrelated to the Solar System"),
                     ("火星与木星之间的小行星带", "in the asteroid belt between Mars and Jupiter"),
                     ("只能在地球大气层中", "only in Earth’s atmosphere"))),
    PQ("q-ph-es03-03","physics-8ES-s03","mcq",
       "小行星与行星相比，一个主要差别是？",
       "Compared with a planet, a main difference is that an asteroid is typically:",
       "a", "小行星质量、体积小得多，通常没有清理轨道，也不能像大行星那样用自身引力塑成稳定的近球形（有的近球形但仍远小于行星）。",
       "Asteroids are much smaller in mass and size, and they have not generally cleared their orbits. They are not large planets, even if a few are roughly rounded.",
       options=_opts(("小得多", "much smaller"),
                     ("一定比任何行星都大", "always larger than any planet"),
                     ("自己能发光，像恒星一样", "able to shine by itself, like a star"),
                     ("不是太阳系的成员", "not a member of the Solar System"))),
    PQ("q-ph-es03-04","physics-8ES-s03","short",
       "主小行星带大致位于哪两颗行星之间？",
       "Between which two planets does the main asteroid belt roughly lie?",
       "Mars and Jupiter", "火星与木星之间。",
       "Between Mars and Jupiter.",
       accepted=["Mars and Jupiter","Jupiter and Mars","mars and jupiter","火星和木星","火星与木星","木星和火星"]),
    PQ("q-ph-es03-05","physics-8ES-s03","mcq",
       "小行星绕什么运行（主小行星带中的大多数）？",
       "What do most asteroids in the main belt orbit?",
       "d", "它们是太阳系的成员，大多数绕太阳运行。",
       "They are members of the Solar System, and most of them orbit the Sun.",
       options=_opts(("只绕银河系中心，绝不绕太阳", "only the centre of the Milky Way, never the Sun"),
                     ("只绕地球", "only the Earth"),
                     ("只绕北极星", "only the Pole Star"),
                     ("太阳", "the Sun"))),
    PQ("q-ph-es03-06","physics-8ES-s03","mcq",
       "偶尔有小行星的轨道靠近地球。对此较合理的认识是？",
       "Some asteroids have orbits that come near the Earth. A reasonable view is that:",
       "b", "近地小行星值得监测，极少数可能带来撞击风险，但不必把每一颗小行星都想象成即将撞上地球。",
       "Near-Earth asteroids are worth monitoring; a very small number could pose an impact risk, but it is not true that every asteroid is about to hit the Earth.",
       options=_opts(("每一颗小行星都必定在明天撞击地球", "every asteroid will certainly hit the Earth tomorrow"),
                     ("少数轨道靠近地球的天体需要监测，但不是所有小行星都会撞击地球", "a few bodies that pass near Earth are monitored; not every asteroid will hit the Earth"),
                     ("小行星不可能有轨道", "asteroids cannot have orbits"),
                     ("小行星都在太阳内部，无法靠近地球", "all asteroids are inside the Sun, so they cannot approach Earth"))),
    PQ("q-ph-es03-07","physics-8ES-s03","mcq",
       "小行星与星系的关系，正确的是？",
       "Which statement about asteroids and galaxies is correct?",
       "a", "小行星是太阳系内的小天体；太阳系又位于银河系中。不要把小行星说成一个星系。",
       "Asteroids are small bodies in the Solar System; the Solar System itself lies in the Milky Way. An asteroid is not a galaxy.",
       options=_opts(("小行星属于太阳系，太阳系又在星系（银河系）中", "Asteroids belong to the Solar System, which itself lies in a galaxy (the Milky Way)"),
                     ("每颗小行星都是一个独立的星系", "Each asteroid is a separate galaxy"),
                     ("星系比小行星小", "A galaxy is smaller than an asteroid"),
                     ("小行星与太阳系、星系都无关", "Asteroids are unrelated to the Solar System and to galaxies"))),
]
add(lesson("physics-8ES-s03","小行星","Asteroids",
"本节你将学会说明小行星是什么、它们大致在哪里，并区分小行星与行星、星系。",
"You will learn what asteroids are, where many of them are found, and how they differ from planets and from galaxies.",
r"""- **小行星**是太阳系中较小的岩石或金属天体，大多绕太阳运行。
- 许多小行星位于**火星与木星之间的小行星带**。
- 它们比行星小得多。
- 少数轨道靠近地球的天体需要监测，但不是每一颗都会撞击地球。
- 小行星属于太阳系；太阳系又位于银河系中。""",
r"""- An **asteroid** is a relatively small rocky or metallic body in the Solar System, usually orbiting the Sun.
- Many lie in the **asteroid belt between Mars and Jupiter**.
- They are much smaller than planets.
- A few near-Earth objects are monitored, but not every asteroid is going to hit the Earth.
- Asteroids belong to the Solar System, which itself lies in the Milky Way.""",
r"""第 8 阶段要求认识小行星。它们是环绕太阳的较小天体，质量远小于行星。主小行星带位于火星与木星之间，像一条由许多石质或金属残块组成的环带——但远不是一块实心的大圆环。

有的小行星轨道会靠近地球，科学家会监测这些近地天体。把“存在小行星”理解成“明天一定撞上地球”是不准确的。

## 例题

有人把小行星说成“迷你星系”，或把小行星带说成“在银河系以外”。正确关系是：小行星在太阳系内，太阳系在银河系内。""",
r"""Stage 8 asks you to know what asteroids are. They are relatively small bodies orbiting the Sun, much less massive than planets. The main asteroid belt lies between Mars and Jupiter — a zone of many rocky or metallic bodies, not a solid ring.

Some asteroids follow paths that come near the Earth, and these near-Earth objects are monitored. It is not accurate to treat “asteroids exist” as “one will certainly hit the Earth tomorrow”.

## Worked example

Someone calls an asteroid a “mini galaxy”, or places the asteroid belt “outside the Milky Way”. The correct relationship is: asteroids are in the Solar System, and the Solar System is in the Milky Way.""",
r"""- **把小行星当成行星或恒星。** 它们小得多，自己不发光。
- **记错小行星带的位置。** 主带在火星与木星之间。
- **把小行星与星系混为一谈。** 尺度完全不同。""",
r"""- **Treating an asteroid as a planet or a star.** They are much smaller, and they do not shine by themselves.
- **Misplacing the asteroid belt.** The main belt is between Mars and Jupiter.
- **Mixing asteroids up with galaxies.** The scales are completely different.""",
[q["id"] for q in qs], diagram=D_ASTEROID))
questions += qs

# ========== Chapter practice and papers (original questions, not copies) ==========

def CQ(qid, section_id, typ, stem_zh, stem_en, answer, exp_zh, exp_en, **kw):
    return PQ(qid, section_id, typ, stem_zh, stem_en, answer, exp_zh, exp_en, **kw)

# ----- 8Pf 本章练习 -----
pf_prac = [
    CQ("q-ph-pf-pr01","physics-8Pf-s01","numeric",
       r"一列火车以 $25\ \text{m/s}$ 匀速行驶 $3$ 分钟。路程是多少米？",
       r"A train travels at a steady $25\ \text{m/s}$ for $3$ minutes. How far does it go, in metres?",
       "4500", r"$t=3\times 60=180\ \text{s}$，$s=25\times 180=4500\ \text{m}$。",
       r"$t=3\times 60=180\ \text{s}$, $s=25\times 180=4500\ \text{m}$.", tolerance=0),
    CQ("q-ph-pf-pr02","physics-8Pf-s01","numeric",
       r"把 $54\ \text{km/h}$ 换算成 $\text{m/s}$。",
       r"Convert $54\ \text{km/h}$ into $\text{m/s}$.",
       "15", r"$54\div 3.6=15\ \text{m/s}$。", r"$54\div 3.6=15\ \text{m/s}$.", tolerance=0.01),
    CQ("q-ph-pf-pr03","physics-8Pf-s02","mcq",
       "路程—时间图像上一段水平线表示物体？",
       "A horizontal section on a distance–time graph means the object is:",
       "c", "路程不变，速度为零，物体静止。斜率才是速度，不是加速度。",
       "Distance is not changing, so the speed is zero and the object is stationary. The gradient is speed, not acceleration.",
       options=_opts(("正在加速", "accelerating"),
                     ("以很大的恒定速度运动", "moving at a large constant speed"),
                     ("静止", "stationary"),
                     ("加速度等于这段的斜率", "has acceleration equal to the gradient"))),
    CQ("q-ph-pf-pr04","physics-8Pf-s03","numeric",
       r"向右 $18\ \text{N}$、向左 $7\ \text{N}$。合力大小是多少牛顿？",
       r"Forces of $18\ \text{N}$ right and $7\ \text{N}$ left. What is the size of the resultant, in newtons?",
       "11", r"$18-7=11\ \text{N}$，方向向右。力是非平衡的。",
       r"$18-7=11\ \text{N}$ to the right. The forces are unbalanced.", tolerance=0),
    CQ("q-ph-pf-pr05","physics-8Pf-s03","mcq",
       "物体沿直线做匀速运动，作用在它上面的力？",
       "An object moves in a straight line at constant speed. The forces on it are:",
       "a", "匀速直线运动与静止一样，合力为零，力是平衡的。",
       "Steady straight-line motion, like rest, means a zero resultant: the forces are balanced.",
       options=_opts(("平衡的（合力为零）", "balanced (resultant zero)"),
                     ("一定非平衡，否则它会停下", "must be unbalanced, otherwise it would stop"),
                     ("不存在，因为运动中不能有力", "absent, because a moving object cannot have forces"),
                     ("只能向下", "only downward"))),
    CQ("q-ph-pf-pr06","physics-8Pf-s04","numeric",
       r"力 $8\ \text{N}$，垂直力臂 $1.5\ \text{m}$。力矩是多少 $\text{N\,m}$？",
       r"A force of $8\ \text{N}$ has a perpendicular distance of $1.5\ \text{m}$. What is the moment in $\text{N\,m}$?",
       "12", r"$M=8\times 1.5=12\ \text{N\,m}$。必须用垂直距离。",
       r"$M=8\times 1.5=12\ \text{N\,m}$. The distance must be perpendicular.", tolerance=0.01),
    CQ("q-ph-pf-pr07","physics-8Pf-s05","numeric",
       r"$60\ \text{N}$ 的力作用在 $0.3\ \text{m}^2$ 上。压强是多少 $\text{N/m}^2$？",
       r"A $60\ \text{N}$ force acts on $0.3\ \text{m}^2$. What is the pressure in $\text{N/m}^2$?",
       "200", r"$p=F/A=60/0.3=200\ \text{N/m}^2$。", r"$p=F/A=60/0.3=200\ \text{N/m}^2$.", tolerance=0.01),
    CQ("q-ph-pf-pr08","physics-8Pf-s07","mcq",
       "气体中的扩散通常比液体中更快，主要是因为气体粒子？",
       "Diffusion is usually faster in a gas than in a liquid mainly because gas particles:",
       "b", "气体粒子间距更大、运动更自由。扩散来自粒子自身的无规则运动，不必搅拌。",
       "Gas particles are more widely spaced and move more freely. Diffusion comes from the particles’ own random motion; stirring is not required.",
       options=_opts(("完全静止", "are completely still"),
                     ("间距更大、运动更自由", "are more widely spaced and move more freely"),
                     ("一定更重", "must be heavier"),
                     ("只能在真空中运动", "can move only in a vacuum"))),
]
questions += pf_prac
sets.append(pset("practice-physics-8Pf", "physics-8Pf", "practice",
                 "本章练习 · 力与能量", "Chapter practice · Forces and energy",
                 [q["id"] for q in pf_prac], minutes=15, published="2026-11-10T09:00:00+08:00"))

# ----- 8Pf 本章测试卷 (25 min, 12 q) -----
pf_paper = [
    CQ("q-ph-pf-pa01","physics-8Pf-s01","numeric",
       r"一名骑行者 $12\ \text{s}$ 内前进 $90\ \text{m}$。平均速度是多少 $\text{m/s}$？",
       r"A cyclist travels $90\ \text{m}$ in $12\ \text{s}$. What is the average speed in $\text{m/s}$?",
       "7.5", r"$v=90/12=7.5\ \text{m/s}$。", r"$v=90/12=7.5\ \text{m/s}$.", tolerance=0.05),
    CQ("q-ph-pf-pa02","physics-8Pf-s01","numeric",
       r"把 $18\ \text{m/s}$ 换算成 $\text{km/h}$。",
       r"Convert $18\ \text{m/s}$ into $\text{km/h}$.",
       "64.8", r"$18\times 3.6=64.8\ \text{km/h}$。", r"$18\times 3.6=64.8\ \text{km/h}$.", tolerance=0.05),
    CQ("q-ph-pf-pa03","physics-8Pf-s02","numeric",
       r"某段路程—时间图像中，路程从 $5\ \text{m}$ 均匀增到 $29\ \text{m}$，用时 $6\ \text{s}$。速度是多少 $\text{m/s}$？",
       r"On a distance–time graph, distance rises steadily from $5\ \text{m}$ to $29\ \text{m}$ in $6\ \text{s}$. What is the speed in $\text{m/s}$?",
       "4", r"要用变化量：$\Delta s=24\ \text{m}$，$v=24/6=4\ \text{m/s}$。不要用 $29/6$。",
       r"Use the change: $\Delta s=24\ \text{m}$, $v=24/6=4\ \text{m/s}$. Do not use $29/6$.", tolerance=0.01),
    CQ("q-ph-pf-pa04","physics-8Pf-s02","mcq",
       "路程—时间图像的斜率表示？",
       "The gradient of a distance–time graph represents:",
       "c", r"斜率是 $\Delta s/\Delta t$，即速度。加速度是速度—时间图像的斜率。",
       r"The gradient is $\Delta s/\Delta t$, which is speed. Acceleration is the gradient of a speed–time graph.",
       options=_opts(("加速度", "acceleration"),
                     ("力", "force"),
                     ("速度", "speed"),
                     ("压强", "pressure"))),
    CQ("q-ph-pf-pa05","physics-8Pf-s03","mcq",
       "书静放在桌上。正确的说法是？",
       "A book rests on a table. Which statement is correct?",
       "d", "静止说明合力为零：重力与支持力平衡，不是“不受力”。",
       "Being at rest means the resultant is zero: weight and the support force are balanced, not “no forces”.",
       options=_opts(("书不受任何力", "No forces act on the book"),
                     ("只有重力，所以书在加速下落", "Only weight acts, so the book is accelerating downwards"),
                     ("合力向上，书将会飞起", "The resultant is upwards, so the book will rise"),
                     ("重力与支持力平衡", "Weight and the support force are balanced"))),
    CQ("q-ph-pf-pa06","physics-8Pf-s03","mcq",
       "非平衡力可以？",
       "An unbalanced force can:",
       "a", "使物体加速、减速或改变方向。",
       "speed an object up, slow it down or change its direction.",
       options=_opts(("使物体加速、减速或改变方向", "speed an object up, slow it down or change its direction"),
                     ("只让物体永远保持静止", "only keep an object at rest forever"),
                     ("取消物体的质量", "cancel an object’s mass"),
                     ("不改变运动状态", "leave the motion unchanged"))),
    CQ("q-ph-pf-pa07","physics-8Pf-s04","numeric",
       r"要用 $5\ \text{N}$ 产生 $12\ \text{N\,m}$ 的力矩，垂直力臂应为多少米？",
       r"What perpendicular distance, in metres, is needed for a $5\ \text{N}$ force to give a moment of $12\ \text{N\,m}$?",
       "2.4", r"$d=M/F=12/5=2.4\ \text{m}$。", r"$d=M/F=12/5=2.4\ \text{m}$.", tolerance=0.01),
    CQ("q-ph-pf-pa08","physics-8Pf-s04","numeric",
       r"轻质杠杆左边 $15\ \text{N}$、力臂 $0.4\ \text{m}$。右边 $6\ \text{N}$ 使之平衡，力臂是多少米？",
       r"On the left of a light lever, $15\ \text{N}$ acts $0.4\ \text{m}$ from the pivot. A $6\ \text{N}$ force on the right keeps balance. How far from the pivot is it, in metres?",
       "1", r"$15\times 0.4=6\times d \Rightarrow d=1\ \text{m}$。平衡看的是力矩，不只是力相等。",
       r"$15\times 0.4=6\times d \Rightarrow d=1\ \text{m}$. Equilibrium is about moments, not only equal forces.", tolerance=0.01),
    CQ("q-ph-pf-pa09","physics-8Pf-s05","numeric",
       r"压强为 $40\ \text{N/m}^2$，面积 $1.5\ \text{m}^2$。力是多少牛顿？",
       r"The pressure is $40\ \text{N/m}^2$ on an area of $1.5\ \text{m}^2$. What is the force in newtons?",
       "60", r"$F=pA=40\times 1.5=60\ \text{N}$。", r"$F=pA=40\times 1.5=60\ \text{N}$.", tolerance=0),
    CQ("q-ph-pf-pa10","physics-8Pf-s05","mcq",
       "雪地靴不容易陷进雪里，主要是因为？",
       "Snowshoes are less likely to sink into snow mainly because they:",
       "b", "增大面积从而减小压强，人的重力几乎不变。",
       "increase the area and so reduce the pressure; the person’s weight is almost unchanged.",
       options=_opts(("使人的重力变小", "reduce the person’s weight"),
                     ("增大面积，减小压强", "increase the area and reduce the pressure"),
                     ("把雪的质量变为零", "make the mass of the snow zero"),
                     ("取消所有的力", "cancel all forces"))),
    CQ("q-ph-pf-pa11","physics-8Pf-s06","mcq",
       "体积相近时加热密闭气体，压强升高。粒子模型的解释是？",
       "Heating a closed gas at almost constant volume raises the pressure. In the particle model this is because particles:",
       "c", "运动更快，碰撞更频繁、更有力。压强来自各向碰撞，不只是“空气重量向下”。",
       "move faster, so collisions are more frequent and harder. Pressure comes from collisions in all directions, not only “the weight of air pushing down”.",
       options=_opts(("停止运动", "stop moving"),
                     ("从容器中全部消失", "all leave the container"),
                     ("运动更快，碰撞更频繁、更有力", "move faster, so collisions are more frequent and harder"),
                     ("变成液体并沉到器底", "become a liquid and sink to the bottom"))),
    CQ("q-ph-pf-pa12","physics-8Pf-s07","mcq",
       "不必搅拌，色素也会在水中慢慢散开。这主要是？",
       "A dye slowly spreads in still water with no stirring. This is mainly:",
       "a", "液体中的扩散：粒子不断无规则运动。搅拌会加快混合，但不是扩散发生的必要条件。",
       "diffusion in a liquid: particles move randomly. Stirring speeds mixing but is not required for diffusion.",
       options=_opts(("扩散", "diffusion"),
                     ("反射定律", "the law of reflection"),
                     ("力矩平衡", "moment equilibrium"),
                     ("电磁铁断电", "switching an electromagnet off"))),
]
questions += pf_paper
sets.append(pset("paper-physics-8Pf", "physics-8Pf", "paper",
                 "本章测试卷 · 力与能量", "Chapter test · Forces and energy",
                 [q["id"] for q in pf_paper], minutes=25, published="2026-11-10T09:00:00+08:00"))

# ----- 8Ps practice + paper -----
ps_prac = [
    CQ("q-ph-ps-pr01","physics-8Ps-s01","numeric",
       r"平面镜反射中，入射角为 $42^\circ$。反射角是多少度？",
       r"For reflection at a plane mirror, the angle of incidence is $42^\circ$. What is the angle of reflection, in degrees?",
       "42", r"$i=r$，反射角为 $42^\circ$。角从法线量起。",
       r"$i=r$, so the angle of reflection is $42^\circ$. Measure from the normal.", tolerance=0),
    CQ("q-ph-ps-pr02","physics-8Ps-s01","numeric",
       r"光线与镜面成 $25^\circ$。入射角是多少度？",
       r"A ray makes $25^\circ$ with the mirror surface. What is the angle of incidence, in degrees?",
       "65", r"入射角从法线量：$90^\circ-25^\circ=65^\circ$。",
       r"The angle of incidence is measured from the normal: $90^\circ-25^\circ=65^\circ$.", tolerance=0),
    CQ("q-ph-ps-pr03","physics-8Ps-s02","mcq",
       "光线从空气斜射入玻璃时，通常？",
       "A ray going from air into glass at an angle usually:",
       "b", "进入更光密介质，向法线偏折。不要画成 $i=r$。",
       "Entering a denser medium, it bends towards the normal. Do not draw this as $i=r$.",
       options=_opts(("远离法线", "bends away from the normal"),
                     ("向法线偏折", "bends towards the normal"),
                     ("反射角等于入射角后不再进入玻璃", "reflects with $i=r$ and never enters the glass"),
                     ("颜色立刻变成单一紫色", "instantly becomes only violet"))),
    CQ("q-ph-ps-pr04","physics-8Ps-s02","mcq",
       "光线从水斜射入空气时，通常？",
       "A ray going from water into air at an angle usually:",
       "a", "进入更光疏（更快）的介质，远离法线。",
       "Entering a less dense (faster) medium, it bends away from the normal.",
       options=_opts(("远离法线", "bends away from the normal"),
                     ("向法线偏折", "bends towards the normal"),
                     ("一定沿法线前进", "must travel along the normal"),
                     ("停止传播", "stops travelling"))),
    CQ("q-ph-ps-pr05","physics-8Ps-s03","mcq",
       "白光通过三棱镜色散后，偏折通常最大的可见光是？",
       "After a prism disperses white light, the visible colour usually bent most is:",
       "d", "紫光偏折最大，红光最小。棱镜是分开原已存在的色光，不是制造颜色。",
       "Violet is bent most, red least. The prism separates colours already in white light; it does not create them.",
       options=_opts(("红光", "red"),
                     ("只有黄光", "yellow only"),
                     ("所有颜色完全相同", "all colours equally"),
                     ("紫光", "violet"))),
    CQ("q-ph-ps-pr06","physics-8Ps-s03","short",
       "可见光谱中，哪一种色光通过棱镜时通常偏折最小？",
       "Which visible colour is usually bent the least by a prism?",
       "red", "红光偏折最小。", "Red is bent the least.",
       accepted=["red","red light","红","红光"]),
    CQ("q-ph-ps-pr07","physics-8Ps-s04","mcq",
       "红光与绿光适当叠加，通常得到？",
       "Red light and green light added suitably usually give:",
       "c", "色光加色：红+绿可得黄。不要用颜料混合的规则去套。",
       "Additive colour: red + green can give yellow. Do not use paint-mixing rules here.",
       options=_opts(("黑", "black"),
                     ("只有蓝", "blue only"),
                     ("黄", "yellow"),
                     ("磁场", "a magnetic field"))),
    CQ("q-ph-ps-pr08","physics-8Ps-s04","mcq",
       "白光照射只反射绿光、吸收其他可见光的物体，它看起来是？",
       "White light falls on an object that reflects only green and absorbs other visible colours. It looks:",
       "a", "进入眼睛的主要是被反射的绿光。",
       "Mainly the reflected green light reaches the eye.",
       options=_opts(("绿色", "green"),
                     ("白色，因为入射光是白的", "white, because the incoming light is white"),
                     ("一定是黑色，因为有光被吸收", "black for sure, because some light is absorbed"),
                     ("没有颜色且物体消失", "colourless, and the object vanishes"))),
]
questions += ps_prac
sets.append(pset("practice-physics-8Ps", "physics-8Ps", "practice",
                 "本章练习 · 光与声（本阶段为光）", "Chapter practice · Light and sound (light at this stage)",
                 [q["id"] for q in ps_prac], minutes=15, published="2026-11-08T09:00:00+08:00"))

ps_paper = [
    CQ("q-ph-ps-pa01","physics-8Ps-s01","short",
       "写出平面镜的反射定律（可写 $i=r$ 并说明从哪量角）。",
       "State the law of reflection at a plane surface (you may write $i=r$ and say how the angles are measured).",
       "i=r", "入射角等于反射角，二者都从法线量起；入射光线、法线、反射光线共面。",
       "The angle of incidence equals the angle of reflection, both measured from the normal; the incident ray, normal and reflected ray are coplanar.",
       accepted=["i=r","i = r","angle of incidence equals angle of reflection","入射角等于反射角","入射角＝反射角"]),
    CQ("q-ph-ps-pa02","physics-8Ps-s01","numeric",
       r"入射角为 $28^\circ$。反射角是多少度？",
       r"The angle of incidence is $28^\circ$. What is the angle of reflection, in degrees?",
       "28", r"$i=r=28^\circ$。", r"$i=r=28^\circ$.", tolerance=0),
    CQ("q-ph-ps-pa03","physics-8Ps-s01","numeric",
       r"光线与镜面成 $40^\circ$。反射角是多少度？",
       r"A ray makes $40^\circ$ with the mirror. What is the angle of reflection, in degrees?",
       "50", r"入射角 $=90^\circ-40^\circ=50^\circ$，故反射角也是 $50^\circ$。",
       r"Angle of incidence $=90^\circ-40^\circ=50^\circ$, so the angle of reflection is also $50^\circ$.", tolerance=0),
    CQ("q-ph-ps-pa04","physics-8Ps-s01","mcq",
       "入射角、反射角必须从哪一条线量起？",
       "The angles of incidence and reflection must be measured from:",
       "b", "法线，不是镜面。", "the normal, not the mirror surface.",
       options=_opts(("镜面", "the mirror surface"),
                     ("法线", "the normal"),
                     ("光源到眼睛的连线", "the line from the lamp to the eye"),
                     ("任意一条平行线", "any convenient parallel line"))),
    CQ("q-ph-ps-pa05","physics-8Ps-s02","mcq",
       "光线从空气斜射入水面，通常会？",
       "A ray going from air into water at an angle usually:",
       "c", "进入更光密介质，向法线偏折。空气—水与空气—玻璃规则相同。",
       "Entering a denser medium, it bends towards the normal. The same rule holds for air–water and air–glass.",
       options=_opts(("远离法线", "bends away from the normal"),
                     ("不进入水中", "does not enter the water"),
                     ("向法线偏折", "bends towards the normal"),
                     ("变成声波", "becomes a sound wave"))),
    CQ("q-ph-ps-pa06","physics-8Ps-s02","short",
       "光线沿法线从空气进入玻璃，方向会怎样？",
       "A ray travels from air into glass along the normal. What happens to its direction?",
       "no bending", "不偏折，方向不变（在玻璃中会变慢）。",
       "No bending: the direction stays the same (though the light slows in the glass).",
       accepted=["no bending","does not bend","straight on","no change of direction","不偏折","不改变方向","沿直线","goes straight"]),
    CQ("q-ph-ps-pa07","physics-8Ps-s02","mcq",
       "池底看起来比实际浅，一个原因是？",
       "A pool can look shallower than it is. One reason is:",
       "a", "从水中射出的光线在水面远离法线，沿直线追迹会觉得池底被抬高。",
       "Rays leaving the water bend away from the normal; tracing them back in straight lines raises the apparent bottom.",
       options=_opts(("水中射出的光线远离法线，池底的像被抬高", "rays leaving the water bend away from the normal, raising the image of the bottom"),
                     ("水把所有光反射回太阳", "the water reflects all light back to the Sun"),
                     ("反射定律不再成立", "the law of reflection has failed"),
                     ("这只与小行星有关", "it is only to do with asteroids"))),
    CQ("q-ph-ps-pa08","physics-8Ps-s03","mcq",
       "白光色散说明白光？",
       "Dispersion of white light shows that white light:",
       "d", "由多种色光组成。棱镜将它们分开，而不是制造新颜色。",
       "is a mixture of colours. The prism separates them; it does not create new colours.",
       options=_opts(("是单一颜色，颜色由棱镜制造", "is a single colour, and the prism creates the others"),
                     ("不能通过玻璃", "cannot pass through glass"),
                     ("与扩散是同一过程", "is the same process as diffusion"),
                     ("由多种色光组成", "is made up of a range of colours"))),
    CQ("q-ph-ps-pa09","physics-8Ps-s03","mcq",
       "棱镜光谱中，红光与紫光相比通常？",
       "In a prism spectrum, red light compared with violet is usually:",
       "b", "红光偏折较小。", "bent less than violet.",
       options=_opts(("偏折更大", "bent more"),
                     ("偏折更小", "bent less"),
                     ("完全不通过棱镜", "does not pass through the prism at all"),
                     ("总是与紫光重合", "always overlaps violet exactly"))),
    CQ("q-ph-ps-pa10","physics-8Ps-s04","mcq",
       "红、绿、蓝三束色光适当叠加可以得到？",
       "Red, green and blue light added suitably can give:",
       "a", "加色三原色会合可得白光。", "the additive primaries can combine to give white light.",
       options=_opts(("白光", "white light"),
                     ("只能得到黑", "black only"),
                     ("真空", "a vacuum"),
                     ("地磁场", "the Earth’s magnetic field"))),
    CQ("q-ph-ps-pa11","physics-8Ps-s04","mcq",
       "只用蓝光照射一块只能反射红光（吸收蓝光）的物体，它看起来最可能？",
       "Blue light alone falls on an object that can reflect only red (and absorbs blue). It is most likely to look:",
       "c", "没有可反射的红光，蓝光又被吸收，看起来很暗或接近黑色。颜色与照明有关。",
       "There is no red to reflect and the blue is absorbed, so it looks very dark or nearly black. Colour depends on the lighting.",
       options=_opts(("明亮的红色", "bright red"),
                     ("明亮的白色", "bright white"),
                     ("很暗或接近黑色", "very dark or nearly black"),
                     ("绿色", "green"))),
]
questions += ps_paper
sets.append(pset("paper-physics-8Ps", "physics-8Ps", "paper",
                 "本章测试卷 · 光与声（本阶段为光）", "Chapter test · Light and sound (light at this stage)",
                 [q["id"] for q in ps_paper], minutes=25, published="2026-11-08T09:00:00+08:00"))

# ----- 8Pe practice + paper -----
pe_prac = [
    CQ("q-ph-pe-pr01","physics-8Pe-s01","mcq",
       "条形磁体外部的磁感线通常？",
       "Field lines outside a bar magnet usually:",
       "a", "从 N 极出发回到 S 极。线条是模型，不是真实绳子；越密表示越强。",
       "leave the N pole and return to the S pole. The lines are a model, not real strings; closer lines mean a stronger field.",
       options=_opts(("从 N 极出发，回到 S 极", "leave N and return to S"),
                     ("从 S 极出发，回到 N 极", "leave S and return to N"),
                     ("没有方向", "have no direction"),
                     ("只存在于磁体内部", "exist only inside the magnet"))),
    CQ("q-ph-pe-pr02","physics-8Pe-s01","mcq",
       "磁感线画得更密的地方，磁场通常？",
       "Where field lines are closer together, the field is usually:",
       "c", "更强，例如靠近磁极处。", "stronger, for example near the poles.",
       options=_opts(("更弱", "weaker"),
                     ("为零", "zero"),
                     ("更强", "stronger"),
                     ("与疏密无关", "unrelated to spacing"))),
    CQ("q-ph-pe-pr03","physics-8Pe-s01","short",
       "用什么简单仪器可以显示磁场的方向？",
       "What simple instrument can show the direction of a magnetic field?",
       "compass", "小磁针（指南针）。", "A plotting compass.",
       accepted=["compass","plotting compass","a compass","磁针","小磁针","指南针"]),
    CQ("q-ph-pe-pr04","physics-8Pe-s02","mcq",
       "电磁铁的一个重要优点是？",
       "An important advantage of an electromagnet is that it:",
       "b", "可以通过通断电来开关磁性，便于放下工件。",
       "can be switched on and off with the current, so a load can be dropped.",
       options=_opts(("永远无法关断", "can never be switched off"),
                     ("可以通断电来开关", "can be switched on and off with the current"),
                     ("不需要线圈", "needs no coil"),
                     ("只能用于色散", "can only be used for dispersion"))),
    CQ("q-ph-pe-pr05","physics-8Pe-s02","mcq",
       "断开电流后，电磁铁通常会？",
       "When the current is switched off, an electromagnet usually:",
       "d", "磁性大大减弱或消失，可以放下被吸住的铁质物体。",
       "lose most or all of its magnetism, so a lifted iron object can be released.",
       options=_opts(("变得更强且无法放下工件", "become stronger and unable to release a load"),
                     ("变成棱镜", "turn into a prism"),
                     ("质量变为零", "have zero mass"),
                     ("磁性减弱或消失，可放下工件", "lose magnetism and can drop a load"))),
    CQ("q-ph-pe-pr06","physics-8Pe-s03","mcq",
       "其他条件相近时，增加匝数通常使电磁铁？",
       "If other conditions are similar, more turns usually make an electromagnet:",
       "a", "更强。电流增大、加上铁芯也会增强。比较时一次只改一个因素。",
       "stronger. A larger current or an iron core also helps. Change one factor at a time in a fair test.",
       options=_opts(("更强", "stronger"),
                     ("一定更弱", "always weaker"),
                     ("不再需要电流", "no longer need a current"),
                     ("与匝数无关", "independent of turns"))),
    CQ("q-ph-pe-pr07","physics-8Pe-s03","short",
       "列出两个能使电磁铁更强的因素。",
       "Name two factors that can make an electromagnet stronger.",
       "current and turns", "更大电流、更多匝数、加上铁芯，答出两个即可。",
       "A larger current, more turns, or an iron core — any two.",
       accepted=["current and turns","current, turns","current and core","turns and core","电流和匝数","电流与匝数","电流和铁芯","匝数和铁芯","更大电流，更多匝数"]),
    CQ("q-ph-pe-pr08","physics-8Pe-s03","mcq",
       "比较匝数的影响时，公平实验应？",
       "In a fair test of the number of turns you should:",
       "b", "只改变匝数，控制电流、铁芯等其他变量。",
       "change only the number of turns and control current, core and other variables.",
       options=_opts(("同时随意改电流和铁芯", "also change current and core at random"),
                     ("只改变匝数，控制其他变量", "change only the turns and control other variables"),
                     ("不必记录结果", "not record any results"),
                     ("拿走所有导线", "remove all the wire"))),
]
questions += pe_prac
sets.append(pset("practice-physics-8Pe", "physics-8Pe", "practice",
                 "本章练习 · 电与磁", "Chapter practice · Electricity and magnetism",
                 [q["id"] for q in pe_prac], minutes=12, published="2026-11-07T09:00:00+08:00"))

pe_paper = [
    CQ("q-ph-pe-pa01","physics-8Pe-s01","mcq",
       "磁场是？",
       "A magnetic field is:",
       "c", "磁体周围有磁力作用的空间。",
       "the region around a magnet where magnetic forces act.",
       options=_opts(("一种可见的绳子", "a visible string"),
                     ("只有声音才能通过的区域", "a region that only sound can pass through"),
                     ("磁体周围有磁力作用的空间", "the region around a magnet where magnetic forces act"),
                     ("电流的单位", "the unit of current"))),
    CQ("q-ph-pe-pa02","physics-8Pe-s01","mcq",
       "两个磁极靠近时？",
       "When two magnetic poles are brought close:",
       "a", "同名相斥，异名相吸。", "like poles repel and unlike poles attract.",
       options=_opts(("同名相斥，异名相吸", "like poles repel and unlike attract"),
                     ("同名相吸，异名相斥", "like poles attract and unlike repel"),
                     ("没有任何力", "there is never a force"),
                     ("只有重力起作用", "only gravity acts"))),
    CQ("q-ph-pe-pa03","physics-8Pe-s01","mcq",
       "小磁针的 N 极指向该处磁场的？",
       "The N pole of a plotting compass points in the direction of:",
       "b", "该点磁场的方向（磁体外磁感线从 N 到 S）。",
       "the field at that point (outside a magnet, lines run from N to S).",
       options=_opts(("重力方向", "the weight"),
                     ("该点磁场的方向", "the magnetic field at that point"),
                     ("声波传播方向", "the direction of a sound wave"),
                     ("任意随机方向，没有规则", "a random direction with no rule"))),
    CQ("q-ph-pe-pa04","physics-8Pe-s01","mcq",
       "磁感线是？",
       "Magnetic field lines are:",
       "d", "描述方向和相对强弱的图示模型，不是实物。",
       "a diagram model for direction and relative strength, not real objects.",
       options=_opts(("可以捡起来的铁丝", "iron wires you can pick up"),
                     ("只在水中出现", "found only in water"),
                     ("电流本身", "the current itself"),
                     ("表示方向和强弱的模型图线", "model lines showing direction and strength"))),
    CQ("q-ph-pe-pa05","physics-8Pe-s02","mcq",
       "最简单的电磁铁通常包括？",
       "The simplest electromagnet usually includes:",
       "a", "绕在铁芯上的绝缘线圈，并通以电流。",
       "an insulated coil on an iron core, with a current in the coil.",
       options=_opts(("铁芯、绝缘线圈和电流", "an iron core, an insulated coil and a current"),
                     ("只有一块不能关断的永磁体", "only a permanent magnet that cannot be switched off"),
                     ("一块玻璃棱镜", "a glass prism"),
                     ("一根干燥的木棒", "a dry wooden rod"))),
    CQ("q-ph-pe-pa06","physics-8Pe-s02","mcq",
       "铁芯的主要作用是？",
       "The main job of the iron core is to:",
       "c", "增强并集中磁场。常用软铁，以便断电后迅速退磁。",
       "strengthen and concentrate the field. Soft iron is used so that it demagnetises quickly when the current stops.",
       options=_opts(("阻止电流", "stop the current"),
                     ("产生色散", "produce dispersion"),
                     ("增强并集中磁场", "strengthen and concentrate the field"),
                     ("让线圈短路", "short the coil"))),
    CQ("q-ph-pe-pa07","physics-8Pe-s02","mcq",
       "电磁铁可用于？",
       "Electromagnets can be used in:",
       "b", "起重、电铃、继电器等需要可开关磁性的装置。",
       "lifting magnets, bells, relays and other devices that need switchable magnetism.",
       options=_opts(("代替所有平面镜", "replacing every plane mirror"),
                     ("可开关的起重、电铃、继电器等", "switchable lifting, bells and relays"),
                     ("在真空中传播声音", "sending sound through a vacuum"),
                     ("测量星系的质量（本课范围）", "measuring galaxy masses (at this stage)"))),
    CQ("q-ph-pe-pa08","physics-8Pe-s03","mcq",
       "其他条件相近时，增大电流通常使电磁铁？",
       "If other conditions are similar, a larger current usually makes an electromagnet:",
       "d", "更强。但电流过大导致过热会既不安全也不再公平。",
       "stronger. A current so large that the wire overheats is unsafe and may spoil a fair test.",
       options=_opts(("更弱", "weaker"),
                     ("与电流无关", "independent of current"),
                     ("失去铁芯", "lose its core"),
                     ("更强", "stronger"))),
    CQ("q-ph-pe-pa09","physics-8Pe-s03","mcq",
       "有铁芯的线圈与空心线圈相比（其他条件相近）通常？",
       "A coil with an iron core, compared with an air-cored coil (other conditions similar), is usually:",
       "a", "更强。", "stronger.",
       options=_opts(("更强", "stronger"),
                     ("更弱", "weaker"),
                     ("完全一样", "identical"),
                     ("不能吸起任何铁质物体", "unable to attract any iron"))),
    CQ("q-ph-pe-pa10","physics-8Pe-s03","mcq",
       "电流过大、导线明显发热时，主要问题是？",
       "If a very large current makes the wire heat up badly, a main problem is:",
       "b", "不安全，且可能改变电阻、损坏绝缘，实验不再公平。",
       "it can be unsafe, and it may change the resistance or damage insulation, so the test is no longer fair.",
       options=_opts(("发热证明电磁铁一定变弱", "heating proves the electromagnet must be weaker"),
                     ("不安全，实验也可能不再公平", "it may be unsafe, and the test may no longer be fair"),
                     ("发热完全有益，应继续加大电流", "heating is entirely helpful, so increase the current further"),
                     ("这时应浇水并继续通大电流", "pour water on it and keep a large current flowing"))),
    CQ("q-ph-pe-pa11","physics-8Pe-s02","short",
       "为什么电磁铁的线圈常用绝缘导线？",
       "Why is the wire of an electromagnet usually insulated?",
       "short circuit", "防止相邻圈短路，电流才能一圈圈绕过铁芯。",
       "To prevent neighbouring turns shorting, so the current can travel around the core turn by turn.",
       accepted=["short circuit","prevent a short","insulation prevents shorting","avoid short","防短路","防止短路","避免短路","绝缘防短路","so turns do not short"]),
]
questions += pe_paper
sets.append(pset("paper-physics-8Pe", "physics-8Pe", "paper",
                 "本章测试卷 · 电与磁", "Chapter test · Electricity and magnetism",
                 [q["id"] for q in pe_paper], minutes=20, published="2026-11-07T09:00:00+08:00"))

# ----- 8ES practice + paper -----
es_prac = [
    CQ("q-ph-es-pr01","physics-8ES-s01","mcq",
       "指南针能指示南北，主要是因为？",
       "A compass shows north–south mainly because:",
       "b", "小磁针在地球磁场中转向。",
       "the needle is a small magnet that turns in the Earth’s magnetic field.",
       options=_opts(("指针内部有发动机", "there is a motor inside the needle"),
                     ("地球磁场使磁针转向", "the Earth’s magnetic field turns the needle"),
                     ("阳光把指针推向南方", "sunlight pushes the needle south"),
                     ("它只随风摆动", "it only swings with the wind"))),
    CQ("q-ph-es-pr02","physics-8ES-s01","mcq",
       "地理北极附近，在“地球像条形磁体”的模型中相当于？",
       "In the bar-magnet model of the Earth, the region near geographic north behaves as:",
       "c", "地磁 S 极，因为指南针 N 极被吸向那边。",
       "a magnetic S pole, because a compass N pole is attracted there.",
       options=_opts(("地磁 N 极，只因名称里有“北”", "a magnetic N pole, only because it is called north"),
                     ("没有磁极", "no magnetic pole"),
                     ("地磁 S 极", "a magnetic S pole"),
                     ("一个电场中心", "an electric-field centre"))),
    CQ("q-ph-es-pr03","physics-8ES-s01","short",
       "指南针的 N 极大致指向什么方向？",
       "Roughly which way does a compass N pole point?",
       "north", "大致指向地理北方或磁北。", "Roughly geographic north, or magnetic north.",
       accepted=["north","magnetic north","geographic north","北","北方","磁北","地理北"]),
    CQ("q-ph-es-pr04","physics-8ES-s02","mcq",
       "太阳系位于哪个星系？",
       "The Solar System lies in which galaxy?",
       "a", "银河系。太阳系本身不是一个星系。",
       "the Milky Way. The Solar System itself is not a galaxy.",
       options=_opts(("银河系", "the Milky Way"),
                     ("它自己就是一个星系", "it is a galaxy by itself"),
                     ("月球", "the Moon"),
                     ("不在任何星系中", "it lies in no galaxy"))),
    CQ("q-ph-es-pr05","physics-8ES-s02","mcq",
       "星系是？",
       "A galaxy is:",
       "d", "由大量恒星、气体和尘埃组成的巨大系统。",
       "a huge system of many stars, gas and dust.",
       options=_opts(("一颗单独的行星", "a single planet"),
                     ("一块小岩石", "a small rock"),
                     ("地球大气", "Earth’s atmosphere"),
                     ("由大量恒星、气体和尘埃组成的巨大系统", "a huge system of many stars, gas and dust"))),
    CQ("q-ph-es-pr06","physics-8ES-s03","mcq",
       "许多小行星主要分布在？",
       "Many asteroids are found mainly:",
       "b", "火星与木星之间的小行星带。它们绕太阳运行，比行星小得多。",
       "in the asteroid belt between Mars and Jupiter. They orbit the Sun and are much smaller than planets.",
       options=_opts(("太阳内部", "inside the Sun"),
                     ("火星与木星之间的小行星带", "in the asteroid belt between Mars and Jupiter"),
                     ("银河系以外且与太阳系无关", "outside the Milky Way, unrelated to the Solar System"),
                     ("只能在地球大气中", "only in Earth’s atmosphere"))),
    CQ("q-ph-es-pr07","physics-8ES-s03","short",
       "主小行星带大致位于哪两颗行星之间？",
       "Between which two planets does the main asteroid belt lie?",
       "Mars and Jupiter", "火星与木星之间。", "Between Mars and Jupiter.",
       accepted=["Mars and Jupiter","Jupiter and Mars","mars and jupiter","火星和木星","火星与木星","木星和火星"]),
    CQ("q-ph-es-pr08","physics-8ES-s03","mcq",
       "小行星与星系的关系，正确的是？",
       "Which statement about asteroids and galaxies is correct?",
       "a", "小行星属于太阳系，太阳系又在银河系中。不要把小行星叫做星系。",
       "Asteroids belong to the Solar System, which lies in the Milky Way. An asteroid is not a galaxy.",
       options=_opts(("小行星属于太阳系，太阳系位于星系中", "Asteroids belong to the Solar System, which lies in a galaxy"),
                     ("每颗小行星都是一个星系", "Each asteroid is a galaxy"),
                     ("星系比小行星小", "A galaxy is smaller than an asteroid"),
                     ("二者毫无关系", "They are unrelated"))),
]
questions += es_prac
sets.append(pset("practice-physics-8ES", "physics-8ES", "practice",
                 "本章练习 · 地球与太空", "Chapter practice · Earth and Space",
                 [q["id"] for q in es_prac], minutes=12, published="2026-11-06T09:00:00+08:00"))

es_paper = [
    CQ("q-ph-es-pa01","physics-8ES-s01","mcq",
       "地球周围存在着？",
       "Around the Earth there is:",
       "b", "磁场，可用巨型条形磁体作简单模型。",
       "a magnetic field, modelled simply as a huge bar magnet.",
       options=_opts(("只有电场，没有磁场", "an electric field only, and no magnetic field"),
                     ("磁场", "a magnetic field"),
                     ("一层完全隔绝磁力的墙", "a wall that completely blocks magnetism"),
                     ("与磁无关的真空壳", "a vacuum shell unrelated to magnetism"))),
    CQ("q-ph-es-pa02","physics-8ES-s01","mcq",
       "磁北与地理北极？",
       "Magnetic north and the geographic North Pole:",
       "c", "接近但不完全是同一点。", "are close but not exactly the same point.",
       options=_opts(("永远精确重合", "always coincide exactly"),
                     ("相距半个地球", "are always half a world apart"),
                     ("接近但不完全重合", "are close but not exactly the same"),
                     ("每天对换一次", "swap places once a day"))),
    CQ("q-ph-es-pa03","physics-8ES-s01","mcq",
       "地球磁场的一个作用是？",
       "One role of the Earth’s magnetic field is that it:",
       "a", "有助于偏转部分来自太空的带电粒子。",
       "helps to deflect some charged particles arriving from space.",
       options=_opts(("有助于偏转部分来自太空的带电粒子", "helps to deflect some charged particles from space"),
                     ("让地球停止自转", "stops the Earth rotating"),
                     ("代替太阳发光", "replaces the Sun as a light source"),
                     ("消灭引力", "cancels gravity"))),
    CQ("q-ph-es-pa04","physics-8ES-s01","mcq",
       "指南针 N 极指向地理北方附近，说明那边相当于？",
       "A compass N pole points towards geographic north, which means that region acts as:",
       "d", "地磁 S 极（异名相吸）。这是常见易错点。",
       "a magnetic S pole (unlike poles attract). This is a common pitfall.",
       options=_opts(("地磁 N 极", "a magnetic N pole"),
                     ("没有磁性", "having no magnetism"),
                     ("一个星系的中心", "the centre of a galaxy"),
                     ("地磁 S 极", "a magnetic S pole"))),
    CQ("q-ph-es-pa05","physics-8ES-s02","short",
       "我们的太阳属于哪个星系？",
       "Which galaxy does our Sun belong to?",
       "Milky Way", "银河系。", "The Milky Way.",
       accepted=["Milky Way","the Milky Way","Milky Way galaxy","银河系","银河"]),
    CQ("q-ph-es-pa06","physics-8ES-s02","mcq",
       "从大到小，较合理的顺序是？",
       "From largest to smallest, a reasonable order is:",
       "b", "星系 → 恒星系统 → 行星。", "galaxy → star system → planet.",
       options=_opts(("行星 → 星系 → 恒星", "planet → galaxy → star"),
                     ("星系 → 恒星（及恒星系统）→ 行星", "galaxy → star (and its system) → planet"),
                     ("月球 → 银河系 → 石子", "the Moon → the Milky Way → a pebble"),
                     ("一粒尘埃 → 宇宙 → 一颗行星", "a dust grain → the Universe → one planet"))),
    CQ("q-ph-es-pa07","physics-8ES-s02","mcq",
       "宇宙中星系的数量？",
       "The number of galaxies in the Universe is:",
       "a", "非常多，银河系只是其中之一。",
       "very large; the Milky Way is only one of them.",
       options=_opts(("非常多，银河系只是其中之一", "very large; the Milky Way is only one of them"),
                     ("恰好只有一个", "exactly one"),
                     ("为零", "zero"),
                     ("恰好等于太阳系行星数", "exactly the number of planets in the Solar System"))),
    CQ("q-ph-es-pa08","physics-8ES-s02","mcq",
       "把太阳系称为“一个星系”，错在哪里？",
       "What is wrong with calling the Solar System a galaxy?",
       "c", "太阳系只有一颗恒星及其周围天体，远小于由大量恒星组成的星系。",
       "The Solar System is one star and the bodies around it, much smaller than a galaxy of many stars.",
       options=_opts(("太阳系比任何星系都大", "The Solar System is larger than any galaxy"),
                     ("这两个词永远可以互换", "The two words can always be swapped"),
                     ("太阳系不是由大量恒星组成的系统", "The Solar System is not a huge collection of stars"),
                     ("星系比行星还小", "A galaxy is smaller than a planet"))),
    CQ("q-ph-es-pa09","physics-8ES-s03","mcq",
       "小行星通常是？",
       "An asteroid is usually:",
       "b", "比行星小得多的岩石或金属天体，大多绕太阳运行。",
       "a rocky or metallic body much smaller than a planet, usually orbiting the Sun.",
       options=_opts(("和木星一样大的气体行星", "a gas planet as large as Jupiter"),
                     ("比行星小得多的岩石或金属天体", "a rocky or metallic body much smaller than a planet"),
                     ("一颗恒星", "a star"),
                     ("地球磁场的碎片", "a fragment of the Earth’s magnetic field"))),
    CQ("q-ph-es-pa10","physics-8ES-s03","mcq",
       "主小行星带中的大多数小行星绕什么运行？",
       "Most asteroids in the main belt orbit:",
       "d", "太阳。", "the Sun.",
       options=_opts(("只绕地球", "only the Earth"),
                     ("只绕北极星", "only the Pole Star"),
                     ("只绕银河系中心且绝不绕太阳", "only the centre of the Milky Way, never the Sun"),
                     ("太阳", "the Sun"))),
    CQ("q-ph-es-pa11","physics-8ES-s03","mcq",
       "关于近地小行星，较合理的说法是？",
       "A reasonable statement about near-Earth asteroids is:",
       "a", "少数轨道靠近地球的天体需要监测，但不是每一颗小行星都会撞击地球。",
       "a few bodies that pass near Earth are monitored; not every asteroid will hit the Earth.",
       options=_opts(("少数靠近地球的天体需要监测，并非所有小行星都会撞击地球", "a few near-Earth bodies are monitored; not every asteroid will hit Earth"),
                     ("每一颗都必定在明天撞击地球", "every one will certainly hit the Earth tomorrow"),
                     ("小行星不可能有轨道", "asteroids cannot have orbits"),
                     ("它们都在太阳内部", "they all lie inside the Sun"))),
]
questions += es_paper
sets.append(pset("paper-physics-8ES", "physics-8ES", "paper",
                 "本章测试卷 · 地球与太空", "Chapter test · Earth and Space",
                 [q["id"] for q in es_paper], minutes=20, published="2026-11-06T09:00:00+08:00"))

# ----- Comprehensive paper (all four chapters, ~35 min, 15 questions) -----
comp = [
    CQ("q-ph-comp-01","physics-8Pf-s01","numeric",
       r"一辆汽车 $8\ \text{s}$ 内前进 $96\ \text{m}$。平均速度是多少 $\text{m/s}$？",
       r"A car travels $96\ \text{m}$ in $8\ \text{s}$. What is its average speed in $\text{m/s}$?",
       "12", r"$v=96/8=12\ \text{m/s}$。", r"$v=96/8=12\ \text{m/s}$.", tolerance=0.01),
    CQ("q-ph-comp-02","physics-8Pf-s01","numeric",
       r"把 $90\ \text{km/h}$ 换算成 $\text{m/s}$。",
       r"Convert $90\ \text{km/h}$ into $\text{m/s}$.",
       "25", r"$90\div 3.6=25\ \text{m/s}$。", r"$90\div 3.6=25\ \text{m/s}$.", tolerance=0.01),
    CQ("q-ph-comp-03","physics-8Pf-s02","mcq",
       "路程—时间图像上更陡的直线通常表示？",
       "A steeper straight line on a distance–time graph usually means:",
       "b", "斜率是速度，更陡表示恒定速度更大，不是加速度。",
       "The gradient is speed; a steeper line means a greater constant speed, not acceleration.",
       options=_opts(("加速度更大", "a greater acceleration"),
                     ("恒定速度更大", "a greater constant speed"),
                     ("物体静止", "the object is stationary"),
                     ("力一定更大", "the force must be larger"))),
    CQ("q-ph-comp-04","physics-8Pf-s03","mcq",
       "合力为零时，物体将会？",
       "When the resultant force is zero, an object will:",
       "c", "保持静止或匀速直线运动。静止不等于不受力。",
       "stay at rest or keep a constant speed in a straight line. Rest does not mean “no forces”.",
       options=_opts(("一定立刻停下", "always stop at once"),
                     ("速度一定增大", "always speed up"),
                     ("保持静止或匀速直线运动", "stay at rest or keep a steady speed in a straight line"),
                     ("质量变为零", "have zero mass"))),
    CQ("q-ph-comp-05","physics-8Pf-s04","numeric",
       r"$20\ \text{N}$ 的力，垂直力臂 $0.3\ \text{m}$。力矩是多少 $\text{N\,m}$？",
       r"A $20\ \text{N}$ force has a perpendicular distance of $0.3\ \text{m}$. What is the moment in $\text{N\,m}$?",
       "6", r"$M=20\times 0.3=6\ \text{N\,m}$。必须用垂直距离。",
       r"$M=20\times 0.3=6\ \text{N\,m}$. Use the perpendicular distance.", tolerance=0.01),
    CQ("q-ph-comp-06","physics-8Pf-s05","numeric",
       r"$45\ \text{N}$ 作用在 $0.9\ \text{m}^2$ 上。压强是多少 $\text{N/m}^2$？",
       r"A $45\ \text{N}$ force acts on $0.9\ \text{m}^2$. What is the pressure in $\text{N/m}^2$?",
       "50", r"$p=45/0.9=50\ \text{N/m}^2$。不要与力矩单位 $\text{N\,m}$ 混淆。",
       r"$p=45/0.9=50\ \text{N/m}^2$. Do not confuse this with the moment unit $\text{N\,m}$.", tolerance=0.01),
    CQ("q-ph-comp-07","physics-8Pf-s06","mcq",
       "气体压强主要来自粒子？",
       "Gas pressure is mainly due to particles:",
       "a", "不断碰撞器壁。封闭气体对各个方向的器壁都有压强。",
       "colliding continually with the walls. A trapped gas pushes on every wall, not only downwards.",
       options=_opts(("不断碰撞器壁", "colliding continually with the walls"),
                     ("全部静止在底部", "all sitting still at the bottom"),
                     ("变成光线", "turning into light"),
                     ("只有重量向下，侧面不受力", "their weight only, so the sides feel no force"))),
    CQ("q-ph-comp-08","physics-8Ps-s01","numeric",
       r"光线与平面镜成 $20^\circ$。反射角是多少度？",
       r"A ray makes $20^\circ$ with a plane mirror. What is the angle of reflection, in degrees?",
       "70", r"入射角 $=90^\circ-20^\circ=70^\circ$，故 $r=70^\circ$。不要把 $20^\circ$ 当成入射角。",
       r"Angle of incidence $=90^\circ-20^\circ=70^\circ$, so $r=70^\circ$. Do not treat $20^\circ$ as the angle of incidence.", tolerance=0),
    CQ("q-ph-comp-09","physics-8Ps-s02","mcq",
       "光线从空气斜射入玻璃，通常会？",
       "A ray going from air into glass at an angle usually:",
       "d", "向法线偏折。折射不是 $i=r$。",
       "bends towards the normal. Refraction is not $i=r$.",
       options=_opts(("远离法线", "bends away from the normal"),
                     ("反射角等于入射角且不再进入玻璃", "reflects with $i=r$ and never enters the glass"),
                     ("沿界面滑行", "slides along the boundary"),
                     ("向法线偏折", "bends towards the normal"))),
    CQ("q-ph-comp-10","physics-8Ps-s03","mcq",
       "白光通过棱镜色散时，偏折通常最小的可见光是？",
       "When a prism disperses white light, the visible colour usually bent least is:",
       "b", "红光偏折最小，紫光最大。棱镜分开原已存在的色光。",
       "Red is bent least, violet most. The prism separates colours already present in white light.",
       options=_opts(("紫光", "violet"),
                     ("红光", "red"),
                     ("所有颜色相同", "all colours equally"),
                     ("只是绿光", "green only"))),
    CQ("q-ph-comp-11","physics-8Ps-s04","mcq",
       "红光加绿光适当叠加通常得到黄光。这与红、绿颜料混合常常不同，因为？",
       "Red light plus green light can give yellow. This often differs from mixing red and green paints because:",
       "c", "色光是加色，颜料更多地是减色（吸收）。",
       "lights add (additive colour); paints mainly absorb (subtractive colour).",
       options=_opts(("二者结果永远完全一样", "the results are always identical"),
                     ("颜料会发光而色光只会吸收", "paints emit light while coloured light only absorbs"),
                     ("色光是叠加（加色），颜料更多是吸收（减色）", "lights add (additive); paints mainly absorb (subtractive)"),
                     ("只有颜料遵守反射定律", "only paints obey the law of reflection"))),
    CQ("q-ph-comp-12","physics-8Pe-s01","mcq",
       "条形磁体外部的磁感线从哪一极指向哪一极？",
       "Outside a bar magnet, field lines run from which pole to which pole?",
       "a", "从 N 到 S。线条越密磁场越强。",
       "From N to S. Closer lines mean a stronger field.",
       options=_opts(("从 N 到 S", "from N to S"),
                     ("从 S 到 N", "from S to N"),
                     ("没有固定方向", "in no fixed direction"),
                     ("只指向地心", "only towards the Earth’s centre"))),
    CQ("q-ph-comp-13","physics-8Pe-s03","mcq",
       "使电磁铁更强的一个有效做法是（在安全前提下）？",
       "One effective way to make an electromagnet stronger (safely) is to:",
       "b", "增加匝数、适当增大电流，或使用铁芯。断电后磁性可减弱以便放下工件。",
       "increase the number of turns, increase the current sensibly, or use an iron core. Switching off lets the magnetism fall so a load can be dropped.",
       options=_opts(("切断电流并拆掉铁芯", "switch the current off and remove the core"),
                     ("增加匝数（并保持合适电流与铁芯）", "increase the number of turns (keeping a sensible current and the core)"),
                     ("改用塑料芯并尽量减少匝数", "use a plastic core and as few turns as possible"),
                     ("用裸导线密绕并浇水", "wind bare wire tightly and make it wet"))),
    CQ("q-ph-comp-14","physics-8ES-s01","mcq",
       "指南针 N 极指向地理北方附近，说明该处相当于？",
       "A compass N pole points towards geographic north, so that region acts as:",
       "d", "地磁 S 极。磁北与真北接近但不完全重合。",
       "a magnetic S pole. Magnetic north and true north are close but not the same.",
       options=_opts(("地磁 N 极", "a magnetic N pole"),
                     ("一个星系", "a galaxy"),
                     ("小行星带", "the asteroid belt"),
                     ("地磁 S 极", "a magnetic S pole"))),
    CQ("q-ph-comp-15","physics-8ES-s02","mcq",
       "下列说法正确的是？",
       "Which statement is correct?",
       "a", "太阳系位于银河系；许多小行星在火星与木星之间绕太阳运行。不要把太阳系或小行星叫做星系。",
       "The Solar System lies in the Milky Way; many asteroids orbit the Sun between Mars and Jupiter. Do not call the Solar System or an asteroid a galaxy.",
       options=_opts(("太阳系位于银河系，小行星是太阳系中较小的天体", "The Solar System lies in the Milky Way; asteroids are smaller bodies in the Solar System"),
                     ("太阳系本身就是一个星系，小行星则是更大的星系", "The Solar System is itself a galaxy, and each asteroid is a larger galaxy"),
                     ("小行星带位于太阳内部", "The asteroid belt lies inside the Sun"),
                     ("宇宙中只有银河系一个星系", "The Milky Way is the only galaxy in the Universe"))),
]
questions += comp
sets.append(pset("paper-physics-8-comprehensive", None, "paper",
                 "八年级物理综合测试卷", "Grade 8 Physics comprehensive paper",
                 [q["id"] for q in comp], minutes=35, published="2026-11-11T09:00:00+08:00"))
