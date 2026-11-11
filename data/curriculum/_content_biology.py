"""Grade 8 Biology — complete bilingual course (Cambridge Science 0893 Stage 8)."""
from _helpers import opts
from _course_util import Course, maps_from_units, svg, INK, ACCENT
from _apply import add_lesson, add_extra_questions, add_sets

UNIT_OF, CHAPTER_OF = maps_from_units("biology")
C = Course("biology", UNIT_OF, CHAPTER_OF, recent={
    "biology-8Bs-2": "2026-11-12T09:00:00+08:00",
    "biology-8Bp-4": "2026-11-11T09:00:00+08:00",
    "biology-8Be-2": "2026-11-10T09:00:00+08:00",
}, tag="bi")


def fig(inner, w=520, h=220):
    return svg(inner.replace("{INK}", INK).replace("{ACC}", ACCENT), w=w, h=h)

D_MUSCLE = fig("""
  <line x1="80" y1="160" x2="200" y2="80" {INK}/>
  <line x1="200" y1="80" x2="320" y2="160" {INK}/>
  <circle cx="200" cy="80" r="8" {ACC}/>
  <text x="188" y="68" font-size="12" fill="currentColor">joint</text>
  <line x1="140" y1="150" x2="250" y2="90" {ACC}/>
  <text x="250" y="100" font-size="12" fill="#b85c38">biceps (contracts to bend)</text>
  <line x1="160" y1="90" x2="260" y2="150" {INK}/>
  <text x="80" y="50" font-size="12" fill="currentColor">triceps (contracts to straighten)</text>
  <text x="70" y="200" font-size="13" fill="currentColor">antagonistic pair around a joint</text>
""")
D_ALV = fig("""
  <ellipse cx="160" cy="110" rx="90" ry="70" {INK}/>
  <text x="125" y="115" font-size="13" fill="currentColor">alveolus</text>
  <line x1="250" y1="110" x2="360" y2="70" {ACC}/>
  <text x="370" y="74" font-size="12" fill="#b85c38">O2 in</text>
  <line x1="250" y1="130" x2="360" y2="170" {INK}/>
  <text x="370" y="174" font-size="12" fill="currentColor">CO2 out</text>
  <text x="60" y="210" font-size="12" fill="currentColor">thin wall, moist, rich blood supply, large surface area</text>
""")
D_FOOD = fig("""
  <rect x="60" y="40" width="120" height="140" {INK}/>
  <text x="85" y="70" font-size="13" fill="currentColor">food</text>
  <text x="70" y="100" font-size="12" fill="currentColor">energy store</text>
  <line x1="180" y1="110" x2="260" y2="110" {ACC}/>
  <polygon points="260,110 248,104 248,116" fill="#b85c38"/>
  <rect x="260" y="40" width="200" height="140" {INK}/>
  <text x="280" y="80" font-size="13" fill="currentColor">aerobic respiration</text>
  <text x="280" y="110" font-size="12" fill="currentColor">glucose + oxygen</text>
  <text x="280" y="135" font-size="12" fill="currentColor">→ CO2 + water + energy</text>
""")
D_BIOACC = fig("""
  <circle cx="80" cy="160" r="16" {INK}/>
  <text x="58" y="200" font-size="11" fill="currentColor">plankton</text>
  <text x="68" y="164" font-size="10" fill="#b85c38">*</text>
  <circle cx="200" cy="130" r="22" {INK}/>
  <text x="178" y="200" font-size="11" fill="currentColor">small fish</text>
  <text x="184" y="134" font-size="11" fill="#b85c38">**</text>
  <circle cx="340" cy="100" r="30" {INK}/>
  <text x="312" y="200" font-size="11" fill="currentColor">large fish</text>
  <text x="322" y="104" font-size="12" fill="#b85c38">****</text>
  <text x="80" y="40" font-size="13" fill="currentColor">toxin concentration rises up the food chain</text>
""")

LESSONS = []
def L(**kw):
    LESSONS.append(kw)

# ----- 8Bs.01 -----
L(
    id="biology-8Bs-1",
    title_zh="关节与拮抗肌", title_en="Joints and antagonistic muscles",
    obj_zh="本节你将学会说明关节如何使骨骼运动，以及拮抗肌如何成对拉扯骨头。",
    obj_en="This lesson you will explain how joints allow bones to move and how antagonistic muscles work in pairs to pull bones.",
    kp_zh="""- 骨骼提供支撑和保护，**关节**是骨与骨相连、允许运动的部位。
- 肌肉只能**收缩拉**骨头，不能主动把骨头推回去。
- 因此肌肉常成对工作，称为**拮抗肌**：一块收缩时，另一块舒张。
- 例如屈肘时肱二头肌收缩、肱三头肌舒张；伸肘时相反。
- 肌腱把肌肉连到骨上；韧带连接骨与骨，稳定关节。""",
    kp_en="""- The skeleton supports and protects the body; a **joint** is where bones meet and movement is allowed.
- A muscle can only **contract and pull** a bone; it cannot actively push the bone back.
- Muscles therefore work in pairs called **antagonistic muscles**: when one contracts, the other relaxes.
- To bend the elbow the biceps contracts and the triceps relaxes; to straighten it, the opposite happens.
- Tendons attach muscle to bone; ligaments connect bone to bone and stabilise the joint.""",
    body_zh=r"""人体要完成走路、抓笔、抬头，都离不开骨骼、关节和肌肉的配合。骨骼本身不会自己弯折，运动发生在关节处。

肌肉的工作方式有一个关键限制：它只能缩短（收缩）来拉骨头。要把前臂再伸直，不能指望同一块肌肉再“推”回去，而要靠对面的另一块肌肉收缩。这样成对的肌肉就是拮抗肌。

肘关节是常用例子。肱二头肌收缩，前臂被拉向肩膀，肘关节弯曲；此时肱三头肌放松。肱三头肌收缩时，前臂被拉直，肱二头肌放松。

## 例题

为什么抬起前臂和放下（伸直）前臂需要两块不同的肌肉？

**解：** 肌肉只能拉、不能推。一块肌肉收缩完成弯曲后，必须由另一块拮抗肌收缩，才能把骨头拉回伸直的位置。""",
    body_en=r"""Walking, holding a pen or lifting your head all depend on bones, joints and muscles working together. Bones do not bend in the middle; movement happens at joints.

A muscle has an important limit: it can only shorten (contract) and pull a bone. It cannot push the bone back the other way. To straighten the forearm again, a muscle on the opposite side must contract. That pairing is an antagonistic pair.

The elbow is the usual example. When the biceps contracts, the forearm is pulled towards the shoulder and the elbow bends; the triceps relaxes. When the triceps contracts, the forearm is pulled straight and the biceps relaxes.

## Worked example

Why are two different muscles needed to raise the forearm and then to straighten it?

**Solution:** A muscle can only pull, not push. After one muscle has contracted to bend the joint, the other muscle of the antagonistic pair must contract to pull the bone back to the straightened position.""",
    diff_zh="""- **以为肌肉既能拉又能推。** 肌肉只能收缩来拉。
- **把肌腱和韧带说反。** 肌腱连肌肉与骨，韧带连骨与骨。
- **忘记成对：一块收缩时另一块要舒张。**""",
    diff_en="""- **Thinking a muscle can push as well as pull.** A muscle only pulls by contracting.
- **Swapping tendons and ligaments.** Tendons join muscle to bone; ligaments join bone to bone.
- **Forgetting the pair:** when one muscle contracts, the other relaxes.""",
    diagram=D_MUSCLE,
    questions=[
        dict(type="mcq", stem_zh="肌肉对骨头的作用，最准确的是？", stem_en="The most accurate description of how a muscle acts on a bone is that it:",
             answer="b", exp_zh="肌肉只能收缩，从而拉骨头。", exp_en="A muscle can only contract, and so pull a bone.",
             options=opts(("只能把骨头推开", "can only push the bone away"), ("只能收缩从而拉骨头", "can only contract and so pull the bone"),
                          ("既能随意推也能随意变成韧带", "can push at will and can also turn into a ligament"), ("不附着在骨骼上", "is not attached to the skeleton"))),
        dict(type="mcq", stem_zh="屈肘时，通常发生的是？", stem_en="When the elbow bends, what usually happens?",
             answer="a", exp_zh="肱二头肌收缩，肱三头肌舒张。", exp_en="The biceps contracts and the triceps relaxes.",
             options=opts(("肱二头肌收缩，肱三头肌舒张", "biceps contracts, triceps relaxes"),
                          ("两块肌肉同时尽量收缩并互相推开骨头", "both muscles contract as hard as possible and push the bone"),
                          ("只有韧带在收缩", "only ligaments contract"),
                          ("肱三头肌收缩，肱二头肌也必须同时同样收缩", "the triceps contracts and the biceps must contract equally at the same time"))),
        dict(type="mcq", stem_zh="拮抗肌成对工作，是因为？", stem_en="Antagonistic muscles work in pairs because:",
             answer="c", exp_zh="一块肌肉只能把骨头拉向一个方向，反向要靠另一块。", exp_en="One muscle can only pull a bone one way; the opposite movement needs the other muscle.",
             options=opts(("一块肌肉可以完成所有方向的推和拉", "one muscle can push and pull in every direction"),
                          ("关节不需要肌肉", "joints do not need muscles"),
                          ("一块肌肉只能拉向一个方向，反向要靠另一块", "one muscle can only pull one way, so the opposite movement needs the other"),
                          ("血液会代替肌肉拉动骨骼", "blood pulls the bones instead of muscles"))),
        dict(type="short", stem_zh="肌腱和韧带的作用有何不同？", stem_en="How do the roles of a tendon and a ligament differ?",
             answer="tendon muscle to bone, ligament bone to bone",
             accepted=["tendon muscle to bone, ligament bone to bone", "tendons attach muscle to bone; ligaments connect bone to bone",
                       "肌腱连接肌肉和骨，韧带连接骨和骨", "肌腱连肌肉与骨，韧带连骨与骨"],
             answer_zh="肌腱把肌肉连到骨上；韧带连接骨与骨。", answer_en="Tendons attach muscle to bone; ligaments connect bone to bone.",
             exp_zh="不要把两者说反。", exp_en="Do not swap the two."),
        dict(type="mcq", stem_zh="伸直肘关节时，主要收缩的是？", stem_en="To straighten the elbow, the muscle that mainly contracts is the:",
             answer="d", exp_zh="肱三头肌收缩，把前臂拉直。", exp_en="The triceps contracts and pulls the forearm straight.",
             options=opts(("只有心脏", "heart only"), ("肺", "lungs"), ("肱二头肌", "biceps"), ("肱三头肌", "triceps"))),
        dict(type="mcq", stem_zh="关节的作用是？", stem_en="The role of a joint is to:",
             answer="a", exp_zh="关节是骨与骨相连并允许运动的部位。", exp_en="A joint is where bones meet and movement is allowed.",
             options=opts(("让相连的骨能够运动", "allow the connected bones to move"),
                          ("制造红细胞", "make red blood cells in every joint"),
                          ("进行有氧呼吸的全部过程", "carry out all of aerobic respiration"),
                          ("替代拮抗肌", "replace antagonistic muscles"))),
    ],
)

# ----- 8Bs.02 -----
L(
    id="biology-8Bs-2",
    title_zh="血液的组成与功能", title_en="Components of blood and their functions",
    obj_zh="本节你将学会说出血液的主要组成，并分别说明红细胞、白细胞、血小板和血浆的功能。",
    obj_en="This lesson you will name the main components of blood and state the functions of red cells, white cells, platelets and plasma.",
    kp_zh="""- 血液由**血浆**和血细胞组成。
- **红细胞**运输氧气（借助血红蛋白）；也能运输一部分二氧化碳。
- **白细胞**参与抵御病原体。
- **血小板**参与凝血，帮助伤口止血。
- **血浆**是液体部分，运输二氧化碳、养分、激素、废物和热。""",
    kp_en="""- Blood is made of **plasma** and blood cells.
- **Red blood cells** transport oxygen (using haemoglobin); they also carry some carbon dioxide.
- **White blood cells** help defend against pathogens.
- **Platelets** are involved in clotting, which helps stop bleeding.
- **Plasma** is the liquid part and transports carbon dioxide, nutrients, hormones, wastes and heat.""",
    body_zh=r"""血液是运输系统，也参与防御和止血。第 8 阶段要能把四种主要成分和功能对上号。

血浆是淡黄色的液体，占血液的很大一部分。养分、激素、尿素等废物以及不少二氧化碳溶解在血浆里被运送；血浆也帮助把热带到全身。

红细胞数量很多，含有血红蛋白，能与氧气结合，把氧气从肺运到组织。白细胞种类不同，但共同作用是识别和对抗病原体。血小板在血管损伤时参与形成血凝块，减少失血。

不要把功能记串：运输氧气主要是红细胞，不是血小板；凝血不是红细胞的主要工作。

## 例题

为什么失血过多既会影响供氧，也可能影响止血和抗感染？

**解：** 失血会同时减少红细胞、血小板、白细胞和血浆，因此氧气运输、凝血和防御都可能被削弱。""",
    body_en=r"""Blood is a transport system, and it also helps with defence and clotting. At Stage 8 you should match the four main components to their functions.

Plasma is a pale yellow liquid and makes up a large part of blood. Nutrients, hormones, wastes such as urea, and a good deal of carbon dioxide are carried dissolved in plasma; plasma also helps carry heat around the body.

Red blood cells are very numerous and contain haemoglobin, which binds oxygen and carries it from the lungs to the tissues. White blood cells differ in type, but together they identify and attack pathogens. Platelets help form a clot when a vessel is damaged, so less blood is lost.

Do not swap the functions: oxygen transport is mainly the job of red cells, not platelets; clotting is not the main job of red cells.

## Worked example

Why can severe blood loss affect oxygen supply, clotting and defence against infection?

**Solution:** Blood loss reduces red cells, platelets, white cells and plasma together, so oxygen transport, clotting and defence can all be weakened.""",
    diff_zh="""- **把氧气运输记成血小板的功能。** 氧气主要靠红细胞。
- **以为血浆“什么都不运”。** 血浆运输许多溶解的物质和热。
- **把白细胞说成只运输氧气。** 白细胞的关键作用是防御。""",
    diff_en="""- **Giving oxygen transport to platelets.** Oxygen is carried mainly by red cells.
- **Thinking plasma carries nothing.** Plasma transports many dissolved substances and heat.
- **Saying white cells only carry oxygen.** Their key role is defence.""",
    questions=[
        dict(type="mcq", stem_zh="主要负责运输氧气的是？", stem_en="Oxygen is transported mainly by:",
             answer="a", exp_zh="红细胞含血红蛋白，主要运输氧气。", exp_en="Red blood cells contain haemoglobin and mainly transport oxygen.",
             options=opts(("红细胞", "red blood cells"), ("血小板", "platelets"), ("只有白细胞", "white blood cells only"), ("只有韧带", "ligaments only"))),
        dict(type="mcq", stem_zh="血小板的主要功能是？", stem_en="The main function of platelets is:",
             answer="c", exp_zh="血小板参与凝血、帮助止血。", exp_en="Platelets are involved in clotting, which helps stop bleeding.",
             options=opts(("进行有氧呼吸的全部步骤", "carrying out every step of aerobic respiration"),
                          ("阻挡肺泡与血液接触", "stopping alveoli contacting blood"),
                          ("参与凝血", "being involved in clotting"),
                          ("把二氧化碳变成氧气", "turning carbon dioxide into oxygen"))),
        dict(type="mcq", stem_zh="白细胞的主要功能是？", stem_en="The main function of white blood cells is to:",
             answer="b", exp_zh="白细胞帮助抵御病原体。", exp_en="White blood cells help defend against pathogens.",
             options=opts(("把骨头拉向关节", "pull bones towards joints"), ("抵御病原体", "defend against pathogens"),
                          ("只运输氧气", "transport oxygen only"), ("形成血浆蛋白以外的全部骨骼", "form the entire skeleton besides plasma proteins"))),
        dict(type="short", stem_zh="血浆运输哪些物质？举出至少两项。", stem_en="Name at least two things transported by plasma.",
             answer="nutrients and hormones",
             accepted=["nutrients and hormones", "carbon dioxide and nutrients", "hormones and urea", "heat and nutrients",
                       "养分和激素", "二氧化碳和养分", "激素和尿素", "热和养分", "养分、废物", "二氧化碳、养分、激素"],
             answer_zh="例如养分、激素、二氧化碳、废物或热。", answer_en="For example nutrients, hormones, carbon dioxide, wastes or heat.",
             exp_zh="血浆是液体部分，运输许多溶解的物质和热。", exp_en="Plasma is the liquid part and carries many dissolved substances and heat."),
        dict(type="mcq", stem_zh="血液的液体部分称为？", stem_en="The liquid part of blood is called:",
             answer="d", exp_zh="液体部分是血浆。", exp_en="The liquid part is plasma.",
             options=opts(("肺泡", "an alveolus"), ("肌腱", "a tendon"), ("栖息地", "a habitat"), ("血浆", "plasma"))),
        dict(type="mcq", stem_zh="下列配对正确的是？", stem_en="Which pairing is correct?",
             answer="a", exp_zh="红细胞—运氧；白细胞—防御；血小板—凝血；血浆—运输溶解物质。", exp_en="Red cells—oxygen; white cells—defence; platelets—clotting; plasma—dissolved substances.",
             options=opts(("红细胞运输氧气，血小板参与凝血", "red cells transport oxygen; platelets help in clotting"),
                          ("血小板是主要运氧细胞，红细胞只负责凝血", "platelets are the main oxygen carriers; red cells only clot"),
                          ("血浆不能运输任何物质", "plasma cannot transport anything"),
                          ("白细胞只存在于植物体内", "white cells exist only in plants"))),
    ],
)

