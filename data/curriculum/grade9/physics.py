"""Grade 9 Physics — IGCSE Physics 0625, Year 1.

Order: measurement, motion, mass and weight and density, then forces
(Hooke's law, F = ma, friction, free-body diagrams, terminal velocity).
The timed paper is a practical: density, a pendulum and a spring, with a graph.
g = 9.8 N/kg as used in class.
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


SPEC = {
    "subject_id": "physics",
    "tag": "g9ph",
    "chapters": [
        {
            "id": "g9-phys-1",
            "code": "1",
            "order": 1,
            "title_zh": "第 1 章 · 物理量的测量",
            "title_en": "Chapter 1 · Measurement of physical quantities",
            "note_zh": "单位、图像、反应时间和密度实验的读数。",
            "note_en": "Units, graphs, reaction time, and readings in a density experiment.",
            "units": [{
                "id": "g9-phys-1-u1", "code": "1", "order": 1,
                "title_zh": "测量与图像", "title_en": "Measurement and graphs",
                "lessons": [L(
                    "g9ph-1", "1.1", "测量、图像与反应时间", "Measurement, graphs and reaction time",
                    "会选用合适的单位，把数据画成可用的图像，并用自由落体估算反应时间。",
                    "Choose a suitable unit, plot data so the graph can be used, and estimate reaction time from free fall.",
                    [("物理量要带单位。长度用 m 或 cm，时间用 s，质量用 kg 或 g，前后必须一致。", "A quantity needs a unit. Length in m or cm, time in s, mass in kg or g, and the choice must stay consistent."),
                     ("图像要有标好的轴、均匀刻度和最佳拟合线。直线的梯度用大三角形，不要只用相邻两点。", "A graph needs labelled axes, an even scale and a line of best fit. Take the gradient from a large triangle, not from two neighbouring points."),
                     ("读数要对着刻度、避开视差；量筒读弯月面底部。", "Read opposite the scale to avoid parallax. Read the bottom of the meniscus in a measuring cylinder."),
                     ("尺子下落时 $s = \\tfrac{1}{2}gt^2$。反应时间约零点几秒，距离大约十几到二十厘米。", "For a falling ruler, $s = \\tfrac{1}{2}gt^2$. A reaction time of a few tenths of a second is a fall of roughly ten to twenty centimetres.")],
                    "实验记录先写表：物理量、单位、每一列的原始读数，再算导出量。不要在表里只写已经心算过的密度。图像的自变量通常放横轴。若点几乎在一条过原点的直线上，可以说两个量成正比，但要先看是否真的过原点。\n\n反应时间实验：同学松开尺子，你一看见就捏住。测量下落距离 $s$，用 $g = 9.8\\,\\mathrm{m/s^2}$ 求 $t = \\sqrt{2s/g}$。多测几次取平均，可以减小一次偶然捏早或捏晚的影响。",
                    "Record a table first: quantity, unit, and the raw reading in each column, then the derived quantity. Do not write only a density you calculated in your head. The independent variable usually goes on the horizontal axis. If the points lie on a straight line through the origin, the two quantities are proportional — but check that the line really does pass through the origin.\n\nReaction time: a partner releases a ruler and you catch it when you see it move. Measure the distance $s$ and use $g = 9.8\\,\\mathrm{m/s^2}$ so that $t = \\sqrt{2s/g}$. Repeating and averaging reduces the effect of one catch that was unusually early or late.",
                    "尺子下落 $0.20\\,\\mathrm{m}$。\n\n$t = \\sqrt{2 \\times 0.20 / 9.8} = \\sqrt{0.0408} = 0.202\\,\\mathrm{s}$。反应时间大约是 $0.20\\,\\mathrm{s}$。",
                    "A ruler falls $0.20\\,\\mathrm{m}$.\n\n$t = \\sqrt{2 \\times 0.20 / 9.8} = \\sqrt{0.0408} = 0.202\\,\\mathrm{s}$. The reaction time is about $0.20\\,\\mathrm{s}$.",
                    [("梯度只用两个靠得很近的点，读数误差被放大。", "Taking a gradient from two points that are very close, so the reading error is magnified."),
                     ("反应时间直接用距离除以一个凭空假定的速度。", "Finding reaction time by dividing distance by a speed that was never measured.")],
                    [num("尺子下落 $0.20\\,\\mathrm{m}$，$g = 9.8\\,\\mathrm{m/s^2}$。反应时间大约是多少秒？保留两位小数。", "A ruler falls $0.20\\,\\mathrm{m}$ and $g = 9.8\\,\\mathrm{m/s^2}$. Estimate the reaction time in seconds, to 2 decimal places.", "0.20", "$\\sqrt{0.0408} \\approx 0.20$。", "$\\sqrt{0.0408} \\approx 0.20$.", 2, 0.02),
                     short("画最佳拟合线的梯度时，三角形应当怎样取？", "How should the triangle for a gradient be chosen?", "as large as possible", "尽量大。", "As large as possible.", ["as large as possible", "large triangle", "用大三角形", "a large triangle"], 1),
                     mcq("读取量筒中水面时，眼睛应当？", "When reading a water level, your eye should be:", "b", "与弯月面齐平。", "Level with the meniscus.", [("从上方俯视", "looking down from above"), ("与弯月面齐平", "level with the meniscus"), ("闭上", "closed"), ("只看容器底部", "looking only at the base")])],
                )],
            }],
        },
        {
            "id": "g9-phys-2",
            "code": "2",
            "order": 2,
            "title_zh": "第 2 章 · 运动",
            "title_en": "Chapter 2 · Motion",
            "note_zh": "位移–时间、速度–时间、加速度–时间图像，以及自由落体。",
            "note_en": "Displacement–time, velocity–time and acceleration–time graphs, and free fall.",
            "units": [{
                "id": "g9-phys-2-u1", "code": "2", "order": 1,
                "title_zh": "图像与自由落体", "title_en": "Graphs and free fall",
                "lessons": [
                    L("g9ph-2", "2.1", "运动图像", "Motion graphs",
                      "能从 $s$–$t$、$v$–$t$ 和 $a$–$t$ 图像读出速度、加速度和位移。",
                      "Read speed, acceleration and displacement from $s$–$t$, $v$–$t$ and $a$–$t$ graphs.",
                      [(" $s$–$t$ 图像的梯度是速度。水平线表示静止。", "The gradient of an $s$–$t$ graph is velocity. A horizontal line means the object is at rest."),
                       (" $v$–$t$ 图像的梯度是加速度，图像下的面积是位移。", "The gradient of a $v$–$t$ graph is acceleration. The area under it is displacement."),
                       ("匀加速的 $v$–$t$ 图是一条斜直线，不是曲线。", "Constant acceleration is a straight sloping line on a $v$–$t$ graph, not a curve."),
                       ("$v = u + at$，平均速度 $(u+v)/2$，以及 $v^2 = u^2 + 2as$。", "$v = u + at$, average speed $(u+v)/2$, and $v^2 = u^2 + 2as$.")],
                      "先看纵轴是位置、速度还是加速度，再谈斜率。同一条斜直线，在 $s$–$t$ 图上是匀速，在 $v$–$t$ 图上是匀加速。面积只在 $v$–$t$ 图上表示位移；在 $s$–$t$ 图上谈面积没有这个意义。\n\n计算前统一单位。$20\\,\\mathrm{m/s}$ 经过 $4\\,\\mathrm{s}$ 匀减速到停止，加速度是 $(0-20)/4 = -5\\,\\mathrm{m/s^2}$，位移是三角形面积 $\\tfrac{1}{2}\\times 4\\times 20 = 40\\,\\mathrm{m}$。",
                      "Read the vertical axis before you talk about slope. The same sloping straight line is constant speed on an $s$–$t$ graph and constant acceleration on a $v$–$t$ graph. Area means displacement only on a $v$–$t$ graph.\n\nConvert units first. From $20\\,\\mathrm{m/s}$ to rest in $4\\,\\mathrm{s}$ at constant deceleration, $a = (0-20)/4 = -5\\,\\mathrm{m/s^2}$, and the displacement is the triangular area $\\tfrac{1}{2}\\times 4\\times 20 = 40\\,\\mathrm{m}$.",
                      "汽车从静止以 $2\\,\\mathrm{m/s^2}$ 加速 $5\\,\\mathrm{s}$。\n\n$v = 0 + 2\\times 5 = 10\\,\\mathrm{m/s}$。位移 $s = \\tfrac{1}{2}\\times 5\\times 10 = 25\\,\\mathrm{m}$。",
                      "A car accelerates from rest at $2\\,\\mathrm{m/s^2}$ for $5\\,\\mathrm{s}$.\n\n$v = 0 + 2\\times 5 = 10\\,\\mathrm{m/s}$. Displacement $s = \\tfrac{1}{2}\\times 5\\times 10 = 25\\,\\mathrm{m}$.",
                      [("把 $s$–$t$ 图的斜率说成加速度。", "Calling the slope of an $s$–$t$ graph the acceleration."),
                       ("减速时加速度写成正数，又没有说明方向。", "Writing a deceleration as a positive acceleration without saying anything about direction."),
                       ("面积单位忘了：秒乘米每秒得到米。", "Forgetting that seconds times metres per second give metres.")],
                      [num("从静止以 $2\\,\\mathrm{m/s^2}$ 加速 $5\\,\\mathrm{s}$，末速度是多少 m/s？", "From rest at $2\\,\\mathrm{m/s^2}$ for $5\\,\\mathrm{s}$, what is the final speed in m/s?", "10", "$v = at = 10$。", "$v = at = 10$.", 1, 0),
                       num("上题的位移是多少 m？", "What is the displacement in that same motion, in m?", "25", "三角形面积或 $s = \\tfrac{1}{2}at^2$。", "Triangular area, or $s = \\tfrac{1}{2}at^2$.", 2, 0),
                       mcq("$v$–$t$ 图是一条水平直线，表示？", "A horizontal line on a $v$–$t$ graph means:", "c", "匀速，加速度为零。", "Constant velocity and zero acceleration.", [("静止", "at rest"), ("匀加速", "constant acceleration"), ("匀速", "constant velocity"), ("速度与时间成正比且不过原点以外的任意曲线", "any curve of speed against time")])]),
                    L("g9ph-3", "2.2", "自由落体与 g", "Free fall and g",
                      "知道自由落体加速度约为 $9.8\\,\\mathrm{m/s^2}$，并能把它和重力场强度 $9.8\\,\\mathrm{N/kg}$ 联系起来。",
                      "Use a free-fall acceleration of about $9.8\\,\\mathrm{m/s^2}$, and connect it to a gravitational field strength of $9.8\\,\\mathrm{N/kg}$.",
                      [("近地面、忽略空气阻力时，物体以约 $g = 9.8\\,\\mathrm{m/s^2}$ 向下加速。", "Near the Earth, with air resistance ignored, an object accelerates downwards at about $g = 9.8\\,\\mathrm{m/s^2}$."),
                       ("这个 $g$ 与质量无关。真空中羽毛和铁球一起落地。", "This $g$ does not depend on mass. In a vacuum a feather and a ball land together."),
                       ("$g$ 也可以写成 $9.8\\,\\mathrm{N/kg}$：每千克质量受到的重力。", "$g$ is also $9.8\\,\\mathrm{N/kg}$: the gravitational force on each kilogram."),
                       ("有空气阻力时加速度会变小，最后可能达到终端速度。", "With air resistance the acceleration becomes smaller and a terminal velocity may be reached.")],
                      "从静止下落，$v = gt$，$s = \\tfrac{1}{2}gt^2$。下落 $1\\,\\mathrm{s}$，速度约 $9.8\\,\\mathrm{m/s}$，距离约 $4.9\\,\\mathrm{m}$。估计题有时把 $g$ 取成 $10$，计算题若写了 $9.8$ 就要用 $9.8$。\n\n向上抛出时，上升到最高点的速度为 0，加速度仍然向下，大约仍是 $g$。加速度并不在最高点变成 0。",
                      "From rest, $v = gt$ and $s = \\tfrac{1}{2}gt^2$. In $1\\,\\mathrm{s}$ the speed is about $9.8\\,\\mathrm{m/s}$ and the distance about $4.9\\,\\mathrm{m}$. Estimation sometimes uses $g = 10$. If you have written $9.8$, use $9.8$.\n\nThrown upwards, the speed at the top is 0, but the acceleration is still downwards at about $g$. It does not become zero at the top.",
                      "石块从静止下落 $2.0\\,\\mathrm{s}$，$g = 9.8$。\n\n$s = \\tfrac{1}{2}\\times 9.8\\times 4 = 19.6\\,\\mathrm{m}$。",
                      "A stone falls from rest for $2.0\\,\\mathrm{s}$, $g = 9.8$.\n\n$s = \\tfrac{1}{2}\\times 9.8\\times 4 = 19.6\\,\\mathrm{m}$.",
                      [("最高点加速度写成 0。", "Writing the acceleration at the highest point as 0."),
                       ("空气中的落体也一律写成加速度永远等于 g。", "Claiming that a fall through air has acceleration equal to g for the whole motion.")],
                      [num("从静止自由下落 $2.0\\,\\mathrm{s}$，$g = 9.8\\,\\mathrm{m/s^2}$。下落距离是多少 m？", "An object falls from rest for $2.0\\,\\mathrm{s}$, $g = 9.8\\,\\mathrm{m/s^2}$. How far does it fall, in m?", "19.6", "$\\tfrac{1}{2}gt^2 = 19.6$。", "$\\tfrac{1}{2}gt^2 = 19.6$.", 2, 0.1),
                       mcq("真空中，重铁球和轻羽毛同时释放。", "In a vacuum a heavy ball and a light feather are released together.", "a", "同时落地。", "They land together.", [("同时落地", "they land together"), ("铁球一定先到", "the ball must arrive first"), ("羽毛加速度更大", "the feather has the larger acceleration"), ("两者加速度都是 0", "both have zero acceleration")]),
                       short("物体被竖直上抛，到达最高点时加速度约是多少？", "An object is thrown straight up. What is the acceleration at the highest point, approximately?", "9.8 m/s^2 downward", "速度为 0，加速度仍约为 g 向下。", "Speed is 0; acceleration is still about g downwards.", ["9.8 m/s^2 downward", "9.8 downwards", "g downward", "9.8 m/s2 down"], 2)]),
                ],
            }],
        },
        {
            "id": "g9-phys-3",
            "code": "3",
            "order": 3,
            "title_zh": "第 3 章 · 质量、重量与密度",
            "title_en": "Chapter 3 · Mass, weight and density",
            "units": [{
                "id": "g9-phys-3-u1", "code": "3", "order": 1,
                "title_zh": "质量、重量、密度", "title_en": "Mass, weight and density",
                "lessons": [L(
                    "g9ph-4", "3.1", "质量、重量与密度", "Mass, weight and density",
                    "会用 $W = mg$ 和 $\\rho = m/V$，并说明不规则固体与液体体积怎样测。",
                    "Use $W = mg$ and $\\rho = m/V$, and describe how to find the volume of an irregular solid and of a liquid.",
                    [("质量是物质的多少，单位 kg，不随地点改变。", "Mass is the amount of matter, in kg. It does not change from place to place."),
                     ("重量是重力，$W = mg$。在地球表面 $g = 9.8\\,\\mathrm{N/kg}$，重量的单位是 N。", "Weight is the gravitational force, $W = mg$. At the Earth’s surface $g = 9.8\\,\\mathrm{N/kg}$, and weight is in N."),
                     ("密度 $\\rho = m/V$。规则固体用尺量体积；不规则固体用排水法。", "Density is $\\rho = m/V$. Measure a regular solid with a ruler. Use displacement for an irregular solid."),
                     ("液体：测空容器和装液体后的质量差，体积读量筒。", "For a liquid, the mass is the difference between the full and empty container, and the volume is read from the cylinder.")],
                    "质量 $50\\,\\mathrm{kg}$ 的人，重量 $W = 50 \\times 9.8 = 490\\,\\mathrm{N}$。到月球质量仍是 50 kg，重量变小，因为那里的 $g$ 较小。不要把 50 kg 叫成重量。\n\n排水法：量筒先读 $V_1$，物体完全浸没后再读 $V_2$，体积是 $V_2 - V_1$。物体要全部没入，又不能溅出水。密度的单位随你用的 m 和 V 走：g 和 cm³ 得到 g/cm³，kg 和 m³ 得到 kg/m³。$1\\,\\mathrm{g/cm^3} = 1000\\,\\mathrm{kg/m^3}$。",
                    "A person of mass $50\\,\\mathrm{kg}$ has weight $W = 50 \\times 9.8 = 490\\,\\mathrm{N}$. On the Moon the mass is still 50 kg and the weight is smaller, because $g$ is smaller there. Do not call 50 kg a weight.\n\nDisplacement: read $V_1$, submerge the object completely, read $V_2$. The volume is $V_2 - V_1$. The object must be fully under water and must not splash. The density unit follows the units of m and V. $1\\,\\mathrm{g/cm^3} = 1000\\,\\mathrm{kg/m^3}$.",
                    "石块质量 $48\\,\\mathrm{g}$。水位从 $50\\,\\mathrm{cm^3}$ 升到 $70\\,\\mathrm{cm^3}$。\n\n体积 $= 20\\,\\mathrm{cm^3}$。密度 $= 48/20 = 2.4\\,\\mathrm{g/cm^3}$。",
                    "A stone has mass $48\\,\\mathrm{g}$. The water level rises from $50\\,\\mathrm{cm^3}$ to $70\\,\\mathrm{cm^3}$.\n\nVolume $= 20\\,\\mathrm{cm^3}$. Density $= 48/20 = 2.4\\,\\mathrm{g/cm^3}$.",
                    [("把质量的单位写成牛顿。", "Giving mass the unit newton."),
                     ("排水法用最后的水位当体积，没有减去原来的水。", "Using the final water level as the volume and not subtracting the original water."),
                     ("g 用了 9.8，单位却写成 kg。", "Using 9.8 and then giving the weight in kg.")],
                    [num("质量 $50\\,\\mathrm{kg}$，$g = 9.8\\,\\mathrm{N/kg}$。重量是多少 N？", "Mass $50\\,\\mathrm{kg}$, $g = 9.8\\,\\mathrm{N/kg}$. What is the weight in N?", "490", "$50 \\times 9.8 = 490$。", "$50 \\times 9.8 = 490$.", 1, 0),
                     num("质量 $48\\,\\mathrm{g}$，排水体积 $20\\,\\mathrm{cm^3}$。密度是多少 g/cm³？", "Mass $48\\,\\mathrm{g}$, displaced volume $20\\,\\mathrm{cm^3}$. What is the density in g/cm³?", "2.4", "$48/20 = 2.4$。", "$48/20 = 2.4$.", 2, 0.01),
                     short("质量会不会因为从地球到月球而改变？", "Does mass change when an object is taken from the Earth to the Moon?", "no", "质量不变，重量改变。", "Mass stays the same; weight changes.", ["no", "不变", "mass unchanged"], 1)],
                )],
            }],
        },
        {
            "id": "g9-phys-4",
            "code": "4",
            "order": 4,
            "title_zh": "第 4 章 · 力",
            "title_en": "Chapter 4 · Forces",
            "note_zh": "当前内容：胡克定律、牛顿第二定律、摩擦力、受力图、空气阻力和终端速度。",
            "note_en": "Current work: Hooke's law, Newton's second law, friction, free-body diagrams, air resistance and terminal velocity.",
            "units": [{
                "id": "g9-phys-4-u1", "code": "4", "order": 1,
                "title_zh": "弹力、合力与阻力", "title_en": "Springs, resultant force and resistance",
                "lessons": [
                    L("g9ph-5", "4.1", "胡克定律与弹簧", "Hooke's law and springs",
                      "会用 $F = kx$ 从图像求劲度系数，并指出比例极限。",
                      "Use $F = kx$, find a spring constant from a graph, and identify the limit of proportionality.",
                      [("在弹性限度内，$F = kx$。$x$ 是伸长量，不是弹簧现在的总长度。", "Within the elastic limit, $F = kx$. $x$ is the extension, not the new total length."),
                       ("$F$–$x$ 图在比例区间是过原点的直线，梯度就是 $k$。", "An $F$–$x$ graph is a straight line through the origin in the proportional region, and its gradient is $k$."),
                       ("超过比例极限后，图像弯曲；超过弹性限度后，撤力也不能回到原长。", "Past the limit of proportionality the graph curves. Past the elastic limit the spring does not return to its original length."),
                       ("实验要先记录原长，再加砝码，伸长 = 新长 − 原长。", "Record the original length first. Extension = new length − original length.")],
                      "若力用 N、伸长用 m，$k$ 的单位是 N/m。用 cm 时单位是 N/cm，代入公式前要和题目一致。多个弹簧串联会更“软”，劲度变小；那是下一步的变化，本课先把一根弹簧的 $k$ 求稳。\n\n图像上用比例区间里离得远的两点求梯度。把已经弯曲的点也算进三角形，会把 $k$ 算小。",
                      "If force is in N and extension in m, $k$ is in N/m. In cm the unit is N/cm. Match the question. Springs in series are “softer” and $k$ falls; leave that until the single spring is secure.\n\nTake the gradient from two distant points inside the straight region. Including a point on the curve makes $k$ too small.",
                      "原长 $8.0\\,\\mathrm{cm}$，挂上 $3.0\\,\\mathrm{N}$ 后长 $14.0\\,\\mathrm{cm}$。\n\n伸长 $= 6.0\\,\\mathrm{cm} = 0.060\\,\\mathrm{m}$。$k = F/x = 3.0/0.060 = 50\\,\\mathrm{N/m}$。",
                      "Original length $8.0\\,\\mathrm{cm}$. With $3.0\\,\\mathrm{N}$ the length is $14.0\\,\\mathrm{cm}$.\n\nExtension $= 6.0\\,\\mathrm{cm} = 0.060\\,\\mathrm{m}$. $k = F/x = 3.0/0.060 = 50\\,\\mathrm{N/m}$.",
                      [("用弹簧的总长度代替伸长。", "Using the total length instead of the extension."),
                       ("把比例极限以外的点也当成仍满足 $F = kx$。", "Treating points beyond the limit of proportionality as if $F = kx$ still held.")],
                      [num("力 $3.0\\,\\mathrm{N}$，伸长 $0.060\\,\\mathrm{m}$。劲度系数是多少 N/m？", "A force of $3.0\\,\\mathrm{N}$ causes an extension of $0.060\\,\\mathrm{m}$. What is $k$ in N/m?", "50", "$3/0.06 = 50$。", "$3/0.06 = 50$.", 2, 0),
                       short("伸长量等于什么减什么？", "Extension equals which length minus which?", "loaded length minus original length", "加载后的长度减去原长。", "Loaded length minus original length.", ["loaded length minus original length", "new length - original length", "总长减原长"], 1),
                       mcq("超过弹性限度后撤去力，弹簧将？", "After the elastic limit, when the force is removed, the spring:", "d", "不能回到原来的长度。", "Does not return to its original length.", [("一定变得更短于原长且仍服从胡克定律", "must become shorter than before and still obey Hooke's law"), ("梯度变成质量", "has a gradient equal to the mass"), ("仍然一定回到原长", "must still return to the original length"), ("不能回到原来的长度", "does not return to its original length")])],
                    ),
                    L("g9ph-6", "4.2", "牛顿第二定律、摩擦力与受力图", "Newton's second law, friction and free-body diagrams",
                      "会画受力图，求合力，并用 $F = ma$ 计算加速度。",
                      "Draw a free-body diagram, find the resultant force, and use $F = ma$.",
                      [("牛顿第二定律：$F = ma$。$F$ 是合力，单位 N；质量用 kg。", "Newton’s second law: $F = ma$. $F$ is the resultant force in N, and mass is in kg."),
                       ("受力图只画研究对象受到的力，箭头从物体向外，标明大小和方向。", "A free-body diagram shows only forces on the object you chose. Arrows start on the object and are labelled."),
                       ("摩擦力阻碍相对滑动，方向与相对运动或运动趋势相反。", "Friction opposes slipping. It is opposite to the relative motion, or to the intended motion."),
                       ("合力为零时加速度为零，物体保持静止或匀速直线运动。", "If the resultant force is zero, acceleration is zero: the object stays at rest or moves at constant velocity.")],
                      "水平面上：向右的拉力、向左的摩擦、向下的重量、向上的支持力。支持力与重量在竖直方向抵消时，水平合力是拉力减摩擦。加速度用这个合力除以质量。\n\n$1200\\,\\mathrm{kg}$ 的车，拉力与阻力的合力是 $3000\\,\\mathrm{N}$，则 $a = 3000/1200 = 2.5\\,\\mathrm{m/s^2}$。不要把发动机的牵引力直接当成合力，除非题目说明阻力为零。",
                      "On a level surface: pull to the right, friction to the left, weight down, normal contact force up. If the normal force cancels the weight, the horizontal resultant is pull minus friction. Divide that resultant by the mass.\n\nA $1200\\,\\mathrm{kg}$ car with a resultant of $3000\\,\\mathrm{N}$ has $a = 3000/1200 = 2.5\\,\\mathrm{m/s^2}$. Do not use the driving force as the resultant unless the question says resistance is zero.",
                      "质量 $2.0\\,\\mathrm{kg}$，向右的力 $10\\,\\mathrm{N}$，摩擦 $4\\,\\mathrm{N}$。\n\n合力 $= 6\\,\\mathrm{N}$。$a = 6/2 = 3\\,\\mathrm{m/s^2}$，向右。",
                      "Mass $2.0\\,\\mathrm{kg}$, a $10\\,\\mathrm{N}$ force to the right, friction $4\\,\\mathrm{N}$.\n\nResultant $= 6\\,\\mathrm{N}$. $a = 6/2 = 3\\,\\mathrm{m/s^2}$ to the right.",
                      [("公式里用了其中一个力，而不是合力。", "Putting one of the forces into the formula instead of the resultant."),
                       ("受力图画了物体施加给别人的力。", "Drawing the forces the object exerts on other things."),
                       ("质量用克代入 $F = ma$。", "Putting mass in grams into $F = ma$.")],
                      [num("合力 $3000\\,\\mathrm{N}$，质量 $1200\\,\\mathrm{kg}$。加速度是多少 m/s²？", "Resultant force $3000\\,\\mathrm{N}$, mass $1200\\,\\mathrm{kg}$. What is the acceleration in m/s²?", "2.5", "$3000/1200 = 2.5$。", "$3000/1200 = 2.5$.", 2, 0),
                       num("向右 $10\\,\\mathrm{N}$，向左摩擦 $4\\,\\mathrm{N}$。合力是多少 N？", "10 N to the right and 4 N of friction to the left. What is the resultant, in N?", "6", "10 − 4 = 6，向右。", "10 − 4 = 6, to the right.", 1, 0),
                       short("合力为零时，加速度是多少？", "If the resultant force is zero, what is the acceleration?", "0", "加速度为零。", "The acceleration is zero.", ["0", "zero", "零"], 1)],
                    ),
                    L("g9ph-7", "4.3", "空气阻力与终端速度", "Air resistance and terminal velocity",
                      "能按下落过程说明重量、空气阻力和加速度如何变化，直到终端速度。",
                      "Describe how weight, air resistance and acceleration change during a fall, up to terminal velocity.",
                      [("重量 $mg$ 在近地面可看作不变，方向向下。", "Weight $mg$ can be taken as constant near the Earth, acting downwards."),
                       ("空气阻力随速度增大而增大，方向与运动相反。", "Air resistance increases as speed increases, opposite to the motion."),
                       ("一开始阻力小于重量，合力向下，物体加速。", "At first resistance is less than weight, the resultant is downwards, and the object accelerates."),
                       ("阻力等于重量时合力为零，加速度为零，速度不再增加。这就是终端速度。", "When resistance equals weight the resultant is zero, acceleration is zero, and speed stops increasing. That is terminal velocity.")],
                      "下落可以分成三段写。刚释放：速度几乎为 0，阻力几乎为 0，加速度约等于 $g$。加速过程中阻力变大，合力变小，加速度变小，但速度仍在增加。终端速度：阻力 = 重量，加速度 = 0，速度保持最大的那个恒定值。\n\n打开降落伞后阻力突然变大，大于重量，合力向上，人会减速，直到在更小的速度下阻力再次等于重量，达到一个较小的新终端速度。",
                      "Write the fall in three stages. Just released: speed is almost 0, resistance is almost 0, acceleration is about $g$. While speeding up, resistance grows, the resultant shrinks and acceleration shrinks, but speed is still increasing. At terminal velocity, resistance equals weight, acceleration is 0, and speed stays at that constant value.\n\nWhen a parachute opens, resistance suddenly exceeds weight. The resultant is upwards and the person slows, until resistance again equals weight at a smaller new terminal velocity.",
                      "一个跳伞者已经达到终端速度。此时空气阻力和重量哪一个大？\n\n**解：** 一样大。合力为零，所以加速度为零，速度不变。不是阻力大于重量——那会减速。",
                      "A skydiver has reached terminal velocity. Which is larger, air resistance or weight?\n\n**Solution:** They are equal. The resultant is zero, so acceleration is zero and speed is constant. Resistance is not greater than weight — that would cause a slowdown.",
                      [("终端速度时把加速度写成 g。", "Writing the acceleration at terminal velocity as g."),
                       ("认为速度最大时加速度也最大。", "Thinking the acceleration is greatest when the speed is greatest."),
                       ("打开降落伞后写成立刻静止。", "Writing that a parachute brings the person to rest at once.")],
                      [mcq("达到终端速度时，空气阻力与重量的关系是？", "At terminal velocity, air resistance and weight are:", "a", "大小相等。", "Equal in size.", [("大小相等", "equal in size"), ("阻力一定更大", "resistance must be larger"), ("重量变为 0", "weight has become zero"), ("两者都变为 0", "both have become zero")]),
                       short("刚释放、速度还几乎为零时，加速度大约等于什么？", "Just after release, when speed is still almost zero, the acceleration is about equal to what?", "g", "约等于 g。", "About g.", ["g", "9.8", "9.8 m/s^2"], 1),
                       mcq("降落伞打开、阻力突然大于重量时，跳伞者将？", "When a parachute opens and resistance suddenly exceeds weight, the skydiver:", "c", "减速，直到新的、更小的终端速度。", "Slows down until a new, smaller terminal velocity.", [("立刻加速到更大的终端速度", "immediately accelerates to a larger terminal velocity"), ("加速度变为 g 且速度不变", "has acceleration g and unchanged speed"), ("减速，直到较小的新终端速度", "slows until a smaller new terminal velocity"), ("质量变为 0", "has zero mass")])],
                    ),
                ],
            }],
        },
    ],
    "paper": {
        "id": "paper-g9-phys",
        "title_zh": "练习卷 · 实验：密度、单摆与弹簧",
        "title_en": "Practice paper · practical: density, pendulum and spring",
        "minutes": 40,
        "published": "2026-11-18T15:00:00+08:00",
        "items": [
            ("g9ph-4", num("石块质量 $64.0\\,\\mathrm{g}$。量筒中水从 $40\\,\\mathrm{cm^3}$ 升到 $65\\,\\mathrm{cm^3}$。石块体积是多少 cm³？", "A stone has mass $64.0\\,\\mathrm{g}$. The water rises from $40\\,\\mathrm{cm^3}$ to $65\\,\\mathrm{cm^3}$. What is the volume of the stone in cm³?", "25", "65 − 40 = 25。", "65 − 40 = 25.", 2, 0)),
            ("g9ph-4", num("用上一题的质量，密度是多少 g/cm³？", "Using that mass, what is the density in g/cm³?", "2.56", "64/25 = 2.56。", "64/25 = 2.56.", 3, 0.01)),
            ("g9ph-1", short("读取量筒时，怎样做可以减小视差？", "How do you reduce parallax when reading the cylinder?", "eye level with the meniscus", "视线与弯月面齐平。", "Keep your eye level with the meniscus.", ["eye level with the meniscus", "read at eye level", "与液面齐平", "parallax"], 2)),
            ("g9ph-1", short("为什么密度实验常要重复测量再取平均？", "Why is the density measurement often repeated and averaged?", "to reduce random error", "减小偶然误差。", "To reduce random error.", ["to reduce random error", "random error", "减小偶然误差", "increase reliability"], 2)),
            ("g9ph-2", num("单摆 10 次全振动用时 $12.4\\,\\mathrm{s}$。周期是多少秒？", "Ten complete swings of a pendulum take $12.4\\,\\mathrm{s}$. What is the period, in seconds?", "1.24", "12.4/10 = 1.24。", "12.4/10 = 1.24.", 2, 0.01)),
            ("g9ph-1", short("为什么要测 10 次全振动的总时间，而不是只测 1 次？", "Why time ten swings rather than one?", "to reduce the effect of reaction time", "反应时间的影响被分到更多次振动上。", "The reaction-time error is shared across more swings.", ["to reduce the effect of reaction time", "reaction time", "减小反应时间误差", "smaller percentage uncertainty"], 2)),
            ("g9ph-5", num("弹簧原长 $8.0\\,\\mathrm{cm}$，挂 $3.0\\,\\mathrm{N}$ 后长 $14.0\\,\\mathrm{cm}$。伸长是多少 cm？", "Original length $8.0\\,\\mathrm{cm}$. With $3.0\\,\\mathrm{N}$ the length is $14.0\\,\\mathrm{cm}$. What is the extension in cm?", "6", "14 − 8 = 6。", "14 − 8 = 6.", 2, 0)),
            ("g9ph-5", num("上题若伸长用米，$k = F/x$ 是多少 N/m？", "Using the extension in metres, what is $k = F/x$ in N/m?", "50", "3.0/0.060 = 50。", "3.0/0.060 = 50.", 3, 0)),
            ("g9ph-5", mcq("在比例极限以内，力–伸长图像应当是？", "Within the limit of proportionality, a force–extension graph should be:", "a", "过原点的直线。", "A straight line through the origin.", [("过原点的直线", "a straight line through the origin"), ("一条水平线，力增加而伸长不变", "a horizontal line, force rising and extension fixed"), ("一个圆", "a circle"), ("与质量–时间图相同的任意曲线", "any curve, the same as a mass–time graph")], 2)),
            ("g9ph-5", short("图像开始弯曲之后，还能不能用同一劲度系数继续算更大的力？", "After the graph starts to curve, can the same spring constant still be used for a larger force?", "no", "已经离开比例区间。", "The proportional region has been left.", ["no", "不能", "not within the limit"], 2)),
            ("g9ph-7", mcq("若用 $T^2$ 对摆长 $l$ 作图，在小角度下图像接近？", "For small angles, a graph of $T^2$ against length $l$ is close to:", "b", "过原点的直线，因为 $T^2$ 与 $l$ 成正比。", "A straight line through the origin, because $T^2$ is proportional to $l$.", [("与摆锤质量成正比的曲线", "a curve proportional to the bob’s mass"), ("过原点的直线", "a straight line through the origin"), ("一条竖直的线", "a vertical line"), ("与弹簧的弹性限度相同的折线", "the same kink as a spring’s elastic limit")], 2)),
            ("g9ph-3", num("另一组：摆长 $0.50\\,\\mathrm{m}$ 时测得周期 $1.42\\,\\mathrm{s}$。若只把这个周期平方，得到约多少？（保留两位小数）", "Another reading: length $0.50\\,\\mathrm{m}$, period $1.42\\,\\mathrm{s}$. What is the period squared, to 2 decimal places?", "2.02", "$1.42^2 = 2.0164$，约 $2.02$。作图时用的是这个值，而不是摆锤的质量。", "$1.42^2 = 2.0164$, about $2.02$. The graph uses this value, not the mass of the bob.", 2, 0.02)),
        ],
    },
}
