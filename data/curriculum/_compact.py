"""Helpers to format compact bilingual lesson fields consistently."""

def bullets(pairs):
    """pairs: list of (zh, en) -> (kp_zh, kp_en)"""
    zh = "\n".join(f"- {a}" for a, b in pairs)
    en = "\n".join(f"- {b}" for a, b in pairs)
    return zh, en


def diffs(pairs):
    zh = "\n".join(f"- **{a}**" if not a.startswith("**") else f"- {a}" for a, b in pairs)
    en = "\n".join(f"- **{b}**" if not b.startswith("**") else f"- {b}" for a, b in pairs)
    return zh, en


def body(zh_explain, en_explain, zh_ex, en_ex):
    return (
        zh_explain.strip() + "\n\n## 例题\n\n" + zh_ex.strip(),
        en_explain.strip() + "\n\n## Worked example\n\n" + en_ex.strip(),
    )