# ----- 8Bs.03 -----
L(
    id="biology-8Bs-3",
    title_zh="呼吸系统与气体交换", title_en="The respiratory system and gas exchange",
    obj_zh="本节你将学会描述呼吸系统的主要结构，并说明气体交换在哪里发生、交换的是哪些气体。",
    obj_en="This lesson you will describe the main parts of the respiratory system and state where gas exchange happens and which gases are exchanged.",
    kp_zh="""- 空气经鼻或口、气管、支气管到达肺中的**肺泡**。
- **气体交换**主要在肺泡与血液之间进行：氧气进入血液，二氧化碳离开血液。
- 呼吸运动（胸廓和膈肌的运动）使空气进出肺，它本身不是细胞内的呼吸作用。
- 气管有软骨支撑，以保持气道畅通。
- 第 8 阶段要把“呼吸运动 / 通气”和“细胞里的呼吸作用”分开，下一节和有氧呼吸课还会强调。""",
    kp_en="""- Air travels through the nose or mouth, the trachea and bronchi to the **alveoli** in the lungs.
- **Gas exchange** happens mainly between the alveoli and the blood: oxygen enters the blood and carbon dioxide leaves it.
- Ventilation (movements of the ribcage and diaphragm) moves air in and out of the lungs; that is not the same as respiration inside cells.
- Cartilage supports the trachea and helps keep the airway open.
- At Stage 8, keep **ventilation** separate from **respiration** in cells; later lessons return to this.""",
    body_zh=r"""呼吸系统的任务是把空气送到能进行气体交换的表面，并把用过的气体带走。气体交换的主要场所是肺泡：数量极多，使表面积很大。

吸气时，胸廓扩大、膈肌下降，肺内气压降低，空气进入。呼气时相反。这是通气，目的是不断更新肺泡里的空气，使氧气浓度保持较高、二氧化碳浓度保持较低，有利于扩散。

进入血液的氧气会被红细胞运走，组织产生的二氧化碳则被带回肺泡呼出。不要把“呼吸运动”说成“葡萄糖与氧气在肺泡里反应生成能量”——那是细胞里的有氧呼吸，场所主要不在肺泡腔。

## 例题

气管被食物堵住时，为什么会立刻变得危险？

**解：** 空气无法到达肺泡，气体交换不能正常进行，身体得不到足够氧气，也无法有效排出二氧化碳。""",
    body_en=r"""The respiratory system’s job is to bring air to a surface where gas exchange can happen, and to carry used air away. The main site of gas exchange is the alveoli: there are a great many of them, so the surface area is very large.

When you inhale, the ribcage expands and the diaphragm moves down, pressure in the lungs falls, and air enters. The opposite happens when you exhale. This ventilation continually refreshes the air in the alveoli so that oxygen stays relatively high and carbon dioxide relatively low, which favours diffusion.

Oxygen that enters the blood is carried away by red cells; carbon dioxide from the tissues is brought back to the alveoli and exhaled. Do not describe ventilation as “glucose and oxygen reacting in the air space of an alveolus to release energy” — that is aerobic respiration inside cells, not in the alveolar cavity.

## Worked example

Why is a blocked trachea immediately dangerous?

**Solution:** Air cannot reach the alveoli, so gas exchange cannot occur properly. The body does not receive enough oxygen and cannot remove carbon dioxide effectively.""",
    diff_zh="""- **把通气和细胞呼吸混为一谈。** 通气是空气进出肺；呼吸作用在细胞中释放能量。
- **以为气体交换发生在气管中部。** 主要场所是肺泡。
- **说氧气在肺泡里被“烧掉”。** 氧气进入血液后，在组织细胞中参与呼吸作用。""",
    diff_en="""- **Mixing up ventilation and cellular respiration.** Ventilation moves air in and out; respiration releases energy in cells.
- **Placing gas exchange in the middle of the trachea.** The main site is the alveoli.
- **Saying oxygen is “burned” in the alveolar air space.** Oxygen enters the blood and is used in tissue cells.""",
    questions=[
        dict(type="mcq", stem_zh="气体交换的主要场所是？", stem_en="The main site of gas exchange is the:",
             answer="c", exp_zh="气体交换主要发生在肺泡与血液之间。", exp_en="Gas exchange happens mainly between the alveoli and the blood.",
             options=opts(("肌腱", "tendons"), ("胃", "stomach"), ("肺泡", "alveoli"), ("皮肤上的每根头发", "every hair on the skin"))),
        dict(type="mcq", stem_zh="在肺泡处，通常发生的气体方向是？", stem_en="At the alveoli, the usual direction of the gases is:",
             answer="a", exp_zh="氧气进入血液，二氧化碳离开血液进入肺泡。", exp_en="Oxygen enters the blood; carbon dioxide leaves the blood and enters the alveoli.",
             options=opts(("氧气进入血液，二氧化碳离开血液", "oxygen enters the blood; carbon dioxide leaves the blood"),
                          ("两者都只进不出", "both gases only enter and never leave"),
                          ("二氧化碳进入血液，氧气全部留在气管", "carbon dioxide enters the blood and all oxygen stays in the trachea"),
                          ("气体交换只在关节处发生", "gas exchange happens only at joints"))),
        dict(type="mcq", stem_zh="胸廓和膈肌的运动主要是为了？", stem_en="Movements of the ribcage and diaphragm are mainly for:",
             answer="b", exp_zh="这是通气，使空气进出肺。", exp_en="This is ventilation, moving air in and out of the lungs.",
             options=opts(("在肺泡腔内完成全部有氧呼吸", "completing all of aerobic respiration in the alveolar cavity"),
                          ("使空气进出肺（通气）", "moving air in and out of the lungs (ventilation)"),
                          ("制造红细胞", "making red blood cells"),
                          ("连接骨与骨", "connecting bone to bone"))),
        dict(type="short", stem_zh="通气（呼吸运动）和细胞里的呼吸作用有什么不同？", stem_en="How does ventilation differ from respiration in cells?",
             answer="ventilation moves air; respiration releases energy in cells",
             accepted=["ventilation moves air; respiration releases energy in cells", "ventilation is air in and out of lungs; respiration is in cells",
                       "通气是空气进出肺，呼吸作用在细胞中释放能量", "呼吸运动是通气，呼吸作用在细胞内"],
             answer_zh="通气是空气进出肺；呼吸作用在细胞中释放能量。",
             answer_en="Ventilation moves air in and out of the lungs; respiration releases energy in cells.",
             exp_zh="两个词在日常口语里常混用，课上要分开。", exp_en="Everyday speech often mixes the words; in class they must be kept apart."),
        dict(type="mcq", stem_zh="气管中的软骨有助于？", stem_en="Cartilage in the trachea helps to:",
             answer="d", exp_zh="软骨支撑气管，保持气道开放。", exp_en="Cartilage supports the trachea and helps keep the airway open.",
             options=opts(("进行光合作用", "carry out photosynthesis"), ("运输氧气替代红细胞", "transport oxygen in place of red cells"),
                          ("把血液变成血浆以外的固体骨", "turn blood into bone other than plasma"), ("保持气道畅通", "keep the airway open"))),
        dict(type="mcq", stem_zh="下列顺序正确的是？", stem_en="Which order is correct?",
             answer="a", exp_zh="空气经气管、支气管到达肺泡。", exp_en="Air travels via the trachea and bronchi to the alveoli.",
             options=opts(("气管 → 支气管 → 肺泡", "trachea → bronchi → alveoli"),
                          ("肺泡 → 胃 → 气管作为吸气路径", "alveoli → stomach → trachea as the path for inhaled air"),
                          ("关节 → 韧带 → 肺泡", "joint → ligament → alveolus"),
                          ("血浆 → 气管 → 体外作为吸气顺序", "plasma → trachea → outside as the inhalation sequence"))),
    ],
)

# ----- 8Bs.04 -----
L(
    id="biology-8Bs-4",
    title_zh="肺泡处的扩散", title_en="Diffusion of gases in the lungs",
    obj_zh="本节你将学会用扩散解释氧气和二氧化碳如何在肺泡与血液之间移动，并说明肺泡如何适合气体交换。",
    obj_en="This lesson you will use diffusion to explain how oxygen and carbon dioxide move between alveoli and blood, and how alveoli are adapted for gas exchange.",
    kp_zh="""- **扩散**是粒子从高浓度向低浓度的净移动。
- 肺泡里氧气浓度高于血液，氧气扩散进入血液；血液里二氧化碳浓度高于肺泡，二氧化碳扩散进入肺泡。
- 肺泡的适应：数量多（表面积大）、壁薄、湿润、周围有丰富的毛细血管。
- 通气不断更新空气，血液不断流走，有助于保持浓度差。
- 没有浓度差，净扩散就会减慢或停止。""",
    kp_en="""- **Diffusion** is the net movement of particles from a higher concentration to a lower concentration.
- Oxygen is at a higher concentration in the alveolar air than in the blood, so it diffuses into the blood; carbon dioxide is higher in the blood, so it diffuses into the alveoli.
- Adaptations of alveoli: very large number (large surface area), thin walls, a moist surface, and a rich capillary supply.
- Ventilation refreshes the air and blood flow carries gases away, which helps maintain the concentration gradient.
- If the gradient falls, net diffusion slows or stops.""",
    body_zh=r"""气体不会被肺泡“主动抓进血液”，它们顺着浓度差扩散。吸气后，肺泡中氧气较多、二氧化碳较少；从组织回来的血液则氧气较少、二氧化碳较多。于是氧气进入血液，二氧化碳进入肺泡，再被呼出。

肺泡长得“适合交换”：很多很小的气囊放大了总面积；壁极薄，扩散路程短；表面湿润，气体容易溶解后通过；外面包着毛细血管，使气体很快被运走或送来。如果通气不足或血液循环变差，浓度差变小，交换效率就会下降。

## 例题

为什么剧烈运动后呼吸会加快、加深？

**解：** 肌肉细胞呼吸作用加快，需要更多氧气、产生更多二氧化碳。加快通气能更快更新肺泡空气，保持较大的浓度差，使扩散持续高效进行。""",
    body_en=r"""Gases are not actively grabbed from the alveoli into the blood; they diffuse down a concentration gradient. After inhaling, alveolar air is relatively rich in oxygen and poor in carbon dioxide. Blood returning from the tissues is the other way round. So oxygen diffuses into the blood and carbon dioxide diffuses into the alveoli, then is exhaled.

Alveoli are adapted for this exchange: huge numbers give a large surface area; walls are very thin, so the diffusion path is short; the surface is moist, so gases can dissolve and cross; capillaries surround them so gases are carried away or delivered quickly. If ventilation or blood flow is poor, the gradient shrinks and exchange becomes less effective.

## Worked example

Why do you breathe faster and more deeply after hard exercise?

**Solution:** Muscle cells respire faster, so they need more oxygen and produce more carbon dioxide. Faster ventilation refreshes alveolar air more quickly, keeping a steeper concentration gradient so diffusion stays efficient.""",
    diff_zh="""- **说气体从低浓度走向高浓度。** 净扩散是从高到低。
- **把适应特征只写成“肺泡很大”而忘了“很多且壁薄”。**
- **忘记通气和血流对维持浓度差的作用。**""",
    diff_en="""- **Saying gases move from low to high concentration.** Net diffusion is from high to low.
- **Describing the adaptation only as “one huge alveolus”.** There are many, with thin walls.
- **Forgetting that ventilation and blood flow maintain the gradient.**""",
    diagram=D_ALV,
    questions=[
        dict(type="mcq", stem_zh="扩散是指粒子的净移动方向为？", stem_en="In diffusion, the net movement of particles is from:",
             answer="a", exp_zh="从高浓度到低浓度。", exp_en="From higher concentration to lower concentration.",
             options=opts(("高浓度到低浓度", "higher to lower concentration"), ("低浓度到高浓度", "lower to higher concentration"),
                          ("只在固体金属中发生", "solids metals only"), ("只从血浆到骨骼", "plasma to bone only"))),
        dict(type="mcq", stem_zh="肺泡中氧气进入血液，是因为？", stem_en="Oxygen enters the blood at the alveoli because:",
             answer="c", exp_zh="肺泡气中氧气浓度高于血液，氧气向低浓度处扩散。", exp_en="The oxygen concentration is higher in alveolar air than in the blood, so oxygen diffuses into the blood.",
             options=opts(("血液中氧气浓度更高", "the concentration is higher in the blood"),
                          ("氧气主动从低浓度被推到更高浓度", "oxygen is pushed from low to even higher concentration"),
                          ("肺泡气中氧气浓度高于血液", "the concentration is higher in the alveolar air than in the blood"),
                          ("血小板把氧气泵进骨头", "platelets pump oxygen into bones"))),
        dict(type="mcq", stem_zh="下列哪一项是肺泡适合气体交换的特征？", stem_en="Which is an adaptation of alveoli for gas exchange?",
             answer="b", exp_zh="壁薄、表面积大、湿润并有丰富毛细血管。", exp_en="Thin walls, a large surface area, a moist surface and a rich capillary supply.",
             options=opts(("壁极厚，以减慢扩散", "very thick walls, to slow diffusion"),
                          ("壁薄且总表面积大", "thin walls and a large total surface area"),
                          ("完全没有血液供应", "no blood supply at all"),
                          ("表面保持完全干燥且只有一个大气囊", "a completely dry surface and only one large air sac"))),
        dict(type="short", stem_zh="为什么通气有助于肺泡处的气体扩散？", stem_en="Why does ventilation help diffusion at the alveoli?",
             answer="it maintains the concentration gradient",
             accepted=["it maintains the concentration gradient", "it refreshes the air so oxygen stays high and CO2 stays low",
                       "维持浓度差", "更新空气，保持氧气高、二氧化碳低", "不断更新肺泡空气以保持浓度差"],
             answer_zh="通气更新肺泡空气，维持氧气高、二氧化碳低的浓度差。",
             answer_en="Ventilation refreshes alveolar air, keeping oxygen high and carbon dioxide low, so the gradient is maintained.",
             exp_zh="没有浓度差，净扩散就会减慢。", exp_en="Without a gradient, net diffusion slows."),
        dict(type="mcq", stem_zh="血液中的二氧化碳进入肺泡，是因为？", stem_en="Carbon dioxide enters the alveoli from the blood because:",
             answer="d", exp_zh="血液中二氧化碳浓度更高，向肺泡扩散。", exp_en="The concentration is higher in the blood, so it diffuses into the alveoli.",
             options=opts(("肺泡中二氧化碳浓度更高", "the concentration is higher in the alveoli"),
                          ("二氧化碳不能扩散", "carbon dioxide cannot diffuse"),
                          ("韧带把二氧化碳拉过去", "ligaments pull the carbon dioxide across"),
                          ("血液中二氧化碳浓度高于肺泡", "the concentration is higher in the blood than in the alveoli"))),
        dict(type="mcq", stem_zh="丰富的毛细血管有助于气体交换，是因为？", stem_en="A rich capillary supply helps gas exchange because:",
             answer="a", exp_zh="血液能迅速运走氧气、送来二氧化碳，有助于维持浓度差。", exp_en="Blood can carry oxygen away and bring carbon dioxide, helping to maintain the gradient.",
             options=opts(("气体可以被迅速运走或送来，维持浓度差", "gases can be carried away or delivered quickly, maintaining the gradient"),
                          ("毛细血管会把肺泡变成关节", "capillaries turn alveoli into joints"),
                          ("血液会阻止扩散", "blood prevents diffusion"),
                          ("这样肺泡壁就会变厚", "the alveolar walls then become thicker"))),
    ],
)

