"""DK 依成分重建證據包的許可證紀錄（2026-11-05，用戶核准；全程不用 AI；做法比照 ZaTxGNN 的同名腳本）。

原本的許可證紀錄來自 src/dktxgnn/collectors/dkfda.py ＋ data/loader.py：loader 依「AktiveSubstanser」字串去重
（drop_duplicates(subset=["Active_Ingredients"])），同一個成分字串只留第一個產品，所以每個藥只收到一兩張
「代表品」許可，張數不對；而且那張常是獸用品（ivermectin 只收到 Bimectin Vet.，頁面就寫成人用 Markedsført）。

來源：Lægemiddelstyrelsen 已許可藥品清單 xlsx（data/raw/danish_medicines.xlsx；--download 先重新下載，網址同 license_adapter.URL）。
清單只列現行許可，沒有狀態欄：在列的許可一律視為有效（status 空白，與 license_adapter 相同）。

做法：
1. 成分對應沿用站上的 data/processed/drug_mapping.csv（原始主成分字串 → DrugBank ID，映射成功者）；
   清單裡新出現的成分字串對照不到時，逐一成分（逗號分隔）用單一成分字串的對照補。
2. 證據包的 DrugBank ID 對到的全部產品都收（不再一個成分字串只留一個）。
3. 獸用品：ATC 以 Q 開頭，或品名含「Vet.」→ 放進 thaifda.veterinary_records（不算人用許可；頁面許可證表的獸用列由
   license_table_sync.drop_excluded_rows 刪除）。只有獸用許可的藥，概覽狀態列寫「Kun godkendt som veterinærlægemiddel」
   （check_drug_page.VET_ONLY）。
4. records：人用產品，單方在前，最多 20 筆；total_matches＝人用不重複 Drugid 數（多於 20 筆時頁面寫「mindst N」）。
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


def ncomp(r):
    return len([c for c in re.split(r",\s*", r.get("ingredients") or "") if c.strip()])


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    only = [a for a in argv if not a.startswith("--") and a != rep]
    if "--download" in argv:
        download()
    prods, by_raw = load_products(), load_mapping()
    by_base = base_map(by_raw)
    in_list = {p["license_id"]: p for p in prods}
    if len(prods) < 10000:
        raise SystemExit(f"清單只有 {len(prods)} 筆，疑似格式改變，不重建")
    by_db = {}
    for p in prods:
        for db in db_ids(p["ingredients"], by_raw, by_base):
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
            continue
        seen, human, vet = set(), [], []
        for p in by_db.get(db, []):
            if p["license_id"] in seen:
                continue
            seen.add(p["license_id"])
            (vet if is_vet(p) else human).append({k: v for k, v in p.items() if not k.startswith("_")})
        new_ids = {r["license_id"] for r in human} | {r["license_id"] for r in vet}
        # 新清單查不到的舊紀錄（下架或改號）：不推定為撤銷，原紀錄照留（與 license_adapter 相同）
        for r in old:
            if r.get("license_id") not in in_list and r.get("license_id") not in new_ids:
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
