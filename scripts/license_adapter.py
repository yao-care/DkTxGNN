"""DK（Lægemiddelstyrelsen 已許可藥品清單）下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：https://laegemiddelstyrelsen.dk/LinkArchive.ashx?id=0BD4960F0D7744E3BABC951431681ECC&lang=en（每日更新的 xlsx，免金鑰；沿用站上 download_danish_data.py）。
清單只列現行許可（godkendte）的藥品、沒有狀態欄：在列不改紀錄（證據包 status 原本空白，reviewer 視為有效），
新清單查不到的 Drugid 保留原狀態、列在 summary（不推定為撤銷）。證據包（thaifda 區塊）license_id＝Drugid（11 碼）。

2026-11-17（用戶要求確認查不到的許可證）：另下載 Lægemiddelstyrelsen「Afregistrerede lægemidler」（已撤銷許可清單，
xls，兩個工作表：上個月、過去一年，欄位 DrugId／AfRegDato）。現行清單沒有、而且在撤銷清單上的 Drugid＝官方確認已撤銷，
preprocess 標 license_status＝cancelled、dkma_not_listed（第一次發現日）與 dkma_afreg_dato（撤銷清單的撤銷日）；
撤銷超過一年、已不在撤銷清單的號，只收在 EMA_CONFIRMED（集中許可，EMA medicines output 為 Withdrawn／Lapsed，每筆附依據）。
EMA 暫停（Suspended）的集中許可收在 EMA_SUSPENDED（每筆附依據）：暫停不是撤銷，標 license_status＝not_marketed
（事實層「核准但未上市」，不算有效、也不算撤銷），status 改「Suspenderet (EMA)」（原值存 status_before_ema_suspended），也標 dkma_not_listed。
現行清單沒有、但 EMA 仍 Authorised 的號（Omidria 28105324513，2015-07-28 許可、未在 EU 上市）不判定，照舊列為查不到。
標過的號之後又出現在現行清單就取消標記；現行清單少於 MIN_CURRENT 或撤銷清單下載失敗時不做新的判定（已標的維持）。
"""
import io
import json
import time
from pathlib import Path

import openpyxl
import requests

RAW_FILE = "raw/dkma_drugids.json"
URL = "https://laegemiddelstyrelsen.dk/LinkArchive.ashx?id=0BD4960F0D7744E3BABC951431681ECC&lang=en"
AFREG_URL = "https://laegemiddelstyrelsen.dk/LinkArchive.ashx?id=E2B34167E69C41B1BD6C30FC7C218DE5&lang=da"
CURRENT: set = set()   # fetch() 填：現行清單的 Drugid；空的就不做新判定
AFREG: dict = {}       # fetch() 填：撤銷清單的 Drugid → 撤銷日（YYYY-MM-DD）；下載失敗＝空、不做新判定
MARKED: set = set()    # fetch() 填：證據包裡已標 dkma_not_listed 的 Drugid（撤銷清單只留一年，標過的靠這個延續）
MIN_CURRENT = 10000
# 撤銷超過一年（不在撤銷清單）的集中許可：EMA medicines output（2026-11-17 下載）的狀態與日期
EMA_CONFIRMED = {
    "28103228501": "PegIntron EMEA/H/C/000280: EMA Withdrawn 2021-04-21",
    "28104194907": "Ariclaim EMEA/H/C/000552: EMA Withdrawn 2018-07-09",
    "28104528909": "Ribavirin BioPartners EMEA/H/C/001184: EMA Lapsed 2013-04-09",
    "28106295319": "Nyxthracis (previously Obiltoxaximab SFL) EMEA/H/C/005169: EMA Withdrawn",
}
# 現行清單沒有、EMA 集中許可為暫停（Suspended）的號：EMA medicines output（2026-11-17 下載）的狀態；暫停期間不得上市，但不是撤銷
EMA_SUSPENDED = {
    "28106561320": "Oxbryta EMEA/H/C/004869: EMA Suspended (medicines output 2026-11-17; EPAR: currently suspended from use in the EU; "
                   "EMA recommended suspension 2024-09-26)",
}
SUSPENDED_STATUS = "Suspenderet (EMA)"


def fetch():
    for attempt in range(4):
        try:
            r = requests.get(URL, timeout=300, headers={"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"})
            r.raise_for_status()
            if r.content[:2] != b"PK":
                raise RuntimeError("回傳的不是 xlsx")
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))
    ws = openpyxl.load_workbook(io.BytesIO(r.content), read_only=True).active
    ws.reset_dimensions()
    rows = ws.iter_rows(values_only=True)
    head = [str(x or "").strip() for x in next(rows)]
    if "Drugid" not in head:
        raise RuntimeError(f"欄位改變：{head}")
    out = []
    for row in rows:
        v = dict(zip(head, row)).get("Drugid")
        if v not in (None, ""):
            out.append({"drugid": str(int(float(v))) if str(v).replace(".", "", 1).isdigit() else str(v).strip()})
    CURRENT.clear()
    if len(out) >= MIN_CURRENT:
        CURRENT.update(r["drugid"] for r in out)
    AFREG.clear()
    AFREG.update(_fetch_afreg())
    MARKED.clear()
    for f in (Path(__file__).resolve().parents[1] / "data/bundles").glob("*/drug_bundle.json"):
        try:
            b = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        for r in _recs(b):
            if r.get("dkma_not_listed"):
                MARKED.add(record_id(r))
    return out


