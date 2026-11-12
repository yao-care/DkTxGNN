"""本站（DkTxGNN）查核機制的在地設定（2026-11-12 建）：頁面文字、資料來源、頁首規則、許可證格式、歷史刪改提交。

同目錄 page_format／licenses／withdrawn 與 scripts/apply_drug_reviews.py、build_license_snapshot.py、reviews_from_edits.py、
check_original_indications.py 都讀這裡；核心流程比照 TwTxGNN 與 UsTxGNN，只有這份是本站自己的寫法。
本站的市場資料是 Lægemiddelstyrelsen（丹麥藥品管理局）已許可藥品清單（11 碼許可證號；獸用＝ATC Q 開頭或品名含 Vet.），
頁面文字用丹麥文。本站沒有程式產生的許可證表（市場段落的表是報告寫的），所以沒有程式區塊標記。
"""
import re

SITE = "DkTxGNN"
CODE = "dk"
BUNDLE_KEY = "thaifda"  # 證據包裡本站市場資料的鍵（收集器沿用初始化包的欄位名）

# ---------- 頁首等級（page_format） ----------
LEVEL_LABELS = ["Evidensniveau", "Evidensniveau (rang 1)", "Evidensgrad"]  # 總覽表的證據等級欄名（2026-11-12 實測）
HEADER_LABEL = r"Evidensniveau"
WITHDRAWN = r"Trukket tilbage"
# 頁首規則：2026-11-12 實測 748 頁有總覽等級，頁首全部＝格裡第一個等級（主預測）；整格取最高會有 10 頁不同
HEADER_RULE = "first"
DESC_LEVEL_RE = re.compile(r"evidensniveau (L[1-5]|N/A)\b(?![–-]L)", re.I)


def desc_level_text(level):
    return "kun kendte anvendelser" if level == "N/A" else f"evidensniveau {level}"


DISCLAIMER_RE = re.compile(r"^## Ansvarsfraskrivelse\b", re.M)

# ---------- 頁面文字（apply_drug_reviews） ----------
T = {
    "label": {"correct": "Rettelse ved gennemgang", "annotate": "Note ved gennemgang", "rereview": "Afventer fornyet vurdering",
              "rereview_result": "Resultat af fornyet vurdering"},
    "action": {"correct": "Rettet", "annotate": "Note tilføjet", "rereview": "Markeret til fornyet vurdering",
               "section": "Afsnit med kilde tilføjet", "rereview_result": "Fornyet vurdering afsluttet",
               "header_level": "Evidensniveau i sidehovedet genberegnet ud fra Hurtigt overblik",
               "description_level": "Evidensniveau i sidebeskrivelsen sat til sidehovedets niveau"},
    "verdict": {"maintain": "Fastholdt", "downgrade": "Nedgraderet", "upgrade": "Opgraderet", "withdraw": "Trukket tilbage"},
    "log_head": "## Gennemgangslog",
    "log_cols": "| Gennemgået | Punkt | Handling | Kilde |",
    "head": "> **{label} ({date})**: ",
    "originally": "Oprindeligt stod der: \"{claim}\"",
    "source": "Kilde: {src}.",
    "decision": "Anbefalet beslutning: {note}",
    "level_same": "evidensniveau {o} uændret",
    "level_change": "evidensniveau {o} → {n}",
    "table_updated": (" {labels} på denne side er opdateret efter den fornyede vurdering; de oprindelige værdier står i "
                      "gennemgangsloggen nedenfor."),
    "rereviewed": "Markeret til fornyet vurdering → vurderet igen (se resultatet af den fornyede vurdering)",
    "hdr": "Evidensniveau i sidehovedet genberegnet ud fra Hurtigt overblik ({o} → {n})",
    "hdr_withdraw": "Hovedforudsigelsen blev trukket tilbage ved fornyet vurdering; evidensniveau i sidehovedet genberegnet ({o} → {n})",
    "listed_under": ", nu opført under \"{t}\"",
    "rr": "Fornyet vurdering: {v}, {c}",
    "tu": "; {l}: \"{a}\" → \"{b}\"",
    "desc": ("Sidebeskrivelse: \"evidensniveau {o}\" ændret til \"{n}\" (følger sidehovedets niveau; anden tekst uændret, "
             "originalen gemt i loggen)"),
    "revised": " (revideret {d}; tidligere version gemt i loggen)",
    "superseded": "Erstattet af programgenereret tilladelsestabel (oprindeligt: {a})",
    "regen": "Findes ikke længere, efter at rapporten blev genereret igen ({d}: {n}; oprindeligt: {a})",
    "prog": "Findes ikke længere efter en programrettelse ({d}: {n}; oprindeligt: {a})",
    "wd": "Gennemgang trukket tilbage ({d}: {n}; oprindeligt: {a})",
    "intro": ("Nedenfor er gennemgangsloggen for denne side: udsagn kontrolleret mod Lægemiddelstyrelsens liste over godkendte "
              "lægemidler. Rettelser er begrænset til grundlæggende faktuelle udsagn; modelforudsigelser, evidensniveauer og "
              "konklusioner er ikke omskrevet."),
    "intro_levels": ("Nedenfor er gennemgangsloggen for denne side; evidensniveauet i sidehovedet følger Hurtigt overblik. "
                     "Modelforudsigelser, oversigtstabellen og konklusioner er ikke omskrevet."),
    "intro_rr": ("Nedenfor er gennemgangsloggen for denne side. Rettelser er begrænset til grundlæggende faktuelle udsagn, og "
                 "modellens forudsigelsestekst er ikke omskrevet; evidensniveauer og beslutninger er kun ændret af et resultat af "
                 "fornyet vurdering (nedgradering, opgradering eller tilbagetrækning), med de oprindelige værdier nedenfor."),
}

