"""正文許可證張數的程式改寫（2026-11-24 建，用戶決定把 KrTxGNN／MyTxGNN 的做法移植到本站；結構照 COTxGNN 的同名檔，規則是本站丹麥文句型）。

正文裡「N gyldige (markedsførings)tilladelser」「Antal godkendelser: N」「Alle N tilladelser er gyldige」「N af de M tilladelser er gyldige」
這類 Lægemiddelstyrelsen 許可證張數敘述，由程式依許可證快照（snapshots/dk_licenses.json.gz 的 facts）改寫，每週資料更新後跟著改，
不逐筆寫查核紀錄（同 Tw／Kr／My：程式改寫的張數敘述是程式產生的正文）。

只改「句型明確、數字確定是本藥人用許可證張數」的地方，其餘一律不動：
  - 句子要有許可證名詞（tilladelse(r)、markedsføringstilladelse(r)、godkendelse(r)、registrering(er)、licens(er)）緊接在數字右邊
    （中間只可有 nationale／gyldige／danske 等形容詞），或數字左邊是「Antal godkendelser／tilladelser:」；
    沒有交互作用、試驗、文獻、劑量、年份等字樣。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、引言框、front matter；
    查核紀錄 replacement／anchor 所在的句子（改了紀錄會對不上）。
  - 整句不動（列在 skipped）：有保留（mindst、ufuldstændig、ikke komplet、kan være）、講證據包或查詢（indsamlede data、dataene viser、fundet、
    gennemgået）、相對數或子集（heraf、herunder, bl.a.、blandt, andre, yderligere, desuden, flere, kun）、劑型或廠商（tabletter、kapsler、
    injektion、oral、indehaves、producent…）、獸用、EU／EMA 集中許可；事實層 partial 的頁整頁不動。
  - 數字不動：顯示筆數（tabellen viser、her vises、de N første、「N af dem」）、劑量與年份。
角色看數字右側（同一子句內）：afregistrerede／annullerede…→註銷；gyldige→有效；for/til enkeltstofpræparater…→單方；
for/til kombinationspræparater→複方；兩者可疊（gyldige … for enkeltstofpræparater＝有效單方）；其餘→總數。
子句裡括號或「og de er gyldige／alle med status gyldig／alle kombinationspræparater」這類說「全部都是…」的字樣是前提：
  事實不符（說全部有效而有非有效、說全部單方而有複方…）整句不動、列 premise。
「N af de M tilladelser er gyldige」：N＝有效數、M＝總數。「Alle N tilladelser」：N＝總數。
數字已等於該角色的任一合理讀法就不動；不等於時各讀法相同才改，不同就列 ambiguous。
跨過 0／1（單複數要跟著變：1 gyldig tilladelse ↔ 2 gyldige tilladelser）不改、列 plural；文字數詞（én、to、tre、begge…）不改、
跟事實不符時列 wordnum；改了要寫查核紀錄。
同一行只要有一句含許可證數字而被略過，整行都不動（免得前後句數字對不上）。
"""
from __future__ import annotations

import re

