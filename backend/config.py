from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
CURRICULUM_DIR = DATA_DIR / "curriculum"
USER_DB = DATA_DIR / "user.db"
SITE_CONFIG_PATH = ROOT / "site.config.json"
FRONTEND_DIST = ROOT / "frontend" / "dist"

_DEFAULTS = {
    "name_en": "Edmond Study Hub",
    "name_zh": "Edmond 学习站",
    "subtitle_en": "Cambridge Lower Secondary & IGCSE · Year 8",
    "subtitle_zh": "剑桥中学初级阶段与 IGCSE · 八年级",
    "port": 8787,
}


def load_site_config() -> dict:
    cfg = dict(_DEFAULTS)
    if SITE_CONFIG_PATH.is_file():
        cfg.update(json.loads(SITE_CONFIG_PATH.read_text(encoding="utf-8")))
    return cfg


def load_json(name: str):
    path = CURRICULUM_DIR / name
    return json.loads(path.read_text(encoding="utf-8"))
