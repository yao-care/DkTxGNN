"""Lægemiddelstyrelsen「AktiveSubstanser」欄的成分切分與單方／複方判定（2026-11-12）。

原本的判定（reviewer/drug_evidence_pack.py）用「;;」切成分，但本站證據包的成分欄是 xlsx 原文、以「, 」分隔，
所以每筆都被判成單方（事實層 single_total＝total；thiamine、oxytetracycline、cysteine 的複方都被算成單方）。

規則：
1. 只切括號外、後面接空白的逗號（「Follitropin Alfa (biosyntetisk, rekombinant)」「2,5-hydrat」不切）。
2. 修飾語併回前一段：小寫開頭的片段（humant、inaktiveret、renset、rig på omega-3-syrer、middelkædelængde、toxoid…）
   與大寫修飾語（VANDFRIT、RENSET…）；例外是「單一字、帶鹽類字尾、本身不是純鹽類詞」的小寫片段
   （indacaterolmaleat：Ultibro 的第二個成分）算成分。
3. 同一成分的不同寫法算一個（基底與鹽類一起列：「Cabozantinib, Cabozantinib (S)-Malat」「NITROFURANTOIN,
   Nitrofurantoinmonohydrat」「Insulin aspart, insulin aspart protamin」）：去括號、去空白後，一個是另一個的開頭，
   或共同開頭至少 10 個字母。
"""
import re

UPPER_QUALIFIERS = {"VANDFRIT", "VANDFRI", "RENSET", "RAFFINERET", "HYDROGENERET", "KONCENTRERET"}
SALT_SUFFIX = re.compile(r"(maleat|fumarat|chlorid|bromid|sulfat|acetat|citrat|tartrat|mesilat|mesylat|besilat|succinat|"
                         r"phosphat|fosfat|nitrat|lactat|gluconat|natrium|kalium|calcium)$")
PURE_SALT = re.compile(r"^(mono|di|tri|sesqui|hemi)?hydrat$|^vandfri(t)?$")


def split_ingredients(s):
    out, depth, cur = [], 0, ""
    s = str(s or "")
    for i, ch in enumerate(s):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if ch == "," and depth == 0 and s[i + 1:i + 2] == " ":
            out.append(cur)
            cur = ""
            continue
        cur += ch
    out.append(cur)
    parts = []
    for p in (x.strip() for x in out):
        if not p:
            continue
        low_qual = p[:1].islower() and not (" " not in p and len(p) >= 8 and SALT_SUFFIX.search(p) and not PURE_SALT.match(p))
        if parts and (low_qual or p.upper() in UPPER_QUALIFIERS and p == p.upper() or p in ("vandfrit", "renset")):
            parts[-1] = f"{parts[-1]}, {p}"
        else:
            parts.append(p)
    return parts


def _key(p):
    return re.sub(r"[^a-zæøå0-9]", "", re.sub(r"\([^)]*\)", "", p.lower().split(",")[0]))


def _same(a, b):
    a, b = _key(a), _key(b)
    if not a or not b:
        return False
    if a.startswith(b) or b.startswith(a):
        return True
    n = 0
    for x, y in zip(a, b):
        if x != y:
            break
        n += 1
    return n >= 10


def substances(s):
    """去掉同一成分的重複寫法後的成分清單"""
    out = []
    for p in split_ingredients(s):
        if not any(_same(p, q) for q in out):
            out.append(p)
    return out


def kind(s):
    return "single" if len(substances(s)) <= 1 else "combo"