# ---------- 許可證（licenses、build_license_snapshot） ----------
# 市場段落標題寫法很多（2026-11-12 實測：Information om det danske marked、Markedsinformation for／i Danmark、
# Oplysninger om …、Dansk markedsinformation、Denmark Market Information …）；N/A 頁的報告大標題（Kendte anvendelser og …）不算
MARKET_SEC = re.compile(r"^## (?!.*Kendte anvendelser)(?=.*(?:marked|Market))(?=.*(?:[Dd]ansk|Danmark|Denmark)).*$")
ID_RE = re.compile(r"\b\d{11}\b")  # Lægemiddelstyrelsen 許可證號（2026-11-12 依證據包實測：全部 11 碼數字）


# 事實層（依成分重建）漏收、但 Lægemiddelstyrelsen 已許可清單確有本藥成分的許可證號：{頁: {號碼: 依據}}（gate 視為本藥號碼）
EXTRA_OWN = {
    "cysteine": {"28107076923": "data/raw/danish_medicines.xlsx（data-20261105-231027）：Pedismof Preterm，AktiveSubstanser 含 Cystein；"
                                "同系列 Pedismof、Pedismof Infant 已在事實層，Preterm 漏收（2026-11-12 人工對照）"},
}


def own_ids(tf):
    return sorted({str(r.get("license_id") or "").strip() for r in tf.get("records") or [] if r.get("license_id")})


# ---------- 刪改轉紀錄（reviews_from_edits） ----------
# 2026-10-31～11-06 的許可證刪改（git log docs/_drugs；排程狀態格 7b06fe8eb、欄位名統一、排除表、AI 重產、description、表格空行不算）
COMMITS = ["c57b56f26", "96dc2e6a1", "47c61b3a4"]
# 期間內以 AI 整份重產報告或套排除表重寫段落的提交
REGEN_COMMITS = ["666777573", "0083fa7c5", "cd85608fc", "f1449cd15", "6b61328c0", "48f665477", "0cb31009a", "b7f7e2bbf",
                 "1bfec7fc4", "521af6aca"]
# 依錯配事實刪句、之後修正事實的頁：這些刪句不是錯誤更正，整頁不轉紀錄（gallium：c57b56f26 依錯配事實刪掉兩處「丹麥無許可」，
# 96dc2e6a1 修正事實為 0 張、6266374ab 還原其中一句；另一處（"Lægemidlet er ikke i øjeblikket tilgængeligt …"）沒有還原，頁面暫不動）
RESTORED = {"gallium.md": "c57b56f26 依錯配事實刪句，96dc2e6a1 修正事實、6266374ab 部分還原"}
SOURCES = [{"title": "Lægemiddelstyrelsen: liste over godkendte lægemidler",
            "url": "https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/"}]