# ----- 8Bp.01 -----
L(
    id="biology-8Bp-1",
    title_zh="均衡饮食与营养素", title_en="A balanced diet and nutrients",
    obj_zh="本节你将学会说明什么是均衡饮食，并说出主要营养素的作用。",
    obj_en="This lesson you will explain what a balanced diet is and state the roles of the main nutrients.",
    kp_zh="""- **均衡饮食**提供适量的各类营养素、水和纤维，既不过少也不过量。
- **糖类（碳水化合物）**和**脂肪**是主要的能量来源；脂肪还帮助吸收某些维生素、构成细胞膜。
- **蛋白质**用于生长和修复。
- **维生素**和**矿物质**需要量较小，但缺乏会生病；**纤维**帮助肠道蠕动；**水**是各种反应和运输所必需。
- “均衡”不是只吃一种所谓健康食物，也不是吃得越多越好。""",
    kp_en="""- A **balanced diet** provides the right amounts of each type of nutrient, plus water and fibre — not too little and not too much.
- **Carbohydrates** and **fats** are the main energy sources; fats also help absorb some vitamins and form cell membranes.
- **Proteins** are used for growth and repair.
- **Vitamins** and **minerals** are needed in smaller amounts, but lack of them causes deficiency disease; **fibre** helps the gut move food; **water** is needed for reactions and transport.
- “Balanced” does not mean eating only one so-called healthy food, or eating as much as possible.""",
    body_zh=r"""身体不能只靠一种物质运转。均衡饮食的意思是：在一段时间内，各类营养素、水和纤维的摄入与需求大致匹配。

糖类是常见的即时能量来源；脂肪含能量更高，也可储存。蛋白质提供氨基酸，用于建造和修补细胞，例如肌肉和酶。维生素和矿物质种类多、需要量不大，但缺少某一种就可能出现缺乏症（例如缺少维生素 C 与坏血病有关）。纤维本身不是供能的主要营养素，却能帮助粪便通过肠道。水则参与运输和许多反应。

不同年龄、活动量和健康状况需要的能量和某些营养素不同，所以“一份标准餐”不能套用所有人，但各类都要有、分量要合适，这个原则是共同的。

## 例题

只吃大量水果、完全不摄入蛋白质，算均衡吗？

**解：** 不算。水果可提供维生素、纤维和一些糖类，但长期缺乏蛋白质会妨碍生长和修复。""",
    body_en=r"""The body cannot run on one substance alone. A balanced diet means that, over time, the intake of each type of nutrient, plus water and fibre, roughly matches what the body needs.

Carbohydrates are a common source of energy for immediate use; fats are more energy-dense and can be stored. Proteins provide amino acids for building and repairing cells, including muscle and enzymes. Vitamins and minerals are needed in smaller amounts, but a lack of one of them can cause a deficiency disease (for example, lack of vitamin C is linked with scurvy). Fibre is not a main energy nutrient, but it helps faeces move through the gut. Water is involved in transport and many reactions.

Energy and some nutrient needs change with age, activity and health, so one “standard meal” does not fit everyone. The shared idea is still that all the groups should be present in suitable amounts.

## Worked example

Is it balanced to eat large amounts of fruit and no protein at all?

**Solution:** No. Fruit can provide vitamins, fibre and some carbohydrate, but a long-term lack of protein would interfere with growth and repair.""",
    diff_zh="""- **把均衡理解成“吃得很少”或“只吃蔬菜”。** 关键是种类齐全、分量合适。
- **以为蛋白质的主要作用是供能。** 它主要用于生长和修复（也能供能，但不是首先要记的功能）。
- **忽略水和纤维。** 它们也是均衡饮食的一部分。""",
    diff_en="""- **Taking “balanced” to mean “eating very little” or “only vegetables”.** The point is the right range and the right amounts.
- **Treating protein as mainly an energy source.** Its first role to remember is growth and repair (it can also supply energy).
- **Leaving out water and fibre.** They are part of a balanced diet too.""",
    questions=[
        dict(type="mcq", stem_zh="蛋白质的主要作用是？", stem_en="The main role of protein is:",
             answer="b", exp_zh="蛋白质主要用于生长和修复。", exp_en="Protein is used mainly for growth and repair.",
             options=opts(("只运输氧气", "transporting oxygen only"), ("生长和修复", "growth and repair"),
                          ("替代所有水分", "replacing all water"), ("进行气体在肺泡外的扩散即可，无需饮食", "allowing diffusion outside alveoli so that diet is unnecessary"))),
        dict(type="mcq", stem_zh="均衡饮食的含义最接近？", stem_en="A balanced diet is closest to:",
             answer="a", exp_zh="适量提供各类营养素、水和纤维。", exp_en="Providing suitable amounts of each type of nutrient, plus water and fibre.",
             options=opts(("适量摄入各类营养素、水和纤维", "suitable amounts of each nutrient, plus water and fibre"),
                          ("只吃一种食物，越多越好", "eating as much as possible of one food only"),
                          ("完全不摄入脂肪和糖类", "cutting out all fat and carbohydrate"),
                          ("不需要水", "needing no water"))),
        dict(type="mcq", stem_zh="糖类和脂肪在饮食中的主要共同作用是？", stem_en="A main shared role of carbohydrate and fat in the diet is to:",
             answer="c", exp_zh="两者都是重要的能量来源。", exp_en="Both are important sources of energy.",
             options=opts(("只构成韧带", "form ligaments only"), ("代替白细胞", "replace white blood cells"),
                          ("提供能量", "provide energy"), ("阻止所有扩散", "stop all diffusion"))),
        dict(type="short", stem_zh="纤维在饮食中的一种作用是什么？", stem_en="Give one role of fibre in the diet.",
             answer="helps food move through the gut",
             accepted=["helps food move through the gut", "helps prevent constipation", "aids peristalsis",
                       "帮助肠道蠕动", "帮助粪便通过肠道", "预防便秘"],
             answer_zh="帮助食物和粪便在肠道中移动。", answer_en="It helps food and faeces move through the gut.",
             exp_zh="纤维不是主要的供能营养素，但对肠道功能重要。", exp_en="Fibre is not a main energy nutrient, but it matters for the gut."),
        dict(type="mcq", stem_zh="维生素和矿物质的特点是？", stem_en="Vitamins and minerals are typically:",
             answer="d", exp_zh="需要量较小，但缺乏可能导致缺乏症。", exp_en="Needed in smaller amounts, but a lack can cause deficiency disease.",
             options=opts(("完全不需要", "not needed at all"), ("可以完全替代水", "able to replace water completely"),
                          ("只存在于金属矿中，不能出现在食物里", "found only in metal ores, never in food"),
                          ("需要量较小，缺乏时仍可能引起疾病", "needed in smaller amounts, but a lack can still cause disease"))),
        dict(type="mcq", stem_zh="只吃大量某一种“健康食物”、完全缺少蛋白质，算均衡吗？", stem_en="Is it balanced to eat large amounts of one “healthy” food and no protein?",
             answer="a", exp_zh="种类不全就不均衡，长期缺蛋白质会影响生长和修复。", exp_en="Missing a whole group means it is not balanced; lack of protein affects growth and repair.",
             options=opts(("不算，因为种类不全、蛋白质不足", "no, because a group is missing and protein is lacking"),
                          ("算，因为吃得足够多", "yes, because the amount eaten is large"),
                          ("算，因为健康食物可以代替所有营养素", "yes, because one healthy food can replace every nutrient"),
                          ("不算，因为均衡饮食禁止所有水果", "no, because a balanced diet bans all fruit"))),
    ],
)

# ----- 8Bp.02 -----
L(
    id="biology-8Bp-2",
    title_zh="能量储存与食物", title_en="Energy stores and food",
    obj_zh="本节你将学会说明食物是能量的储存，以及不同食物提供的能量可以不同。",
    obj_en="This lesson you will explain that food is an energy store and that different foods can provide different amounts of energy.",
    kp_zh="""- 食物中的化学能可以被身体用于生命活动。
- 单位质量食物所含能量并不相同：脂肪通常比同样质量的糖类或蛋白质提供更多能量。
- 能量需要与活动量、生长等有关：摄入长期远高于消耗，多余能量可能以脂肪形式储存。
- 实验室可用燃烧食物加热水的简单方法比较能量（注意这是粗略比较，有热量损失）。
- 有能量的食物仍需作为均衡饮食的一部分来看，不能只比“热量高低”。""",
    kp_en="""- Chemical energy in food can be used by the body for life processes.
- Energy per unit mass is not the same for every food: fat usually provides more energy than the same mass of carbohydrate or protein.
- Energy need depends on activity and growth; if intake stays much higher than use, extra energy may be stored as fat.
- In the laboratory, burning a food to heat water is a simple way to compare energy (it is rough, because some heat is lost).
- Energy content still has to be seen as part of a balanced diet, not as the only number that matters.""",
    body_zh=r"""我们走路、保持体温、建造新细胞，都需要能量。这些能量来自食物中的化学能储存。身体通过呼吸作用把其中一部分转移出来，供生命活动使用。

不同食物“含多少能量”可以差很多。同样质量下，脂肪通常比糖类含有更多能量。这就是为什么油炸食品往往能量很高。但高能量不等于“更好”：如果长期摄入超过消耗，多余的能量会储存起来，体内脂肪增加。活动量大、正在生长的人通常需要更多能量。

课堂里有时会燃烧一块食物来加热试管里的水，用水温升髙来比较相对能量。结果只是近似，因为不少热量散失到空气中。

## 例题

为什么比较两种零食时，只看“谁的能量更高”是不够的？

**解：** 还要看脂肪、糖、盐、蛋白质和纤维等是否合适，以及一份的质量和你真正需要多少能量。""",
    body_en=r"""Walking, keeping warm and building new cells all need energy. That energy comes from chemical stores in food. Respiration transfers some of it so that life processes can go on.

Foods differ a lot in how much energy they contain. For the same mass, fat usually provides more energy than carbohydrate. That is why fried foods are often energy-dense. High energy is not automatically “better”: if intake stays above use, the extra may be stored and body fat can increase. People who are very active or still growing usually need more energy.

In class you may burn a piece of food to heat water in a tube and use the temperature rise to compare relative energy. The result is only approximate, because a good deal of heat is lost to the air.

## Worked example

Why is it not enough, when comparing two snacks, to ask only “which has more energy”?

**Solution:** You also need to consider fat, sugar, salt, protein and fibre, the mass of a portion, and how much energy you actually need.""",
    diff_zh="""- **以为所有食物单位质量能量都一样。** 脂肪通常更高。
- **把“能量高”直接等于“更健康”。**
- **把课堂燃烧实验当成精确的热量计结果。** 会有热量损失。""",
    diff_en="""- **Thinking every food has the same energy per gram.** Fat is usually higher.
- **Equating “high energy” with “healthier”.**
- **Treating a class burning experiment as a precise calorimeter result.** Heat is lost.""",
    diagram=D_FOOD,
    questions=[
        dict(type="mcq", stem_zh="同样质量下，通常提供能量最多的是？", stem_en="For the same mass, which usually provides the most energy?",
             answer="b", exp_zh="脂肪单位质量的能量通常高于糖类或蛋白质。", exp_en="Fat usually provides more energy per unit mass than carbohydrate or protein.",
             options=opts(("水", "water"), ("脂肪", "fat"), ("纤维本身作为最主要供能物质", "fibre as the main energy source"), ("空气", "air"))),
        dict(type="mcq", stem_zh="食物对人体的一个关键作用是提供？", stem_en="A key role of food for the body is to provide:",
             answer="a", exp_zh="食物储存化学能，可供生命活动使用。", exp_en="Food stores chemical energy that can be used for life processes.",
             options=opts(("生命活动所需的能量", "energy for life processes"), ("只提供无法使用的惰性沙子", "only inert sand that cannot be used"),
                          ("肺泡壁增厚所需的软骨", "cartilage needed to thicken alveolar walls"), ("替代所有氧气使呼吸不再需要", "a substitute for all oxygen so respiration is unnecessary"))),
        dict(type="mcq", stem_zh="长期摄入能量远高于消耗，可能发生？", stem_en="If energy intake stays much higher than energy use, a likely result is:",
             answer="c", exp_zh="多余能量可能以脂肪形式储存。", exp_en="Extra energy may be stored as fat.",
             options=opts(("体内能量储存自动变为零", "body energy stores automatically fall to zero"),
                          ("蛋白质不再具有任何功能", "protein loses all function"),
                          ("多余能量可能以脂肪形式储存", "extra energy may be stored as fat"),
                          ("扩散会反向从低到高且永久停止通气", "diffusion permanently reverses from low to high and ventilation stops"))),
        dict(type="short", stem_zh="课堂用燃烧食物加热水来比较能量时，为什么结果往往偏低？", stem_en="In a class experiment that burns food to heat water, why is the energy value often too low?",
             answer="heat is lost to the surroundings",
             accepted=["heat is lost to the surroundings", "not all heat goes into the water", "energy lost to the air",
                       "热量散失到周围", "不是所有热都进入水中", "有热量损失"],
             answer_zh="部分热量会散失到周围空气中，没有全部用于升高水温。",
             answer_en="Some heat is lost to the surrounding air and does not all go into raising the water temperature.",
             exp_zh="这是粗略比较，不是精密测量。", exp_en="It is a rough comparison, not a precise measurement."),
        dict(type="mcq", stem_zh="活动量很大的人，通常需要？", stem_en="A very active person usually needs:",
             answer="d", exp_zh="活动耗能更多，通常需要更多能量摄入（仍要保持均衡）。", exp_en="Activity uses more energy, so intake usually needs to be higher (while still remaining balanced).",
             options=opts(("完全不需要能量", "no energy at all"), ("只需要纤维，不需要任何其他营养", "fibre only, and no other nutrients"),
                          ("比静止时更少的能量", "less energy than when resting"), ("比活动少时更多的能量（并仍要均衡）", "more energy than when less active, while still eating a balanced diet"))),
        dict(type="mcq", stem_zh="比较两种食物时，只看能量高低是否足够判断哪一种更适合？", stem_en="When comparing two foods, is energy content alone enough to decide which is more suitable?",
             answer="a", exp_zh="还要考虑其他营养素、份量和需要。", exp_en="Other nutrients, portion size and need also matter.",
             options=opts(("不够，还要看其他营养素、份量和需要", "no: other nutrients, portion size and need also matter"),
                          ("足够，能量最高的一定最好", "yes: the highest-energy food is always best"),
                          ("足够，能量最低的一定最好", "yes: the lowest-energy food is always best"),
                          ("食物不含能量，所以不必比较", "food contains no energy, so comparison is unnecessary"))),
    ],
)

