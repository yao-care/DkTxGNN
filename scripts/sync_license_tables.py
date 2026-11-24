"""藥物頁市場段落（site.MARKET_SEC，例「## Markedsinformation for Danmark」「## Information om det danske marked」）的
許可證表改由程式依證據包產生（2026-11-24，用戶決定；全程不用 AI）。

為什麼：市場段落原本是報告（AI）寫的自由格式表（欄名有十幾種寫法、「Godkendt indikation」欄全是「Ikke angivet」、
沒有狀態欄或狀態寫死），Lægemiddelstyrelsen 的清單每週變，表上的號碼與狀態就跟事實矛盾，checker 擋下整頁、要人處理。
改成程式表後，每週排程（scripts/license_adapter.py 的 sync_tables）與建快照（scripts/build_license_snapshot.py 結尾）自動重排。
做法比照 COTxGNN／DETxGNN／SgTxGNN 的同名程式：
- 段落裡第一張表（不論原欄位）換成
  「| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |」。
  欄位全取證據包 thaifda.records（Lægemiddelstyrelsen「Liste over godkendte lægemidler」原文，丹麥文、不翻譯）：
  license_id（Drugid）、brand_name_en（Navn）、dosage_form（Lægemiddelform）、ingredients（AktiveSubstanser）；
  site.EXTRA_OWN 人工確認的補充號碼一併列（事實層也算它）。
- 狀態（Status 欄）照事實層的分類（records 的 license_status，scripts/license_adapter.py 寫入）：沒有 license_status＝在現行清單
  →「Gyldig」；cancelled（撤銷清單有撤銷日，或 EMA 確認撤回）→「Afregistreret」；not_marketed（例 Oxbryta：EMA 暫停）→ 證據包 status 原文
  （「Suspenderet (EMA)」）；其他→「Status ukendt」。排序：Gyldig → 核准未上市 → 未知 → Afregistreret，同一類照證據包原順序。
- 獸用許可（thaifda.veterinary_records：ATC Q 開頭或品名含 Vet.）不在表上、事實層也不算；有的話表下另加一句程式說明張數（VET_LINE）。
- 列數：原表列數與 min(5, 總數) 取大（最多 20）；段落裡有報告寫的「表上列了幾筆」說明句（vises／viser／tabellen／de N første…）
  時照原表列數，免得說明句跟表對不上。重排時以頁面上現有程式表的列數為準，所以每週重排列數不變。
- 表下一句程式說明（SHOW）：列數＝總數「Tabellen viser alle N …」，較少「Tabellen viser N af M …」，
  證據包只收了部分紀錄（total_matches 大於收錄筆數，事實層 partial）時「Tabellen viser N af mindst K …」（K＝收錄筆數，同概覽表張數列的 mindst）。
- 沒有任何人用紀錄時改一句 NONE_LINE。段落裡沒有表的頁在標題下補程式區塊。表以外的報告文字不動
  （正文張數由 scripts/rewrite_license_counts.py 依事實層改寫）。
程式區塊標記：程式產生的表（連同 SHOW 句，或 NONE_LINE）前後各一行「<!-- licenses:begin -->」「<!-- licenses:end -->」；
gate（src/dktxgnn/regulatory/site.py 的 program_block_problems）依 snapshots/dk_licenses.json.gz 檢查程式區塊＝快照重算的結果。
用法（repo 根目錄）：
  python3 scripts/sync_license_tables.py [--dry-run] [--check] [頁 ...]      # 依證據包（要先還原 data/）
  python3 scripts/sync_license_tables.py --from-snapshot [--check] [頁 ...]  # 依快照（不需要 data/；apply_drug_reviews、建快照結尾用）
"""
import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dktxgnn.regulatory import site as C  # noqa: E402

SEC_RE = C.MARKET_SEC
HEAD = ["| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |",
        "|---------|------|------|------|------|"]
SRC = "Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler"
NONE_LINE = f"{SRC[0].upper()}{SRC[1:]} indeholder ingen markedsføringstilladelser til humane lægemidler med dette aktive stof."
SHOW_ALL1 = f"Tabellen viser den eneste markedsføringstilladelse til et humant lægemiddel med dette aktive stof i {SRC}."
SHOW_ALL = "Tabellen viser alle {m} markedsføringstilladelser til humane lægemidler med dette aktive stof i " + SRC + "; gyldige tilladelser står først."
SHOW_SOME = "Tabellen viser {n} af {m} markedsføringstilladelser til humane lægemidler med dette aktive stof i " + SRC + "; gyldige tilladelser står først."
SHOW_PART = ("Tabellen viser {n} af mindst {m} markedsføringstilladelser til humane lægemidler med dette aktive stof i " + SRC +
             "; gyldige tilladelser står først. Dataene i denne rapport omfatter kun en del af tilladelserne.")