from . import site as C

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÆØÅ*\[(>»\"-]|\d)")
NUM = re.compile(r"(?<![\w.,/-])(\d+)(?![\w/%-]|[.,]\d)")
ADJ = r"(?:(?:nationale?|danske?|gyldige|gyldigt?|aktive|registrerede|humane|separate|forskellige),?\s+)"
LIC_N = r"(?:enkeltstof-?s?)?(?:markedsførings)?(?:tilladelse(?:r|n|rne)?|godkendelse(?:r|n|rne)?)|registrering(?:er|en|erne)?|licens(?:er|en)?|enkeltstofs?(?:produkt|præparat)licens\w*"
NOUN_RIGHT = re.compile(rf"\s*{ADJ}*(?:{LIC_N})\b", re.I)
ANTAL_LEFT = re.compile(r"\b(antal(?:let)? (?:af )?(?:markedsførings)?(?:tilladelser|godkendelser|registreringer)(?: er)?|i alt)\s*[:]?\s*$", re.I)
WORDNUM = {"én": 1, "ét": 1, "to": 2, "tre": 3, "fire": 4, "fem": 5, "seks": 6, "syv": 7, "otte": 8, "ni": 9,
           "ti": 10, "elleve": 11, "tolv": 12, "begge": 2}
WORD_RX = re.compile(r"\b(" + "|".join(WORDNUM) + r")\b" + rf"(?=\s*{ADJ}*(?:{LIC_N}|enkeltstof\w*(?:præparat|produkt)\w*|kombinationspræparat\w*)\b)", re.I)
NOT_LICENSE = re.compile(r"interaktion|forsøg|studie|artik|PMID|NCT|patient|tilfælde|bivirkning|\bmg\b|\bml\b|%|\bår\b|måned|uge|dage?\b|"
                         r"kandidat|forudsig|score|rang|DrugBank|ChEMBL|PubMed|ClinicalTrials|publikation|receptor|veterinær|\bVet\.|"
                         r"\bEMA\b|\bEU\b|central|Taiwan|TFDA|Oprindeligt stod der", re.I)
HEDGED = re.compile(r"\bmindst\b|ufuldstændig|ikke (er )?(komplet|fuldstændig)|delvis|\bkan (være|have)\b|muligvis|formentlig|"
                    r"indsamlede data|dataene viser|data, der er indsamlet|fundet|fandt|gennemgå|identificeret|\bheraf\b|\bherunder\b|"
                    r"\bbl\.\s?a\.|\bblandt\b|\bandre\b|\banden\b|\bandet\b|yderligere|\bdesuden\b|\bflere\b|\bkun\b|\bogså\b|\bsjette\b|"
                    r"indehave|indehaver|producent|fremstil|tilhører|\bA/S\b|\bApS\b|\bGmbH\b|\bLtd\b|\bB\.V\.|"
                    r"tablet|kapsl|injektion|infusion|\boral\w*|kutan|creme|salve|gel\b|øjendråbe|næsespray|inhal|suppositor|"
                    r"opløsning|suspension|plaster|pulver|sirup|rektal|vaginal|administrationsvej|lægemiddelform", re.I)
DISPLAY_LEFT = re.compile(r"(viser|vises|vist|ses|listet|opført|første|ovenfor|nedenfor|tabellen)\s+(?:de\s+|her\s+)?(?:\w+\s+)?$", re.I)
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)
VALID_W = r"gyldige?|gyldigt"
CANC_W = r"afregistrerede|annullerede|tilbagekaldte|udløbne|inaktive"
SINGLE_W = r"enkeltstof\w*|monopræparat\w*|mono-?præparat\w*|enkelt indholdsstof|eneste aktive stof|ét aktivt stof|ét aktivt indholdsstof"
COMBO_W = r"kombinationspræparat\w*|kombinationsprodukt\w*"


def _clause(s, b):
    """數字右邊到子句結尾（; 、. 、句尾）為止；括號照算進去"""
    m = re.search(r"[;.](?=\s|$)|$", s[b:])
    return s[b:b + m.start()]


def _direct(right):
    """數字右側直接修飾名詞的角色：valid／cancelled／single／combo 的集合"""
    out = set()
    m = re.match(rf"\s*(?:(?:nationale|danske|humane)\s+)?(?:(?P<v>{VALID_W})|(?P<c>{CANC_W}))\s+", right, re.I)
    if m:
        out.add("valid" if m.group("v") else "cancelled")
    if re.match(rf"\s*(?:{ADJ})*(?:{SINGLE_W})", right, re.I):
        out.add("single")
    if re.match(rf"\s*(?:{ADJ})*(?:{COMBO_W})", right, re.I):
        out.add("combo")
    n = NOUN_RIGHT.match(right)
    if n:
        after = right[n.end():]
        if re.match(rf"\s+(?:for|til)\s+(?:lægemidler med\s+|lægemidler til mennesker med\s+|præparater med\s+)?(?:{SINGLE_W})", after, re.I):
            out.add("single")
        if re.match(rf"\s+(?:for|til)\s+(?:{COMBO_W})", after, re.I):
            out.add("combo")
        if re.match(rf"\s+(?:er|var)\s+(?:{VALID_W})\b", after, re.I):
            out.add("valid")
        if re.match(rf"\s+(?:er|blev|var)\s+(?:{CANC_W}|afregistreret|annulleret|tilbagekaldt)\b", after, re.I):
            out.add("cancelled")
    return out