# ----- 8Bp.03 -----
L(
    id="biology-8Bp-3",
    title_zh="生活方式与健康（饮食与吸烟）", title_en="Lifestyle and health (diet and smoking)",
    obj_zh="本节你将学会说明不均衡饮食和吸烟如何影响健康，并能用结构与功能的知识解释部分危害。",
    obj_en="This lesson you will explain how an unbalanced diet and smoking can affect health, using what you know about structure and function.",
    kp_zh="""- 长期能量摄入过多、加上活动不足，与超重及一些心脏和代谢问题的风险上升有关。
- 饮食中某些脂肪和盐过多，也可能增加心血管疾病的风险。
- **吸烟**会把有害物质带入气道和血液。焦油可损害肺泡和纤毛，使气体交换和清洁气道变难。
- 一氧化碳能与血红蛋白结合，减少氧气运输；尼古丁可使血管收缩、加重心脏负担。
- 健康选择不能只用“某一天吃多了”或“只吸过一次”来理解，要看长期习惯。""",
    kp_en="""- Long-term energy intake well above use, with little activity, is linked with overweight and a higher risk of some heart and metabolic problems.
- A diet too high in some fats and in salt may also raise the risk of cardiovascular disease.
- **Smoking** takes harmful substances into the airways and blood. Tar can damage alveoli and cilia, making gas exchange and cleaning the airways harder.
- Carbon monoxide can bind to haemoglobin and reduce oxygen transport; nicotine can narrow blood vessels and add strain to the heart.
- Health choices are about long-term habits, not a single heavier meal or a single cigarette taken in isolation.""",
    body_zh=r"""生活方式里，饮食和吸烟对八年级来说是两条最常讨论的线索，因为它们直接连到已经学过的血液、肺泡和能量。

饮食方面，问题往往出在“长期不均衡”：能量持续过多、某些脂肪或盐过多，或某些营养素长期缺乏。风险是逐渐累积的，不是吃一顿油腻饭就立刻等于某种疾病，但习惯很重要。

吸烟的危害可以用结构来解释。焦油会黏附并损害肺泡，减小气体交换的有效面积，还可能麻痹清除尘粒的纤毛。一氧化碳抢占血红蛋白上的位置，使氧气运输变差。尼古丁影响循环系统，使心脏需要更费力地工作。这些变化合在一起，让活动和运动都更吃力，并增加疾病风险。

## 例题

为什么一氧化碳会使人感到更容易气喘或运动困难？

**解：** 一氧化碳与血红蛋白结合，减少可运输的氧气，组织得到的氧不足，尤其在需要更多氧的运动时更明显。""",
    body_en=r"""For Year 8, diet and smoking are the two lifestyle threads most often discussed, because they connect directly to blood, alveoli and energy.

On diet, the issue is usually a long-term imbalance: energy well above use for a long time, too much of some fats or salt, or a long-term lack of a nutrient. Risk builds up; one heavier meal does not instantly equal a disease, but habits matter.

The harms of smoking can be explained with structure. Tar can coat and damage alveoli, reducing the effective surface for gas exchange, and it can also affect the cilia that help clean the airways. Carbon monoxide binds to haemoglobin and reduces oxygen transport. Nicotine affects the circulation and can make the heart work harder. Together, these changes make activity more difficult and raise the risk of disease.

## Worked example

Why can carbon monoxide make someone feel breathless or find exercise harder?

**Solution:** Carbon monoxide binds to haemoglobin, so less oxygen is transported. Tissues receive less oxygen, which is especially noticeable when more oxygen is needed during exercise.""",
    diff_zh="""- **把“风险增加”说成“吃一口就必然生病”。** 要区分短期与长期。
- **只会说吸烟“不好”，说不出焦油、一氧化碳或尼古丁与结构的联系。**
- **忘记一氧化碳影响的是氧气运输。**""",
    diff_en="""- **Turning “higher risk” into “one mouthful always causes disease”.** Keep short-term and long-term distinct.
- **Only saying smoking is “bad” without linking tar, carbon monoxide or nicotine to structure.**
- **Forgetting that carbon monoxide affects oxygen transport.**""",
    questions=[
        dict(type="mcq", stem_zh="一氧化碳对血液运输氧气的影响是？", stem_en="Carbon monoxide affects oxygen transport by:",
             answer="b", exp_zh="它与血红蛋白结合，减少可运输的氧气。", exp_en="It binds to haemoglobin and reduces the oxygen that can be carried.",
             options=opts(("增加血浆中的氧气至无限", "raising oxygen in plasma without limit"),
                          ("与血红蛋白结合，减少氧气运输", "binding to haemoglobin and reducing oxygen transport"),
                          ("把红细胞变成血小板", "turning red cells into platelets"),
                          ("只损害韧带，不影响血液", "damaging ligaments only, not the blood"))),
        dict(type="mcq", stem_zh="焦油损害肺泡，主要影响？", stem_en="Tar damaging the alveoli mainly affects:",
             answer="a", exp_zh="有效气体交换面积减小，交换变难。", exp_en="The effective surface for gas exchange is reduced, so exchange is harder.",
             options=opts(("气体交换", "gas exchange"), ("只影响头发颜色", "hair colour only"),
                          ("肌腱改连到气管", "tendons attaching instead to the trachea"), ("使扩散必须从低浓度到高浓度", "forcing diffusion to run from low to high concentration"))),
        dict(type="mcq", stem_zh="长期能量摄入远高于消耗，主要相关风险是？", stem_en="A long-term energy intake well above use is mainly linked with:",
             answer="c", exp_zh="与超重及一些心脏和代谢问题的风险上升有关。", exp_en="It is linked with overweight and a higher risk of some heart and metabolic problems.",
             options=opts(("肺泡数目瞬间增加十倍且无任何风险", "an instant ten-fold increase in alveoli and no risk"),
                          ("蛋白质功能完全消失于一天之内", "protein function vanishing completely in a single day"),
                          ("超重及相关健康风险上升", "overweight and a higher related health risk"),
                          ("气候变为天气", "climate turning into weather"))),
        dict(type="short", stem_zh="写出吸烟中一种有害物质及其一种危害。", stem_en="Name one harmful substance in cigarette smoke and one effect it has.",
             answer="carbon monoxide reduces oxygen transport",
             accepted=["carbon monoxide reduces oxygen transport", "tar damages alveoli", "nicotine strains the heart", "tar affects cilia",
                       "一氧化碳减少氧气运输", "焦油损害肺泡", "尼古丁加重心脏负担", "焦油影响纤毛"],
             answer_zh="例如一氧化碳减少氧气运输，或焦油损害肺泡。",
             answer_en="For example, carbon monoxide reduces oxygen transport, or tar damages alveoli.",
             exp_zh="能把物质和结构/功能联系起来即可。", exp_en="Link the substance to a structure or function."),
        dict(type="mcq", stem_zh="尼古丁对循环系统的一种影响是？", stem_en="One effect of nicotine on the circulation is that it can:",
             answer="d", exp_zh="尼古丁可使血管收缩，加重心脏负担。", exp_en="Nicotine can narrow blood vessels and add strain to the heart.",
             options=opts(("把血液全部变成纯氧气", "turn all of the blood into pure oxygen"),
                          ("使血红蛋白只能运输纤维", "make haemoglobin transport only fibre"),
                          ("完全无害于心脏", "be completely harmless to the heart"),
                          ("使血管收缩，心脏工作更费力", "narrow blood vessels so the heart has to work harder"))),
        dict(type="mcq", stem_zh="关于饮食与健康，较准确的说法是？", stem_en="A fair statement about diet and health is:",
             answer="a", exp_zh="长期习惯更重要，不能把一餐绝对化，但风险可以累积。", exp_en="Long-term habits matter more than one meal, but risk can still build up.",
             options=opts(("长期习惯很重要，风险可以累积，但不能把一餐说成必然致病", "long-term habits matter and risk can build, but one meal is not certain disease"),
                          ("只要有一餐油腻就必然立即患病", "one heavier meal always causes immediate disease"),
                          ("饮食与健康无关", "diet is unrelated to health"),
                          ("只吃能量最高的食物一定最健康", "the highest-energy diet is always the healthiest"))),
    ],
)

# ----- 8Bp.04 -----
L(
    id="biology-8Bp-4",
    title_zh="有氧呼吸", title_en="Aerobic respiration",
    obj_zh="本节你将学会写出有氧呼吸的文字方程式，并把它与通气、气体交换区分开来。",
    obj_en="This lesson you will write the word equation for aerobic respiration and keep it distinct from ventilation and gas exchange.",
    kp_zh="""- **有氧呼吸**在有氧气时把食物中的化学能转移出来，供生命活动使用。
- 文字方程式：葡萄糖 $+$ 氧气 $\\rightarrow$ 二氧化碳 $+$ 水（并释放能量）。
- 场所在**细胞**中（后续课程会提到线粒体），不是在肺泡的空腔里完成整个反应。
- 氧气由呼吸系统和血液供给，二氧化碳由血液带回肺泡排出。
- 不要把有氧呼吸说成“吸气这个动作”。""",
    kp_en="""- **Aerobic respiration** transfers chemical energy from food, in the presence of oxygen, so that life processes can go on.
- Word equation: glucose $+$ oxygen $\\rightarrow$ carbon dioxide $+$ water (and energy is released).
- It takes place in **cells** (later courses mention mitochondria), not as the whole reaction happening in the air space of an alveolus.
- The respiratory system and blood supply the oxygen; blood carries carbon dioxide back to the alveoli to be exhaled.
- Do not use “aerobic respiration” to mean the act of breathing in.""",
    body_zh=r"""有氧呼吸是细胞获取可用能量的主要方式之一。葡萄糖来自食物中的糖类等，氧气来自气体交换。反应的产物是二氧化碳和水，同时把能量转移出来，供肌肉收缩、保持体温和建造新物质等使用。

文字方程式要写对方向和名称：

葡萄糖 $+$ 氧气 $\rightarrow$ 二氧化碳 $+$ 水

能量是释放出来的，通常不作为“物质”写在方程式的某一侧，但你必须知道这个过程会释放能量。运动时呼吸加快，是因为细胞需要更多氧气、产生更多二氧化碳，通气必须跟上，而不是因为“呼吸运动本身等于有氧呼吸”。

## 例题

一个人屏住呼吸时，有氧呼吸会立刻完全停止吗？

**解：** 不会立刻完全停止。体内血液和肺部还暂存一些氧气，细胞可继续呼吸一段时间；但氧气很快会不够，不能长时间这样。""",
    body_en=r"""Aerobic respiration is one of the main ways cells obtain useful energy. Glucose comes from carbohydrate in food; oxygen comes from gas exchange. The products are carbon dioxide and water, and energy is transferred for muscle contraction, keeping warm and building new substances.

Get the names and the direction right in the word equation:

glucose $+$ oxygen $\rightarrow$ carbon dioxide $+$ water

Energy is released; it is not usually written as a substance on one side of the word equation, but you must know that the process releases energy. You breathe faster during exercise because cells need more oxygen and make more carbon dioxide, so ventilation must keep up — not because the chest movement itself is aerobic respiration.

## Worked example

If a person holds their breath, does aerobic respiration stop immediately?

**Solution:** Not immediately. Some oxygen remains in the blood and lungs, so cells can continue for a short time. That store does not last long, so you cannot hold your breath for very long.""",
    diff_zh="""- **把通气叫成有氧呼吸。** 一个是空气进出肺，一个是细胞内的反应。
- **把葡萄糖或氧气写到生成物一侧。**
- **以为反应发生在气管空腔里。** 它发生在细胞中。""",
    diff_en="""- **Calling ventilation aerobic respiration.** One moves air in and out of the lungs; the other is a reaction in cells.
- **Putting glucose or oxygen on the product side.**
- **Placing the reaction in the air space of the trachea.** It happens in cells.""",
    questions=[
        dict(type="short", stem_zh="写出有氧呼吸的文字方程式。", stem_en="Write the word equation for aerobic respiration.",
             answer="glucose + oxygen -> carbon dioxide + water",
             accepted=["glucose + oxygen -> carbon dioxide + water", "glucose + oxygen → carbon dioxide + water",
                       "葡萄糖+氧气→二氧化碳+水", "葡萄糖＋氧气→二氧化碳＋水", "葡萄糖 + 氧气 → 二氧化碳 + 水"],
             answer_zh="葡萄糖 $+$ 氧气 $\\rightarrow$ 二氧化碳 $+$ 水",
             answer_en="glucose $+$ oxygen $\\rightarrow$ carbon dioxide $+$ water",
             exp_zh="能量被释放，但物质名称按左反应物、右生成物来写。", exp_en="Energy is released; write the substances with reactants on the left and products on the right."),
        dict(type="mcq", stem_zh="有氧呼吸主要发生在？", stem_en="Aerobic respiration takes place mainly in:",
             answer="c", exp_zh="它发生在细胞中，不是在肺泡空腔里完成整个反应。", exp_en="It takes place in cells, not as the whole reaction in the alveolar air space.",
             options=opts(("只在肺泡的空腔中", "the air space of the alveoli only"), ("只在气管中", "the trachea only"),
                          ("细胞中", "cells"), ("关节腔内替代肌肉收缩", "the joint cavity, replacing muscle contraction"))),
        dict(type="mcq", stem_zh="有氧呼吸释放的能量可用来？", stem_en="Energy released by aerobic respiration can be used to:",
             answer="a", exp_zh="供生命活动使用，例如肌肉收缩和保持体温。", exp_en="Power life processes, such as muscle contraction and keeping warm.",
             options=opts(("供生命活动使用，例如肌肉收缩", "power life processes such as muscle contraction"),
                          ("把扩散永远变成从低到高", "make diffusion run from low to high for ever"),
                          ("停止血液运输", "stop blood transport"),
                          ("把氧气变成葡萄糖作为唯一生成物", "turn oxygen into glucose as the only product"))),
        dict(type="mcq", stem_zh="下列哪一项正确区分了通气和有氧呼吸？", stem_en="Which statement correctly separates ventilation and aerobic respiration?",
             answer="d", exp_zh="通气是空气进出肺；有氧呼吸是细胞中利用氧释放能量的反应。", exp_en="Ventilation moves air in and out of the lungs; aerobic respiration is the reaction in cells that uses oxygen and releases energy.",
             options=opts(("二者是完全相同的过程", "they are exactly the same process"),
                          ("有氧呼吸是胸廓运动，通气是葡萄糖分解", "respiration is rib movement; ventilation is the breakdown of glucose"),
                          ("通气只在细胞内发生", "ventilation happens only inside cells"),
                          ("通气是空气进出肺，有氧呼吸在细胞中释放能量", "ventilation moves air in and out; aerobic respiration releases energy in cells"))),
        dict(type="mcq", stem_zh="运动时呼吸加快，主要是因为细胞？", stem_en="You breathe faster during exercise mainly because cells:",
             answer="b", exp_zh="呼吸作用加快，需要更多氧气、产生更多二氧化碳。", exp_en="They respire faster, so they need more oxygen and produce more carbon dioxide.",
             options=opts(("停止了有氧呼吸", "have stopped aerobic respiration"),
                          ("需要更多氧气并产生更多二氧化碳", "need more oxygen and produce more carbon dioxide"),
                          ("不再需要葡萄糖", "no longer need glucose"),
                          ("把肺泡变成了关节", "have turned alveoli into joints"))),
        dict(type="mcq", stem_zh="有氧呼吸的生成物包括？", stem_en="The products of aerobic respiration include:",
             answer="a", exp_zh="生成物是二氧化碳和水，并释放能量。", exp_en="The products are carbon dioxide and water, and energy is released.",
             options=opts(("二氧化碳和水", "carbon dioxide and water"), ("只有葡萄糖和氧气", "glucose and oxygen only"),
                          ("只有血小板", "platelets only"), ("纯氮气作为唯一生成物", "pure nitrogen as the only product"))),
    ],
)