VET_LINE1 = ("Dataene indeholder desuden 1 tilladelse til et veterinærlægemiddel (ATC-kode Q eller »Vet.« i navnet), "
             "som ikke er medtaget i tabellen eller i antallet ovenfor.")
VET_LINE = ("Dataene indeholder desuden {v} tilladelser til veterinærlægemidler (ATC-kode Q eller »Vet.« i navnet), "
            "som ikke er medtaget i tabellen eller i antallet ovenfor.")
VET_NONE1 = "Dataene indeholder 1 tilladelse til et veterinærlægemiddel (ATC-kode Q eller »Vet.« i navnet)."
VET_NONE = "Dataene indeholder {v} tilladelser til veterinærlægemidler (ATC-kode Q eller »Vet.« i navnet)."
SHOW_RX = re.compile(r"^Tabellen viser (den eneste|alle \d+|\d+ af (mindst )?\d+) markedsføringstilladelse(r)? til (et )?human[et]? lægemid")
VET_RX = re.compile(r"^Dataene indeholder (desuden )?\d+ tilladelser? til (et )?veterinærlægemid\w* \(ATC-kode Q eller »Vet\.« i navnet\)")
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
MAX_ROWS = 20
SNAP = ROOT / "snapshots" / f"{C.CODE}_licenses.json.gz"
# 報告寫的「表上列了幾筆」說明句：有這種句子時程式表照原表列數（不擴到 5 列）
DISPLAY_RX = re.compile(r"\b(vises|viser|vist|listet|listes|opført|opstillet|udvalg|eksempler)\b|\btabellen\b|\bde \d+ første\b|"
                        r"\bde første \d+\b|\bovenstående\b", re.I)
RANK = {"valid": 0, "not_marketed": 1, "unknown": 2, "cancelled": 3}
LABEL = {"valid": "Gyldig", "cancelled": "Afregistreret", "unknown": "Status ukendt"}


def cls(rec):
    return rec.get("license_status") or "valid"


def label(rec):
    c = cls(rec)
    if c == "not_marketed":
        return str(rec.get("status") or "").strip() or "Godkendt, ikke markedsført"
    return LABEL.get(c, LABEL["unknown"])


def cell(x, n=80):
    t = re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()
    return t if len(t) <= n else t[:n - 1].rstrip(" ,") + "…"


def records(tf, stem):
    recs = list(tf.get("records") or [])
    have = {str(r.get("license_id") or "").strip() for r in recs}
    for k, e in (getattr(C, "EXTRA_OWN", {}).get(stem) or {}).items():  # 人工確認、事實層也算的補充號碼
        if k not in have:
            recs.append({"license_id": k, "brand_name_en": e.get("product"), "dosage_form": e.get("dosage_form"),
                         "ingredients": e.get("ingredients")})
    return recs


def table_rows(recs):
    seen, out = set(), []
    for i, r in sorted(enumerate(recs), key=lambda x: (RANK.get(cls(x[1]), 2), x[0])):
        k = str(r.get("license_id") or "").strip()
        if not k or k in seen:
            continue
        seen.add(k)
        out.append(f"| {k} | {cell(r.get('brand_name_en') or r.get('brand_name_zh'), 70) or 'Ikke angivet'} | "
                   f"{cell(r.get('dosage_form'), 60) or 'Ikke angivet'} | {cell(r.get('ingredients'), 70) or 'Ikke angivet'} | "
                   f"{label(r)} |")
    return out


def entry_of(tf, stem):
    """快照與產表共用的摘要：rows（最多 20 列）、total、partial、listed（收錄筆數）、vet（獸用許可張數）"""
    rows = table_rows(records(tf, stem))
    tm = int(tf.get("total_matches") or 0)
    partial = tm > len(tf.get("records") or [])
    vet = len({str(r.get("license_id") or "").strip() for r in tf.get("veterinary_records") or []} - {""})
    return {"rows": rows[:MAX_ROWS], "total": len(rows) if not partial else max(tm, len(rows)), "partial": partial,
            "listed": len(rows), "vet": vet}


def rows_of(tf, fc=None, stem=None):
    e = entry_of(tf, stem or "")
    return e["rows"], e["total"]


def snap_extra(tf, stem=None):
    e = entry_of(tf, stem or "")
    return {"partial": e["partial"], "listed": e["listed"], "vet": e["vet"]}


def show_line(n, total, partial, k):
    if partial:
        return SHOW_PART.format(n=n, m=k)
    if n >= total:
        return SHOW_ALL1 if total == 1 else SHOW_ALL.format(m=total)
    return SHOW_SOME.format(n=n, m=total)


