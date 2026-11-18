"""Grade 9 (IGCSE Year 1) seed content. Initial draft — see data/README.md."""
from __future__ import annotations

from .biology import SPEC as BIOLOGY
from .chemistry import SPEC as CHEMISTRY
from .chinese import SPEC as CHINESE
from .computer_science import SPEC as COMPUTER_SCIENCE
from .economics import SPEC as ECONOMICS
from .english import SPEC as ENGLISH
from .mathematics import SPEC as MATHEMATICS
from .physics import SPEC as PHYSICS
from .deepen import deepen
from .engine import build_subject

SPECS = (
    CHINESE, MATHEMATICS, ENGLISH, COMPUTER_SCIENCE,
    ECONOMICS, PHYSICS, CHEMISTRY, BIOLOGY,
)


def collect():
    knowledge, questions, sets, units = [], [], [], []
    for spec in SPECS:
        k, q, s, u = build_subject(deepen(spec))
        knowledge.extend(k)
        questions.extend(q)
        sets.extend(s)
        units.extend(u)
    return knowledge, questions, sets, units