# ----- 8Be.01 -----
L(
    id="biology-8Be-1",
    title_zh="生态系统与栖息地", title_en="Ecosystems and habitats",
    obj_zh="本节你将学会区分栖息地和生态系统，并说明生物与环境之间存在相互依赖。",
    obj_en="This lesson you will distinguish a habitat from an ecosystem and explain that organisms and their environment are interdependent.",
    kp_zh="""- **栖息地**是生物生活的地方。
- **生态系统**包括某区域内的所有生物，以及它们的非生物环境，还有彼此间的相互作用。
- 生物依赖环境提供资源（如光、水、食物、栖身之所）；它们也会改变环境。
- 食物关系把不同生物连在一起，一种生物数量变化可能影响其他生物。
- 描述时要同时看到生物因素和非生物因素。""",
    kp_en="""- A **habitat** is the place where an organism lives.
- An **ecosystem** includes all the organisms in an area, their non-living environment, and the interactions between them.
- Organisms depend on the environment for resources such as light, water, food and shelter; they also change the environment.
- Feeding relationships link organisms, so a change in one population can affect others.
- Descriptions should include both living and non-living factors.""",
    body_zh=r"""一片红树林、一个池塘、校园里的一块草地，都可以从两个层次来看。问“这只螃蟹住在哪里”，你在说栖息地。问“这里的植物、动物、微生物，以及水、土壤、光线如何互相影响”，你在说生态系统。

生态系统强调相互关系。植物需要光、水和矿物质；动物可能依赖植物作为食物或隐蔽处；分解者把遗体和废物中的物质释放回环境。温度、水、光照等非生物条件会限制哪些生物能生存；生物的活动，例如树荫或掘土，又会改变这些条件。

因此，保护一个物种往往也要保护它的栖息地，以及它赖以生存的其他物种。

## 例题

若池塘被填平，失去的仅仅是“一块空地”吗？

**解：** 不是。那是许多生物的栖息地，也是一个生态系统：食物关系和非生物条件一起被破坏，依赖它的物种会受到影响。""",
    body_en=r"""A mangrove, a pond or a patch of grass on a school field can be looked at on two levels. “Where does this crab live?” is a habitat question. “How do the plants, animals and microbes interact with the water, soil and light?” is an ecosystem question.

An ecosystem is about relationships. Plants need light, water and minerals; animals may depend on plants for food or shelter; decomposers return materials from dead remains and waste to the environment. Non-living conditions such as temperature, water and light limit which organisms can live there; the organisms’ activities, such as shade from trees or burrowing, can change those conditions in turn.

That is why protecting a species often means protecting its habitat and the other species it depends on.

## Worked example

If a pond is filled in, is only “an empty space” lost?

**Solution:** No. It was a habitat for many organisms and also an ecosystem. Feeding relationships and non-living conditions are destroyed together, and species that depended on it are affected.""",
    diff_zh="""- **把栖息地和生态系统当成完全同一个词。** 栖息地侧重“地方”，生态系统还包含相互作用与非生物环境。
- **只写生物，不写光、水、土壤等非生物因素。**
- **以为一种生物数量变化不会影响其他生物。**""",
    diff_en="""- **Treating habitat and ecosystem as the same word.** Habitat emphasises place; an ecosystem also includes interactions and the non-living environment.
- **Listing only organisms and ignoring light, water and soil.**
- **Assuming a change in one population cannot affect others.**""",
    questions=[
        dict(type="mcq", stem_zh="栖息地指的是？", stem_en="A habitat is:",
             answer="b", exp_zh="栖息地是生物生活的地方。", exp_en="A habitat is the place where an organism lives.",
             options=opts(("只指非生物的温度数字", "a temperature number only, with no place"), ("生物生活的地方", "the place where an organism lives"),
                          ("只指有氧呼吸方程式", "the word equation for aerobic respiration only"), ("血液的液体部分", "the liquid part of blood"))),
        dict(type="mcq", stem_zh="生态系统包括？", stem_en="An ecosystem includes:",
             answer="a", exp_zh="所有生物、非生物环境以及它们之间的相互作用。", exp_en="All the organisms, the non-living environment and the interactions between them.",
             options=opts(("生物、非生物环境及其相互作用", "organisms, the non-living environment and their interactions"),
                          ("只有一块岩石，不含任何生物和相互作用", "only a rock, with no organisms or interactions"),
                          ("只有一种动物，不含环境", "only one animal and no environment"),
                          ("只包括实验室仪器", "laboratory apparatus only"))),
        dict(type="mcq", stem_zh="一种植物大量减少，可能影响以它为食的动物，这说明？", stem_en="If a plant population falls sharply, animals that eat it may be affected. This shows that:",
             answer="c", exp_zh="生物通过食物等关系相互依赖。", exp_en="Organisms are interdependent through relationships such as feeding.",
             options=opts(("生物之间毫无关系", "organisms are not related at all"),
                          ("栖息地不存在", "habitats do not exist"),
                          ("生物之间存在相互依赖", "organisms are interdependent"),
                          ("非生物因素永远不会起作用", "non-living factors never matter"))),
        dict(type="short", stem_zh="举出一个非生物因素，并说明它如何影响生物。", stem_en="Give one non-living factor and say how it can affect organisms.",
             answer="light affects plant growth",
             accepted=["light affects plant growth", "water availability affects survival", "temperature limits where organisms can live",
                       "光照影响植物生长", "水分影响生存", "温度限制生物分布", "土壤影响植物"],
             answer_zh="例如光照影响植物生长，或温度、水分限制哪些生物能生存。",
             answer_en="For example, light affects plant growth, or temperature and water limit where organisms can live.",
             exp_zh="非生物因素是生态系统的一部分。", exp_en="Non-living factors are part of the ecosystem."),
        dict(type="mcq", stem_zh="保护某种鸟类时，也要保护树林和昆虫，主要是因为？", stem_en="Protecting a bird species often means protecting woodland and insects mainly because:",
             answer="d", exp_zh="鸟依赖栖息地以及其他物种提供食物和隐蔽。", exp_en="The bird depends on its habitat and on other species for food and shelter.",
             options=opts(("鸟不需要栖息地", "the bird does not need a habitat"),
                          ("生态系统只包含那一种鸟", "the ecosystem contains only that bird"),
                          ("昆虫与鸟类不可能有关系", "insects cannot be related to birds"),
                          ("它依赖栖息地和其他生物", "it depends on its habitat and on other organisms"))),
        dict(type="mcq", stem_zh="下列叙述更像在描述生态系统而不仅仅是栖息地的是？", stem_en="Which description is more about an ecosystem than only a habitat?",
             answer="a", exp_zh="它同时提到生物、环境和相互作用。", exp_en="It includes organisms, the environment and their interactions.",
             options=opts(("池塘中的生物、水体和它们如何相互影响", "the organisms in a pond, the water, and how they affect one another"),
                          ("只说“鱼住在水里”这一地点", "only the statement “the fish lives in water” as a place"),
                          ("只写有氧呼吸方程式", "only the aerobic respiration equation"),
                          ("只写肺泡壁很薄", "only that alveolar walls are thin"))),
    ],
)

# ----- 8Be.02 -----
L(
    id="biology-8Be-2",
    title_zh="有毒物质的生物累积", title_en="Bioaccumulation of toxic substances",
    obj_zh="本节你将学会解释有毒物质如何沿食物链累积，以及为什么顶端的生物往往受害更明显。",
    obj_en="This lesson you will explain how toxic substances can build up along a food chain and why top predators are often more strongly affected.",
    kp_zh="""- 有些有毒物质不易分解，也不易被生物排出。
- 它们可从环境进入生产者或小型生物，再沿食物链传递。
- **生物累积**指这些物质在生物体内逐渐积聚；沿食物链向上，浓度往往越来越高。
- 顶端的捕食者吃下大量已被污染的猎物，体内毒素可能达到有害水平。
- 因此即使环境中的起始浓度看起来不高，食物链顶端仍可能出现严重问题。""",
    kp_en="""- Some toxic substances break down only slowly and are not easily excreted.
- They can enter producers or small organisms from the environment and then pass along a food chain.
- **Bioaccumulation** is the build-up of these substances in organisms; concentrations often become higher at each step up the chain.
- Top predators eat many contaminated prey, so the toxin in their bodies may reach harmful levels.
- Even if the starting concentration in the environment looks low, serious effects can still appear at the top of the chain.""",
    body_zh=r"""有的污染物会停在生物体内，而不是很快被分解或排出。浮游生物可能只含有很少一点，小鱼吃下许多浮游生物后体内浓度升高，大鱼再吃许多小鱼，浓度就更高。这种沿食物链向上的浓缩，常被称为生物累积（相关课堂用语还有生物放大）。

这解释了为什么有时水里测到的浓度似乎不高，以鱼为食的鸟或哺乳动物却出现繁殖失败或中毒。人若经常食用受污染的大型鱼，也同样处于食物链的靠上位置。

减少这类危害，要从源头控制排放，而不能只看“某一层生物好像还没事”。

## 例题

为什么处于食物链顶端的猛禽，往往比浮游生物更容易表现出有毒物质的危害？

**解：** 猛禽摄食许多已经含有毒素的猎物，毒素在体内积聚到更高浓度。""",
    body_en=r"""Some pollutants stay in living tissue instead of being broken down or excreted quickly. Plankton may contain only a little; small fish eat many plankton and the concentration in their bodies rises; larger fish eat many small fish and the concentration rises again. This increase up a food chain is often called bioaccumulation (you may also meet the term biomagnification).

That is why the concentration in the water can look low, while fish-eating birds or mammals show poisoning or breeding failure. People who often eat contaminated large fish are also fairly high in the chain.

Reducing this kind of harm means controlling the source of the pollutant, not only checking whether one layer of the chain “looks fine”.

## Worked example

Why may a bird of prey at the top of a food chain show toxic effects more clearly than plankton?

**Solution:** The bird eats many prey that already contain the toxin, so the substance builds up to a higher concentration in its body.""",
    diff_zh="""- **以为环境浓度低就一定对顶端生物无害。** 可以沿食物链升高。
- **把生物累积说成“毒素在空气中自己消失”。**
- **只讨论一种生物，不看它吃什么、被什么吃。**""",
    diff_en="""- **Assuming a low environmental concentration must be harmless at the top of the chain.** It can increase along the chain.
- **Describing bioaccumulation as “the toxin simply vanishes in the air”.**
- **Looking at one organism only, without what it eats and what eats it.**""",
    diagram=D_BIOACC,
    questions=[
        dict(type="mcq", stem_zh="生物累积是指有毒物质？", stem_en="Bioaccumulation means that a toxic substance:",
             answer="b", exp_zh="在生物体内积聚，并常沿食物链向上浓度升高。", exp_en="Builds up in organisms and often becomes more concentrated up the food chain.",
             options=opts(("立刻从所有生物体内消失", "vanishes at once from every organism"),
                          ("在生物体内积聚，并常沿食物链升高", "builds up in organisms and often increases up the food chain"),
                          ("只存在于岩石中，不能进入食物链", "exists only in rocks and cannot enter a food chain"),
                          ("使栖息地这个词失去意义", "makes the word habitat meaningless"))),
        dict(type="mcq", stem_zh="通常体内有毒物质浓度可能最高的是？", stem_en="The highest concentration of a toxin is often found in:",
             answer="a", exp_zh="顶端捕食者摄食许多已受污染的猎物。", exp_en="Top predators eat many already contaminated prey.",
             options=opts(("食物链顶端的捕食者", "a predator at the top of the food chain"),
                          ("完全不进食的岩石", "a rock that never feeds"),
                          ("刚进入水体、尚未被生物吸收的全部毒素且不会再传递", "all of the toxin just entering the water, with no further transfer possible"),
                          ("干燥空气中的纯氧气", "pure oxygen in dry air"))),
        dict(type="mcq", stem_zh="即使水中起始浓度看起来不高，顶端生物仍可能受害，是因为？", stem_en="Even if the starting concentration in water looks low, top organisms may still be harmed because:",
             answer="c", exp_zh="毒素可沿食物链逐步浓缩。", exp_en="The toxin can become more concentrated along the food chain.",
             options=opts(("扩散定律在生态系统中不成立且气体不能移动", "diffusion never happens in ecosystems and gases cannot move"),
                          ("有毒物质一定是蛋白质的唯一来源", "the toxin must be the only source of protein"),
                          ("物质可沿食物链逐步累积、浓度升高", "the substance can accumulate and become more concentrated along the chain"),
                          ("顶端生物不吃任何东西", "top organisms eat nothing"))),
        dict(type="short", stem_zh="为什么控制有毒物质的排放源头很重要？", stem_en="Why is it important to control toxic substances at their source?",
             answer="they can build up along food chains",
             accepted=["they can build up along food chains", "low starting levels can still harm top predators",
                       "它们可沿食物链累积", "起始浓度低也可能伤害顶端生物", "进入食物链后难以消除"],
             answer_zh="它们可沿食物链累积，起始浓度低也可能在顶端造成危害。",
             answer_en="They can build up along food chains, so even a low starting level may harm organisms at the top.",
             exp_zh="进入生物体后往往不易分解或排出。", exp_en="Once inside organisms they are often not easily broken down or excreted."),
        dict(type="mcq", stem_zh="有些有毒物质容易生物累积，是因为它们？", stem_en="Some toxic substances bioaccumulate readily because they:",
             answer="d", exp_zh="不易分解，也不易被排出。", exp_en="Break down only slowly and are not easily excreted.",
             options=opts(("很快就被全部排出且从不进入生物", "are all excreted at once and never enter organisms"),
                          ("只溶解在纯净的葡萄糖中", "dissolve only in pure glucose"),
                          ("是肺泡的适应特征", "are adaptations of alveoli"),
                          ("不易分解也不易被排出", "are not easily broken down or excreted"))),
        dict(type="mcq", stem_zh="小鱼体内毒素浓度高于它所吃的浮游生物，最合理的解释是？", stem_en="A small fish has a higher toxin concentration than the plankton it eats. The best explanation is:",
             answer="a", exp_zh="它吃下许多浮游生物，毒素在体内积聚。", exp_en="It eats many plankton, so the toxin builds up in its body.",
             options=opts(("它吃下许多猎物，毒素在体内积聚", "it eats many prey, so the toxin builds up in its body"),
                          ("浮游生物处于食物链的最顶端", "plankton are at the very top of the food chain"),
                          ("毒素不能沿食物链传递", "toxins cannot pass along a food chain"),
                          ("这证明栖息地不存在", "this proves that habitats do not exist"))),
    ],
)