def vet_line(v, none=False):
    if not v:
        return []
    if none:
        return [VET_NONE1 if v == 1 else VET_NONE.format(v=v)]
    return [VET_LINE1 if v == 1 else VET_LINE.format(v=v)]


def expected_block(entry, n):
    """程式區塊的內容（不含標記與空行）：n 列的表＋SHOW 句（＋獸用說明）；沒有任何人用紀錄時是 NONE_LINE（＋獸用說明）"""
    rows = entry.get("rows") or []
    vet = int(entry.get("vet") or 0)
    if not rows:
        return [NONE_LINE] + vet_line(vet, none=True)
    listed = entry.get("listed") or len(rows)
    n = max(1, min(n, listed, len(rows), MAX_ROWS))
    return HEAD + rows[:n] + [show_line(n, entry.get("total") or listed, bool(entry.get("partial")), listed)] + vet_line(vet)


def _with_blank(block):
    """寫進頁面的樣子：表與 SHOW 句之間、SHOW 句與獸用句之間空一行"""
    out = []
    for x in block:
        if out and not (x.startswith("|") and out[-1].startswith("|")):
            out.append("")
        out.append(x)
    return out


def strip_marks(lines):
    return [l for l in lines if l.strip() not in (BEGIN, END)]


def wrap(block):
    return [BEGIN, ""] + _with_blank(block) + ["", END]


def _bounds(lines):
    a = next((i for i, l in enumerate(lines) if SEC_RE.match(l)), None)
    if a is None:
        return None, None
    a += 1
    return a, next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))


def _review_mask(lines):
    """查核框（<!-- review:begin … review:end -->）內的行號：找表、判斷說明句時不算"""
    m, inside = set(), None
    for i, l in enumerate(lines):
        s = l.strip()
        if inside is None and s.startswith("<!-- review:begin "):
            inside = s.split()[2]
        if inside is not None:
            m.add(i)
            if s == f"<!-- review:end {inside} -->":
                inside = None
    return m


def _is_prog(l):
    s = l.strip()
    return bool(SHOW_RX.match(s)) or bool(VET_RX.match(s)) or s == NONE_LINE


def _target_rows(lines, a, b, x, y, nrows_avail, was_prog):
    r0 = max(0, (y - x + 1) - 2)
    if was_prog:  # 重排：照頁面上現有程式表的列數
        return max(1, min(MAX_ROWS, r0))
    mask = _review_mask(lines)
    disp = any(DISPLAY_RX.search(lines[k]) for k in range(a, b) if k not in mask and not lines[k].startswith("|")
               and not _is_prog(lines[k]))
    n = r0 if (disp and r0) else max(r0, min(5, nrows_avail))
    return max(1, min(MAX_ROWS, n))


# 2026-11-24 第三輪（用戶決定，比照 JpTxGNN 的 add_section）：公開頁整頁沒有市場段落、但證據包有許可證紀錄（人用或獸用）時，
# 在這些段落之前（照順序找第一個）補「## NEW_SEC」標題與程式區塊；noindex 頁不補。
NEW_SEC = "Information om det danske marked"
ADD_BEFORE = ["Sikkerhedsovervejelser", "Konklusion og næste skridt", "Gennemgangslog", "Ansvarsfraskrivelse"]


def add_section(text, entry):
    fm = text.split("---", 2)[1] if text.startswith("---") else ""
    if re.search(r"^noindex:\s*true", fm, re.M) or not (entry.get("rows") or entry.get("vet")):
        return None
    lines = text.split("\n")
    heads = {m.group(1): i for i, l in enumerate(lines) for m in [re.match(r"^## (.+?)\s*$", l)] if m}
    at = next((heads[h] for h in ADD_BEFORE if h in heads), None)
    if at is None:
        return None
    nrows = entry.get("listed") or len(entry.get("rows") or [])
    sec = ["## " + NEW_SEC, ""] + wrap(expected_block(entry, min(5, nrows) or 1)) + [""]
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(lines[:at] + sec + lines[at:]))
    return t2 if t2 != text else None


