"""依複方逐成分對照補收證據包漏收的許可（2026-11-24 第三輪，用戶決定；全程不用 AI）。

問題：證據包的許可是 rebuild_licenses_by_ingredient.py 依 data/processed/drug_mapping.csv（成分字串整串 → DrugBank ID）收的。
複方的整串寫法一換（Rosufenx「FENOFIBRAT, Rosuvastatin calcium」→ 清單現在寫「FENOFIBRAT, Rosuvastatincalcium」）就對不到，
逐成分時「fenofibrat」沒有單方對照（丹麥的 fenofibrate 全是複方），結果只對到 rosuvastatin；有些複方整串本來就只對到一個成分
（「CLINDAMYCINPHOSPHAT, Tretinoin」只對到 tretinoin）。所以複方只收進其中一個成分的證據包。

做法：照 rebuild_licenses_by_ingredient.db_ids_components（原對照＋複方逐成分對照）重算每個產品的 DrugBank ID；
比原規則（db_ids）多對到的 ID、證據包裡還沒有的許可，就補進該 ID 的證據包：
- 人用 → records（不超過原收集器的 20 筆上限；超過的只記在 records_not_stored 並算進 total_matches）；
- 獸用（ATC Q 開頭或品名含 Vet.，或人工清單 veterinary）→ veterinary_records；
- 人工清單（scripts/license_manual_overrides.json）exclude／exclude_atc 的不收；excluded_records 裡的不收。
每筆記 source（清單與日期、補收規則）與 added（補收日）。只加不刪、可重複執行（已收的、已記在 records_not_stored 的不重收）。
清單只列現行許可，沒有狀態欄：補進來的一律視為有效（status 空白，與重建、license_adapter 相同）。

2026-11-24 第四輪（用戶決定）：每週排程原本只補「新規則比原規則多對到」的複方，11-05 依成分重建之後才核准、原規則也對得到的單方許可
（例 olanzapine 6 張 2026-1x 核准的學名藥）不會進證據包，張數落後。改成照 rebuild_licenses_by_ingredient 的同一套規則（db_ids_components：
原對照＋複方逐成分對照，不放寬）重算本藥對到的全部產品，證據包還沒有的都補（原規則對得到的 source 寫「matched by ingredient」，
只有逐成分對照才對得到的照舊寫「combination product matched per ingredient」）。
要知道證據包「已經算進 total_matches、但因 20 筆上限沒存」的是哪幾張：11-05 重建時沒記號碼（records_not_stored 是 11-24 才加的），
所以 total_matches 大於 records＋records_not_stored 的證據包（隱藏筆數 gap）不能直接補，否則會重複計數：
- --baseline-xlsx <11-05 重建用的清單>：一次性回填 records_not_stored＝照同一規則在那份清單對到、證據包裡沒有的人用許可；
  只在對到的張數正好等於 gap 時回填，不等就不動、列進報告（2026-11-24 回填 145 個證據包，全部相等）。
- 回填後仍有 gap 的證據包整個不補、列進報告（停損，不推定）。

用法（repo 根目錄）：python3 scripts/add_component_licenses.py [--download] [--xlsx 檔] [--baseline-xlsx 檔] [--dry-run] [--report out.tsv]
每週排程（.github/workflows/license-refresh.yml）在 license_refresh 前以 --download 跑。
"""
import datetime
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import rebuild_licenses_by_ingredient as R  # noqa: E402