def _premise(clause, direct):
    """子句裡說「全部都是…」的字樣（括號、og de er gyldige、alle med status gyldig、alle kombinationspræparater…），扣掉直接修飾的部分"""
    out = set()
    lo = clause.lower()
    if "valid" not in direct and re.search(rf"\b({VALID_W})\b", lo) and not re.search(r"\bikke (er )?gyldig|\bingen\b", lo):
        out.add("valid")
    if "single" not in direct and re.search(SINGLE_W, lo):
        out.add("single")
    if "combo" not in direct and re.search(COMBO_W, lo):
        out.add("combo")
    if re.search(rf"\b(ingen|uden) (\w+ )?(annuller|afregistrer|tilbagekald)", lo):
        out.add("none_cancelled")
    return out


def _value(role, f):
    t, v = f.get("total"), f.get("valid")
    st, vs = f.get("single_total"), f.get("valid_single")
    ct = None if t is None or st is None else t - st
    cv = None if v is None or vs is None else v - vs
    return {"total": t, "valid": v, "cancelled": None if t is None or v is None else (f.get("cancelled") or 0),
            "single": st, "combo": ct, "valid_single": vs, "valid_combo": cv}.get(role)


def _role_of(direct):
    if "cancelled" in direct:
        return "cancelled"
    if "valid" in direct:
        return "valid_single" if "single" in direct else "valid_combo" if "combo" in direct else "valid"
    if "single" in direct:
        return "single"
    if "combo" in direct:
        return "combo"
    return "total"


def _premise_ok(role, prem, f):
    t, v, st, vs = f.get("total"), f.get("valid"), f.get("single_total"), f.get("valid_single")
    sub_valid = role.startswith("valid")
    if ("valid" in prem or "none_cancelled" in prem) and not sub_valid and v != t:
        return False
    if "single" in prem:
        if role in ("total", "valid") and (vs if role == "valid" else st) != (v if role == "valid" else t):
            return False
    if "combo" in prem:
        if role in ("total", "valid") and (vs if role == "valid" else st):
            return False
        if role == "single":
            return False
    if "valid" in prem and role in ("single", "combo"):
        sv = vs if role == "single" else (None if v is None or vs is None else v - vs)
        if sv != _value(role, f):
            return False
    return True


def _readings(role, prem, f, explicit):
    """(可接受的讀法集合, 要改成的值或 None＝讀法不一)"""
    t, v = f.get("total"), f.get("valid")
    if role == "total":
        if explicit or "valid" in prem or "none_cancelled" in prem:
            return {t}, t
        return {t, v}, t if t == v else None
    x = _value(role, f)
    return {x}, x