SENT = re.compile(r'(?<=[.!?])\s+(?=[A-ZÆØÅ0-9(*"\[])|\n')
PROGRAM_LINES = []
CLASSIFY = [
    ("tw", re.compile(r"Taiwan|TFDA", re.I)),
    ("vet", re.compile(r"veterinær|\bVet\.", re.I)),
    ("cancel", re.compile(r"ikke (længere )?(markedsført|godkendt|registreret)|ingen (gyldige )?(markedsførings)?tilladelse|"
                          r"\bnul markedsføringstilladelser|afregistreret|tilbagekaldt|udløbet|ophørt", re.I)),
    ("count", re.compile(r"\d+\s*(gyldige )?(markedsførings)?tilladelse|alle [^.]{0,40}gyldige|\bgyldig", re.I)),
    ("holder", re.compile(r"producent|indehaver|fremstill", re.I)),
    ("combo", re.compile(r"enkeltstof|kombinationspræparat|kombination", re.I)),
]
SUMMARY = "Fjernet: \"{text}\""
REGEN_NOTE = "rapporten blev genereret igen i november 2026 og indeholder ikke længere dette udsagn"


def reason_kind(reason):
    """人工清單（scripts/license_sentence_fixes.json）的中文理由 → 類別；判斷不了回 None（改用被刪文字分類）"""
    if re.search(r"台灣|TFDA|模板殘留", reason):
        return "tw"
    if re.search(r"製造商|持有人|許可持有", reason):
        return "holder"
    if re.search(r"獸用", reason):
        return "vet"
    if re.search(r"單方|複方", reason):
        return "combo"
    return "count" if re.search(r"張|有效|總數|nul|矛盾", reason) else None


def _fig(fc):
    if not fc or fc.get("total") is None:
        return ""
    return (f" Lægemidlet har {fc['total']} markedsføringstilladelse{'r' if fc['total'] != 1 else ''} (gyldige: "
            f"{fc.get('valid') or 0}); de aktuelle tal står i Hurtigt overblik og i tabellen under markedsinformationen.")


def note_for(kind, date, fc):
    d = f"Lægemiddelstyrelsens liste over godkendte lægemidler, genopbygget efter aktivt stof den {date}"
    if kind == "tw":
        return "Fjernet: resterende skabelontekst om Taiwans TFDA, som ikke vedrører denne danske side."
    if kind == "vet":
        return (f"Fjernet: udsagnet om veterinære og humane tilladelser passede ikke med {d}, hvor veterinærlægemidler "
                "(ATC-kode Q eller \"Vet.\" i navnet) er skilt ud." + _fig(fc))
    if kind == "cancel":
        return (f"Fjernet: det stod, at lægemidlet ikke var godkendt eller markedsført i Danmark, eller at tilladelsen var udløbet, "
                f"hvilket ikke passer med {d}." + _fig(fc))
    if kind == "count":
        return f"Fjernet: antallet eller status af markedsføringstilladelser passede ikke med {d}." + _fig(fc)
    if kind == "holder":
        return f"Fjernet: oplysningen om producent eller indehaver af tilladelsen passede ikke med {d}."
    if kind == "combo":
        return f"Fjernet: beskrivelsen af enkeltstof- eller kombinationspræparater passede ikke med {d}." + _fig(fc)
    return f"Fjernet: det var i modstrid med {d}." + _fig(fc)


# ---------- 原適應症交叉驗證（check_original_indications） ----------
ORIG_LABELS = ["Oprindelig indikation"]
ORIG_NONE_RE = re.compile(r"^\s*(ikke (registreret|angivet|oplyst|tilgængelig)|ingen|—|-|N/A)", re.I)
ORIG_SPLIT_RE = re.compile(r"[;,/()]+|\bog\b|\beller\b", re.I)
