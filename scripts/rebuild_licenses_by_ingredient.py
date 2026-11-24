"""DK 依成分重建證據包的許可證紀錄（2026-11-05，用戶核准；全程不用 AI；做法比照 ZaTxGNN 的同名腳本）。

原本的許可證紀錄來自 src/dktxgnn/collectors/dkfda.py ＋ data/loader.py：loader 依「AktiveSubstanser」字串去重
（drop_duplicates(subset=["Active_Ingredients"])），同一個成分字串只留第一個產品，所以每個藥只收到一兩張
「代表品」許可，張數不對；而且那張常是獸用品（ivermectin 只收到 Bimectin Vet.，頁面就寫成人用 Markedsført）。

來源：Lægemiddelstyrelsen 已許可藥品清單 xlsx（data/raw/danish_medicines.xlsx；--download 先重新下載，網址同 license_adapter.URL）。
清單只列現行許可，沒有狀態欄：在列的許可一律視為有效（status 空白，與 license_adapter 相同）。

做法：
1. 成分對應沿用站上的 data/processed/drug_mapping.csv（原始主成分字串 → DrugBank ID，映射成功者）；
   清單裡新出現的成分字串對照不到時，逐一成分（逗號分隔）用單一成分字串的對照補。
   2026-11-24 起複方另外逐成分查（db_ids_components：單方對照＋從複方對照列推得的成分對照 component_map），
   整串寫法換了（Rosufenx）或整串只對到一個成分的複方也收進每個成分的證據包；超過 20 筆的 Drugid 記在 records_not_stored。
   每週排程不跑這支，跑 scripts/add_component_licenses.py（只加不刪）。
2. 證據包的 DrugBank ID 對到的全部產品都收（不再一個成分字串只留一個）。
3. 獸用品：ATC 以 Q 開頭，或品名含「Vet.」→ 放進 thaifda.veterinary_records（不算人用許可；頁面許可證表的獸用列由
   license_table_sync.drop_excluded_rows 刪除）。只有獸用許可的藥，概覽狀態列寫「Kun godkendt som veterinærlægemiddel」
   （check_drug_page.VET_ONLY）。
4. records：人用產品，單方在前，最多 20 筆；total_matches＝人用不重複 Drugid 數（多於 20 筆時頁面寫「mindst N」）。
4b. 人工清單 scripts/license_manual_overrides.json（2026-11-05 用戶決定，每筆附依據）：exclude_atc／exclude 的產品不算本藥，
   veterinary 的產品判為獸用（gallium 排除 V09 放射性診斷藥；phenylbutazone 的 Butagran Equi 判為獸用）。
5. 新清單查不到的舊紀錄照留（不推定為撤銷，與 license_adapter 相同）。停損：原本收錄、仍在清單上的人用許可有一半以上
   不在新結果裡 → 對應可能有誤，不改、列進報告。
用法（repo 根目錄）：python3 scripts/rebuild_licenses_by_ingredient.py [--download] [--dry-run] [--report out.tsv] [頁 ...]
"""
import csv
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "data/bundles"
XLSX = ROOT / "data/raw/danish_medicines.xlsx"
MAPPING = ROOT / "data/processed/drug_mapping.csv"
OVERRIDES = ROOT / "scripts/license_manual_overrides.json"
CAP = 20


def download():
    import requests
    sys.path.insert(0, str(ROOT / "scripts"))
    import license_adapter
    for attempt in range(4):
        try:
            r = requests.get(license_adapter.URL, timeout=300, headers={"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"})
            r.raise_for_status()
            if r.content[:2] != b"PK":
                raise RuntimeError("回傳的不是 xlsx")
            XLSX.write_bytes(r.content)
            return
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))


def load_products():
    import openpyxl
    ws = openpyxl.load_workbook(XLSX, read_only=True).active
    ws.reset_dimensions()
    rows = ws.iter_rows(values_only=True)
    head = [str(x or "").strip() for x in next(rows)]
    if not {"Drugid", "Navn", "AktiveSubstanser", "ATC-kode"} <= set(head):
        raise RuntimeError(f"欄位改變：{head}")
    out = []
    for row in rows:
        d = dict(zip(head, row))
        v = d.get("Drugid")
        if v in (None, ""):
            continue
        k = str(int(float(v))) if str(v).replace(".", "", 1).isdigit() else str(v).strip()
        g = lambda c: "" if d.get(c) is None else str(d.get(c)).strip()  # noqa: E731
        out.append({"license_id": k, "brand_name_zh": g("Navn"), "brand_name_en": g("Navn"), "ingredients": g("AktiveSubstanser"),
                    "indication": "", "dosage_form": g("Lægemiddelform"), "manufacturer": g("MftIndehaver"),
                    "license_holder": g("MftIndehaver"), "approval_date": "", "expiry_date": "", "status": "",
                    "_atc": g("ATC-kode")})
    return out


def is_vet(p):
    return p["_atc"].upper().startswith("Q") or bool(re.search(r"\bVet\.", p["brand_name_zh"]))