def rewrite_sentence(sent, f):
    """回傳 (新句子, 跳過理由或 None)。"""
    if not re.search(LIC_N, sent, re.I):
        return sent, None
    if NOT_LICENSE.search(sent):
        return sent, None
    cands = []
    for m in NUM.finditer(sent):
        a, b = m.start(1), m.end(1)
        left, right = sent[max(0, a - 60):a], sent[b:]
        if re.match(r"\s*af\s+(de|dem|i alt)\b", right, re.I) and re.search(r"(viser|vises|ses|vist|første|tabellen|her)\b", sent, re.I):
            continue  # 「tabellen viser 4 af dem」「Dette er 5 af i alt 20」：顯示筆數
        if DISPLAY_LEFT.search(left) or re.match(r"\s+første\b", right, re.I):
            continue
        mof = re.match(r"\s*af\s+(?:de\s+|i alt\s+)?(\d+)\b", right, re.I)
        if mof:  # 「N af de M tilladelser er gyldige」：N 的角色看 M 後面
            direct = _direct(right[mof.end():])
            if not NOUN_RIGHT.match(right[mof.end():]):
                continue
            cands.append((m, _role_of(direct) if direct else "valid" if re.search(VALID_W, right, re.I) else None,
                          _premise(_clause(sent, b), direct), True))
            continue
        if re.search(r"\baf\s+(de\s+|i alt\s+)?$", left, re.I) and NOUN_RIGHT.match(right):
            cands.append((m, "total", set(), True))
            continue
        if NOUN_RIGHT.match(right) or (ANTAL_LEFT.search(left) and re.match(r"\s*(\(|$|[;,.]|\s*" + ADJ + r"*(?:" + LIC_N + r"))", right, re.I)):
            direct = _direct(right)
            if re.search(r"\balle\s+$", left, re.I):  # 「Alle N tilladelser er gyldige」：N＝總數、說全部有效
                prem = _premise(_clause(sent, b), set())
                cands.append((m, "total", prem, True))
                continue
            role = _role_of(direct)
            cands.append((m, role, _premise(_clause(sent, b), direct), False))
    words = [w for w in WORD_RX.finditer(sent)]
    if not cands and not words:
        return sent, None
    if HEDGED.search(sent):
        return sent, "hedged/subset"
    for w in words:  # 文字數詞：不改；跟事實不符就列出
        n = WORDNUM[w.group(1).lower()]
        if n not in {f.get("total"), f.get("valid"), f.get("single_total"), f.get("valid_single"),
                     None if f.get("total") is None or f.get("single_total") is None else f["total"] - f["single_total"]}:
            return sent, "wordnum"
    explicit = sum(1 for c in cands if c[1] not in (None, "total")) > 0
    subs = []
    for m, role, prem, expl in cands:
        if role is None:
            return sent, "ambiguous"
        old = int(m.group(1))
        ok, val = _readings(role, prem, f, explicit or expl)
        if not _premise_ok(role, prem, f):
            return sent, "premise"
        if old in ok:
            continue
        if val is None:
            return sent, "ambiguous"
        if old <= 1 or val <= 1:
            return sent, "plural"
        subs.append((m, val))
    if not subs:
        return sent, None
    out, pos = [], 0
    for m, v in subs:
        out.append(sent[pos:m.start(1)])
        out.append(str(v))
        pos = m.end(1)
    out.append(sent[pos:])
    return "".join(out), None


def _line(ln, f, protect, skipped):
    if ln.startswith(("|", "#", ">")) or not ln.strip():
        return ln
    if any(rx.match(ln.strip()) for rx in C.PROGRAM_LINES):
        return ln
    parts = SENT_SPLIT.split(ln)
    seps = SENT_SPLIT.findall(ln)
    new, held = [], False
    for s in parts:
        if any(p and (p in s or s in p) for p in protect):
            new.append(s)
            continue
        ns, why = rewrite_sentence(s, f)
        if why:
            skipped.append((why, s.strip()))
            held = True
        new.append(ns)
    if held:  # 同一行有句子判斷不了：整行不動，免得改了一句、旁邊的句子對不上
        return ln
    out = new[0]
    for sep, s in zip(seps, new[1:]):
        out += sep + s
    return out


def rewrite(text, facts, protect=()):
    """text：整頁 markdown。facts：快照的 facts。回傳 (新內容, skipped)。front matter、查核框、程式區塊、表格不動。"""
    skipped = []
    if not facts or facts.get("partial") or facts.get("total") is None:
        return text, skipped
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines = [ln if "\x00" in ln else _line(ln, facts, protect, skipped) for ln in body.split("\n")]
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
