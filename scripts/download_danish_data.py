#!/usr/bin/env python3
"""Download Danish Medicines Agency drug data.

Downloads the official list of authorised medicinal products from
Lægemiddelstyrelsen (Danish Medicines Agency).
"""

import requests
from pathlib import Path

# Official download URL for authorised medicinal products
# Updated daily at https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/
EXCEL_URL = "https://laegemiddelstyrelsen.dk/LinkArchive.ashx?id=0BD4960F0D7744E3BABC951431681ECC&lang=en"


def download_danish_medicines():
    """Download Danish medicines list Excel file."""
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; DkTxGNN/1.0)"
    }

    print("Downloading Danish Medicines Agency data...")
    print(f"URL: {EXCEL_URL}")

    resp = requests.get(EXCEL_URL, headers=headers, timeout=60)
    resp.raise_for_status()

    # Save to data/raw
    output_path = Path(__file__).parent.parent / "data" / "raw" / "danish_medicines.xlsx"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "wb") as f:
        f.write(resp.content)

    print(f"Saved to: {output_path}")
    print(f"File size: {len(resp.content) / 1024:.1f} KB")

    return output_path


if __name__ == "__main__":
    download_danish_medicines()