# ----- 8Be.03 -----
L(
    id="biology-8Be-3",
    title_zh="新物种与入侵物种", title_en="New and invasive species",
    obj_zh="本节你将学会说明新物种进入一个生态系统可能带来的影响，并解释什么情况下它会成为入侵物种。",
    obj_en="This lesson you will explain how a newly arrived species can affect an ecosystem, and when it may be called invasive.",
    kp_zh="""- 物种可以通过自然扩散或人类活动进入新的地区。
- 新来者可能成为食物、猎物、竞争者或捕食者，从而改变原有关系。
- 若它迅速繁殖、缺少天敌，并明显危害原有物种或栖息地，常被称为**入侵物种**。
- 不是每一个新来的物种都会造成严重破坏，但一旦造成破坏，往往很难彻底清除。
- 预防（如不随意放生、控制货物携带）通常比事后补救更有效。""",
    kp_en="""- Species can arrive in a new area by natural spread or by human activity.
- A newcomer may become food, prey, a competitor or a predator, and so change existing relationships.
- If it spreads rapidly, has few natural enemies, and clearly harms native species or habitats, it is often called an **invasive species**.
- Not every new species causes serious damage, but once damage is done it is often very hard to remove the species completely.
- Prevention (for example not releasing pets, and checking goods that might carry organisms) is usually more effective than later control.""",
    body_zh=r"""生态系统里的物种组成不是永远固定的。有的物种自己扩散到新地方；更多时候，人类的船运、贸易或放生会把生物带到它们原本不会到达的地方。

新物种可能与本地物种竞争食物或空间，可能捕食本地物种，也可能带来疾病，或改变栖息地（例如密集生长遮住水面的植物）。如果缺少能限制它的天敌，数量可能增加很快，原有物种就被排挤。这时人们常称它为入侵物种。

也要避免绝对化：并非每一个新来者都会“毁掉一切”，但一旦形成入侵，清除成本很高，对食物链和栖息地的影响也可能长期存在。新加坡作为港口城市，对生物随货物和船舱水移动格外敏感，这正是课堂讨论的现实意义。

## 例题

为什么“把不想养的宠物放回野外”可能造成生态问题？

**解：** 被放生的动物可能在当地没有天敌，捕食或竞争本地物种，变成入侵者，并且很难再全部收回。""",
    body_en=r"""The mix of species in an ecosystem is not fixed for ever. Some species spread into new places by themselves; more often, shipping, trade or deliberate release carry organisms to places they would not otherwise reach.

A new species may compete with native species for food or space, prey on them, bring disease, or change the habitat (for example a plant that grows so densely that it shades a water surface). If it has few natural enemies, its numbers may rise quickly and native species may be pushed out. In that case it is often called invasive.

Avoid the extreme claim that every newcomer “destroys everything”. But once a species is invasive, removal is costly and effects on food chains and habitats may last a long time. As a port city, Singapore is especially aware of organisms moving with cargo and ships, which is why this idea matters in class.

## Worked example

Why can releasing an unwanted pet into the wild cause ecological problems?

**Solution:** The released animal may have no natural enemies locally, may prey on or compete with native species, and may become invasive. It is then very hard to take them all back.""",
    diff_zh="""- **以为所有新来物种都一定立即毁灭整个生态系统。** 要看它是否迅速扩散并造成危害。
- **以为一旦出现就可以轻易全部清除。** 往往很难。
- **忽略人类活动（放生、运输）在传播中的作用。**""",
    diff_en="""- **Assuming every new species immediately destroys the whole ecosystem.** Ask whether it spreads rapidly and causes harm.
- **Assuming it can easily be removed completely later.** That is often very hard.
- **Ignoring the role of human activity (release, transport) in spreading species.**""",
    questions=[
        dict(type="mcq", stem_zh="入侵物种通常是指新来的物种？", stem_en="An invasive species is usually a newly arrived species that:",
             answer="b", exp_zh="迅速扩散并明显危害原有物种或栖息地。", exp_en="Spreads rapidly and clearly harms native species or habitats.",
             options=opts(("对原有生态系统完全没有影响", "has no effect at all on the existing ecosystem"),
                          ("迅速扩散并危害原有物种或栖息地", "spreads rapidly and harms native species or habitats"),
                          ("只能生活在实验室试管中", "can live only in a laboratory tube"),
                          ("一定是该地原有的顶级捕食者", "must already have been the area’s original top predator"))),
        dict(type="mcq", stem_zh="新物种可能影响生态系统的一种方式是？", stem_en="One way a new species may affect an ecosystem is by:",
             answer="a", exp_zh="与本地物种竞争或捕食它们，或改变栖息地。", exp_en="Competing with or preying on native species, or changing the habitat.",
             options=opts(("与本地物种竞争或捕食它们", "competing with or preying on native species"),
                          ("自动让所有有毒物质消失", "making every toxic substance vanish automatically"),
                          ("停止有氧呼吸在全球发生", "stopping aerobic respiration worldwide"),
                          ("把栖息地变成血浆", "turning habitats into plasma"))),
        dict(type="mcq", stem_zh="新来物种若缺少天敌，更可能？", stem_en="If a newly arrived species has few natural enemies, it is more likely to:",
             answer="c", exp_zh="数量可能增加很快，排挤本地物种。", exp_en="Increase in number quickly and push out native species.",
             options=opts(("立即灭绝且无任何扩散", "die out at once with no spread"),
                          ("只能帮助本地物种，不可能竞争", "only help native species and never compete"),
                          ("数量迅速增加并排挤本地物种", "increase quickly and push out native species"),
                          ("把气候改定义为天气", "redefine climate as weather"))),
        dict(type="short", stem_zh="写出一种可以减少入侵物种风险的做法。", stem_en="Give one action that can reduce the risk from invasive species.",
             answer="do not release pets into the wild",
             accepted=["do not release pets into the wild", "check cargo and ships", "prevention is better than later removal", "don't move species to new habitats",
                       "不随意放生", "检查货物和船舶", "预防比事后清除更有效", "不要把物种带到新栖息地"],
             answer_zh="例如不随意把宠物放生到野外，或控制货物与船舶携带生物。",
             answer_en="For example, do not release pets into the wild, or check cargo and ships that might carry organisms.",
             exp_zh="预防通常比入侵后再清除更有效。", exp_en="Prevention is usually more effective than trying to remove a species later."),
        dict(type="mcq", stem_zh="入侵一旦形成，往往很难彻底清除，因此更重要的是？", stem_en="Once an invasion is established it is often very hard to remove, so it is more important to:",
             answer="d", exp_zh="预防物种被带到新地区。", exp_en="Prevent species being moved into new areas.",
             options=opts(("等到完全入侵后再开始考虑", "wait until the invasion is complete before thinking about it"),
                          ("鼓励随意放生以增加多样性", "encourage unplanned releases to increase diversity"),
                          ("忽略运输途径", "ignore transport routes"),
                          ("预防物种进入新地区", "prevent species entering new areas"))),
        dict(type="mcq", stem_zh="下列说法较准确的是？", stem_en="Which statement is the fairest?",
             answer="a", exp_zh="并非每个新来者都会严重破坏，但造成入侵后影响可能很大且难清除。", exp_en="Not every newcomer causes serious damage, but an invasion can have large effects and be hard to reverse.",
             options=opts(("不是每个新物种都会严重破坏，但入侵后往往难清除、影响可能很大", "not every new species causes serious harm, but an invasion is often hard to reverse and may have large effects"),
                          ("每一个新来的物种都会在一天内毁掉整个地球", "every new species destroys the whole Earth in a day"),
                          ("新物种不可能改变食物关系", "a new species cannot change feeding relationships"),
                          ("只有实验室里的物种才能成为入侵种", "only laboratory species can become invasive"))),
    ],
)

def X(section, **q):
    return (section, q)