MIN_PRODUCTS = 10000


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    if "--xlsx" in argv:
        R.XLSX = Path(argv[argv.index("--xlsx") + 1])
    if "--download" in argv:
        R.download()
    today = datetime.date.today().isoformat()
    xdate = datetime.date.fromtimestamp(R.XLSX.stat().st_mtime).isoformat()
    prods, by_raw = R.load_products(), R.load_mapping()
    if len(prods) < MIN_PRODUCTS:
        raise SystemExit(f"清單只有 {len(prods)} 筆，疑似格式改變，不補收")
    by_base, comp = R.base_map(by_raw), R.component_map()
    overrides = {k: v for k, v in json.loads(R.OVERRIDES.read_text(encoding="utf-8")).items() if not k.startswith("_")} if R.OVERRIDES.exists() else {}
    extra, orig = {}, {}  # DrugBank ID → 照重建規則對到的產品；(ID, Drugid) → 原規則（db_ids）也對得到
    for p in prods:
        o = set(R.db_ids(p["ingredients"], by_raw, by_base))
        for db in R.db_ids_components(p["ingredients"], by_raw, by_base, comp):
            extra.setdefault(db, []).append(p)
            orig[(db, p["license_id"])] = db in o
    base = None
    if "--baseline-xlsx" in argv:  # 一次性回填 records_not_stored（見檔頭）
        keep_x = R.XLSX
        R.XLSX = Path(argv[argv.index("--baseline-xlsx") + 1])
        base = {}
        for p in R.load_products():
            for db in R.db_ids_components(p["ingredients"], by_raw, by_base, comp):
                base.setdefault(db, []).append(p)
        R.XLSX = keep_x
    rows, nb, nrec, nfill, gaps = [], 0, 0, 0, []
    src_c = f"Lægemiddelstyrelsen godkendte lægemidler ({xdate}; combination product matched per ingredient, 2026-11-24 rule)"
    src_o = f"Lægemiddelstyrelsen godkendte lægemidler ({xdate}; matched by ingredient, same rule as the 2026-11-05 rebuild)"
    for f in sorted(R.BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        try:
            b = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            raise SystemExit(f"讀不到證據包 {f}：{e}")  # 讀不到資料就停，不當成沒有紀錄
        db = str((b.get("drug") or {}).get("drugbank_id") or "").upper()
        if not db or db not in extra:
            continue
        reg = b.get("thaifda") or {}
        if not reg:
            continue
        ov = overrides.get(page) or {}

        def mine(p):
            return not (p["license_id"] in ov.get("exclude", []) or any(p["_atc"].upper().startswith(a) for a in ov.get("exclude_atc", [])))

        def human(p):
            return not (R.is_vet(p) or p["license_id"] in ov.get("veterinary", []))
        have = {str(r.get("license_id") or "") for k in ("records", "veterinary_records", "excluded_records") for r in (reg.get(k) or [])}
        have |= {str(x) for x in reg.get("records_not_stored") or []}
        recs, vet = list(reg.get("records") or []), list(reg.get("veterinary_records") or [])
        not_stored = list(reg.get("records_not_stored") or [])
        total = int(reg.get("total_matches") or len(recs))
        gap = total - len(recs) - len(not_stored)
        filled = False
        if gap > 0 and base is not None:
            hid, seen = [], set()
            for p in sorted(base.get(db, []), key=lambda x: x["license_id"]):
                if p["license_id"] in have or p["license_id"] in seen or not mine(p) or not human(p):
                    continue
                seen.add(p["license_id"])
                hid.append(p["license_id"])
            if len(hid) == gap:
                not_stored += hid
                have |= set(hid)
                gap, filled = 0, True
                nfill += 1
                rows.append(f"{page}\t-\t({len(hid)} hidden IDs)\tbackfill_not_stored\t")
        if gap > 0:
            gaps.append(page)
            rows.append(f"{page}\t-\t(total_matches 比已知號碼多 {gap} 張)\tskipped_gap\t")
            continue
        added = []
        for p in sorted(extra[db], key=lambda x: (R.ncomp(x) > 1, x["brand_name_zh"])):
            lid = p["license_id"]
            if lid in have or not mine(p):
                continue
            have.add(lid)
            rec = {k: v for k, v in p.items() if not k.startswith("_")}
            rec.update(source=src_o if orig.get((db, lid)) else src_c, added=today)
            if not human(p):
                vet.append(rec)
                where = "veterinary"
            else:
                total += 1
                if len(recs) < R.CAP:
                    recs.append(rec)
                    where = "records"
                else:
                    not_stored.append(lid)
                    where = "not_stored"
            added.append(lid)
            rows.append(f"{page}\t{lid}\t{p['brand_name_zh']}\t{where}\t{p['ingredients']}")
        if not added and not filled:
            continue
        nb += bool(added)
        nrec += len(added)
        nreg = dict(reg, records=recs, veterinary_records=vet, total_matches=total, found=bool(recs))
        if not_stored:
            nreg["records_not_stored"] = not_stored
        if not dry:
            b["thaifda"] = nreg
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\tlicense_id\tproduct\twhere\tingredients\n" + "\n".join(rows) + "\n", encoding="utf-8")
    if base is not None:
        print(f"回填 records_not_stored：{nfill} 個證據包")
    if gaps:
        print(f"⚠ 已算進總數卻不知道號碼、這次不補的證據包 {len(gaps)} 個：{', '.join(gaps[:20])}")
    print(f"{'（試跑）' if dry else ''}依成分補收：{nb} 個證據包、{nrec} 筆（成分對照 {len(comp)} 個）")


if __name__ == "__main__":
    main(sys.argv[1:])