def process(text, entry):
    """回傳新內容；沒有變就回 None"""
    was_prog = BEGIN in text.split("\n")
    lines = strip_marks(text.split("\n"))
    a, b = _bounds(lines)
    if a is None:
        return add_section(text, entry)
    mask = _review_mask(lines)
    tb = [k for k in range(a, b) if lines[k].startswith("|") and k not in mask]
    nrows = entry.get("listed") or len(entry.get("rows") or [])
    if not tb:
        rest = [l for l in lines[a:b] if not _is_prog(l)]
        while rest and not rest[0].strip():
            rest.pop(0)
        out = lines[:a] + [""] + wrap(expected_block(entry, min(5, nrows) or 1)) + [""] + rest + lines[b:]
    else:
        x = y = tb[0]
        while y + 1 < b and lines[y + 1].startswith("|"):
            y += 1
        n = _target_rows(lines, a, b, x, y, nrows, was_prog)
        rest = [l for l in lines[y + 1:b] if not _is_prog(l)]
        while rest and not rest[0].strip():
            rest.pop(0)
        head = [l for i, l in enumerate(lines[:x]) if i < a or not _is_prog(l)]
        while head and not head[-1].strip():
            head.pop()
        out = head + [""] + wrap(expected_block(entry, n)) + [""] + rest + lines[b:]
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    if not t2.endswith("\n") and text.endswith("\n"):
        t2 += "\n"
    return t2 if t2 != text else None


def block_lines(text):
    lines = text.split("\n")
    if BEGIN not in lines or END not in lines:
        return None
    i, j = lines.index(BEGIN), lines.index(END)
    return [x for x in lines[i + 1:j] if x.strip()]


def carry_block(old_text, new_text):
    """sync_notes_to_docs.py 重寫整頁時用：舊頁的程式區塊移植到新頁的市場段落，取代新頁模型寫的第一張表；
    新頁段落沒有表時接在標題下。舊頁沒有程式區塊就原樣回傳新頁。"""
    old = old_text.replace("\r\n", "\n").split("\n")
    if BEGIN not in old or END not in old:
        return new_text
    blk = old[old.index(BEGIN):old.index(END) + 1]
    lines = strip_marks(new_text.split("\n"))
    a, b = _bounds(lines)
    if a is None:
        return new_text
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        out = lines[:a] + [""] + blk + [""] + lines[a:]
    else:
        x = y = tb[0]
        while y + 1 < b and lines[y + 1].startswith("|"):
            y += 1
        rest = [l for l in lines[y + 1:b] if not _is_prog(l)]
        out = lines[:x] + blk + [""] + rest + lines[b:]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


def _bundle(stem):
    for key in (stem, stem.replace("-", "_"), stem.replace("_", "-")):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return f
    return None


def _snapshot():
    if not SNAP.exists():
        raise SystemExit(f"找不到 {SNAP.relative_to(ROOT)}（跑 scripts/build_license_snapshot.py）")
    return json.loads(gzip.open(SNAP).read().decode("utf-8")).get("drugs", {})


def run(only=None, dry=False, from_snapshot=False):
    """回傳 [(頁, 欄位, 前值, 後值)]（每週排程摘要用）"""
    if from_snapshot:
        snap = _snapshot()
    elif not (ROOT / "data/bundles").is_dir() or not any((ROOT / "data/bundles").glob("*/drug_bundle.json")):
        raise SystemExit("找不到 data/bundles（先還原 data/，或用 --from-snapshot）；讀不到證據包不改頁")  # 交付前驗證：讀不到資料就停
    ch = []
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only is not None and page.stem not in only and page.stem.replace("-", "_") not in only:
            continue
        raw = page.read_bytes().decode("utf-8")
        if "layout: id_redirect" in raw[:3000] or 'http-equiv="refresh"' in raw[:3000]:
            continue
        if from_snapshot:
            entry = snap.get(page.stem)
            if not entry or "rows" not in entry:
                continue
        else:
            bf = _bundle(page.stem)
            if bf is None:
                continue
            entry = entry_of(json.loads(bf.read_text(encoding="utf-8")).get(C.BUNDLE_KEY) or {}, page.stem)
        crlf = "\r\n" in raw[:500]
        t = raw.replace("\r\n", "\n")
        new = process(t, entry)
        if new is None:
            continue
        before, after = block_lines(t), block_lines(new)
        nrow = lambda bl: len([x for x in bl or [] if x.startswith("| ") and x != HEAD[0]])  # noqa: E731
        ch.append((page.stem, "市場段落（程式許可證表）", f"{nrow(before)} 列" if before else "AI 表／無表", f"{nrow(after)} 列"))
        if not dry:
            page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return ch


def main(argv):
    only = {a for a in argv if not a.startswith("--")} or None
    ch = run(only, dry="--dry-run" in argv or "--check" in argv, from_snapshot="--from-snapshot" in argv)
    if "--check" in argv:
        print(f"程式許可證表：{'✗' if ch else '✓'} 待重排 {len(ch)} 頁")
        sys.exit(1 if ch else 0)
    print(f"程式許可證表：改 {len(ch)} 頁")


if __name__ == "__main__":
    main(sys.argv[1:])