BS_PR = add_extra_questions(C, [
    X("biology-8Bs-1", type="mcq", id="q-bi-8Bs-pr01", stem_zh="肌肉只能？", stem_en="A muscle can only:",
      answer="a", exp_zh="肌肉只能收缩来拉骨头。", exp_en="A muscle can only contract and pull a bone.",
      options=opts(("收缩从而拉骨头", "contract and so pull a bone"), ("主动把骨头推回去", "actively push a bone back"),
                   ("变成血浆", "turn into plasma"), ("代替肺泡进行气体交换", "replace alveoli for gas exchange"))),
    X("biology-8Bs-1", type="mcq", id="q-bi-8Bs-pr02", stem_zh="屈肘时肱二头肌和肱三头肌通常？", stem_en="When the elbow bends, the biceps and triceps usually:",
      answer="c", exp_zh="二头肌收缩，三头肌舒张。", exp_en="The biceps contracts and the triceps relaxes.",
      options=opts(("同时同样用力推骨头", "both push the bone equally"), ("都完全不工作", "both do nothing"),
                   ("二头肌收缩，三头肌舒张", "biceps contracts, triceps relaxes"), ("只有韧带收缩", "only ligaments contract"))),
    X("biology-8Bs-2", type="mcq", id="q-bi-8Bs-pr03", stem_zh="运输氧气主要靠？", stem_en="Oxygen is transported mainly by:",
      answer="b", exp_zh="红细胞运输氧气。", exp_en="Red blood cells transport oxygen.",
      options=opts(("血小板", "platelets"), ("红细胞", "red blood cells"), ("只有血浆中的沙子", "sand in plasma only"), ("肌腱", "tendons"))),
    X("biology-8Bs-2", type="mcq", id="q-bi-8Bs-pr04", stem_zh="血小板的功能是？", stem_en="The function of platelets is:",
      answer="d", exp_zh="参与凝血。", exp_en="They are involved in clotting.",
      options=opts(("只运输氧气", "transporting oxygen only"), ("进行全部有氧呼吸", "carrying out all of aerobic respiration"),
                   ("形成关节", "forming joints"), ("参与凝血", "being involved in clotting"))),
    X("biology-8Bs-3", type="mcq", id="q-bi-8Bs-pr05", stem_zh="气体交换主要发生在？", stem_en="Gas exchange mainly happens at the:",
      answer="a", exp_zh="主要场所是肺泡。", exp_en="The main site is the alveoli.",
      options=opts(("肺泡", "alveoli"), ("肌腱", "tendons"), ("胃", "stomach"), ("头发", "hair"))),
    X("biology-8Bs-3", type="short", id="q-bi-8Bs-pr06", stem_zh="通气和细胞呼吸有何不同？", stem_en="How do ventilation and respiration in cells differ?",
      answer="ventilation moves air; respiration releases energy in cells",
      accepted=["ventilation moves air; respiration releases energy in cells", "通气是空气进出肺，呼吸作用在细胞中释放能量", "呼吸运动是通气，呼吸作用在细胞内"],
      answer_zh="通气是空气进出肺；呼吸作用在细胞中释放能量。", answer_en="Ventilation moves air; respiration releases energy in cells.",
      exp_zh="不要把两个词混用。", exp_en="Do not mix the two words."),
    X("biology-8Bs-4", type="mcq", id="q-bi-8Bs-pr07", stem_zh="扩散的净方向是？", stem_en="The net direction of diffusion is from:",
      answer="c", exp_zh="从高浓度到低浓度。", exp_en="From higher to lower concentration.",
      options=opts(("低到高", "lower to higher"), ("只在金属中", "metals only"), ("高到低", "higher to lower"), ("无法发生在气体中", "never in gases"))),
    X("biology-8Bs-4", type="mcq", id="q-bi-8Bs-pr08", stem_zh="肺泡适合气体交换的一个原因是？", stem_en="One reason alveoli are adapted for gas exchange is that they have:",
      answer="b", exp_zh="壁薄、表面积大。", exp_en="Thin walls and a large surface area.",
      options=opts(("极厚的壁", "very thick walls"), ("薄壁和很大的总表面积", "thin walls and a large total surface area"),
                   ("完全没有血液供应", "no blood supply"), ("干燥且只有一个囊", "a dry surface and only one sac"))),
])
BS_PA = add_extra_questions(C, [
    X("biology-8Bs-1", type="mcq", id="q-bi-8Bs-pa01", stem_zh="拮抗肌成对工作是因为肌肉？", stem_en="Antagonistic muscles work in pairs because a muscle:",
      answer="a", exp_zh="只能拉向一个方向，反向靠另一块。", exp_en="Can only pull one way; the other muscle does the reverse.",
      options=opts(("只能拉向一个方向", "can only pull one way"), ("可以随意推和拉所有方向", "can push and pull in every direction"),
                   ("不附着于骨", "is not attached to bone"), ("替代关节", "replaces the joint"))),
    X("biology-8Bs-1", type="short", id="q-bi-8Bs-pa02", stem_zh="肌腱连接什么？", stem_en="What does a tendon connect?",
      answer="muscle to bone", accepted=["muscle to bone", "muscles to bones", "肌腱连接肌肉和骨", "肌肉与骨"],
      answer_zh="肌肉和骨。", answer_en="Muscle to bone.", exp_zh="韧带则连接骨与骨。", exp_en="A ligament connects bone to bone."),
    X("biology-8Bs-1", type="mcq", id="q-bi-8Bs-pa03", stem_zh="伸肘时主要收缩的是？", stem_en="The muscle that mainly contracts to straighten the elbow is the:",
      answer="d", exp_zh="肱三头肌。", exp_en="The triceps.",
      options=opts(("肺", "lungs"), ("只有心脏", "heart only"), ("肱二头肌", "biceps"), ("肱三头肌", "triceps"))),
    X("biology-8Bs-2", type="mcq", id="q-bi-8Bs-pa04", stem_zh="白细胞的主要功能是？", stem_en="The main function of white blood cells is:",
      answer="b", exp_zh="抵御病原体。", exp_en="Defending against pathogens.",
      options=opts(("只运氧", "oxygen transport only"), ("抵御病原体", "defence against pathogens"),
                   ("形成韧带", "forming ligaments"), ("代替通气", "replacing ventilation"))),
    X("biology-8Bs-2", type="mcq", id="q-bi-8Bs-pa05", stem_zh="血浆运输的可以是？", stem_en="Plasma can transport:",
      answer="c", exp_zh="养分、激素、废物、二氧化碳和热等。", exp_en="Nutrients, hormones, wastes, carbon dioxide and heat, for example.",
      options=opts(("只有整块骨骼", "whole bones only"), ("只有肺泡", "alveoli only"),
                   ("养分、激素或二氧化碳等溶解物质", "dissolved substances such as nutrients, hormones or carbon dioxide"),
                   ("无法运输任何物质", "nothing at all"))),
    X("biology-8Bs-2", type="mcq", id="q-bi-8Bs-pa06", stem_zh="血液的液体部分是？", stem_en="The liquid part of blood is:",
      answer="a", exp_zh="血浆。", exp_en="Plasma.",
      options=opts(("血浆", "plasma"), ("关节", "a joint"), ("栖息地", "a habitat"), ("气管软骨", "tracheal cartilage"))),
    X("biology-8Bs-3", type="mcq", id="q-bi-8Bs-pa07", stem_zh="肺泡处通常？", stem_en="At the alveoli, usually:",
      answer="d", exp_zh="氧气进入血液，二氧化碳离开血液。", exp_en="Oxygen enters the blood; carbon dioxide leaves the blood.",
      options=opts(("两种气体都不移动", "neither gas moves"), ("只有二氧化碳进入血液、氧气离开", "only carbon dioxide enters the blood and oxygen leaves"),
                   ("气体交换发生在肌腱里", "gas exchange happens in tendons"), ("氧气进入血液，二氧化碳离开血液", "oxygen enters the blood and carbon dioxide leaves it"))),
    X("biology-8Bs-3", type="mcq", id="q-bi-8Bs-pa08", stem_zh="胸廓和膈肌运动的作用是？", stem_en="Ribcage and diaphragm movements are for:",
      answer="b", exp_zh="通气，使空气进出肺。", exp_en="Ventilation, moving air in and out of the lungs.",
      options=opts(("在肺泡空腔完成全部有氧呼吸", "completing all aerobic respiration in the alveolar cavity"),
                   ("通气", "ventilation"), ("制造红细胞", "making red cells"), ("连接骨与骨", "joining bone to bone"))),
    X("biology-8Bs-4", type="mcq", id="q-bi-8Bs-pa09", stem_zh="氧气在肺泡进入血液是因为？", stem_en="Oxygen enters the blood at alveoli because:",
      answer="a", exp_zh="肺泡气中氧气浓度更高。", exp_en="The concentration is higher in the alveolar air.",
      options=opts(("肺泡气中氧气浓度高于血液", "the concentration is higher in alveolar air than in blood"),
                   ("血液中氧气浓度更高", "the concentration is higher in the blood"),
                   ("扩散从低到高", "diffusion runs from low to high"), ("血小板泵氧入骨", "platelets pump oxygen into bone"))),
    X("biology-8Bs-4", type="mcq", id="q-bi-8Bs-pa10", stem_zh="丰富的毛细血管有助于？", stem_en="A rich capillary supply helps to:",
      answer="c", exp_zh="迅速运走或送来气体，维持浓度差。", exp_en="Carry gases quickly and maintain the gradient.",
      options=opts(("增厚肺泡壁", "thicken alveolar walls"), ("阻止扩散", "prevent diffusion"),
                   ("维持浓度差", "maintain the concentration gradient"), ("把肺泡变成关节", "turn alveoli into joints"))),
    X("biology-8Bs-3", type="mcq", id="q-bi-8Bs-pa11", stem_zh="气管软骨的作用是？", stem_en="Cartilage in the trachea helps to:",
      answer="d", exp_zh="保持气道开放。", exp_en="Keep the airway open.",
      options=opts(("进行光合作用", "carry out photosynthesis"), ("代替红细胞运氧", "replace red cells"),
                   ("把血液变成骨", "turn blood into bone"), ("保持气道畅通", "keep the airway open"))),
    X("biology-8Bs-1", type="mcq", id="q-bi-8Bs-pa12", stem_zh="韧带的作用是？", stem_en="The role of a ligament is to:",
      answer="a", exp_zh="连接骨与骨，稳定关节。", exp_en="Connect bone to bone and stabilise the joint.",
      options=opts(("连接骨与骨", "connect bone to bone"), ("连接肌肉与骨", "connect muscle to bone"),
                   ("运输氧气", "transport oxygen"), ("在细胞中进行有氧呼吸", "carry out aerobic respiration in cells"))),
])
BP_PR = add_extra_questions(C, [
    X("biology-8Bp-1", type="mcq", id="q-bi-8Bp-pr01", stem_zh="蛋白质主要用于？", stem_en="Protein is used mainly for:",
      answer="b", exp_zh="生长和修复。", exp_en="Growth and repair.",
      options=opts(("只运氧", "oxygen transport only"), ("生长和修复", "growth and repair"), ("替代所有水", "replacing all water"), ("形成气候", "forming climate"))),
    X("biology-8Bp-1", type="mcq", id="q-bi-8Bp-pr02", stem_zh="均衡饮食是指？", stem_en="A balanced diet means:",
      answer="a", exp_zh="适量的各类营养素、水和纤维。", exp_en="Suitable amounts of each nutrient, plus water and fibre.",
      options=opts(("适量的各类营养素、水和纤维", "suitable amounts of each nutrient, plus water and fibre"),
                   ("只吃一种食物越多越好", "as much as possible of one food"), ("完全不需要水", "no need for water"), ("禁止所有糖类和脂肪", "banning all carbohydrate and fat"))),
    X("biology-8Bp-2", type="mcq", id="q-bi-8Bp-pr03", stem_zh="同样质量下通常能量最高的是？", stem_en="For the same mass, the highest energy is usually in:",
      answer="c", exp_zh="脂肪单位质量能量通常更高。", exp_en="Fat usually has more energy per unit mass.",
      options=opts(("水", "water"), ("空气", "air"), ("脂肪", "fat"), ("纤维作为最主要供能物质", "fibre as the main energy source"))),
    X("biology-8Bp-2", type="mcq", id="q-bi-8Bp-pr04", stem_zh="长期能量摄入远高于消耗，可能？", stem_en="If energy intake stays well above use, extra energy may be:",
      answer="d", exp_zh="以脂肪形式储存。", exp_en="Stored as fat.",
      options=opts(("自动消失", "vanish automatically"), ("使蛋白质失去全部功能于一天内", "remove all protein function in a day"),
                   ("把肺泡变成关节", "turn alveoli into joints"), ("以脂肪形式储存", "stored as fat"))),
    X("biology-8Bp-3", type="mcq", id="q-bi-8Bp-pr05", stem_zh="一氧化碳会？", stem_en="Carbon monoxide can:",
      answer="a", exp_zh="与血红蛋白结合，减少氧气运输。", exp_en="Bind to haemoglobin and reduce oxygen transport.",
      options=opts(("与血红蛋白结合，减少氧气运输", "bind to haemoglobin and reduce oxygen transport"),
                   ("把红细胞变成骨骼", "turn red cells into bone"), ("只改变头发颜色", "change hair colour only"), ("增加无限氧气", "raise oxygen without limit"))),
    X("biology-8Bp-3", type="mcq", id="q-bi-8Bp-pr06", stem_zh="焦油损害肺泡，主要影响？", stem_en="Tar damaging alveoli mainly affects:",
      answer="b", exp_zh="气体交换变差。", exp_en="Gas exchange becomes less effective.",
      options=opts(("只影响肌腱颜色", "tendon colour only"), ("气体交换", "gas exchange"), ("气候定义", "the definition of climate"), ("关节名称", "the name of a joint"))),
    X("biology-8Bp-4", type="short", id="q-bi-8Bp-pr07", stem_zh="写出有氧呼吸的文字方程式。", stem_en="Write the word equation for aerobic respiration.",
      answer="glucose + oxygen -> carbon dioxide + water",
      accepted=["glucose + oxygen -> carbon dioxide + water", "glucose + oxygen → carbon dioxide + water", "葡萄糖+氧气→二氧化碳+水", "葡萄糖 + 氧气 → 二氧化碳 + 水"],
      answer_zh="葡萄糖 $+$ 氧气 $\\rightarrow$ 二氧化碳 $+$ 水", answer_en="glucose $+$ oxygen $\\rightarrow$ carbon dioxide $+$ water",
      exp_zh="并释放能量。", exp_en="Energy is also released."),
    X("biology-8Bp-4", type="mcq", id="q-bi-8Bp-pr08", stem_zh="有氧呼吸发生在？", stem_en="Aerobic respiration takes place in:",
      answer="c", exp_zh="细胞中。", exp_en="Cells.",
      options=opts(("只在肺泡空腔", "the alveolar cavity only"), ("只在气管", "the trachea only"), ("细胞中", "cells"), ("关节腔替代肌肉", "the joint cavity, replacing muscle"))),
])
BP_PA = add_extra_questions(C, [
    X("biology-8Bp-1", type="mcq", id="q-bi-8Bp-pa01", stem_zh="糖类和脂肪的共同作用之一是？", stem_en="A shared role of carbohydrate and fat is to:",
      answer="a", exp_zh="提供能量。", exp_en="Provide energy.",
      options=opts(("提供能量", "provide energy"), ("只构成韧带", "form ligaments only"), ("代替白细胞", "replace white cells"), ("阻止扩散", "stop diffusion"))),
    X("biology-8Bp-1", type="mcq", id="q-bi-8Bp-pa02", stem_zh="纤维的一种作用是？", stem_en="One role of fibre is to:",
      answer="d", exp_zh="帮助食物在肠道中移动。", exp_en="Help food move through the gut.",
      options=opts(("替代所有水分", "replace all water"), ("运输氧气", "transport oxygen"),
                   ("进行有氧呼吸作为反应物", "act as a reactant in aerobic respiration"), ("帮助肠道蠕动", "help the gut move food"))),
    X("biology-8Bp-1", type="mcq", id="q-bi-8Bp-pa03", stem_zh="只吃大量水果、完全没有蛋白质，算均衡吗？", stem_en="Is fruit only, with no protein, a balanced diet?",
      answer="b", exp_zh="不算，缺少蛋白质会影响生长和修复。", exp_en="No; lack of protein affects growth and repair.",
      options=opts(("算，因为吃得多", "yes, because the amount is large"), ("不算，种类不全", "no, a group is missing"),
                   ("算，一种食物可代替一切", "yes, one food can replace everything"), ("不算，因为禁止水果", "no, because fruit is banned"))),
    X("biology-8Bp-2", type="mcq", id="q-bi-8Bp-pa04", stem_zh="课堂燃烧食物加热水，结果往往偏低，是因为？", stem_en="A class food-burning experiment often underestimates energy because:",
      answer="c", exp_zh="部分热量散失到周围。", exp_en="Some heat is lost to the surroundings.",
      options=opts(("水不能升温", "water cannot warm up"), ("食物不含能量", "food contains no energy"),
                   ("部分热量散失到周围", "some heat is lost to the surroundings"), ("脂肪不能燃烧", "fat cannot burn"))),
    X("biology-8Bp-2", type="mcq", id="q-bi-8Bp-pa05", stem_zh="比较零食时只看能量是否足够？", stem_en="Is energy content alone enough when comparing snacks?",
      answer="a", exp_zh="还要看其他营养素、份量和需要。", exp_en="Other nutrients, portion size and need also matter.",
      options=opts(("不够", "no"), ("够，最高者最好", "yes, the highest is best"), ("够，最低者最好", "yes, the lowest is best"), ("食物无能量", "food has no energy"))),
    X("biology-8Bp-3", type="mcq", id="q-bi-8Bp-pa06", stem_zh="尼古丁可能？", stem_en="Nicotine can:",
      answer="d", exp_zh="使血管收缩，加重心脏负担。", exp_en="Narrow blood vessels and strain the heart.",
      options=opts(("把血液变成纯氧", "turn blood into pure oxygen"), ("完全无害于心脏", "be harmless to the heart"),
                   ("让血红蛋白只运纤维", "make haemoglobin carry only fibre"), ("使血管收缩，心脏更费力", "narrow vessels so the heart works harder"))),
    X("biology-8Bp-3", type="short", id="q-bi-8Bp-pa07", stem_zh="写出吸烟中一种有害物质及其一种危害。", stem_en="Name one harmful substance in smoke and one effect.",
      answer="tar damages alveoli",
      accepted=["tar damages alveoli", "carbon monoxide reduces oxygen transport", "nicotine strains the heart",
                "焦油损害肺泡", "一氧化碳减少氧气运输", "尼古丁加重心脏负担"],
      answer_zh="例如焦油损害肺泡。", answer_en="For example, tar damages alveoli.", exp_zh="能对应到结构或功能即可。", exp_en="Link it to a structure or function."),
    X("biology-8Bp-3", type="mcq", id="q-bi-8Bp-pa08", stem_zh="关于饮食与健康，较准确的是？", stem_en="A fair statement about diet and health is:",
      answer="b", exp_zh="长期习惯更重要，风险可累积。", exp_en="Long-term habits matter; risk can build.",
      options=opts(("一餐油腻必然立即致病", "one heavier meal always causes immediate disease"),
                   ("长期习惯很重要，风险可以累积", "long-term habits matter and risk can build"),
                   ("饮食与健康无关", "diet is unrelated to health"), ("能量最高一定最健康", "highest energy is always healthiest"))),
    X("biology-8Bp-4", type="mcq", id="q-bi-8Bp-pa09", stem_zh="有氧呼吸的生成物包括？", stem_en="Products of aerobic respiration include:",
      answer="c", exp_zh="二氧化碳和水。", exp_en="Carbon dioxide and water.",
      options=opts(("只有葡萄糖和氧气", "glucose and oxygen only"), ("只有血小板", "platelets only"),
                   ("二氧化碳和水", "carbon dioxide and water"), ("纯氮作为唯一生成物", "pure nitrogen only"))),
    X("biology-8Bp-4", type="mcq", id="q-bi-8Bp-pa10", stem_zh="运动时呼吸加快，是因为细胞？", stem_en="Breathing is faster in exercise because cells:",
      answer="a", exp_zh="需要更多氧、产生更多二氧化碳。", exp_en="Need more oxygen and make more carbon dioxide.",
      options=opts(("需要更多氧气并产生更多二氧化碳", "need more oxygen and produce more carbon dioxide"),
                   ("停止呼吸作用", "stop respiring"), ("不再需要葡萄糖", "no longer need glucose"), ("把肺泡变成关节", "turn alveoli into joints"))),
    X("biology-8Bp-4", type="mcq", id="q-bi-8Bp-pa11", stem_zh="正确区分通气与有氧呼吸的是？", stem_en="Which correctly separates ventilation and aerobic respiration?",
      answer="d", exp_zh="通气是空气进出肺，有氧呼吸在细胞中释放能量。", exp_en="Ventilation moves air; respiration releases energy in cells.",
      options=opts(("二者完全相同", "they are the same"), ("通气只在细胞内", "ventilation is only in cells"),
                   ("有氧呼吸是胸廓运动", "respiration is rib movement"), ("通气是空气进出肺，有氧呼吸在细胞中释放能量", "ventilation moves air; respiration releases energy in cells"))),
    X("biology-8Bp-2", type="mcq", id="q-bi-8Bp-pa12", stem_zh="活动量大的人通常需要？", stem_en="A very active person usually needs:",
      answer="b", exp_zh="更多能量，但仍要均衡。", exp_en="More energy, while still eating a balanced diet.",
      options=opts(("完全不需要能量", "no energy"), ("更多能量（并仍要均衡）", "more energy, still balanced"),
                   ("只需要纤维", "fibre only"), ("比静止时更少能量", "less energy than at rest"))),
])
BE_PR = add_extra_questions(C, [
    X("biology-8Be-1", type="mcq", id="q-bi-8Be-pr01", stem_zh="栖息地是？", stem_en="A habitat is:",
      answer="a", exp_zh="生物生活的地方。", exp_en="The place where an organism lives.",
      options=opts(("生物生活的地方", "the place where an organism lives"), ("只是一个温度数字", "a temperature number only"),
                   ("有氧呼吸方程式", "the respiration equation"), ("血浆", "plasma"))),
    X("biology-8Be-1", type="mcq", id="q-bi-8Be-pr02", stem_zh="生态系统包括？", stem_en="An ecosystem includes:",
      answer="c", exp_zh="生物、非生物环境及相互作用。", exp_en="Organisms, the non-living environment and interactions.",
      options=opts(("只有一块不含生物的岩石", "only a rock with no organisms"), ("只有一种动物", "only one animal"),
                   ("生物、非生物环境及相互作用", "organisms, the non-living environment and interactions"), ("只包括仪器", "apparatus only"))),
    X("biology-8Be-1", type="short", id="q-bi-8Be-pr03", stem_zh="举一个非生物因素及其影响。", stem_en="Give one non-living factor and an effect.",
      answer="light affects plant growth",
      accepted=["light affects plant growth", "water affects survival", "temperature limits distribution", "光照影响植物生长", "水分影响生存", "温度限制分布"],
      answer_zh="例如光照影响植物生长。", answer_en="For example, light affects plant growth.", exp_zh="非生物因素是生态系统的一部分。", exp_en="Non-living factors are part of the ecosystem."),
    X("biology-8Be-2", type="mcq", id="q-bi-8Be-pr04", stem_zh="生物累积是指毒素？", stem_en="Bioaccumulation means a toxin:",
      answer="b", exp_zh="在体内积聚并常沿食物链升高。", exp_en="Builds up and often increases up the chain.",
      options=opts(("立刻从所有生物消失", "vanishes from all organisms at once"), ("在体内积聚并常沿食物链升高", "builds up and often increases up the food chain"),
                   ("不能进入食物链", "cannot enter a food chain"), ("只存在于岩石", "exists only in rocks"))),
    X("biology-8Be-2", type="mcq", id="q-bi-8Be-pr05", stem_zh="体内浓度往往最高的是？", stem_en="The highest concentration is often in:",
      answer="d", exp_zh="顶端捕食者。", exp_en="A top predator.",
      options=opts(("完全不进食的岩石", "a rock that never feeds"), ("纯氧", "pure oxygen"), ("刚入水且不再传递的全部毒素", "all toxin just entering water with no transfer"), ("食物链顶端的捕食者", "a top predator"))),
    X("biology-8Be-2", type="mcq", id="q-bi-8Be-pr06", stem_zh="水中起始浓度不高，顶端仍可能受害，因为？", stem_en="A low starting level in water may still harm the top because:",
      answer="a", exp_zh="可沿食物链浓缩。", exp_en="It can become more concentrated along the chain.",
      options=opts(("可沿食物链累积升高", "it can accumulate and increase along the chain"), ("顶端生物不进食", "top organisms do not eat"),
                   ("扩散在生态系统中不存在", "diffusion never happens in ecosystems"), ("毒素是唯一蛋白质来源", "the toxin is the only protein source"))),
    X("biology-8Be-3", type="mcq", id="q-bi-8Be-pr07", stem_zh="入侵物种通常会？", stem_en="An invasive species typically:",
      answer="c", exp_zh="迅速扩散并危害原有物种或栖息地。", exp_en="Spreads rapidly and harms native species or habitats.",
      options=opts(("对生态系统全无影响", "has no effect"), ("只能生活在试管中", "lives only in a test tube"),
                   ("迅速扩散并造成危害", "spreads rapidly and causes harm"), ("一定是本地原有顶级捕食者", "must already have been the native top predator"))),
    X("biology-8Be-3", type="mcq", id="q-bi-8Be-pr08", stem_zh="减少入侵风险的做法是？", stem_en="A way to reduce invasion risk is to:",
      answer="b", exp_zh="不随意放生，并注意运输途径。", exp_en="Avoid releasing pets and watch transport routes.",
      options=opts(("鼓励随意放生", "encourage unplanned release"), ("不把宠物放到野外，并注意货物与船舶", "not release pets, and check cargo and ships"),
                   ("等到完全入侵后再考虑预防", "wait until invasion is complete"), ("忽略运输", "ignore transport"))),
])
BE_PA = add_extra_questions(C, [
    X("biology-8Be-1", type="mcq", id="q-bi-8Be-pa01", stem_zh="一种植物减少可能影响以其为食的动物，说明？", stem_en="If a plant decrease affects animals that eat it, this shows:",
      answer="a", exp_zh="生物相互依赖。", exp_en="Organisms are interdependent.",
      options=opts(("生物相互依赖", "organisms are interdependent"), ("生物毫无关系", "organisms are unrelated"),
                   ("栖息地不存在", "habitats do not exist"), ("非生物因素从不重要", "non-living factors never matter"))),
    X("biology-8Be-1", type="mcq", id="q-bi-8Be-pa02", stem_zh="保护一种鸟也要保护树林，因为？", stem_en="Protecting a bird often means protecting woodland because:",
      answer="c", exp_zh="它依赖栖息地和其他生物。", exp_en="It depends on its habitat and other organisms.",
      options=opts(("鸟不需要栖息地", "the bird needs no habitat"), ("生态系统只包含那只鸟", "the ecosystem is only that bird"),
                   ("它依赖栖息地和其他生物", "it depends on its habitat and other organisms"), ("昆虫与鸟不可能有关", "insects cannot relate to birds"))),
    X("biology-8Be-1", type="mcq", id="q-bi-8Be-pa03", stem_zh="更像描述生态系统的是？", stem_en="Which is more about an ecosystem than only a habitat?",
      answer="b", exp_zh="同时包含生物、环境和相互作用。", exp_en="It includes organisms, environment and interactions.",
      options=opts(("只说鱼住在水里", "only “the fish lives in water”"), ("池塘中的生物、水体和相互作用", "organisms, water and interactions in a pond"),
                   ("只写呼吸方程式", "only the respiration equation"), ("只写肺泡壁薄", "only that alveolar walls are thin"))),
    X("biology-8Be-2", type="short", id="q-bi-8Be-pa04", stem_zh="为什么控制毒素排放源头很重要？", stem_en="Why is it important to control toxins at source?",
      answer="they can build up along food chains",
      accepted=["they can build up along food chains", "low levels can still harm top predators", "它们可沿食物链累积", "起始浓度低也可能伤害顶端生物"],
      answer_zh="它们可沿食物链累积。", answer_en="They can build up along food chains.", exp_zh="进入生物后不易排出。", exp_en="They are often not easily excreted."),
    X("biology-8Be-2", type="mcq", id="q-bi-8Be-pa05", stem_zh="有些毒素易累积，因为它们？", stem_en="Some toxins bioaccumulate because they are:",
      answer="d", exp_zh="不易分解也不易排出。", exp_en="Not easily broken down or excreted.",
      options=opts(("很快全部排出", "all excreted at once"), ("只溶在葡萄糖中", "dissolved only in glucose"),
                   ("肺泡的适应", "adaptations of alveoli"), ("不易分解也不易排出", "not easily broken down or excreted"))),
    X("biology-8Be-2", type="mcq", id="q-bi-8Be-pa06", stem_zh="小鱼体内毒素高于浮游生物，是因为？", stem_en="A fish has more toxin than the plankton it eats because:",
      answer="a", exp_zh="它吃下许多猎物，毒素积聚。", exp_en="It eats many prey, so the toxin builds up.",
      options=opts(("它吃下许多猎物，毒素积聚", "it eats many prey and the toxin builds up"), ("浮游生物在食物链顶端", "plankton are at the top of the chain"),
                   ("毒素不能传递", "toxins cannot pass along a chain"), ("栖息地不存在", "habitats do not exist"))),
    X("biology-8Be-3", type="mcq", id="q-bi-8Be-pa07", stem_zh="新物种影响生态系统的一种方式是？", stem_en="A new species may affect an ecosystem by:",
      answer="c", exp_zh="竞争或捕食本地物种。", exp_en="Competing with or preying on native species.",
      options=opts(("自动消除所有毒素", "removing all toxins automatically"), ("停止全球呼吸作用", "stopping respiration worldwide"),
                   ("竞争或捕食本地物种", "competing with or preying on native species"), ("把栖息地变成血浆", "turning habitats into plasma"))),
    X("biology-8Be-3", type="mcq", id="q-bi-8Be-pa08", stem_zh="缺少天敌时，新来物种更可能？", stem_en="With few enemies, a newcomer is more likely to:",
      answer="b", exp_zh="数量迅速增加并排挤本地种。", exp_en="Increase quickly and push out native species.",
      options=opts(("立即灭绝", "die out at once"), ("迅速增加并排挤本地种", "increase quickly and push out native species"),
                   ("只帮助本地种", "only help native species"), ("重新定义气候", "redefine climate"))),
    X("biology-8Be-3", type="mcq", id="q-bi-8Be-pa09", stem_zh="入侵一旦形成往往难清除，因此更应？", stem_en="Because removal is hard, it is more important to:",
      answer="a", exp_zh="预防物种进入新地区。", exp_en="Prevent species entering new areas.",
      options=opts(("预防物种进入新地区", "prevent species entering new areas"), ("鼓励放生", "encourage release"),
                   ("忽略运输", "ignore transport"), ("等到完全入侵再考虑", "wait until invasion is complete"))),
    X("biology-8Be-3", type="mcq", id="q-bi-8Be-pa10", stem_zh="较准确的说法是？", stem_en="The fairest statement is:",
      answer="d", exp_zh="并非每个新物种都严重破坏，但入侵后影响可能很大。", exp_en="Not every newcomer causes serious harm, but an invasion can have large effects.",
      options=opts(("每个新物种一天内毁掉地球", "every new species destroys Earth in a day"), ("新物种不能改变食物关系", "new species cannot change feeding relationships"),
                   ("只有实验室物种可入侵", "only laboratory species can invade"), ("不是每个新物种都严重破坏，但入侵后往往难清除", "not every new species causes serious harm, but an invasion is often hard to reverse"))),
    X("biology-8Be-1", type="short", id="q-bi-8Be-pa11", stem_zh="用一句话区分栖息地和生态系统。", stem_en="In one sentence, distinguish habitat and ecosystem.",
      answer="habitat is the place; ecosystem includes organisms, environment and interactions",
      accepted=["habitat is the place; ecosystem includes organisms, environment and interactions",
                "栖息地是生活的地方，生态系统还包括生物、非生物环境及相互作用", "栖息地侧重地方，生态系统包含相互作用"],
      answer_zh="栖息地是生物生活的地方；生态系统还包括非生物环境与相互作用。",
      answer_en="A habitat is the place an organism lives; an ecosystem also includes the non-living environment and interactions.",
      exp_zh="不要把两个词完全等同。", exp_en="Do not treat the two words as identical."),
])