def load_mapping():
    by_raw = {}
    with open(MAPPING, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            if str(r.get("映射成功")).strip().lower() != "true" or not r.get("drugbank_id"):
                continue
            by_raw.setdefault(r["原始主成分"].strip().lower(), set()).add(r["drugbank_id"].strip().upper())
    return by_raw


# 丹麥文鹽類／水合物字尾（黏在成分名後面：Alfentanilhydrochloridhydrat、BISOPROLOLFUMARAT）
DK_SALT = re.compile(r"(hydrochlorid|dihydrochlorid|hydrobromid|hydrogen\w*|hydrat|monohydrat|dihydrat|trihydrat|sesquihydrat|hemihydrat|"
                     r"fumarat|maleat|mesilat|mesylat|besilat|tartrat|citrat|succinat|acetat|propionat|valerat|sulfat|nitrat|phosphat|fosfat|"
                     r"natrium|kalium|calcium|magnesium|bromid|chlorid|tosilat|lactat|gluconat|embonat|pamoat|stearat|oleat|"
                     r"dinatrium|meglumin|arginin|lysin|olamin|erbumin|tert-butylamin|trometamol|kaliumsalt|natriumsalt|vandfri|\s)+$")


def dk_base(c):
    c = re.sub(r"\([^)]*\)", " ", c.strip().lower())
    c = " ".join(c.split())
    b = DK_SALT.sub("", c).strip(" -")
    return b if len(b) >= 4 else c


def db_ids(ing, by_raw, by_base=None):
    k = ing.strip().lower()
    if k in by_raw:
        return by_raw[k]
    ids = set()
    for c in re.split(r",\s*", k):
        got = by_raw.get(c.strip(), set())
        if not got and by_base is not None:
            got = by_base.get(dk_base(c), set())  # 新出現的寫法：去掉鹽類字尾後跟單一成分的對照比
        ids |= got
    return ids


def base_map(by_raw):
    out = {}
    for k, v in by_raw.items():
        if "," not in k:
            out.setdefault(dk_base(k), set()).update(v)
    return {k: v for k, v in out.items() if len(v) == 1}  # 同一個主體對到多個 DrugBank ID 的不用


# ---- 複方逐成分對照（2026-11-24 第三輪，用戶決定）----
# drug_mapping.csv 是依當時清單的成分字串整串對照；複方有兩個問題：
#   1. 清單裡成分字串的寫法換了（Rosufenx「FENOFIBRAT, Rosuvastatin calcium」→「…Rosuvastatincalcium」），整串對不到，
#      逐成分時「fenofibrat」又沒有單方對照（丹麥的 fenofibrate 全是複方），只對到 rosuvastatin；
#   2. 有些複方整串只對到其中一個成分（「CLINDAMYCINPHOSPHAT, Tretinoin」只對到 tretinoin）。
# 所以複方另外逐成分查：成分名去鹽類字尾後，先查單方對照（base_map），再查從複方對照列推得的成分對照（component_map）。
# component_map：drug_mapping 每一列複方（原始主成分有兩個以上成分）＋一個 DrugBank ID，
# 這個 ID 的名稱（標準化成分（不含逗號時）或 DrugBank 詞彙名）跟複方裡恰好一個成分相近（一方是另一方開頭，或 SequenceMatcher ≥ 0.85），
# 就把那個成分（去鹽類字尾）記成這個 ID；同一個成分對到多個 ID 的不用。

def _letters(s):
    return re.sub(r"[^a-z]", "", str(s or "").lower())


def _close(a, b):
    import difflib
    a, b = _letters(a), _letters(b)
    if len(a) < 5 or len(b) < 5:
        return False
    if a.startswith(b) or b.startswith(a):
        return True
    return difflib.SequenceMatcher(None, a, b).ratio() >= 0.85


def _substances(ing):
    sys.path.insert(0, str(ROOT / "src"))
    from dktxgnn.regulatory.ingredients import substances
    return substances(ing)


def component_map():
    vocab = {}
    vf = ROOT / "data/external/drugbank_vocab.csv"
    if vf.exists():
        with open(vf, encoding="utf-8", newline="") as f:
            vocab = {r["drugbank_id"].strip().upper(): r["drug_name"] for r in csv.DictReader(f)}
    out = {}
    with open(MAPPING, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            if str(r.get("映射成功")).strip().lower() != "true" or not r.get("drugbank_id"):
                continue
            comps = _substances(r["原始主成分"])
            if len(comps) < 2:
                continue
            db = r["drugbank_id"].strip().upper()
            names = [n for n in ((r.get("標準化成分") or "") if "," not in (r.get("標準化成分") or "") else "", vocab.get(db, "")) if n]
            hit = [c for c in comps if any(_close(dk_base(c), n) for n in names)]
            if len(hit) == 1:
                out.setdefault(dk_base(hit[0]), set()).add(db)
    return {k: v for k, v in out.items() if len(v) == 1}


def db_ids_components(ing, by_raw, by_base, comp):
    """db_ids 加上複方逐成分對照（單方照舊）"""
    ids = set(db_ids(ing, by_raw, by_base))
    parts = _substances(ing)
    if len(parts) < 2:  # 單方：原對照對不到時才用複方推得的成分對照（Peyona「Caffeincitrat」、Cayston「AZTREONAMLYSIN」）
        return ids or set(comp.get(dk_base(parts[0]), set()) if parts else set())
    for c in parts:
        k = dk_base(c)
        ids |= by_raw.get(c.strip().lower()) or by_base.get(k) or comp.get(k) or set()
    return ids


def ncomp(r):
    return len([c for c in re.split(r",\s*", r.get("ingredients") or "") if c.strip()])


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    only = [a for a in argv if not a.startswith("--") and a != rep]
    if "--download" in argv:
        download()
    prods, by_raw = load_products(), load_mapping()
    overrides = {k: v for k, v in json.loads(OVERRIDES.read_text(encoding="utf-8")).items() if not k.startswith("_")} if OVERRIDES.exists() else {}
    by_base = base_map(by_raw)
    comp = component_map()
    in_list = {p["license_id"]: p for p in prods}
    if len(prods) < 10000:
        raise SystemExit(f"清單只有 {len(prods)} 筆，疑似格式改變，不重建")
    by_db = {}
    for p in prods:
        for db in db_ids_components(p["ingredients"], by_raw, by_base, comp):
            by_db.setdefault(db, []).append(p)
    rows, held, changed = [], [], 0
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        if only and page not in only:
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        db = str((b.get("drug") or {}).get("drugbank_id") or "").upper()
        reg = b.get("thaifda") or {}
        old = reg.get("records") or []
        if not db:
            ov = overrides.get(page)
            if not ov or not old:
                continue
            # 證據包沒有 DrugBank ID（gallium）：不重建，只對原紀錄套人工清單
            def drop(r):
                q = in_list.get(r.get("license_id")) or {}
                return r.get("license_id") in ov.get("exclude", []) or any(str(q.get("_atc") or "").upper().startswith(a) for a in ov.get("exclude_atc", []))
            keep = [r for r in old if not drop(r)]
            if len(keep) == len(old):
                continue
            nreg = dict(reg, found=bool(keep), records=keep, total_matches=len(keep),
                        excluded_records=[r for r in old if drop(r)], excluded_reason=ov.get("reason", ""))
            rows.append(f"{page}\t{len(old)}\t{len(keep)}\t0\tmanual_exclude")
            changed += 1
            if not dry:
                b["thaifda"] = nreg
                f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
            continue
        seen, human, vet = set(), [], []
        ov = overrides.get(page) or {}
        for p in by_db.get(db, []):
            if p["license_id"] in seen:
                continue
            seen.add(p["license_id"])
            if p["license_id"] in ov.get("exclude", []) or any(p["_atc"].upper().startswith(a) for a in ov.get("exclude_atc", [])):
                continue  # 人工清單：不是本藥
            (vet if is_vet(p) or p["license_id"] in ov.get("veterinary", []) else human).append({k: v for k, v in p.items() if not k.startswith("_")})
        new_ids = {r["license_id"] for r in human} | {r["license_id"] for r in vet}
        # 新清單查不到的舊紀錄（下架或改號）：不推定為撤銷，原紀錄照留（與 license_adapter 相同）
        for r in old:
            if r.get("license_id") not in in_list and r.get("license_id") not in new_ids and r.get("license_id") not in ov.get("exclude", []):
                (vet if re.search(r"\bVet\.", r.get("brand_name_zh") or "") else human).append(r)
                new_ids.add(r.get("license_id"))
        lost = [r.get("license_id") for r in old if r.get("license_id") in in_list and not is_vet(in_list[r["license_id"]])
                and r.get("license_id") not in new_ids]
        if lost and len(lost) * 2 > len([r for r in old if r.get("license_id") in in_list]):
            held.append(f"{page}\t原有、仍在清單上的人用許可 {len(lost)} 張不在新結果：{','.join(lost[:5])}")
            continue
        human.sort(key=lambda r: (ncomp(r) > 1, r["brand_name_zh"]))
        vet.sort(key=lambda r: r["brand_name_zh"])
        nreg = dict(reg, found=bool(human), records=human[:CAP], total_matches=len(human), veterinary_records=vet,
                    records_not_stored=[r["license_id"] for r in human[CAP:]],
                    source="Lægemiddelstyrelsen godkendte lægemidler (all products by ingredient, 2026-11-05 rebuild)")
        if nreg == reg:
            continue
        rows.append(f"{page}\t{len(old)}\t{len(human)}\t{len(vet)}\t{'vet_only' if vet and not human else ''}")
        changed += 1
        if not dry:
            b["thaifda"] = nreg
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\told_records\thuman\tveterinary\tnote\n" + "\n".join(rows) + "\n", encoding="utf-8")
        Path(rep).with_suffix(".held.tsv").write_text("\n".join(held) + "\n", encoding="utf-8")
    vo = sum(1 for r in rows if r.endswith("vet_only"))
    print(f"重建 {changed} 個證據包（只有獸用許可 {vo} 個；停損擋下 {len(held)} 個）")


if __name__ == "__main__":
    main(sys.argv[1:])