def _fetch_afreg():
    """撤銷清單（xls）；失敗回空 dict（不做新判定）"""
    try:
        import xlrd
        for attempt in range(3):
            try:
                r = requests.get(AFREG_URL, timeout=180, headers={"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"})
                r.raise_for_status()
                break
            except Exception:
                if attempt == 2:
                    raise
                time.sleep(10 * (attempt + 1))
        wb = xlrd.open_workbook(file_contents=r.content)
        out = {}
        for sh in wb.sheets():
            head = [str(x).strip() for x in sh.row_values(0)] if sh.nrows else []
            if "DrugId" not in head or "AfRegDato" not in head:
                raise RuntimeError(f"撤銷清單欄位改變：{sh.name} {head}")
            i, j = head.index("DrugId"), head.index("AfRegDato")
            for n in range(1, sh.nrows):
                row = sh.row_values(n)
                k = str(row[i]).strip().split(".")[0]
                if not k.isdigit():
                    continue
                d = row[j]
                d = xlrd.xldate_as_datetime(d, wb.datemode).strftime("%Y-%m-%d") if isinstance(d, float) else str(d).strip()
                out[k] = max(out.get(k, ""), d)
        if len(out) < 100:
            raise RuntimeError(f"撤銷清單只有 {len(out)} 筆")
        return out
    except Exception as e:
        print(f"Afregistrerede lægemidler 下載或解析失敗，不做新的已撤銷判定：{e}")
        return {}


def _recs(bundle):
    t = bundle.get("thaifda") or {}
    return (t.get("records") or []) + (t.get("veterinary_records") or [])


def confirmed_absent(lid):
    """給 license_refresh：現行清單沒有，且撤銷清單／EMA_CONFIRMED／先前已標＝官方確認已撤銷"""
    lid = str(lid).strip()
    if not CURRENT or lid in CURRENT:
        return False
    return lid in AFREG or lid in EMA_CONFIRMED or lid in EMA_SUSPENDED or lid in MARKED


def preprocess(bundle):
    """官方確認已撤銷的 Drugid 標 cancelled（dkma_not_listed＝第一次發現日）；又出現在現行清單的取消標記。有改回 True"""
    if not CURRENT:
        return False
    today = time.strftime("%Y-%m-%d")
    ch = False
    for r in _recs(bundle):
        lid = record_id(r)
        if not lid:
            continue
        if lid in CURRENT:
            if r.get("dkma_not_listed"):
                if "status_before_ema_suspended" in r:
                    r["status"] = r.pop("status_before_ema_suspended")
                for k in ("dkma_not_listed", "license_status", "dkma_afreg_dato", "ema_confirmed", "ema_suspended"):
                    r.pop(k, None)
                ch = True
        elif not r.get("dkma_not_listed") and lid in EMA_SUSPENDED and lid not in AFREG:
            r["dkma_not_listed"] = today
            r["license_status"] = "not_marketed"
            r["ema_suspended"] = EMA_SUSPENDED[lid]
            r["status_before_ema_suspended"] = r.get("status", "")
            r["status"] = SUSPENDED_STATUS
            ch = True
        elif not r.get("dkma_not_listed") and (lid in AFREG or lid in EMA_CONFIRMED):
            r["dkma_not_listed"] = today
            r["license_status"] = "cancelled"
            if lid in AFREG:
                r["dkma_afreg_dato"] = AFREG[lid]
            else:
                r["ema_confirmed"] = EMA_CONFIRMED[lid]
            ch = True
    return ch


def validate(new, old):
    p = []
    if len(new) < 5000:
        p.append(f"只解析出 {len(new)} 筆，疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    return {r["drugid"]: "listed" for r in new}


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    return False  # 在列不改紀錄；只用來確認仍在列，查不到的列在 summary


# 2026-11-24（用戶決定）：市場段落的許可證表改由程式產生（scripts/sync_license_tables.py）。每週排程（母目錄
# license_refresh_20261029.py 的 sync_tables 掛鉤）對狀態有變的證據包重排程式表；3b 自我檢查另允許改的非表格行＝PAGE_NOTE
# （表下程式說明句、獸用說明句、NONE_LINE、程式區塊標記）。
PAGE_NOTE = (r"^(Tabellen viser (den eneste|alle \d+|\d+ af (mindst )?\d+) markedsføringstilladelser? til (et )?human[et]? lægemid.*|"
             r"Dataene indeholder (desuden )?\d+ tilladelser? til (et )?veterinærlægemid.*|"
             r"Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler indeholder ingen markedsføringstilladelser.*|"
             r"<!-- licenses:(begin|end) -->)$")


def sync_tables(site_root, bundles):
    """狀態有變的藥：市場段落的程式許可證表依證據包重排（Gyldig 在前），狀態照事實層分類；SHOW 句跟著改
    （規則見 scripts/sync_license_tables.py）。回傳 [(頁, 欄位, 前值, 後值)]"""
    import importlib.util
    p = Path(site_root) / "scripts/sync_license_tables.py"
    s = importlib.util.spec_from_file_location("dk_sync_license_tables", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    if not bundles:
        return []
    return m.run(only=set(bundles))

