"""DK（Lægemiddelstyrelsen 已許可藥品清單）下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：https://laegemiddelstyrelsen.dk/LinkArchive.ashx?id=0BD4960F0D7744E3BABC951431681ECC&lang=en（每日更新的 xlsx，免金鑰；沿用站上 download_danish_data.py）。
清單只列現行許可（godkendte）的藥品、沒有狀態欄：在列不改紀錄（證據包 status 原本空白，reviewer 視為有效），
新清單查不到的 Drugid 保留原狀態、列在 summary（不推定為撤銷）。證據包（thaifda 區塊）license_id＝Drugid（11 碼）。
"""
import io
import time

import openpyxl
import requests

RAW_FILE = "raw/dkma_drugids.json"
URL = "https://laegemiddelstyrelsen.dk/LinkArchive.ashx?id=0BD4960F0D7744E3BABC951431681ECC&lang=en"


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
    return out


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