COMP = add_extra_questions(C, [
    X("biology-8Bs-1", type="mcq", id="q-bi-comp-01", stem_zh="屈肘时通常？", stem_en="When the elbow bends, usually:",
      answer="b", exp_zh="肱二头肌收缩，肱三头肌舒张。", exp_en="Biceps contracts, triceps relaxes.",
      options=opts(("两块肌肉同时尽力推骨头", "both muscles push equally"), ("二头肌收缩，三头肌舒张", "biceps contracts, triceps relaxes"),
                   ("只有韧带收缩", "only ligaments contract"), ("肌肉把骨头推回去", "the muscle pushes the bone back"))),
    X("biology-8Bs-2", type="mcq", id="q-bi-comp-02", stem_zh="运输氧气主要靠？", stem_en="Oxygen is carried mainly by:",
      answer="a", exp_zh="红细胞。", exp_en="Red blood cells.",
      options=opts(("红细胞", "red blood cells"), ("血小板", "platelets"), ("肌腱", "tendons"), ("韧带", "ligaments"))),
    X("biology-8Bs-3", type="mcq", id="q-bi-comp-03", stem_zh="气体交换主要在？", stem_en="Gas exchange is mainly at the:",
      answer="c", exp_zh="肺泡。", exp_en="Alveoli.",
      options=opts(("胃", "stomach"), ("关节", "joints"), ("肺泡", "alveoli"), ("头发", "hair"))),
    X("biology-8Bs-4", type="mcq", id="q-bi-comp-04", stem_zh="扩散的净方向是从？", stem_en="Net diffusion is from:",
      answer="d", exp_zh="高浓度到低浓度。", exp_en="Higher to lower concentration.",
      options=opts(("低到高", "low to high"), ("只在金属中", "metals only"), ("无法在气体中发生", "never in gases"), ("高到低", "high to low"))),
    X("biology-8Bp-1", type="mcq", id="q-bi-comp-05", stem_zh="蛋白质主要用于？", stem_en="Protein is used mainly for:",
      answer="a", exp_zh="生长和修复。", exp_en="Growth and repair.",
      options=opts(("生长和修复", "growth and repair"), ("只运氧", "oxygen transport only"), ("替代所有水", "replacing all water"), ("形成气候", "forming climate"))),
    X("biology-8Bp-2", type="mcq", id="q-bi-comp-06", stem_zh="同样质量下能量通常最高的是？", stem_en="For the same mass, energy is usually highest in:",
      answer="b", exp_zh="脂肪。", exp_en="Fat.",
      options=opts(("水", "water"), ("脂肪", "fat"), ("空气", "air"), ("纤维作为最主要供能物质", "fibre as the main energy source"))),
    X("biology-8Bp-3", type="mcq", id="q-bi-comp-07", stem_zh="一氧化碳减少氧气运输，是因为它？", stem_en="Carbon monoxide reduces oxygen transport because it:",
      answer="c", exp_zh="与血红蛋白结合。", exp_en="Binds to haemoglobin.",
      options=opts(("把红细胞变成骨", "turns red cells into bone"), ("只改变发色", "only changes hair colour"),
                   ("与血红蛋白结合", "binds to haemoglobin"), ("增加无限氧气", "raises oxygen without limit"))),
    X("biology-8Bp-4", type="short", id="q-bi-comp-08", stem_zh="写出有氧呼吸的文字方程式。", stem_en="Write the word equation for aerobic respiration.",
      answer="glucose + oxygen -> carbon dioxide + water",
      accepted=["glucose + oxygen -> carbon dioxide + water", "glucose + oxygen → carbon dioxide + water", "葡萄糖+氧气→二氧化碳+水", "葡萄糖 + 氧气 → 二氧化碳 + 水"],
      answer_zh="葡萄糖 $+$ 氧气 $\\rightarrow$ 二氧化碳 $+$ 水", answer_en="glucose $+$ oxygen $\\rightarrow$ carbon dioxide $+$ water",
      exp_zh="并释放能量。", exp_en="Energy is released."),
    X("biology-8Bp-4", type="mcq", id="q-bi-comp-09", stem_zh="有氧呼吸发生在？", stem_en="Aerobic respiration occurs in:",
      answer="b", exp_zh="细胞中。", exp_en="Cells.",
      options=opts(("只在肺泡空腔", "the alveolar cavity only"), ("细胞中", "cells"), ("只在气管", "the trachea only"), ("关节腔", "the joint cavity"))),
    X("biology-8Be-1", type="mcq", id="q-bi-comp-10", stem_zh="生态系统包括？", stem_en="An ecosystem includes:",
      answer="a", exp_zh="生物、非生物环境及相互作用。", exp_en="Organisms, non-living environment and interactions.",
      options=opts(("生物、非生物环境及相互作用", "organisms, the non-living environment and interactions"),
                   ("只有一种动物", "only one animal"), ("只包括仪器", "apparatus only"), ("一块不含生物的岩石而已", "only a rock with no organisms"))),
    X("biology-8Be-2", type="mcq", id="q-bi-comp-11", stem_zh="食物链中毒素浓度往往最高的是？", stem_en="Toxin concentration is often highest in:",
      answer="d", exp_zh="顶端捕食者。", exp_en="The top predator.",
      options=opts(("不进食的岩石", "a rock that never feeds"), ("纯氧", "pure oxygen"), ("刚入水且不再传递者", "toxin that never transfers"), ("顶端捕食者", "the top predator"))),
    X("biology-8Be-3", type="mcq", id="q-bi-comp-12", stem_zh="入侵物种通常？", stem_en="An invasive species typically:",
      answer="c", exp_zh="迅速扩散并造成危害。", exp_en="Spreads rapidly and causes harm.",
      options=opts(("全无影响", "has no effect"), ("只活在试管里", "lives only in a test tube"),
                   ("迅速扩散并危害原有物种或栖息地", "spreads rapidly and harms native species or habitats"), ("一定是原有顶级捕食者", "must already have been the native top predator"))),
    X("biology-8Bs-2", type="mcq", id="q-bi-comp-13", stem_zh="血小板的功能是？", stem_en="Platelets are involved in:",
      answer="a", exp_zh="凝血。", exp_en="Clotting.",
      options=opts(("凝血", "clotting"), ("只运氧", "oxygen transport only"), ("形成关节", "forming joints"), ("全部有氧呼吸", "all of aerobic respiration"))),
    X("biology-8Be-1", type="mcq", id="q-bi-comp-14", stem_zh="栖息地指？", stem_en="A habitat is:",
      answer="b", exp_zh="生物生活的地方。", exp_en="The place where an organism lives.",
      options=opts(("血浆", "plasma"), ("生物生活的地方", "the place where an organism lives"),
                   ("呼吸方程式", "the respiration equation"), ("只是温度数字", "a temperature number only"))),
    X("biology-8Be-3", type="mcq", id="q-bi-comp-15", stem_zh="减少入侵风险，更应？", stem_en="To reduce invasion risk, it is better to:",
      answer="d", exp_zh="预防进入，不随意放生。", exp_en="Prevent arrival and not release pets.",
      options=opts(("鼓励放生", "encourage release"), ("忽略运输", "ignore transport"),
                   ("等到完全入侵再考虑", "wait until invasion is complete"), ("预防进入新地区，不随意放生", "prevent entry to new areas and not release pets"))),
])

for lesson in LESSONS:
    add_lesson(C, lesson)

add_sets(C, [
    dict(kind="practice", chapter="biology-8Bs", title_zh="本章练习 · 结构与功能", title_en="Chapter practice · Structure and function", qids=BS_PR, minutes=15),
    dict(kind="paper", chapter="biology-8Bs", title_zh="本章测试卷 · 结构与功能", title_en="Chapter test · Structure and function", qids=BS_PA, minutes=25),
    dict(kind="practice", chapter="biology-8Bp", title_zh="本章练习 · 生命过程", title_en="Chapter practice · Life processes", qids=BP_PR, minutes=15),
    dict(kind="paper", chapter="biology-8Bp", title_zh="本章测试卷 · 生命过程", title_en="Chapter test · Life processes", qids=BP_PA, minutes=25),
    dict(kind="practice", chapter="biology-8Be", title_zh="本章练习 · 生态系统", title_en="Chapter practice · Ecosystems", qids=BE_PR, minutes=12),
    dict(kind="paper", chapter="biology-8Be", title_zh="本章测试卷 · 生态系统", title_en="Chapter test · Ecosystems", qids=BE_PA, minutes=20),
], comprehensive=dict(
    id="paper-biology-8-comprehensive",
    title_zh="八年级生物综合测试卷", title_en="Grade 8 Biology comprehensive paper",
    qids=COMP, minutes=35, published="2026-11-12T09:00:00+08:00",
))

knowledge_bi = C.knowledge
questions_bi = C.questions
sets_bi = C.sets
